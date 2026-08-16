#!/usr/bin/env python3
"""Une los resultados de las rondas de investigacion en hechos.json, sin duplicados."""
import json, sys, re, unicodedata
from pathlib import Path

AQUI = Path(__file__).parent
SALIDA = AQUI / "hechos.json"

def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()

def cargar(ruta):
    d = json.load(open(ruta, encoding="utf-8"))
    if "result" in d: d = d["result"]
    return d.get("hechos", []), d.get("descartados", [])

def main(rutas):
    hechos, descartados, vistos = [], [], set()
    for r in rutas:
        h, x = cargar(r)
        descartados += x
        for f in h:
            # clave de dedup: quien + primeras palabras de que_hizo
            k = (norm(f.get("quien"))[:45], norm(f.get("que_hizo"))[:60])
            if k in vistos: continue
            vistos.add(k)
            hechos.append({
                "quien": f.get("quien"),
                "tipo": f.get("tipo"),
                "origen": f.get("origen"),
                "pais": f.get("pais"),
                "que_hizo": f.get("que_hizo"),
                "cifra": f.get("cifra"),
                "cuando": f.get("cuando"),
                "categoria": f.get("categoria"),
                "zona": f.get("zona"),
                "fuente_url": f.get("fuente_url"),
                "fuente_nombre": f.get("fuente_nombre"),
                "cita": f.get("cita"),
                "confianza": f.get("confianza", "alta"),
                "dominio": f.get("dominio"),
            })
    doc = {
        "_regla": "Cada hecho lleva fuente enlazada y cita textual que lo sostiene. Ver directives/reglas-editoriales.md. Nada entra sin verificar.",
        "verificado_el": "2026-08-15",
        "total": len(hechos),
        "hechos": hechos,
        "descartados": descartados,
    }
    json.dump(doc, open(SALIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(hechos)} hechos unicos, {len(descartados)} descartados -> hechos.json")

if __name__ == "__main__":
    main(sys.argv[1:] or [str(AQUI / ".tmp_ronda1.json")])
