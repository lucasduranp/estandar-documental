# Ejecución técnica — Estándar Documental v1.3.4

## Principio

La skill gobierna **qué debe conseguir el documento** y delega la mecánica al especialista oficial de documentos. No reconstruir dentro de Estándar Documental capacidades ya existentes.

> **El especialista ejecuta. Estándar Documental gobierna.**

## Regla de routing para DOCX

Cuando la salida sea Word/DOCX en Work o Codex:

1. seleccionar explícitamente la capacidad **@Documents / Documents** disponible en la superficie;
2. aplicar Estándar Documental como capa de gobernanza;
3. no invocar runtimes heredados ni loaders locales propios como ruta de producción;
4. si @Documents no está disponible en esa superficie, detenerse e informar la limitación exacta.

El fallo de un runtime heredado no debe contaminar la ruta oficial de documentos.

## Flujo

1. Definir Contrato de Tarea.
2. Cargar decisiones bloqueadas.
3. Seleccionar perfil y composición.
4. Invocar @Documents.
5. Construir DOCX con Aptos declarada.
6. Ejecutar QA estructural y visual.
7. Liberar FINAL o BLOQUEADO.

## Aptos y render

- Aptos es obligatoria en el DOCX.
- Verificar estilos/tema/runs del archivo.
- No cambiar de fuente porque el preview local no tenga Aptos.
- Si el preview auxiliar sustituye la fuente, usarlo para revisar composición, clipping, balance y jerarquía, dejando claro que la fidelidad tipográfica del preview es limitada.
- El target primario de fidelidad tipográfica es Microsoft Word / Microsoft 365.
- Diseñar con holgura suficiente para evitar layouts frágiles ante pequeñas diferencias de métricas.

## Otros especialistas

### Datos
Usar especialista de datos para cálculos, validación y gráficos cuantitativos.

### Investigación
Usar web/investigación solo cuando el contenido requiera evidencia pública actual.

### Diseño / Canva
Usar Canva u otra herramienta visual cuando un diagrama o recurso visual mejore materialmente la comprensión. Word sigue siendo el contenedor editable.

## QA

Delegar controles mecánicos a @Documents y herramientas disponibles:
- validez del archivo;
- estilos;
- headings;
- tablas;
- accesibilidad;
- fuentes declaradas;
- metadatos;
- paginación;
- render/preview.

Estándar Documental conserva controles inteligentes:
- propósito;
- arquitectura;
- jerarquía;
- representación;
- densidad y espacio;
- utilidad visual;
- aplicabilidad;
- fidelidad.

## Estado de liberación

- **FINAL**: todos los controles aplicables pasan; el DOCX declara Aptos y no hay defectos BLOQUEANTES/MAYORES.
- **BLOQUEADO**: falta una capacidad imprescindible, existe un defecto material o el DOCX no cumple una decisión bloqueada.

La ausencia de Aptos en un preview auxiliar, por sí sola, no bloquea si el DOCX conserva Aptos como fuente declarada.
