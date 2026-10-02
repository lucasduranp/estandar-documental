# Protocolo de regresión

Autoridad: paquete aprobado por el usuario en `regression/approved-v1.1`. Su nombre todavía dice Candidate; el usuario aprobó expresamente esa versión. Mantener constructores fuente, casos, Goldens y aserciones originales sin cambios. La implementación original de aserciones se conserva incluso cuando los controles mejorados son más estrictos.

## Reproducción

Dependencias: Python 3 con python-docx, lxml y PyMuPDF; ejecutable LibreOffice; Aptos nativa disponible para ese renderizador. PyYAML se requiere adicionalmente para el validador de creación de skills. Usar el Python empaquetado del entorno y dependencias locales a la tarea cuando sea necesario. No empaquetar fuentes propietarias ni cambiar silenciosamente configuración de fuentes del sistema.

```text
python scripts/run_regression.py --work-dir EMPTY_DIRECTORY --soffice PATH_TO_SOFFICE
python scripts/enhanced_checks.py EMPTY_DIRECTORY
python scripts/self_test.py
```

Los literales de comando permanecen en inglés porque son interfaces técnicas. Usar rutas absolutas de script fuera del directorio de la skill. El ejecutor requiere un directorio vacío para excluir renders obsoletos. Solo adapta las cuatro rutas de entorno de los scripts originales, recupera la imagen GD07 exacta desde la relación del DOCX aprobado, reconstruye casos crudos y exige que cada parte interna coincida con los Goldens. Luego aplica únicamente la normalización de alineación documentada y la corrección de rejilla PR01, ejecuta los auditores históricos incluidos, renderiza de nuevo, comprueba fuentes incrustadas y ejecuta las 148 aserciones sin cambios. Finaliza con código distinto de cero ante fallos de aserción/fuente o dependencias ausentes. Informes y PNG son evidencia, no aprobación visual manual.

Las 31 aserciones mejoradas añaden controles de formato directo de historia completa, integridad XML/relaciones, pareo de valores de fila GD04, consistencia de rejilla PR01 y preservación de delta estrecho. Los 11 tests auxiliares verifican comportamiento de fallo, incluyendo manejo de glifos de fuentes de símbolos. Nunca sustituirlos por presencia de texto en un informe QA antiguo.

## Aceptación manual

Inspeccionar cada página final, verificar que el texto sobreviva al render, revisar hashes y completar revisión de fuente/contenido/uso final. Para cambios solo de alineación exigir equivalencia XML efectiva y píxeles renderizados idénticos contra archivos originales. Para PR01 exigir el delta documentado de cinco anchos y revisar la tabla corregida preservando estructura no relacionada. Volver a renderizar e inspeccionar tras cambios; PNG finales idénticos pueden reutilizar inspección solo si existe prueba de hash de la misma imagen exacta.

Ejecutar `quick_validate.py` del creador de skills y verificar enlaces relativos, sintaxis Python, round-trip ZIP y hashes de liberación. Promover solo después de aprobar cada control; los scripts dejan intencionalmente pendientes los controles visuales/de uso final. Los informes QA fuente son históricos. La evidencia actual se encuentra en `validation/` y en el informe de liberación.

La suite cubre ocho ejemplos controlados de una página. No certifica documentos largos arbitrarios ni todas las versiones de Word; los documentos de producción aún requieren sus propios controles.
