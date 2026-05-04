#!/usr/bin/env python3
import json
import re
import subprocess
from collections import Counter


def git(*args):
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip()


def shortstat(text):
    match = re.search(
        r"(?:(\d+) files? changed)?(?:, (\d+) insertions?\(\+\))?(?:, (\d+) deletions?\(-\))?",
        text,
    )
    if not match:
        return {"files": 0, "insertions": 0, "deletions": 0}
    files, insertions, deletions = match.groups()
    return {
        "files": int(files or 0),
        "insertions": int(insertions or 0),
        "deletions": int(deletions or 0),
    }


def category_for(path):
    lower = path.lower()
    name = lower.rsplit("/", 1)[-1]

    if any(part in lower for part in ("/test/", "/tests/", "/spec/", "__tests__/")):
        return "test"
    if name.startswith(("test_", "test.", "spec.",)) or ".test." in name or ".spec." in name:
        return "test"
    if name in {"readme.md", "changelog.md"} or lower.endswith((".md", ".mdx", ".rst", ".txt")):
        return "docs"
    if any(part in lower for part in ("/.github/", "/.gitlab/", "/ci/", "/workflows/")):
        return "ci"
    if name in {
        "package.json",
        "package-lock.json",
        "pnpm-lock.yaml",
        "yarn.lock",
        "tsconfig.json",
        "pyproject.toml",
        "cargo.toml",
        "go.mod",
        "go.sum",
        "makefile",
        "dockerfile",
    } or lower.endswith((".json", ".yaml", ".yml", ".toml", ".ini", ".cfg")):
        return "config"
    if any(part in lower for part in ("/scripts/", "/bin/", "/hack/")) or lower.endswith((".sh", ".ps1")):
        return "scripts"
    if lower.endswith((
        ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".mp4", ".mov", ".pdf",
    )):
        return "assets"
    if lower.endswith((
        ".js", ".jsx", ".ts", ".tsx", ".py", ".rb", ".go", ".rs", ".java", ".kt", ".c", ".cc", ".cpp", ".h", ".hpp", ".cs", ".php", ".swift",
    )):
        return "source"
    return "other"


branch = git("rev-parse", "--abbrev-ref", "HEAD") or "HEAD"
staged_files = [line for line in git("diff", "--cached", "--name-only").splitlines() if line]
unstaged_files = [line for line in git("diff", "--name-only").splitlines() if line]
untracked_files = [line for line in git("ls-files", "--others", "--exclude-standard").splitlines() if line]
all_files = sorted(set(staged_files + unstaged_files + untracked_files))

has_staged = bool(staged_files)
has_unstaged = bool(unstaged_files)
has_untracked = bool(untracked_files)

if has_staged and (has_unstaged or has_untracked):
    change_scope = "mixed"
elif has_staged:
    change_scope = "staged"
elif has_unstaged:
    change_scope = "unstaged"
elif has_untracked:
    change_scope = "untracked-only"
else:
    change_scope = "clean"

categories = Counter(category_for(path) for path in all_files)
combined_diff = []
if has_staged:
    combined_diff.append("### STAGED DIFF\n" + git("diff", "--cached", "--stat", "--patch"))
if has_unstaged:
    combined_diff.append("### UNSTAGED DIFF\n" + git("diff", "--stat", "--patch"))
if has_untracked:
    combined_diff.append("### UNTRACKED FILES\n" + "\n".join(untracked_files))
diff_preview = "\n\n".join(part for part in combined_diff if part)[:8000]

report = {
    "branch": branch,
    "change_scope": change_scope,
    "has_staged": has_staged,
    "has_unstaged": has_unstaged,
    "has_untracked": has_untracked,
    "file_count": len(all_files),
    "files_by_category": dict(sorted(categories.items())),
    "diff_stats": {
        "staged": shortstat(git("diff", "--cached", "--shortstat")),
        "unstaged": shortstat(git("diff", "--shortstat")),
        "untracked": {"files": len(untracked_files), "insertions": 0, "deletions": 0},
    },
    "diff_preview": diff_preview,
    "recent_commits": [
        line for line in git("log", "-5", "--pretty=format:%s").splitlines() if line
    ],
}

print(json.dumps(report, indent=2, ensure_ascii=False))
