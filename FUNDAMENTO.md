# Fundamento de «Ciudades al azar»

## Alcance de la lectura

Se examinaron visualmente las seis hojas escaneadas del archivo `ECONOMIA ESPACIAL KRUGMAN Y FUJITA_C11.pdf`: contienen el final de p. 212 y el capítulo 11 completo, pp. 213–223. El documento no tiene capa de texto. Las referencias siguientes corresponden a la numeración impresa, no al número de hoja PDF. Los capítulos anteriores completos no se pudieron consultar: el libro original excedía el límite de transferencia. Las conexiones se basan en la recapitulación explícita del capítulo 11 y deben distinguirse de una revisión directa de los capítulos 1 y 10.

## Zipf: hecho estilizado, no motor del juego

En pp. 213–215, el número de ciudades por encima de un tamaño S se aproxima mediante N(S)=k S^(-a), con a cercano a 1. La regla rango-tamaño equivalente es S(r)=C r^(-1/a); para a=1, la segunda ciudad tiene la mitad del tamaño de la primera, la tercera un tercio, etc. El capítulo informa para las áreas metropolitanas estadounidenses ln(N)=10,549−1,004 ln(S). También advierte dificultades de comparabilidad de las definiciones urbanas y la importancia de estudiar la cola superior.

El juego pone **rango en el eje horizontal y población en el vertical**, ambos logarítmicos. Las figuras del libro usan la orientación inversa; por eso la pendiente teórica del juego es −1/a, no −a. Zipf tiene pendiente −1 en ambas orientaciones. La línea Zipf se ancla al tamaño de la ciudad más grande observada: es una referencia normalizada, no una regresión ni una ciudad observada. El gráfico usa los 50 mayores tamaños para observar la cola superior, tal como la simulación de p. 219. Los empates se ordenan por identificador, sin significado económico.

La pendiente descriptiva mostrada es OLS de log(S) sobre log(r) para esos puntos. No estima rigurosamente una cola de Pareto; no tiene intervalos de confianza, selección estadística de umbral ni prueba de bondad de ajuste. La desviación de la ciudad seleccionada es 100 [S(r)/(S(1)/r)−1]. No se otorga puntuación por acercarse a Zipf ni se altera la simulación para conseguirlo.

## Simon: mecanismo y supuestos (pp. 217–219)

La población está compuesta por unidades indivisibles de igual tamaño, los «trozos» del libro. No son años ni habitantes empíricamente calibrados. En cada paso se agrega exactamente una unidad:

1. Con probabilidad constante π, nace una ciudad de una unidad.
2. Con probabilidad 1−π, la unidad se suma a una ciudad existente i con probabilidad condicional S_i/P.

Así, Pr(i recibe la unidad)=(1−π)S_i/P y E[ΔS_i]/S_i=(1−π)/P. Las ciudades grandes reciben más unidades en términos absolutos; la tasa esperada proporcional es la misma. No hay ventajas productivas, tamaño óptimo, distancias, decisiones de localización optimizadoras, comercio, congestión ni desaparición. El mapa es una representación visual: ubicación, bosques y río no intervienen en el algoritmo.

Se comienza con diez ciudades de una unidad y se llega a P=1.000; esto reproduce las condiciones ilustrativas de p. 219 para π=0,2 (multiplicación de población por cien). El jugador puede elegir π=0,05 o π=0,2 antes de empezar. Se ofrece una historia alternativa que cambia únicamente π, con igual semilla y población final; no se cambia π a mitad de una trayectoria que luego se presenta como estacionaria. La semilla es visible y exportable. No se limita el número de ciudades al número de edificios detallados: todas participan y las pequeñas se muestran como puntos.

En estado asintótico, suponiendo estabilidad de n_S/P, la ecuación [11.3] es:

    n_S / n_(S−1) = (1−π)(S−1) / [(1−π)S + 1].

Su aproximación para S grande produce una densidad con elasticidad −a−1 y a=1/(1−π), ecuaciones [11.5]–[11.6]. Para π=0,2, a=1,25 y la pendiente rango-tamaño esperada es −0,8. Para π=0,05, a≈1,053 y la pendiente es −0,95. Estas son relaciones de cola **asintóticas**, no garantías para las primeras 1.000 unidades. El juego muestra esta advertencia junto al gráfico y en el cierre.

## El problema que no debe ocultarse (pp. 220–221)

Cuando π se acerca a cero, a se acerca a uno, pero la aproximación al estado estable requiere un crecimiento poblacional enorme. Con π=0 no nacen ciudades; no se puede inferir que un conjunto fijo de semillas converja por ello a Zipf. El capítulo critica que incluso el crecimiento histórico observado podría ser insuficiente para explicar la regularidad empírica mediante este mecanismo. El juego no ofrece π=0 como atajo a una Zipf perfecta y formula una pregunta explícita sobre esta limitación.

## Sistemas urbanos y aglomeración

En p. 213 y pp. 215–217 se recapitula la jerarquía urbana del capítulo 10: diferencias sectoriales de economías de escala y costes de transporte pueden dar lugar a ciudades de distintos órdenes. Su existencia no produce automáticamente Zipf. Ajustar unos parámetros para parecerse a un gráfico no explica una regularidad robusta.

En p. 216 se recapitula a Henderson, tratado en el capítulo 1: economías externas específicas de una industria y deseconomías ligadas al tamaño urbano global favorecen especialización y tamaños característicos según la función productiva. Pueden explicar diversidad, pero no establecen por sí solas una ley de potencia ni su estabilidad temporal. La conclusión de p. 223 confronta estas fuerzas centrípetas y centrífugas con el crecimiento proporcional de los modelos estocásticos.

La extensión territorial del juego **no implementa esos equilibrios económicos**. Es un experimento didáctico explícito para mostrar que introducir ventajas territoriales cambia los supuestos. Tras P=1.000 se bifurca el mismo estado en dos ramas y se agregan otras 1.000 unidades en cada una. Se conserva π y se usan los mismos sorteos de fundación y asignación (números aleatorios comunes) para reducir ruido en la comparación, sin pretender identificar un efecto empírico.

En el control se mantiene Simon. En la intervención:

    Pr(i | no fundación) = w_i S_i / Σ_j(w_j S_j).

El jugador elige una ciudad y un peso fijo: mercado w=2 (atracción ilustrativa), congestión w=0,5 (penalización ilustrativa), o w=1 (sin intervención). Los demás pesos son uno. El incremento proporcional esperado ahora depende del peso territorial; se rompe la neutralidad entre ciudades. Los factores son elecciones de diseño, no parámetros del libro. No hay presupuesto, bienestar, salarios, alquileres, firmas ni transporte modelados; por eso no se llama política óptima a ningún resultado. La congestión aquí es un peso exógeno, no una función endógena del tamaño. La intervención no afecta a la probabilidad de fundación y nunca se aplica a la rama de control.

Se elige el plan antes del crecimiento de las ramas. La ciudad objetivo se bloquea al confirmar o tras doce segundos; seleccionar otras ciudades después solo inspecciona información. Esto evita tratar como un único experimento una intervención que cambia silenciosamente de objetivo. Si no se toma una decisión, se ejecuta el control sin intervención y se indica en pantalla.

## Secuencia y discusión crítica

El reloj comienza con las instrucciones: 20 s de preparación, 75 s de Simon, 35 s de lectura de resultados, 70 s de experimento (hasta 12 s para decidir) y 40 s de conclusiones: **240 s en total**. Se pueden adelantar fases. El reloj no se pausa al abrir la ficha, y recupera el tiempo transcurrido si la pestaña pierde foco; la conclusión queda disponible después del final. El jugador observa, formula una predicción, decide π, selecciona una ciudad, aplica una regla y responde dos preguntas. No hay victoria por tamaño ni incentivos para confundir concentración con bienestar.

Los aprendizajes comprobados con las preguntas son: (1) las ciudades grandes tienen más crecimiento absoluto, no mayor tasa proporcional esperada en Simon; (2) π pequeño no garantiza Zipf en una muestra corta, debido a la lenta convergencia. El cierre invita además a preguntar: ¿una pendiente parecida demuestra un mecanismo?, ¿qué cambia al delimitar ciudades de otra forma?, ¿qué fuerzas económicas faltan?, ¿por qué una ciudad mayor no implica mayor bienestar?

## Otros modelos y límites de la representación

Las pp. 221–222 discuten Gibrat/Gabaix: independencia del tamaño tanto de la tasa como de su variación, con condiciones de borde; también mencionan conexiones espaciales aleatorias como conjetura. No se implementan ni se confunden con Simon. En particular, el crecimiento unitario de Simon no reproduce automáticamente todos los supuestos de varianza de Gibrat. La conclusión del capítulo presenta un enigma abierto en el marco del texto; el prototipo no declara que Simon lo resuelva.

La ambientación latinoamericana contemporánea es ficticia, sin calibración geográfica. Cada conjunto de edificios representa una ciudad; las manzanas no son unidades independientes de la distribución rango-tamaño. El terreno no es evidencia de accesibilidad ni de productividad, los edificios no representan sectores y las unidades no son población real. Los gráficos muestran simulaciones, nunca datos metropolitanos observados. Los resultados dependen de π, la semilla, el estado inicial y el horizonte. Para una presentación académica conviene anunciar estas diferencias al principio.
