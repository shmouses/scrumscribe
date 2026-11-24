---
name: test-design
description: Decide when a feature needs separate test or evaluation tickets and write them. Use when adding acceptance tests as examples, planning integration tests, or defining evaluation sets and pass thresholds for AI-driven features.
---

# Test design

Design tests when the story is written, as concrete examples. Create a separate ticket only when a trigger applies.

## Triggers

| Trigger | Ticket | What it holds |
|---|---|---|
| Normal story | None | Given/When/Then examples in the story; tests are part of the Definition of Done |
| Epic crosses services or teams | Integration test ticket | End-to-end paths to prove, test data, environments |
| NFR with a measurable target | Eval ticket | Target, measurement method, pass threshold, where results are recorded |
| Feature driven by an AI model | Eval ticket | Eval set (size and source), metrics, pass threshold, who signs off, how often it re-runs |
| Risky release | QA validation or UAT ticket | What real users check before go-live, and the go or no-go owner |

## Example mapping

For each business rule, write two or three concrete examples: one normal, one boundary, one failure. Each example becomes an acceptance test. If you cannot write an example, the rule is not understood yet: send it back as a question.

## Eval tickets for AI features

An eval ticket must state:
1. What is being judged (task and output).
2. The eval set: where examples come from, how many, who labels them.
3. Metrics, each with a pass threshold.
4. A baseline to beat, if one exists.
5. The re-run trigger (model change, prompt change, data change).

## Optional companion tools

- **BMAD Method's Test Architect (TEA) module** for risk-based test strategy and release gates.
- **A strict code review step** (for example a "thermonuclear" review prompt, an idea from the Thermos plugin for Cursor) once code exists. Add it to the Definition of Done for high-risk tickets. It reviews code; it does not design tests.

These are optional. This skill works without them.
