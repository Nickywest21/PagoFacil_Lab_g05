"""MINI DUELO - Parte 2 del laboratorio.

Escribe aquí tus pruebas. El docente las ejecutará contra versiones del código
con defectos escondidos ("mutantes") y contará cuántos logran detectar.

REGLAS
  1. Solo puedes importar de `pytest` y de `pagofacil.comision`.
  2. TODAS tus pruebas deben PASAR con el código correcto (el que cumple
     ESPECIFICACION.md). Si una falla con el código correcto, no puntúas.
  3. Diseña desde la especificación (caja negra): particiones y valores límite.
  4. Evita montos cuyo resultado caiga justo en medio centavo (redondeo ambiguo).


  5. Trabaja SOLO en este archivo durante el duelo.
"""
import pytest
from pagofacil.comision import calcular_comision, calcular_total


@pytest.mark.parametrize("monto, esperado", [
    (0.01, 0.0),       # VL: menor monto válido -> Tramo 1
    (50, 0.0),         # PE: Tramo 1
    (100, 0.0),        # VL: frontera Tramo 1 (incluye Q100)
    (100.01, 1.5),     # VL: límite inferior Tramo 2 (1.50015 -> 1.50)
    (200, 3.0),        # PE: Tramo 2 limpio
    (500, 7.5),        # PE: Tramo 2
    (1000, 15.0),      # VL: frontera Tramo 2 (incluye Q1,000)
    (1000.01, 10.0),   # VL: límite inferior Tramo 3
    (1500, 15.0),      # PE: Tramo 3 sin llegar al tope
    (1999.99, 20.0),   # Redondeo: 19.9999 -> 20.00
    (2400, 24.0),      # PE: Tramo 3 cercano al tope
    (2500, 25.0),      # VL: comisión exactamente Q25.00
    (2510, 25.0),      # VL: supera tope
    (10000, 25.0),     # PE: tope aplicado
])
def test_comision_por_tramos(monto, esperado):
    assert calcular_comision(monto) == esperado


@pytest.mark.parametrize("monto, esperado", [
    (50, 50.0),        # Tramo 1: total sin comisión
    (100, 100.0),      # Límite Tramo 1
    (200, 203.0),      # Tramo 2 (200 + 3.00)
    (1500, 1515.0),    # Tramo 3 (1500 + 15.00)
    (5000, 5025.0),    # Tope (5000 + 25.00)
])
def test_total_por_tramos(monto, esperado):
    assert calcular_total(monto) == esperado


@pytest.mark.parametrize("monto", ["100", None, True, False, [], {}])
def test_tipo_invalido(monto):
    # Mutante bonus: True/False no son números válidos -> TypeError
    with pytest.raises(TypeError):
        calcular_comision(monto)
    with pytest.raises(TypeError):
        calcular_total(monto)


@pytest.mark.parametrize("monto", [0, 0.0, -0.01, -100])
def test_monto_no_positivo(monto):
    with pytest.raises(ValueError):
        calcular_comision(monto)
    with pytest.raises(ValueError):
        calcular_total(monto)