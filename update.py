#!/usr/bin/env python3
"""
Mantenimiento diario de Desde Donde Estes.

Hace tres cosas, en orden de cuanto se puede confiar en ellas:

1. RECONSTRUYE
   Corre construir_sitio.py, que genera sitio.html e index.html a partir de
   sitio-template.html + hechos.json + contenido.json + reels.json.

2. REVISA ENLACES (necesita red)
   Abre todos los enlaces salientes del sitio publicado y avisa cual dejo de
   responder. Un 403 casi siempre es el medio bloqueando robots, no un enlace
   muerto: hay que abrirlo en el navegador antes de quitarlo.

3. VIGILA EL SISMO (necesita red)
   Consulta el USGS y COMPARA con lo que el sitio dice hoy. No reescribe nada
   solo: si el USGS cambia la magnitud, la profundidad o el epicentro, avisa
   para que una persona decida. El sitio afirma cosas con fuente, y corregir
   automaticamente una cifra ya publicada tiene que pasar por alguien.

Tambien avisa si la fecha de verificacion del sitio ya esta vieja.

Uso:
    python3 update.py                 # todo
    python3 update.py --solo-build    # solo reconstruir, sin red
    python3 update.py --solo-enlaces  # solo revisar enlaces

Sale con codigo 1 si hay enlaces caidos o si el USGS no coincide, para que
GitHub Actions abra una alerta.
"""

import datetime
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).parent
SITIO = AQUI / "sitio.html"
PLANTILLA = AQUI / "sitio-template.html"
CONSTRUCTOR = AQUI / "construir_sitio.py"

USGS_ID = "us6000tjl2"
USGS_URL = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&eventid={USGS_ID}"

# Lo que el sitio afirma hoy. Si el USGS se separa de esto, se avisa.
ESPERADO = {"magnitud": 7.4, "lugar": "palmar", "profundidad_km": 110}
TOLERANCIA_MAG = 0.05
TOLERANCIA_PROF = 3

UA = "desde-donde-estes/1.0 (revision de enlaces de un directorio de ayuda humanitaria)"
TIMEOUT = 25
DIAS_PARA_AVISAR = 7


# ------------------------------------------------------------- 1. construir

def construir():
    r = subprocess.run([sys.executable, str(CONSTRUCTOR)], capture_output=True, text=True)
    if r.stdout.strip():
        print("  " + r.stdout.strip().replace("\n", "\n  "))
    if r.returncode != 0:
        print(r.stderr.strip())
        raise SystemExit("La construccion fallo. No se sigue.")


# --------------------------------------------------------------- 2. enlaces

def enlaces_del_sitio():
    """Todas las URLs salientes del sitio publicado, menos Instagram.

    Instagram queda fuera a proposito: sus embeds le responden distinto a un
    bot que a una persona y llenarian el reporte de falsos positivos.
    """
    html = SITIO.read_text(encoding="utf-8")
    urls = set()
    for u in re.findall(r"https?://[^\s\"'<>\\)]+", html):
        u = u.rstrip(".,;")
        if "instagram.com" in u:
            continue
        urls.add(u)
    return sorted(urls)


def revisar_uno(u):
    codigo = "sin respuesta"
    for metodo in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": UA}, method=metodo)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                if r.status == 200:
                    return u, 200
                codigo = r.status
        except urllib.error.HTTPError as ex:
            codigo = ex.code
            if codigo not in (403, 405, 999):
                return u, codigo
        except Exception as ex:
            codigo = type(ex).__name__
    return u, codigo


def revisar_enlaces():
    urls = enlaces_del_sitio()
    print(f"  Revisando {len(urls)} enlaces...")
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(revisar_uno, urls))
    rotos = [(u, c) for u, c in res if c != 200]
    print(f"  Responden bien: {len(res) - len(rotos)} de {len(res)}")
    if rotos:
        print(f"\n  {len(rotos)} por revisar:")
        for u, c in sorted(rotos, key=lambda x: str(x[1])):
            print(f"    {c}  {u}")
        print("\n  Un 403 suele ser el medio bloqueando robots, no un enlace muerto.")
        print("  Abrelo en el navegador antes de quitar nada del sitio.")
    return rotos


# ------------------------------------------------------------------ 3. USGS

def vigilar_sismo():
    req = urllib.request.Request(USGS_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        g = json.loads(r.read().decode("utf-8"))

    props = g["properties"]
    prof = round(g["geometry"]["coordinates"][2])
    mag, lugar = props["mag"], props["place"]
    print(f"  USGS dice: M{mag} · {lugar} · {prof} km")

    difs = []
    if abs(float(mag) - ESPERADO["magnitud"]) > TOLERANCIA_MAG:
        difs.append(f"magnitud: el sitio dice {ESPERADO['magnitud']}, el USGS dice {mag}")
    if ESPERADO["lugar"] not in lugar.lower():
        difs.append(f"epicentro: el USGS ahora dice '{lugar}'")
    if abs(prof - ESPERADO["profundidad_km"]) > TOLERANCIA_PROF:
        difs.append(f"profundidad: el sitio dice {ESPERADO['profundidad_km']} km, el USGS dice {prof} km")

    if difs:
        print("\n  EL USGS YA NO COINCIDE CON LO QUE DICE EL SITIO:")
        for d in difs:
            print(f"    - {d}")
        print("  No se cambio nada solo. Corrigelo a mano en sitio-template.html")
        print("  (CIFRAS y el kicker), ajusta ESPERADO aqui arriba y vuelve a construir.")
    else:
        print("  Coincide con lo que dice el sitio.")
    return difs


# --------------------------------------------------------------- 4. frescura

def revisar_frescura():
    tpl = PLANTILLA.read_text(encoding="utf-8")
    m = re.search(r'var VERIFICADO\s*=\s*"(\d{4}-\d{2}-\d{2})"', tpl)
    if not m:
        print("  No encontre la fecha de verificacion en la plantilla.")
        return
    fecha = datetime.date.fromisoformat(m.group(1))
    dias = (datetime.date.today() - fecha).days
    if dias >= DIAS_PARA_AVISAR:
        print(f"  Los datos se verificaron hace {dias} dias ({fecha}).")
        print("  El sitio ya le avisa solo al visitante, pero toca revisar cifras y enlaces.")
    else:
        print(f"  Verificado hace {dias} dias ({fecha}). Fresco.")


def main():
    args = sys.argv[1:]
    solo_build = "--solo-build" in args
    solo_enlaces = "--solo-enlaces" in args
    problemas = []

    if not solo_enlaces:
        print("Construccion")
        construir()
        print()
        print("Frescura")
        revisar_frescura()
        print()

    if not solo_build:
        print("Enlaces")
        problemas += revisar_enlaces()
        print()
        print("Sismo")
        try:
            problemas += vigilar_sismo()
        except Exception as ex:
            print(f"  No pude consultar el USGS: {type(ex).__name__}")
        print()

    if problemas:
        print(f"Salida con error: {len(problemas)} cosas por revisar a mano.")
        sys.exit(1)
    print("Todo en orden.")


if __name__ == "__main__":
    main()
