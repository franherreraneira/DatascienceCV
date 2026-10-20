# Fuentes del caso histórico y del catálogo geográfico

## Aroca y Atienza (2016)

Aroca, Patricio y Atienza, Miguel. «Spatial concentration in Latin America and the role of institutions». *Investigaciones Regionales – Journal of Regional Research*, 36, pp. 233–253. PDF aportado en la conversación: `Dialnet-SpatialConcentrationInLatinAmericaAndTheRoleOfInst-5819481.pdf`. Se revisaron la sección 2.1, pp. 240–241, la figura 4 visualmente y la discusión institucional de la sección 2.2 y las conclusiones.

La figura 4, p. 241, atribuye su serie a Vallone y Atienza (2012), *Concentration, development and evolution of the urban system in Chile between 1885 and 2002*, WP2012-03, Universidad Católica del Norte. Los doce rótulos se transcribieron, sin estimar ni interpolar valores, a `data/coeficiente-zipf-paper.csv`:

| Año | Coeficiente publicado |
| --- | ---: |
| 1885 | 1,107 |
| 1895 | 1,021 |
| 1907 | 1,045 |
| 1920 | 0,993 |
| 1930 | 0,993 |
| 1940 | 0,989 |
| 1952 | 0,960 |
| 1960 | 0,918 |
| 1970 | 0,877 |
| 1982 | 0,832 |
| 1992 | 0,824 |
| 2002 | 0,825 |

El artículo describe proximidad a Zipf durante las primeras cuatro décadas del siglo XX y una creciente asimetría desde los años 1940. Su coeficiente disminuye; no se debe sustituir mecánicamente por la pendiente log(tamaño) frente a log(rango) del gráfico del juego, cuyos ejes y convención están declarados. El gráfico histórico usa observaciones censales como categorías: el espacio entre puntos no representa intervalos temporales iguales.

La expansión de la urbanización y de la industrialización por sustitución de importaciones aparece en el relato de la concentración inicial. Para su persistencia, los autores discuten dependencia de trayectoria, centralización política y fiscal, propiedad del capital, capital humano, innovación y compras públicas (pp. 240–250). El juego presenta sus argumentos y evidencias; no simula efectos causales ni calibra una política institucional con esos coeficientes.

La figura 3 utiliza la Región Metropolitana y población nacional, con fuentes censales y CASEN; el texto menciona aproximadamente 11% al inicio del siglo XX, más de 30% al inicio de los años 1970 y alrededor de 40% en 2002. Se atribuyen al artículo y requieren revisar unidades y comparabilidad antes de un análisis censal propio. Santiago ciudad, Gran Santiago y Región Metropolitana no son unidades intercambiables. El documento es de 2016 y no informa la situación actual de 2026.

## Poblaciones aportadas en la conversación

`data/poblaciones-aportadas.csv` reproduce las cifras que el usuario proporcionó para 34 ciudades y cinco años: 1885, 1907, 1920, 1930 y 1940. **No se verificaron con las tablas censales originales y no figuran como esa tabla en el paper.** Se presentan como cifras orientativas aportadas, pendientes de cotejo censal, no como datos censales certificados ni como la base con la que se calculó la figura 4.

Los signos `~` se conservan. Un campo vacío y `—` en pantalla significan dato ausente, nunca cero. No se interpola. Las fechas de fundación indicadas para Coyhaique y Puerto Natales proceden igualmente del mensaje del usuario. Las coordenadas utilizadas para situar esta muestra son geográficas de referencia, no delimitaciones urbanas históricas.

Por ejemplo, con esas cifras Santiago pasa de 190.000 a 952.000 habitantes, mientras Valparaíso pasa de 115.000 a 209.900. La razón primera/segunda de esta muestra aumenta de aproximadamente 1,65 a 4,54. No equivale a participación nacional, no demuestra causalidad y no permite reproducir el coeficiente del sistema urbano completo. Las áreas de los círculos del mapa histórico son proporcionales a habitantes; las barras comparan los mayores tamaños de la muestra.

## Catálogo de nombres

Fuente: GeoNames, distribuida mediante **lutangar/cities.json**, https://github.com/lutangar/cities.json, consultada el 20 de octubre de 2026. Archivo original: https://raw.githubusercontent.com/lutangar/cities.json/master/cities.json. Licencia declarada: **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/. Fuentes de GeoNames: https://www.geonames.org/datasources/.

Se extrajeron los registros con país `CL`, se conservaron los nombres y coordenadas, se añadió el ancla de la conversación que faltaba y se ordenaron por latitud. Se eliminaron una duplicación cercana de Cañete y un registro de Vallenar con longitud inconsistente. Se retienen homónimos de El Carmen con sus coordenadas. El resultado tiene **304 referencias** y se entrega en `data/catalogo-ciudades-chile.json`; la procedencia y modificaciones están en ese archivo. Los datos derivados mantienen la atribución y la licencia CC BY 4.0 para los registros de esa fuente; los nombres añadidos se identifican por separado.

La cobertura declarada por la fuente comprende ciudades de más de 1.000 habitantes o sedes administrativas. **No se verificó que sea el inventario completo y oficial de ciudades, pueblos y entidades del INE.** Comunas, ciudades, localidades y áreas metropolitanas tienen definiciones diferentes. El acceso directo al inventario del INE estuvo bloqueado por la conectividad del entorno; no se sustituyó esa verificación por una afirmación de exhaustividad.

Las referencias se dibujan y buscan independientemente de los 24 núcleos iniciales del escenario. Buscar no funda ciudades ni cambia una probabilidad. El etiquetado se restringe a las 16 capitales regionales; todos los del catálogo están en el buscador. Los territorios insulares alejados se representan mediante recuadros esquemáticos fuera de su posición continental, identificados como referencias insulares. No se usa distancia dibujada como variable económica.

El código del prototipo conserva su licencia original; los registros geográficos incorporados tienen la licencia y atribución anteriores. La distribución incluye los datos derivados editables. No se redistribuye el libro ni el PDF del artículo en el paquete.

## Estado inicial ilustrativo del escenario chileno

`data/escenario-chileno.csv` no procede de GeoNames, del paper ni de una tabla censal. Es una decisión didáctica solicitada para representar una jerarquía encabezada por el Gran Santiago: 24 núcleos, 6.000 grupos abstractos, de los cuales 3.000 se asignan a ese núcleo y 550 a cada uno de Gran Concepción y Gran Valparaíso. Los demás pesos permiten representar centros secundarios, incluido Rengo, con menor tamaño inicial. La ventaja inicial y las 2.000 llegadas del horizonte aseguran que Gran Santiago conserve la primacía sin manipular los sorteos. Las ubicaciones metropolitanas son anclas ilustrativas, no delimitaciones oficiales. No se deben interpretar las participaciones de esta muestra simulada como proporciones nacionales observadas.
