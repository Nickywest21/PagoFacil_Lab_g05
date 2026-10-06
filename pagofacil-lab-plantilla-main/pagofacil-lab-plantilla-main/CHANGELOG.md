# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
[Versionado Semántico](https://semver.org/lang/es/).

## [Sin publicar]

## [1.0.1] - 2026-10-05
### Corregido
- El Tramo 1 usaba `<` en vez de `<=`: una transferencia de Q100.00 exacto cobraba comisión en lugar de ser gratis.
- El tope de Q25.00 estaba definido como `TOPE_COMISION` pero nunca se aplicaba, así que los montos mayores a Q2,500.00 cobraban más de Q25.00 (Q3,000.00 pagaba Q30.00).
- `calcular_total` restaba la comisión en vez de sumarla, de modo que el total debitado al cliente era menor que el monto de la transferencia.

## [1.0.0]
### Agregado
- Cálculo de la comisión de transferencias (`calcular_comision`).
- Cálculo del total a debitar (`calcular_total`).
- Validación del monto (`validar_monto`).
