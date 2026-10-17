---
name: simplified-syntax
description: Rewrite prose in Simplified Syntax, a terse, telegraphic register that drops articles, prepositions, connectors, verb tense, and periods, joins compound concepts into single words, and follows action-object-context ordering. Use whenever the user asks to write, rewrite, compress, or "simplify-syntax" any text, or asks for output in this style by name. Also apply when the user writes to you in this register and wants replies matched to it. Do NOT apply to code, file paths, config, or verbatim quotes.
---
# Simplified Syntax Style Specification 0.4

## Rule 1: No Articles

Remove all article: "a," "an," "the";

- goodexample: "Rust give strong memorysafety"
- badexample: "Rust gives a strong memory safety guarantee"

## Rule 2: No Preposition
<!-- TODO: Some preposition contradict example, rework, expose potential use; Relationship expression need (better more) option -->

Remove all preposition: "to," "from," "with," "for," "into," "via," "about," "of," "in," "on," "at," "by," "between," "through," "against," "over," "under";

- goodexample: "I go store, buy bread"
- badexample: "I go to the store to buy some bread"

## Rule 3: No Connectors

Remove all connector: "and," "but," "or," "yet," "so," "however," "therefore," "although," "because," "while," "whereas";

- goodexample: "Rust fast safe concurrent"
- badexample: "Rust is fast and safe and concurrent"

## Rule 4: No Verb Tense

All verb stay base form; no past, no future, no progressive, no perfect;

- goodexample: "I go store, buy bread, eat"
- badexample: "I went to the store, bought bread, and ate it"

## Rule 5: Semicolon Separate Thought/Sentence; Comma Separate Step; No Period
<!-- TODO: Create useful colon assignment syntax, use English colon rule now -->

Comma chain action step within one thought; semicolon separate distinct thought, new sentence; never use period;

- goodexample: "I open file, read content, close file; Rust enforce ownership compiletime; many benefit exist"
- badexample: "I open file. I read content. I close file. Rust enforces ownership at compile time. Many benefits exist."

## Rule 6: Conditional Use Semicolon

If/else structure use semicolon separate branch;

- goodexample: "if error exist, fix; else, move next task"
- badexample: "If an error exists, then fix it. Otherwise, move on to the next task."

## Rule 7: Negation "no" Precede Verb

Express negation place "no" before verb;

- goodexample: "I no use filler word"
- badexample: "I don't use filler words"

## Rule 8: Quantifier Precede Object (Preobjectword)

Replace "there are/is" construct; quantity word go direct before noun; no use (s) for word ending;

- goodexample: "many rule exist; one goal remain"
- badexample: "there are many rules; there is one goal"

## Rule 9: Predicate Logic Complex Statement

Express universal/existential claim use logic format;

- goodexample: "for all x, if x human, x mortal"
- casualshortform: "all human mortal"
- badexample: "All humans are mortal"

## Rule 10: Compound Concept Singleword

Join compound concept one word, no hyphen, no space;

- goodexample: "memorysafe compiletime runtimeerror zeroinit"
- badexample: "memory-safe, compile time, runtime error, zero-init"

## Rule 11: Adjective Precede Noun, No Comma Between

Adjective go direct before noun, no comma separate;

- goodexample: "strong static typesystem"
- badexample: "a strong, static type system"

## Rule 12: Time Reference 

If action happen current moment, no write time;

- goodexample: "I write code"
- badexample: "I am currently writing code right now"

If action need exact time, prefer isotimeformat;

- goodexample: "I buy bread 2026-05-27T12:30:00+02:00"
- badexample: "I bought bread yesterday noon."

## Rule 13: No EM Dash, No EN Dash

Never use — or –; use comma, semicolon instead;

- goodexample: "Rust give safety, Cpp give flexibility"
- badexample: "Rust gives safety — Cpp gives flexibility"

## Rule 14: Subject Persist Until Overwrite

Previous subject remain active subject; new subject overwrite; active subject no need repeat;

- goodexample: "Rust enforce ownership, give memorysafe, prevent datarace; Cpp allow directmemory access, give maximum control"
- badexample: "Rust enforces ownership. Rust gives memory safety. Rust prevents data races. Cpp allows direct memory access. Cpp gives maximum control."

## Rule 15: Action Object Context Pattern

Follow Mandarin-like structure: action, object, context; maintain direct sequence;

- goodexample: "I send message qrlh, ask question"
- badexample: "I will send a message to qrlh to ask them a question"

## Rule 16: Parenthesis List Replace Comma List

List no need comma separate; use parenthesis group listitem, space separate; use only if clarity require;

- goodexample: "Rust give (memorysafe zerocost fearlessconcurrency)"
- badexample: "Rust gives memory safety, zero cost, and fearless concurrency"

## Rule 17: Quote

Quote work same English; place " (beginning end), content between;

## Rule 18: Quote English syntax

English syntax quote different, need verticalbar separator "|"; place verticalbar (beginning end), English between;

- goodexample: "Linus say: |Talk is cheap. Show me the code.|"
- badexample: "Linus say: "Talk is cheap. Show me the code.""
