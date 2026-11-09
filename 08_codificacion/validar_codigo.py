"""Validador de documentos del proyecto: convencion W compacta del proyecto.

Fuente operativa: ``08_codificacion/codificacion.md`` e instrucciones del usuario. Sin dependencias externas (stdlib pura).

Formato del codigo de documento::

    WyyxxEETTTNNN

    Wyyxx  W + 2 digitos del anio + 2 digitos del consecutivo de la Orden de Proyecto
    EE     especialidad, 2 letras (Tabla A)
    TTT    tipo de documento, 1-3 letras (Tabla B)
    NNN    consecutivo, 3 digitos numericos con ceros a la izquierda, por serie

Uso::

    python 08_codificacion/validar_codigo.py W2644PRESP015
    python 08_codificacion/validar_codigo.py W2644MEINF001 --anio 2026
    python 08_codificacion/validar_codigo.py --listado 06_entregables/listado_documentos.csv

Exit 0 si el codigo cumple forma y siglas de tabla; exit 1 con mensaje si no.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

# --- Tablas de guía de codificación del proyecto (ver codificacion.md, seccion 5) ---------------------------------

ESPECIALIDADES: dict[str, str] = {
    "DI": "Direccion",
    "PR": "Proceso",
    "CI": "Civil",
    "ME": "Mecanica",
    "ES": "Estructura",
    "TU": "Tuberia",
    "EL": "Electrica",
    "IC": "Instrumentacion y control",
    "SC": "Contraincendios",
    "HV": "Aire Acondicionado",
}

# tipo -> (descripcion, sub-carpeta guía de codificación del proyecto)
TIPOS: dict[str, tuple[str, str]] = {
    "ACT": ("Actas", "ADMINISTRATIVOS"),
    "TR": ("Correspondencia", "ADMINISTRATIVOS"),
    "CRO": ("Cronograma", "ADMINISTRATIVOS"),
    "ORG": ("Organigrama", "ADMINISTRATIVOS"),
    "PRE": ("Presentacion", "ADMINISTRATIVOS"),
    "INF": ("Informe", "INFORMES"),
    "DTS": ("Hoja de datos de equipo o instrumento", "HOJAS DE DATOS"),
    "RFQ": ("Requerimiento de Cotizacion", "DOCUMENTOS TECNICOS"),
    "DOC": ("Documento tecnico", "DOCUMENTOS TECNICOS"),
    "ESP": ("Especificacion", "ESPECIFICACIONES"),
    "CAL": ("Memoria de calculo", "MEMORIAS DE CALCULO"),
    "M3D": ("Modelo 3D", "MEMORIAS DE CALCULO"),
    "PCL": ("Nube de puntos", "MEMORIAS DE CALCULO"),
    "ISO": ("Isometrico", "PLANOS"),
    "PLN": ("Plano, LayOut, PFD, PID", "PLANOS"),
    "LIS": ("Listado", "LISTADOS"),
    "APU": ("Analisis de precios unitarios", "PRESUPUESTO"),
    "PTO": ("Presupuesto", "PRESUPUESTO"),
    "VO": ("Volumen de obra", "PRESUPUESTO"),
}

# Siglas toleradas fuera de tabla: la norma las usa en un ejemplo. Se aceptan con aviso.
# valor -> (nota, sub-carpeta guía de codificación del proyecto equivalente)
TIPOS_TOLERADOS: dict[str, tuple[str, str]] = {
    "LAY": ("LayOut (guía de codificación del proyecto lo ejemplifica; use PLN salvo exigencia del cliente)", "PLANOS"),
}

_RE_CODIGO = re.compile(r"^W(\d{2})(\d{2})([A-Z]{2})([A-Z][A-Z0-9]{0,2})(\d{3})$")
_RE_FECHA = re.compile(r"^(\d{2})/(\d{2})/(\d{4})$")
_RE_FIRMA = re.compile(r"^(?:[A-ZÁÉÍÓÚÑ]\.){1,3}[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑ'-]+$")


class CodigoInvalido(ValueError):
    """El codigo no cumple la forma WyyxxEETTTNNN."""


def parse_codigo(codigo: str) -> dict:
    """Descompone un codigo de documento. Lanza CodigoInvalido si la forma no cumple."""
    m = _RE_CODIGO.match(codigo.strip())
    if not m:
        raise CodigoInvalido(
            f"'{codigo}' no cumple la forma WyyxxEETTTNNN "
            "(W + 2 digitos anio + 2 digitos proyecto + 2 letras especialidad + 1..3 caracteres tipo + 3 digitos; sin separadores)."
        )
    yy, xx, esp, tipo, consec = m.groups()
    if tipo in TIPOS:
        tipo_nombre, sub_carpeta = TIPOS[tipo]
    elif tipo in TIPOS_TOLERADOS:
        tipo_nombre, sub_carpeta = TIPOS_TOLERADOS[tipo]
    else:
        tipo_nombre, sub_carpeta = "(fuera de tabla)", ""
    return {
        "codigo": codigo.strip(),
        "anio": 2000 + int(yy),
        "yy": yy,
        "consecutivo_proyecto": int(xx),
        "proyecto": f"W{yy}{xx}",
        "especialidad": esp,
        "especialidad_nombre": ESPECIALIDADES.get(esp, "(fuera de tabla)"),
        "tipo": tipo,
        "tipo_nombre": tipo_nombre,
        "consecutivo": int(consec),
        "consecutivo_str": consec,
        "sub_carpeta": sub_carpeta,
    }


def validar(codigo: str, *, anio_esperado: int | None = None) -> list[tuple[str, str]]:
    """Valida forma + siglas de tabla.

    Devuelve una lista de ``(nivel, mensaje)`` con ``nivel`` en ``{"error", "aviso"}``.
    Lista vacia = conforme sin observaciones. Un ``"error"`` implica no conformidad
    (exit 1 en CLI); un ``"aviso"`` es tolerado (exit 0, se informa por stderr).
    Lanza CodigoInvalido si la forma del codigo es incorrecta.
    """
    info = parse_codigo(codigo)
    obs: list[tuple[str, str]] = []

    if info["especialidad"] not in ESPECIALIDADES:
        obs.append(("error",
                    f"especialidad '{info['especialidad']}' no esta en la Tabla A de guía de codificación del proyecto."))
    if info["tipo"] not in TIPOS:
        if info["tipo"] in TIPOS_TOLERADOS:
            obs.append(("aviso", f"tipo '{info['tipo']}': {TIPOS_TOLERADOS[info['tipo']][0]}."))
        else:
            obs.append(("error",
                        f"tipo '{info['tipo']}' no esta en la Tabla B de guía de codificación del proyecto."))
    if info["consecutivo"] == 0:
        obs.append(("aviso", "consecutivo 000: la numeracion por serie empieza en 001."))
    if anio_esperado is not None and info["anio"] != anio_esperado:
        obs.append(("error",
                    f"anio del codigo ({info['anio']}) != anio esperado ({anio_esperado})."))
    return obs


def es_conforme(codigo: str, *, anio_esperado: int | None = None) -> bool:
    """True si la forma es valida y no hay observaciones de nivel 'error'."""
    try:
        obs = validar(codigo, anio_esperado=anio_esperado)
    except CodigoInvalido:
        return False
    return not any(nivel == "error" for nivel, _ in obs)


def _slug(texto: str) -> str:
    nfkd = unicodedata.normalize("NFKD", texto)
    ascii_txt = nfkd.encode("ascii", "ignore").decode("ascii")
    ascii_txt = re.sub(r"[^A-Za-z0-9\s-]+", "", ascii_txt).strip().lower()
    return re.sub(r"[\s_]+", "-", ascii_txt)[:40].strip("-")


def sugerir_nombre_archivo(codigo: str, rev: int | str, titulo: str) -> str:
    """Devuelve 'WyyxxEETTTNNN_Rev<n>_titulo-breve' (sin extension)."""
    parse_codigo(codigo)  # valida la forma
    return f"{codigo.strip()}_Rev{rev}_{_slug(titulo)}"


_COLUMNAS_LISTADO = (
    "codigo", "revision", "fecha", "especialidad", "tipo",
    "titulo", "elaboro", "aprobo", "archivo", "estado",
)


def revisar_listado(path_csv: str | Path) -> list[str]:
    """Valida un Listado de Documentos del Proyecto. Devuelve lista de problemas (vacia = OK)."""
    path = Path(path_csv)
    problemas: list[str] = []
    if not path.is_file():
        return [f"no existe el archivo: {path}"]

    with path.open(encoding="utf-8-sig", newline="") as fh:
        lector = csv.DictReader(fh)
        faltan = [c for c in _COLUMNAS_LISTADO if c not in (lector.fieldnames or [])]
        if faltan:
            problemas.append(f"faltan columnas en el encabezado: {', '.join(faltan)}")
            return problemas

        vistos: dict[str, int] = {}
        for i, fila in enumerate(lector, start=2):  # fila 1 = encabezado
            codigo = (fila.get("codigo") or "").strip()
            if not codigo:
                problemas.append(f"fila {i}: 'codigo' vacio.")
                continue
            try:
                info = parse_codigo(codigo)
            except CodigoInvalido as exc:
                problemas.append(f"fila {i}: {exc}")
                continue

            for nivel, msg in validar(codigo):
                if nivel == "error":
                    problemas.append(f"fila {i} [{codigo}]: {msg}")

            clave = f"{codigo}#Rev{(fila.get('revision') or '').strip()}"
            if clave in vistos:
                problemas.append(
                    f"fila {i}: duplicado de {clave} (ya en fila {vistos[clave]})."
                )
            vistos[clave] = i

            fecha = (fila.get("fecha") or "").strip()
            mf = _RE_FECHA.match(fecha)
            if not mf:
                problemas.append(f"fila {i} [{codigo}]: fecha '{fecha}' no es dd/mm/aaaa.")
            else:
                dd, mm, _ = (int(x) for x in mf.groups())
                if not (1 <= dd <= 31 and 1 <= mm <= 12):
                    problemas.append(f"fila {i} [{codigo}]: fecha '{fecha}' fuera de rango.")

            esp_col = (fila.get("especialidad") or "").strip().upper()
            if esp_col and esp_col != info["especialidad"]:
                problemas.append(
                    f"fila {i} [{codigo}]: columna especialidad '{esp_col}' "
                    f"!= codigo '{info['especialidad']}'."
                )
            tipo_col = (fila.get("tipo") or "").strip().upper()
            if tipo_col and tipo_col != info["tipo"]:
                problemas.append(
                    f"fila {i} [{codigo}]: columna tipo '{tipo_col}' "
                    f"!= codigo '{info['tipo']}'."
                )

            for campo in ("elaboro", "aprobo"):
                val = (fila.get(campo) or "").strip()
                if val and not _RE_FIRMA.match(val):
                    problemas.append(
                        f"fila {i} [{codigo}]: {campo} '{val}' no cumple "
                        "'X.Y.APELLIDO' en mayusculas."
                    )
    return problemas


def _imprimir_desglose(info: dict) -> None:
    print(f"  codigo........... {info['codigo']}")
    print(f"  proyecto......... {info['proyecto']}  (anio {info['anio']}, "
          f"consecutivo {info['consecutivo_proyecto']})")
    print(f"  especialidad..... {info['especialidad']}  {info['especialidad_nombre']}")
    print(f"  tipo............. {info['tipo']}  {info['tipo_nombre']}")
    print(f"  consecutivo...... {info['consecutivo_str']}")
    print(f"  sub-carpeta...... {info['sub_carpeta'] or '(sin asignar)'}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("codigo", nargs="?", help="Codigo de documento, ej. W2644PRESP015")
    ap.add_argument("--anio", type=int, default=None, help="Anio esperado del proyecto (ej. 2026)")
    ap.add_argument("--listado", type=Path, default=None,
                    help="Ruta a un Listado de Documentos del Proyecto (CSV) a validar")
    args = ap.parse_args(argv)

    if args.listado is not None:
        problemas = revisar_listado(args.listado)
        if problemas:
            print(f"LISTADO CON PROBLEMAS ({len(problemas)}):", file=sys.stderr)
            for p in problemas:
                print(f"  - {p}", file=sys.stderr)
            return 1
        print(f"Listado OK: {args.listado}")
        return 0

    if not args.codigo:
        ap.error("indica un codigo o usa --listado")

    try:
        info = parse_codigo(args.codigo)
    except CodigoInvalido as exc:
        print(f"CODIGO INVALIDO: {exc}", file=sys.stderr)
        return 1

    obs = validar(args.codigo, anio_esperado=args.anio)
    print("Desglose:")
    _imprimir_desglose(info)

    errores = [m for n, m in obs if n == "error"]
    avisos = [m for n, m in obs if n == "aviso"]
    if avisos:
        print(f"\nAVISOS ({len(avisos)}):", file=sys.stderr)
        for a in avisos:
            print(f"  - {a}", file=sys.stderr)
    if errores:
        print(f"\nERRORES ({len(errores)}):", file=sys.stderr)
        for e in errores:
            print(f"  - {e}", file=sys.stderr)
        print("\nNO CONFORME con la convencion W compacta del proyecto.", file=sys.stderr)
        return 1
    print("\nOK: forma y siglas conformes a la convencion W compacta del proyecto"
          + (" (con avisos)." if avisos else "."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
