---
name: estandar-documental
description: Crear, adaptar, replicar y auditar documentos Word profesionales con composición adaptativa, perfiles por propósito, integridad de fuentes, fidelidad visual y control de calidad. Usar cuando se solicite un DOCX profesional nuevo o la modificación de uno existente, incluidos informes, documentos de estudio, resúmenes, actas, comparaciones, dossiers y guías operativas.
---

# Estándar Documental

## Gobernanza obligatoria

Antes de cualquier ejecución o cambio del estándar, leer [Decisiones bloqueadas](references/decisiones-bloqueadas.md).

- **Aptos es la tipografía oficial y obligatoria de Estándar Documental.**
- La conformidad tipográfica se verifica en el **DOCX**, no en la lista de fuentes de un preview auxiliar.
- Trabajar en español por defecto.
- No importar decisiones visuales de otros sistemas. **Avenir Next pertenece a las publicaciones de LinkedIn de Agrícola Zhong Yi, no a Estándar Documental.**
- Clasificar modo: **CREAR**, **ADAPTAR** o **REPLICAR**.
- Seleccionar perfil.
- Definir propósito, audiencia, resultado esperado, fuentes, referencia aprobada, elementos bloqueados y salida.
- Mantener coherencia entre título, alcance y contenido.

Leer [Perfiles](references/perfiles.md).

## Routing obligatorio para DOCX

Aplicar [Ejecución Técnica](references/ejecucion-tecnica.md).

- En Work/Codex, seleccionar explícitamente **@Documents / Documents** para crear o editar DOCX.
- No usar runtimes heredados ni loaders locales propios como ruta de producción.
- Si @Documents no está disponible, informar la limitación exacta.
- Un fallo de runtime heredado no es un fallo de Estándar Documental ni debe bloquear una ruta oficial disponible.

## Fuente visual

En CREAR:
1. referencia aprobada compatible;
2. sistema de marca compatible;
3. si no existe, [Sistema Visual por Defecto](references/sistema-visual-default.md).

La fuente visual puede definir color, composición e iconografía, pero no sustituye Aptos.

## Diseñar según función

Aplicar [Composición Adaptativa](references/composicion-adaptativa.md).

- Elegir representación según lo que el lector deba comprender, decidir, recordar o hacer.
- Exigir función clara a cada visual.
- Evitar decoración, pseudo-infografías y relleno.
- Resolver espacio por contenido/arquitectura antes que por miniaturización.

## Gates

- **Tipografía del archivo:** DOCX declara Aptos.
- **Jerarquía:** ruta visual inequívoca.
- **Sistema visual:** composición intencional, no Word genérico.
- **Uso de página:** sin grandes vacíos accidentales ni compresión innecesaria.
- **Densidad:** sin paredes de texto ni columnas estrechas.
- **Semántica Word:** estructura nativa correcta.
- **Alcance:** título y contenido coherentes.
- **Aplicabilidad:** acción/decisión/regla localizable rápido.
- **Render/preview:** revisar tras último cambio; si el preview no tiene Aptos, tratarlo como limitación de preview, no como autorización para cambiar la fuente.

### COMPACTO_OPERACIONAL

- objetivo/acción primero;
- pocos bloques claros;
- microestructuras operativas;
- intención editorial visible;
- página equilibrada;
- lectura normal sin zoom;
- cierre con comprobación o próximo paso.

## Ejecutar

Aplicar [Implementación Word](references/implementacion-word.md).

- @Documents ejecuta la mecánica DOCX.
- Estándar Documental gobierna calidad y aceptación.
- Si el resultado es genérico o viola decisiones bloqueadas, corregir antes de liberar.

## Verificar

Aplicar [Control de Calidad](references/control-calidad.md).

- Verificar Aptos dentro del DOCX.
- Revisar visualmente todas las páginas.
- Auditar headings, listas, tablas, accesibilidad y composición.
- Declarar **FINAL** solo con gates aplicables aprobados.
- Mantener **BLOQUEADO** solo por defectos reales del documento/capacidad, no por ausencia de Aptos en un preview auxiliar.

Para cambios de la skill, seguir [Protocolo de Regresión](references/regresion.md).
