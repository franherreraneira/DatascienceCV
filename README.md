# Ciudades al azar · versión guiada

Juego educativo sobre el capítulo 11 de *Economía espacial* de Fujita, Krugman y Venables, pp. 213–223. Ambientación de una región latinoamericana ficticia, con edificios, viviendas, plazas y avenidas.

Abre **Ciudades-al-azar.html** o **index.html** en un navegador moderno. No necesita conexión, instalación, cuentas ni servidor. La partida dura como máximo cuatro minutos y tiene tres pasos:

1. **Mira:** los grupos van llegando y las ciudades crecen. El juego explica la regla de Simon en palabras y Zipf con tres barras.
2. **Elige:** selecciona una ciudad y prueba un mercado, congestión o deja todo igual. Tienes hasta treinta segundos; sin respuesta se conserva el crecimiento original.
3. **Compara:** observa esa ciudad con tu decisión y sin intervención. Puedes volver a la comparación con Zipf y responder una pregunta final.

Desde el segundo paso, el mapa ofrece las vistas **Atraen · centrípetas** y **Dispersan · centrífugas**. Selecciona un icono o usa el menú de ejemplos para leer su explicación. Son ocho mecanismos ilustrados; explorar no aplica ninguna intervención. Solo el escenario elegido cambia las probabilidades de llegada. La congestión no elimina población ni representa mudanzas.

El gráfico rango-tamaño logarítmico sigue disponible mediante «Ver gráfico rango-tamaño». Las fórmulas, supuestos, fuentes y exportación JSON se encuentran en «Explicación del capítulo». El mapa, las barras y el gráfico permiten seleccionar ciudades; también hay un selector y controles con teclado. Los botones permiten avanzar más rápido. Volver a jugar genera otra semilla.

Consulta **FUNDAMENTO.md** para la justificación conceptual y **GUION.md** para presentar la experiencia. Las conexiones con los capítulos 1 y 10 proceden de su recapitulación en el capítulo 11; no se dispuso de esos capítulos completos.

Todos los recursos son dibujos locales con Canvas. Las verificaciones están en `tests/validate.py` (Playwright y Chromium solo son necesarios para desarrollo).

## Publicación

Sitio: https://franherreraneira.github.io/DatascienceCV/

`index.html` y el HTML descargable deben ser idénticos. La rama `gh-pages` sirve el sitio estático desde su raíz. `.nojekyll` evita el procesamiento con Jekyll. El paquete **Ciudades-al-azar-entrega.zip** incluye el juego autónomo y la documentación.
