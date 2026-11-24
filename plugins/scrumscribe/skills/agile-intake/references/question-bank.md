# Question bank

Use the ids in the first column in `gaps.md` and in the charter's `required_areas`. Check the listed sources first. Ask the PO only what the sources do not answer. Rephrase questions in the PO's own words and domain.

| id | Area | Example questions | Check first |
|---|---|---|---|
| goal | Goal | What outcome proves this worked? Which Product Goal does it serve? What happens if we do nothing? | Confluence roadmap, epic description |
| users | Users | Who uses it? How often? What do they do today instead? | Confluence personas, support tickets, analytics docs |
| scope | Scope | What is in? What is explicitly out (no-gos)? What could turn into a rabbit hole? | Existing epic, similar past epics |
| appetite | Appetite | How much time is this worth: days, one sprint, a quarter? What is the deadline, and is it real? | Roadmap dates, release calendar |
| behaviour | Behaviour | What is the main path? What other paths exist? Which business rules apply? What data does it touch? | Repo, existing stories, process docs |
| quality | Quality (NFRs) | Targets for speed, availability, security, accessibility, and the other characteristics that matter here | Confluence standards pages, SLAs |
| dependencies | Dependencies | Which teams, systems, vendors or approvals does it need? | Repo, Jira links, architecture pages |
| data-compliance | Data and compliance | Does it handle personal data? Audit, retention or regulatory needs? | Confluence policy pages |
| ready-done | Ready and Done | Does the team's Definition of Ready and Done cover this, or does it need extra criteria? | Charter, Confluence |
| success-metrics | Success metrics | Which number should move, by how much, and by when? How is it measured today? | Analytics docs, OKRs |
| rollout | Rollout | Feature flag, pilot group, migration, training, support plan? | Release pages, runbooks |
| ownership | Ownership | Which pod owns it? Who reviews design, tests and docs? | team.yaml, Confluence team pages |

## Splitting prompts (use during Behaviour)

Based on Mike Cohn's SPIDR approach:

- **Spike:** Is there something we must learn before we can size this?
- **Paths:** What is the simplest path through this? What are the other paths?
- **Interfaces:** Does it need every channel or device on day one?
- **Data:** Can the first version support only the common data types?
- **Rules:** Can some business rules wait for a later story?

## Asking well

- At most five questions per round.
- Multiple choice where possible, always with "other".
- One line on why each question matters.
- Never ask what you already found. Show it and ask for confirmation.
