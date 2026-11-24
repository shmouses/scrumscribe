# Walkthrough: "Finance wants invoice exports"

An illustrative, hand-written example of what each stage is designed to produce. It is **not output from a real run**. The company, people and numbers are invented.

**Team:** Larkspur Travel, a booking platform. Two-week Scrum. Jira project `LARK`, Confluence space `PROD`.
**PO's opening message:** "Finance keeps asking us to pull invoices by hand. Can we let them export them?"

---

## Stage 1 of 5: Discover

`context.md` (excerpt)

| Fact | Source |
|---|---|
| Invoices are stored per booking; about 4,000 per month | Confluence: *Billing data model* |
| A 2025 epic `LARK-812` "Invoice PDF download" shipped single-invoice PDFs | Jira `LARK-812` |
| Finance role exists in the permission model | Repo: `auth/roles.py` |
| No Definition of Done page found in `PROD` | Confluence search |

## Stage 2 of 5: Gap check

| Area | Status | Note |
|---|---|---|
| Goal | Inferred (medium) | Save Finance manual work; no metric stated |
| Users | Known | Finance role, from repo |
| Scope | Missing | Which invoices? Which format? |
| Appetite | Missing | |
| Behaviour | Inferred (low) | Probably filter by month |
| Quality | Missing | Volume known (4,000/month), speed target unknown |
| Data and compliance | Inferred (high) | Invoices contain customer names and addresses |
| Definition of Done | Missing | No page found |

## Stage 3 of 5: Questions (round 1, five questions)

1. **Which format does Finance need?** CSV / Excel / PDF bundle / other. *Why: it decides the story split.*
2. **How much time is this worth?** A few days / one sprint / more. *Why: this sets the scope limit.*
3. **What range should an export cover?** One month / any date range / other. *Why: big ranges change the speed target.*
4. **What does success look like?** For example "Finance stops asking engineers for exports". *Why: it gives us a metric.*
5. **Does your team have a Definition of Done page?** Link / no, suggest one. *Why: every story is checked against it.*

**PO answers:** CSV. One sprint. One month first, any range later. "Zero manual export requests to engineering." No DoD page; suggest one.

**PO decision:** "Good enough to draft. Keep the Definition of Done as an open item." (recorded in `answers.md`)

## Stage 4 of 5: Draft

**Scope Guard verdict: Fits**, after one split by **Data** (one month first, custom ranges deferred) and one deferral (Excel format).

| Story | Outcome | Criteria |
|---|---|---|
| LARK-S1 Export one month of invoices as CSV | Finance can download a month of invoices in one file | 4 |
| LARK-S2 Restrict export to the Finance role | Only Finance can export invoice data | 3 |
| LARK-S3 Log every export | Finance managers can see who exported what and when | 3 |

Deferred: custom date ranges, Excel format. No-go: editing invoices from the export screen.

**NFR-1 Performance efficiency:** 95% of one-month exports finish in under 10 s for up to 5,000 invoices. Verified by a load test.

**Test designer:** one eval ticket for NFR-1 (trigger: NFR with a target). No integration ticket (single service).

**Red-team findings:** must fix: S1 did not say what happens when a month has zero invoices. Fixed: "then the file contains only the header row and a message says no invoices were found".

**Writer:** before "The export should be fast and secure." After "The export finishes in under 10 s for 95% of one-month requests. Only the Finance role can start it."

## Stage 5 of 5: Review and hand off

- **PO approval:** "Approved, go ahead." (recorded in `approvals.md`)
- **Owner suggestions:** S1 and S3 to the Billing pod (backend level 3, capacity 80%), S2 reviewed by the security champion. One capacity flag: the Billing pod has two other stories this sprint.
- **Second approval (Scrum Master):** "Approved, move S3 to next sprint." Owners changed as asked.
- **Posted:** epic `LARK-1040` and stories `LARK-1041` to `LARK-1044`, linked to a new Confluence page *Invoice CSV export: spec*. Each write would trigger the approval hook's confirmation.

**Done:** epic and 4 tickets posted. **Next:** draft a Definition of Done page with the team. **Blocked:** none.
