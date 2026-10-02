# Validación — Estándar Documental v1.3.1 CANDIDATA

## Estado

**PLUGIN INSTALABLE CORRECTO. SMOKE TEST FUNCIONAL v1.3.0: FALLÓ EN CALIDAD PROFESIONAL. v1.3.1 INCORPORA CORRECCIONES Y REQUIERE UN ÚLTIMO RETEST.**

## Hallazgos del smoke test fallido

El DOCX de prueba evidenció problemas que debieron bloquear la liberación:

- gran vacío inferior mientras el contenido estaba comprimido en la zona superior;
- narrativa distribuida en una tabla de una sola fila usada como layout;
- secciones visibles sin estilos Heading reales;
- dos tablas sin fila de encabezado semántico;
- exceso de formato directo;
- jerarquía y densidad insuficientemente resueltas para COMPACTO_OPERACIONAL;
- alcance del contenido más amplio que el título de “preparar”.

## Correcciones v1.3.1

- gates no negociables incorporados directamente en SKILL.md;
- reglas específicas de COMPACTO_OPERACIONAL;
- bloqueo explícito de layout narrativo con tablas;
- exigencia de headings semánticos;
- gate de balance/ocupación de página;
- gate de coherencia entre título, alcance y contenido;
- obligación de render + inspección visual después del último cambio;
- nuevos evals AQ08-AQ10 y NEG06-NEG07.

## Pendiente

1. Actualizar/reinstalar plugin v1.3.1.
2. Repetir exactamente el mismo smoke test.
3. Si el nuevo DOCX pasa visual, semántica y funcionalmente, marcar v1.3.1 como VIGENTE y cerrar esta fase.
