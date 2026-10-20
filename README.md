# Ciudades al azar · versión guiada

Juego educativo sobre el capítulo 11 de *Economía espacial* de Fujita, Krugman y Venables, pp. 213–223. Ambientación de una región latinoamericana ficticia, con edificios, viviendas, plazas y avenidas.

Abre **Ciudades-al-azar.html** o **index.html** en un navegador moderno. No necesita conexión, instalación, cuentas ni servidor. La exposición tiene una guía de cinco minutos y tres pasos. Tú decides cuándo avanzar: el reloj no cierra explicaciones, no elige escenarios ni termina la partida.

1. **Mira:** los grupos van llegando y las ciudades crecen. El juego explica la regla de Simon en palabras y Zipf con tres barras.
2. **Decide y aplica:** primero aparece una explicación breve de Zipf, Simon y las fuerzas económicas. Después elige una ciudad, marca un escenario y pulsa **Aplicar mi decisión y ver qué pasa**. Marcar una opción solo crea una vista previa. No hay límite para confirmar: sin pulsar ese botón, la población espera y no se aplica ningún escenario.
3. **Compara:** una introducción muestra los tamaños observados y explica la diferencia con y sin intervención. Después explora las dos versiones de la ciudad. Puedes volver a la comparación con Zipf y responder una pregunta final.

Desde el segundo paso, el mapa ofrece las vistas **Atraen · centrípetas** y **Dispersan · centrífugas**. Selecciona un icono o usa el menú de ejemplos para leer su explicación. Son ocho mecanismos ilustrados; explorar no aplica ninguna intervención. Solo el escenario elegido cambia las probabilidades de llegada. La congestión no elimina población ni representa mudanzas.

El mapa ocupa una mayor parte de la pantalla. **Ver detalle** acerca la ciudad del escenario y **Ampliar mapa** abre una vista grande con sus controles y el reloj. Puedes cerrar esa vista con **Volver al juego** o **Escape**. El reloj sigue avanzando. Cambiar la cámara no altera las reglas ni el escenario.

El gráfico rango-tamaño logarítmico sigue disponible mediante «Ver gráfico rango-tamaño». Puedes volver a abrir la explicación breve con **Zipf, Simon y fuerzas**, también después de terminar. La explicación permanece abierta hasta que tú continúes. El reloj es orientativo y puede llegar a cero sin forzar ningún cambio. Las fórmulas, supuestos, fuentes y exportación JSON se encuentran en «Explicación del capítulo». El mapa, las barras y el gráfico permiten seleccionar ciudades; también hay un selector y controles con teclado. Solo los botones cambian de sección. «Completar llegadas y comparar» completa las 1.000 llegadas del experimento si aún quedaban grupos por llegar; después abre la introducción del paso 3. Volver a jugar genera otra semilla.

Consulta **FUNDAMENTO.md** para la justificación conceptual y **GUION.md** para presentar la experiencia. Las conexiones con los capítulos 1 y 10 proceden de su recapitulación en el capítulo 11; no se dispuso de esos capítulos completos.

Todos los recursos son dibujos locales con Canvas. Las verificaciones están en `tests/validate.py` (Playwright y Chromium solo son necesarios para desarrollo).

## Publicación

Sitio: https://franherreraneira.github.io/DatascienceCV/

`index.html` y el HTML descargable deben ser idénticos. La rama `gh-pages` sirve el sitio estático desde su raíz. `.nojekyll` evita el procesamiento con Jekyll. El paquete **Ciudades-al-azar-entrega.zip** incluye el juego autónomo y la documentación.
