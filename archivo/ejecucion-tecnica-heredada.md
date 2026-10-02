# Ejecución técnica heredada — v1.2 / candidata inicial v1.3

Este documento conserva la especificación de la ruta empaquetada heredada para trazabilidad. **No gobierna la ejecución activa de Estándar Documental v1.3.**

La implementación heredada incluía un constructor DOCX propio, preflight, manifiesto de ejecución, controles de fuentes, visuales, preservación y regresión. Se conserva como antecedente porque la candidata v1.3 fue validada inicialmente contra esta arquitectura, pero la versión activa prioriza herramientas especialistas existentes para reducir complejidad y evitar duplicar capacidades de plataforma.

La fuente histórica completa permanece en el paquete `Estandar_Documental_v1.3_CANDIDATA_ES.zip` y en la regresión aprobada v1.1. No reinstalar esta ruta como autoridad sin una decisión explícita de versión.

## Principios heredados que sí continúan vigentes

- liberación cerrada ante falta de evidencia;
- integridad y trazabilidad;
- preservación de referencias aprobadas;
- revisión visual página por página;
- separación entre hechos, interpretación y recomendación;
- no miniaturizar para resolver paginación;
- no afirmar PASS solo por controles automáticos.

## Elementos que dejan de ser requisito operativo general

- constructor DOCX propio como ruta principal;
- uso obligatorio de Aptos fuera de la regresión histórica;
- 25,4 mm como hard gate universal;
- dependencia de scripts internos cuando una herramienta especialista disponible ya resuelve la función;
- identidad `professional-document-standard`.

La documentación operativa vigente está en `references/ejecucion-tecnica.md`.
