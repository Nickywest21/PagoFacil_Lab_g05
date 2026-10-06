"""Comisiones de transferencias de PagoFácil GT. Montos en quetzales (Q).

Reglas (ver ESPECIFICACION.md):
  * Hasta Q100 (inclusive): sin comisión.
  * Más de Q100 y hasta Q1,000 (inclusive): 1.5 %.
  * Más de Q1,000: 1 %.
  * La comisión nunca supera Q25.
  * La comisión se redondea a 2 decimales.
"""

LIMITE_SIN_COMISION = 100
LIMITE_TARIFA_INTERMEDIA = 1000
TASA_INTERMEDIA = 0.015
TASA_REDUCIDA = 0.01
TOPE_COMISION = 25


def validar_monto(monto):
    """Devuelve el monto como float. TypeError si no es número; ValueError si es <= 0."""
    if isinstance(monto, bool) or not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número")
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    return float(monto)


def calcular_comision(monto):
    """Comisión (en Q, con 2 decimales) que paga el cliente por transferir `monto`."""
    monto = validar_monto(monto)
    if monto < LIMITE_SIN_COMISION:
        comision = 0.0
    elif monto <= LIMITE_TARIFA_INTERMEDIA:
        comision = monto * TASA_INTERMEDIA
    else:
        comision = monto * TASA_REDUCIDA
    return round(comision, 2)


def calcular_total(monto):
    """Total que se debita al cliente: monto + comisión (2 decimales)."""
    comision = calcular_comision(monto)
    return round(monto - comision, 2)
