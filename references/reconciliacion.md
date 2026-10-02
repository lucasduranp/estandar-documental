# Correcciones de implementación probadas

## Discrepancia de alineación

El espécimen aprobado tiene ocho propiedades `w:pPr/w:jc=center` en las columnas Ajuste y Estado de la tabla. Son sobreescrituras de presentación de párrafo, no propiedades de geometría de celda. El `style_lint.py` histórico contaba sangrías y espaciado, pero omitía alineación; por eso su antiguo conteo cero no demostraba ausencia de sobreescrituras de alineación.

El espécimen también tiene un pie directamente alineado a la derecha. Los siete casos canónicos comparten ese pie; GD07 además centra directamente el párrafo de imagen. El constructor aprobado elimina el cuerpo de demostración del espécimen, lo que explica por qué esas ocho sobreescrituras de tabla no aparecen en los casos.

`normalize_alignment.py` mueve cada alineación a un estilo de párrafo derivado de su estilo original. Preserva formato efectivo y deja intactas propiedades de tabla/celda, texto, tema y numeración. Los recursos/Goldens originales son inmutables. El recurso reconciliado tiene nueve migraciones; GD01–GD06 una cada uno; GD07 dos. La inspección estricta incluye cuerpo, encabezados y pies y reporta cero formato directo de párrafo/run para el Core. La reversión restaura equivalencia XML. El renderizado a 108 DPI produce píxeles idénticos para ambas páginas del espécimen y para las siete páginas canónicas.

## Defecto de rejilla PR01

El constructor aprobado original escribe anchos de celda 1360/4875/1133/1133/1133 twips en la primera tabla, pero conserva una rejilla de cinco columnas de 1927 twips. El render nativo usa por ello columnas iguales y anula la reparación geométrica objetivo.

`repair_pr01_grid.py` cambia solo esos cinco anchos de rejilla para que coincidan con los anchos de celda existentes. No selecciona un diseño nuevo. La aserción añadida falla en el original aprobado y pasa después de la corrección. Cada otra parte del paquete permanece byte a byte idéntica; revertir los cinco valores restaura equivalencia XML del documento. El contenido y las fuentes originales permanecen preservados. La segunda tabla sube naturalmente porque la primera reparada se vuelve más corta; su contenido, estructura y estilo no cambian.

## Manifiesto del paquete fuente

Las 20 entradas de payload coinciden con sus SHA-256 suministrados. El manifiesto original también se enumera a sí mismo con el SHA-256 de un archivo vacío, auto-referencia creada antes de escribir su contenido. Conservarlo como evidencia histórica; el manifiesto de liberación calcula hashes de payload y se excluye a sí mismo. El usuario confirmó expresamente que el ZIP denominado Candidate v1.1 es la autoridad aprobada; la redacción antigua de “esperando confirmación” es histórica.

## Renderizador

Esta validación utilizó LibreOffice 26.2.6.3 extraído al espacio de trabajo y las fuentes Aptos originales del usuario. Word abrió y paginó GD01, pero la exportación PDF se detuvo; no se afirma un APROBADO de exportación PDF de Word. La evidencia nativa de fuente en LibreOffice/PDF es la autoridad visual final de esa ejecución. Las fuentes y binarios del renderizador no forman parte del paquete de la skill.
