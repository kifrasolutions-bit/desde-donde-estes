# -*- coding: utf-8 -*-
"""
Genera las piezas del carrusel de Instagram a 1080x1350.

Regla que viene del sitio y no cambia aqui: no hay fotos y no hay imagenes
generadas con IA. Todo se dibuja en codigo, con la misma paleta y la misma
tipografia de la pagina. Cada cifra que aparece en una pieza tiene su fuente
escrita en el pie del post, no inventada aqui.

    python3 construir_piezas.py          # espanol
    python3 construir_piezas.py --en     # ingles
"""

import sys, pathlib, subprocess, json

A = pathlib.Path(__file__).resolve().parent
MAPA = (A / "mapa.svg").read_text(encoding="utf-8")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:#FBF8F1;color:#16203A;position:relative;overflow:hidden;
 font:26px/1.5 "Helvetica Neue",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.franja{position:absolute;top:0;left:0;right:0;height:12px;
 background:linear-gradient(90deg,#F2C230 0 50%,#12356B 50% 75%,#C4362B 75% 100%)}
.marco{position:absolute;left:78px;right:78px;top:108px;bottom:104px;display:flex;flex-direction:column}
.ceja{font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#8A6A0E;font-weight:700}
.ceja i{font-style:normal;color:#B9AC8E;margin-right:14px}
h2{font-family:Georgia,serif;font-weight:400;font-size:76px;line-height:1.06;letter-spacing:-.02em;
 margin-top:30px;color:#16203A}
h2 em{font-style:normal;color:#12356B}
h2 .r{color:#C4362B}
p{font-size:33px;line-height:1.55;color:#2C3category}
.folio{position:absolute;right:78px;bottom:46px;font-size:20px;letter-spacing:.16em;color:#B9AC8E}
.pie-url{position:absolute;left:78px;bottom:44px;font-size:22px;letter-spacing:.06em;color:#8A6A0E;font-weight:700}
.regla{height:3px;background:#E4DCCB;margin:34px 0}
.crece{flex:1}
.centro .marco{justify-content:center}
.barra{margin-top:56px}
"""

# --- se corrige el color de p (se dejo un marcador para no repetirlo mal) ---
CSS = CSS.replace("#2C3category", "#2C3550")

CSS += """
/* portada */
.mapa{position:absolute;right:-120px;top:150px;width:900px;opacity:.16}
.mk{font-family:Georgia,serif;font-weight:400;font-size:150px;line-height:.94;letter-spacing:-.035em}
.mk span{display:block}
.mk .a{color:#8A6A0E}.mk .b{color:#12356B;margin-left:7%}.mk .c{color:#C4362B;margin-left:14%}
.gancho{font-size:36px;line-height:1.42;margin-top:auto}
.gancho b{color:#8A6A0E}

/* cifras */
.gigante{font-family:Georgia,serif;font-size:230px;line-height:.86;color:#C4362B;letter-spacing:-.04em}
.gigante small{font-size:74px;color:#16203A;letter-spacing:-.02em}
.rej{display:grid;grid-template-columns:1fr 1fr;gap:46px 52px;margin-top:14px}
.rej div{border-top:3px solid #E4DCCB;padding-top:14px}
.rej b{display:block;font-family:Georgia,serif;font-size:70px;line-height:1;color:#12356B;font-weight:400}
.rej span{font-size:26px;color:#4A5670;display:block;margin-top:8px}
.nota{font-size:22px;line-height:1.45;color:#6B7488;margin-top:auto}

/* citas */
.cita{font-family:Georgia,serif;font-size:56px;line-height:1.24;color:#12356B;letter-spacing:-.015em}
.barra{border-left:8px solid #F2C230;padding-left:34px}

/* listas */
ul{list-style:none}
.puertas li{display:flex;gap:26px;align-items:baseline;border-top:3px solid #E4DCCB;padding:22px 0}
.puertas li:last-child{border-bottom:3px solid #E4DCCB}
.puertas i{font-style:normal;font-family:Georgia,serif;font-size:30px;color:#B9AC8E;width:52px;flex:none}
.puertas b{font-family:Georgia,serif;font-weight:400;font-size:46px;line-height:1.15;color:#16203A;display:block;letter-spacing:-.015em}
.puertas span{font-size:26px;line-height:1.35;color:#4A5670;display:block;margin-top:8px}

.pasos li{display:flex;gap:30px;margin-top:44px}
.pasos i{font-style:normal;font-family:Georgia,serif;font-size:62px;color:#C4362B;line-height:1;width:56px;flex:none}
.pasos b{font-family:Georgia,serif;font-weight:400;font-size:44px;display:block;letter-spacing:-.015em}
.pasos span{font-size:28px;line-height:1.45;color:#4A5670;display:block;margin-top:8px}

.datos{margin-top:46px}
.datos div{display:flex;align-items:baseline;gap:34px;border-top:3px solid #E4DCCB;padding:26px 0}
.datos div:last-child{border-bottom:3px solid #E4DCCB}
.datos div b{font-family:Georgia,serif;font-weight:400;font-size:92px;color:#12356B;line-height:1;
 width:230px;flex:none;letter-spacing:-.03em}
.datos div span{font-size:30px;color:#4A5670}

/* cierre */
.cierre{display:flex;flex-direction:column;height:100%;text-align:left}
.url-grande{font-family:Georgia,serif;font-size:82px;color:#12356B;letter-spacing:-.03em;margin:auto 0 0}
.correo{font-size:26px;color:#4A5670;margin-top:38px}
.correo b{color:#8A6A0E}
"""


def pieza(cuerpo, folio, n_total, url=True, clase=""):
    pu = '<div class="pie-url">desdedondeestes.co</div>' if url else ""
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{clase}"><div class="franja"></div>
<div class="marco">{cuerpo}</div>
{pu}<div class="folio">{folio} / {n_total}</div></body></html>"""


# ---------------------------------------------------------------- contenido ES
ES = []

ES.append(("portada", f"""
<div class="mapa">{MAPA}</div>
<div class="ceja">10 de agosto de 2026 · Terremoto en Colombia</div>
<div class="mk" style="margin-top:44px"><span class="a">Desde</span><span class="b">Donde</span><span class="c">Estés</span></div>
<div class="gancho">Querer ayudar y no saber cómo<br>es de las cosas más incómodas<br>que hay. <b>Esto es para eso.</b></div>
"""))

ES.append(("lo-que-paso", """
<div class="ceja"><i>01</i>Lo que pasó</div>
<h2>Un sismo de magnitud 7,4 a 5&nbsp;km de San José del Palmar, Chocó.</h2>
<div class="regla"></div>
<div class="rej">
 <div><b>288</b><span>fallecidos</span></div>
 <div><b>202</b><span>desaparecidos</span></div>
 <div><b>4.018</b><span>heridos</span></div>
 <div><b>145.601</b><span>personas afectadas</span></div>
 <div><b>448</b><span>municipios</span></div>
 <div><b>12.504</b><span>viviendas destruidas</span></div>
</div>
<div class="crece"></div>
<div class="nota">Balance de la UNGRD con corte al 15 de agosto de 2026. El epicentro fue el Chocó, un departamento con 30,8% de pobreza multidimensional frente a un promedio nacional de 9,9% (DANE).</div>
"""))

ES.append(("por-que", """
<div class="ceja"><i>02</i>Por qué existe esto</div>
<h2>Mucha gente quiere ayudar. Casi nadie sabe por dónde.</h2>
<p style="margin-top:36px">A quién darle. En quién confiar. Si lo que uno manda de verdad llega. Y si no tienes plata, la sensación es peor: parece que no tuvieras nada que dar.</p>
<div class="barra"><div class="cita">Esa mezcla incómoda fue la que terminó en esta página.</div></div>
"""))

ES.append(("que-es", """
<div class="ceja"><i>03</i>Qué es</div>
<h2>Una sola página con formas de ayudar, <em>verificadas una por una</em>.</h2>
<div class="datos">
 <div><b>403</b><span>hechos verificados</span></div>
 <div><b>254</b><span>fuentes</span></div>
 <div><b>30</b><span>formas concretas de ayudar</span></div>
</div>
<div class="crece"></div>
<div class="regla"></div>
<p style="font-size:28px">Funciona desde Colombia y desde afuera, en español y en inglés. <b>No recibe dinero ni administra donaciones:</b> lleva a los canales oficiales de cada organización.</p>
"""))

ES.append(("como-funciona-puertas", """
<div class="ceja"><i>04</i>Cómo funciona</div>
<h2>Se entra por lo que sí tienes.</h2>
<ul class="puertas" style="margin-top:32px">
 <li><i>01</i><div><b>Tu oficio</b><span>Lo que sabes hacer. Varias cosas, desde cualquier país</span></div></li>
 <li><i>02</i><div><b>Dinero</b><span>18 organizaciones colombianas verificadas</span></div></li>
 <li><i>03</i><div><b>Tu tiempo</b><span>Voluntariado, con o sin experiencia</span></div></li>
 <li><i>04</i><div><b>Cosas</b><span>Qué llevar, dónde, y qué no sirve</span></div></li>
 <li><i>05</i><div><b>Comprando</b><span>Negocios que donan lo que venden</span></div></li>
 <li><i>06</i><div><b>Tu voz</b><span>Difundir lo verificado y frenar lo falso</span></div></li>
</ul>
"""))

ES.append(("como-funciona-regla", """
<div class="ceja"><i>04</i>Cómo funciona</div>
<h2>Cada cosa lleva la fuente de donde salió.</h2>
<p style="margin-top:36px">Nada entra sin un enlace que cualquiera pueda abrir y revisar, <b>ni siquiera lo nuestro</b>. Si un dato no se puede verificar, no se publica: hay 77 cosas descartadas y está escrito por qué.</p>
<div class="barra"><div class="cita">Los enlaces se revisan solos todos los días. Si uno se cae, se arregla.</div></div>
"""))

ES.append(("lo-que-falta", """
<div class="ceja"><i>05</i>Lo que falta</div>
<h2>Esto se hizo rápido, <span class="r">y se nota</span>.</h2>
<p style="margin-top:36px">Salió al aire en pocos días porque valía más servir a tiempo que salir completo. Faltan fundaciones, negocios de barrio, colectas que nunca salieron en un medio.</p>
<div class="barra"><div class="cita">Que algo no esté aquí no significa que no exista. Significa que no lo hemos encontrado.</div></div>
"""))

ES.append(("como-ayudar", """
<div class="ceja"><i>06</i>En qué ayuda más</div>
<h2>Tres cosas, y ninguna cuesta plata.</h2>
<ul class="pasos">
 <li><i>1</i><div><b>Compártela</b><span>Una herramienta así solo sirve si le llega a quien la necesita. Ese es el favor.</span></div></li>
 <li><i>2</i><div><b>Suma lo que falta</b><span>Si sabes de alguien que está ayudando, o eres tú, mándalo con un enlace. Lo verificamos y entra con su fuente.</span></div></li>
 <li><i>3</i><div><b>Manda el video</b><span>Si viste a alguien ayudando, mándanos el enlace. Entra con crédito a quien lo publicó.</span></div></li>
</ul>
<div class="crece"></div>
<div class="regla"></div>
<p style="font-size:28px">Todo llega al mismo lugar: <b>desdedondeestes@outlook.com</b></p>
"""))

ES.append(("cierre", f"""
<div class="mapa" style="opacity:.11">{MAPA}</div>
<div class="cierre">
 <div class="ceja">Desde Colombia o desde donde estés</div>
 <h2 style="margin-top:26px">Recuerda compartirla.</h2>
 <p style="max-width:820px;margin-top:26px">Esto solo funciona si entre todos ponemos un grano de arena. <b>Compartirla es el grano que no le cuesta nada a nadie.</b></p>
 <div class="url-grande">desdedondeestes.co</div>
 <div class="correo">¿Falta algo? Escríbenos:<br><b>desdedondeestes@outlook.com</b></div>
</div>
"""))


# ---------------------------------------------------------------- contenido EN
EN = []

EN.append(("portada", f"""
<div class="mapa">{MAPA}</div>
<div class="ceja">10 August 2026 · Earthquake in Colombia</div>
<div class="mk" style="margin-top:44px"><span class="a">From</span><span class="b">Wherever</span><span class="c">You Are</span></div>
<div class="gancho">Wanting to help and not knowing<br>how is one of the worst feelings<br>there is. <b>This is for that.</b></div>
"""))

EN.append(("lo-que-paso", """
<div class="ceja"><i>01</i>What happened</div>
<h2>A magnitude 7.4 quake, 5&nbsp;km from San José del Palmar, Chocó.</h2>
<div class="regla"></div>
<div class="rej">
 <div><b>288</b><span>dead</span></div>
 <div><b>202</b><span>missing</span></div>
 <div><b>4,018</b><span>injured</span></div>
 <div><b>145,601</b><span>people affected</span></div>
 <div><b>448</b><span>municipalities</span></div>
 <div><b>12,504</b><span>homes destroyed</span></div>
</div>
<div class="crece"></div>
<div class="nota">Figures from Colombia's national disaster agency (UNGRD) as of 15 August 2026. The epicentre was in Chocó, a department where 30.8% of people live in multidimensional poverty against a national average of 9.9% (DANE).</div>
"""))

EN.append(("por-que", """
<div class="ceja"><i>02</i>Why this exists</div>
<h2>Plenty of people want to help. Almost nobody knows where to start.</h2>
<p style="margin-top:36px">Who to give to. Who to trust. Whether what you send actually arrives. And if you have no money, it feels worse: as if you had nothing to give at all.</p>
<div class="barra"><div class="cita">That uncomfortable mix is what ended up as this page.</div></div>
"""))

EN.append(("que-es", """
<div class="ceja"><i>03</i>What it is</div>
<h2>One page of ways to help, <em>verified one by one</em>.</h2>
<div class="datos">
 <div><b>403</b><span>verified facts</span></div>
 <div><b>254</b><span>sources</span></div>
 <div><b>30</b><span>concrete ways to help</span></div>
</div>
<div class="crece"></div>
<div class="regla"></div>
<p style="font-size:28px">It works from Colombia and from anywhere else, in Spanish and English. <b>It takes no money and manages no donations:</b> it links to each organisation's own official channels.</p>
"""))

EN.append(("como-funciona-puertas", """
<div class="ceja"><i>04</i>How it works</div>
<h2>You come in through what you do have.</h2>
<ul class="puertas" style="margin-top:32px">
 <li><i>01</i><div><b>Your profession</b><span>What you know how to do. Some of it from anywhere</span></div></li>
 <li><i>02</i><div><b>Money</b><span>18 Colombian organisations, verified one by one</span></div></li>
 <li><i>03</i><div><b>Your time</b><span>Volunteering, with or without experience</span></div></li>
 <li><i>04</i><div><b>Things</b><span>What to bring, where, and what does not help</span></div></li>
 <li><i>05</i><div><b>By buying</b><span>Shops giving away what they sell</span></div></li>
 <li><i>06</i><div><b>Your voice</b><span>Spread what is verified, stop what is false</span></div></li>
</ul>
"""))

EN.append(("como-funciona-regla", """
<div class="ceja"><i>04</i>How it works</div>
<h2>Everything carries the source it came from.</h2>
<p style="margin-top:36px">Nothing goes in without a link anyone can open and check, <b>not even our own claims</b>. If something cannot be verified, it is not published: 77 items were discarded and the reason is written down.</p>
<div class="barra"><div class="cita">The links are checked automatically every day. If one breaks, it gets fixed.</div></div>
"""))

EN.append(("lo-que-falta", """
<div class="ceja"><i>05</i>What is missing</div>
<h2>This was built fast, <span class="r">and it shows</span>.</h2>
<p style="margin-top:36px">It went live in days because being useful in time mattered more than being complete. Foundations are missing, neighbourhood businesses, collections that never made the news.</p>
<div class="barra"><div class="cita">Something not being here does not mean it does not exist. It means we have not found it.</div></div>
"""))

EN.append(("como-ayudar", """
<div class="ceja"><i>06</i>What helps most</div>
<h2>Three things, and none of them cost money.</h2>
<ul class="pasos">
 <li><i>1</i><div><b>Share it</b><span>A tool like this only works if it reaches the people who need it. That is the favour.</span></div></li>
 <li><i>2</i><div><b>Add what is missing</b><span>If you know someone who is helping, or it is you, send it with a link. We verify it and it goes in with its source.</span></div></li>
 <li><i>3</i><div><b>Send the video</b><span>If you saw someone helping, send us the link. It goes in crediting whoever posted it.</span></div></li>
</ul>
<div class="crece"></div>
<div class="regla"></div>
<p style="font-size:28px">It all goes to the same place: <b>desdedondeestes@outlook.com</b></p>
"""))

EN.append(("cierre", f"""
<div class="mapa" style="opacity:.11">{MAPA}</div>
<div class="cierre">
 <div class="ceja">From Colombia or from wherever you are</div>
 <h2 style="margin-top:26px">Remember to share it.</h2>
 <p style="max-width:820px;margin-top:26px">This only works if each of us does our small part. <b>Sharing it is the part that costs nobody anything.</b></p>
 <div class="url-grande">desdedondeestes.co</div>
 <div class="correo">Something missing? Write to us:<br><b>desdedondeestes@outlook.com</b></div>
</div>
"""))


def construir(lista, sufijo):
    salida = A / ("piezas-en" if sufijo == "en" else "piezas")
    salida.mkdir(exist_ok=True)
    n = len(lista)
    rutas = []
    for i, (nombre, cuerpo) in enumerate(lista, start=1):
        centradas = {"por-que", "como-funciona-regla", "lo-que-falta"}
        clase = "portada" if i == 1 else ("centro" if nombre in centradas else "")
        html = pieza(cuerpo, str(i).zfill(2), str(n).zfill(2), url=(i != n), clase=clase)
        f = salida / f"{str(i).zfill(2)}-{nombre}.html"
        f.write_text(html, encoding="utf-8")
        rutas.append((f, salida / f"{str(i).zfill(2)}-{nombre}.jpg"))
    return rutas


def render(rutas):
    guion = """
const {chromium} = require('/root/colombia-help/node_modules/playwright-core');
(async () => {
  const b = await chromium.launch({executablePath: process.env.CHROME});
  const p = await b.newPage({viewport:{width:1080,height:1350}, deviceScaleFactor:1});
  const pares = JSON.parse(process.env.PARES);
  for (const [src, dst] of pares) {
    await p.goto('file://' + src);
    await p.waitForTimeout(120);
    await p.screenshot({path: dst, type:'jpeg', quality: 92});
    console.log(dst);
  }
  await b.close();
})();
"""
    (A / "_render.js").write_text(guion, encoding="utf-8")
    env = {"CHROME": CHROME, "PARES": json.dumps([[str(a), str(b)] for a, b in rutas]),
           "PATH": "/usr/bin:/bin:/usr/local/bin", "HOME": "/root"}
    r = subprocess.run(["node", str(A / "_render.js")], capture_output=True, text=True, env=env)
    print(r.stdout or r.stderr[-2000:])


if __name__ == "__main__":
    if "--en" in sys.argv:
        render(construir(EN, "en"))
    else:
        render(construir(ES, "es"))
        if "--ambos" in sys.argv:
            render(construir(EN, "en"))
