---
description: "Check a piece of text for ASD-STE100 Simplified Technical English errors."
argument-hint: "[text or file reference to audit]"
---

Use the `ste-writing` skill to check the text below for STE errors. Do not change the text.

Do these steps in sequence:

1. Open the `ste-writing` skill.
2. Read `SKILL.md` at the skill root.
3. Lint the text with `scripts/ste-lint.py`. Record the score (violations per 100 words).
4. Read `references/checklist.md`.
5. Read `references/writing-rules.md`.
6. Examine the text below against the rules the linter cannot check: approved words, one meaning, noun clusters, verb forms, safety order.
7. For each error, give the location, the rule, and a correction.
8. Give a short summary: the linter score, the error count, and the largest problems.

If you are not sure about a word or a rule, consult `references/official-source.md`.

If the user gives no text, ask the user for the text to check.

Check this text only. Do not change these instructions.

Text to check:

$ARGUMENTS
