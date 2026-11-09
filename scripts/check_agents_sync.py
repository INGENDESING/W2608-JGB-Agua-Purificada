"""Verifica que las dos copias de AGENTS.md (raíz del MASTER y Plantilla/) sean idénticas.

La política del proyecto exige que ambas copias sean byte-idénticas (ver nota de sesión
2026-09-25). Este script convierte ese control manual (diff) en un chequeo ejecutable.

Uso:
    python scripts/check_agents_sync.py          # exit 0 si son idénticas, 1 si difieren
    python scripts/check_agents_sync.py --fix    # copia Plantilla/AGENTS.md -> raíz
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # .../MASTER PROYECTOS GENERALES INGENIERIA
RAIZ = ROOT / "AGENTS.md"
COPIA = ROOT / "Plantilla" / "AGENTS.md"


def main() -> int:
    fix = "--fix" in sys.argv
    if not RAIZ.exists() or not COPIA.exists():
        print(f"ERROR: falta {RAIZ} o {COPIA}", file=sys.stderr)
        return 1

    a, b = RAIZ.read_bytes(), COPIA.read_bytes()
    if a == b:
        print("OK: AGENTS.md raíz y Plantilla/ son byte-idénticos.")
        return 0

    print("ERROR: AGENTS.md raíz y Plantilla/ difieren.", file=sys.stderr)
    if fix:
        RAIZ.write_bytes(b)
        print("Corregido: raíz actualizada desde Plantilla/AGENTS.md (la plantilla es la fuente).")
        return 0
    print("Ejecuta con --fix para copiar Plantilla/AGENTS.md -> raíz.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
