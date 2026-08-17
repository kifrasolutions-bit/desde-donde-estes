#!/usr/bin/env python3
"""Inyecta cifras.json y textos.json dentro de sitio-template.html.

Las cifras que cambian a diario, la fecha de verificacion y los textos que se
retocan seguido viven en esos dos JSON y no dentro de los 90 KB de la
plantilla. Asi una actualizacion diaria es editar un archivo pequeno.

Si un patron no aparece exactamente una vez, se detiene. Vale mas no construir
que construir mal y publicar una cifra a medias.
"""
import json
import re
from pathlib import Path


def aplicar(tpl, c):
    def j(o):
        return json.dumps(o, ensure_ascii=False)

    tpl, n = re.subn(r'var VERIFICADO = "[^"]*";',
                     'var VERIFICADO = "%s";' % c["verificado"], tpl)
    if n != 1:
        raise SystemExit("VERIFICADO aparece %d veces, se esperaba 1." % n)

    nuevo = "var CIFRAS=" + j(c["medidor"]) + ";"
    tpl, n = re.subn(r"var CIFRAS=\[.*?\];", lambda m: nuevo, tpl, flags=re.S)
    if n != 1:
        raise SystemExit("CIFRAS aparece %d veces, se esperaba 1." % n)

    # Hay dos declaraciones de CTX y manda la ultima. Se reemplazan todas para
    # que no queden desfasadas entre si.
    nuevo = "var CTX=" + j(c["contexto"]) + ";"
    tpl, n = re.subn(r"var CTX=\[.*?\];", lambda m: nuevo, tpl, flags=re.S)
    if n < 1:
        raise SystemExit("No se encontro CTX.")

    # Los pies con fecha de corte viven en un ternario es/en. Se reemplaza el
    # bloque entero, no cada rama por separado.
    for patron, es, en in [
        (r"'Lo que ya se hizo, con corte al[^']*'\s*\n\s*:\s*'[^']*';",
         c["corte_es"], c["corte_en"]),
        (r"'Balance de la UNGRD con corte al.*?\n\s*:\s*'.*?';",
         c["pie_ctx_es"], c["pie_ctx_en"]),
    ]:
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
