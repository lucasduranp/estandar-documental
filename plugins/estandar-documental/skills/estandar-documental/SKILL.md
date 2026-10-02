---
name: estandar-documental
description: Crear, adaptar, replicar y auditar documentos Word profesionales con composición adaptativa, perfiles por propósito, integridad de fuentes, fidelidad visual y control de calidad. Usar cuando se solicite un DOCX profesional nuevo o la modificación de uno existente, incluidos informes, documentos de estudio, resúmenes, actas, comparaciones, dossiers y guías operativas.
---

# Estándar Documental

## Gobernar antes de construir

- Trabajar en español por defecto.
- Tratar Professional Document Standard y versiones anteriores como antecedentes históricos, nunca como fallback operativo.
- Clasificar primero el modo: **CREAR**, **ADAPTAR** o **REPLICAR**.
- Seleccionar después el perfil: **COMPACTO_OPERACIONAL**, **ANALÍTICO_NEGOCIO**, **VISUAL_COMERCIAL**, **REFERENCIA_RÁPIDA_OPERACIONAL** o **ESTUDIO_APRENDIZAJE**.
- Definir propósito, audiencia/uso, resultado esperado, fuentes de verdad, referencia aprobada, elementos bloqueados y salida.

Leer [Perfiles](references/perfiles.md) para elegir el objetivo correcto. Leer [Idioma y Gobernanza](references/idioma-gobernanza.md) cuando haya dudas de nomenclatura o versiones.

## Diseñar según la función

Aplicar [Composición Adaptativa](references/composicion-adaptativa.md).

- Elegir texto, tabla, gráfico, diagrama, imagen o combinación según lo que el lector deba comprender, decidir, recordar o hacer.
- Exigir una función clara a cada visual.
- Evitar cuotas de imágenes, decoración de relleno y pseudo-infografías.
- Resolver problemas de espacio en este orden: eliminar redundancia → sintetizar → mejorar estructura → cambiar representación → redistribuir → añadir página → ajustar tamaños profesionales.
- Tratar una referencia aprobada en ADAPTAR/REPLICAR como baseline bloqueada, no como inspiración.

Para **ESTUDIO_APRENDIZAJE**, leer además [Estudio y Aprendizaje](references/estudio-aprendizaje.md).

## Ejecutar con especialistas

Aplicar [Ejecución Técnica](references/ejecucion-tecnica.md) y [Implementación Word](references/implementacion-word.md).

- Usar la capacidad documental disponible para creación/edición DOCX, estructura, accesibilidad y render.
- Usar herramientas de datos para cálculos y gráficos cuantitativos.
- Usar investigación cuando se necesite evidencia pública actual.
- Usar Canva/diseño solo cuando un recurso visual mejore materialmente la comprensión.
- Mantener Word como contenedor editable y semántico cuando la salida final sea DOCX.
- No reconstruir dentro de esta skill capacidades ya resueltas por especialistas mantenidos por la plataforma.

## Proteger integridad y contexto

Leer [Integridad](references/integridad.md) y [Aislamiento de Contexto](references/aislamiento-contexto.md).

- No inventar datos ni completar desconocidos por estética.
- Separar hecho, evidencia reportada, supuesto, estimación e interpretación.
- Mantener trazabilidad de cálculos y afirmaciones materiales.
- Evitar que memoria o contexto previo amplíen el alcance solicitado.

Para ADAPTAR/REPLICAR, leer [Preservación](references/preservacion.md).

## Verificar antes de liberar

Aplicar [Control de Calidad](references/control-calidad.md).

- Delegar controles mecánicos a herramientas existentes.
- Evaluar además propósito, arquitectura, jerarquía, representación, densidad, uso del espacio, utilidad visual, aplicabilidad y fidelidad.
- Revisar visualmente todas las páginas después del último cambio material.
- Declarar **FINAL** solo con todos los controles aplicables aprobados y sin defectos BLOQUEANTES/MAYORES.
- Mantener **BLOQUEADO** cuando falte evidencia o exista un defecto material.

Para cambios de la propia skill, seguir [Protocolo de Regresión](references/regresion.md). Consultar [Referencias de Diseño](references/referencias-diseno.md) al actualizar criterios; no reinvestigar la web en cada ejecución normal.
