# Validación — Estándar Documental v1.3.3 CANDIDATA

## Estado

**CORREGIDA REGRESIÓN DE GOBERNANZA: APTOS RESTAURADA COMO DECISIÓN BLOQUEADA.**

## Error detectado

v1.3.2 introdujo Avenir Next → Manrope → Aptos como prioridad tipográfica. Eso contradijo una decisión histórica ya aprobada.

La regla correcta es:
- Aptos = tipografía oficial de documentos;
- Avenir Next = publicaciones de LinkedIn de Agrícola Zhong Yi;
- no mezclar ambos sistemas.

## Corrección v1.3.3

- se crea `decisiones-bloqueadas.md`;
- Aptos pasa a gate obligatorio en SKILL.md, sistema visual, implementación Word y QA;
- se elimina cualquier fallback a Avenir Next/Manrope/Calibri;
- si Aptos no está disponible, se bloquea en vez de degradar;
- se añade regresión para impedir que futuras versiones cambien decisiones aprobadas;
- el sistema visual positivo permanece, pero siempre construido con Aptos.

## Pendiente

1. actualizar plugin a v1.3.3;
2. repetir el mismo smoke test;
3. aprobar solo si combina: Aptos + calidad visual intencional + estructura Word correcta;
4. si pasa, marcar v1.3.3 como VIGENTE.
