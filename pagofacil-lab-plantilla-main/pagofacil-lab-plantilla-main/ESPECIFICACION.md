# Especificación · Comisión de transferencias (PagoFácil GT)

Documento de referencia del laboratorio. Es la **fuente de verdad**: si el código y este
documento discrepan, el defecto está en el código.

## Reglas de negocio

| Tramo | Monto de la transferencia (Q) | Comisión |
|-------|-------------------------------|----------|
| 1 | Hasta 100 (**incluye** 100) | Q0.00 |
| 2 | Más de 100 y hasta 1,000 (**incluye** 1,000) | 1.5 % del monto |
| 3 | Más de 1,000 | 1 % del monto |

- **RN1 · Tope:** la comisión nunca es mayor que **Q25.00**.
- **RN2 · Redondeo:** la comisión se redondea a **2 decimales**.
- **RN3 · Total:** `total = monto + comisión`, redondeado a 2 decimales.
- **RN4 · Monto válido:** número (`int` o `float`) **mayor que 0**.
  - Si no es un número (texto, `None`, listas, `True`/`False`) → `TypeError`.
  - Si es un número menor o igual que 0 → `ValueError`.

## Funciones (módulo `pagofacil/comision.py`)

| Función | Devuelve | Errores |
|---------|----------|---------|
| `validar_monto(monto)` | el monto como `float` | `TypeError`, `ValueError` (RN4) |
| `calcular_comision(monto)` | comisión en Q (`float`, 2 decimales) | los de `validar_monto` |
| `calcular_total(monto)` | total a debitar en Q (`float`, 2 decimales) | los de `validar_monto` |

## Ejemplos de referencia

| Monto | Comisión | Total | Por qué |
|------:|---------:|------:|---------|
| 50 | 0.00 | 50.00 | Tramo 1 |
| 200 | 3.00 | 203.00 | Tramo 2 (1.5 %) |
| 3000 | 25.00 | 3025.00 | Tramo 3: 1 % = 30, el tope lo baja a 25 |

## Nota para diseñar casos de prueba

Evita montos cuyo resultado caiga **justo en medio centavo** (por ejemplo 101 → 1.515 o
1000.5 → 10.005): el redondeo binario de los `float` los vuelve ambiguos. Usa múltiplos de 10
o los valores límite (`100.01`, `1000.01`).
