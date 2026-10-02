# Ejecución técnica — Estándar Documental v1.3

## Principio

La skill gobierna **qué debe conseguir el documento** y delega la mecánica a la mejor herramienta disponible. No reconstruir dentro de Estándar Documental capacidades que ya existen en especialistas de documentos, datos, investigación, diseño o accesibilidad.

> **El especialista ejecuta. Estándar Documental gobierna.**

## Flujo

1. Definir Contrato de Tarea: propósito, audiencia/uso, resultado esperado, modo, perfil, fuentes, referencia aprobada y salida.
2. Elegir representación y composición mediante Composición Adaptativa.
3. Seleccionar especialistas estrictamente necesarios.
4. Construir el documento.
5. Renderizar/revisar con herramientas existentes.
6. Aplicar controles de calidad, fidelidad y uso final.
7. Liberar como FINAL o mantener BLOQUEADO.

## Especialistas

### Documento / DOCX
Usar la capacidad documental disponible para:
- creación y edición Word;
- estilos y estructura semántica;
- paginación;
- tablas;
- accesibilidad;
- renderizado y revisión técnica.

La herramienta no decide por sí sola propósito, perfil, fidelidad ni aceptación.

### Datos
Usar especialista de datos para:
- cálculos;
- validación de dataset;
- gráficos cuantitativos;
- reconciliación y métricas.

Estándar Documental decide qué representación entra al documento y cómo se interpreta.

### Investigación
Usar investigación/web cuando el contenido requiera evidencia pública actual, verificación externa o contraste experto. No investigar de nuevo si la información ya está suficientemente respaldada y vigente.

### Diseño / Canva
Usar Canva u otra herramienta visual cuando un diagrama, mapa conceptual, marco, comparativa visual o recurso de estudio/comercial mejore materialmente la comprensión. No invocarla por decoración ni por cuota de imágenes.

Cuando la salida final sea DOCX, Word sigue siendo el contenedor editable y semántico. Evitar rasterizar texto principal innecesariamente.

## Perfiles

- COMPACTO_OPERACIONAL: rapidez y acción.
- ANALÍTICO_NEGOCIO: evidencia y decisión.
- VISUAL_COMERCIAL: narrativa y comunicación respaldada.
- REFERENCIA_RÁPIDA_OPERACIONAL: consulta inmediata.
- ESTUDIO_APRENDIZAJE: comprensión, memoria, recuperación y aplicación.

Los perfiles son funciones objetivo, no plantillas.

## Márgenes, tipografía y formato

A4 vertical y márgenes de 25,4 mm son valores seguros por defecto para CREAR. Pueden ajustarse de forma razonada —por ejemplo, aproximadamente 20–25,4 mm— cuando mejoren claramente el uso de página sin degradar legibilidad.

En ADAPTAR/REPLICAR gobierna la referencia aprobada.

No reducir tipografía ni visuales hasta hacerlos ilegibles para cumplir un número de páginas arbitrario.

## Preservación

Para ADAPTAR/REPLICAR:
- trabajar sobre copia reversible;
- identificar elementos bloqueados;
- modificar solo lo autorizado o funcionalmente imprescindible;
- comparar antes/después;
- revisar el documento completo tras cambios;
- bloquear rediseños colaterales.

La referencia aprobada es una baseline bloqueada, no una inspiración.

## QA

Delegar controles mecánicos cuando exista herramienta especializada:
- archivo válido;
- clipping/overflow;
- headings;
- tablas;
- accesibilidad;
- fuentes;
- metadatos;
- render.

Estándar Documental conserva los controles inteligentes:
- propósito;
- arquitectura;
- jerarquía;
- representación;
- densidad y espacio;
- utilidad visual;
- aplicabilidad;
- fidelidad.

Un aprobado automático nunca sustituye la revisión visual y contextual final.

## Scripts

Los scripts incluidos en este repositorio son **helpers de regresión/validación**, no un runtime obligatorio para producir todos los documentos. La ruta técnica heredada se conserva en `archivo/ejecucion-tecnica-heredada.md` y en la evidencia histórica, pero no gobierna v1.3.

## Estado de liberación

- **FINAL**: todos los controles aplicables pasan y no existen defectos BLOQUEANTES/MAYORES.
- **BLOQUEADO**: falta evidencia, existe un defecto material o no puede verificarse una condición obligatoria.

No declarar FINAL por el mero hecho de que el archivo haya sido generado.
