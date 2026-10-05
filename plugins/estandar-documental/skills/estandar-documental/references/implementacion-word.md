# Implementación Word nativa — v1.3.2

## Principio

La estructura Word debe ser semántica, editable y mantenible **sin reducir el documento a una apariencia genérica**. Usar la capacidad documental disponible; Estándar Documental gobierna propósito, sistema visual, arquitectura, fidelidad y aceptación.

En ADAPTAR/REPLICAR, la referencia válida del usuario/proyecto gobierna sobre defaults genéricos.

## Valores por defecto y adaptabilidad

Para CREAR:
- A4 vertical como punto de partida;
- márgenes 20–25,4 mm según composición;
- orientación horizontal solo cuando aporte una ventaja funcional clara;
- sistema visual obligatorio: referencia/brand o [Sistema Visual por Defecto](sistema-visual-default.md).

No reducir tipografía o visuales hasta hacerlos incómodos de leer.

## Tipografía

- Evitar Calibri como salida genérica de CREAR.
- Usar primero tipografía aprobada; si no existe, Avenir Next → Manrope → Aptos según disponibilidad real.
- Verificar render final; si la fuente sustituye o falla, elegir el siguiente fallback.
- Aplicar estilos Word para los roles repetibles en lugar de formato directo masivo.

## Estructura semántica

- usar estilos Título/Heading reales para estructura;
- listas nativas y numeración semántica;
- tablas semánticas para datos/comparación/registro;
- una estructura tabular **puede** usarse como soporte de composición simple si mejora el escaneo y mantiene orden de lectura obvio, pero no para párrafos narrativos densos ni como falsa tabla de datos;
- evitar alturas fijas que recorten;
- mantener headings/captions unidos a su contenido;
- preservar orden de lectura, proporciones, hipervínculos y secciones válidas.

## Composición

La implementación Word debe obedecer [Composición Adaptativa](composicion-adaptativa.md) y el sistema visual elegido.

Si el documento se ve como Word por defecto:
1. no liberar;
2. revisar jerarquía;
3. aplicar tokens tipográficos/cromáticos;
4. mejorar agrupación y ritmo;
5. incorporar una estructura visual útil si aporta escaneo;
6. volver a renderizar.

En una página solicitada explícitamente, revisar el área útil completa. Mucho espacio blanco puede ser válido si es intencional; no es válido cuando refleja contenido mal distribuido.

## Visuales

Canva/diseño puede producir diagramas, mapas conceptuales, marcos, comparativas o recursos gráficos. Integrarlos manteniendo legibilidad, editabilidad y función real.

## Control final

Después del último cambio material:
- renderizar;
- revisar todas las páginas a miniatura y al 100%;
- comprobar clipping, superposición, títulos huérfanos, tablas rotas, miniaturización y vacíos accidentales;
- confirmar balance, jerarquía, tipografía, paleta y ritmo;
- confirmar que el documento no parece un borrador de Word;
- validar accesibilidad y estructura semántica;
- reabrir el DOCX final y repetir render tras cualquier corrección.

La herramienta documental resuelve la mecánica; Estándar Documental decide si el resultado es profesionalmente aceptable.
