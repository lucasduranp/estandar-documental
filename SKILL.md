---
name: estandar-documental
description: Crea, adapta y replica documentos Word profesionales con Estándar Documental v1.3: composición adaptativa, perfiles por propósito, integridad de fuentes, fidelidad, control de calidad visual y uso de especialistas cuando aportan valor. Úsalo para informes, documentos de estudio, resúmenes, actas, comparaciones, dossiers y otros DOCX profesionales; no para respuestas solo en chat, correos, diapositivas u hojas de cálculo.
metadata:
  version: "1.3"
---

# Estándar Documental

## Idioma y nomenclatura

El idioma de trabajo, documentación y artefactos guardados es **español por defecto**. Esto incluye títulos, nombres de perfiles, manifiestos, cambios de versión, referencias, evaluaciones, criterios de calidad y nombres de archivos nuevos.

Se permite mantener en inglés únicamente nombres oficiales, citas, APIs, nombres de herramientas y literales técnicos heredados cuando sean necesarios para compatibilidad. La documentación debe presentar primero el nombre canónico en español.

Una misma decisión debe tener **un único nombre canónico en español**. Ver [Idioma y Gobernanza](references/idioma-gobernanza.md).

## Autoridad y propósito

Esta skill es la autoridad documental vigente. `Professional Document Standard` y sus artefactos anteriores son **antecedentes/regresión histórica**, no autoridad de ejecución ni fallback automático.

El objetivo no es imponer una plantilla: es producir la **mejor solución profesional razonable para el uso real del documento**, con estructura mantenible, evidencia trazable, composición inteligente y resultado aplicable.

## Flujo obligatorio

1. **GOBERNAR** — fijar fuente de verdad, restricciones y precedencia.
2. **COMPRENDER** — definir propósito, audiencia/uso, resultado esperado, modo, perfil, fuentes, referencia aprobada/elementos bloqueados y salida.
3. **DISEÑAR** — aplicar [Composición Adaptativa](references/composicion-adaptativa.md): arquitectura, representación, densidad, espacio y visuales según función, no plantilla.
4. **EJECUTAR** — usar las mejores herramientas especialistas disponibles. Estándar Documental conserva autoridad de propósito, arquitectura, fidelidad y aceptación.
5. **VERIFICAR** — aplicar [Control de Calidad](references/control-calidad.md): integridad, estructura, accesibilidad, visual, calidad inteligente, fidelidad y uso final.
6. **LIBERAR** — **FINAL** solo con controles aplicables aprobados y sin defectos BLOQUEANTES/MAYORES. Si falta evidencia: **BLOQUEADO**.

## Modos de cambio

- **CREAR** — libertad de composición alta dentro del estándar y de las fuentes.
- **ADAPTAR** — preservar sistema visual y decisiones aprobadas; cambiar solo lo necesario.
- **REPLICAR** — máxima fidelidad; solo cambios solicitados o reparaciones imprescindibles.

Para ediciones estrictamente acotadas, aplicar [Preservación](references/preservacion.md).

## Perfiles

Leer [Perfiles](references/perfiles.md). Son **funciones objetivo**, no diseños rígidos:

- **COMPACTO_OPERACIONAL** — rapidez de comprensión y acción.
- **ANALÍTICO_NEGOCIO** — evidencia, comparación y decisión.
- **VISUAL_COMERCIAL** — narrativa, marca y comunicación respaldada.
- **REFERENCIA_RÁPIDA_OPERACIONAL** — recuperación inmediata durante la ejecución.
- **ESTUDIO_APRENDIZAJE** — comprender, conectar, recordar, recuperar y aplicar; mayor señalización visual y color semántico.

## Reglas de composición

- Propósito antes que formato.
- Elegir texto, tabla, gráfico, diagrama, imagen o combinación según la necesidad.
- **Todo visual debe tener una función**: explicar, comparar, evidenciar, orientar, revelar patrón/relación, priorizar o facilitar recuperación.
- No existe cuota mínima de visuales.
- No resolver paginación miniaturizando. Orden: eliminar redundancia → sintetizar → mejorar estructura → cambiar representación → redistribuir → añadir página → ajustar tamaños profesionales.
- El espacio blanco es funcional cuando marca jerarquía; es defecto cuando es accidental.
- Tabla + visual solo si cumplen funciones distintas.
- Una referencia aprobada en ADAPTAR/REPLICAR es **baseline bloqueada**, no inspiración.

## Word y ejecución técnica

Leer [Implementación Word](references/implementacion-word.md) y [Ejecución Técnica](references/ejecucion-tecnica.md).

Usar primero la capacidad documental disponible para creación/edición DOCX, estilos, estructura, accesibilidad y render. Usar datos para cálculos/gráficos, investigación para evidencia actual y Canva/diseño para recursos visuales cuando aporten valor.

**No reconstruir dentro de esta skill un runtime paralelo si la plataforma ya dispone de la capacidad necesaria.**

VISUAL_COMERCIAL y ESTUDIO_APRENDIZAJE pueden requerir especialistas visuales. Cuando la salida sea DOCX, Word sigue siendo el contenedor editable/semántico; no aplanar el documento completo a imágenes.

A4 vertical y 25,4 mm son valores seguros por defecto para CREAR, no hard gates universales. Pueden ajustarse de forma justificada —por ejemplo, aproximadamente 20–25,4 mm— si mejora el uso de página sin perjudicar legibilidad. En ADAPTAR/REPLICAR gobierna la referencia aprobada.

## Integridad y contexto

Leer [Integridad](references/integridad.md) y [Aislamiento de Contexto](references/aislamiento-contexto.md). Nunca inventar datos ni completar DESCONOCIDO/PENDIENTE por estética. Para ANALÍTICO_NEGOCIO, mantener trazabilidad de evidencia, cálculos e interpretación.

## Control de calidad y regresión

Leer [Control de Calidad](references/control-calidad.md). Toda salida requiere revisión visual página por página después del último cambio material.

Para cambios de skill, seguir [Protocolo de Regresión](references/regresion.md). La regresión histórica sirve como evidencia, no como plantilla rígida. Ejecutar también las evaluaciones v1.3 de delegación y calidad.

El benchmark estable está resumido en [Referencias de Diseño](references/referencias-diseno.md). No investigar la web en cada ejecución normal; reinvestigar al actualizar la skill, ante un problema no cubierto, un formato extraordinario o solicitud explícita.
