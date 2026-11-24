---
name: setup
description: Create or update the team charter (.scrumscribe/charter.yaml) and team file (.scrumscribe/team.yaml) that tailor ScrumScribe to any organization, from a short interview, existing Confluence pages, or a plain-English description of how the team works.
argument-hint: "[optional: describe how your team works, e.g. 'two-week Scrum, PRD and ADRs, no BDD']"
disable-model-invocation: true
---

# ScrumScribe setup

This skill tailors the harness to one team. It writes two files the team owns:

- `.scrumscribe/charter.yaml`: how the team works.
- `.scrumscribe/team.yaml`: who is on the team, their skills, what they own, their capacity.

Templates live in this plugin at `${CLAUDE_PLUGIN_ROOT}/templates/charter.yaml` and `${CLAUDE_PLUGIN_ROOT}/templates/team.yaml`. Copy them, then fill them in.

## Three ways in. Use whichever the person offers.

1. **Plain English.** If the person describes their process ("we run two-week Scrum, epics and stories, we want a PRD and ADRs"), map it onto the charter fields. Show the resulting YAML and ask for a yes before saving.
2. **Read what exists.** If an Atlassian connection is available, read the team's Confluence space for a team charter, Definition of Ready, Definition of Done and working agreements, and the Jira project for issue types and required fields. Propose values with source links. Ask only about what you could not find.
3. **Short interview.** Ask the questions below, at most five per round, multiple choice where possible.

## Interview questions

Round 1: process
1. Which way of working fits best? Scrum / Kanban / Shape Up / mixed (describe)
2. How long is a sprint or cycle? 1 week / 2 weeks / 6 weeks / no fixed length
3. Which ticket levels do you use? Epic > Story > Sub-task / Epic > Story / Story only / other
4. What does a story need before it enters a sprint (Definition of Ready)? Point me to the page, or I'll suggest a starting list.
5. What makes work "done" (Definition of Done)? Point me to the page, or I'll suggest a starting list.

Round 2: documents and style
1. Which documents do you want produced? Offer the catalogue in `${CLAUDE_PLUGIN_ROOT}/skills/agile-intake/references/document-catalogue.md` and let them pick.
2. Do you write acceptance criteria as Given/When/Then, as checklists, or both?
3. Writing style: plain technical English (STE-style), ADHD-friendly layout, both, or your own guide?
4. Which Jira project key and Confluence space should I use?
5. Who gives the second approval before anything is posted? Scrum Master (default) / QA lead / tech lead / delivery lead / nobody (PO approval only)

Round 3: team (writes team.yaml)
1. Which pods or squads exist, and what does each own?
2. For each person: a name or handle, work skills with a 1 to 3 level, what they are accountable for, and rough capacity.
3. Who reviews what (for example: tech lead reviews ADRs, QA lead reviews test plans)?

## Rules

- Keep `team.yaml` to minimal work data: a name or handle, role, skills, ownership, capacity. No contact details, health or performance ratings.
- Never store passwords, keys or tokens in either file. Connections are configured in Claude Code, not here.
- Unknown values stay as `null` with a `# TODO` comment. Do not invent them.
- After saving, show a five-line summary of the charter and suggest running `/scrumscribe:po`.
- Suggest adding `.scrumscribe/work/` to the project's `.gitignore`: session work will hold internal Jira and Confluence content. The charter and team file can be committed if the team wants.
