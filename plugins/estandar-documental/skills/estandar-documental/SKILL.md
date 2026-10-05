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
- Verificar que el título, alcance y contenido describan exactamente el mismo entregable.

Leer [Perfiles](references/perfiles.md). Leer [Idioma y Gobernanza](references/idioma-gobernanza.md) cuando haya dudas de nomenclatura.

## Fijar la fuente visual antes de diseñar

En **CREAR**, elegir una fuente visual explícita:

1. referencia aprobada del usuario/proyecto;
2. sistema visual de marca vigente;
3. si no existe ninguna, usar [Sistema Visual por Defecto](references/sistema-visual-default.md).

Nunca dejar que Word o el especialista elijan silenciosamente un estilo genérico por defecto.

En **ADAPTAR/REPLICAR**, gobierna la referencia aprobada y no se aplica el sistema visual por defecto.

## Diseñar según la función

Aplicar [Composición Adaptativa](references/composicion-adaptativa.md).

- Elegir texto, tabla, gráfico, diagrama, imagen o combinación según lo que el lector deba comprender, decidir, recordar o hacer.
- Exigir una función clara a cada visual.
- Evitar cuotas de imágenes, decoración de relleno y pseudo-infografías.
- Resolver problemas de espacio en este orden: eliminar redundancia → sintetizar → mejorar estructura → cambiar representación → redistribuir → añadir página → ajustar tamaños profesionales.
- Tratar una referencia aprobada en ADAPTAR/REPLICAR como baseline bloqueada, no como inspiración.

Para **ESTUDIO_APRENDIZAJE**, leer además [Estudio y Aprendizaje](references/estudio-aprendizaje.md).

## Gates no negociables de calidad profesional

Antes de liberar cualquier DOCX:

- **Jerarquía:** ruta visual inequívoca entre título, mensaje principal, secciones y cierre.
- **Sistema visual:** tipografía, color, reglas, superficies y espaciados deben responder a una lógica consistente.
- **Genericidad:** en CREAR, bloquear apariencia de Word por defecto salvo petición explícita de estilo plano.
- **Uso de página:** no aceptar contenido comprimido con grandes zonas vacías accidentales.
- **Densidad:** no aceptar paredes de texto, columnas estrechas con párrafos largos ni texto miniaturizado.
- **Semántica Word:** usar estructura nativa cuando corresponda sin sacrificar una composición profesional.
- **Alcance:** el contenido no puede ampliar silenciosamente el título o propósito.
- **Aplicabilidad:** acción, decisión, regla o dato principal localizable en segundos.
- **Render final:** revisar todas las páginas después del último cambio material. Un archivo generado pero no inspeccionado sigue **BLOQUEADO**.

### Gate adicional para COMPACTO_OPERACIONAL

Un documento compacto no es simplemente “una página”. Debe:

- priorizar objetivo/conclusión/acción en la primera zona de lectura;
- organizar el contenido en pocos bloques claramente distinguibles;
- usar microestructuras operativas cuando mejoren la ejecución;
- mostrar intención editorial visible, no una lista genérica de viñetas;
- aprovechar la página de forma equilibrada;
- mantener lectura normal sin zoom;
- cerrar con comprobación, acción o próximo paso.

## Ejecutar con especialistas

Aplicar [Ejecución Técnica](references/ejecucion-tecnica.md) y [Implementación Word](references/implementacion-word.md).

- Usar la capacidad documental disponible para creación/edición DOCX, estructura, accesibilidad y render.
- Usar herramientas de datos para cálculos y gráficos cuantitativos.
- Usar investigación cuando se necesite evidencia pública actual.
- Usar Canva/diseño cuando un recurso visual mejore materialmente la comprensión.
- Mantener Word como contenedor editable y semántico cuando la salida final sea DOCX.
- No reconstruir dentro de esta skill capacidades ya resueltas por especialistas.
- Si el especialista devuelve un resultado genérico o viola los gates anteriores, **corregirlo**; no aceptar su salida como autoridad estética.

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
- Evaluar propósito, arquitectura, jerarquía, sistema visual, representación, densidad, uso del espacio, utilidad visual, aplicabilidad y fidelidad.
- Revisar visualmente todas las páginas después del último cambio material.
- Auditar estructura Word: headings, tablas, listas y accesibilidad.
- Declarar **FINAL** solo con todos los controles aplicables aprobados y sin defectos BLOQUEANTES/MAYORES.
- Mantener **BLOQUEADO** cuando falte evidencia o exista un defecto material.

Para cambios de la propia skill, seguir [Protocolo de Regresión](references/regresion.md). Consultar [Referencias de Diseño](references/referencias-diseno.md) al actualizar criterios; no reinvestigar la web en cada ejecución normal.
