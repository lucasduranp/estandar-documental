# Idioma y gobernanza de nomenclatura

## Regla general

Todo contenido, documentación y artefacto nuevo que se guarde dentro del sistema debe estar en **español por defecto**: nombres de documentos, referencias, perfiles, manifiestos, cambios de versión, evaluaciones, criterios de QA, comentarios operativos y nombres de archivos nuevos.

## Excepciones técnicas

Se mantienen en su forma original solo cuando sea necesario para compatibilidad o precisión:
- nombres oficiales de normas, marcos, productos y herramientas;
- citas y títulos de fuentes externas;
- nombres de APIs, funciones y scripts;
- claves o literales técnicos exigidos por una herramienta;
- identificadores históricos de la regresión aprobada.

Cuando un literal técnico en inglés deba aparecer, la documentación debe presentar primero su equivalente canónico en español. Ejemplo: **ESTUDIO_APRENDIZAJE** (`STUDY_LEARNING`).

## Regresión histórica

La suite anterior se conserva como evidencia de procedencia y regresión, identificada en `regression/provenance.json`. Sus nombres históricos no se usan como nomenclatura operativa vigente.

## Unicidad

Una regla, perfil o modo debe tener un solo nombre canónico en español. No introducir variantes paralelas que dificulten búsqueda o reutilización.
