# Changelog

All notable changes to this project are listed here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Feedback questionnaire (GitHub issue form) linked from the README and the site.

### Changed
- README and site describe ScrumScribe as a simple, generic harness built on existing open-source harnesses and methods, and note that it is a personal side project.

## [0.2.0] - 2026-11-23

### Added
- Guide for using ScrumScribe in Cursor, Codex, Gemini CLI, GitHub Copilot and other Agent Skills tools (README and site).
- Single-agent mode: tools without subagents follow `skills/po/helpers/` one helper at a time.
- Portable paths: skills explain how to resolve `${CLAUDE_PLUGIN_ROOT}` when a tool doesn't fill it in.
- Validator checks: helper copies match `agents/`, and every plugin path named in a skill or agent exists.

### Changed
- Templates moved into skill folders (`skills/setup/templates/`, `skills/po/templates/`) so they travel with the skills.

### Builder self-check
- `claude plugin validate` passes; `scripts/validate.py` passes (8 checks).
- Copied the skills into a Cursor-style `.cursor/skills/` folder: every relative path from `po/SKILL.md` resolved.
- Not yet tested in a live Cursor, Codex or Gemini CLI session.

## [0.1.0] - 2026-11-23

### Added
- `/scrumscribe:po` orchestrator skill with five stages: discover, gap check, ask, draft, hand off.
- `/scrumscribe:setup` skill to build `.scrumscribe/charter.yaml` and `.scrumscribe/team.yaml`.
- Skills: `agile-intake` (question bank, FR and NFR formats, document catalogue), `scope-guard`, `test-design`, `ticket-writing`.
- Six read-only helper agents: intake analyst, scope guard, test designer, red-team reviewer, writer, owner suggester.
- PreToolUse approval hook that asks before any Atlassian MCP tool that is not a known read (fails closed).
- Templates: charter, team file, story, spike, NFR, test, eval, handoff.
- Worked example, documentation site, validation script and CI.

### Builder self-check
- `claude plugin validate` passes for the marketplace and the plugin (Claude Code 2.1.331).
- Hook matcher tested (also in `scripts/validate.py`): asks on 8 Atlassian write tools including `executeWrite` and `executeDestructive`; passes 7 read tools and 2 non-Atlassian tools.
- Hook output parsed as valid JSON with `permissionDecision: ask`.
- Independent review 01: Pass with fixes. All must-fix and should-fix items addressed before first publish.
- Not yet run end to end on a real team's Jira project.
