# Brief para Claude Design · "Desde Donde Estés"

> Todo lo que necesitas para diseñar esta página está en este documento. Los textos son
> definitivos y verificados: **no los reescribas, no los resumas y no toques ninguna cifra.**
> Lo que sí queremos de ti es la propuesta visual completa, con libertad.

---

## 1. Qué es esto

Una página que reúne formas verificadas de ayudar tras el terremoto de magnitud 7,4 del
10 de agosto de 2026 en Colombia (epicentro 5 km al sur de San José del Palmar, Chocó; golpeó
Chocó, Buenaventura, Valle del Cauca, Cali y el Eje Cafetero).

No es un sitio de donaciones. No recibe dinero, no procesa pagos, no administra nada. Es un
sitio que **muestra lo que ya está pasando** y le da a cada visitante una puerta de entrada
según lo que tenga para dar.

**El héroe no es una organización ni el autor: es todo el que se une.** Colombianos y
extranjeros, personas y empresas, presentes y a distancia. Eso tiene una consecuencia de
diseño que importa: la palabra "todos" casi no aparece escrita. Se muestran muchos casos
singulares con nombre y la suma la hace el lector. Un país del Golfo y una niña de Sabaneta
con una alcancía, sin que ninguno de los dos se vea más importante que el otro.

**Está escrito en agradecimiento, no en petición.** Todos los sitios de donación del mundo
piden. Este da las gracias. Esa es la gramática de la página entera.

**Contexto emocional que manda sobre el diseño:** Colombia acaba de pasar una elección que
partió el país por la mitad, y mucha gente está usando la emergencia para pelear. Este sitio
no juzga, no señala, no toma partido y no evalúa a ningún gobierno. La prueba que aplicamos a
cada decisión: *¿alguien que votó distinto se sigue sintiendo invitado?* El diseño tiene que
pasar esa misma prueba.

Y hay otro público, igual de importante: **gente que quiere ayudar, no sabe cómo, y se siente
culpable por no saber.** La página no está para quitarles la excusa. Está para quitarles la
culpa y darles una herramienta.

---

## 2. Qué queremos de ti (y qué no)

**Queremos una propuesta visual completa, con libertad.** Puedes cambiar layout, tipografía,
color, ritmo, jerarquía y componentes. Propón: para eso te estamos escribiendo.

**Entrega esperada:** un archivo HTML autocontenido, con estos mismos textos reales dentro,
que funcione como maqueta navegable. No lo conectes a datos ni inventes contenido de relleno:
usa las muestras que te damos y repítelas si necesitas llenar una grilla, marcando claramente
que es repetición.

**Lo que se respeta sin discusión:**

1. Los cinco movimientos de la historia y su orden (sección 4). La estructura no es capricho,
   es una directiva narrativa ya acordada.
2. Todos los textos, tal cual. Si un texto te estorba visualmente, dilo en una nota, no lo
   cambies.
3. Todas las cifras, exactas. Cada una está verificada contra una fuente pública. Cambiar un
   número, redondearlo o inventar uno para que quede bonito destruye lo único que sostiene
   este proyecto.
4. Cada tarjeta de hecho lleva visible su fuente y su fecha. No es un detalle legal: es el
   producto.

---

## 3. Dirección visual pedida

**Que transmita calma, calidez y paz.** Es lo contrario de un sitio de emergencia. Nada de
rojos de alerta a pantalla completa, contadores regresivos, urgencia falsa ni fotos de
catástrofe.

**Los colores de la bandera (amarillo, azul, rojo) van como acento, no como bloque.** Hoy el
sitio usa un azul `#132A4D` en secciones enteras y cansa la vista: eso es exactamente lo que
hay que resolver. Piensa en el amarillo como luz cálida, no como señal de advertencia; en el
azul como reposo, no como corporativo; y en el rojo con cuentagotas.

Paleta actual, como punto de partida y no como obligación:

```
--amarillo:#F2C230   --amarillo-claro:#FBE9AE   --amarillo-hondo:#8A6A0E
--azul:#12356B       --azul-hondo:#132A4D   ← este es el que molesta
--rojo:#C4362B       --rojo-suave:#F7E7E4
--papel:#FBF8F1      --papel-2:#F3EDE0
--tinta:#16203A      --tinta-2:#4A5670      --tinta-3:#818CA4
--verde:#2F6B4F      --verde-suave:#E8F2EC  ← sección para afectados
--linea:#E4DCCB      --linea-2:#CFC5AF
```

### Tres palabras, tres colores

El nombre tiene tres palabras y la bandera tiene tres colores. **Queremos que esa coincidencia
sea el ancla del diseño.**

```
DESDE   →  amarillo
DONDE   →  azul
ESTÉS   →  rojo
```

En ese orden, que es el orden de la bandera de arriba abajo. La idea nos gusta porque el
nombre ya dice lo que el sitio hace, y esto lo vuelve visible sin explicarlo: tres palabras,
tres colores, un país.

Dónde puede vivir esa idea, además del logotipo: en la marca de la barra superior, en el
titular de apertura, en los tres momentos del marcador de fase, en cómo se colorean los
acentos de las secciones, en la franja superior, en el favicon, en la imagen de previsualización
que sale cuando alguien comparte el enlace por WhatsApp. Propón tú dónde funciona mejor.

Tres cosas que hay que resolver bien y por eso te las señalamos:

1. **Las proporciones de la bandera no son iguales.** El amarillo ocupa la mitad, el azul y el
   rojo un cuarto cada uno. Si trasladas eso literalmente al peso visual de los tres colores en
   la página, probablemente funcione mejor que repartirlos en tercios.
2. **El nombre en inglés tiene cuatro palabras: *From Wherever You Are*.** Se puede agrupar en
   tres unidades (`From / Wherever / You Are`), pero necesitamos que en inglés no se sienta
   forzado ni roto. Si te parece que ahí el recurso no aguanta, dilo y propón cómo se comporta
   la marca en inglés.
3. **Que no se vuelva un truco.** Si los tres colores aparecen en cada título, cada botón y
   cada tarjeta, deja de ser una idea y se vuelve ruido, y además rompe la calma que pedimos.
   Buscamos que se lea una vez, fuerte y claro, y que después el resto de la página respire.

**Fuera los "eyebrow": esas etiquetitas en mayúsculas sobre cada título.** Hoy hay una en
cada sección y se sienten generadas por IA. Elimínalas o resuelve la jerarquía de otra
manera: un título que se explique solo, un número, un cambio de fondo, un filete. Si crees
que alguna sección de verdad las necesita, argumenta por qué en una nota.

**Otros antipatrones a evitar:** gradientes de dashboard, glassmorphism, sombras flotantes
por todas partes, emojis, iconografía genérica de stock, animaciones que exigen atención,
tipografía de startup. El registro es más cercano a una publicación editorial cuidada que a
una landing page.

**Sí funciona bien hoy y vale la pena conservar en espíritu:** el papel cálido de fondo, la
serif del titular de apertura, y que las tarjetas se sientan como fichas de archivo con su
fuente al pie.

**No hay fotos.** Decisión tomada: no se usan imágenes generadas con IA (una foto inventada
de un evento real destruiría la credibilidad de 403 hechos verificados) y no usamos fotos de
prensa porque dar crédito no es una licencia. Así que el diseño se sostiene con tipografía,
color, espacio y gráficos dibujados en código. Si propones ilustración abstracta o formas
geométricas, adelante, siempre que no simulen documentar nada real.

**Móvil primero.** La mayoría va a llegar por un enlace de WhatsApp, en un teléfono, y
posiblemente con datos limitados y en la calle.

**Accesibilidad:** contraste AA como mínimo, foco visible en teclado, y que nada dependa solo
del color para entenderse.

---

## 4. Arquitectura: los cinco movimientos

En este orden. Entre paréntesis, la función narrativa de cada uno.

1. **Lo que se cayó** (apertura) — El texto de agradecimiento y la frase de la abundancia.
   Sin nombre de autor, por decisión expresa.
2. **Lo que llevamos** (logro colectivo) — Las cifras de lo que se ha hecho, no las de la
   pérdida. Abre con lo logrado, a propósito.
3. **Quiénes somos "todos"** (el corazón) — La cadena de casos singulares, con filtros y con
   reels de Instagram intercalados. Es la sección más larga y la más importante.
4. **Lo que falta aquí** (honestidad) — La sección que admite que la lista está incompleta e
   invita a sumar. Es nueva y es central para el proyecto: no la trates como pie de página.
5. **Dónde estamos hoy** (fase) — Rescate / atención humanitaria / reconstrucción. Aquí viven
   las cifras de pérdida, como contexto, nunca como titular.
6. **Las puertas** (acción) — "¿Qué puedes dar?" con seis ejes desplegables.
7. **Si el terremoto te afectó** (para las víctimas, no para quien ayuda) — Recursos gratuitos.
   Va en verde suave para separarla claramente del resto.
8. **Lo que falta** (la brecha) — El medidor de lo donado contra el costo de la reconstrucción.
9. **Lo que todavía puedes alcanzar** (futuro) — Conciertos que aún no han pasado.
10. **Cómo se hizo esto** (transparencia) — Doce entradas en acordeón, incluida quién está
    detrás y los errores que cometimos.
11. **Pie** — Qué no hace el sitio, correo de contacto, fuentes principales.

Hay además una **barra superior fija** con: marca, interruptor ES/EN, interruptor "Estoy en
Colombia / Estoy fuera", y un botón "Quiero ayudar".

Y una **franja de frescura** arriba del todo que dice cuándo se verificaron los datos y
avisa si ya pasaron muchos días.

---

## 5. Componentes a diseñar

| # | Componente | Notas |
|---|---|---|
| 1 | Barra superior | Dos interruptores de dos estados + botón. Se apila en móvil. |
| 2 | Franja de frescura | Dos estados: fresco y viejo (advertencia). |
| 3 | Apertura | Serif grande, cita de agradecimiento, frase de abundancia, dos botones. |
| 4 | Tarjeta de cifra | Número grande + texto + fuente enlazada. Van 4 a 6 en grilla. |
| 5 | Chips de filtro | Cuatro estados: todos / desde Colombia / desde el exterior / personas. |
| 6 | Tarjeta de hecho | Quien, cifra destacada, qué hizo, y al pie: origen, fecha, fuente enlazada. Tiene variante ancha (`grande`) y tres colores de cifra. Van 46 en la grilla. |
| 7 | Tarjeta de reel | Portada oscura con botón de play. El iframe de Instagram **solo se carga al hacer clic**, nunca antes. Lleva un pie de texto y un enlace "abrir en Instagram". |
| 8 | Sección "lo que falta aquí" | Texto + un botón que abre el correo. Tiene que sentirse como una invitación cálida, no como un aviso legal. |
| 9 | Marcador de fase | Tres pasos, uno activo. |
| 10 | Ejes de "qué puedes dar" | Seis botones grandes con icono, nombre y descripción; al tocar uno se despliega un panel de opciones debajo. Arranca abierto en "Mi oficio", no en Dinero, para que quien no tiene plata no se sienta inútil en el primer segundo. |
| 11 | Tarjeta de opción | Etiqueta ("Desde cualquier país" / "Presencial en Colombia"), nombre, descripción, botón de acción, fuente. Hay una variante `aviso` para advertencias. |
| 12 | Tarjeta de recurso | Para la sección verde de afectados. |
| 13 | Medidor de brecha | Barra proporcional con dos leyendas y un párrafo explicativo. |
| 14 | Tarjeta de concierto | Fecha, nombre, lugar, artistas, destino del dinero, precio. Estado extra: "ya pasó". |
| 15 | Acordeón de transparencia | Doce entradas, texto largo, tiene que invitar a leerse. |
| 16 | Pie | Tres párrafos y una lista de 14 fuentes. |

---

## 6. Comportamientos que el diseño tiene que soportar

- **Bilingüe ES/EN completo.** No solo la interfaz: también las descripciones. El inglés es
  más largo en promedio; que nada se rompa. En inglés, las cifras propias van en dólares.
- **Detección de ubicación por zona horaria del navegador**, leída localmente. Sin cookies,
  sin IP, sin terceros. Cambia qué canales de donación se muestran primero (una llave Bre-B no
  le sirve a nadie en Londres). **Los hechos nunca se filtran por ubicación**: si sabemos que
  estás en España, lo hecho desde España sube, pero todo lo demás sigue ahí.
- **"Ver más"** en la cadena: arranca con 12 tarjetas y va cargando.
- **Filtros** que reordenan la cadena sin ocultar nada.
- **Los reels no cargan código de Meta hasta que el usuario hace clic.** Es una decisión de
  privacidad, no una optimización.

---

## 7. Volumen real de contenido

| Cosa | Cantidad |
|---|---|
| Hechos verificados en la base | 403, de 254 fuentes distintas |
| Hechos visibles en la cadena | 46 |
| Reels | 3 hoy, van a ser más |
| Cifras de portada | 4 |
| Ejes de "qué puedes dar" | 6 |
| Opciones dentro de los ejes | 27 |
| Recursos para afectados | 5 |
| Conciertos | 5 |
| Entradas de transparencia | 12 |
| Fuentes en el pie | 14 |

---

## 8. Todos los textos de interfaz, ES y EN

Bloque literal del sitio actual. Las claves te dicen dónde va cada cadena.

```js
var T = {
   es:{
    m_co:'Estoy en Colombia', m_intl:'Estoy fuera', cta:'Quiero ayudar',
    kicker:'10 de agosto de 2026 · San José del Palmar, Chocó',
    gracias:'En situaciones como esta, las máscaras y las diferencias desaparecen. Solo queda algo mucho más poderoso: <b>la solidaridad, el amor por el prójimo y las ganas de ayudar.</b>',
    firma:'Gracias a todos los que están aportando, ayudando y acompañando de cualquier manera.',
    posib:'Hoy hay <b>un mundo de formas de ayudar</b> a quienes más lo necesitan. Aquí están reunidas <b>algunas</b>, para que encuentres la tuya. Faltan muchas, y por eso esto se sigue construyendo entre todos.',
    cta1:'Encontrar mi forma de ayudar →', cta2:'Ver quiénes se están uniendo',
    e_llev:'Lo que llevamos entre todos', h_llev:'Esto no lo hizo nadie solo',
    e_cad:'Quiénes somos "todos"', h_cad:'Un país del Golfo y una barbería de Boston',
    s_cad:'No hay orden por tamaño. A propósito. Cada tarjeta lleva la fuente que la respalda.',
    f_todos:'Todos', f_col:'Desde Colombia', f_ext:'Desde el exterior', f_gente:'Personas y comunidades',
    mas:'Ver más', menos:'Ver menos',
    e_sum:'Lo que falta aquí', h_sum:'Esta lista está incompleta, y no lo escondemos',
    s_sum:'Este sitio se construyó rápido, a propósito: valía más salir a tiempo que salir completo.',
    p_sum:'Seguro falta la fundación de tu barrio, la empresa que está mandando camiones, el grupo de amigos que armó una colecta, la marca que está donando lo que vende. No es que no cuenten: <b>es que todavía no los hemos encontrado.</b> Si sabes de alguien que está ayudando, o eres tú, cuéntanos y lo verificamos para sumarlo.',
    n_sum:'Pedimos una sola cosa: un enlace o una fuente que podamos revisar. Nada entra sin eso, ni siquiera lo nuestro. Escribir no compromete a nadie ni cuesta nada.',
    b_sum:'Contarnos cómo estás ayudando →',
    asu:'Quiero sumar una forma de ayudar',
    bsu:'Cuéntanos, en las palabras que quieras:\n\n1) Quién está ayudando (persona, negocio, fundación, colectivo)\n2) Qué está haciendo exactamente\n3) Un enlace o una fuente donde podamos verificarlo (nota de prensa, publicación de la propia cuenta, sitio web)\n4) Ciudad o zona\n\nGracias por tomarte el tiempo. Lo revisamos y, si se puede verificar, entra con su fuente.',
    e_hoy:'Dónde estamos hoy', h_hoy:'El rescate termina. Empieza lo largo.',
    s_hoy:'La atención del mundo dura semanas. La reconstrucción, años.',
    fases:['Rescate','Atención humanitaria','Reconstrucción'],
    e_dar:'Encuentra tu forma', h_dar:'¿Qué puedes dar?',
    s_dar:'No todo se ayuda con plata. Toca lo que tengas y se despliegan las opciones verificadas.',
    e_afe:'Si el terremoto te afectó', h_afe:'Esto es para ti, no para quien ayuda',
    s_afe:'Servicios gratuitos verificados para quienes perdieron algo. Ninguno cobra.',
    e_bre:'Lo que falta', h_bre:'Lo donado es histórico. Y no alcanza.',
    s_bre:'Las dos cosas son ciertas al mismo tiempo, y por eso esto no puede parar cuando se vayan las cámaras.',
    expl:'<b>Y está bien que no alcance.</b> La donación privada representa cerca del 5% del financiamiento proyectado de la reconstrucción. El resto sale del presupuesto público y de la cooperación internacional. Lo privado no es lo que más pesa: <b>es lo que llega primero</b>, mientras lo demás se tramita.',
    e_con:'Lo que todavía puedes alcanzar', h_con:'Conciertos que aún no pasan',
    s_con:'Casi todo lo demás en esta página ya ocurrió. Esto no.',
    e_tra:'Cómo se hizo esto', h_tra:'Lo que puedes revisar y lo que no pudimos verificar',
    s_tra:'La única razón para confiar en una lista es poder auditarla.',
    f1:'<b>Este sitio no recibe dinero, no procesa pagos y no administra donaciones.</b> Solo enlaza a los canales oficiales de cada organización, y cada dato lleva su fuente y su fecha.',
    f3:'Proyecto ciudadano independiente. Escríbenos a <a href="mailto:'+CORREO+'">'+CORREO+'</a> si quieres sumar una forma de ayudar, corregir un dato o pedir que retiremos algo.',
    f_src:'Fuentes principales', pasado:'Ya pasó', desde:'Desde',
    reelplay:'Ver el reel', reelsub:'Se carga desde Instagram solo cuando le das clic', reelopen:'Abrir en Instagram',
    stale:'Estos datos se verificaron el {d}, hace {n} días. Las cifras oficiales cambian rápido: confirma en la fuente antes de transferir.',
    fresco:'Datos verificados el {d}. Cada cifra enlaza a su fuente.'
   },
   en:{
    m_co:"I'm in Colombia", m_intl:"I'm abroad", cta:'I want to help',
    kicker:'August 10, 2026 · San José del Palmar, Chocó',
    gracias:'In moments like this, the masks and the differences fall away. What is left is something far more powerful: <b>solidarity, love for one another, and the will to help.</b>',
    firma:'Thank you to everyone who is giving, helping and standing alongside, in whatever way they can.',
    posib:'There is <b>a whole world of ways to help</b> the people who need it most. <b>Some</b> of them are gathered here, so you can find yours. Many are missing, which is why this keeps being built by all of us.',
    cta1:'Find my way to help →', cta2:'See who is stepping up',
    e_llev:'What we have done together', h_llev:'No one did this alone',
    e_cad:'Who "everyone" actually is', h_cad:'A Gulf state and a barbershop in Boston',
    s_cad:'Nothing is ordered by size. On purpose. Every card carries the source that backs it.',
    f_todos:'All', f_col:'From Colombia', f_ext:'From abroad', f_gente:'People and communities',
    mas:'Show more', menos:'Show less',
    e_sum:'What is missing here', h_sum:'This list is incomplete, and we are not hiding it',
    s_sum:'This site was built fast, on purpose: getting it out in time mattered more than getting it complete.',
    p_sum:'The foundation on your street is probably missing. So is the company sending trucks, the group of friends who ran a collection, the brand giving away what it sells. It is not that they do not count: <b>it is that we have not found them yet.</b> If you know someone who is helping, or it is you, tell us and we will verify it and add it.',
    n_sum:'We ask for one thing only: a link or a source we can check. Nothing goes in without that, not even our own material. Writing to us commits you to nothing.',
    b_sum:'Tell us how you are helping →',
    asu:'I want to add a way of helping',
    bsu:'Tell us, in whatever words you like:\n\n1) Who is helping (person, business, foundation, collective)\n2) What exactly they are doing\n3) A link or source where we can verify it (news article, a post from their own account, a website)\n4) City or area\n\nThank you for taking the time. We check it, and if it can be verified, it goes in with its source.',
    e_hoy:'Where things stand today', h_hoy:'The rescue is ending. The long part begins.',
    s_hoy:"The world's attention lasts weeks. Rebuilding takes years.",
    fases:['Rescue','Humanitarian relief','Reconstruction'],
    e_dar:'Find your way in', h_dar:'What can you give?',
    s_dar:'Not everything is helped with money. Tap what you have and the verified options open up.',
    e_afe:'If the earthquake affected you', h_afe:'This part is for you, not for the helpers',
    s_afe:'Verified free services for people who lost something. None of them charge.',
    e_bre:'What is still missing', h_bre:'What has been given is historic. And it is not enough.',
    s_bre:'Both things are true at once, and that is exactly why this cannot stop when the cameras leave.',
    expl:'<b>And it is fine that it is not enough.</b> Private donations are expected to cover around 5% of the financing for reconstruction. The rest comes from the public budget and international cooperation. Private giving is not the biggest share: <b>it is the share that arrives first</b>, while everything else is still being processed.',
    e_con:'What you can still catch', h_con:'Concerts that have not happened yet',
    s_con:'Almost everything else on this page already happened. These have not.',
    e_tra:'How this was made', h_tra:'What you can check, and what we could not verify',
    s_tra:'The only reason to trust a list is being able to audit it.',
    f1:'<b>This site takes no money, processes no payments and manages no donations.</b> It only links to each organisation\\u2019s official channels, and every figure carries its source and its date. Amounts we write ourselves are converted to US dollars at COP $3,128.65 per dollar, the Banco de la República rate for 15 August 2026. Figures quoted from news sources are left exactly as those sources published them.',
    f3:'Independent citizen project. Write to <a href="mailto:'+CORREO+'">'+CORREO+'</a> to add a way of helping, correct a figure, or ask us to take something down.',
    f_src:'Main sources', pasado:'Already happened', desde:'From',
    reelplay:'Play the reel', reelsub:'Loads from Instagram only when you click', reelopen:'Open on Instagram',
    stale:'This data was verified on {d}, {n} days ago. Official figures change fast: check the source before transferring.',
    fresco:'Verified on {d}. Every figure links to its source.'
   }
  };
```

---

## 9. Las seis puertas de "¿Qué puedes dar?", con todo su contenido

### Eje `dinero` — Dinero · lo que llega primero  /  EN: Money · the part that arrives first
- **Adopta un Hogar** — Reconstrucción de vivienda en Chocó, Valle y Eje Cafetero. La Fundación Grupo Argos y Nicky Jam duplican cada peso que pongas, hasta $26.000 millones.
  - EN: **Adopta un Hogar** — Rebuilding homes in Chocó, Valle del Cauca and the Coffee Region. Grupo Argos Foundation and Nicky Jam match every peso, up to about US$8.3 million (COP $26 billion).
  - botón: `Ir a donar →` / `Go to donate →` · fuente: Semana + El Tiempo + sitio oficial
- **Cruz Roja Colombiana** — Salud de emergencia, agua, rescate y reunificación familiar. Campaña #TodosPorColombia, desde $10.000.
  - EN: **Colombian Red Cross** — Emergency healthcare, water, rescue and family reunification. #TodosPorColombia campaign, from about US$3 (COP $10,000).
  - botón: `Ir a donar →` / `Go to donate →` · fuente: El Colombiano + sitio oficial
- **Fundación PLAN** — Alojamiento temporal, agua segura, protección infantil y transferencias monetarias en Chocó. Tiene portal aparte para donantes fuera de Colombia.
  - EN: **Fundación PLAN** — Temporary shelter, safe water, child protection and cash transfers in Chocó. Separate portal for donors outside Colombia.
  - botón: `Ir a donar →` / `Go to donate →` · fuente: Cablenoticias + sitio oficial
- **Una Garra por Colombia** — 32 refugios de animales colapsados o en riesgo y unos 1.870 perros y gatos. Teja, cemento, malla, alimento y medicinas.
  - EN: **Una Garra por Colombia** — 32 animal shelters collapsed or at risk and around 1,870 dogs and cats. Roofing, cement, mesh, food and medicine.
  - botón: `Ir a la vaki →` / `Go to the fundraiser →` · fuente: Noticias RCN + Infobae
- **ABACO · Bancos de Alimentos** — Red nacional de bancos de alimentos. Acepta transferencia internacional a Bancolombia con NIT 900326456-1.
  - EN: **ABACO · Food Banks** — National food bank network. Accepts international wires to Bancolombia, tax ID 900326456-1.
  - botón: `Ir a donar →` / `Go to donate →` · fuente: Cablenoticias + El Colombiano
- **Gobernación del Chocó** — Cuenta oficial del departamento donde estuvo el epicentro. Banco de Bogotá, ahorros 578818429, NIT 891.680.010-3.
  - EN: **Chocó regional government** — Official account of the department where the epicentre was. Banco de Bogotá savings 578818429, tax ID 891.680.010-3.
  - botón: `Ver los datos de la cuenta →` / `See the account details →` · fuente: El Colombiano
- **ProPacífico · Colombia Unida** — Administra los fondos de la alianza del sector privado con la Alcaldía de Cali y la Gobernación del Valle. Acepta pagos nacionales e internacionales.
  - EN: **ProPacífico · Colombia Unida** — Manages the funds of the private sector alliance with the Cali and Valle governments. Accepts national and international payments.
  - botón: `Ver cómo aportar →` / `See how to give →` · fuente: Occidente + El País de Cali

### Eje `oficio` — Tu oficio · lo que sabes hacer  /  EN: Your profession · what you know how to do
- **SismoAyuda Colombia** — Si eres ingeniero estructural, civil o arquitecto: revisas fotos de viviendas dañadas y emites evaluación técnica siguiendo ATC-20 y EMS-98. Todo remoto. Son orientaciones preliminares y no reemplazan la inspección oficial.
  - EN: **SismoAyuda Colombia** — If you are a structural or civil engineer, or an architect: you review photos of damaged homes and issue a technical assessment following ATC-20 and EMS-98. Entirely remote. Preliminary guidance only; does not replace official inspection.
  - botón: `Registrarme como inspector →` / `Register as an inspector →` · fuente: Sitio oficial de la plataforma
- **Profesionales de la salud** — Convocatoria de la Asociación Colombiana de Sociedades Científicas y Assosalud. Prioritarios: cirugía, ortopedia y traumatología, medicina intensiva, pediatría, psiquiatría y psicología. Requiere viajar.
  - EN: **Health professionals** — Call from the Colombian Association of Scientific Societies and Assosalud. Priority areas: surgery, orthopaedics and trauma, intensive care, paediatrics, psychiatry and psychology. Requires travelling.
  - botón: `Ir al formulario →` / `Go to the form →` · fuente: El Tiempo · 11 ago
- **Ingenieros y arquitectos en Cali** — La Secretaría de Gestión del Riesgo convoca ingenieros civiles, estructurales y arquitectos para evaluar edificaciones. Punto de encuentro: Cruz Roja Seccional Valle, Cra. 38 Bis #5-91.
  - EN: **Engineers and architects in Cali** — Cali's risk management office is calling for civil and structural engineers and architects to assess buildings. Meeting point: Red Cross Valle branch, Cra. 38 Bis #5-91.
  - botón: `Ver la convocatoria →` / `See the call →` · fuente: El País de Cali · confirmar vigencia

### Eje `tiempo` — Tu tiempo · con o sin experiencia  /  EN: Your time · with or without experience
- **Cruz Roja Bogotá · inmediato** — Recibir, revisar, ordenar y empacar donaciones. Puntos en Usaquén (Calle 161A #7F-55) y la sede de la Carrera 24 #73-38, que opera 24 horas.
  - EN: **Red Cross Bogotá · immediate** — Receiving, checking, sorting and packing donations. Points at Usaquén (Calle 161A #7F-55) and the headquarters at Carrera 24 #73-38, open 24 hours.
  - botón: `Inscribirme →` / `Sign up →` · fuente: Alcaldía de Bogotá
- **terremotocolombia.co** — Plataforma ciudadana de código abierto. Formulario corto: nombre, teléfono, qué puedes ofrecer y en qué zona estás. Los coordinadores contactan después.
  - EN: **terremotocolombia.co** — Citizen-run, open source. Short form: name, phone, what you can offer and where you are. Coordinators follow up.
  - botón: `Ir al formulario →` / `Go to the form →` · fuente: Noticias RCN
- **El Minuto de Dios** — Formulario donde indicas tu disponibilidad por días y horas. No exige formación previa y ubican rápido.
  - EN: **El Minuto de Dios** — A form where you give your availability by day and hour. No prior training required and they place people quickly.
  - botón: `Ir al formulario →` / `Go to the form →` · fuente: Noticias RCN
- **Cruz Roja Ciclo IV · léelo antes** — El voluntariado formal de la Cruz Roja en Bogotá es otra cosa: cuesta $148.000 de inscripción más $345.000 del curso, y toma cuatro meses. No es ayuda de emergencia, es voluntariado de largo plazo. Lo incluimos para que nadie se lleve una sorpresa.
  - EN: **Red Cross Cycle IV · read this first** — The Red Cross formal volunteer programme in Bogotá is a different thing: about US$47 to register plus about US$110 for the course, over four months. It is not emergency help, it is long-term volunteering. We list it so no one is caught out.
  - botón: `Solo si buscas compromiso largo` / `Only if you want a long commitment` · fuente: Portafolio

### Eje `cosas` — Cosas · pero las correctas  /  EN: Things · but the right ones
- **Mapa vivo de acopio en Bogotá** — La Alcaldía mantiene un mapa interactivo con los puntos habilitados, horarios y qué necesita cada uno. Se actualiza a diario. Úsalo antes que cualquier lista fija, incluida esta.
  - EN: **Bogotá's live collection map** — The city keeps an interactive map of open collection points, hours and what each one needs. Updated daily. Use it before any fixed list, including this one.
  - botón: `Abrir el mapa · capa 127089 →` / `Open the map · layer 127089 →` · fuente: Alcaldía de Bogotá
- **ProPacífico recoge donde estés** — Piden sobre todo medicamentos e insumos médicos para Chocó, Tuluá y Quibdó. Carrera 4 # 22-07 en Cali, y si los llamas recogen la donación en tu ubicación.
  - EN: **ProPacífico will collect from you** — They mainly need medicines and medical supplies for Chocó, Tuluá and Quibdó. Carrera 4 # 22-07 in Cali, and if you call they will collect from you.
  - botón: `324 566 6775 · 312 833 8340 →` / `+57 324 566 6775 · +57 312 833 8340 →` · fuente: El País de Cali
- **Qué sí sirve y qué no** — Agua sellada, cobijas, enlatados de fácil apertura, pañales, gasas. Nada de perecederos, medicamentos empezados ni ropa usada en mal estado. Lo que no sirve ocupa bodega y transporte que hacen falta.
  - EN: **What helps and what does not** — Sealed water, blankets, easy-open tinned food, nappies, gauze. No perishables, no opened medication, no worn-out clothing. What does not help takes up storage and transport that is needed.
  - botón: `Ver la lista completa →` / `See the full list →` · fuente: Cruz Roja Colombiana vía Infobae
- **Acopio para animales · Corferias** — Alimento seco y húmedo, arena, guacales, collares, correas, gasas y antisépticos. Carrera 37 # 24-67, del 13 al 17 de agosto, de 10 a.m. a 6 p.m. Organiza el Idypba.
  - EN: **Animal donations · Corferias** — Dry and wet food, litter, carriers, collars, leads, gauze and antiseptics. Carrera 37 # 24-67, August 13 to 17, 10 a.m. to 6 p.m. Run by Bogotá's animal welfare institute.
  - botón: `Ver horarios y lista →` / `See hours and list →` · fuente: Infobae

### Eje `voz` — Tu voz · difundir lo cierto  /  EN: Your voice · spreading what is true
- **Comparte esta página** — Cada organización aquí está verificada contra su fuente. Mandarla es darle a alguien una lista en la que puede confiar, en vez de una cadena de WhatsApp sin origen.
  - EN: **Share this page** — Every organisation here is checked against its source. Sending it means giving someone a list they can trust, instead of an unsourced chain message.
  - botón: `Copiar el enlace →` / `Copy the link →` · fuente: 385 hechos · 236 fuentes
- **Frena lo falso** — Ya circula video de otro país presentado como si fuera este terremoto: lo encontramos en el propio hashtag, con comentaristas señalando que era de Chile. Antes de compartir, mira si la cuenta es de quien hizo la cosa. Si no puedes decir quién grabó y cuándo, no lo mandes.
  - EN: **Stop what is false** — Footage from another country is already circulating as if it were this earthquake: we found it in the hashtag itself, with commenters pointing out it was from Chile. Before sharing, check whether the account belongs to whoever did the thing. If you cannot say who filmed it and when, do not send it.
  - botón: `Verificado el 15 de agosto` / `Verified on August 15` · fuente: Hallazgo propio, documentado en transparencia
- **Mándanos lo que viste** — Si viste a alguien ayudando y quieres que aparezca aquí, mándanos el enlace. Lo verificamos y entra con crédito a quien lo publicó. Recibir no implica publicar.
  - EN: **Send us what you saw** — If you saw someone helping and you want them here, send us the link. We verify it and it goes up with credit to whoever posted it. Receiving does not mean publishing.
  - botón: `Escríbenos →` / `Write to us →` · fuente: Todo se verifica antes de publicar

### Eje `comprando` — Comprando · negocios que donan lo que venden  /  EN: By buying · shops giving away what they sell
- **Arte por Colombia** — 24 galerías y más de 130 artistas venden obra por catálogo digital y el 100% del valor va a Cruz Roja, Presentes, Manos Visibles y Una Garra por Colombia. Las galerías y los artistas asumen todos los costos. En sus primeros días superó los $260 millones.
  - EN: **Arte por Colombia** — 24 galleries and over 130 artists selling work through a digital catalogue; 100% of the price goes to the Red Cross, Presentes, Manos Visibles and Una Garra por Colombia. Galleries and artists cover every cost. It passed about US$83,000 in its first days.
  - botón: `Ver cómo comprar →` / `See how to buy →` · fuente: Periódico Arteria + El Tiempo
- **Maglione** — Marca colombiana de tejidos. Dona todo el dinero de las ventas de su tienda física y su página web del 14 al 19 de agosto, repartido entre cinco fundaciones de las regiones afectadas. Es una ventana corta: verifica que siga abierta.
  - EN: **Maglione** — Colombian knitwear brand. Giving away all revenue from its shop and website between 14 and 19 August, split across five foundations in the affected regions. Short window: check it is still running.
  - botón: `Ir a la tienda →` / `Go to the shop →` · fuente: El Espectador
- **Libertario Coffee Roasters** — Tostador de café que donó una tonelada de producto, abrió acopio en Bogotá, Medellín y Cartagena, y destina el 20% de las ventas de su café Libre en bolsa durante agosto.
  - EN: **Libertario Coffee Roasters** — Coffee roaster that donated a tonne of product, opened collection points in Bogotá, Medellín and Cartagena, and gives 20% of sales of its bagged Libre coffee through August.
  - botón: `Ir a la tienda →` / `Go to the shop →` · fuente: Revista Diners
- **Zierra Leona** — Destina el 100% de las ventas de su referencia Panthera T-shirt Ivory a los animales afectados, y su tienda en el Valle del Cauca funciona como punto de recolección.
  - EN: **Zierra Leona** — Gives 100% of sales of its Panthera T-shirt Ivory to animals affected by the quake, and its Valle del Cauca shop doubles as a collection point.
  - botón: `Ir a la tienda →` / `Go to the shop →` · fuente: El Espectador
- **Soreil** — Destina el 20% de sus ventas de agosto a comprar ropa interior para donarla a las personas afectadas. No enlazamos su tienda porque encontramos dos dominios distintos con su nombre y no pudimos confirmar cuál es el oficial: aquí va la nota que lo documenta.
  - EN: **Soreil** — Gives 20% of its August sales to buying underwear to donate to affected families. We are not linking a shop because we found two different domains under that name and could not confirm which is official; this links to the article instead.
  - botón: `Leer la nota →` / `Read the article →` · fuente: El Espectador
- **¿Tienes un negocio? Esta puerta también es tuya** — Varias de estas marcas no donaron dinero propio: destinaron un porcentaje o el total de lo que vendieron en unos días. Se puede hacer con cualquier tamaño de negocio, y no exige tener caja. Si montas algo así, cuéntanos con un enlace y lo sumamos.
  - EN: **Do you run a business? This door is yours too** — Several of these brands did not give their own money: they pledged a share, or all, of what they sold over a few days. It works at any size and does not require cash on hand. If you set one up, send us a link and we will add it.
  - botón: `Escríbenos →` / `Write to us →` · fuente: Idea recogida de las campañas ya verificadas aquí

---

## 10. Sección verde: "Si el terremoto te afectó"

Esta sección es para las víctimas, no para quien ayuda. Tiene que verse claramente distinta
del resto de la página.

- **Evaluación estructural gratis de tu vivienda** — Subes la dirección y fotos de los daños, y un ingeniero o arquitecto voluntario emite una evaluación técnica siguiendo ATC-20 y EMS-98. Llega por correo. Son orientaciones preliminares y no reemplazan la inspección oficial de la UNGRD, la Defensa Civil, los bomberos o tu municipio.
  - EN: **Free structural assessment of your home** — You upload your address and photos of the damage, and a volunteer engineer or architect issues a technical assessment following ATC-20 and EMS-98. It arrives by email. Preliminary guidance only; it does not replace official inspection by UNGRD, Civil Defence, the fire service or your municipality.
  - botón: `Reportar mi vivienda →` · fuente: SismoAyuda Colombia · sitio oficial
- **Asesoría jurídica gratuita en el Valle** — La Gobernación del Valle con la Universidad Santiago de Cali atiende gratis daños en vivienda, reclamaciones a seguros, contratos y arriendos, y derechos de petición.
  - EN: **Free legal advice in Valle del Cauca** — The Valle del Cauca government with Universidad Santiago de Cali gives free advice on home damage, insurance claims, contracts and tenancy, and formal petitions.
  - botón: `consuljuridico@usc.edu.co →` · fuente: Occidente
- **Brigada jurídica gratuita** — La firma Pérez-Llorca Gómez-Pinzón abrió asesoría gratuita en cinco áreas: seguros, laboral, inmobiliario, obligaciones bancarias y Registro Único de Damnificados.
  - EN: **Free legal brigade** — The law firm Pérez-Llorca Gómez-Pinzón opened free advice in five areas: insurance, employment, property, bank obligations and the official disaster victims registry.
  - botón: `Ver la nota →` · fuente: Semana
- **Atención veterinaria remota 24 horas** — Fixit atiende consultas veterinarias remotas gratuitas todo el día. Teléfonos 333 602 5800 y 601 438 7525.
  - EN: **24-hour remote veterinary care** — Fixit offers free remote veterinary consultations around the clock. Phones +57 333 602 5800 and +57 601 438 7525.
  - botón: `Ver los teléfonos →` · fuente: El Tiempo
- **Si aparecen perfiles pidiendo dinero en tu nombre** — La familia Saavedra, tras perder a varios de los suyos, advirtió públicamente que había perfiles falsos haciéndose pasar por familiares. Si te pasa, publícalo desde tus propias cuentas y señala cuál es tu único canal autorizado. Eso es lo que permite a los demás distinguir.
  - EN: **If fake profiles ask for money in your name** — The Saavedra family, after losing several of their own, publicly warned that fake profiles were impersonating relatives. If it happens to you, post it from your own accounts and state which is your only authorised channel. That is what lets everyone else tell the difference.
  - botón: `Leer la alerta →` · fuente: Publimetro

---

## 11. Conciertos

- Sáb 15 ago · Medellín · **Colombia, Medellín te quiere** · Centro de Eventos La Macarena · Luis Alfonso, Kapo, Pipe Bueno, Jhonny Rivera y 25 más ·  · Todo lo recaudado en boletería
- Dom 16 ago · Miami · **Unidos por los nuestros** · Kaseya Center · Marc Anthony, Chayanne, Ricardo Montaner, Feid, Silvestre Dangond y 17 más ·  · Formato teletón · Colombia y Venezuela
- Mar 18 ago · Envigado · **Vallenatón por Colombia** · Centro de Eventos Centauro · Daniel Calderón, Jorge Celedón, Nelson Velásquez y 10 más ·  · Apoyo a la emergencia
- Dom 23 ago · Bogotá · **Colombia Voces por la Vida** · Vive Claro Distrito Cultural · Karol G, Andrés Cepeda, Miguel Bosé, Sebastián Yatra y 16 más · → Presentes Corporación · Reconstrucción de viviendas
- Sáb 29 ago · Bogotá · **Si nos organizamos cabemos todos** · Movistar Arena · 4:00 p.m. · Carlos Vives, Feid, Kapo, Manuel Turizo, ChocQuibTown, Piso 21 y 6 más · → 100% de la boletería a Fundación PLAN · Desde $130.000 · Tuboleta

---

## 12. Transparencia (acordeón)

Las dos primeras entradas son lo más personal que tiene el sitio. Merecen tratamiento, no
quedar sepultadas en un acordeón gris al final.

- **¿Quién está detrás de esto?**
  Mi nombre no importa. Soy un colombiano que sintió mucho no haber podido ayudar físicamente, porque no vive en Colombia, y buscando la manera de ayudar decidí que esta era la mejor que tenía. Lo único que espero es que la gente lo comparta, para que esto le sirva a muchas más personas y siga creando esa sinergia.
  - EN **Who is behind this?**: My name does not matter. I am a Colombian who felt it deeply that I could not help in person, because I do not live in Colombia, and looking for a way to help I decided this was the best one I had. The only thing I hope for is that people share it, so it reaches many more people and keeps that synergy going.
- **Esto se hizo rápido, y se nota**
  Salió al aire en pocos días porque valía más servir a tiempo que salir completo. La consecuencia es que faltan cosas: fundaciones que no encontramos, empresas que están mandando camiones sin que la prensa lo cuente, colectas de barrio que nunca salieron en un medio. Que algo no esté aquí no significa que no exista ni que no sirva: significa que no lo hemos encontrado. Por eso el sitio tiene un correo abierto para que cualquiera sume lo que falta, con su enlace, y lo verificamos igual que todo lo demás.
  - EN **This was built fast, and it shows**: It went live in a matter of days because being useful in time mattered more than being complete. The consequence is that things are missing: foundations we did not find, companies sending trucks with no press coverage, neighbourhood collections that never made the news. Something not being here does not mean it does not exist or does not work: it means we have not found it. That is why the site has an open inbox for anyone to add what is missing, with a link, and we verify it like everything else.
- **Esto no promueve nada ni a nadie**
  Se hizo una investigación, y se hizo rápido. El fin de esta página no es promover a nadie: es mostrar las maneras en que otras personas, comunidades y empresas ya están ayudando, para que quien entre encuentre la suya y de pronto piense en una forma propia de aportar. Nadie paga por aparecer aquí, nadie nos pidió que lo pusiéramos, y si alguien quiere que lo retiremos, lo retiramos.
  - EN **This promotes nothing and no one**: Research was done, and it was done fast. The point of this page is not to promote anyone: it is to show the ways other people, communities and companies are already helping, so that whoever lands here finds their own way in, and perhaps thinks of one of their own. Nobody pays to appear here, nobody asked us to list them, and if anyone wants to be taken down, we take them down.
- **Por qué las cifras cambian de moneda**
  En inglés, las cifras que escribimos nosotros van en dólares, porque es la moneda que casi todo el mundo entiende. La conversión usa la TRM del Banco de la República del 15 de agosto de 2026: $3.128,65 por dólar. Las cifras que vienen citadas de una noticia se dejan exactamente como las publicó la fuente, sin tocarlas, porque cambiarlas sería reescribir a otro.
  - EN **Why the figures change currency**: In English, the amounts we write ourselves are shown in US dollars, because that is the currency almost everyone understands. The conversion uses the Banco de la República rate for 15 August 2026: COP $3,128.65 per dollar. Figures quoted from a news source are left exactly as that source published them, untouched, because changing them would mean rewriting someone else.
- **Cómo se armó esta lista**
  Se hicieron dos rondas de investigación con agentes que buscaron en prensa colombiana, comunicados de empresas, boletines de gremios y sitios oficiales. Cada hecho encontrado pasó por un verificador independiente que abrió la URL, comprobó que la página sostuviera la afirmación, corrigió las cifras que no coincidían y descartó lo que no se sostenía. De los hechos en bruto quedaron 403 confirmados y 77 descartados o corregidos, y la lista sigue creciendo con lo que la gente nos manda.
  - EN **How this list was put together**: Two rounds of research were run with agents searching Colombian press, company statements, trade body bulletins and official sites. Every fact found went through an independent verifier that opened the URL, checked the page supported the claim, corrected figures that did not match and discarded what did not hold up. Of the raw facts, 403 were confirmed and 77 discarded or corrected, and the list keeps growing with what people send us.
- **Qué se descartó y por qué**
  Citas que no aparecían en la página que supuestamente las contenía. Cifras que no coincidían con la fuente. Datos atribuidos a quien no correspondía. Mensajes de apoyo sin acción concreta detrás. Y todo lo que traía carga política, comparaciones entre quién dio y quién no, o señalamientos de culpables. Dos nombres muy conocidos quedaron fuera porque la fuente afirmaba una donación sin publicar monto, fecha ni destinatario verificable.
  - EN **What was discarded and why**: Quotes that did not appear on the page supposedly containing them. Figures that did not match the source. Facts attributed to the wrong party. Messages of support with no concrete action behind them. And anything carrying political weight, comparisons between who gave and who did not, or blame. Two very well-known names were left out because the source claimed a donation without publishing an amount, a date or a verifiable recipient.
- **Corrección: dijimos que un sitio estaba vacío y estaba equivocado**
  La herramienta con la que revisamos sitios lee el HTML antes de que corra el JavaScript. quieroayudar.co carga sus datos del lado del cliente, así que vimos el cascarón con los contadores en cero y concluimos mal. No podemos renderizar JavaScript de sitios externos. Queda dicho aquí en vez de borrado en silencio.
  - EN **Correction: we said a site was empty and we were wrong**: The tool we use to check sites reads the HTML before JavaScript runs. quieroayudar.co loads its data client-side, so we saw the shell with counters at zero and drew the wrong conclusion. We cannot render JavaScript from external sites. This is stated here rather than quietly deleted.
- **En el hashtag circula video de otro país**
  Revisando #FuerzaColombia el 15 de agosto encontramos una publicación con más de mil likes cuyo video, según dos comentaristas, es de Chile de mayo de este año. Por eso este sitio no toma videos de hashtags: solo enlaza contenido publicado por quien hizo la acción. Un video prueba quién lo publicó, no que las imágenes sean de este terremoto.
  - EN **Footage from another country is circulating in the hashtag**: Reviewing #FuerzaColombia on August 15 we found a post with over a thousand likes whose video, according to two commenters, is from Chile in May of this year. That is why this site does not take videos from hashtags: it only links content posted by whoever did the thing. A video proves who posted it, not that the footage is from this earthquake.
- **Las cifras suben cada día y por eso llevan fecha**
  En cinco días el balance pasó de más de 130 fallecidos el 11 de agosto, a 224 según OCHA ese mismo día, a 239, a 285, y a 288 con 4.018 heridos según la UNGRD al 15 de agosto. Las viviendas averiadas pasaron de 8.385 a 80.744 a medida que avanzaron los censos de daño. No confíes en una cifra sin fecha, ni aquí ni en ningún lado.
  - EN **The figures rise every day, which is why they carry a date**: In five days the tally went from over 130 dead on August 11, to 224 per OCHA that same day, to 239, to 285, and to 288 with 4,018 injured per UNGRD as of August 15. Damaged homes went from 8,385 to 80,744 as damage assessments advanced. Do not trust a figure without a date, here or anywhere.
- **Créditos no son donaciones**
  Los USD 450 millones del Banco Mundial y los USD 300 millones del BID son línea de crédito y financiamiento contingente, no dinero donado. Están redactados de forma que nadie los pueda sumar como ayuda entregada. El Banco Mundial además aparece con tres cifras distintas en distintas fuentes: USD 200.000 para evaluación de daños, USD 200 millones desembolsados, y esa línea de USD 450 millones. Las tres son ciertas y son cosas distintas.
  - EN **Credit is not the same as a donation**: The World Bank's USD $450 million and the IDB's USD $300 million are credit lines and contingent financing, not donated money. They are worded so no one can add them as delivered aid. The World Bank also appears with three different figures across sources: USD $200,000 for damage assessment, USD $200 million disbursed, and that USD $450 million line. All three are true and they are different things.
- **Discrepancias que dejamos a la vista**
  La profundidad del sismo: el Servicio Geológico Colombiano reportó 103 km y el USGS 110,3 km. Son dos soluciones del mismo evento, no un error. El número de cuenta de Colombia Unida aparece como 001280353 en el volante, El País de Cali y CWMás, y como 0012803533 en Occidente.co. Usamos la versión en la que coinciden tres fuentes, pero confírmalo antes de transferir. Y la fecha del concierto del Movistar Arena aparecía como martes 29 en El Espectador, cuando Tuboleta dice sábado 29: mandó la taquilla.
  - EN **Discrepancies we leave in plain sight**: The quake's depth: the Colombian Geological Survey reported 103 km and USGS 110.3 km. Two solutions for the same event, not an error. The Colombia Unida account number appears as 001280353 on the flyer, in El País de Cali and CWMás, and as 0012803533 on Occidente.co. We use the version three sources agree on, but confirm before transferring. And the Movistar Arena concert date appeared as Tuesday the 29th in El Espectador, while Tuboleta says Saturday the 29th: the box office wins.
- **Qué no hacemos**
  No recibimos dinero, no procesamos pagos y no administramos donaciones. No auditamos estados financieros ni gastos administrativos de ninguna organización: verificamos que el enlace exista, que corresponda a quien dice ser y que mencione esta emergencia. No evaluamos a ningún gobierno, ni al nacional ni al local, ni para elogiarlo ni para criticarlo. Y no publicamos imágenes de personas en su peor momento.
  - EN **What we do not do**: We take no money, process no payments and manage no donations. We do not audit any organisation's financial statements or overhead: we verify that the link exists, belongs to who it claims to, and references this emergency. We do not assess any government, national or local, to praise or to criticise. And we do not publish images of people at their worst moment.

---

## 13. Muestras de tarjetas de hecho

Así se ven los datos reales. Fíjate en el contraste de escala entre una y otra: eso es la
tesis del sitio, y el diseño no puede hacer que la primera se vea más importante que la
segunda.

- **Emiratos Árabes Unidos** · USD 10 millones · exterior · 12 ago · fuente: Cancillería
- **Niña anónima de Sabaneta** · una alcancía llena de monedas · Colombia · 13 ago · fuente: El Colombiano
- **Vecinos del barrio Florez Buenaños, Quibdó** · aportes de $20.000 a $50.000 por vecino ·
  Colombia · 10 ago · fuente: El Tiempo
- **Panadería La Central (Andalucía, Valle)** · perdió el local y salió a regalar el pan que
  quedó · Colombia · 10 ago · fuente: El País (Cali)
- **Óscar Conde, desarrollador** · más de 1.000 personas localizadas con la plataforma que
  hizo solo · Colombia · 11 ago · fuente: Noticias Caracol
- **Liga Radio Quindío** · red de emergencia activada en 15 minutos; repetidoras restablecidas
  con paneles solares · Colombia · 11 ago · fuente: ARRL
- **Alejandro Riaño / The Juanpis Live Show** · 100% de lo recaudado · Colombia · 29 ago ·
  fuente: Portafolio

Estructura de cada hecho: `quien`, `cifra`, `que_hizo`, `cuando`, `zona`, `origen`
(colombia/exterior/mixto), `categoria`, `fuente_nombre`, `fuente_url`, `cita` textual.

---

## 14. Restricciones técnicas duras

- **Un solo archivo HTML autocontenido.** Cero dependencias externas: sin CDN, sin fuentes de
  Google, sin frameworks, sin analytics, sin píxeles de rastreo. Si quieres una tipografía
  especial, propónla y explica cómo la embebemos, pero el sitio tiene que funcionar sin
  descargar nada de terceros.
- **Sin `localStorage`, `sessionStorage` ni ningún almacenamiento del navegador.**
- **El único contenido de terceros es el iframe de Instagram, y solo tras un clic.**
- CSS y JS en línea, en el mismo archivo.
- Tiene que abrir bien en un teléfono de gama media con conexión mala.

---

## 15. Cómo se aplica lo que entregues

El sitio de producción se genera con un script: `sitio-template.html` + `hechos.json` +
`contenido.json` + `reels.json` → `sitio.html`. Por eso pedimos tu propuesta como maqueta y no
como archivo final: nosotros portamos tu diseño a la plantilla para que los datos sigan
saliendo del pipeline verificado. **No hace falta que resuelvas nada de eso**, pero sí ayuda
que el HTML que entregues tenga estructura limpia y clases con nombres claros.

---

## 16. Criterios con los que vamos a mirar tu propuesta

1. ¿Transmite calma? Si la primera reacción es urgencia o alarma, falló.
2. ¿Alguien que votó distinto se sigue sintiendo invitado?
3. ¿Se puede leer un hecho y ver su fuente sin esfuerzo?
4. ¿La tarjeta del país del Golfo y la de la niña con la alcancía se ven igual de importantes?
5. ¿Quien no tiene dinero encuentra su puerta en los primeros segundos?
6. ¿Sobrevive en un teléfono, con una mano, en la calle?
7. ¿Queda alguna etiqueta en mayúsculas sobre un título? No debería.
8. ¿Se entiende, sin que nadie lo explique, que las tres palabras del nombre son los tres
   colores de la bandera? ¿Y se entiende sin gritar?

---

## 17. Lo que nos gustaría que propongas y todavía no está resuelto

- El sistema de marca a partir de "tres palabras, tres colores": cómo se ve el logotipo, qué
  pasa en inglés, y hasta dónde se estira la idea antes de volverse truco.
- Una tipografía que suene cálida y seria a la vez, embebible sin CDN.
- Un tratamiento para el azul que no canse a pantalla completa.
- Cómo marcar visualmente que la lista está incompleta sin que parezca un error.
- Cómo se ve la cadena de 46 tarjetas sin sentirse un muro.
- Si hay una manera de que el sitio se sienta hecho por una persona y no por una institución,
  sin usar el nombre de nadie.
