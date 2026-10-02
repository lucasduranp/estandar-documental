# Implementación Word nativa — v1.3

## Principio

La estructura Word debe ser semántica, editable y mantenible. Usar la capacidad documental disponible para construir y editar DOCX; Estándar Documental gobierna propósito, arquitectura, fidelidad y aceptación.

En ADAPTAR/REPLICAR, la referencia válida del usuario/proyecto gobierna sobre defaults genéricos.

## Valores por defecto y adaptabilidad

Para CREAR:
- A4 vertical como punto de partida;
- márgenes de 25,4 mm como default seguro;
- aproximadamente 20–25,4 mm cuando mejore materialmente el uso de página sin reducir legibilidad;
- orientación horizontal solo cuando aporte una ventaja funcional clara.

No reducir tipografía o visuales hasta hacerlos incómodos de leer para cumplir un número de páginas arbitrario.

La familia tipográfica debe ser profesional, disponible en el entorno de destino y coherente con la referencia/proyecto. Aptos puede ser válida, pero no es una obligación universal.

## Estructura

- usar estilos Título/Encabezado reales;
- listas nativas y numeración semántica;
- tablas para datos, comparaciones y registros estructurados, no como mecanismo genérico de layout;
- encabezados semánticos de tabla;
- evitar alturas fijas que recorten contenido;
- mantener headings unidos al contenido siguiente;
- mantener captions unidos a sus visuales;
- preservar orden de lectura;
- mantener relaciones de aspecto;
- texto alternativo significativo;
- hipervínculos reales;
- secciones válidas.

## Composición

La implementación Word debe obedecer [Composición Adaptativa](composicion-adaptativa.md), no una plantilla fija.

Si una tabla, visual o bloque no funciona:
1. corregir contenido/arquitectura;
2. cambiar representación;
3. redistribuir espacio;
4. añadir página si es necesario;
5. solo después ajustar tamaños dentro de rangos profesionales.

## Visuales

Canva/diseño puede producir diagramas, mapas conceptuales, marcos, comparativas o recursos gráficos. Integrarlos en Word de manera que:
- el recurso siga siendo legible;
- el texto principal no quede rasterizado innecesariamente;
- no se deforme ni recorte sin intención;
- la composición general siga editable y navegable;
- el visual tenga función real.

## Control final

Después del último cambio material:
- renderizar;
- revisar todas las páginas;
- confirmar que no existen clipping, superposición, títulos huérfanos, tablas rotas, páginas vacías, miniaturización o vacíos accidentales;
- validar accesibilidad y estructura semántica;
- revisar fidelidad cuando aplique.

La herramienta documental resuelve la mecánica; Estándar Documental decide si el resultado es profesionalmente aceptable.
