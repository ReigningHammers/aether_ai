# Aether - Personal Momentum Engine 🧠

**Local-first, API-first Jarvis successor built for ReigningHammers empire.**

Unifies AI reasoning, home control, memory graph, voice personas, and smart task routing into one sovereign layer.

## How It Works (Core Philosophy)
1. **Command Intake** (`POST /v1/command`) → Any natural language or structured request.
2. **Unified Flow** (enforced contract):
   - Core API → Enrich with Memory Graph → Safety/Permissions → CLI Brain Router (decides Grok/local/Claude) → Executor (Skill modules) → Event Log + PDCA trace → Persona-formatted Response (Kal/Val/Aether).
3. **Modular Skills** — All plug into the same FastAPI app without creating new silos.

## Quick Start - Windows
See `setup.ps1` / Docker Desktop.

## Skills Status
- ✅ Skill 1 Core API
- 🟡 Skill 2+ (ready for expansion)

Full docs in `/docs`.