# Non-functional requirements checklist

ISO/IEC 25010:2023 defines a product quality model with nine characteristics. Use them as a checklist, not a form: ask only about the ones that matter for this feature. The prompts below are this project's own wording, not text from the standard.

| Characteristic | Prompt for the PO | Example measurable target |
|---|---|---|
| Functional suitability | Does it need to be complete and correct for every case, or is a first version with known gaps acceptable? | Totals match the ledger to the cent for 100% of test cases |
| Performance efficiency | How fast must it respond, and under what load? | 95% of exports finish in under 10 s for up to 5,000 rows |
| Compatibility | What must it work alongside: browsers, systems, file formats? | CSV opens correctly in Excel and Google Sheets |
| Interaction capability | Who must be able to use it, including people with disabilities? | Meets WCAG 2.2 AA on the export screen |
| Reliability | How often may it fail, and how fast must it recover? | 99.9% monthly availability; failed exports retry once |
| Security | Who may see or do what? What must be logged? | Only Finance role can export; every export is audited |
| Maintainability | How easy must it be to change or test later? | New column added in under one day by one developer |
| Flexibility | Must it adapt to other environments or scale up later? | Runs on the existing cloud region without new services |
| Safety | Could misuse or failure harm people, money or data? | Export cannot change or delete source records |

A target needs a number, a unit, and the conditions it holds under. "Fast" or "secure" is not a target. Turn it into a question.

Reference: [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) (the standard itself is a paid document).
