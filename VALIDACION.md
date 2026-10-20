# Validación de la versión guiada

Se ejecutó `python3 tests/validate.py` con Playwright y Chromium: **82 comprobaciones aprobadas**. El juego no necesita estas herramientas para ejecutarse.

Se verificaron las tres etapas, las instrucciones sin selección de parámetros, la aparición progresiva de los controles y la secuencia automática completa de 300 segundos. La opción neutral se aplica si no hay confirmación en cuarenta y cinco segundos, después de la explicación breve y conserva exactamente el mismo resultado en ambas ramas. Confirmar el mercado fija su ciudad objetivo; inspeccionar otra ciudad después no lo mueve.

Las tres barras iniciales muestran tamaños reales en una escala lineal común; las referencias de Zipf están en la mitad y el tercio de la mayor. La selección de barras se vincula al mapa. El gráfico logarítmico de las cincuenta mayores se puede explorar por teclado y con clics. Los resultados presentan la ciudad objetivo en dos versiones, y la pregunta final distingue patrón y causa.

Se conservan población entera positiva, reproducción por semilla, nacimiento de ciudades y asignación proporcional. Las frecuencias condicionales se contrastaron con 30.000 sorteos independientes a un estado fijo. Ambas ramas reciben el mismo número de grupos y los mismos sorteos de fundación. También se comprobó la exportación JSON desde la ficha académica.

Se revisaron capturas de portada, barras de Zipf, comparación, proyección y móvil. La interfaz y el texto ampliado caben en 1366 × 768; a 390 px no hay desbordamiento horizontal y se usa desplazamiento vertical. El documento se ejecutó con la red desactivada, sin solicitudes externas ni errores JavaScript.

El Chromium administrado bloquea `file://`; por eso se ejecutó el contenido exacto del HTML mediante `set_content` en un contexto offline. No se alteraron políticas del navegador. Las pruebas locales no equivalen por sí solas a comprobar el despliegue público.

No se realizaron estudios con participantes: la simplificación de la interfaz está implementada y probada funcionalmente, pero su comprensión debe comprobarse con una persona durante el ensayo. No se afirma una mejora de aprendizaje medida empíricamente.

En la ampliación de fuerzas se verificó que Simon no dibuja flechas territoriales y que la capa conceptual aparece desde el segundo paso. Hay cuatro ejemplos centrípetos y cuatro centrífugos. El selector y los iconos actualizan la explicación; explorar no cambia población ni aplica escenarios. Se confirmó que el mercado selecciona la vista de atracción y la congestión, la de dispersión. El escenario de congestión reduce la llegada de grupos a la ciudad objetivo frente al control de la misma semilla, preserva la población previa y mantiene P=2.000 en ambas ramas. Las capturas incluyen atracción, dispersión y resultado con congestión.

Las tarjetas de fuerzas se reubican cuando la ciudad elegida queda en un borde, para no tapar su posición. Se comprobó la visibilidad de la ciudad seleccionada en la geometría del esquema.

En la versión de cinco minutos se comprobó que el reloj comienza en 5:00, que la partida sigue activa después de cuatro minutos y que termina automáticamente a los 300 segundos. La elección permanece abierta después de treinta segundos y se aplica la opción neutral al superar cuarenta y cinco. La vista ampliada mantiene una sola instancia del mapa, conserva sus controles y reloj, enfoca la ciudad del escenario y vuelve al juego con Escape o el botón, también en móvil. Ampliar o acercar no modifica la población. Se revisaron capturas del mapa completo y del detalle.

Se comprobó que la explicación breve aparece antes de la decisión y distingue patrón de tamaños, proceso aleatorio y mecanismos económicos. Durante ella no crece la población. Puede continuarse con su botón o avanzar automáticamente a los treinta segundos. Se comprobó también el cambio seguro desde el mapa ampliado y la posibilidad de repasar después de terminar, sin alterar resultados. En móvil, la explicación comienza mostrando el título y no salta al botón situado al final; no tiene desbordamiento horizontal.

Marcar un escenario mantiene el peso original, muestra una vista previa y activa un botón de aplicación independiente. Solo la confirmación modifica el escenario. Una selección de mercado no confirmada se ignora al agotarse el tiempo y se continúa con la regla neutral. La exportación conserva la selección pendiente y el motivo de aplicación para distinguir ambos casos.
