# Validación — Estándar Documental v1.3 CANDIDATA

## Estado actual

**CANDIDATA VALIDADA CONTRA LA ESPECIFICACIÓN ACTUAL DE SKILL CREATOR. NO PROMOVIDA A VIGENTE.**

La revisión se realizó contra el `Skill Creator` oficial de OpenAI y su `quick_validate.py`, además de la especificación actual de `agents/openai.yaml`.

## Ajustes aplicados

- la skill instalable quedó aislada en `estandar-documental/`;
- la carpeta instalable contiene solo `SKILL.md`, `agents/openai.yaml` y referencias necesarias;
- README, changelog, evals, regresión y archivo histórico quedaron fuera del paquete instalable;
- `SKILL.md` usa únicamente `name` y `description` en el frontmatter;
- se redujo el cuerpo a instrucciones operativas y referencias de carga progresiva;
- `agents/openai.yaml` incorpora nombre visible, descripción corta y prompt por defecto;
- el prompt por defecto menciona explícitamente `$estandar-documental`;
- la carpeta de la skill coincide exactamente con su nombre técnico;
- no se incluyen scripts ni assets sin necesidad funcional.

## Resultados de validación

- nombre: `estandar-documental` — válido, hyphen-case y menor a 64 caracteres;
- description: 369 caracteres — dentro del máximo de 1024 y sin caracteres prohibidos;
- frontmatter: solo `name` + `description`;
- SKILL.md: 63 líneas — por debajo de la recomendación de 500;
- `short_description`: 40 caracteres — dentro del rango recomendado 25–64;
- `default_prompt`: referencia `$estandar-documental`;
- referencias: un nivel de profundidad desde SKILL.md;
- documentación auxiliar de desarrollo: fuera de la carpeta instalable.

## Pendiente

1. Pruebas reales de COMPACTO, ANALÍTICO, ESTUDIO, ADAPTAR y REPLICAR.
2. Instalación desde la misma release en ChatGPT Web.
3. Instalación en Desktop/Codex mediante Skill Installer.
4. Smoke test de disponibilidad y comportamiento en ambas superficies.
5. Promoción a VIGENTE solo si no aparecen fallos materiales.

## Regla de promoción

No declarar FINAL/VIGENTE por el mero hecho de pasar validación estructural. La promoción exige prueba funcional y verificación de instalación.
