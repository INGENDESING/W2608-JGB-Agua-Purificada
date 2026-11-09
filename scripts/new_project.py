"""Bootstrap de un proyecto JAGDESING a partir de la plantilla MASTER.

Uso:
    python scripts/new_project.py P2601 "Bavaria" "Rediseño línea CIP tanque T-101"

Clona la plantilla a ``../P2601-BAV-REDISENO_CIP/``, reemplaza códigos en LaTeX/YAML
y pre-pobla ``bases_diseno.yaml`` y ``contexto.md`` con los metadatos.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

PLANTILLA = Path(__file__).resolve().parents[1]
EXCLUDE = {".venv", "__pycache__", ".pytest_cache", ".ruff_cache", ".claude"}
EXCLUDE_EXT = (".aux", ".log", ".out", ".toc", ".lof", ".lot", ".spl",
               ".pdf", ".fdb_latexmk", ".fls", ".synctex.gz")
# Carpetas de la bóveda de memoria cuyo contenido NO se hereda (solo estructura)
MEMORIA_RESET = ("sesiones", "decisiones", "lecciones")


def _copy_tree(src: Path, dst: Path) -> None:
    def _ignore(d: str, names: list[str]) -> list[str]:
        ignored = [n for n in names if n in EXCLUDE or n.endswith(EXCLUDE_EXT)]
        # 06_entregables: heredar solo listado_documentos.csv y REV0/; no arrastrar
        # revisiones ni borradores de la master.
        if Path(d).name == "06_entregables":
            ignored += [n for n in names
                        if n not in (".gitkeep", "listado_documentos.csv", "REV0")
                        and n not in ignored]
        # Vaciar notas de memoria de la plantilla master: el proyecto nuevo arranca limpio
        if Path(d).parent.name == "memoria" and Path(d).name in MEMORIA_RESET:
            ignored += [n for n in names if n != ".gitkeep" and n not in ignored]
        # Vaciar investigaciones de la master: solo se hereda la plantilla guía
        if Path(d).name == "investigaciones":
            ignored += [n for n in names
                        if n not in (".gitkeep", "plantilla_investigacion.md") and n not in ignored]
        return ignored

    shutil.copytree(src, dst, ignore=_ignore)


def _slug(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9\s]+", "", s).strip()
    return re.sub(r"\s+", "_", s).upper()[:30]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("codigo", help="Código JAGDESING (ej. P2601)")
    ap.add_argument("cliente", help="Cliente (ej. Bavaria)")
    ap.add_argument("proyecto", help="Nombre del proyecto")
    ap.add_argument("--dest", type=Path, default=None, help="Carpeta destino (debe ser externa al MASTER)")
    ap.add_argument("--in-place", action="store_true", help="Inicializar in-place en la carpeta actual (cuando ya se copio y pego la plantilla)")
    args = ap.parse_args()

    if args.in_place:
        dest = Path.cwd()
        if dest.resolve() == PLANTILLA.parent.resolve() or dest.resolve() == PLANTILLA.resolve():
            print("ERROR: Prohibido inicializar in-place dentro del repositorio MASTER o de la Plantilla.", file=sys.stderr)
            return 1
    else:
        if not args.dest:
            print("ERROR: Debe especificar --dest hacia la carpeta del cliente en OneDrive, o usar --in-place.", file=sys.stderr)
            return 1
        if args.dest.resolve() == PLANTILLA.parent.resolve() or args.dest.resolve() == PLANTILLA.resolve():
            print("ERROR: Prohibido generar proyectos dentro del repositorio MASTER o de la Plantilla.", file=sys.stderr)
            return 1
        slug = f"{args.codigo}-{_slug(args.cliente)[:3]}-{_slug(args.proyecto)}"
        dest = args.dest / slug
        if dest.exists():
            print(f"ERROR: {dest} ya existe.", file=sys.stderr)
            return 1
        _copy_tree(PLANTILLA, dest)

    if args.in_place:
        for p in MEMORIA_RESET:
            target_dir = dest / "memoria" / p
            if target_dir.exists():
                for f in target_dir.iterdir():
                    if f.name != ".gitkeep":
                        if f.is_dir():
                            shutil.rmtree(f)
                        else:
                            f.unlink()

    # Reemplazos clave
    yaml_path = dest / "00_bases_diseno" / "bases_diseno.yaml"
    txt = yaml_path.read_text(encoding="utf-8")
    txt = txt.replace('codigo: "P25XX"', f'codigo: "{args.codigo}"')
    txt = txt.replace('nombre: "PLANTILLA MASTER"', f'nombre: "{args.proyecto}"')
    txt = txt.replace('cliente: "CLIENTE"', f'cliente: "{args.cliente}"')
    txt = txt.replace('fecha_emision: "AAAA-MM-DD"', f'fecha_emision: "{date.today().isoformat()}"')
    yaml_path.write_text(txt, encoding="utf-8")

    # Reemplazos en metadatos LaTeX (config/datos_proyecto.tex)
    tex_path = dest / "02_informe_tex" / "config" / "datos_proyecto.tex"
    tex = tex_path.read_text(encoding="utf-8")
    tex = tex.replace(r"\newcommand{\projecttitle}{DISEÑO/DIAGNOSTICO}",
                      rf"\newcommand{{\projecttitle}}{{{args.proyecto.upper()}}}")
    tex = tex.replace(r"\newcommand{\documentcode}{P25XX-PR-XXX-00X}",
                      rf"\newcommand{{\documentcode}}{{{args.codigo}-PR-XXX-00X}}")
    tex = tex.replace(r"\newcommand{\targetcompany}{P25XX}",
                      rf"\newcommand{{\targetcompany}}{{{args.codigo}}}")
    tex = tex.replace(r"\newcommand{\docFechaLarga}{MES DIA 202X}",
                      rf"\newcommand{{\docFechaLarga}}{{{date.today().isoformat()}}}")
    tex_path.write_text(tex, encoding="utf-8")

    # Renombrar el maestro LaTeX al código del proyecto (convención guía de codificación del proyecto)
    master_old = dest / "02_informe_tex" / "P25XX-PR-INF-00X REVX.tex"
    master_new = dest / "02_informe_tex" / f"{args.codigo}-PR-INF-001 Rev0.tex"
    if master_old.exists():
        master_old.rename(master_new)

    # Sincronizar el membrete con el código y el maestro del proyecto
    membrete_path = dest / "02_informe_tex" / "config" / "membrete_config.yaml"
    mb = membrete_path.read_text(encoding="utf-8")
    mb = mb.replace("P25XX-PR-INF-00X REVX.tex", master_new.name)
    mb = mb.replace("P25XX", args.codigo)
    membrete_path.write_text(mb, encoding="utf-8")

    # contexto.md inicial
    ctx = dest / "contexto.md"
    ctx.write_text(
        f"""# Contexto del proyecto: {args.codigo} — {args.proyecto}

## Estado actual
- Cliente: {args.cliente}
- Última tarea completada: Bootstrap de plantilla.
- Próxima tarea pendiente: Completar `00_bases_diseno/bases_diseno.yaml`.
- Fecha de última actualización: {date.today().isoformat()}

## Bases de diseño congeladas
- Código de proyecto JAGDESING (congelado): {args.codigo}  — formato `WyyxxEETTTNNN`, ver `08_codificacion/codificacion.md`.
- Resto pendiente — ver `00_bases_diseno/bases_diseno.yaml`.

## Decisiones de diseño clave
(Por documentar)

## Archivos clave
- `00_bases_diseno/bases_diseno.yaml` — fuente única de propiedades y condiciones.
- `01_calculos/memorias/` — memorias ejecutables.
- `02_informe_tex/` — informe técnico LaTeX.
- `03_dashboards_html/` — dashboards interactivos.
- `08_codificacion/codificacion.md` — nomenclatura y codificación de entregables (norma guía de codificación del proyecto).
- `06_entregables/listado_documentos.csv` — Listado de Documentos del Proyecto.

## Preguntas abiertas
- [ ] (pendiente)

## Comandos útiles
- `uv sync` — instalar dependencias Python.
- `uv run pytest` — ejecutar tests.
- `uv run 03_dashboards_html/build_dashboard.py` — regenerar dashboard.
- `python 08_codificacion/validar_codigo.py {args.codigo}-PR-INF-001` — validar un código de documento.

## Memoria Obsidian
- Inicio de sesión: escribir `inicio.md` y ejecutar su protocolo token-eficiente.
- `memoria/00_MOC.md` — nodo central del cerebro del proyecto (grafo interconectado).
- `memoria/plantillas/` — formatos de nota (sesión, decisión, lección).
- Skill: `skills/memoria-obsidian/SKILL.md` (o `.agents/skills/memoria-obsidian/SKILL.md`).
""",
        encoding="utf-8",
    )

    print(f"Proyecto creado en: {dest}")

    # Activación del Cerebro Obsidian del nuevo proyecto:
    fecha_hoy = date.today().isoformat()
    nota_arranque = dest / "memoria" / "sesiones" / f"{fecha_hoy}_arranque.md"
    nota_arranque.parent.mkdir(parents=True, exist_ok=True)
    nota_arranque.write_text(
        f"""---
tipo: sesion
fecha: {fecha_hoy}
proyecto: {args.codigo}
tags: [sesion, arranque, inicializacion]
---

# Sesión {fecha_hoy} — Inicialización y arranque del proyecto

## Qué se hizo
1. Inicialización del proyecto {args.codigo} ({args.proyecto}) para {args.cliente}.
2. Estampado de bases de diseño, metadatos LaTeX y registro de entregables guía de codificación del proyecto.
3. Activación del cerebro de memoria Obsidian con MOC interconectado.

## Qué quedó pendiente
- Diligenciar `00_bases_diseno/bases_diseno.yaml` con parámetros y normas de proceso.
- Congelar bases de diseño en `contexto.md`.

## Decisiones tomadas
- Proyecto regido bajo norma de codificación guía de codificación del proyecto y filosofía SST ISO 45001.

## Archivos modificados
- `00_bases_diseno/bases_diseno.yaml` — bases de diseño iniciales.
- `02_informe_tex/config/datos_proyecto.tex` — metadatos LaTeX.
- `memoria/00_MOC.md` — cerebro del proyecto activado.
- `contexto.md` — estado de arranque.
""",
        encoding="utf-8",
    )

    (dest / "memoria" / "00_MOC.md").write_text(
        f"""# 🧠 Cerebro del Proyecto: {args.codigo} — {args.proyecto}

> **Mapa de Contenido (MOC) Central**. Bóveda de conocimiento interconectada para el proyecto.
> Compatible con Antigravity (agy), Gemini CLI, OpenAI Codex, Claude Code y cualquier IA.
> Protocolo operativo: `skills/memoria-obsidian/SKILL.md` | Protocolo de arranque token-eficiente: `inicio.md`.

**Cliente:** {args.cliente} | **Código congelado:** `{args.codigo}`
**Última sesión:** [[{fecha_hoy}_arranque]] — Inicialización del proyecto

---

## 📌 1. Gobernanza y Entregables del Proyecto
- [[../00_bases_diseno/bases_diseno.yaml|Bases de Diseño congeladas (fuente única de verdad)]]
- [[../06_entregables/listado_documentos.csv|Listado Oficial de Documentos y Revisiones (guía de codificación del proyecto)]]
- [[../08_codificacion/codificacion.md|Norma de Codificación JAGDESING]]
- [[../CalidadProyectos/Aplicacion45001.md|Gestión SST e ISO 45001:2018 (Peligros y Jerarquía de Controles)]]
- [[../contexto.md|Estado Vigente del Proyecto (Contexto del Asistente)]]

## 🔬 2. Ingeniería, Cálculos e Informes
- [[../01_calculos/|Módulos de cálculo y memorias ejecutables]]
- [[../02_informe_tex/|Informe Técnico Principal en LaTeX]]
- [[../03_dashboards_html/|Dashboards offline de ingeniería]]
- [[../04_planos_svg/|Planos, diagramas PFD / P&ID]]
- [[../05_memorias_excel/|Memorias de cálculo vivas en Excel]]

## 🗓️ 3. Bitácora de Sesiones
- [[{fecha_hoy}_arranque]] — Inicialización del proyecto y configuración del cerebro Obsidian.

## 🎯 4. Registro de Decisiones de Diseño (ADR)
> Registra cada decisión técnica (material, correlación, norma, criterio de diseño) en `decisiones/D-NNN_titulo.md`.
- (sin decisiones adicionales aún)

## 💡 5. Lecciones Aprendidas y Solución de Errores
> Registra cada fallo técnico resuelto o límite normativo en `lecciones/L-NNN_titulo.md`.
- (sin lecciones registradas aún)

## 🌐 6. Bóveda Global
- Bóveda global JAGDESING: ver `config.yaml` (`boveda_global`)
""",
        encoding="utf-8",
    )
    (dest / "task" / "todo.md").write_text(
        """# Plan: (sin plan vigente)

> Escribe aquí el plan de la tarea actual según `AGENTS.md` → `<fase_1_analisis>`.
> Los planes cerrados se archivan en `task/todo_historico.md`.
""",
        encoding="utf-8",
    )
    historico = dest / "task" / "todo_historico.md"
    if historico.exists():
        historico.write_text(
            "# Histórico de planes cerrados\n\n(sin planes archivados)\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
