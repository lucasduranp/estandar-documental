# Cambios — v1.3.2

## Corrección de regresión visual

La v1.3.1 resolvió problemas semánticos y de balance, pero sobrecorrigió hacia una salida genérica de Word. La comparación con el documento visualmente superior mostró que faltaba una **dirección visual positiva**, no solo restricciones.

### Añadido

- Sistema Visual por Defecto — Editorial Ejecutivo;
- selección obligatoria de fuente visual antes de CREAR;
- gate de genericidad;
- prioridad tipográfica Avenir Next → Manrope → Aptos según disponibilidad;
- paleta editorial neutra por roles;
- arquetipos positivos para COMPACTO_OPERACIONAL;
- permiso controlado de estructuras multicolumna simples cuando mejoran el escaneo;
- bloqueo explícito de Calibri/default Word sin justificación;
- evals AQ11, AQ12 y NEG08.

### Conservado

- estructura Word semántica;
- coherencia título/alcance;
- render final obligatorio;
- balance de página;
- integridad, fidelidad y accesibilidad.

### Estado

CANDIDATA hasta repetir el mismo smoke test y confirmar que combina calidad visual intencional con estructura Word correcta.
