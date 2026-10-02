---
name: estandar-documental
description: Crea, adapta y replica documentos Word profesionales con Estándar Documental v1.3: composición adaptativa, perfiles por propósito, integridad de fuentes, fidelidad, control de calidad visual y uso de especialistas cuando aportan valor. Úsalo para informes, documentos de estudio, resúmenes, actas, comparaciones, dossiers y otros DOCX profesionales; no para respuestas solo en chat, correos, diapositivas u hojas de cálculo.
metadata:
  version: "1.3"
---

# Estándar Documental

## Idioma y nomenclatura

El idioma de trabajo, documentación y artefactos guardados es **español por defecto**. Esto incluye títulos, nombres de perfiles, manifiestos, cambios de versión, referencias, evaluaciones, criterios de calidad y nombres de archivos nuevos.

Se permite mantener en inglés únicamente nombres oficiales, citas, APIs, nombres de herramientas y **literales técnicos heredados que el runtime exija**. Cuando exista un literal técnico en inglés, la documentación debe presentar primero su nombre canónico en español y, solo cuando sea necesario para ejecutar código, indicar el literal entre `backticks`.

Una misma decisión debe tener **un único nombre canónico en español**. No crear sinónimos paralelos para la misma regla.

Ver también [Idioma y Gobernanza](references/idioma-gobernanza.md).

## Autoridad y propósito

Esta skill es la autoridad documental vigente. `Professional Document Standard` y sus artefactos v1.1 son **antecedentes y regresión histórica**, no autoridad de ejecución ni reemplazo automático. Los nombres internos heredados de estilos Word (`PDSBullet`, etc.) pueden conservarse por compatibilidad técnica, pero no definen la identidad ni las reglas vigentes.

El objetivo no es imponer una plantilla: es producir la **mejor solución profesional razonable para el uso real del documento**, con estructura mantenible, evidencia trazable, composición inteligente y resultado aplicable.

## Flujo obligatorio

1. **GOBERNAR** — fijar fuente de verdad, restricciones y precedencia. Nunca degradar silenciosamente a una versión histórica.
2. **COMPRENDER** — registrar el Contrato de Tarea: propósito, audiencia/uso, resultado o acción esperada, modo, perfil, fuentes, referencia aprobada/elementos bloqueados y salida.
3. **DISEÑAR** — aplicar [Composición Adaptativa](references/composicion-adaptativa.md): arquitectura, representación, densidad, espacio y visuales según función, no según plantilla.
4. **EJECUTAR** — usar primero especialistas cuando aporten valor. DOCX para mecánica/render/accesibilidad; datos para cálculos; investigación para evidencia actual; Canva/diseño para recursos visuales útiles. Estándar Documental conserva la autoridad de propósito, arquitectura, fidelidad y aceptación.
5. **VERIFICAR** — aplicar [Control de Calidad](references/control-calidad.md): integridad, estructura, accesibilidad, visual, calidad inteligente, fidelidad y uso final. Un aprobado técnico no equivale a un buen documento.
6. **LIBERAR** — estado **FINAL** solo con todos los controles aplicables aprobados y sin defectos bloqueantes o mayores. Si falta evidencia: **BLOQUEADO**, nunca aprobación implícita.

## Modos de cambio

- **CREAR** — libertad de composición alta dentro del estándar y de las fuentes. Literal técnico heredado: `CREATE`.
- **ADAPTAR** — preservar sistema visual y decisiones aprobadas; cambiar solo lo necesario para el nuevo contenido/uso. Literal técnico heredado: `ADAPT`.
- **REPLICAR** — máxima fidelidad; solo cambios solicitados o reparaciones técnicas imprescindibles. Literal técnico heredado: `REPLICATE`.

Para ediciones estrictamente acotadas sobre DOCX existente, [Preservación](references/preservacion.md) sigue disponible como ruta técnica cerrada. No sustituye la decisión CREAR/ADAPTAR/REPLICAR.

## Perfiles

Leer [Perfiles](references/perfiles.md). Los perfiles son **funciones objetivo**, no diseños rígidos:

- **COMPACTO_OPERACIONAL** — rapidez de comprensión y acción. Literal técnico heredado: `COMPACT_OPERATIONAL`.
- **ANALÍTICO_NEGOCIO** — evidencia, comparación y decisión. Literal técnico heredado: `ANALYTICAL_BUSINESS`.
- **VISUAL_COMERCIAL** — narrativa, marca y comunicación respaldada. Literal técnico heredado: `VISUAL_COMMERCIAL`.
- **REFERENCIA_RÁPIDA_OPERACIONAL** — recuperación inmediata durante la ejecución. Literal técnico heredado: `QUICK_REFERENCE_OPERATIONAL`.
- **ESTUDIO_APRENDIZAJE** — comprender, conectar, recordar, recuperar y aplicar; mayor señalización visual y color semántico. Literal técnico heredado: `STUDY_LEARNING`.

## Reglas de composición

- Propósito antes que formato. Elegir texto, tabla, gráfico, diagrama, imagen o combinación según la pregunta que debe resolver.
- **Todo visual debe tener una función**: explicar, comparar, evidenciar, orientar, revelar patrón/relación, priorizar o facilitar recuperación.
- No hay cuota mínima de visuales. Cero visuales es válido si es mejor.
- No resolver paginación miniaturizando. Orden: eliminar redundancia → sintetizar → mejorar estructura → cambiar representación → redistribuir → añadir página → ajustar tamaños dentro de rangos profesionales.
- El espacio blanco es funcional cuando marca jerarquía; es defecto cuando es accidental o produce desequilibrio.
- Tabla + visual solo si cumplen funciones distintas. Si son sustitutivos o redundantes, elegir uno.
- Una referencia aprobada en ADAPTAR/REPLICAR es **referencia bloqueada**, no inspiración.

## Word y ejecución técnica

Para nuevos documentos, leer [Implementación Word](references/implementacion-word.md). El recurso canónico y el runtime empaquetado siguen como **ruta de respaldo validada** para COMPACTO_OPERACIONAL y ANALÍTICO_NEGOCIO; no deben limitar perfiles más visuales si existe un especialista capaz de construirlos correctamente.

VISUAL_COMERCIAL y ESTUDIO_APRENDIZAJE son preferentemente ejecutados con especialistas. Canva puede producir diagramas, marcos, mapas conceptuales o recursos visuales; el especialista DOCX mantiene la estructura Word y Estándar Documental decide integración y estado FINAL/BLOQUEADO. No convertir el documento completo en un diseño plano cuando la salida debe seguir editable/accesible.

Los valores canónicos por defecto son A4 vertical y 25,4 mm. En CREAR con especialista pueden ajustarse de forma justificada —por ejemplo, márgenes de aproximadamente 20–25,4 mm— cuando mejore materialmente el uso de página sin perjudicar legibilidad; registrar la excepción y validarla visualmente. La ruta de respaldo empaquetada conserva 25,4 mm exactos para proteger su regresión histórica.

## Integridad y contexto

Leer [Integridad](references/integridad.md) y [Aislamiento de Contexto](references/aislamiento-contexto.md). Nunca inventar datos, completar DESCONOCIDO/PENDIENTE por estética ni permitir que memoria/contexto cambie el entregable solicitado. Para ANALÍTICO_NEGOCIO, mantener trazabilidad de evidencia, cálculos e interpretación.

## Control de calidad y regresión

Leer [Control de Calidad](references/control-calidad.md). Toda salida debe pasar revisión visual página por página después del último cambio. Para cambios de skill, seguir [Protocolo de Regresión](references/regresion.md); los Goldens v1.1 permanecen inmutables y sirven como regresión histórica, no como plantillas rígidas. Ejecutar también las evaluaciones v1.3 de delegación y calidad.

El benchmark estable detrás de estas reglas está resumido en [Referencias de Diseño](references/referencias-diseno.md); no investigar la web en cada ejecución normal. Reinvestigar solo al actualizar la skill, ante un problema no cubierto, un formato extraordinario o una solicitud explícita.
