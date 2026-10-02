# Preservación

Partir del documento suministrado y crear una copia reversible antes de editar.

## Objetivo

Modificar únicamente lo solicitado y preservar todo lo demás que siga siendo válido: contenido, tipografía, marca, geometría, tablas, encabezados, pies, imágenes, relaciones, secciones, campos y lenguaje visual.

Una referencia aprobada es una **baseline bloqueada**, no una inspiración para rediseñar.

## Antes de editar

Registrar:
- documento fuente;
- alcance exacto del cambio;
- elementos bloqueados;
- tablas/visuales/secciones objetivo;
- cambios permitidos;
- cualquier excepción funcional necesaria.

Cuando la herramienta disponible permita hashes o diferencias estructurales, utilizarlos. Cuando no, comparar semántica y visualmente antes/después.

## Durante la edición

- no normalizar el documento completo a defaults del estándar;
- no cambiar tipografía, colores, proporciones o layout fuera del alcance;
- reparar solo defectos demostrados y dependencias necesarias;
- mantener tablas y visuales legibles;
- no introducir un nuevo sistema visual;
- documentar cualquier cambio colateral imprescindible.

## Después de editar

Revisar el documento completo, no solo el bloque modificado:
- contenido preservado;
- estructura Word;
- paginación;
- tablas;
- imágenes;
- encabezados/pies;
- numeración;
- fuentes;
- accesibilidad;
- clipping/superposición;
- fidelidad visual.

Un cambio no solicitado que altere materialmente una pieza aprobada es **BLOQUEANTE**.

## Regresión histórica

PR01/GD08 permanece como antecedente de preservación dentro de la regresión histórica. Su procedencia se registra en [regression/provenance.json](../regression/provenance.json). No se utiliza como plantilla visual ni como obligación de implementación.

## Tipografía

Preservar la tipografía original válida del documento. Aptos pertenece a una familia histórica de regresión; no autoriza convertir documentos existentes a Aptos.
