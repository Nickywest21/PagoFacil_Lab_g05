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
