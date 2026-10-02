# Ejecución técnica de Estándar Documental v1.3 — ruta de producción

## Autoridad y alcance

Evolución: v1.1 validada → Estándar Documental v1.2 → v1.3 candidata. La regresión histórica permanece inmutable.

La identidad técnica canónica es `estandar-documental`. `professional-document-standard` es solo antecedente histórico y no debe emitirse como autoridad actual. El constructor empaquetado sigue siendo una ruta de respaldo validada para los perfiles COMPACTO_OPERACIONAL y ANALÍTICO_NEGOCIO; VISUAL_COMERCIAL, REFERENCIA_RÁPIDA_OPERACIONAL y ESTUDIO_APRENDIZAJE usan ejecución con especialista hasta que exista una ruta empaquetada equivalente y validada.

Los literales técnicos de JSON, nombres de scripts, estados (`PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`) e identificadores heredados permanecen en inglés cuando el código los exige. Esta es una excepción técnica; la documentación visible y la nomenclatura conceptual son en español.

## Contrato de tarea y preflight

Antes de construir, capturar el prompt exacto en `task_contract.explicit_user_goal`. Registrar `requested_deliverable` (DOCX), `requested_scope`, `audience_if_known` (null si se desconoce), `research_required`, `allowed_context`, `forbidden_scope_expansion`, `source_policy` y `unknown_information`. El contexto es subordinado a la tarea explícita.

Seleccionar modo y perfil semánticamente antes del preflight; el preflight valida la selección, no clasifica lenguaje natural. Para la ruta empaquetada, los literales heredados son `NEW_DOCUMENT`, `COMPACT_OPERATIONAL` y `ANALYTICAL_BUSINESS`.

El JSON de solicitud también entrega `mode`, `profile`, `asset_path` y `output_path`. Ejecutar:

```text
python scripts/runtime_preflight.py request.json execution.json
python scripts/build_document.py execution.json content.json
```

Usar rutas nuevas para salida y manifiesto. El preflight registra inicio y controles. Falta/recurso incorrecto, SHA-256 fijado incorrecto, contrato/perfil/ruta de salida inválidos producen salida distinta de cero. Documento nuevo debe quedar vinculado al recurso reconciliado dentro de esta candidata. El constructor vuelve a comprobar la vinculación contra los bytes reales. El hash esperado está fijado en `runtime_preflight.py` y nunca lo aporta el llamador.

## Constructor empaquetado

El constructor de producción lee el paquete canónico completo y reemplaza el cuerpo de demostración por componentes semánticos aprobados. Conserva estilos, tema, numeración, configuración, pie y setup de página. Elimina etiqueta de encabezado de demostración, imagen y relación fuente, además de metadatos descriptivos. No construye desde un DOCX vacío.

Para la ruta de respaldo empaquetada no se aceptan estilos, fuentes, tamaños, márgenes, colores, alineación ni OOXML aportados por el llamador. El overflow se resuelve en el contenido, nunca reduciendo el Core. CREAR con especialista puede usar excepciones de layout controladas por QA v1.3; esas excepciones están fuera de la ruta histórica de respaldo.

`content.json` es una lista de objetos. Los componentes de párrafo usan `type` y `text`: `title`, `deck`, `body`, `source_note`, `caption`, `callout`. `heading` añade `level` 1–3; `bullets` y `numbered_list` usan `items`. `table` usa `rows` con el conteo de columnas y geometría del espécimen aprobado, incluyendo encabezado semántico. Las listas heredan numeración nativa canónica.

COMPACTO_OPERACIONAL y ANALÍTICO_NEGOCIO están calificados en esta ruta. VISUAL_COMERCIAL, REFERENCIA_RÁPIDA_OPERACIONAL y ESTUDIO_APRENDIZAJE deben ejecutarse con especialista; no forzarlos al constructor ni inventar componentes no soportados. La preservación usa una ruta separada vinculada a la fuente y no impone recurso canónico.

## Manifiesto y liberación

`execution_manifest.py` registra resultados reales de controles, evidencia, hashes y timestamps. Todos los controles comienzan en `NOT_RUN`. `PASS` requiere evidencia; la liberación permanece `BLOCKED` hasta que todos los controles obligatorios pasen sin bloqueantes. El constructor A/B registra construcción, no aprobación de evidencia, visual, accesibilidad o fuentes. Una salida modificada exige nueva ejecución y nueva evidencia QA. El manifiesto es registro de auditoría, no una certificación inviolable.

E2E-01, E2E-02 y E2E-03 ejecutan controles bloqueantes según ruta, renderizado e inspección visual explícita. Registrar hashes exactos de salida y render. Distinguir liberación del documento de `skill_release`.

## Fase C — núcleo, fuentes y visual

Tras preflight/construcción, ejecutar el control visual con un directorio de render nuevo y un adaptador de renderizador nativo. Debe crearse `render-receipt.json` con hashes de DOCX/PDF/imágenes y número esperado de páginas. E2E-01 Compacto espera una página A4. El control verifica que todos los párrafos DOCX aparezcan en el PDF. Un comprobante de render sin inspección actual no libera.

Después de abrir todas las imágenes de página vigentes, registrar `inspection.json` con: estado, revisor, fecha, hashes de DOCX/PDF/comprobante, páginas e imágenes inspeccionadas, controles de recorte, superposición, glifos, paginación, legibilidad, tablas y alcance, además de hallazgos con severidad/detalle. `PASS` requiere todos los checks en `PASS` y cero BLOCKER/MAJOR. Es una atestación de revisión, no una afirmación de que el juicio visual pueda automatizarse por completo.

Vincular los comprobantes a `manifest.phase_c` y ejecutar `python scripts/release_gate.py execution.json` como operación final. Código 0 significa liberación técnica `PASS`; distinto de cero significa `BLOCKED`. No puede liberar: un `PASS` manual, comprobante ausente, hash obsoleto, lista incompleta de páginas, inspección faltante, sustitución tipográfica o hallazgo mayor sin resolver.

`core_gate.py` revisa geometría/partes canónicas, encabezados, referencias reales de listas, formato de párrafos/runs/celdas, geometría aprobada de tablas, propiedades de filas, campos y relaciones internas. `font_gate.py` usa evidencia de uso real de texto en PDF y nombres incrustados de fontTools; recursos de fuente no usados no sustituyen uso real de Aptos/Aptos Bold.

## Fase D — ejecución analítica

Para ANALÍTICO_NEGOCIO (`ANALYTICAL_BUSINESS`), los componentes pueden añadir metadatos técnicos `claim_type`, `evidence_ids` y `calculation`. El constructor elimina esos metadatos del Word final. Las tablas deben usar el componente semántico canónico: encabezado único no vacío, al menos una fila de datos, rejilla aprobada, sin celdas vacías ni altura fija de fila. Las tablas de layout se bloquean.

Vincular `manifest.phase_d.content` y `manifest.phase_d.evidence` a los JSON exactos usados. `analytical_gate.py` exige registro de fuentes oficiales válido, rastrea componentes factuales a IDs de fuente, separa hecho, interpretación y recomendación, y bloquea puntajes/cálculos sin fórmula, insumos, método y fuentes reconstruibles. El manifiesto recomputa este control en cada guardado y verifica hash del contenido construido. Un `PASS` aportado por el llamador no lo sustituye.

E2E-02 ejecuta controles Core, Evidencia, Accesibilidad, Fuente, Visual completo y Uso final. Tras sus negativos, reconstruir E2E-01 desde entradas nuevas para confirmar que Compacto sigue pasando.

## Fase E — preservación

Para la ruta técnica `PRESERVATION`, el perfil debe ser null, se vincula el DOCX fuente con SHA-256 exacto, `expected_changes.json` y sin recurso canónico. Ejecutar:

```text
python scripts/runtime_preflight.py request.json execution.json
python scripts/preservation_snapshot.py original.docx --output snapshot-before.json
python scripts/preservation_build.py execution.json
python scripts/preservation_snapshot.py adjusted.docx --output snapshot-after.json
```

El constructor de preservación modifica solo los objetos de tabla nombrados. Los anchos objetivo deben sumar exactamente el ancho útil de sección. Sincroniza rejilla y anchos de celda, preserva encabezados repetidos y añade protección nativa `cantSplit` cuando corresponde. Copia byte a byte cada parte del paquete no documental y rechaza reutilizar la ruta de salida.

`preservation_gate.py` compara texto antes/después, estructura del cuerpo no tabular, estilos, tema, numeración, fuentes, encabezados/pies, medios, relaciones, secciones, setup de página y tablas objetivo/no objetivo. Solo pasan diferencias declaradas en `expected_changes.json`; `unexpected_changes` debe ser cero. El formato directo se evalúa por diferencia, no aplicando al documento existente la regla histórica de cero formato directo del Core.

Renderizar original y ajustado en directorios nuevos e inspeccionar todas las páginas. El control visual de preservación exige evidencia de render completa, geometría y número de páginas coherentes, inventario de texto visible sin cambios salvo duplicados de paginación y `PASS` tras inspección sin BLOCKER/MAJOR. El control de fuentes compara familias/recursos realmente usados en PDF antes/después y exige que las estructuras OOXML de fuente permanezcan sin cambios; nunca convierte el archivo a Aptos.

Los controles obligatorios de esta ruta son preflight, build, structural, preservation, accessibility, font, visual_render, visual_inspection y final_use. Los controles Core y evidence quedan `NOT_RUN` porque no aplican. Evidencia faltante, delta no solicitado o `unexpected_changes > 0` mantiene `BLOCKED`.

## Fase F — aislamiento de contexto

Todo contrato de documento nuevo debe contener `explicit_user_goal`, `requested_scope`, `allowed_context` y `forbidden_scope_expansion` no vacíos. El prompt exacto conserva autoridad: memoria, historia y contexto de proyecto pueden apoyar un hecho o encuadre dentro del alcance, pero no crear un propósito, audiencia, narrativa personal o flujo de trabajo nuevo.

Vincular contenido y registro de fuentes exactos en `manifest.phase_f.content` y `manifest.phase_f.evidence`. `scope_context_gate.py` valida registros de fuente y citas, detecta componentes factuales sin respaldo y bloquea contenido de entrevista, cargo, búsqueda laboral, CV, experiencia personal o material previo cuando no fue solicitado. Si el concepto fue pedido explícitamente, el contrato lo autoriza.

E2E-04 añade metadatos semánticos `scope_role` y `context_origin`; el constructor los elimina del render Word. El control Alcance/Contexto es obligatorio para todos los documentos nuevos. Vinculaciones faltantes, hash obsoleto, diferencia entre contenido revisado y DOCX, hechos no trazados, contexto permitido contaminado o expansión material del alcance mantienen la liberación `BLOCKED`.

## Dependencias técnicas

Dependencias del runtime: lxml, pypdf, Pillow y fontTools; la generación PDF de tests negativos usa reportlab. `quick_validate.py` requiere PyYAML. El renderizador requiere LibreOffice/Aptos nativos y Poppler según el comprobante de ejecución. Estas dependencias técnicas pueden conservar sus nombres oficiales en inglés.
