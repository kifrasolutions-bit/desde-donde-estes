#!/usr/bin/env python3
"""
Genera sitio.html, el sitio publicable de Desde Donde Estes.

Fuentes de entrada:
  sitio-template.html  la plantilla con marcadores __X__
  hechos.json          los 385 hechos verificados (base completa)
  contenido.json       opciones, recursos, conciertos, transparencia y fuentes
  extras/*.json        las altas de cada dia, que se fusionan sobre contenido.json
  reels.json           los reels de Instagram, si hay
  cifras.json          las cifras que cambian a diario y unos textos sueltos

La seleccion del flujo NO vive en un archivo aparte: se calcula aqui a partir
de FLUJO_ORDEN. El criterio es variedad de escala, no ranking. Un pais del Golfo
al lado de una nina con una alcancia, y ninguno mas grande que el otro.
Para cambiar que sale en el flujo, edita FLUJO_ORDEN.

Uso:  python3 construir_sitio.py
"""
import json
from pathlib import Path

import cifras
import extras

A = Path(__file__).parent

# Orden curado del flujo. Alterna escala y origen a proposito.
FLUJO_ORDEN = [
    "Emiratos", "Nina anonima de Sabaneta", "Nina anónima de Sabaneta", "Blessd",
    "Desenlace Macramé", "Centro Deportivo Luz Mery Tristán", "Vendedores ambulantes de helados",
    "POA", "Global Empowerment", "Xielo Skydive",
    "Florez Buenaños", "Barriles Carnivore", "Natalia Campo",
    "Fundacion Santo Domingo", "Fundación Santo Domingo", "Panadería La Central",
    "Olla comunitaria de vendedores", "FC Barcelona", "Óscar Conde",
    "Andres Solomon", "Andrés Solomón", "Starlink", "Taliana Vargas",
    "Los Primos Barbershop", "El Mono Bandido", "Colombia Florece", "Puntos Colombia",
    "Tiendas Ara · las vueltas",
    "Pastor Wilmer", "Fonda The Ranch AXM",
    "Only Home",
    "Colchones Happy Sleep",
    "Konrad Lorenz", "Esther Ordóñez", "La Cobra", "Ladrilleras", "Franklin Santana",
    "Federacion Internacional de Sociedades", "Federación Internacional de Sociedades",
    "Motorrad Angels",
    "Emerson Cuesta", "La Esquina", "Johana Arroyave", "PRAXIS", "encontrados.co",
    "Metalli Colombia", "Fedetranscarga",
    "Nidia Góngora",
    "Estudio Orgánico",
    "Felipe Rios", "Felipe Ríos", "Justice for Colombia", "Liga Radio Quindío",
    "Arturo Calle", "Fundación Arturo Calle · contrapartida", "Habitantes de Buenaventura",
    "Amigos de Colombia",
    "Jose Andres", "José Andrés", "Susana María Ramírez", "Uber",
    "Choripana", "Ventolini", "The Kitchen Brothers", "Giro de Rigo", "Santa Sede",
    "Colombianos en Melbourne", "All Hands and Hearts",
    "Juan David Berrío", "Libertario", "Banco de Alimentos de Bogotá", "TECHO",
    "Manos Visibles", "Senza Create", "Yango", "Lideresas del barrio San Vicente",
    "Children Change", "AfroUdeA",
]


def leer(nombre, defecto=None):
    p = A / nombre
    if not p.exists():
        return defecto
    return json.loads(p.read_text(encoding="utf-8"))


def armar_flujo(hechos):
    """Selecciona los hechos del flujo segun FLUJO_ORDEN, sin repetir."""
    usados, flujo = set(), []
    for clave in FLUJO_ORDEN:
        for h in hechos:
            if h.get("quien") and clave.lower() in h["quien"].lower():
                k = h["quien"]
                if k in usados:
                    break
                usados.add(k)
                flujo.append(h)
                break
    return flujo


def main():
    base = leer("hechos.json", {"hechos": []})
    hechos = base.get("hechos", [])
    total = base.get("total", len(hechos))
    fuentes = len({h.get("fuente_url") for h in hechos if h.get("fuente_url")})

    # El mapa junta los hechos con ubicaciones.json, que dice de donde sale
    # cada uno. Ese archivo se edita a mano y manda: si un hecho no esta ahi,
    # no dibuja punto. Asi la base de hechos no carga datos derivados.
    ub = leer("ubicaciones.json", {"coordenadas": {}, "origen": {}})
    coords, origenes = ub.get("coordenadas", {}), ub.get("origen", {})

    def ubicado(h):
        par = origenes.get(h["quien"])
        if not par:
            return None
        lugar, pais = par[0], par[1]
        xy = coords.get(lugar)
        return None if not xy else (lugar, pais, xy)

    flujo = armar_flujo(hechos)
    if not flujo:
        raise SystemExit("El flujo salio vacio. Revisa hechos.json y FLUJO_ORDEN.")

    # extras/ trae las altas del dia; ver extras.py para el porque.
    cont = extras.aplicar(leer("contenido.json", {}))
    reels = leer("reels.json", {"reels": []})

    def j(o):
        return json.dumps(o, ensure_ascii=False)

    tpl = (A / "sitio-template.html").read_text(encoding="utf-8")
    tpl = cifras.aplicar(tpl, leer("cifras.json") or {})
    reemplazos = [
        ("__HECHOS__", j(flujo)),
        # El mapa usa TODOS los hechos ubicados, no solo los del flujo curado:
        # la gracia es que se vean los 415, no 62. Del hecho se manda solo lo
        # que el panel necesita, con el texto recortado, para no duplicar la
        # base entera dentro de la pagina.
        ("__HECHOS_MAPA__", j([
            {
                "quien": h["quien"],
                "que_hizo": (h["que_hizo"][:170].rsplit(" ", 1)[0] + "…")
                            if len(h["que_hizo"]) > 175 else h["que_hizo"],
                "fuente_url": h["fuente_url"],
                "fuente_nombre": h["fuente_nombre"],
                "origen_lugar": u[0],
                "origen_pais": u[1],
                "origen_xy": u[2],
            }
            for h, u in ((h, ubicado(h)) for h in hechos) if u
        ])),
        ("__REELS__", j(reels)),
        ("__OPCIONES__", j(cont.get("opciones", {}))),
        ("__RECURSOS__", j(cont.get("recursos", []))),
        ("__CONCIERTOS__", j(cont.get("conciertos", []))),
        # Solo se publican las entradas marcadas en_sitio. Las demas se quedan
        # en contenido.json, que vive en el repositorio publico: el registro no
        # se pierde, simplemente no va en la pagina.
        ("__TRANSPARENCIA__", j([t for t in cont.get("transparencia", []) if t.get("en_sitio")])),
        ("__FUENTES_LISTA__", j(cont.get("fuentes", []))),
        ("__TOTAL__", str(total)),
        ("__FUENTES__", str(fuentes)),
    ]
    for marca, valor in reemplazos:
        if marca not in tpl:
            raise SystemExit(f"Falta el marcador {marca} en sitio-template.html")
        tpl = tpl.replace(marca, valor)

    if "CORREO-PENDIENTE" in tpl:
        print("  AVISO: el correo de contacto sigue sin poner.")
        print("  Cambialo en sitio-template.html antes de publicar.")

    (A / "sitio.html").write_text(tpl, encoding="utf-8")
    # index.html es lo que sirve GitHub Pages en la raiz. Tiene que ser el sitio
    # nuevo, no el directorio viejo. Se escribe identico, no como copia manual,
    # para que nunca queden desincronizados.
    (A / "index.html").write_text(tpl, encoding="utf-8")
    print(f"sitio.html e index.html generados")
    print(f"  {len(flujo)} hechos en el flujo, de {total} en la base")
    print(f"  {fuentes} fuentes distintas · {len(tpl):,} bytes")


if __name__ == "__main__":
    main()
