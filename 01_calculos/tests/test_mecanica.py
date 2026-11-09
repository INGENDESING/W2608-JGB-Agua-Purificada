"""Verificación de src/mecanica.py contra cálculo manual (ASME VIII Div.1).

Caso base genérico: P = 1.0 MPa(g), R = 600 mm, D = 1200 mm, S = 138 MPa, E = 1.0.

Cálculo manual:
- Casco UG-27(c)(1):  t = 1.0×600/(138×1.0 − 0.6×1.0) = 600/137.4 = 4.3668 mm
- Cabezal UG-32(e), M = 1.77:  t = 1.0×1200×1.77/(2×138×1.0 − 0.2×1.0)
                                 = 2124/275.8 = 7.7012 mm
"""
from __future__ import annotations

import pytest

from src import mecanica


def test_casco_cilindrico_caso_base():
    t = mecanica.espesor_casco_cilindrico(1.0, 600.0, 138.0, 1.0)
    assert t == pytest.approx(600.0 / 137.4, rel=1e-6)


def test_casco_fuera_de_dominio_ug27():
    # P >= 0.385·S·E debe rechazarse (dominio de UG-27(c)(1))
    with pytest.raises(ValueError):
        mecanica.espesor_casco_cilindrico(60.0, 600.0, 138.0, 1.0)


def test_cabeza_toriesferica_fd_caso_base():
    t = mecanica.espesor_cabeza_toriesferica(1.0, 1200.0, 138.0, 1.0, M=1.77)
    assert t == pytest.approx(2124.0 / 275.8, rel=1e-6)


def test_factor_m_korbogen_vs_fd():
    # Korbogen (M = 1.54, r = 0.1·D) requiere menos espesor que F&D (M = 1.77)
    t_kor = mecanica.espesor_cabeza_toriesferica(1.0, 1200.0, 138.0, 1.0, M=1.54)
    t_fd = mecanica.espesor_cabeza_toriesferica(1.0, 1200.0, 138.0, 1.0, M=1.77)
    assert t_kor < t_fd
