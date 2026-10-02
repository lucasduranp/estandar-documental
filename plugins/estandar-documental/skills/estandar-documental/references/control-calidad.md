# Controles de aceptación — v1.3

## Controles

| Control | Evidencia requerida |
|---|---|
| Requisitos / Propósito | Resultados solicitados mapeados; propósito y uso real satisfechos |
| Evidencia / Integridad de datos | Registro de fuentes, cifras/cálculos verificados, desconocidos visibles, conflictos resueltos o declarados |
| Contenido / Arquitectura | Síntesis correcta, secuencia lógica, jerarquía y longitud proporcional |
| Representación | Texto/tabla/gráfico/diagrama/imagen elegidos por función; redundancia justificada |
| Composición | Legibilidad, densidad, uso del espacio, balance y ritmo profesionales |
| Utilidad Visual | Cada visual aporta una función cognitiva/informativa; no pseudo-visuales ni decoración competitiva |
| Aplicabilidad | El lector puede decidir, ejecutar, consultar, comprender o aprender según el objetivo |
| Fidelidad | Para ADAPTAR/REPLICAR: referencia aprobada preservada salvo cambios autorizados/necesarios |
| Estructura Word nativa | Estilos/encabezados/listas/tablas/secciones/campos/enlaces válidos; preservación por diferencia cuando aplique |
| Integridad de construcción | DOCX válido, abre sin reparación, dependencias presentes, archivo final reabierto |
| Accesibilidad | Secuencia de encabezados, orden de lectura, encabezados de tabla, texto alternativo/enlaces, idioma, contraste y señales no basadas solo en color |
| Control visual técnico | Render final; toda página inspeccionada para recortes, superposiciones, pérdida de glifos, paginación y usabilidad de tablas |
| Uso final | Escenario real de lectura/edición/navegación/impresión/reunión/estudio completado sin corrección pendiente |

Un aprobado técnico no compensa una mala solución editorial o visual.

## Candidatos a BLOQUEO duro

- dato/cita inventado, cálculo materialmente errado o afirmación sin trazabilidad;
- recorte, superposición, contenido perdido o archivo corrupto;
- texto/visual materialmente ilegible;
- miniaturización usada como estrategia de paginación;
- tabla inutilizable o usada como diseño sin función de datos/registro;
- grandes vacíos accidentales o composición claramente desequilibrada;
- pseudo-infografía: texto convertido en cajas/flechas sin mejora real;
- visual decorativo que compite con la información;
- tabla + visual redundantes sin función diferenciada;
- pérdida de fidelidad o rediseño no solicitado en ADAPTAR/REPLICAR;
- viñetas/numeración/encabezados rotos;
- evidencia/incertidumbre presentada de forma engañosa;
- documento formalmente completo pero inutilizable para su propósito.

## Revisión visual y de calidad

Revisar al menos: propósito, arquitectura, jerarquía, representación, composición/densidad, utilidad visual, aplicabilidad y fidelidad cuando aplique. Hacer vista general en miniatura + revisión al 100%/tamaño legible. Toda modificación posterior invalida la aprobación visual anterior.

## Fidelidad tipográfica

La ruta canónica histórica v1.1/v1.2 conserva Aptos y su control histórico. En una ruta con especialista, la familia tipográfica debe ser profesional, disponible en el entorno de destino y coherente con la referencia/proyecto; no forzar Aptos sobre una marca existente. Nunca empaquetar fuentes comerciales sin permiso.

## Severidad

**BLOQUEANTE**: integridad/evidencia/archivo/fidelidad crítica/legibilidad crítica.  
**MAYOR**: jerarquía, representación, densidad, composición, tabla o aplicabilidad que impiden uso profesional.  
**MENOR**: defecto visible reparable sin afectar comprensión.  
**PULIDO**: no reabre diseño una vez alcanzada suficiencia profesional.

Los scripts técnicos pueden seguir usando los literales `PASS`, `FAIL`, `NOT_RUN` y `BLOCKED` por compatibilidad. En documentación y reportes visibles, usar **APROBADO, FALLA, NO_EJECUTADO y BLOQUEADO**. FINAL requiere todos los controles aplicables aprobados y cero defectos BLOQUEANTES/MAYORES. Cero hallazgos automáticos nunca sustituye revisión contextual.
