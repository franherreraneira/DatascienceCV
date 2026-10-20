# Ciudades al azar · versión guiada

Juego educativo sobre el capítulo 11 de *Economía espacial* de Fujita, Krugman y Venables, pp. 213–223. Mapa esquemático de Chile con ciudades de nombres reales y poblaciones simuladas. Las ubicaciones son aproximadas y el ancho del país se amplía para facilitar la proyección.

Abre **Ciudades-al-azar.html** o **index.html** en un navegador moderno. No necesita conexión, instalación, cuentas ni servidor. La exposición tiene una guía de cinco minutos y tres pasos. Tú decides cuándo avanzar: el reloj no cierra explicaciones, no elige escenarios ni termina la partida.

1. **Mira:** los grupos de personas van llegando y las ciudades crecen. El juego explica la regla de Simon en palabras y Zipf con tres barras.
2. **Decide y aplica:** primero aparece una explicación breve de Zipf, Simon y las fuerzas económicas. Después elige una ciudad, marca un escenario y pulsa **Aplicar mi decisión y ver qué pasa**. Marcar una opción solo crea una vista previa. No hay límite para confirmar: sin pulsar ese botón, la población espera y no se aplica ningún escenario.
3. **Compara:** una introducción muestra los tamaños observados y explica la diferencia con y sin intervención. Después explora las dos versiones de la ciudad. Puedes volver a la comparación con Zipf y responder una pregunta final.

Desde el segundo paso, el mapa ofrece las vistas **Atraen · centrípetas** y **Dispersan · centrífugas**. Selecciona un icono o usa el menú de ejemplos para leer su explicación. Son ocho mecanismos ilustrados; explorar no aplica ninguna intervención. Solo el escenario elegido cambia las probabilidades de llegada. La congestión no elimina población ni representa mudanzas.

Puedes **arrastrar el mapa** con la mano, acercar con **rueda o pellizco**, usar **+ / −**, restablecer con **⌂** y desplazarte con **Mayús + flechas**. **Buscar nombres** abre 304 referencias de ciudades y localidades, admite búsquedas sin tildes y centra el lugar. Los nombres se revelan según el zoom. La fuente GeoNames cubre ciudades de más de 1.000 habitantes o sedes administrativas: no se certifica que sea el inventario completo oficial del INE. Las referencias buscadas no se convierten en ciudades del modelo.

El mapa incluye costa, islas, relieve, ríos y lagos esquemáticos. Los emplazamientos se buscan sobre tierra seca, con margen de seguridad y sin ocupar las parcelas rurales. Las ciudades nombradas siguen en el selector el recorrido propuesto desde Rancagua hasta Puerto Williams; no es una medición de distancias viales desde Santiago. Villarrica y Pucón, así como Ancud y Castro, se muestran por separado; Concepción / Talcahuano se mantiene como una entrada. Tras los 32 nombres, las fundaciones adicionales se llaman «Localidad simulada». Santiago aparece como referencia geográfica, sin añadir una ciudad al modelo.

Cinco áreas de agricultura, praderas y recursos rurales ilustran **factores inmóviles**: parte de la actividad se mantiene donde están la tierra y los recursos, fuera de grandes centros. En la vista de dispersión, elige «Factores inmóviles» o pulsa un campo del mapa para explorar esa explicación. Las parcelas tienen colores y surcos propios y se distinguen mejor con el mapa ampliado y el detalle. Esta capa es conceptual; no cambia las reglas de Simon ni simula población rural.

El mapa ocupa una mayor parte de la pantalla. **Ver detalle** acerca la ciudad del escenario y **Ampliar mapa** abre una vista grande con sus controles y el reloj. Puedes cerrar esa vista con **Volver al juego** o **Escape**. El reloj sigue avanzando. Cambiar la cámara no altera las reglas ni el escenario.

El gráfico rango-tamaño logarítmico sigue disponible mediante «Ver gráfico rango-tamaño». Puedes volver a abrir la explicación breve con **Zipf, Simon y fuerzas**, también después de terminar. La explicación permanece abierta hasta que tú continúes. El reloj es orientativo y puede llegar a cero sin forzar ningún cambio. Las fórmulas, supuestos, fuentes y exportación JSON se encuentran en «Explicación del capítulo». El mapa, las barras y el gráfico permiten seleccionar ciudades; también hay un selector y controles con teclado. Solo los botones cambian de sección. «Completar llegadas y comparar» completa las 1.000 llegadas del experimento si aún quedaban grupos por llegar; después abre la introducción del paso 3. Volver a jugar genera otra semilla.

**Chile: de Zipf a la primacía** abre una exploración histórica independiente: la figura 4 de Aroca y Atienza (2016), con sus doce coeficientes entre 1885 y 2002, y las cifras orientativas aportadas para 34 ciudades en 1885–1940. El mapa y las barras cambian con el año; el deslizador permite leer los coeficientes del artículo. Las cifras de ciudades están pendientes de cotejo censal y no son la base de esa figura. Se explican la centralización y las instituciones como argumentos del artículo, sin atribuir la historia chilena al sorteo de Simon. Abrir el buscador o la historia pausa la simulación y su reloj; no cambia decisiones ni resultados. El avance principal sigue siendo manual y los cinco minutos son una referencia.

**FUENTES_CHILE.md** documenta fuentes, unidades, licencias y limitaciones; los archivos de `data/` permiten revisar las cifras. Los datos geográficos GeoNames/lutangar tienen licencia CC BY 4.0; el código conserva su licencia original. No se necesitan esos archivos externos para jugar, pues los datos se incluyen también dentro de cada HTML.

Consulta **FUNDAMENTO.md** para la justificación conceptual y **GUION.md** para presentar la experiencia. Las conexiones con los capítulos 1 y 10 proceden de su recapitulación en el capítulo 11; no se dispuso de esos capítulos completos.

Todos los recursos son dibujos locales con Canvas. Las verificaciones están en `tests/validate.py` (Playwright y Chromium solo son necesarios para desarrollo).

## Publicación

Sitio: https://franherreraneira.github.io/DatascienceCV/

`index.html` y el HTML descargable deben ser idénticos. La rama `gh-pages` sirve el sitio estático desde su raíz. `.nojekyll` evita el procesamiento con Jekyll. El paquete **Ciudades-al-azar-entrega.zip** incluye el juego autónomo y la documentación.
