# Desde Donde Estés

**https://desdedondeestes.co**

Formas verificadas de ayudar tras el terremoto de magnitud 7,4 del 10 de agosto de 2026 en
Colombia, con epicentro 5 km al sur de San José del Palmar, Chocó.

El sitio no recibe dinero, no procesa pagos y no administra donaciones. Solo enlaza a los
canales oficiales de cada organización, y cada cifra lleva su fuente y su fecha.

Este repositorio es público para que cualquiera pueda comprobar los datos uno por uno.

---

## Cómo se verifica

Cada hecho publicado tiene: quién lo hizo, qué hizo, cifra si la hay, fecha, zona, y una URL
de fuente con una cita textual que sostiene la afirmación. Lo que no se pudo comprobar no se
publica, y queda registrado en `hechos.json` bajo `descartados`, con la razón del descarte.

Reglas que se siguen sin excepción:

- Nada entra sin una fuente que se pueda abrir.
- Las cifras citadas de un medio se dejan como las publicó ese medio. Las cifras que
  escribimos nosotros se convierten a dólares en la versión en inglés, con la tasa y la fecha
  escritas en el pie.
- Cuando las fuentes se contradicen, se muestran las dos versiones en vez de escoger una.
- Un mensaje de apoyo no es una acción: para entrar hace falta algo concreto.
- No se evalúa a ningún gobierno ni se toma partido.
- No se usan imágenes generadas con inteligencia artificial ni fotografías de terceros.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` / `sitio.html` | El sitio publicado. Un solo archivo, sin dependencias externas. |
| `hechos.json` | La base de hechos verificados y los descartados con su razón. |
| `contenido.json` | Opciones de ayuda, recursos para afectados, conciertos, transparencia y fuentes. |
| `reels.json` | Los reels de Instagram que se muestran. |
| `sitio-template.html` | La plantilla con los marcadores que rellena el generador. |
| `construir_sitio.py` | Genera `index.html` y `sitio.html` a partir de lo anterior. |
| `update.py` | Mantenimiento: reconstruye, revisa que los enlaces sigan vivos y compara con el USGS. |

## Cómo se reconstruye

```bash
python3 construir_sitio.py   # genera el sitio
python3 update.py            # ademas revisa enlaces y consulta el USGS
```

Un flujo de GitHub Actions corre `update.py` todos los días a las 7:00 a.m. hora de Colombia.
Si un enlace deja de responder o el USGS ya no coincide con lo que dice el sitio, abre una
incidencia. **No corrige cifras solo:** una cifra publicada solo la cambia una persona, con su
fuente.

## Corregir o sumar algo

Si falta una organización, si un dato está mal o si quieres que retiremos algo, escribe a
**desdedondeestes@outlook.com** con un enlace que se pueda revisar. También puedes abrir una
incidencia aquí.

Esta lista está incompleta a propósito: se construyó rápido porque valía más salir a tiempo
que salir completa. Que algo no esté aquí no significa que no exista, significa que no lo
hemos encontrado.
