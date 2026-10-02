# Estándar Documental

Repositorio canónico de la skill **Estándar Documental**.

## Estado actual

- Versión: **1.3.0-candidata**
- Estado: **CANDIDATA / NO FINAL**
- Idioma operativo y documental: **español**
- Fuente de verdad: este repositorio
- Skill instalable: `estandar-documental/`
- Antecesor: Professional Document Standard (solo linaje y regresión histórica)

## Gobernanza

Este repositorio es la única fuente canónica. Las instalaciones en ChatGPT Web y Desktop/Codex deben derivarse de la misma versión publicada aquí.

Un ZIP, una instalación local o una copia en un chat no reemplazan esta fuente.

## Estructura

```
estandar-documental/       ← carpeta instalable de la skill
├── SKILL.md
├── agents/openai.yaml
└── references/

evals/                     ← evaluación de desarrollo, no se instala
regression/                ← trazabilidad histórica, no se instala
archivo/                   ← antecedentes heredados, no se instala
CHANGELOG.md
VALIDACION_CANDIDATA.md
VERSION
```

La carpeta instalable contiene solo lo necesario para que la skill funcione. Documentación de desarrollo, changelog, regresión y evals permanecen fuera para evitar contaminar el contexto de la skill.

## Flujo de publicación

BORRADOR → CANDIDATA → VALIDADA → RELEASE CANÓNICA → INSTALADA EN CHATGPT WEB → INSTALADA EN DESKTOP/CODEX → VERIFICADA EN SUPERFICIES → FINAL

## Reglas generales

- Todo contenido y documentación se mantiene en español por defecto.
- No existe fallback operativo al antiguo Professional Document Standard.
- Las referencias históricas sirven solo para regresión y trazabilidad.
- Una pieza aprobada puede quedar bloqueada para ADAPTAR o REPLICAR.
- El estándar prioriza propósito, comprensión, uso real, fidelidad y calidad profesional por sobre plantillas rígidas.

## Instalación Desktop/Codex

La ruta oficial para Skill Installer es:

```
--repo lucasduranp/estandar-documental --path estandar-documental
```

Como el repositorio es privado, Skill Installer usará las credenciales Git existentes o `GITHUB_TOKEN`/`GH_TOKEN` cuando corresponda.

## ChatGPT Web

La instalación web debe derivarse de la misma carpeta `estandar-documental/` de esta release. No mantener una variante funcional separada.
