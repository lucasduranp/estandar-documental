# Preservación

Partir del documento suministrado y crear una copia de trabajo reversible. Registrar hash previo y objetivo autorizado exacto. Inventariar texto del cuerpo, estilos de párrafo/carácter, tablas objetivo y no objetivo, encabezados, pies, imágenes, relaciones, secciones y campos antes de editar.

Preservar tipografía, marca y geometría válidas fuera del cambio solicitado. No normalizar el archivo completo al Core. Reparar solo defectos demostrados y referencias dependientes necesarias; documentar cada diferencia permitida. Comparar las partes XML y el contenido semántico resultante contra la fuente y luego comparar renderizados. Diferencias de bytes producidas por serialización ZIP no equivalen automáticamente a cambios de contenido.

Para toda edición de producción, crear instantáneas legibles por máquina antes/después y una especificación de cambios esperados que nombre cada objeto y operación permitidos. La reparación de anchos de tabla debe usar la geometría de sección existente: los anchos finales deben sumar exactamente el ancho útil de página y la rejilla junto con cada celda deben coincidir. Preservar o añadir encabezado repetido nativo y protección contra división de filas solo cuando la tarea lo exija. Un cambio no declarado en tabla, contenido, estilo, tema, fuente, color, encabezado/pie, imagen, relación, numeración, campo o configuración de página es inesperado y bloquea la liberación. `unexpected_changes` debe ser cero.

Renderizar e inspeccionar fuente y resultado completos. Registrar comprobantes e inspecciones contra hashes reales. Una liberación de preservación requiere aprobar estructura, preservación, accesibilidad, fidelidad de fuentes del PDF, render visual completo, inspección visual y uso final. El formato directo existente se evalúa por diferencia; no se impone sobre un documento preservado la regla histórica de cero formato directo del Core.

PR01 permanece como caso histórico aprobado de regresión. GD08 es su nombre histórico y no pertenece a la familia visual canónica. Sus entradas, salidas y aserciones exactas permanecen en `regression/approved-v1.1`; ver [Reconciliación](reconciliacion.md). No aplicar normalización de alineación canónica a PR01.

El control de fuentes para preservación verifica las fuentes originales intencionadas contra la fuente y su render nativo. Aptos es obligatoria para la familia Core histórica, no una autorización para cambiar la tipografía de un documento preservado.
