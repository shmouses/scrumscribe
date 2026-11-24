---
name: agile-intake
description: Method for gathering enough information to write well-structured agile requirements. Use when gap-checking a feature request against a question bank, turning PO answers into functional and non-functional requirements, or choosing which project documents a team needs.
---

# Agile Intake

Read what already exists first. Ask only for what is missing. Every requirement traces to a source.

## Known, Inferred, Missing

For each area in `${CLAUDE_PLUGIN_ROOT}/skills/agile-intake/references/question-bank.md`, mark one of:

| Mark | Meaning | Next step |
|---|---|---|
| Known | Found in a source or stated by the PO | Cite the source |
| Inferred | Likely, from indirect evidence | Ask the PO to confirm if it affects scope, cost or risk |
| Missing | No evidence | Ask the PO, or record as an open item |

Give each Inferred item a confidence: high, medium or low. Low confidence counts as Missing.

## Which areas are required

The charter's `required_areas` decides, using the question-bank ids. The default is `goal`, `users`, `scope` (including no-gos), `appetite`, `behaviour` and `ready-done`. The others (`quality`, `dependencies`, `data-compliance`, `success-metrics`, `rollout`, `ownership`) are asked when relevant.

## Functional requirement format

```markdown
### FR-<number>: <verb + object>
**Story:** As a <user>, I want <capability> so that <outcome>.
**Acceptance criteria**
1. Given <context>, when <action>, then <observable result>.
2. ...
**Source:** <PO answer date | Confluence link | Jira key>
**Notes:** <rules, data limits, open questions>
```

Keep 3 to 5 acceptance criteria per requirement. More than 5 usually means the story should be split (see the `scrumscribe:scope-rules` skill). If the charter sets `acceptance_criteria_style: checklist`, write the criteria as a numbered checklist of observable results instead of Given/When/Then.

## Non-functional requirement format

```markdown
### NFR-<number>: <characteristic>: <short name>
**Target:** <measurable value, with units and conditions>
**Verified by:** <test, monitor, review, or audit>
**Applies to:** <FR ids or "whole epic">
**Source:** <...>
```

An NFR without a measurable target is not finished. Turn it into a question for the PO. Use `${CLAUDE_PLUGIN_ROOT}/skills/agile-intake/references/nfr-iso25010.md` to walk the quality characteristics, and ask only about the ones that matter for this feature.

## Choosing documents

Offer the catalogue in `${CLAUDE_PLUGIN_ROOT}/skills/agile-intake/references/document-catalogue.md`. The charter's `docs_wanted` list is the team's choice. Scrum's three commitments (Product Goal, Sprint Goal, Definition of Done) are always assumed to exist; if they don't, flag it once.

## Traceability rule

Nothing appears in a requirement without a source. If a statement came from you, the model, mark it `Proposed` and ask the PO to accept or reject it.
