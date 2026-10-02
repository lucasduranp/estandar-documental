# Scripts auxiliares

Estándar Documental v1.3 no depende de un runtime propio para producir documentos.

Los scripts presentes aquí son **helpers de validación/regresión**, no el motor principal de creación. La ejecución normal debe usar primero las capacidades especialistas disponibles en la plataforma.

Helpers conservados:
- `release_gate.py`: comprobación auxiliar de estado de liberación heredado;
- `regression_preflight.py`: inventario de casos de regresión histórica;
- `self_test.py`: tests auxiliares heredados.

No añadir nuevos scripts si una herramienta existente ya resuelve la misma función de forma mantenida y verificable.
