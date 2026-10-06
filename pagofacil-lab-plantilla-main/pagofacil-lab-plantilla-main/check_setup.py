#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica que tu computadora esté lista para el laboratorio.

Ejecuta desde la carpeta de TU repositorio:
    python check_setup.py        (macOS/Linux: python3 check_setup.py)

Al final copia TODA la salida en la plataforma del curso (o toma una captura completa).
"""
import platform
import re
import subprocess
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

OK, MAL, AVISO = "[ OK ]", "[FALLA]", "[AVISO]"
resultados = []


def run(*cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:  # git no instalado, etc.
        return 127, "", str(e)


def check(nombre, estado, detalle="", arreglo=""):
    resultados.append((nombre, estado, detalle, arreglo))


# 1. Python
v = sys.version_info
if v >= (3, 10):
    check("Python", OK, f"{v.major}.{v.minor}.{v.micro}")
elif v >= (3, 9):
    check("Python", AVISO, f"{v.major}.{v.minor} (funciona; se recomienda 3.10 o superior)")
else:
    check("Python", MAL, f"{v.major}.{v.minor}", "Instala Python 3.10 o superior desde python.org")

# 2. pytest
try:
    import pytest
    mayor = int(re.match(r"(\d+)", pytest.__version__).group(1))
    if mayor >= 7:
        check("pytest", OK, pytest.__version__)
    else:
        check("pytest", MAL, pytest.__version__, "python -m pip install -U pytest")
except ImportError:
    check("pytest", MAL, "no instalado", "python -m pip install -r requirements.txt")

# 3. git
rc, out, _ = run("git", "--version")
if rc == 0:
    check("git", OK, out)
else:
    check("git", MAL, "no encontrado", "Instala Git desde git-scm.com y abre una terminal nueva")

# 4. identidad de git
_, nombre, _ = run("git", "config", "user.name")
_, correo, _ = run("git", "config", "user.email")
if nombre and correo:
    check("git identidad", OK, f"{nombre} <{correo}>")
else:
    check("git identidad", MAL, "falta user.name o user.email",
          'git config --global user.name "Tu Nombre"  y  git config --global user.email "tu@correo.com"')

# 5. pull.rebase (evita editores de texto inesperados)
_, rebase, _ = run("git", "config", "pull.rebase")
if rebase == "true":
    check("git pull.rebase", OK, "true")
else:
    check("git pull.rebase", AVISO, "sin configurar", "git config --global pull.rebase true")

# 6. estar dentro de un repositorio
rc, top, _ = run("git", "rev-parse", "--show-toplevel")
if rc != 0:
    check("Repositorio", MAL, "esta carpeta no es un repositorio git",
          "Entra a la carpeta clonada de tu equipo: cd pagofacil-lab-gNN")
else:
    _, origin, _ = run("git", "remote", "get-url", "origin")
    nombre_repo = re.sub(r"\.git$", "", origin.rstrip("/").split("/")[-1]) if origin else ""
    if not origin:
        check("Remoto origin", MAL, "no hay remoto 'origin'", "Clona tu repositorio con git clone <URL>")
    elif "plantilla" in nombre_repo.lower():
        check("Repositorio de equipo", MAL, f"estás en la PLANTILLA ({nombre_repo})",
              "Crea tu repo con 'Use this template' y clona ESE repositorio")
    elif re.fullmatch(r"pagofacil-lab-g\d{2}", nombre_repo):
        check("Repositorio de equipo", OK, nombre_repo)
    else:
        check("Repositorio de equipo", AVISO, f"{nombre_repo} (se esperaba pagofacil-lab-gNN)",
              "Renombra el repo en GitHub: Settings > General > Repository name")
    if origin:
        rc, _, err = run("git", "ls-remote", "--heads", "origin")
        if rc == 0:
            check("Conexión con GitHub", OK, "se puede leer el remoto")
        else:
            check("Conexión con GitHub", MAL, "no se pudo leer el remoto",
                  "Revisa internet, que el repo sea Public y tu inicio de sesión (gh auth login)")
    _, rama, _ = run("git", "branch", "--show-current")
    if rama == "main":
        check("Rama actual", OK, rama)
    else:
        check("Rama actual", AVISO, rama or "(desconocida)", "Se espera 'main'")

print("=" * 64)
print("  VERIFICACIÓN DEL ENTORNO · Laboratorio Pruebas y Versionamiento")
print("=" * 64)
fallas = 0
for nombre, estado, detalle, arreglo in resultados:
    print(f"{estado} {nombre:24s} {detalle}")
    if estado == MAL:
        fallas += 1
        print(f"         -> Cómo arreglarlo: {arreglo}")
    elif estado == AVISO and arreglo:
        print(f"         -> Recomendado: {arreglo}")
print("-" * 64)
print(f"Sistema: {platform.system()} {platform.release()} | Python: {platform.python_version()}")
print(f"Fecha: {time.strftime('%Y-%m-%d %H:%M')}")
if fallas == 0:
    print("RESULTADO: LISTO PARA EL LABORATORIO")
else:
    print(f"RESULTADO: FALTAN {fallas} COSA(S) POR ARREGLAR")
sys.exit(0 if fallas == 0 else 1)
