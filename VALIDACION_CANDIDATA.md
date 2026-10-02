# Validación — Estándar Documental v1.3 CANDIDATA

## Estado

**CANDIDATA VALIDADA A NIVEL ESTÁTICO/UNITARIO. NO PROMOVIDA A VIGENTE.**

La candidata se normalizó al español para documentación activa, referencias, evaluaciones, nomenclatura conceptual y nombres de archivos nuevos. Los literales técnicos exigidos por scripts/APIs y la regresión histórica congelada permanecen sin traducir cuando cambiarlos afectaría compatibilidad o reproducibilidad.

## Nomenclatura canónica

- CREAR (`CREATE` técnico heredado)
- ADAPTAR (`ADAPT`)
- REPLICAR (`REPLICATE`)
- COMPACTO_OPERACIONAL (`COMPACT_OPERATIONAL`)
- ANALÍTICO_NEGOCIO (`ANALYTICAL_BUSINESS`)
- VISUAL_COMERCIAL (`VISUAL_COMMERCIAL`)
- REFERENCIA_RÁPIDA_OPERACIONAL (`QUICK_REFERENCE_OPERATIONAL`)
- ESTUDIO_APRENDIZAJE (`STUDY_LEARNING`)

## Controles ejecutados

- JSON de evaluaciones: válido.
- Enlaces relativos de documentación activa: válidos.
- Sintaxis Python: válida.
- `self_test.py`: **11/11 PASS**.
- `test_runtime_ab.py`: **9/9 PASS**.
- `test_word_list_gate.py`: **11/11 pruebas negativas + control positivo PASS**.
- Regresión histórica `regression/approved-v1.1`: preservada sin modificación de contenido.

## Excepciones deliberadas

No se traducen/renombran:
- nombres de funciones, APIs, dependencias y comandos técnicos;
- claves JSON o literales que el runtime exige;
- identificadores y archivos dentro de `regression/approved-v1.1`, porque forman parte de una regresión histórica congelada y basada en hashes.

## Gate pendiente antes de promover a VIGENTE

Sigue pendiente la aceptación visual/regresión con fuente Aptos nativa y renderizador compatible. La candidata no debe declararse FINAL/VIGENTE hasta completar ese gate.
