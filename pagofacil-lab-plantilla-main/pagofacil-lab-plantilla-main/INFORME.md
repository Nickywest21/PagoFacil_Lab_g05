# Informe del laboratorio · Pruebas y versionamiento

> Reemplaza **cada** `<<COMPLETAR>>` con tu respuesta. No borres los encabezados.
> Extensión esperada: 1.5 a 2 páginas. Se entrega haciendo `git push` de este archivo.

## 1. Datos del equipo

- **Equipo (gNN):** <<COMPLETAR>>
- **Repositorio (URL):** <<COMPLETAR>>

| Integrante | Carnet | Usuario de GitHub |
|------------|--------|-------------------|
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |

## 2. Evidencia

Pega la salida real de estos comandos (bloque de código):

`python -m pytest -q`
```
<<COMPLETAR>>
```

`git log v1.0.0..v1.0.1 --oneline --decorate`
```
<<COMPLETAR>>
```

## 3. Bitácora de defectos

| # | Pruebas que fallaban | Síntoma (mensaje del error) | Causa raíz | Corrección (qué línea cambió) | Commit | Quién |
|---|----------------------|-----------------------------|------------|-------------------------------|--------|-------|
| 1 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| 2 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| 3 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |

**Pregunta:** al inicio había 6 pruebas fallando pero solo 3 defectos. ¿Por qué? ¿Qué diferencia hay entre *síntoma* y *causa raíz*?

<<COMPLETAR>>

## 4. Versionamiento

1. Corrigieron 3 defectos sin cambiar la interfaz pública. ¿Por qué la nueva versión es `1.0.1` y no `1.1.0` ni `2.0.0`?
   <<COMPLETAR>>
2. Si agregaran la función nueva `calcular_comision_con_iva(monto)` sin tocar nada existente, ¿qué versión sería y por qué?
   <<COMPLETAR>>
3. Si cambiaran `calcular_comision(monto)` para exigir un segundo parámetro obligatorio `moneda`, ¿qué versión sería y por qué?
   <<COMPLETAR>>
4. Ejecuten `git diff v1.0.0 v1.0.1 --stat`. ¿Qué archivos cambiaron y por qué es útil poder comparar dos versiones?
   <<COMPLETAR>>

## 5. Mini duelo

Tabla de casos que diseñaron (mínimo 6 filas; indiquen la técnica):

| Partición o límite que cubre | Entrada | Resultado esperado | Técnica |
|------------------------------|---------|--------------------|---------|
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |

- **Resultado del marcador (mutantes detectados de 7):** <<COMPLETAR>>
- **¿Qué mutantes sobrevivieron (si alguno) y qué caso de prueba les habría faltado?** <<COMPLETAR>>

## 6. Reflexión (5 a 8 líneas)

Su suite visible quedó 100 % en verde y, aun así, el duelo puede encontrar defectos escondidos.
¿Qué implica eso para la estrategia de pruebas? Relaciónenlo con la pirámide de pruebas, con
qué conviene automatizar y con el caso Knight Capital de la clase.

<<COMPLETAR>>
