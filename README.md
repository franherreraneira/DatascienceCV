# Ciudades al azar

Prototipo educativo offline para una exposición sobre Fujita, Krugman y Venables, *Economía espacial*, capítulo 11, «Una digresión empírica: el tamaño de las ciudades», pp. 213–223 del PDF proporcionado.

Abre **Ciudades-al-azar.html** con doble clic en un navegador moderno. No necesita instalación, servidor, conexión ni cuentas. Todos los gráficos se dibujan localmente. La partida dura como máximo 4 minutos desde «Comenzar simulación»; los controles permiten adelantar etapas. La ficha académica y esta documentación se consultan fuera del tiempo de exposición.

El mapa y el gráfico permiten seleccionar ciudades. También hay un selector accesible con teclado. El experimento territorial permite decidir durante sus primeros 12 segundos; luego el plan se bloquea para que la comparación conserve una intervención definida. Sin decisión, se continúa sin intervención. Se pueden exportar los resultados como JSON y volver a jugar con otra semilla.

Consulta **FUNDAMENTO.md** para las ecuaciones, fuentes por página, limitaciones y conexiones con sistemas urbanos. Las referencias a los capítulos 1 y 10 proceden de la discusión que hace el capítulo 11: no se dispuso de esos capítulos completos.

Los recursos visuales son dibujos originales generados con Canvas; muestran edificios contemporáneos, viviendas, plazas, avenidas y buses, sin recursos externos. No hay suite de construcción ni dependencias. Las verificaciones del prototipo están en `tests/validate.py` (requiere Playwright y Chromium únicamente para desarrollo, no para jugar).

## Publicación web

`index.html` es una copia autónoma del juego y `.nojekyll` permite servirlo como sitio estático. La rama `gh-pages` se prepara como fuente de publicación. Si GitHub Pages aún no está activado, entra a **Settings → Pages**, elige **Deploy from a branch**, selecciona **gh-pages** y **/(root)** y guarda. La URL del sitio solo debe anunciarse como operativa después de comprobar el despliegue.

Para descargar sin ejecutar: abre `Ciudades-al-azar-entrega.zip` en el repositorio de GitHub y usa **Download raw file**.
