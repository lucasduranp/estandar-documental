# Selección de perfiles — v1.3

Los perfiles definen **qué optimizar**, no cómo debe verse cada página. La Composición Adaptativa decide la representación y composición concreta.

| Perfil canónico | Literal técnico heredado | Optimiza | Prueba de uso final |
|---|---|---|---|
| **COMPACTO_OPERACIONAL** | `COMPACT_OPERATIONAL` | rapidez + acción | ¿El lector encuentra decisión, estado y próximos pasos sin releer? |
| **ANALÍTICO_NEGOCIO** | `ANALYTICAL_BUSINESS` | evidencia + comparación + decisión | ¿Puede evaluar conclusión, supuestos, cálculos y compensaciones? |
| **VISUAL_COMERCIAL** | `VISUAL_COMMERCIAL` | narrativa + marca + comunicación respaldada | ¿Entiende la oferta/mensaje sin afirmaciones ni decoración injustificada? |
| **REFERENCIA_RÁPIDA_OPERACIONAL** | `QUICK_REFERENCE_OPERATIONAL` | recuperación + ejecución inmediata | ¿Puede localizar una regla, paso o dato en segundos durante el trabajo? |
| **ESTUDIO_APRENDIZAJE** | `STUDY_LEARNING` | comprender + conectar + recordar + recuperar + aplicar | ¿El diseño ayuda realmente a aprender y recuperar, no solo a verse más visual? |

## Principios comunes

- Un perfil puede mezclar páginas textuales, tablas y visuales si la función lo exige.
- Una restricción de una página solo existe cuando el encargo la requiere; nunca miniaturizar para alcanzarla.
- A4 vertical es el valor por defecto, no una obligación estética universal. Horizontal u otra excepción exige beneficio material y control visual.
- El perfil no autoriza afirmaciones sin respaldo, decoración gratuita ni pérdida de editabilidad/accesibilidad.

## ESTUDIO_APRENDIZAJE

Aplicar [Estudio y Aprendizaje](estudio-aprendizaje.md). Debe usar más señalización visual que los otros perfiles, pero sin cuota fija de imágenes. Color, diagramas, ejemplos resueltos, comparativas y preguntas de recuperación se justifican por su función cognitiva.

## Ruta de respaldo empaquetada

El constructor canónico empaquetado sigue calificado solo para COMPACTO_OPERACIONAL y ANALÍTICO_NEGOCIO mediante sus literales técnicos heredados. VISUAL_COMERCIAL, REFERENCIA_RÁPIDA_OPERACIONAL y ESTUDIO_APRENDIZAJE requieren una ruta con especialista mientras no exista una implementación empaquetada equivalente y validada. No fingir soporte: si el especialista necesario no está disponible y la función del perfil depende de él, bloquear o reducir el alcance de forma explícita.
