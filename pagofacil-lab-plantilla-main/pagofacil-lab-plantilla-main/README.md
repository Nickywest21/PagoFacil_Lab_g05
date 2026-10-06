# PagoFácil GT · Laboratorio de pruebas y versionamiento

Ingeniería de Software 1 · Laboratorio: **Rescata el repositorio + Mini duelo** (60 min).

Este repositorio contiene la **v1.0.0** de PagoFácil GT, publicada con **3 defectos**.
Tu equipo debe rescatarla: leer el reporte de pruebas, corregir con commits pequeños,
publicar la **v1.0.1** y luego demostrar con un duelo qué tan buenas son sus pruebas.

## Comandos que necesitarás

```bash
python -m pip install -r requirements.txt   # una sola vez
python -m pytest -v                          # correr las pruebas
git pull                                     # ANTES de empezar a teclear
git add .  &&  git commit -m "fix(comision): ..."
git push                                     # DESPUÉS de cada commit
git tag -a v1.0.1 -m "Corrige 3 defectos"    # crear versión
git push --tags                              # publicar las versiones
```

> En macOS/Linux quizá debas usar `python3` en lugar de `python`. En Windows también funciona `py`.

## Contenido

| Ruta | Para qué sirve |
|------|----------------|
| `ESPECIFICACION.md` | Reglas de negocio. Es la fuente de verdad. |
| `src/pagofacil/comision.py` | Código a rescatar (tiene 3 defectos). |
| `tests/test_comision.py`, `tests/test_total.py` | Pruebas oficiales. **No las modifiques.** |
| `tests/test_duelo.py` | Tu archivo para el mini duelo. |
| `CHANGELOG.md` | Registro de versiones. Lo actualizas antes de publicar v1.0.1. |
| `INFORME.md` | Informe de entrega (se completa después del laboratorio). |
| `check_setup.py` | Verifica que tu computadora esté lista. |
| `tarea_previa/` | Práctica de calentamiento con pytest (tarea previa). |

Todo lo demás está en la **Guía del estudiante**.
