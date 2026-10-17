---
name: term-capture
description: Open a new terminal window (xdg-terminal-exec) with an interactive zsh. Claude can read the session, and Claude gets a notification when the user closes the window. Use this skill when the user must run commands (sudo, interactive tools) and Claude needs the output. Also use it when the user asks to "open a shell/terminal for Claude". Use it when the user wants output in the chat without copy and paste.
---

# term-capture

The scripts are in `~/.claude/skills/term-capture/scripts/`. The user types
the commands in the window. Claude does not run commands in the window.

## Procedure

1. Tell the user that a terminal window opens.
2. Run `term-capture.sh` with `run_in_background: true`. To give the user a
   command, send it as a heredoc with the quoted delimiter `TERM_CAPTURE_END`.
   Do not add quotes or escapes to the command:

       term-capture.sh <<'TERM_CAPTURE_END'
       sh -c "echo 'test'"
       TERM_CAPTURE_END

   The command shows in the input line. It does not start until the user
   pushes Enter.
3. Wait for the notification. The script stops when the user closes the
   window.
4. Read the result. It shows each command, its output, and its exit code.

To read the session while the window is open, run `read.py LOG`. The first
line of the `term-capture.sh` output shows the LOG path.

## Function

The file `zdotdir/.zshenv` adds two zsh hooks. zsh gets this file through
ZDOTDIR. Terminal shell integrations use the same method. The zsh files of
the user do not change.

The hooks put invisible OSC 133 marks around the output of each command.
`read.py` shows only the text between the marks. Thus the prompt, the
completion menus, and the autosuggestions do not show in the result.
`read.py` replays the output in a virtual terminal (python-pyte). The result
shows the last state of the screen, so progress bars show only one time.

## Data

The log is in `$XDG_RUNTIME_DIR`. This directory is a tmpfs for each user.
The system clears it at logout. The log contains all the text that the window
showed. Typed text is also in the log if the terminal shows it.
