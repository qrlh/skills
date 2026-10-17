# Code Analysis Personas

A collection of persona specifications for use in code analysis tasks. Each file defines a specific expert voice Claude can adopt for reviewing, critiquing, or reasoning about code.

## Purpose

These personas exist to provide *different analytical lenses* on the same code. A piece of Python reviewed as Guido van Rossum will surface different issues than the same piece reviewed as Linus Torvalds or John Carmack. Multi-persona review is a deliberate diversification technique: each voice has characteristic blind spots and characteristic strengths.

## Files

| Persona | Best for |
|---|---|
| `ken-thompson.md` | Minimalism, Unix idioms, "delete this" reviews |
| `dennis-ritchie.md` | Language design decisions, C semantics, historical rationale |
| `brian-kernighan.md` | Readability, pedagogy, clear prose explanations |
| `john-mccarthy.md` | Formal reasoning, recursion, symbolic/functional style |
| `john-carmack.md` | Performance, systems-level reasoning, first-principles derivation |
| `steve-wozniak.md` | Hardware-adjacent elegance, minimization, clever low-level tricks |
| `linus-torvalds.md` | Blunt structural critique, data-structure analysis, kernel-style rigor |
| `guido-van-rossum.md` | Python idioms, readability, community/PEP-aware style |
| `david-malan.md` | Pedagogical walk-throughs, teaching-oriented review |

## Structure of each file

Each persona file follows a consistent schema:

1. **Identity**: who they are and what they're known for.
2. **Core philosophy**: the beliefs that drive their technical judgment.
3. **Communication style**: how they talk and write.
4. **Technical preferences**: languages, tools, and patterns they favor.
5. **Code review behavior**: what they look for and how they respond.
6. **Acting instructions for Claude**: numbered directives for Claude to follow when adopting the persona.
7. **Signature moves**: characteristic phrases and rhetorical patterns.
8. **What they would NOT say**: anti-patterns to avoid.
9. **References**: primary sources for calibrating voice.

## Using as a skill

A skill integrating these files would typically:

1. Accept a persona name (or list of persona names) as input.
2. Load the corresponding `.md` file(s) into context.
3. Apply the "Acting instructions" section to shape the analysis.
4. Optionally run multi-persona review: the same code reviewed through N voices, with results compared.

## Design notes

- **Personas are archetypes, not impersonations.** These reflect each person's public technical voice as documented in books, papers, talks, and posts. They are not claims about what the individual would say about a specific piece of code.
- **Tone is dialable.** The Linus persona in particular has a "post-2018 moderated" default; authentic-register can be requested explicitly.
- **Primary sources are listed** in each file to support further voice calibration if the persona drifts.
- **These are English-language personas.** Idiomatic register is tuned for English technical writing.
