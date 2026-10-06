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

from pagofacil.comision import calcular_comision, calcular_total, validar_monto  # noqa: F401


def test_ejemplo_monto_bajo():  # ejemplo que ya pasa; puedes borrarlo o conservarlo
    assert calcular_comision(50) == 0


# --- Tus pruebas empiezan aquí ---
# Técnicas: partición de equivalencia (PE) y valores límite (VL).


@pytest.mark.parametrize("monto, esperado", [
    (0.01, 0.0),       # VL: menor monto válido -> Tramo 1
    (100, 0.0),        # VL: frontera Tramo 1 (incluye Q100)
    (100.01, 1.5),     # VL: primer valor del Tramo 2 (1.50015 -> 1.50)
    (500, 7.5),        # PE: representativo Tramo 2
    (1000, 15.0),      # VL: frontera Tramo 2 (incluye Q1,000, sigue en 1.5 %)
    (1000.01, 10.0),   # VL: primer valor del Tramo 3 (10.0001 -> 10.00)
    (1999.99, 20.0),   # Redondeo: 19.9999 -> 20.00 (truncar daría 19.99)
    (2400, 24.0),      # PE: Tramo 3 sin llegar al tope
    (2500, 25.0),      # VL: comisión exactamente igual al tope
    (2510, 25.0),      # VL: primer valor que supera el tope
    (100000, 25.0),    # PE: monto muy grande, tope
])
def test_comision_por_tramos(monto, esperado):
    assert calcular_comision(monto) == esperado


@pytest.mark.parametrize("monto, esperado", [
    (100, 100.0),      # Tramo 1: total sin comisión
    (100.01, 101.51),  # Tramo 2 en el límite
    (200, 203.0),      # Tramo 2
    (5000, 5025.0),    # Tope
])
def test_total(monto, esperado):
    assert calcular_total(monto) == esperado


@pytest.mark.parametrize("monto", ["100", None, True, False])
def test_tipo_invalido(monto):
    # True/False: la especificación los declara "no número" -> TypeError,
    # aunque en Python bool sea subclase de int.
    with pytest.raises(TypeError):
        calcular_comision(monto)


@pytest.mark.parametrize("monto", [0, 0.0, -0.01, -100])
def test_monto_no_positivo(monto):
    with pytest.raises(ValueError):
        calcular_comision(monto)