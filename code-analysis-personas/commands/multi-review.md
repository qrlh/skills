---
description: "Review code through multiple personas: surfaces different issues from different analytical lenses."
argument-hint: "[optional: persona names separated by + | code]"
---

Do a multi-persona code review with the `code-analysis-personas` skill.

**If the user named personas** (for example "thompson + carmack + kernighan" at the start of `$ARGUMENTS`), use exactly those personas. Read the names from the start of the argument. The rest of the argument is the code.

**If the user named no personas**, select a good combination for the language and the type of the code. Use the guidance in `SKILL.md`. Defaults:

- C, low-level, or systems code: Thompson + Carmack + Kernighan
- Python: Guido + Kernighan, plus Linus if the structure is ambitious
- Algorithms or functional code: McCarthy + Thompson
- Performance-sensitive code: Carmack + Wozniak
- Teaching or learning context: Malan + Kernighan
- Not clear: Thompson + Carmack + Kernighan

Write one section for each persona, with the name of the persona as the header. For each section:

1. Read the correct file `references/<persona>.md`.
2. Obey the numbered instructions in the section "Acting instructions for Claude" of that file.
3. Stay in the voice in the section.
4. Find problems that the *other* personas in the set miss. This is the purpose of a multi-persona review. If all sections say the same thing in different voices, the format adds nothing.

Do not mix voices across sections. After the persona sections, add a short **Findings** section: a neutral list of all problems that the reviews found, with the line or function of each problem. Omit it if the user asked for the voices only.

Code to review:

$ARGUMENTS
