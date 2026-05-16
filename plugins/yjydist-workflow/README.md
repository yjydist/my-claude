# yjydist-workflow

A lightweight personal workflow for Claude Code.

## Workflow

Use three user-invoked skills. In Claude Code, invoke them with the plugin namespace:

- `/yjydist-workflow:plan` clarifies requirements and writes `PLAN.md`.
- `/yjydist-workflow:do` reads `PLAN.md` and executes the implementation plan.
- `/yjydist-workflow:done` checks acceptance criteria and deletes `PLAN.md` after user confirmation.

## PLAN.md Format

```markdown
# {{Task Title}}

## Requirements

### Goal
- {{Final outcome}}

### Acceptance
- {{Verifiable completion standard}}

### Boundaries
- {{Explicitly out of scope}}

## Implementation Plan

- [ ] {{Task derived from requirements}}
- [ ] {{Task derived from requirements}}
```

## Principles

- Keep only one temporary workflow file: `PLAN.md`.
- Separate requirements from implementation tasks.
- Define acceptance before implementation.
- Do not create `LOG.md`, `.skill-rules`, or archives.
- Delete `PLAN.md` when the task is accepted as complete.

## Not Included

- No legacy `commands/` directory.
- No agents, hooks, MCP servers, settings, logs, or archives.
