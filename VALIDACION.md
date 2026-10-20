# Validación de la versión guiada con avance manual

Se ejecutó `python3 tests/validate.py` con Playwright y Chromium: **96 comprobaciones aprobadas**. El juego no necesita estas herramientas para ejecutarse.

Se verificaron las tres etapas y sus introducciones. Esperar diez minutos no cambia de etapa, no cierra la explicación y no aplica un escenario por defecto. Una selección pendiente mantiene el peso original y P=1.000 hasta confirmar. Solo «Aplicar mi decisión y ver qué pasa» fija la ciudad y el escenario. Confirmar después de una espera larga permite completar correctamente las nuevas llegadas. El reloj de cinco minutos es orientativo: llegar a cero no termina la partida; «Terminar» lo hace.

El paso 2 presenta la finalidad del experimento y distingue Zipf como patrón, Simon como proceso y las fuerzas como mecanismos económicos. El paso 3 introduce los tamaños inicial y finales reales, y explica la diferencia respecto del control. Se comprobaron mercado, congestión y neutral, además de una realización en la que un mercado cambia las probabilidades pero el tamaño final de su ciudad coincide con el control. Esa coincidencia se explica como un resultado observado, no como ausencia de cambio en la regla. La congestión significa menos llegadas nuevas frente al control, sin pérdida de población previa.

Las barras iniciales usan tamaños reales en escala lineal y referencias de Zipf en la mitad y el tercio de la mayor. La selección se vincula al mapa; el gráfico logarítmico de las cincuenta mayores admite teclado y clics. Explorar las ocho fuerzas ilustrativas no aplica intervenciones. Ampliar o acercar el mapa conserva el mismo modelo, sus controles y una sola instancia del lienzo; se vuelve con el botón o Escape.

Se conservan población entera positiva, reproducción por semilla, nacimiento de ciudades y asignación proporcional. Las frecuencias condicionales se contrastaron con 30.000 sorteos independientes a un estado fijo. Ambas ramas reciben el mismo total de grupos y los mismos sorteos de fundación. Se verificaron la exportación JSON, la pregunta sobre patrón y causa y la revisión de las explicaciones después de terminar.

Se revisaron capturas de portada, introducciones, mapa, comparación, proyección y móvil. La interfaz y el texto ampliado caben en 1366 × 768; a 390 px no hay desbordamiento horizontal y se usa desplazamiento vertical. El documento se ejecutó con la red desactivada, sin solicitudes externas ni errores JavaScript.

El Chromium administrado bloquea `file://`; por eso se ejecutó el contenido exacto del HTML mediante `set_content` en un contexto offline. No se alteraron políticas del navegador. Las pruebas locales no equivalen por sí solas a comprobar el despliegue público.

No se realizaron estudios con participantes: la comprensión debe comprobarse durante el ensayo. No se afirma una mejora de aprendizaje medida empíricamente.

Se verificaron los 32 nombres del recorrido chileno, la separación de las ciudades mencionadas en pares y el orden de los primeros diez nombres en el selector. Se revisaron **1.000 emplazamientos**: todos únicos, en terreno seco y fuera de las parcelas rurales. Los centros de los polígonos de agua son rechazados por el mismo comprobador que utiliza la ubicación de ciudades. El mapa incluye islas y cinco áreas rurales; pulsar una parcela abre la explicación sin alterar población ni aplicar un escenario. Su explicación identifica factores inmóviles y declara que esta capa no modifica Simon. Las instrucciones e indicadores identifican «grupos de personas». Se revisaron nuevas capturas del contorno completo y el detalle de campos y ciudades, también en móvil.
