# Correcciones de implementación probadas — archivo histórico

Este documento conserva hallazgos técnicos de la línea PDS/v1.1-v1.2. **No gobierna Estándar Documental v1.3.**

## Discrepancia de alineación

El espécimen aprobado tenía sobreescrituras directas de alineación que los lint históricos no detectaban. La corrección probada consistió en trasladar alineaciones a estilos derivados sin cambiar formato efectivo, tabla, tema ni numeración. Los Goldens originales permanecieron inmutables y el render comparado se mantuvo visualmente equivalente.

## Defecto de rejilla PR01

El constructor histórico conservaba una rejilla de cinco columnas iguales aunque los anchos de celda indicaban otra geometría. La reparación sincronizó únicamente esos cinco anchos de rejilla con los anchos de celda existentes, preservando contenido, fuentes y estructura no relacionada.

## Manifiesto histórico

Las entradas de payload del paquete fuente coincidieron con sus hashes, salvo la autoentrada del manifiesto histórico que usaba el hash de archivo vacío. Este defecto está registrado en `regression/provenance.json`.

## Renderizador histórico

La validación histórica utilizó LibreOffice y Aptos nativa. Esto documenta aquella regresión; **no convierte LibreOffice ni Aptos en requisitos universales de v1.3**.

La fuente histórica completa permanece identificada por hash en la procedencia de regresión.
