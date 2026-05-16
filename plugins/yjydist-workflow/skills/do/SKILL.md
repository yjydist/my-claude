---
name: do
description: This skill should be used when the user invokes `/yjydist-workflow:do`, asks to execute or continue an existing PLAN.md workflow, work through the PLAN.md checklist, complete the next unchecked task, or implement tasks while preserving Goal, Acceptance, and Boundaries.
argument-hint: [optional focus]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, LSP
version: 0.1.0
---

# Do Skill

Execute the implementation plan in the current `PLAN.md`. Use the file as the source of truth for the current task, while keeping the workflow lightweight and temporary.

## Core Principles

- Read `PLAN.md` before taking action.
- Execute from the first unchecked implementation task unless the user provides a focus argument.
- Automatically continue through the plan when safe, with short progress updates at meaningful checkpoints.
- Update checklist status in `PLAN.md` as tasks are completed.
- Do not create `LOG.md`, `.skill-rules`, archive folders, or extra workflow files.
- Do not delete `PLAN.md`; cleanup belongs to `/yjydist-workflow:done`.

## Required First Step

Read `PLAN.md` from the current working directory.

If `PLAN.md` is missing:

1. Tell the user no active workflow plan exists.
2. Suggest running `/yjydist-workflow:plan` with the task idea.
3. Stop without creating a plan unless the user asks to plan now.

## Execution Workflow

1. Parse the `Requirements` section.
2. Parse the `Implementation Plan` checklist.
3. Identify unchecked tasks.
4. If the invocation argument names a task, milestone, or focus area, prioritize the matching unchecked task.
5. Work through unchecked tasks in order when no focus is provided.
6. After completing a task, update its checkbox from `[ ]` to `[x]`.
7. Continue to the next unchecked task when it is safe and still aligned with requirements.
8. Stop and ask the user when a decision would change the `Requirements` section, expand scope, introduce risky actions, or conflict with boundaries.

## Requirement Protection

Treat the `Requirements` section as user-owned. Do not change `Goal`, `Acceptance`, or `Boundaries` unless one of these is true:

- The user explicitly asks to change requirements.
- A contradiction or misunderstanding is discovered and the user confirms the correction.
- The user provides new scope that must be reflected before continuing.

Implementation tasks may be adjusted when discovery reveals a better path. Keep those changes small and directly tied to the existing requirements. If a checklist change is more than marking progress or adding an obviously required follow-up, summarize the proposed edit before applying it.

## Plan Updates

When updating `PLAN.md`:

- Mark completed tasks with `[x]`.
- Add new implementation tasks only when required to satisfy existing acceptance criteria.
- Avoid writing process logs or long notes.
- Keep notes short and inline only when they affect the next action.
- Preserve the template structure.

## Validation

Before declaring the implementation complete:

1. Check all implementation tasks are complete or explicitly deferred by the user.
2. Run or perform implementation checks when practical; final closeout remains part of `/yjydist-workflow:done`.
3. Report any unchecked acceptance item clearly.
4. Suggest `/yjydist-workflow:done` only when acceptance appears satisfied.

## Communication

Provide brief progress updates after meaningful work, not after every tiny step. Explain blockers and requirement conflicts clearly. Keep the conversation focused on action and verification rather than process narration.
