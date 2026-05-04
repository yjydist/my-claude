# My Claude Marketplace

Personal Claude Code plugins and skills collection.

## Usage

Add this marketplace to Claude Code:

```bash
/plugin marketplace add https://github.com/yjydist/my-claude
```

Then install plugins:

```bash
/plugin install git@my-claude
```

## Plugins

| Plugin | Description |
|--------|-------------|
| **git** | Git workflow tools including commit message generation with Conventional Commits support |

## git Plugin

### Skills

- **`/git:git-commit-msg`** - Analyze staged/unstaged changes and generate Conventional Commits style commit messages

### How it works

The `git-commit-msg` skill runs a bundled Python script that analyzes your repository's git state:

- Current branch name
- Staged, unstaged, and untracked files
- File categorization (source, test, docs, config, scripts, assets)
- Diff statistics and preview
- Recent commit history (for style reference)

Based on this analysis, it suggests an appropriate Conventional Commits message with the correct type (`feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`, `build`, `revert`).

## Development

### Local testing

Test a plugin locally:

```bash
claude --plugin-dir ./plugins/git
```

### Validate

Validate marketplace and plugin structure:

```bash
claude plugin validate .
```

## Adding New Plugins

1. Create a new directory under `plugins/`
2. Add `.claude-plugin/plugin.json` manifest
3. Add skills, agents, hooks, or other components
4. Register the plugin in `.claude-plugin/marketplace.json`
