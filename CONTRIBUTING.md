# Contributing

Thanks for helping. This project is small on purpose, so the bar for adding things is "does it make tickets clearer or safer without adding moving parts?"

## Ways to help

- **Fill in the [feedback questionnaire](../../issues/new?template=feedback_survey.yml)** (about 3 minutes). It covers how your team works today and how you would change the workflow.
- **Try it on a real backlog** and open an issue with what worked and what didn't. This is the most useful thing right now.
- **Recommend a harness** that does this better, or part of it, with the [recommendation template](../../issues/new?template=harness_recommendation.yml).
- **Improve a skill or agent prompt.** Keep the plain-English style: short sentences, one idea each.
- **Add a charter preset** for a way of working we don't cover yet.

## Ground rules for changes

1. Helpers stay read-only. Never add a write tool, MCP server or shell access to an agent in `agents/`.
2. No secrets or personal data in any file, example or test.
3. Examples use invented companies and people.
4. Credit borrowed ideas in the README. Don't copy other projects' code or text without a compatible license and attribution.
5. Run the checks before opening a pull request:

```bash
python3 scripts/validate.py
claude plugin validate .
claude plugin validate ./plugins/scrumscribe
```

6. Add a line to `CHANGELOG.md` under an `Unreleased` heading.

## Development

Load the plugin from your clone without installing it:

```bash
claude --plugin-dir ./plugins/scrumscribe
```

Then run `/scrumscribe:setup` in a scratch project.
