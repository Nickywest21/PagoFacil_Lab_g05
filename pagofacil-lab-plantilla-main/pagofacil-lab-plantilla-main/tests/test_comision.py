"""Pruebas unitarias de comision.py (suite visible del equipo de QA).

Ejecutar:  python -m pytest -v
"""
import pytest

from pagofacil.comision import calcular_comision


def test_monto_bajo_no_paga_comision():
    assert calcular_comision(50) == 0


def test_monto_exacto_100_no_paga_comision():
    assert calcular_comision(100) == 0


@pytest.mark.parametrize("monto, esperado", [(200, 3.0), (500, 7.5)])
def test_tarifa_intermedia(monto, esperado):
    assert calcular_comision(monto) == esperado


@pytest.mark.parametrize("monto", [3000, 10000, 1_000_000])
def test_tope_maximo_de_q25(monto):
    assert calcular_comision(monto) == 25


def test_monto_negativo_es_invalido():
    with pytest.raises(ValueError):
        calcular_comision(-5)
