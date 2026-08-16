# Cómo se publica el sitio

> Dominio: **desdedondeestes.co**, comprado en GoDaddy.
> Hosting: GitHub Pages, cuenta `kifrasolutions-bit`.
> Estado: pendiente de tu orden para crear el repositorio.

---

## Parte 1 · Lo que hago yo (cuando me des la orden)

1. Creo el repositorio `desde-donde-estes` en tu cuenta de GitHub, público.
2. Subo el sitio, los datos, los scripts, las directivas y el flujo de mantenimiento.
3. Activo GitHub Pages sobre la rama principal.
4. Configuro el dominio `desdedondeestes.co` en la configuración de Pages.
5. Corro el mantenimiento una vez a mano, con red de verdad, para revisar los 77 enlaces
   antes de que lo vea nadie.

El archivo `CNAME` ya está creado en la carpeta con el dominio adentro. Ese archivo es lo que
le dice a GitHub cuál es tu dominio, y tiene que estar en la raíz del repositorio.

---

## Parte 2 · DNS en GoDaddy — HECHO el 15 de agosto de 2026

Los registros ya quedaron creados. Estado verificado en el panel:

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| A | @ | 185.199.108.153 | 1 hora |
| A | @ | 185.199.109.153 | 1 hora |
| A | @ | 185.199.110.153 | 1 hora |
| A | @ | 185.199.111.153 | 1 hora |
| AAAA | @ | 2606:50c0:8000::153 | 1 hora |
| AAAA | @ | 2606:50c0:8001::153 | 1 hora |
| AAAA | @ | 2606:50c0:8002::153 | 1 hora |
| AAAA | @ | 2606:50c0:8003::153 | 1 hora |
| CNAME | www | kifrasolutions-bit.github.io | 1 hora |

El registro `A` de estacionamiento de GoDaddy ("WebsiteBuilder Site") se reemplazó por la
primera IP de GitHub, así que ya no existe. El `CNAME` de `www` apuntaba al propio dominio y
se cambió a GitHub. Los `NS`, el `SOA`, el `_domainconnect` y el `TXT` de `_dmarc` quedaron
intactos: son de GoDaddy y no estorban.

Falta confirmar la propagación. Las consultas públicas de DNS todavía pueden devolver los
valores viejos hasta una hora, porque el TTL anterior era de una hora.

---

## Parte 2 bis · Referencia, por si hay que rehacerlo

Entra a **Mis productos → desdedondeestes.co → DNS → Administrar zonas**.

### Borra primero lo que viene de fábrica

GoDaddy deja puesto un registro `A` de tipo `@` apuntando a una IP suya de estacionamiento, y
casi siempre un `CNAME` de `www` apuntando a su propio parqueadero. **Esos dos hay que
borrarlos o editarlos**, porque si se quedan, el dominio sigue mostrando la página de GoDaddy
en vez del sitio.

### Crea estos cuatro registros A

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| A | @ | 185.199.108.153 | 1 hora |
| A | @ | 185.199.109.153 | 1 hora |
| A | @ | 185.199.110.153 | 1 hora |
| A | @ | 185.199.111.153 | 1 hora |

Sí, son cuatro registros con el mismo nombre `@` y distinto valor. Es correcto y es a
propósito: si un servidor de GitHub se cae, el navegador usa otro.

### Crea también estos cuatro registros AAAA

Son los mismos servidores en IPv6. No son obligatorios, pero sin ellos el sitio no carga para
quien tenga conexión solo IPv6, que en móviles es cada vez más común.

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| AAAA | @ | 2606:50c0:8000::153 | 1 hora |
| AAAA | @ | 2606:50c0:8001::153 | 1 hora |
| AAAA | @ | 2606:50c0:8002::153 | 1 hora |
| AAAA | @ | 2606:50c0:8003::153 | 1 hora |

### Y un CNAME para www

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| CNAME | www | kifrasolutions-bit.github.io | 1 hora |

Con eso, `www.desdedondeestes.co` también funciona y GitHub redirige al dominio principal.
GitHub recomienda tener el `www` configurado junto con el dominio raíz cuando se usa HTTPS.

**Fuente de las direcciones IP:** documentación oficial de GitHub Pages sobre dominios
personalizados, consultada el 15 de agosto de 2026. No van de memoria.

### No compres nada más

GoDaddy va a ofrecerte hosting, correo profesional, certificado SSL y constructor de páginas.
No necesitas ninguno. El hosting es gratis en GitHub Pages, el certificado lo emite GitHub
solo, y el correo ya existe.

---

## Parte 3 · Después de los registros

1. Los cambios de DNS tardan entre unos minutos y una hora en propagarse. A veces más.
2. Cuando GitHub detecte el dominio, en la configuración de Pages aparece una casilla que dice
   **"Enforce HTTPS"**. Hay que activarla. Puede tardar un rato en habilitarse porque GitHub
   primero emite el certificado.
3. Prueba las cuatro direcciones: `desdedondeestes.co`, `www.desdedondeestes.co`, y las dos
   con `https://` delante. Las cuatro tienen que terminar en el sitio, con candado.
4. Abre el enlace desde otro teléfono, con datos móviles, antes de mandárselo a nadie.

---

## Si algo sale mal

**Sale la página de estacionamiento de GoDaddy.** Quedó el registro A viejo. Vuelve a la zona
DNS y bórralo.

**Sale error de certificado.** El certificado todavía no se emitió. Espera y vuelve a intentar
"Enforce HTTPS" más tarde.

**Sale 404 de GitHub.** El archivo `CNAME` del repositorio no coincide con el dominio, o Pages
no está apuntando a la rama correcta. Eso lo reviso yo.

**Todo se puede deshacer.** El sitio es un archivo HTML: si un día quieres moverlo a otro
hosting, se cambian los registros DNS y los enlaces que la gente ya compartió siguen sirviendo
igual. Ese fue el argumento para tener dominio propio.
