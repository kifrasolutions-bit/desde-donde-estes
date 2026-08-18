#!/usr/bin/env python3
"""Fusiona los archivos de extras/ sobre el contenido ya leido.

Existe por una restriccion del entorno, no por diseno: contenido.json pesa
69 KB y el conector de GitHub con el que sube el agente se cae por encima de
los 8 KB, asi que las altas diarias no se podian publicar. Cada dia deja su
archivo pequeno en extras/ y aqui se pegan al final de la seccion que toque.

Se aplican en orden alfabetico, que por el nombre de archivo es orden de fecha.

Si algun dia se puede editar contenido.json directamente, se vuelca todo esto
alli y se borra la carpeta: nada mas depende de ella.
"""
import json
from pathlib import Path


def aplicar(cont, carpeta=None):
    carpeta = Path(carpeta or Path(__file__).parent / "extras")
    if not carpeta.is_dir():
        return cont

    for ruta in sorted(carpeta.glob("*.json")):
        d = json.loads(ruta.read_text(encoding="utf-8"))

        anadir = d.get("anadir", {})
        for puerta, tarjetas in anadir.get("opciones", {}).items():
            if puerta not in cont.get("opciones", {}):
                raise SystemExit("%s: la puerta '%s' no existe en contenido.json." % (ruta.name, puerta))
            cont["opciones"][puerta]["o"] += tarjetas

        for seccion in ("recursos", "conciertos", "transparencia", "fuentes", "casos"):
            if anadir.get(seccion):
                cont.setdefault(seccion, [])
                cont[seccion] += anadir[seccion]

        # Un par que no aparece exactamente una vez detiene la construccion, igual
        # que en cifras.py: vale mas no construir que publicar algo a medias.
        for viejo, nuevo in d.get("cambios", []):
            crudo = json.dumps(cont, ensure_ascii=False)
            if crudo.count(viejo) != 1:
                raise SystemExit("%s: el texto a cambiar aparece %d veces, se esperaba 1: %s"
                                 % (ruta.name, crudo.count(viejo), viejo[:60]))
            cont = json.loads(crudo.replace(viejo, nuevo))

    if cont.get("conciertos"):
        cont["conciertos"].sort(key=lambda c: c.get("iso", ""))

    return cont
