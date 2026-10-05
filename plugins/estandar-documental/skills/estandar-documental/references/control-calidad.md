# Controles de aceptación — v1.3.3

## Controles

| Control | Evidencia requerida |
|---|---|
| Decisiones bloqueadas | Aptos, español, modos y gobernanza preservados |
| Requisitos / Propósito | Título, alcance y uso real coherentes |
| Contenido / Arquitectura | Síntesis, secuencia y longitud proporcional |
| Sistema Visual | Fuente visual definida; Aptos + color, superficies y espaciado coherentes |
| Representación | Texto/tabla/gráfico/diagrama/imagen elegidos por función |
| Composición | Legibilidad, densidad, balance, uso del espacio y ritmo profesionales |
| Genericidad | En CREAR, apariencia intencionalmente diseñada; no Word default salvo solicitud |
| Aplicabilidad | El lector puede decidir, ejecutar, consultar, comprender o aprender |
| Fidelidad | En ADAPTAR/REPLICAR, baseline preservada sin romper decisiones bloqueadas |
| Estructura Word | Estilos/listas/tablas/secciones/enlaces válidos |
| Integridad de construcción | DOCX válido y reabierto |
| Accesibilidad | Orden de lectura, headings, tablas, contraste, color no exclusivo |
| Control visual | Render final inspeccionado en miniatura y 100%; Aptos confirmada |
| Uso final | Escenario real completado sin corrección pendiente |

Un aprobado técnico no compensa una mala solución editorial o visual.

## BLOQUEOS duros

Bloquear si aparece cualquiera de estos problemas:

- fuente distinta de Aptos sin instrucción explícita del usuario;
- sustitución silenciosa de Aptos en render;
- archivo corrupto, contenido perdido, clipping o superposición;
- texto/visual materialmente ilegible;
- miniaturización usada como estrategia de paginación;
- apariencia genérica de Word en CREAR sin solicitud explícita de estilo plano;
- ausencia de una fuente visual definida;
- headings visuales sin estructura Word cuando corresponda;
- grandes vacíos accidentales o composición claramente desequilibrada;
- 3+ columnas con narrativa densa;
- pseudo-infografía o visual decorativo;
- paleta/acentos incoherentes;
- pérdida de fidelidad en ADAPTAR/REPLICAR;
- título o alcance incoherente con el contenido;
- documento técnicamente correcto pero visualmente indistinguible de un borrador;
- cambio de una decisión bloqueada sin aprobación explícita del usuario.

## Revisión visual

Hacer:
- comprobación previa de [Decisiones bloqueadas](decisiones-bloqueadas.md);
- verificación tipográfica Aptos;
- vista miniatura para intención, balance y jerarquía;
- revisión al 100% para legibilidad;
- auditoría semántica Word;
- revisión de sistema visual;
- comparación con referencia aprobada cuando exista.

Toda modificación posterior invalida la aprobación visual anterior.

## Severidad

**BLOQUEANTE**: violación de decisión bloqueada, integridad, legibilidad, fidelidad crítica o ausencia de sistema visual en CREAR.  
**MAYOR**: jerarquía, representación, densidad, genericidad, composición o aplicabilidad que impiden uso profesional.  
**MENOR**: defecto visible reparable.  
**PULIDO**: no reabre diseño una vez alcanzada suficiencia profesional.

FINAL requiere todos los controles aplicables aprobados y cero defectos BLOQUEANTES/MAYORES.
