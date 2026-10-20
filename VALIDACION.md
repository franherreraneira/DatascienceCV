# Validación del prototipo

Se ejecutó `python3 tests/validate.py` con Playwright y Chromium del entorno. **37 comprobaciones aprobadas**. No hay dependencias de ejecución ni servicios requeridos por el juego.

Se verificaron:

- Conservación de unidades, nacimientos indivisibles y asignación proporcional. La frecuencia condicional se contrastó mediante 30.000 sorteos independientes a un estado fijo, sin confundir un resultado finito con una predicción asintótica.
- Reproducción por semilla, comparación de probabilidades de fundación y ramas pareadas. Sin intervención, ambas ramas coinciden exactamente; mercado y congestión cambian el tamaño de la ciudad elegida frente a su control.
- La secuencia completa desatendida termina en 240 segundos. Los controles también permiten adelantar fases y conservar resultados. Seleccionar otra ciudad después de fijar el plan no cambia su objetivo.
- Selección por teclado, selector y clic en el gráfico, preguntas con retroalimentación, reinicio y exportación de resultados JSON.
- Todas las fases y el modo de proyección caben en 1366 × 768. No hay desbordamiento horizontal a 390 px; en móvil la interfaz se desplaza verticalmente.
- Ejecución en un contexto de navegador con la red desactivada, sin solicitudes externas ni errores JavaScript durante la secuencia.

El Chromium administrado de esta máquina bloquea la navegación `file://` por política. Para las pruebas se cargó el contenido exacto del HTML con `set_content`, manteniendo el contexto sin red. No se modificaron políticas del navegador. La apertura con doble clic queda como vía de uso del documento autónomo en un navegador normal; esa navegación concreta no se pudo probar en este Chromium administrado.

Se inspeccionaron capturas de la portada, comparación, conclusiones, proyección y móvil. No se probó con participantes ni se ha demostrado empíricamente que los cuatro minutos sean suficientes para que todos lean y comprendan cada elemento. El guion propone una exposición conducida y conviene ensayarla antes de presentar.

Estas pruebas validan el documento HTML autónomo y el paquete ZIP; no establecen por sí solas la disponibilidad del sitio público en GitHub Pages. Abrir el juego descargado no necesita acceso a Internet. No se ejecuta un servidor permanente en este entorno.
