"""Memoria de cálculo MC-002 — Curva de Moody (ejemplo de pipeline Python → pgfplots).

Genera el factor de fricción de Darcy en función de Re para varias rugosidades
relativas usando la correlación de Churchill (1977), válida en todo régimen, y
exporta el resultado a ``02_informe_tex/assets/moody_churchill.csv`` para que la
figura del informe (``sections/09_resultados.tex``) lo grafique con pgfplots.

Solo usa la librería estándar + ``src/hidraulica``: no añade dependencias.

Ejecutar:
    uv run 01_calculos/memorias/MC-002_grafica_moody.py
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "01_calculos"))

from src import hidraulica  # noqa: E402

CSV_OUT = ROOT / "02_informe_tex" / "assets" / "moody_churchill.csv"
RUGOSIDADES = [0.0, 1e-4, 4e-4, 1e-3]  # ε/D: lisa, acero nuevo, acero comercial, CI usada
N_PUNTOS = 60


def main() -> None:
    # Barrido logarítmico Re = 1e3 .. 1e8 (laminar → turbulento pleno)
    res = [10 ** (3 + 5 * i / (N_PUNTOS - 1)) for i in range(N_PUNTOS)]
    series = {eps_D: [hidraulica.factor_friccion_churchill(Re, eps_D) for Re in res]
              for eps_D in RUGOSIDADES}

    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Re"] + [f"f_eps{eps_D:g}" for eps_D in RUGOSIDADES])
        for i, Re in enumerate(res):
            w.writerow([f"{Re:.6e}"] + [f"{series[e][i]:.6e}" for e in RUGOSIDADES])

    # Chequeo dimensional/sanidad: f laminar tiende a 64/Re (Darcy)
    Re_lam, f_lam = res[0], series[0.0][0]
    err = abs(f_lam - 64.0 / Re_lam) / (64.0 / Re_lam)
    print(f"CSV generado   : {CSV_OUT}")
    print(f"Puntos/serie   : {N_PUNTOS} (Re {res[0]:.0e} – {res[-1]:.0e})")
    print(f"Chequeo laminar: f={f_lam:.5f} vs 64/Re={64.0/Re_lam:.5f} (err {err:.2%})")
    assert err < 0.02, "Churchill fuera del límite laminar de Darcy"
    assert all(math.isfinite(v) and v > 0 for s in series.values() for v in s)


if __name__ == "__main__":
    main()
