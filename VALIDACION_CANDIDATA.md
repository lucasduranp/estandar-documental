# Validación — Estándar Documental v1.3

## Estado

**MIGRADA A PLUGIN SKILLS-ONLY. PENDIENTE DE SMOKE TEST FUNCIONAL.**

## Verificado

- manifest portable en `plugins/estandar-documental/plugin.json`;
- fallback compatible en `plugins/estandar-documental/.codex-plugin/plugin.json`;
- skill en `plugins/estandar-documental/skills/estandar-documental/`;
- plugin sin MCP, apps, hooks ni scripts innecesarios;
- marketplace repo en `.agents/plugins/marketplace.json`;
- marketplace apunta al repositorio público y a `./plugins/estandar-documental`;
- manifest portable usa el schema Agent Plugins 1.0;
- presentación OpenAI vive en `extensions.com.openai`;
- copia activa antigua de la skill en raíz eliminada;
- evals, regresión y archivo histórico permanecen fuera del plugin.

## Pendiente

1. Instalar/actualizar el plugin desde el marketplace.
2. Ejecutar un DOCX real en Work.
3. Verificar invocación en Codex.
4. Si pasa, marcar v1.3.0 como VIGENTE.
