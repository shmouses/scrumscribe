# ScrumScribe (plugin)

ScrumScribe is a human-in-the-loop harness for product teams. A Product Owner describes what they need in plain English. The plugin reads Jira, Confluence and the repo, asks only for missing information, drafts lean user stories with testable acceptance criteria plus test and eval tickets, and posts them to Jira and Confluence only after the Product Owner and a second approver (the Scrum Master by default) approve.

## Use

```text
/plugin marketplace add shmouses/scrumscribe
/plugin install scrumscribe@scrumscribe
```

1. `/scrumscribe:setup` tailors it to your team (`.scrumscribe/charter.yaml`, `.scrumscribe/team.yaml`).
2. `/scrumscribe:po <what you need>` runs a session.

Posting needs an Atlassian MCP connection (for example `/plugin install atlassian@claude-plugins-official`, then sign in through `/mcp`). Without it, everything is drafted to `.scrumscribe/work/`.

Helper agents are read-only. A hook asks for confirmation before any Atlassian tool that is not a known read.

Full documentation, diagrams and a worked example: see the repository README.
