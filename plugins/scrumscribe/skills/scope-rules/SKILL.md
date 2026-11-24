---
name: scope-rules
description: Rules that keep ticket scope lean. Use when splitting requirements into stories, checking a set of stories against a time budget (appetite), or deciding what to cut, defer or turn into a spike.
---

# Scope rules

Fix the time, flex the scope. Cut before you add.

## 1. Start from the appetite

The appetite is how much time the work is worth, set before the solution is designed (an idea from Basecamp's *Shape Up*). Read it from `answers.md` or the charter's `appetite_default`. If there is none, stop and ask the PO.

## 2. Name rabbit holes and no-gos

Every epic lists:
- **Rabbit holes:** parts that could eat weeks (unknown tech, unclear rules, tangled dependencies), and how each is patched or avoided.
- **No-gos:** what is explicitly out of scope.

## 3. Split by user value, one axis at a time

Use SPIDR (Mike Cohn): spikes, paths, interfaces, data, rules.

- Split on one axis, then re-check the smaller stories.
- Happy path first. Edge paths, extra channels, rare data and extra rules come later.
- Never split by technical layer ("backend story", "frontend story"). Each story must give a user something they can see or use.

## 4. Apply the lazy-senior test to every story

Borrowed from the Ponytail skill's principle (the best code is the code never written), applied to tickets:

- Is this story needed to meet the epic's acceptance criteria? If not, cut it or move it to a later epic.
- Does something that already exists cover it? Reuse beats rebuild.
- Is this a "while we're here" addition? Move it out.

## 5. Check limits

Defaults, overridable in the charter under `limits`:

| Check | Default limit | If exceeded |
|---|---|---|
| Stories per epic | 8 | PO confirms or the epic splits |
| Acceptance criteria per story | 5 | Split the story |
| Story size | Fits one sprint (Kanban: the team's usual cycle time) | Split, or turn the unknown part into a spike |
| NFRs without a measurable target | 0 | Back to the PO as a question |

## 6. Verdict

Return one of:

- **Fits:** the stories fit the appetite. List them.
- **Does not fit:** give the PO up to three options, each with what is gained and lost: split into two epics, cut named stories, defer named stories, or raise the appetite.

Never silently drop a requirement. Every cut or deferral is listed so the PO can see it.
