---
name: ste-writing
description: Write, rewrite, or check technical documentation in ASD-STE100 Simplified Technical English (STE) - the controlled-language standard that makes procedures and descriptions clear and unambiguous for non-native English readers and machine translation. Use this skill whenever the user asks to write in STE or Simplified Technical English, convert or "STE-ify" existing text, audit a manual, procedure, or work instruction for STE compliance, apply approved-word / one-meaning / short-sentence / active-voice rules, or produce aircraft, defense, or general maintenance instructions. Also use it whenever the user mentions ASD-STE100, STE100, controlled English, or simplified English for technical writing.
---

# ASD-STE100 Simplified Technical English (STE)

> **Note on this document.** The instructions in this skill obey the STE
> writing rules. The sentences are short, active, and direct. The prose is
> not machine-checked against the approved dictionary, because the full
> dictionary is not in this skill (see "Limits" below).

## 1. What this skill does

This skill helps you to do three tasks:

- Write technical documentation in STE.
- Change existing text into STE.
- Check text for STE errors.

STE is a controlled language. STE makes technical text easy to read. Readers
who do not know English well can understand STE text. Machine translators can
process STE text correctly.

## 2. When to use STE

Use STE for procedures and descriptions. For example:

- maintenance instructions
- assembly and installation steps
- warnings, cautions, and notes
- equipment and system descriptions

Do not use STE for these text types:

- marketing text
- legal text
- narrative or literary prose

STE cannot be the only standard. Use STE together with a style guide and an
approved terminology list.

## 3. The two parts of STE

STE has two parts:

1. **The writing rules.** There are 53 rules in 9 groups.
2. **The dictionary.** There are approximately 900 approved words.

Read the correct reference file for the task:

| Task | Read this file |
|------|----------------|
| Apply the rules | `references/writing-rules.md` |
| Replace unapproved words | `references/dictionary.md` |
| Remove AI-slop words | `references/slop-words.md` |
| See before/after text | `references/examples.md` |
| Check your output | `references/checklist.md` |
| Confirm a rule or a word in the source | `references/official-source.md` |

## 4. The core rules

Obey these rules first. They give the largest effect on readability. For all
53 rules, read `references/writing-rules.md`.

### Words

- Use each approved word as one part of speech only.
- Use each approved word with one approved meaning only.
- Do not make a multi-word noun of more than 3 words.
- Keep technical nouns and technical verbs. The dictionary does not list them.

### Verbs

- Use only these verb forms: the infinitive, the imperative, the simple
  present, the simple past, the simple future, and the past participle.
- Use the past participle as an adjective only.
- Use the active voice.
- In descriptions, use the passive voice only if the agent is not known.
- Do not use the "-ing" form as a verb. Use it as a noun or a modifier only.
- Do not make complex verbs with auxiliary verbs.

### Sentences

- Write no more than 20 words in a procedure sentence.
- Write no more than 25 words in a descriptive sentence.
- Write one instruction in each sentence.
- Do not remove the subject, the verb, or the article to make a sentence
  short.

### Paragraphs

- Write one topic in each paragraph.
- Write no more than 6 sentences in a procedure paragraph.
- Use a vertical list for complex information.

### Safety

- Put the warning or the caution before the step, not after it.
- Start a safety instruction with a command or a condition.

## 5. The two modes

Select the mode before you write.

- **Strict mode.** Use it for procedures, runbooks, safety text, and error
  messages. Apply all rules and both length limits. Use only approved words.
- **Flavored mode.** Use it for general prose: README files, PR descriptions,
  and documentation. Apply the sentence rules, the paragraph rules, the active
  voice, and the slop-word replacements. Do not enforce the full dictionary.
  The text keeps enough range to read naturally.

Strict mode is the default. Use flavored mode when the user asks for general
prose, or when full dictionary control makes the text robotic.

In both modes, write only the requested text. Do not add a preamble, a
summary, or closing remarks.

## 6. The linter

The file `scripts/ste-lint.py` checks the mechanical subset of the rules. It
needs only Python 3. It reports violations per 100 words. A lower score is
better.

```
python3 scripts/ste-lint.py FILE...
```

Use the linter in two cases:

1. Before you deliver text, lint it. Correct what the linter finds.
2. When you convert text, lint the source and the result. Report both scores.
   The delta shows the effect.

The linter cannot check the judgment rules. It does not know the approved
words. Your review stays necessary.

## 7. Workflow

Do these steps in sequence.

1. Identify the text type. Decide if the text is a procedure or a description.
2. Select the mode: strict or flavored (see Section 5).
3. Read the reference files that apply to the task.
4. Write or change the text. Obey the core rules.
5. In strict mode, find each unapproved word. Replace it with an approved
   word from `references/dictionary.md`.
6. In both modes, replace or delete the words in `references/slop-words.md`.
7. Check the text against `references/checklist.md`.
8. Lint the text with `scripts/ste-lint.py` (see Section 6). Correct the
   findings.
9. If you are not sure about a word or a rule, consult the official standard.
   Read `references/official-source.md`.
10. If the user wants a comparison, show the Non-STE text and the STE text
    together, with the two linter scores.

## 8. When you are not sure

The paraphrased guidance in this skill is enough for most tasks. But it is not
the authority. The official ASD-STE100 document is the authority.

Consult the official document in these cases:

- You are not sure if a word is approved.
- You are not sure of the approved meaning of a word.
- You are not sure how a rule applies to a difficult sentence.
- The user asks for the exact rule wording or the official examples.

To consult the document:

1. Read `references/official-source.md`. It has the rule map.
2. Find the correct section and rule number.
3. Look for the official copy at `references/official/`. Read the Markdown
   version (`ASD-STE100_ISSUE9.md`) first if the user added one. It is easier
   to search and to read than the PDF. If only the PDF is present, read the
   PDF. If neither is present, give the user the exact section and rule
   number. Point the user to https://asd-ste100.org.
4. Do not guess. If you cannot confirm, tell the user.

## 9. Limits

Obey these limits. They keep the skill correct and legal.

- This skill does not contain the full ASD-STE100 document.
- ASD owns the copyright and the trademark. The full standard is free.
- Get the official copy from https://asd-ste100.org.
- The word list in this skill is a small example set. It is not complete and
  it is not authoritative.
- A software checker cannot think for you. Always use your judgment.
- The current issue is Issue 9 (January 2025). Rule numbers can change between
  issues. Use the official document as the reference for exact rule numbers.
