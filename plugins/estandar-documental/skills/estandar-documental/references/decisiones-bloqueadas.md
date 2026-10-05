# Decisiones bloqueadas — Estándar Documental

Estas decisiones son **fuente de verdad** y no pueden cambiarse por optimización, perfil, herramienta, referencia genérica ni criterio estético del modelo.

Solo pueden modificarse mediante una instrucción explícita del usuario que indique que desea cambiar el estándar. Una excepción puntual para un documento no modifica esta lista.

## Tipografía

- **Aptos es la tipografía oficial y obligatoria de Estándar Documental.**
- Se aplica en CREAR, ADAPTAR y REPLICAR cuando el documento pertenece al sistema Estándar Documental.
- No sustituir por Avenir Next, Manrope, Calibri u otra familia por disponibilidad, perfil o preferencia estética.
- La obligación tipográfica se verifica en el **DOCX**: estilos, tema y/o runs deben declarar Aptos según corresponda.
- La ausencia de Aptos en un renderizador auxiliar **no autoriza sustitución** y tampoco bloquea por sí sola la construcción del DOCX si este mantiene Aptos como fuente declarada.
- El entorno objetivo primario es Microsoft Word / Microsoft 365. Un preview auxiliar puede usar sustitución visual sin alterar la fuente declarada del archivo; esa limitación debe tratarse como limitación de preview, no como cambio del estándar.
- Una instrucción explícita del usuario puede autorizar otra tipografía para un documento puntual; esa excepción no altera el estándar.

### Separación de sistemas visuales

- **Avenir Next pertenece al sistema visual de publicaciones de LinkedIn de Agrícola Zhong Yi.**
- No importar Avenir Next al Estándar Documental.
- No mezclar decisiones tipográficas de redes sociales, marca o piezas editoriales externas con documentos salvo instrucción explícita.

## Idioma

- Documentación, nomenclatura, referencias y artefactos guardados: **español por defecto**.
- Mantener inglés solo para nombres oficiales, APIs, código o literales técnicos inevitables.

## Formato

- A4 vertical como formato general por defecto.
- 25,4 mm como margen seguro por defecto.
- En CREAR, aproximadamente 20–25,4 mm puede usarse solo cuando mejora materialmente la composición y pasa QA.
- No miniaturizar contenido para cumplir una página.

## Gobernanza

- GitHub es la única fuente canónica de la skill.
- Una decisión aprobada no se reinterpreta silenciosamente en versiones posteriores.
- Antes de modificar una regla establecida, revisar este archivo y cualquier referencia bloqueada aplicable.
- Si una nueva propuesta contradice una decisión bloqueada, prevalece la decisión bloqueada hasta que el usuario la cambie explícitamente.

## Modos

- CREAR: diseño nuevo dentro del estándar.
- ADAPTAR: preservar sistema aprobado y cambiar solo lo necesario.
- REPLICAR: máxima fidelidad; solo cambios solicitados o reparaciones imprescindibles.

## Regla de regresión

Toda versión nueva debe comprobar que no cambia accidentalmente:
1. tipografía oficial;
2. idioma operativo;
3. modos;
4. fuente canónica;
5. decisiones de preservación/fidelidad;
6. defaults de formato aprobados.

Una mejora visual nunca autoriza romper estas decisiones.
