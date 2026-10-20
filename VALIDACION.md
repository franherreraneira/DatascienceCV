# Validación de la versión guiada

Se ejecutó `python3 tests/validate.py` con Playwright y Chromium: **55 comprobaciones aprobadas**. El juego no necesita estas herramientas para ejecutarse.

Se verificaron las tres etapas, las instrucciones sin selección de parámetros, la aparición progresiva de los controles y la secuencia automática completa de 240 segundos. La opción neutral se aplica si no hay respuesta en treinta segundos y conserva exactamente el mismo resultado en ambas ramas. Instalar el mercado fija su ciudad objetivo; inspeccionar otra ciudad después no lo mueve.

Las tres barras iniciales muestran tamaños reales en una escala lineal común; las referencias de Zipf están en la mitad y el tercio de la mayor. La selección de barras se vincula al mapa. El gráfico logarítmico de las cincuenta mayores se puede explorar por teclado y con clics. Los resultados presentan la ciudad objetivo en dos versiones, y la pregunta final distingue patrón y causa.

Se conservan población entera positiva, reproducción por semilla, nacimiento de ciudades y asignación proporcional. Las frecuencias condicionales se contrastaron con 30.000 sorteos independientes a un estado fijo. Ambas ramas reciben el mismo número de grupos y los mismos sorteos de fundación. También se comprobó la exportación JSON desde la ficha académica.

Se revisaron capturas de portada, barras de Zipf, comparación, proyección y móvil. La interfaz y el texto ampliado caben en 1366 × 768; a 390 px no hay desbordamiento horizontal y se usa desplazamiento vertical. El documento se ejecutó con la red desactivada, sin solicitudes externas ni errores JavaScript.

El Chromium administrado bloquea `file://`; por eso se ejecutó el contenido exacto del HTML mediante `set_content` en un contexto offline. No se alteraron políticas del navegador. Las pruebas locales no equivalen por sí solas a comprobar el despliegue público.

No se realizaron estudios con participantes: la simplificación de la interfaz está implementada y probada funcionalmente, pero su comprensión debe comprobarse con una persona durante el ensayo. No se afirma una mejora de aprendizaje medida empíricamente.

En la ampliación de fuerzas se verificó que Simon no dibuja flechas territoriales y que la capa conceptual aparece desde el segundo paso. Hay cuatro ejemplos centrípetos y cuatro centrífugos. El selector y los iconos actualizan la explicación; explorar no cambia población ni aplica escenarios. Se confirmó que el mercado selecciona la vista de atracción y la congestión, la de dispersión. El escenario de congestión reduce la llegada de grupos a la ciudad objetivo frente al control de la misma semilla, preserva la población previa y mantiene P=2.000 en ambas ramas. Las capturas incluyen atracción, dispersión y resultado con congestión.

Las tarjetas de fuerzas se reubican cuando la ciudad elegida queda en un borde, para no tapar su posición. Se comprobó la visibilidad de la ciudad seleccionada en la geometría del esquema.
