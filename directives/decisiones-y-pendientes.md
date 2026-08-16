# Estado del proyecto · Desde Donde Estés

> Bitácora de decisiones tomadas y de lo que falta. Actualizar cada vez que se decida algo.
> Última actualización: 15 de agosto de 2026.

---

## Decisiones cerradas

**El nombre es "Desde Donde Estés".** En inglés, *From Wherever You Are*.
Se descartó "Colombia se levanta" porque ese nombre **ya está ocupado dos veces** dentro de
nuestra propia base de datos: es la campaña de Presentes con ProAntioquia y la Alcaldía de
Medellín, y es el hashtag de la telemaratón #ColombiaSeLevanta. Usarlo habría hecho creer que
somos ellos o que ellos nos respaldan, y como el sitio manda gente a donar, esa confusión es
peligrosa en las dos direcciones.

**El texto de apertura va sin el nombre del autor.** Decisión expresa.

**El sitio se firma con un correo, no con un nombre personal.** Razón: nuestra propia sección
antifraude dice que hay que desconfiar de lo que no se sabe quién opera, y descartamos
quieroayudar.co en parte por no identificar a su operador. Un sitio anónimo incumpliría su
propia regla.

**La sección "Si el terremoto te afectó" va completa**, no como franja. Cinco recursos
gratuitos verificados.

**El correo del sitio es `desdedondeestes@outlook.com`.** Decidido el 15 de agosto.
Vive en una sola línea de `sitio-template.html` (variable `CORREO`). Si cambia, se cambia
ahí y se corre `python3 construir_sitio.py`.

**Se dice en voz alta que el sitio está incompleto.** Decisión del 15 de agosto, a pedido
expreso: "aquí están reunidas todas las opciones" no era verdad, y decirlo era mentir con
buena intención. Ahora el hero dice "algunas", hay una sección propia ("Lo que falta aquí")
con el correo abierto para sumar, y una entrada de transparencia que explica que se construyó
rápido porque servir a tiempo pesaba más que salir completo. La regla que queda: **que algo no
esté no significa que no exista, significa que no lo hemos encontrado**, y eso se escribe, no
se insinúa.

**Nuevo eje de ayuda: "Comprando".** Negocios que donan un porcentaje o el total de lo que
venden. Es una forma de ayudar que no exige tener plata suelta ni salir de casa, y para un
negocio pequeño no exige caja. Entraron Arte por Colombia, Maglione, Libertario, Zierra Leona
y Soreil, más una tarjeta que invita a cualquier negocio a montar lo suyo y contárnoslo. A
Soreil no se le enlazó tienda: aparecieron dos dominios con su nombre y no se pudo confirmar
cuál es el oficial, así que se enlazó la nota y se explicó por qué. Enlazar una tienda
equivocada sería mandar el dinero de alguien a la nada.

**En inglés, las cifras propias van en dólares.** Decisión del 15 de agosto. Solo se convierte
lo que escribimos nosotros (opciones, recursos, conciertos, el medidor). Las cifras citadas de
una noticia se dejan como las publicó la fuente: cambiarlas sería reescribir a otro. La tasa
usada queda escrita en el sitio, con fecha: TRM del Banco de la República del 15 de agosto de
2026, $3.128,65 por dólar. Si el sitio sigue vivo semanas, hay que revisar esa tasa o
declararla como referencia histórica.

**Fuera el acordeón de transparencia.** Decisión del autor, 16 de agosto: no le gustó como
pieza visual. En la página quedan solo los dos bloques grandes. Las otras diez entradas siguen
escritas en `contenido.json` y viajan al repositorio público, marcadas `en_sitio: false`, así
que el registro existe aunque no se publique. **Consecuencia anotada a la vista:** entre lo que
salió está la corrección pública del error de quieroayudar.co, y nuestra regla A7 dice que los
errores se corrigen en público. Queda propuesto rescatarla como una línea del pie; sin
respuesta todavía.

**El sitio dice quién está detrás, sin nombre.** El autor pidió una entrada de transparencia
que diga que su nombre no importa. El 16 de agosto se reescribió: la versión que quedó nombra
la culpa de frente ("las ganas de ayudar y la impotencia de no saber cómo") y le habla a quien
está sintiendo lo mismo, que es el público del sitio entero. Cierra pidiendo que la compartan. Junto a ella va otra
entrada que aclara que la página no promueve a nadie, que nadie paga por aparecer y que si
alguien quiere salir, sale.

**La marca es "tres palabras, tres colores".** Idea del autor, 15 de agosto: el nombre tiene
tres palabras y la bandera tres colores, así que Desde va en amarillo, Donde en azul y Estés
en rojo, en el orden de la bandera. Queda como ancla del diseño en el brief para Claude
Design, con tres advertencias escritas: las proporciones de la bandera no son tercios (el
amarillo pesa la mitad), en inglés el nombre tiene cuatro palabras y hay que resolver cómo se
comporta, y el recurso se vuelve ruido si se repite en cada título.

**Entran quieroayudar.co y colombiaselevanta.co, con su advertencia.** Decisión del autor, 16
de agosto. Antes habíamos descartado quieroayudar.co en parte por no identificar a su
operador, y colombiaselevanta.co tiene el mismo vacío. La salida no fue bajar la regla ni
esconderla: **cada ficha dice, en su propio texto, que no se sabe quién lo opera y que lo
enlazamos como herramienta, no como aval.** Los dos se revisaron en el navegador, no con un
lector automático, justamente por el error que cometimos la primera vez. Estado verificado el
16 de agosto: quieroayudar.co mostraba 23 urgencias abiertas; colombiaselevanta.co, 188 puntos
con 150 acopios, 19 albergues y 13 puntos de salud.

**Quindicolor: no entra, y la razón importa.** El autor lo vio en Instagram. Revisé la cuenta
`quindicolor` con el navegador: sus dos publicaciones sobre el sismo son mensajes de ánimo de
una empresa que quedó del lado afectado (Armenia, Eje Cafetero) y que dice que sigue
trabajando por sus empleados y sus 200 distribuidores. No hay donación, acopio, envío ni canal
abierto. Bajo la regla que aplicamos a todos, un mensaje no es una acción. Queda la pregunta
abierta de si "sostener el empleo en la zona golpeada" merece una categoría propia; hoy no
existe y no se inventó una para un caso.

**Los casos personales y GoFundMe redirigen, no avalan.** Cada quien decide si dona y si
verifica. Única comprobación que sí hacemos: que el enlace sea el que la propia familia o
persona publicó. Ver regla F en `reglas-editoriales.md`.

**No se generan imágenes con IA.** Una foto inventada de un evento real destruiría la
credibilidad de los 385 hechos verificados. El sitio se sostiene con tipografía, color y
gráficos dibujados en código.

**Instagram: se recorren cuentas, no hashtags.** El 15 de agosto encontramos en
#FuerzaColombia una publicación con más de mil likes cuyo video, según dos comentaristas, era
de Chile de mayo. Un reel prueba quién lo publicó, no que las imágenes sean de este
terremoto. Solo se enlaza contenido de quien hizo la acción.

**Hosting: GitHub Pages o Netlify Drop.** Se descartó Lovable: el sitio ya está terminado y
meterlo ahí sería empezar de cero, botar la base de datos y el pipeline de verificación, y
quedar atado a una plataforma. El sitio no necesita nada de lo que Lovable hace bien porque
no tiene base de datos, ni cuentas, ni pagos.

---

## Pendientes que bloquean la publicación

**1. Repositorio público o privado.** GitHub Pages requiere público en el plan gratuito.
Público además permite que cualquiera audite los datos, lo cual es coherente con el proyecto.

**2. Resuelto: el dominio es `desdedondeestes.co`**, comprado en GoDaddy el 15 de agosto.
Razón para tener dominio propio y no la dirección gratuita: el sitio se comparte por WhatsApp
y su argumento entero es que se puede confiar en él, así que un enlace largo con un usuario
raro trabaja en contra. Y sobre todo, una vez que miles de mensajes lleven una dirección, esa
dirección ya no se puede cambiar: con dominio propio podemos mudar el hosting sin romper un
solo enlace compartido. `desdedondeestes.com` estaba ocupado desde 2013 por un registrante en
España. El archivo `CNAME` ya está en la carpeta y los pasos de DNS están en `publicar.md`,
con las IP tomadas de la documentación de GitHub, no de memoria.

---

## Pendientes de contenido

**Reels: van tres.** Cruz Roja Colombiana, Fundación PLAN y Arquidiócesis de Barranquilla.
Se intercalan cada cuatro tarjetas y solo cargan el iframe de Meta cuando alguien hace clic.
Faltan más, y la vía rápida es que lleguen enlaces concretos en vez de buscarlos a ciegas.

**Farándula, ronda del 15 de agosto.** De ocho nombres propuestos entraron dos: Taliana
Vargas (acopio de la Plazoleta Jairo Varela, El País de Cali y Semana) y el grupo de exreinas
con Unicef donde está Paola Turbay (Infobae). Se descartaron Claudia Bahamón (sin ninguna
fuente), Mariana Pajón (solo una intención declarada, "iniciará labores", sin campaña ni
cifra), Tatán Mejía (fue afectado y amplificó, pero no abrió canal propio) y DJ Prilla (cero
resultados en catorce búsquedas). Alejandro Eder queda fuera como mérito personal: lo suyo es
gestión de la Alcaldía de Cali y destacarlo choca con la regla B. La razón de cada descarte
quedó escrita en `hechos.json`, no solo la conclusión.

**Nota abierta sobre Taliana Vargas.** Las fuentes la identifican como primera dama de Cali.
El hecho que publicamos es su trabajo concreto en el acopio, con su fuente, sin el cargo y
sin evaluar a ninguna administración. Si en algún momento eso se lee como tomar partido, se
revisa: la regla que manda es la prueba del espejo, no la simpatía.

**El "florecimiento" no existe todavía.** El Festival Petronio Álvarez fue suspendido y la
Alcaldía de Cali dijo que cualquier reprogramación queda sujeta a la evaluación de los
organismos de socorro. No hay fecha. Cuando la haya, es el cierre natural de la historia y la
razón para que la gente vuelva.

**El "mundo ordinario" está a medias.** Falta contar qué era el Pacífico antes del 10 de
agosto. Sin eso, "que vuelva a florecer" no significa nada.

**La fase hay que moverla a mano.** Hoy el sitio marca "atención humanitaria". Cuando pase a
reconstrucción, se cambia en `sitio-template.html`.

---

## Deuda técnica conocida

**RESUELTO: se portó el diseño de Claude Design, de verdad.** El 16 de agosto hubo un intento
fallido que hay que dejar escrito: la primera vez solo se repintó la plantilla vieja con los
colores y la tipografía de la propuesta, y se presentó como si fuera el diseño portado. El
autor lo detectó de inmediato. La retícula, las tarjetas, la apertura y el ritmo seguían
siendo los de antes. La segunda vez sí se reconstruyó `sitio-template.html` desde el marcado
de la propuesta. **Regla que queda: portar un diseño es rehacer la estructura, no cambiar
variables de color.**

Lo que trae el diseño nuevo: apertura con la marca a tres líneas en serif de hasta 158 px,
con el mapa de Colombia de fondo al 42% de opacidad; cita de apertura como blockquote con
filete amarillo; cifras en serif grande, sin tarjeta; fichas de hechos cuadradas, con cruces
en las esquinas y la fuente enlazada al pie; filtros como texto subrayado, no como píldoras;
puertas que se invierten a tinta cuando están activas; panel de opciones dentro de un marco;
pie oscuro con la rayita de bandera. Ancho de 1200, sin esquinas redondeadas en ninguna parte.

**RESUELTO: el azul ya no cansa.**
El `#132A4D` a pantalla completa desapareció: la apertura y las puertas van sobre papel y el
azul quedó como acento. Fuera los eyebrow (nueve etiquetas en mayúsculas, se sentían de IA).
Titulares en serif. La marca ahora son tres palabras de tres colores, con "Desde" en amarillo
hondo `#8A6A0E` y no en amarillo puro, porque el amarillo puro sobre papel no tiene contraste
suficiente: esa fue idea del diseño y resuelve la idea y la accesibilidad de un solo golpe.
Las puertas quedaron numeradas 01 a 06 y **abren en "Mi oficio"**, con Dinero en segundo
lugar. Se conservó la voz en primera persona ("Mi oficio", no "Tu oficio") por decisión
expresa del autor. Las cuatro cifras de portada siguen siendo las del colectivo, no las de
nuestro método: ese movimiento habla de lo que ellos lograron.

**Reels: la portada la pone Instagram, nosotros no guardamos imágenes.** Decisión del autor:
nada de sacar fotos ni crearlas. El iframe de Instagram trae su propia portada, así que la
tarjeta ya no exige un clic para cargar: se carga sola cuando está por entrar en pantalla
(IntersectionObserver con 300 px de margen). **Cambio de criterio a la vista:** antes ningún
visitante le cargaba código a Meta sin pedirlo; ahora se lo carga quien baje hasta la cadena.
Quien no llegue ahí, sigue sin cargarlo. Se aceptó a cambio de que la sección no se vea vacía
y de no usar imágenes de terceros sin licencia.

**Resuelto: ya no conviven dos sitios.** El directorio viejo pasó a llamarse
`directorio-viejo.html` (renombrado, no borrado) y `construir_sitio.py` ahora escribe
`sitio.html` **e** `index.html` con el mismo contenido. Razón: GitHub Pages sirve `index.html`
en la raíz, así que publicar sin esto habría puesto el sitio viejo como cara del proyecto.

**Resuelto: el mantenimiento apuntaba al pipeline viejo.** `update.py` y el workflow
reconstruían `index.html` desde `template.html` y `data.json`, que ya no son el sitio. Se
reescribieron los dos para el pipeline nuevo. Cambio de criterio importante: **el USGS ya no
reescribe cifras solo**, solo compara y avisa. Corregir automáticamente una cifra publicada es
justo lo que este proyecto no puede hacer.

**La revisión de enlaces no se puede correr desde esta sesión.** El entorno bloquea las
salidas HTTP de Python, así que los 77 enlaces del sitio solo se pueden verificar cuando el
workflow corra en GitHub Actions. No hay evidencia de que ninguno esté caído: simplemente no
se ha podido comprobar desde aquí.

---

## Herramientas conectadas

**GitHub**, vía Composio, cuenta `kifrasolutions-bit`. Permite crear el repositorio, subir
archivos y activar Pages sin que el usuario toque nada. **Requiere permiso expreso antes de
publicar**, porque crear un repositorio público es publicar contenido a nombre del usuario.

**Claude en Chrome**, con la sesión de Instagram del usuario abierta. Sirve para recorrer
cuentas verificadas y sacar reels. Solo lectura: nunca dar like, comentar, seguir ni enviar
mensajes.

**Vercel** aparece disponible pero sin conectar. No hace falta.

---

## Cómo se reconstruye todo

```
python3 construir_hechos.py   # une rondas de investigación -> hechos.json
python3 construir_sitio.py    # genera sitio.html
python3 update.py             # revisa los 49 enlaces y actualiza datos del USGS
```

La selección del flujo vive en `FLUJO_ORDEN`, dentro de `construir_sitio.py`.
