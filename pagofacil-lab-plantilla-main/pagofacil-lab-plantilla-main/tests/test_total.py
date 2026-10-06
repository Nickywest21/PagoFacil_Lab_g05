"""Pruebas de integración: calcular_total() usa calcular_comision().

Ejecutar:  python -m pytest -v
"""
import pytest

from pagofacil.comision import calcular_total


def test_total_sin_comision():
    assert calcular_total(50) == 50


@pytest.mark.parametrize("monto, esperado", [(200, 203.0), (500, 507.5)])
def test_total_incluye_la_comision(monto, esperado):
    assert calcular_total(monto) == esperado
