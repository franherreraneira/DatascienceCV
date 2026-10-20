# Fundamento de «Ciudades al azar»

## Alcance de la lectura

Se examinaron visualmente las seis hojas escaneadas del archivo `ECONOMIA ESPACIAL KRUGMAN Y FUJITA_C11.pdf`: contienen el final de p. 212 y el capítulo 11 completo, pp. 213–223. El documento no tiene capa de texto. Las referencias siguientes corresponden a la numeración impresa, no al número de hoja PDF. Los capítulos anteriores completos no se pudieron consultar: el libro original excedía el límite de transferencia. Las conexiones se basan en la recapitulación explícita del capítulo 11 y deben distinguirse de una revisión directa de los capítulos 1 y 10. La ampliación visual de fuerzas recoge la síntesis aportada posteriormente por el usuario; no se verificaron directamente los capítulos 6, 17 y 18 ni la literalidad del cuadro 18.1.

## Versión guiada

La interfaz se organiza en tres momentos: mirar, elegir y comparar. La explicación inicial de Zipf usa tres barras de población en escala lineal, con marcas en el tamaño de la primera ciudad, su mitad y su tercio. El gráfico logarítmico de las 50 mayores sigue disponible mediante un botón. Las fórmulas, los supuestos y las referencias están en «Explicación del capítulo», fuera de las instrucciones principales. Esta simplificación de la interfaz no cambia el mecanismo probabilístico.

## Zipf: hecho estilizado, no motor del juego

En pp. 213–215, el número de ciudades por encima de un tamaño S se aproxima mediante N(S)=k S^(-a), con a cercano a 1. La regla rango-tamaño equivalente es S(r)=C r^(-1/a); para a=1, la segunda ciudad tiene la mitad del tamaño de la primera, la tercera un tercio, etc. El capítulo informa para las áreas metropolitanas estadounidenses ln(N)=10,549−1,004 ln(S). También advierte dificultades de comparabilidad de las definiciones urbanas y la importancia de estudiar la cola superior.

El gráfico opcional pone **rango en el eje horizontal y población en el vertical**, ambos logarítmicos. Las barras iniciales ordenan las tres mayores de arriba abajo y representan sus tamaños en una escala lineal común. Las figuras del libro usan la orientación inversa; por eso la pendiente teórica del juego es −1/a, no −a. Zipf tiene pendiente −1 en ambas orientaciones. La línea Zipf se ancla al tamaño de la ciudad más grande observada: es una referencia normalizada, no una regresión ni una ciudad observada. El gráfico usa los 50 mayores tamaños para observar la cola superior, tal como la simulación de p. 219. Los empates se ordenan por identificador, sin significado económico.

La pendiente descriptiva guardada en la exportación es OLS de log(S) sobre log(r) para esos puntos. No estima rigurosamente una cola de Pareto; no tiene intervalos de confianza, selección estadística de umbral ni prueba de bondad de ajuste. La desviación frente a Zipf se aprecia comparando el extremo de cada barra con la marca de referencia correspondiente. No se otorga puntuación por acercarse a Zipf ni se altera la simulación para conseguirlo.

## Simon: mecanismo y supuestos (pp. 217–219)

La población está compuesta por unidades indivisibles de igual tamaño, los «trozos» del libro. No son años ni habitantes empíricamente calibrados. En cada paso se agrega exactamente una unidad:

1. Con probabilidad constante π, nace una ciudad de una unidad.
2. Con probabilidad 1−π, la unidad se suma a una ciudad existente i con probabilidad condicional S_i/P.

Así, Pr(i recibe la unidad)=(1−π)S_i/P y E[ΔS_i]/S_i=(1−π)/P. Las ciudades grandes reciben más unidades en términos absolutos; la tasa esperada proporcional es la misma. No hay ventajas productivas, tamaño óptimo, distancias, decisiones de localización optimizadoras, comercio, congestión ni desaparición. El mapa es una representación visual: ubicación, bosques y río no intervienen en el algoritmo.

Se comienza con diez ciudades de una unidad y se llega a P=1.000; esto reproduce las condiciones ilustrativas de p. 219 para π=0,2 (multiplicación de población por cien). En la versión guiada se fija π=0,2 para evitar pedir una decisión sobre un símbolo antes de explicar el mecanismo. Se expresa como «uno de cada cinco grupos, en promedio», no como una secuencia determinista de cinco. La semilla queda en la exportación y cambia al volver a jugar. No se limita el número de ciudades al número de edificios detallados: todas participan y las pequeñas se muestran como puntos.

En estado asintótico, suponiendo estabilidad de n_S/P, la ecuación [11.3] es:

    n_S / n_(S−1) = (1−π)(S−1) / [(1−π)S + 1].

Su aproximación para S grande produce una densidad con elasticidad −a−1 y a=1/(1−π), ecuaciones [11.5]–[11.6]. Para π=0,2, a=1,25 y la pendiente rango-tamaño esperada es −0,8. Para π=0,05, a≈1,053 y la pendiente es −0,95. Estas son relaciones de cola **asintóticas**, no garantías para las primeras 1.000 unidades. La ficha académica conserva la relación asintótica y el problema de convergencia; la interfaz principal explica que las ciudades no tienen que coincidir con la referencia de Zipf.

## El problema que no debe ocultarse (pp. 220–221)

Cuando π se acerca a cero, a se acerca a uno, pero la aproximación al estado estable requiere un crecimiento poblacional enorme. Con π=0 no nacen ciudades; no se puede inferir que un conjunto fijo de semillas converja por ello a Zipf. El capítulo critica que incluso el crecimiento histórico observado podría ser insuficiente para explicar la regularidad empírica mediante este mecanismo. El juego no ofrece π=0 como atajo a una Zipf perfecta y mantiene esta limitación en la ficha académica para la discusión posterior.

## Sistemas urbanos y aglomeración

En p. 213 y pp. 215–217 se recapitula la jerarquía urbana del capítulo 10: diferencias sectoriales de economías de escala y costes de transporte pueden dar lugar a ciudades de distintos órdenes. Su existencia no produce automáticamente Zipf. Ajustar unos parámetros para parecerse a un gráfico no explica una regularidad robusta.

En p. 216 se recapitula a Henderson, tratado en el capítulo 1: economías externas específicas de una industria y deseconomías ligadas al tamaño urbano global favorecen especialización y tamaños característicos según la función productiva. Pueden explicar diversidad, pero no establecen por sí solas una ley de potencia ni su estabilidad temporal. La conclusión de p. 223 confronta estas fuerzas centrípetas y centrífugas con el crecimiento proporcional de los modelos estocásticos.

La extensión territorial del juego **no implementa esos equilibrios económicos**. Es un experimento didáctico explícito para mostrar que introducir ventajas territoriales cambia los supuestos. Tras P=1.000 se bifurca el mismo estado en dos ramas y se agregan otras 1.000 unidades en cada una. Se conserva π y se usan los mismos sorteos de fundación y asignación (números aleatorios comunes) para reducir ruido en la comparación, sin pretender identificar un efecto empírico.

En el control se mantiene Simon. En la intervención:

    Pr(i | no fundación) = w_i S_i / Σ_j(w_j S_j).

El jugador elige una ciudad y una sola acción: instalar un mercado w=2 (atracción ilustrativa), probar congestión w=0,5 (dispersión ilustrativa) o dejar todo igual w=1 (sin intervención). Los demás pesos son uno. El incremento proporcional esperado ahora depende del peso territorial; se rompe la neutralidad entre ciudades. Los factores son elecciones de diseño, no parámetros del libro. No hay presupuesto, bienestar, salarios, alquileres, firmas ni transporte modelados; por eso no se llama política óptima a ningún resultado. La intervención no afecta a la probabilidad de fundación y nunca se aplica a la rama de control.

Se elige el plan antes del crecimiento de las ramas. La ciudad objetivo se bloquea al confirmar o tras treinta segundos sin respuesta; seleccionar otras ciudades después solo inspecciona información. Esto evita tratar como un único experimento una intervención que cambia silenciosamente de objetivo. Si no se toma una decisión, se ejecuta el control sin intervención y se indica en pantalla.

## Fuerzas visibles: una capa conceptual separada

Las fuerzas se muestran solo a partir del segundo paso. El primer paso conserva Simon sin fuerzas territoriales. Dos vistas permiten explorar cuatro ejemplos centrípetos y cuatro centrífugos mediante iconos, flechas y un selector accesible. Seleccionar una vista o un icono no modifica la población, el azar, el objetivo ni el escenario. Elegir un escenario fija una única regla; inspeccionar otras fuerzas después no la sustituye.

Las flechas hacia dentro representan tendencias de concentración; las flechas hacia fuera, tendencias de dispersión. Los puntos animados no son habitantes, empresas observadas ni trayectorias de migración; no se cuentan como grupos. Color y grosor sirven para destacar el ejemplo seleccionado, no para medir intensidad ni estimar un balance. Se respeta la preferencia de movimiento reducido del navegador.

| Fuerza | Imagen y explicación | Tradición teórica orientativa |
| --- | --- | --- |
| Vinculaciones de mercado | Fábrica conectada: proximidad entre clientes y proveedores. | Hirschman; Krugman, Fujita y Venables. |
| Mercado de trabajo denso | Personas: más opciones para empresas y trabajadores especializados. | Marshall. |
| Circulación de conocimientos | Bombilla: aprendizaje y transmisión de ideas por proximidad. | Marshall y Jacobs, con mecanismos distintos. |
| Acceso a demanda | Bolsa comercial: cercanía a compradores y menores costes de entrega. | Harris y Pred; la competencia monopolística de Dixit y Stiglitz es una herramienta de modelización. |
| Factores inmóviles | Terreno cultivado: recursos y actividad que permanecen en su localización. | von Thünen; sector agrícola inmóvil en Krugman. |
| Suelo y vivienda caros | Casa y precio: competencia por espacio que puede favorecer otras localizaciones. | von Thünen, Alonso, Mills y Muth. |
| Congestión | Vehículos: tráfico y costes urbanos que reducen atracción. | Henderson y la tradición de deseconomías urbanas. |
| Abastecimiento a distancia | Camión: coste de trasladar alimentos y materias primas. | Bairoch y economía espacial. |

Esta tabla es una síntesis conceptual para el prototipo, no una transcripción verificada del cuadro 18.1. No se atribuye todo mecanismo urbano a una sola persona. Los spillovers sectoriales de Marshall y la diversidad urbana destacada por Jacobs no son idénticos. Dixit y Stiglitz no se presentan como autores de una teoría completa de localización o del potencial de mercado por sí solos.

**Qué cambia realmente el algoritmo:** solo el escenario de mercado (peso 2), congestión (peso 0,5) o neutral (peso 1). No hay ocho ecuaciones de fuerzas ni una suma de intensidades. No se calculan alquileres, empleo, vínculos insumo-producto, innovación, transporte o equilibrio endógeno. La versión de congestión representa menor probabilidad de recibir población nueva: no elimina grupos existentes y permite que la ciudad siga creciendo. Esta regla exógena no reproduce la evacuación de habitantes ni una función de congestión que dependa del tamaño.

El control siempre conserva Simon. Las dos ramas mantienen iguales la población total y los sorteos de fundación, y ninguna flecha garantiza Zipf. Tampoco se modela la apertura al comercio internacional: una ilustración de fuerzas no permite inferir los resultados del capítulo 17.

## Secuencia y discusión crítica

El reloj comienza al pulsar «Empezar». Hay **80 s para mirar**, **90 s para elegir y observar la intervención**, y **70 s para comparar y concluir**: 240 s en total. Los primeros 15 s presentan la regla con diez ciudades iguales; durante los siguientes 50 s se simulan las llegadas hasta P=1.000 y los últimos 15 s introducen la comparación con Zipf. Se permite avanzar antes.

En el segundo momento hay hasta treinta segundos para elegir una ciudad y pulsar «Instalar un mercado», «Probar congestión» o «Dejar todo igual». Pulsar una opción la fija y comienza el crecimiento de ambas ramas; el tiempo restante de esa etapa se usa para añadir otras 1.000 unidades. Si no hay respuesta, se aplica la opción neutral al cumplirse treinta segundos. Se conserva un único objetivo para todo el experimento. En el tercer momento se compara esa ciudad con su contrafactual sin intervención; una pestaña permite explorar Zipf aparte, evitando presentar simultáneamente todos los resultados.

El reloj no se pausa al abrir la ficha y recupera el tiempo transcurrido cuando la pestaña vuelve a estar visible. Las conclusiones y los gráficos quedan disponibles después del final. No hay victoria por tamaño ni incentivos para confundir concentración con bienestar.

La única pregunta del cierre comprueba una distinción concreta: parecerse a Zipf no demuestra la causa del crecimiento. Los conceptos matemáticos sobre tasas esperadas, exponentes y convergencia no se evalúan en la interfaz breve; quedan disponibles para discusión académica. La conversación posterior puede preguntar qué cambia al delimitar ciudades de otra forma, qué fuerzas económicas faltan y por qué una ciudad mayor no implica mayor bienestar.

## Otros modelos y límites de la representación

Las pp. 221–222 discuten Gibrat/Gabaix: independencia del tamaño tanto de la tasa como de su variación, con condiciones de borde; también mencionan conexiones espaciales aleatorias como conjetura. No se implementan ni se confunden con Simon. En particular, el crecimiento unitario de Simon no reproduce automáticamente todos los supuestos de varianza de Gibrat. La conclusión del capítulo presenta un enigma abierto en el marco del texto; el prototipo no declara que Simon lo resuelva.

La ambientación latinoamericana contemporánea es ficticia, sin calibración geográfica. Cada conjunto de edificios representa una ciudad; las manzanas no son unidades independientes de la distribución rango-tamaño. El terreno no es evidencia de accesibilidad ni de productividad, los edificios que cuentan población no representan sectores productivos; los iconos de fuerzas son un esquema aparte y las unidades no son población real. Los gráficos muestran simulaciones, nunca datos metropolitanos observados. Los resultados dependen de π, la semilla, el estado inicial y el horizonte. Para una presentación académica conviene anunciar estas diferencias al principio.
