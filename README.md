# Skills

This repository contains skills for Claude Code. Each directory is one skill.
Each skill has a `SKILL.md` file. Claude reads this file and obeys the
instructions in it.

## ste-writing

This skill writes and checks text in ASD-STE100 Simplified Technical English
(STE). STE is a controlled language for technical documentation. It uses
short sentences, the active voice, and approved words with one meaning each.

The skill has these parts:

- the writing rules and a word list (`references/`)
- a linter for the mechanical rules (`scripts/ste-lint.py`)
- the commands `/ste` and `/ste-audit`

The full standard is not in this repository. You can get it free of charge
from https://asd-ste100.org.

## code-analysis-personas

This skill reviews code in the voice of a famous programmer. Each persona
finds different problems. For example, Ken Thompson looks for code to delete,
and John Carmack looks at performance.

The personas are Ken Thompson, Dennis Ritchie, Brian Kernighan, John McCarthy,
John Carmack, Steve Wozniak, Linus Torvalds, Guido van Rossum, and David
Malan.

- For a review from one persona, use `/as-<name>`, for example `/as-linus`.
- For a review from more than one persona, use `/multi-review`.

## simplified-syntax

This skill writes text in Simplified Syntax. Simplified Syntax is a
telegraphic style. It removes articles, prepositions, connectors, verb
tenses, and periods. It joins compound concepts into one word.

The skill does not change code, file paths, configuration, or quotes.

## term-capture

This skill opens a new terminal window with an interactive zsh. You type the
commands in the window. Claude reads the output when you close the window.
Use this skill for commands that need sudo or other input from you.

The skill has these properties:

- Claude can put a command in the input line. The command does not start
  until you push Enter.
- Claude gets a notification when you close the window.
- The result shows each command, its output, and its exit code.
- A progress bar shows only its last state.
- Your zsh configuration does not change.

The skill needs these programs: zsh, xdg-terminal-exec, script (util-linux),
and python-pyte.

## Installation

To install one skill, copy its directory to `~/.claude/skills/`.

To make a `.skill` file for each skill, run `package.sh`. The script replaces
the old `.skill` files. Git ignores the `.skill` files.

## License

MIT. Refer to `LICENSE`.

## Trademarks

ASD-STE100 is a trademark of ASD (AeroSpace, Security and Defence Industries
Association of Europe). This project is unofficial. ASD does not endorse it
and is not affiliated with it. The MIT license covers the text and code of
this project only. It does not cover the ASD-STE100 specification.

The persona names in `code-analysis-personas` refer to real people. These
people do not endorse this project and are not affiliated with it. The purpose
of the skill is to change the behavior of the LLM in a useful way. The reviews are
not the words or the opinions of these people. Consider the descriptions of
these people to be caricatures.

## Credits

The STE linter (`ste-writing/scripts/ste-lint.py`) is vendored from
[woosal1337/blog](https://github.com/woosal1337/blog) by Ege Çelebi
(woosal1337). Many thanks to woosal1337 for sharing this tool.
