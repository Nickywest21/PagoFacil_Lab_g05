# Informe del laboratorio · Pruebas y versionamiento

> Reemplaza **cada** `<<COMPLETAR>>` con tu respuesta. No borres los encabezados.
> Extensión esperada: 1.5 a 2 páginas. Se entrega haciendo `git push` de este archivo.

## 1. Datos del equipo

- **Equipo (gNN):** g05
- **Repositorio (URL):** https://github.com/Nickywest21/PagoFacil_Lab_g05.git

| Integrante | Carnet | Usuario de GitHub |
|------------|--------|-------------------|
| Juan Pablo Estrada Rodriguez | 1056124 | juanpaestra8 |
| Christopher Conrado López Vicente | 1053824 | ChristopherLopez1053824 |
| Marc Wilhelm Schaub Garcia | 1243424 | mwschaub |
| Nahomy Mariángel Chitay Duarte | 1211523 | mariangelduarte74 |
| Paula Nicolle West Ortiz | 1245524 | Nickywest21 |

## 2. Evidencia

Pega la salida real de estos comandos (bloque de código):

`python -m pytest -q`
```
...................................                                      [100%]
40 passed in 0.02s
```

`git log v1.0.0..v1.0.1 --oneline --decorate`
```
5dcb1e8 (tag: v1.0.1) docs(changelog): registrar versión 1.0.1
7b760ab Merge commit '3cb0b2c234f5a242a998d7f39ff62a307d86fb13'
9e2aa09 Merge commit 'c191ac2931e89a2af8735c3d69ed82c8c5842b2c'
9713ba2 Merge commit 'b75e26c48af76364f40c63a44889e6897f4fbb00'
c191ac2 (origin/nicky) fix(comision): arreglo de la suma en el round
b75e26c (origin/Christopher, Christopher) "fix(comision): aplicar tope maximo de Q25"
3cb0b2c (origin/JuanPablo) fix(comision): tramo 1 incluye el limite de Q100
```

## 3. Bitácora de defectos

| # | Pruebas que fallaban | Síntoma (mensaje del error) | Causa raíz | Corrección (qué línea cambió) | Commit | Quién |
|---|----------------------|-----------------------------|------------|-------------------------------|--------|-------|
| 1 | `test_monto_exacto_100_no_paga_comision` (1) | `AssertionError: assert 1.5 == 0` | La condición del Tramo 1 usaba `<` en vez de `<=`; la especificación dice "Hasta 100 (**incluye** 100)", así que Q100.00 exacto debía ser gratis. | `src/pagofacil/comision.py` L30: `if monto < LIMITE_SIN_COMISION:` → `if monto <= LIMITE_SIN_COMISION:` | `3cb0b2c` | Juan Pablo Estrada Rodriguez |
| 2 | `test_tope_maximo_de_q25[3000]`, `test_tope_maximo_de_q25[10000]`, `test_tope_maximo_de_q25[1000000]` (3) | `AssertionError: assert 30.0 == 25` (y `100.0 == 25`, `10000.0 == 25`) | La constante `TOPE_COMISION = 25` estaba definida pero nunca se usaba: la RN1 ("la comisión nunca es mayor que Q25.00") no tenía ninguna línea de código que la aplicara. Faltaba el `min(...)` antes del `round`. | `src/pagofacil/comision.py` L36 (nueva): `comision = min(comision, TOPE_COMISION)` antes de `return round(comision, 2)` | `b75e26c` | Christopher Conrado López Vicente |
| 3 | `test_total_incluye_la_comision[200-203.0]`, `test_total_incluye_la_comision[500-507.5]` (2) | `AssertionError: assert 197.0 == 203.0` y `assert 492.5 == 507.5` | `calcular_total` operaba `monto - comision` cuando la RN3 define `total = monto + comisión`. El total debitado quedaba **por debajo** del monto de la transferencia. | `src/pagofacil/comision.py` L43: `return round(monto - comision, 2)` → `return round(monto + comision, 2)` | `c191ac2` | Paula Nicolle West Ortiz |

**Pregunta:** al inicio había 6 pruebas fallando pero solo 3 defectos. ¿Por qué? ¿Qué diferencia hay entre *síntoma* y *causa raíz*?

Las 6 pruebas rojas eran 3 defectos multiplicados por el número de datos que cada uno rompía. El defecto 2 (el tope sin aplicar) tumbaba 3 pruebas porque `test_tope_maximo_de_q25` está parametrizada con tres montos — Q3,000, Q10,000 y Q1,000,000 — que son tres síntomas distintos (Q30.00, Q100.00 y Q10,000.00 esperados frente a Q25.00) de **una sola** causa raíz: la ausencia del `min()`. El defecto 3 tumbaba 2 pruebas por lo mismo: Q200 y Q500 son dos síntomas (Q197.00 y Q492.50 frente a Q203.00 y Q507.50) de un único `+` que debía ser `-`.

*síntoma* es lo que el test observa desde afuera: el valor que salió y el que se esperaba. *causa raíz* es la línea de código del `src/` que hace que ese valor salga así. La diferencia importa porque arreglar el síntoma es imposible —no se puede hacer que `calcular_comision(3000)` devuelva 25 sin tocar `calcular_comision`— mientras que corregir la causa raíz deja verdes **todas** las pruebas afectadas a la vez. Si hubiéramos "arreglado" las 6 pruebas una por una, habríamos tocado `comision.py` tres veces por tres motivos distintos y probablemente introducido un cuarto defecto.

## 4. Version versioning

1. Corrigieron 3 defectos sin cambiar la interfaz pública. ¿Por qué la nueva versión es `1.0.1` y no `1.1.0` ni `2.0.0`?
   Es una **PATCH (1.0.1)** porque el número mayor y el menor no cambian: no agregamos funciones nuevas (eso sería 1.1.0) ni rompimos la interfaz pública —`calcular_comision(monto)`, `calcular_total(monto)` y `validar_monto(monto)` siguen teniendo las mismas firmas, los mismos parámetros y lanzan los mismos `TypeError` / `ValueError`, tal como exige la RN4—. Solo cambiamos el *comportamiento interno* para que cumpla lo que la especificación ya prometía. Bajo SemVer, una corrección de comportamiento que no rompe a quien ya integraba el código es un cambio de parche.
2. Si agregaran la función nueva `calcular_comision_con_iva(monto)` sin tocar nada existente, ¿qué versión sería y por qué?
   Sería **1.1.0 (MINOR)**. Es functionality nueva y 100 % retrocompatible: las funciones actuales siguen funcionando igual y nadie que use la versión anterior se rompe, así que no vale la pena un 2.0.0. SemVer reserva el menor para "agregué algo, nada de lo que existía se rompió".
3. Si cambiaran `calcular_comision(monto)` para exigir un segundo parámetro obligatorio `moneda`, ¿qué versión sería y por qué?
   Sería **2.0.0 (MAJOR)**. Un parámetro nuevo y obligatorio es un cambio incompatible: todo el código de los consumidores que hoy llama `calcular_comision(3000)` empezaría a lanzar `TypeError` de la nada. No hay forma de que alguien actualice sin tocar su código, que es exactamente la definición de un rompimiento mayor.
4. Ejecuten `git diff v1.0.0 v1.0.1 --stat`. ¿Qué archivos cambiaron y por qué es útil poder comparar dos versiones?
   ```
    .../pagofacil-lab-plantilla-main/check_setup.py      | 4 ++--
    .../pagofacil-lab-plantilla-main/src/pagofacil/comision.py           | 5 +++--
    2 files changed, 5 insertions(+), 4 deletions(-)
   ```
   Cambiaron 2 archivos: `src/pagofacil/comision.py`, que es donde viven los tres defectos (1 línea modificada y 1 agregada por cada corrección), y `check_setup.py`, que es solo un script auxiliar del laboratorio. Comparar dos versiones es útil porque responde de un vistazo **qué cambió entre una entrega y otra** sin tener que revisar commit por commit: con `--stat` ves los archivos afectados y cuántos renglones cambiaron, y con el diff completo ves las líneas exactas. Eso permite auditar una corrección ("¿este cambio de la v1.0.0 a la v1.0.1 metió algo que no debía?"), reproducir un ambiente exacto poniendo `git checkout v1.0.1`, y hacer *bisect* para encontrar el commit que introdujo un fallo.

## 5. Mini duelo

Tabla de casos que diseñaron (mínimo 6 filas; indiquen la técnica):

| Partición o límite que cubre | Entrada | Resultado esperado | Técnica |
|------------------------------|---------|--------------------|---------|
| Tramo 1 · frontera superior (incluye Q100) | `100` | comisión `0.0` | Valor límite (borde derecho) |
| Tramo 1 · Tramo 2 · primer valor sobre la frontera | `100.01` | comisión `1.5` | Valor límite (borde izquierdo) |
| Tramo 2 · Tramo 3 · frontera superior (incluye Q1,000) | `1000` | comisión `15.0` | Valor límite (borde derecho) |
| Tramo 3 · primer valor sobre la frontera | `1000.01` | comisión `10.0` | Valor límite (borde izquierdo) |
| Tramo 3 · representativo sin llegar al tope | `2400` | comisión `24.0` | Partición de equivalencia |
| Tope Q25 · comisión exactamente igual al tope | `2500` | comisión `25.0` | Valor límite |
| Tope Q25 · primer valor que lo supera | `2510` | comisión `25.0` | Valor límite |
| Tope Q25 · monto muy grande | `10000` | comisión `25.0` | Partición de equivalencia |
| RN2 · redondeo a 2 decimales (truncar daría 19.99) | `1999.99` | comisión `20.0` | Valor límite |
| RN4 · tipos inválidos | `"100"`, `None`, `[]`, `{}` | `TypeError` | Partición de equivalencia |
| RN4 · `bool` no es un número válido (mutante bonus) | `True`, `False` | `TypeError` | Partición de equivalencia |
| RN4 · números no positivos | `0`, `0.0`, `-0.01`, `-100` | `ValueError` | Partición de equivalencia |
| RN3 · total = monto + comisión | `100` → `100.0`, `200` → `203.0`, `1500` → `1515.0`, `5000` → `5025.0` | total correcto | Partición de equivalencia |

- **Resultado del marcador (mutantes detectados de 7):** *Pendiente.* El docente aún no ha ejecutado la revisión (minuto 55). Nuestra cobertura apunta a los 6 mutantes normales (las 3 fronteras de los tramos, las 2 tasas, el tope) **más el mutante bonus**, que la RN4 declara explícitamente: `True`/`False` deben levantar `TypeError` aunque en Python `bool` sea subclase de `int`. Creemos que es el único que exige leer la regla con cuidado, porque un mutante que quita el `isinstance(monto, bool)` de `validar_monto` seguiría *"funcionando"* para todos los montos numéricos.
- **¿Qué mutantes sobrevivieron (si alguno) y qué caso de prueba les habría faltado?** *Pendiente de conocer el marcador.* Casos que sabemos que **no** cubrimos, y que son las candidatas más probables a sobrevivir: (a) no verificamos que `validar_monto` devuelva un `float` (un mutante que quite el `return float(monto)`); (b) ya no aplica: `test_total_por_tramos` cubre ahora los tres tramos (Tramo 1 con `50` y `100`, Tramo 2 con `200`, Tramo 3 sin tope con `1500`, y el tope con `5000`); y (c) ningún caso fuerza un redondeo de 3 decimales a 2 dentro de `calcular_total`, porque `200 + 3.0` y `1500 + 15.0` ya salen exactos. El punto (a) sigue siendo el hueco real.

## 6. Reflexión (5 a 8 líneas)

Nuestra suite visible terminó 100 % en verde y aun así el código tenía tres defectos que ni una sola prueba detectaba. Eso revela que "todas las pruebas pasan" no es lo mismo que "el código es correcto": lo que nuestras pruebas medían era precisamente lo que ya sabíamos medir, y todo lo demás se quedó invisible. Lo que preocupa es que los tres defectos eran de la misma familia —condiciones de frontera y una operación aritmética— y los tres cambiaban el dinero que se le cobra al cliente, sin que ninguna prueba lo dijera. En la pirámide de pruebas eso sugiere cómo repartir el esfuerzo: muchos casos unitarios rápidos y baratos en la base, pero ningún volumen de esos casos reemplaza una prueba de integración o una revisión que contraste el código contra la especificación, que es justo donde vivían la RN1 y la RN3. Lo que conviene automatizar es la repetición mecánica —las 3 fronteras, los dos lados de cada una, los tipos inválidos— porque una persona las omite por cansancio aunque lo entienda perfecto. Y lo que conviene no automatizar es el razonamiento sobre si las reglas están bien: el caso Knight Capital de la clase recuerda que años de producción pueden caerse por un signo y un decimal, y ninguna suite lo habría atrapado si nadie se hace la pregunta. La próxima vez la estrategia no es escribir más pruebas, es preguntarse qué regla de negocio todavía no hemos escrito como aserción.