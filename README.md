# Estándar Documental

Fuente canónica de **Estándar Documental v1.3.3 CANDIDATA**.

## Decisiones bloqueadas

Antes de cualquier cambio revisar `plugins/estandar-documental/skills/estandar-documental/references/decisiones-bloqueadas.md`.

Reglas clave:
- **Aptos es la tipografía oficial de todos los documentos.**
- Avenir Next pertenece a publicaciones de LinkedIn de Agrícola Zhong Yi, no a Estándar Documental.
- Español por defecto.
- GitHub es la única fuente canónica.
- Ninguna versión puede cambiar decisiones aprobadas sin instrucción explícita del usuario.

## Arquitectura vigente

```
plugins/
└── estandar-documental/
    ├── plugin.json
    ├── .codex-plugin/
    │   └── plugin.json
    └── skills/
        └── estandar-documental/
            ├── SKILL.md
            ├── agents/openai.yaml
            └── references/

.agents/plugins/marketplace.json
```

El plugin es la unidad de distribución para Desktop/Codex/Work. La copia cloud de ChatGPT Web, cuando se use, debe derivar de la misma skill y versión.

## Estado

Versión: **1.3.3 CANDIDATA**.
Pendiente de un retest final después de restaurar la decisión tipográfica Aptos.
