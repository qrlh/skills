#!/usr/bin/env bash
# Open an interactive zsh in a new terminal window. The script records the
# session in a log file. It waits until the user closes the window. Then it
# shows each command with its output and its exit code.
# Run the script in the background. Then you get a notification when the
# window closes.
# Usage: term-capture.sh [COMMAND]
#        term-capture.sh <<'TERM_CAPTURE_END'
#        COMMAND
#        TERM_CAPTURE_END
# COMMAND is optional. The script puts it in the input line of the first
# prompt, but does not run it. If there is no argument, the script reads
# COMMAND from stdin. A heredoc with a quoted delimiter needs no quotes or
# escapes.
dir=$(dirname "$(readlink -f "$0")")/..
for cmd in xdg-terminal-exec zsh script; do
	command -v "$cmd" >/dev/null || { echo "term-capture: $cmd not found" >&2; exit 1; }
done
log=$(mktemp "${XDG_RUNTIME_DIR:-/tmp}/claude-shell.XXXXXX.log") || exit 1
echo "log: $log"
prefill=${1-}
[[ -z $prefill && ! -t 0 ]] && prefill=$(cat)
setsid xdg-terminal-exec -- env CLAUDE_SHELL_LOG="$log" CLAUDE_SHELL_ORIG_ZDOTDIR="${ZDOTDIR-}" \
	CLAUDE_SHELL_PREFILL="$prefill" \
	ZDOTDIR="$dir/zdotdir" SHELL="$(command -v zsh)" script -qf "$log" \
	>/dev/null 2>&1 </dev/null &
# Wait until script(1) starts (20 seconds maximum).
for ((i = 0; i < 20; i++)); do pgrep -f "script -qf $log" >/dev/null && break; sleep 1; done
if ((i == 20)); then
	echo "term-capture: the terminal window did not open" >&2
	exit 1
fi
# Wait until the user closes the window.
while pgrep -f "script -qf $log" >/dev/null; do sleep 1; done
"$dir/scripts/read.py" "$log"
