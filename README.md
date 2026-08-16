# Desde Donde Estés · Terremoto Colombia 2026

> El sitio publicable es **`sitio.html`**. Se genera con `python3 construir_sitio.py`
> a partir de `sitio-template.html` + `hechos.json` + `contenido.json` + `reels.json`.
> El correo de contacto del sitio es `desdedondeestes@outlook.com` (variable `CORREO` en `sitio-template.html`).

## Cómo publicarlo (nunca has hecho esto, tranquilo)

1. Entra a `app.netlify.com/drop`.
2. Arrastra la carpeta del proyecto a la ventana.
3. En segundos tienes un enlace público. Gratis, sin tarjeta.
4. Después, si quieres, compras un dominio y lo conectas desde Netlify.

Las reglas editoriales mandan sobre todo lo demás: `directives/reglas-editoriales.md`.

---


Sitio de una sola página, sin dependencias externas ni build. Se abre con doble clic o se publica arrastrando la carpeta a Netlify, GitHub Pages o Cloudflare Pages.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El sitio publicado. Es lo único que necesitas subir, junto con la carpeta `fotos`. |
| `data.json` | Las organizaciones. Editable sin tocar el HTML. |
| `fotos.json` | Las fotos de la sección "Cómo nos estamos uniendo". |
| `fotos/` | Carpeta donde van las imágenes. Créala tú. |
| `reels.json` | Los reels de Instagram que se muestran en el sitio. |
| `agregar-reels.html` | Herramienta local para generar `reels.json` pegando enlaces. Ábrela con doble clic. |
| `update.py` | Actualiza los datos del sismo desde el USGS, revisa los 49 enlaces y reconstruye `index.html`. |
| `.github/workflows/actualizar.yml` | Corre `update.py` todos los días y publica solo. |

`index.html` se genera a partir de `template.html` + `data.json` + `fotos.json` + `reels.json`. Si editas cualquiera de esos, corre `python3 update.py --solo-build` para regenerar `index.html`.

## Cómo agregar reels de Instagram

1. Abre `agregar-reels.html` con doble clic.
2. Pega los enlaces de Instagram, uno por línea. Sirven `/reel/`, `/p/` y `/tv/`, con o sin nombre de usuario en la ruta.
3. Ponles pie de foto si quieres. Si dejas el inglés vacío, se usa el español.
4. Copia el resultado en `reels.json` y corre `python3 update.py --solo-build`.

La sección de reels aparece sola cuando hay al menos un enlace válido, y desaparece sola cuando el arreglo está vacío.

Tres cosas sobre los reels:

- **La cuenta tiene que ser pública.** Un perfil privado no se puede embeber; se verá solo el enlace.
- **Embeber no es copiar.** El video lo sigue sirviendo Instagram, con el crédito y el enlace al perfil de quien lo publicó. Por eso no tiene el problema de licencia que sí tienen las fotos de prensa. Aun así, avisarle al autor es lo decente.
- **El video no se carga hasta que alguien le da clic.** Se ve una tarjeta con botón de reproducir, y solo al hacer clic se inserta el iframe de Instagram. Eso mantiene la página liviana y evita cargar código de Meta sin que la persona lo pida.

**No pude probar que el embebido de Instagram funcione de verdad**, porque el entorno donde construí esto no puede cargar Instagram. Verifiqué que la tarjeta se pinta, que el enlace es correcto y que al hacer clic se inserta el iframe apuntando a `instagram.com/reel/CODIGO/embed/`. Ábrelo en tu navegador con un reel real antes de publicar.

## Cómo agregar fotos

1. Crea la carpeta `fotos` al lado de `index.html` y pon ahí las imágenes.
2. Abre `fotos.json` y llena una entrada por foto:

```json
{
  "archivo": "acopio-corferias.jpg",
  "autor": "Nombre de quien tomó la foto",
  "licencia": "CC BY 4.0",
  "fuente": "https://enlace-a-donde-la-obtuviste",
  "es": "Pie de foto en español.",
  "en": "Caption in English."
}
```

3. Los cinco campos son obligatorios. **Si falta uno, la foto no se muestra.** Es a propósito: obliga a que nada publicado quede sin crédito ni permiso.

## Sobre los derechos de las fotos

Dar crédito no equivale a tener licencia. Republicar una foto de AFP, Reuters, EFE, Getty, El Tiempo, Semana o Infobae sin comprar licencia es infracción de derechos de autor, aunque cites la fuente. Estas agencias sí hacen reclamaciones.

Lo que sí puedes usar:

- **Fotos tuyas o de gente que te las ceda por escrito.** Guarda el mensaje donde te dan permiso. Es la vía más limpia.
- **Fotos con licencia Creative Commons o de dominio público.** Wikimedia Commons tiene una categoría llamada "2026 Colombia earthquake". No pude abrirla desde el entorno donde construí esto, así que no sé qué contiene ni bajo qué licencias. Revísala tú y copia la licencia exacta de cada archivo al campo `licencia`.
- **Fotos de las propias fundaciones.** Cruz Roja Colombiana, el Idypba de Bogotá, Laika, los refugios de animales y las fundaciones del Chocó suelen dar permiso a cambio de crédito y enlace. Escríbeles. Es un correo de dos líneas y además abre conversación con ellos.
- **Entidades públicas colombianas.** Revisa los términos de uso de cada sitio antes de asumir que son libres. No todas lo son.

Lo que no deberías hacer: usar bancos de imágenes genéricos (Unsplash, Pexels) para ilustrar este terremoto. La licencia lo permite, pero la foto no es del evento y el sitio deja de ser honesto.

## Los dos modos

El switch "¿Desde dónde vas a ayudar?" cambia el sitio entero:

- **Estoy en Colombia**: se muestra todo, incluidos centros de acopio, qué llevar y puntos físicos para animales.
- **Estoy fuera de Colombia**: se ocultan las secciones físicas y las organizaciones que solo reciben por rieles colombianos. Actualmente solo se oculta el Banco de Alimentos de Bogotá, que únicamente ofrece llave Bre-B y entrega presencial.

En `data.json`, el campo `intl` de cada organización controla esto:

- `"yes"`: confirmado que acepta pagos desde el exterior.
- `"no"`: confirmado que no. Se oculta en modo exterior.
- `"unknown"`: no se pudo confirmar. Se muestra con etiqueta de advertencia.

El campo `until` marca campañas con fecha límite. Si la fecha ya pasó respecto a `verified_on`, la tarjeta muestra "Ventana cerrada el X" en vez de "Abierta hasta el X". Hoy lo usa la Fundación Bancolombia, habilitada hasta el 30 de agosto de 2026.

El campo `v` marca el nivel de verificación: `"full"` si la propia página de la organización menciona esta emergencia, `"partial"` si el vínculo con el terremoto está documentado por un tercero pero no por su página de donación.

## Mantenimiento

Cada tarjeta muestra "Verificado 15 de agosto de 2026". Esa fecha es el valor del sitio y también su fecha de caducidad. Si dejas de revisar los enlaces, actualiza la fecha o retira la etiqueta, porque un "verificado" viejo es peor que no tenerlo.
