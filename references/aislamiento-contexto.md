# Aislamiento de Contexto y Control de Alcance

El prompt exacto del usuario define el entregable. Antes de construir, registrar objetivo, alcance solicitado, contexto permitido y expansión prohibida. Una conversación previa, memoria, proyecto o documento puede aportar hechos o encuadre relevantes solo cuando el resultado siga siendo reconocible como el entregable explícitamente pedido.

No inferir una nueva audiencia, decisión, propósito personal o flujo de trabajo a partir del contexto histórico. Por ejemplo, un resumen de empresa no se convierte en preparación de entrevista, ajuste a un cargo, narrativa de CV, posicionamiento personal, preguntas para otra persona o material de búsqueda laboral salvo que el prompt actual lo pida.

Para documento nuevo, vincular el JSON de contenido exacto y el registro de evidencias a `manifest.phase_f`. Todo hecho externo debe citar una fuente actual conocida. Cuando el contexto previo aporte un componente, marcar `context_origin=prior_context`, mantenerlo dentro de un rol de alcance permitido y revalidarlo contra el registro de evidencias actual. El hecho de ser histórico no vuelve automáticamente pertinente un contenido.

El control de Alcance/Contexto compara el contenido revisado con el DOCX final y falla de forma cerrada. Expansiones prohibidas, contexto permitido contaminado, contenido obsoleto, hechos sin respaldo, citas desconocidas, notas de fuente faltantes o cualquier ampliación material del alcance bloquean la liberación. Un estado APROBADO escrito manualmente no puede sustituir la recomputación del control.
