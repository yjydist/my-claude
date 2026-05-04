---
name: git-commit-msg
description: This skill should be used when the user asks to "generate a commit message", "write a commit message", "suggest a conventional commit", "summarize these git changes", or "what should I commit this as". Analyze staged, unstaged, or untracked Git changes and produce a Conventional Commits style message.
user-invocable: false
---

# Git Commit Message Generator

Analyze repository changes and generate concise, professional commit messages that follow the Conventional Commits specification.

## Workflow

### 1. Analyze Changes

Run the bundled analysis script to get a structured summary of repository changes:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/analyze_git_changes.py"
```

The script outputs JSON containing:

- Current branch name
- Whether changes are staged, unstaged, or untracked
- File count and categorization (source, test, docs, config, scripts, assets, other)
- Diff statistics (insertions / deletions)
- Diff preview (up to 8000 characters)
- Recent commit messages (as style references)

### 2. Decide the Commit Scope

Prefer staged changes when available. If the repository contains both staged and unstaged or untracked changes, generate the commit message for the staged changes and explicitly note that other working tree changes exist.

If no staged changes exist, analyze the full working tree and make that basis explicit in the explanation.

### 3. Generate Commit Message

Use the analysis output to choose the commit message. Determine the type from the primary behavior change, not just the file extensions or categories.

#### Type Selection (Conventional Commits)

Choose the most appropriate type based on the nature of the changes:

| Type | Usage Scenario |
|------|----------------|
| `feat` | New feature, capability, or functionality |
| `fix` | Bug fix or error correction |
| `docs` | Documentation-only changes |
| `style` | Formatting-only changes with no behavior change |
| `refactor` | Code restructuring without behavior change |
| `perf` | Performance optimization |
| `test` | Adding or modifying tests or test infrastructure |
| `chore` | Tooling, maintenance, or repository housekeeping |
| `ci` | CI/CD configuration changes |
| `build` | Build system or dependency management changes |
| `revert` | Reverting a previous commit |

Use file categorization only as a supporting signal. Do not infer the type from category counts alone.

#### Scope (Optional but Recommended)

Add a scope only when the changes are clearly concentrated in one module, package, component, or subsystem. Omit the scope when the changes span multiple unrelated areas.

Examples:

```text
feat(auth): add OAuth2 login support
fix(api): resolve null pointer issue on user endpoint
```

#### Subject Line

- Maximum 72 characters
- Use imperative mood ("add" not "added" or "adding")
- No trailing period
- Lowercase after the type or type/scope prefix

Examples:

- `feat: add user authentication middleware`
- `fix: resolve memory leak in data processor`
- `refactor(api): simplify error handling logic`
- `docs: update deployment instructions`

#### Body (Add When Necessary)

Add a body when the change is complex or needs rationale:

- Leave one blank line after the subject
- Wrap lines to 72 characters when practical
- Explain what changed and why it matters, not the implementation steps
- Mention issue references when relevant

Example:

```text
feat: implement rate limiting for API endpoints

Add token bucket algorithm to prevent abuse of public endpoints.
Default configuration is 100 requests per minute per IP.

Closes #234
```

### 4. Output Format

Return output in exactly two parts:

1. A single commit message inside a code block.
2. A brief explanation of why the type and optional scope were chosen, and whether the message is based on staged changes or the full working tree.

If the changes obviously combine multiple unrelated intentions, recommend splitting them into separate commits before presenting the best single-message fallback.

## Edge Cases

- **No changes detected**: Inform the user there is nothing to commit.
- **Mixed staged and unstaged changes**: Base the message on staged changes and mention the extra working tree changes.
- **Large diffs**: Focus on the highest-signal files and visible behavior changes; note uncertainty if the preview is insufficient.
- **Binary files**: Mention them in the explanation or body if they materially affect the commit.
- **Generated files or lockfiles**: Treat them as supporting changes unless they are the main purpose of the commit.

## Recent Commit Style Reference

Use recent commit subjects from the analysis output to match repository wording and tone, but keep Conventional Commits structure as the higher priority.
