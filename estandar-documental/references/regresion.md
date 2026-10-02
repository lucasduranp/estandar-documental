# Protocolo de regresión — v1.3

## Objetivo

La regresión histórica demuestra que cambios futuros no reintroducen defectos ya conocidos. **No gobierna el diseño de documentos nuevos** y no obliga a usar el runtime heredado.

## Baseline histórica

La suite aprobada v1.1 cubre:
- GD01 proporcionalidad y desconocidos;
- GD02 respuesta primero + evidencia;
- GD03 uso en reunión;
- GD04 comparación y tabla ancha;
- GD05 jerarquía/numeración;
- GD06 procedencia e incertidumbre;
- GD07 imagen/comercial;
- PR01 preservación.

Su procedencia y hashes se registran en `regression/provenance.json`.

Los archivos históricos originales pueden conservar nombres y literales en inglés porque son evidencia congelada. No deben usarse como nomenclatura operativa vigente.

## Regresión v1.3

Para cada cambio de skill verificar:

1. **Estructura de skill**
   - `SKILL.md` válido;
   - enlaces relativos válidos;
   - documentación activa en español;
   - sin referencias a archivos inexistentes.

2. **Evaluaciones v1.3**
   - ejecutar/revisar `evals/casos_calidad_v1_3.json`;
   - ejecutar/revisar `evals/casos_delegacion.json`;
   - confirmar que los casos negativos son rechazados.

3. **Preservación histórica**
   - no reinterpretar Goldens como plantillas;
   - no modificar evidencia histórica sin crear nueva versión;
   - mantener hashes/procedencia documentados.

4. **Prueba real**
   - al menos un caso representativo de cada área modificada;
   - render y revisión visual página por página;
   - comprobar propósito, arquitectura, representación, densidad, utilidad visual, aplicabilidad y fidelidad.

5. **Instalación**
   - validar con Skill Creator;
   - instalar la misma release en ChatGPT Web y Desktop/Codex;
   - ejecutar smoke test en cada superficie.

## Helpers

Los scripts que permanezcan en `scripts/` son auxiliares de validación/regresión. **No son un runtime obligatorio de producción**. Si una herramienta especialista existente resuelve mejor la función, usar la herramienta.

## Promoción

Promover a VIGENTE solo cuando:
- la estructura sea válida;
- los evals relevantes pasen;
- no exista regresión funcional conocida;
- la revisión visual real pase;
- la release instalada corresponda a la misma versión canónica en las superficies objetivo.

La ausencia de errores automáticos no sustituye revisión humana/visual.
