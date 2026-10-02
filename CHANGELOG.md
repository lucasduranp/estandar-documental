# Cambios — v1.3.1

## Corrección tras smoke test real

El primer DOCX generado con v1.3.0 fue técnicamente válido pero profesionalmente deficiente. Esta versión convierte esos fallos en gates explícitos.

### Añadido

- gate obligatorio de balance y uso de página;
- reglas específicas para COMPACTO_OPERACIONAL;
- bloqueo de tablas usadas como layout narrativo;
- exigencia de Heading styles para secciones visibles;
- gate de coherencia título/alcance/contenido;
- render e inspección final como condición de liberación;
- casos de regresión que reproducen el fallo observado.

### Estado

CANDIDATA hasta repetir una vez el mismo smoke test y aprobarlo.
