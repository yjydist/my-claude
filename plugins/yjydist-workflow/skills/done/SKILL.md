---
name: done
description: This skill should be used when the user invokes `/yjydist-workflow:done`, asks to close an existing PLAN.md workflow, verify acceptance criteria, confirm all checklist work is complete, or delete the temporary PLAN.md after successful verification and explicit confirmation.
argument-hint: [optional notes]
allowed-tools: Read, Bash(rm:*), Bash(ls:*), Bash(test:*)
version: 0.1.0
---

# Done Skill

Close the current lightweight workflow by checking `PLAN.md` against its acceptance criteria and deleting the temporary plan only after user confirmation.

## Core Principles

- Treat `PLAN.md` as temporary workflow scratch space.
- Verify acceptance before cleanup.
- Ask for explicit user confirmation before deleting `PLAN.md`.
- Delete `PLAN.md` after confirmation instead of archiving it.
- Do not create `LOG.md`, `.skill-rules`, archive folders, or replacement summary files.

## Required First Step

Read `PLAN.md` from the current working directory.

If `PLAN.md` is missing:

1. Tell the user there is no active workflow plan to close.
2. Stop without creating or deleting anything.

## Closeout Workflow

1. Read the `Goal`, `Acceptance`, `Boundaries`, and `Implementation Plan` sections.
2. Check whether every implementation task is completed or intentionally deferred by the user.
3. Check whether each acceptance item appears satisfied.
4. If acceptance is not satisfied, explain what remains and suggest returning to `/yjydist-workflow:do`.
5. If acceptance appears satisfied, summarize the result briefly.
6. Ask the user to confirm deletion of `PLAN.md`.
7. Wait for an explicit affirmative response such as `yes`, `confirm`, or `delete PLAN.md`. Treat silence, ambiguity, or new instructions as no confirmation.
8. Delete `PLAN.md` only after explicit confirmation.
9. Report that the workflow is closed.

## Verification Guidance

Use the acceptance criteria as the primary source of truth. Do not rely only on checked implementation tasks. A plan can have all tasks checked while still failing acceptance.

When verification requires commands or manual review:

- Run safe local checks when they are clearly implied by the acceptance criteria and available through the current tool permissions.
- If a check needs tools or commands that are unavailable, state the exact check that could not be run.
- Ask the user for confirmation when acceptance depends on subjective review or external systems.
- State clearly when an acceptance item could not be verified.

## Deletion Rule

Delete only `PLAN.md` in the current working directory. Do not remove archives, notes, generated outputs, source files, or other project files as part of this skill.

If the user asks to keep the plan instead, leave it in place and stop.

## Completion Message

After deleting `PLAN.md`, provide a short closeout message:

- State that the workflow is complete.
- Mention that `PLAN.md` was deleted.
- Avoid creating a separate summary document.
