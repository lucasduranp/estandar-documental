# Validación — Estándar Documental v1.3.4 CANDIDATA

## Diagnóstico

El bloqueo de v1.3.3 no fue causado por la decisión Aptos, sino por dos reglas operativas mal definidas:

1. se confundió “Aptos obligatoria en el DOCX” con “Aptos debe estar instalada en todo renderer auxiliar”;
2. Work intentó una ruta de runtime/loader en vez de exigir explícitamente el especialista oficial @Documents.

## Corrección

- Aptos sigue bloqueada como tipografía oficial;
- se verifica en el DOCX, no por la lista de fuentes del preview;
- la ausencia de Aptos en un renderer auxiliar no bloquea por sí sola;
- el target primario es Microsoft Word / Microsoft 365;
- para DOCX en Work/Codex se exige explícitamente @Documents/Documents;
- runtimes heredados quedan fuera de producción;
- se añaden AQ14, AQ15 y NEG11.

## Pendiente

Un único retest con @Documents + Estándar Documental v1.3.4.
