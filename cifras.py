#!/usr/bin/env python3
"""Inyecta cifras.json y textos.json dentro de sitio-template.html.

Las cifras que cambian, la fecha de verificacion y los textos que se retocan
seguido viven en esos dos JSON y no dentro de los 90 KB de la plantilla.

Si un patron no aparece exactamente una vez, se detiene. Vale mas no construir
que construir mal y publicar una cifra a medias.
"""
import json
import re
from pathlib import Path


def quitar_medidor(tpl):
    """Saca la banda de cifras agregadas. Retirada el 17 de agosto de 2026.

    Cualquier marcador invita a compararse contra un total, y el total de la
    reconstruccion no lo conoce nadie, asi que la comparacion siempre da
    desanimo. Ademas el mapa y la cadena de hechos ya muestran lo mismo con
    nombre propio y fuente, que es la regla C2.

    Para reactivarla, poner cifras en "medidor" dentro de cifras.json.
    """
    patron = r'\n<section class="banda">.*?data-i="h_llev".*?</section>\n'
    tpl, n = re.subn(patron, "\n", tpl, flags=re.S)
    if n != 1:
        raise SystemExit("La banda del medidor aparece %d veces, se esperaba 1." % n)

    viejo = "  function pintaCifras(){\n    var box=$('#cifras');box.innerHTML='';"
    if tpl.count(viejo) != 1:
        raise SystemExit("No se pudo poner el guardia en pintaCifras.")
    tpl = tpl.replace(viejo, "  function pintaCifras(){\n    var box=$('#cifras');\n    if(!box) return;\n    box.innerHTML='';")
    return tpl


def quitar_brecha(tpl):
    """Saca la seccion "Lo donado es historico. Y no alcanza."

    Retirada el 17 de agosto de 2026. Era lo mas contrario a C3 bis y C6 bis
    que tenia la pagina: una barra que dibujaba lo donado contra una estimacion
    del costo total, el 5% que se retiro de C6, y un titular que terminaba en
    "no alcanza". El argumento que valia la pena esta en C6 bis: la donacion
    privada es la parte que llega primero.

    Para reactivarla, poner "brecha": true en cifras.json.
    """
    patron = r'\n<section class="brecha">.*?</section>\n'
    tpl, n = re.subn(patron, "\n", tpl, flags=re.S)
    if n != 1:
        raise SystemExit("La seccion brecha aparece %d veces, se esperaba 1." % n)

    # El JS que llenaba la leyenda escribe ahora en un div suelto, para no
    # tocar 90 KB de plantilla por dos lineas.
    viejo = "var ley=$('#leyenda');ley.innerHTML='';"
    if tpl.count(viejo) != 1:
        raise SystemExit("No se pudo neutralizar la leyenda de la brecha.")
    tpl = tpl.replace(viejo, "var ley=$('#leyenda')||el('div');ley.innerHTML='';")
    return tpl


def aplicar(tpl, c):
    def j(o):
        return json.dumps(o, ensure_ascii=False)

    tpl, n = re.subn(r'var VERIFICADO = "[^"]*";',
                     'var VERIFICADO = "%s";' % c["verificado"], tpl)
    if n != 1:
        raise SystemExit("VERIFICADO aparece %d veces, se esperaba 1." % n)

    if not c.get("medidor"):
        tpl = quitar_medidor(tpl)

    if not c.get("brecha"):
        tpl = quitar_brecha(tpl)

    nuevo = "var CIFRAS=" + j(c["medidor"]) + ";"
    tpl, n = re.subn(r"var CIFRAS=\[.*?\];", lambda m: nuevo, tpl, flags=re.S)
    if n != 1:
        raise SystemExit("CIFRAS aparece %d veces, se esperaba 1." % n)

    # Hay dos declaraciones de CTX y manda la ultima. Se reemplazan todas.
    nuevo = "var CTX=" + j(c["contexto"]) + ";"
    tpl, n = re.subn(r"var CTX=\[.*?\];", lambda m: nuevo, tpl, flags=re.S)
    if n < 1:
        raise SystemExit("No se encontro CTX.")

    pies = [(r"'Balance de la UNGRD con corte al.*?\n\s*:\s*'.*?';",
             c["pie_ctx_es"], c["pie_ctx_en"])]
    if c.get("medidor"):
        pies.insert(0, (r"'Lo que ya se hizo, con corte al[^']*'\s*\n\s*:\s*'[^']*';",
                        c["corte_es"], c["corte_en"]))

    for patron, es, en in pies:
        rep = j(es) + "\n      : " + j(en) + ";"
        tpl, n = re.subn(patron, lambda m: rep, tpl, flags=re.S)
        if n != 1:
            raise SystemExit("El pie con fecha de corte aparece %d veces." % n)

    pares = list(c.get("textos", []))
    ruta = Path(__file__).parent / "textos.json"
    if ruta.exists():
        pares += json.loads(ruta.read_text(encoding="utf-8")).get("pares", [])

    for viejo, nuevo_txt in pares:
        if tpl.count(viejo) != 1:
            raise SystemExit("El texto a cambiar no aparece 1 vez: " + viejo[:60])
        tpl = tpl.replace(viejo, nuevo_txt)

    return tpl
