# Security policy

ScrumScribe can write to Jira and Confluence through your own Atlassian connection. Its safety rests on three things: read-only helper agents (enforced by their tool lists), a hook that asks before any Atlassian MCP tool that is not a known read (enforced), and two recorded human approvals (followed by the orchestrator, not technically enforced).

## Reporting a problem

If you find a way for the harness to write, assign, delete or leak data without a human approval, please report it privately through [GitHub's private vulnerability reporting](../../security/advisories/new) instead of opening a public issue.

Please include the Claude Code version, the plugin version, and the steps that reproduce it.

## What this project never needs

- Your Atlassian, GitHub or model API credentials in any file. Connections are configured in Claude Code.
- Personal data about team members beyond minimal work data. `team.yaml` holds a name or handle, skills, ownership and capacity.
