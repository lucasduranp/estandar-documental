# Implementación Word nativa — v1.3.4

## Principio

La estructura Word debe ser semántica, editable, mantenible y visualmente profesional. El especialista oficial de documentos ejecuta; Estándar Documental gobierna.

Antes de ejecutar, leer [Decisiones bloqueadas](decisiones-bloqueadas.md).

## Ruta técnica

- En Work/Codex usar explícitamente **@Documents / Documents**.
- No usar runtime heredado ni loader local propio como ruta principal.
- Si @Documents no está disponible, informar esa limitación en vez de improvisar otro runtime.

## Valores por defecto

Para CREAR:
- A4 vertical;
- márgenes 20–25,4 mm según composición;
- orientación horizontal solo con ventaja funcional;
- sistema visual obligatorio: referencia compatible o Sistema Visual por Defecto.

## Tipografía — decisión bloqueada

- **Aptos es la única tipografía oficial.**
- Declarar Aptos en estilos/tema/runs del DOCX.
- No usar Avenir Next, Manrope, Calibri ni otra familia como fallback.
- La disponibilidad de Aptos en un preview auxiliar no gobierna el archivo.
- Si el preview no dispone de Aptos, no cambiar la fuente: comprobar que el DOCX sigue declarando Aptos y realizar QA visual con holgura de composición.
- El destino primario es Microsoft Word / Microsoft 365.

## Estructura semántica

- estilos Título/Heading reales;
- listas nativas;
- tablas semánticas para datos/comparación/registro;
- estructuras de composición solo cuando mejoren claramente el escaneo;
- orden de lectura preservado;
- sin clipping ni alturas fijas frágiles;
- hipervínculos y secciones válidas.

## Composición

Si el documento se ve como Word genérico:
1. no liberar;
2. revisar jerarquía;
3. mejorar color, ritmo y agrupación;
4. mantener Aptos;
5. volver a renderizar/previsualizar.

Diseñar con holgura; evitar layouts que dependan de ajustes milimétricos de una fuente instalada localmente.

## Control final

Después del último cambio material:
- verificar en el DOCX que Aptos está declarada;
- reabrir el DOCX;
- renderizar/previsualizar con la capacidad disponible;
- revisar todas las páginas a miniatura y 100%;
- comprobar clipping, superposición, balance, jerarquía, paleta y ritmo;
- validar accesibilidad y estructura;
- si el preview sustituye Aptos, tratarlo como limitación del preview y no como sustitución del archivo.

La conformidad tipográfica se determina por el DOCX y su target Word/Microsoft 365, no por la lista de fuentes del renderer auxiliar.
