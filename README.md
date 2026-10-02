# Estándar Documental

Fuente canónica de **Estándar Documental v1.3**.

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

- **GitHub** es la única fuente de verdad.
- El plugin es la unidad de distribución para Desktop/Codex/Work.
- La skill vive dentro del plugin.
- La copia cloud de ChatGPT Web, cuando se use, debe derivar de la misma skill y misma versión.
- No editar copias instaladas manualmente.

## Estado

Versión: **1.3.0**.
Pendiente únicamente del smoke test funcional antes de marcarla VIGENTE.
