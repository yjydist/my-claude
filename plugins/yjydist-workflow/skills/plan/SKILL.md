---
name: plan
description: This skill should be used when the user invokes `/yjydist-workflow:plan`, asks to make a plan first, create a temporary PLAN.md, clarify scope before coding, define goal/acceptance/boundaries, or turn a task idea into a lightweight implementation checklist.
argument-hint: [task idea]
allowed-tools: Read, Write, Edit, Bash(ls:*), Bash(pwd:*)
version: 0.1.0
---

# Plan Skill

Create or update a temporary `PLAN.md` that acts as the collaboration contract for the current task. Keep the workflow lightweight: one task, one temporary plan file, no logs, no archives, no persistent preference files.

## Core Principles

- Separate requirements from implementation tasks.
- Define acceptance before implementation.
- Keep the plan short enough to guide action without becoming project documentation.
- Treat `PLAN.md` as temporary scratch space, not a project asset.
- Do not create `LOG.md`, `.skill-rules`, archive folders, or extra workflow files.

## Workflow

1. Understand the user's task idea from the invocation argument, if provided, and the current conversation.
2. If the task is underspecified, ask concise clarifying questions before writing `PLAN.md`.
3. Clarify these requirement fields:
   - Goal: the final outcome the user wants.
   - Acceptance: observable checks that prove the goal is complete.
   - Boundaries: explicit non-goals, files, technologies, or behaviors to avoid.
4. After requirements are clear, derive implementation tasks from those requirements.
5. Write `PLAN.md` in the current working directory.
6. Tell the user that the plan is ready and suggest running `/yjydist-workflow:do` when they want execution to begin.

## Clarifying Questions

Prefer asking 1-3 focused questions when details are missing. Good questions identify decisions that affect scope or correctness, not boilerplate preferences.

Ask about:

- What counts as successful completion.
- What must stay out of scope.
- Whether there are constraints on files, dependencies, tools, tests, or runtime behavior.
- Whether the user wants a small first milestone or a fuller implementation pass.

Skip questions when the user has already provided enough detail to produce a safe, useful plan.

## PLAN.md Template

Use this exact structure:

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
- [ ] {{Task derived from requirements}}
```

## Writing Guidelines

- Use a concise title that describes the current task.
- Keep `Goal` focused on outcomes, not implementation steps.
- Keep `Acceptance` concrete and checkable. Prefer commands, observable behavior, or review criteria when applicable.
- Keep `Boundaries` explicit. Ask once for boundaries when scope is unclear; use `- None specified` only after the user declines or no meaningful boundary is apparent.
- Keep implementation tasks action-oriented and derived from requirements.
- Avoid over-splitting. A short plan with 3-7 meaningful tasks is usually better than a long checklist.
- Use current repository language and tooling when known, but avoid inventing details not established by the user or codebase.

## Updating Existing PLAN.md

If `PLAN.md` already exists:

1. Read it before making changes.
2. Ask whether to replace it when it appears to describe a different task.
3. Update it directly when the user is continuing the same task.
4. Do not silently discard existing plan content.

## Completion

End by summarizing the plan in one or two sentences. Do not start implementation during this skill unless the user explicitly asks to combine planning and execution.
