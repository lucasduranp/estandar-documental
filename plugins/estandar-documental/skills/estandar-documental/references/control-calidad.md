# Controles de aceptación — v1.3.4

## Controles

| Control | Evidencia requerida |
|---|---|
| Decisiones bloqueadas | Aptos, español, modos y gobernanza preservados |
| Routing | @Documents usado para DOCX; no runtime heredado |
| Tipografía del archivo | DOCX declara Aptos en estilos/tema/runs aplicables |
| Requisitos / Propósito | Título, alcance y uso coherentes |
| Contenido / Arquitectura | Síntesis, secuencia y longitud proporcional |
| Sistema Visual | Color, superficies, espaciado y jerarquía coherentes con Aptos |
| Composición | Legibilidad, densidad, balance y uso del espacio |
| Genericidad | En CREAR, apariencia intencionalmente diseñada |
| Aplicabilidad | El lector puede ejecutar/decidir/consultar |
| Fidelidad | Baseline preservada en ADAPTAR/REPLICAR |
| Estructura Word | Estilos/listas/tablas/secciones válidos |
| Integridad | DOCX válido y reabierto |
| Accesibilidad | Orden de lectura, headings, tablas, contraste |
| Control visual | Preview/render revisado; limitaciones de fuente del preview no cambian el DOCX |
| Uso final | Escenario real completado sin corrección pendiente |

## BLOQUEOS duros

Bloquear si:
- el DOCX declara una fuente distinta de Aptos sin autorización;
- @Documents no está disponible y no existe otra capacidad documental oficial;
- se usa un runtime heredado como sustituto improvisado;
- archivo corrupto, clipping, superposición o ilegibilidad;
- apariencia genérica en CREAR;
- pérdida de fidelidad;
- cambio de decisión bloqueada sin autorización.

**No bloquear solo porque un renderer auxiliar no tenga Aptos**, siempre que:
1. el DOCX declare Aptos;
2. la composición tenga holgura suficiente;
3. el preview permita revisar layout general;
4. no se haya sustituido la fuente dentro del archivo.

## Revisión visual

- vista miniatura;
- revisión al 100%;
- auditoría semántica;
- verificación de Aptos en el DOCX;
- comparación con referencia cuando exista.

## Severidad

**BLOQUEANTE**: violación real del DOCX/decisiones, ausencia de capacidad oficial, integridad o legibilidad crítica.  
**MAYOR**: genericidad, jerarquía, composición o aplicabilidad deficiente.  
**MENOR**: defecto reparable.  
**PULIDO**: no reabre diseño tras alcanzar suficiencia profesional.

FINAL requiere todos los controles aplicables aprobados y cero defectos BLOQUEANTES/MAYORES.
