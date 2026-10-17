# term-capture: This file restores the ZDOTDIR of the user. Then zsh reads
# the startup files of the user as usual. This file also adds two hooks.
# The hooks put invisible OSC 133 marks around the output of each command.
# Terminal shell integrations (ghostty, kitty) use the same method.
if [[ -n $CLAUDE_SHELL_ORIG_ZDOTDIR ]]; then
  ZDOTDIR=$CLAUDE_SHELL_ORIG_ZDOTDIR
else
  unset ZDOTDIR
fi
unset CLAUDE_SHELL_ORIG_ZDOTDIR
[[ -f ${ZDOTDIR:-$HOME}/.zshenv ]] && source "${ZDOTDIR:-$HOME}/.zshenv"

# Before the command starts: write the C mark with the terminal width and the
# command line.
_claude_preexec() {
  _claude_ran=1
  print -rn -- $'\e]133;C;cols='"$COLUMNS"';cmdline='"${1//[$'\a\e']/}"$'\a'
}
# Before the next prompt: write the D mark with the exit code.
_claude_precmd() {
  local rc=$?
  [[ -n $_claude_ran ]] || return 0
  print -rn -- $'\e]133;D;'"$rc"$'\a'
  unset _claude_ran
}
autoload -Uz add-zsh-hook
add-zsh-hook preexec _claude_preexec
add-zsh-hook precmd _claude_precmd

# At the first prompt: put CLAUDE_SHELL_PREFILL in the input line. zsh does
# not run it. The user can edit it, and then push Enter.
_claude_prefill() {
  [[ -n $CLAUDE_SHELL_PREFILL ]] && print -rz -- "$CLAUDE_SHELL_PREFILL"
  unset CLAUDE_SHELL_PREFILL
  add-zsh-hook -d precmd _claude_prefill
}
add-zsh-hook precmd _claude_prefill
