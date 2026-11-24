#!/usr/bin/env python3
"""Repository checks for ScrumScribe. No third-party packages needed (PyYAML used if present).

Checks:
  1. Every JSON file parses.
  2. Every skill and agent has frontmatter with a name and a description.
  3. Helper agents only have read-only tools.
  4. No obvious secrets in any tracked text file.
  5. No unreplaced placeholders.
  6. The approval hook asks on Atlassian write tools and not on reads.
  7. Helper copies in skills/po/helpers/ match agents/ exactly (used by tools without subagents).
  8. Every ${CLAUDE_PLUGIN_ROOT}/... path named in a skill or agent exists.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "scrumscribe"
READ_ONLY_TOOLS = {"Read", "Grep", "Glob", "Skill"}
SECRET_PATTERNS = [
    r"ghp_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}", r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}", r"xox[baprs]-[A-Za-z0-9-]{10,}", r"ATATT[A-Za-z0-9_\-]{20,}",
]
PLACEHOLDER = "__GH_" + "OWNER__"  # split so a find-and-replace never edits this check
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".html", ".css", ".js", ".svg", ".txt"}
errors = []

def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    return fields

files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]

for p in files:
    if p.suffix == ".json":
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p.relative_to(ROOT)}: invalid JSON ({e})")

skills = list((PLUGIN / "skills").glob("*/SKILL.md"))
agents = list((PLUGIN / "agents").glob("*.md"))
if not skills or not agents:
    errors.append("no skills or agents found")
for p in skills + agents:
    fm = frontmatter(p)
    if not fm or not fm.get("name") or not fm.get("description"):
        errors.append(f"{p.relative_to(ROOT)}: missing name or description in frontmatter")

for p in agents:
    fm = frontmatter(p) or {}
    tools = {t.strip() for t in fm.get("tools", "").split(",") if t.strip()}
    if not tools:
        errors.append(f"{p.relative_to(ROOT)}: agent must list its tools explicitly")
    elif not tools <= READ_ONLY_TOOLS:
        errors.append(f"{p.relative_to(ROOT)}: non-read-only tools {sorted(tools - READ_ONLY_TOOLS)}")

for p in files:
    if p.suffix in TEXT_SUFFIXES and p.name != "validate.py":
        text = p.read_text(encoding="utf-8", errors="ignore")
        for pat in SECRET_PATTERNS:
            if re.search(pat, text):
                errors.append(f"{p.relative_to(ROOT)}: looks like a secret ({pat})")
        if PLACEHOLDER in text:
            errors.append(f"{p.relative_to(ROOT)}: unreplaced {PLACEHOLDER} placeholder")

# 6. Hook matcher behaviour (Claude Code tests matchers as unanchored JavaScript regexes;
#    Python's re behaves the same for this pattern).
hook = json.loads((PLUGIN / "hooks" / "hooks.json").read_text(encoding="utf-8"))
matcher = re.compile(hook["hooks"]["PreToolUse"][0]["matcher"])
must_ask = ["mcp__atlassian__createJiraIssue", "mcp__plugin_atlassian_atlassian__editJiraIssue",
            "mcp__atlassian__executeWrite", "mcp__atlassian__executeDestructive", "mcp__atlassian__manageJiraSprint",
            "mcp__atlassian__enableConfluencePublicLink", "mcp__claude_ai_Atlassian__setConfluenceContentStatus",
            "mcp__atlassian__transitionJiraIssue"]
must_pass = ["mcp__atlassian__getJiraIssue", "mcp__atlassian__searchJiraIssuesUsingJql", "mcp__atlassian__lookupJiraAccountId",
             "mcp__atlassian__getAccessibleAtlassianResources", "mcp__atlassian__executeRead", "mcp__atlassian__atlassianUserInfo",
             "mcp__atlassian__fetch", "mcp__github__create_issue", "Write"]
for name in must_ask:
    if not matcher.search(name):
        errors.append(f"hook does not ask on write tool {name}")
for name in must_pass:
    if matcher.search(name):
        errors.append(f"hook asks on read or unrelated tool {name}")

# 7. Helper copies stay in sync with agents/.
helpers_dir = PLUGIN / "skills" / "po" / "helpers"
for p in agents:
    copy = helpers_dir / p.name
    if not copy.exists() or copy.read_text(encoding="utf-8") != p.read_text(encoding="utf-8"):
        errors.append(f"skills/po/helpers/{p.name} is missing or differs from agents/{p.name}")

# 8. Plugin paths named in skills and agents exist.
for p in list((PLUGIN / "skills").rglob("*.md")) + agents:
    for ref in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./<>-]+)", p.read_text(encoding="utf-8")):
        ref = ref.rstrip(".")
        if "<" in ref:
            continue
        if not (PLUGIN / ref).exists():
            errors.append(f"{p.relative_to(ROOT)}: path not found: {ref}")

try:
    import yaml  # optional
    for p in files:
        if p.suffix in {".yml", ".yaml"}:
            yaml.safe_load(p.read_text(encoding="utf-8"))
except ImportError:
    pass
except Exception as e:
    errors.append(f"YAML error: {e}")

print(f"Checked {len(skills)} skills, {len(agents)} agents, {len(files)} files.")
if errors:
    print("\n".join("FAIL  " + e for e in errors))
    sys.exit(1)
print("All checks passed.")
