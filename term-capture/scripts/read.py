#!/usr/bin/env python3
# Show each command of a term-capture session, with its output and its exit
# code. The script uses only the text between the OSC 133 marks. A virtual
# terminal (pyte) replays the output. Thus the result shows the last state of
# the screen, and each progress bar shows only one time.
# The script does not show the screen of full-screen programs (yazi, vim,
# less). It shows one line in its place.
# Usage: read.py LOG
import re
import sys

import pyte

MARK = b"\x1b]133;"
START = re.compile(rb"C;(?:cols=(\d+);)?cmdline=(.*)", re.S)
END = re.compile(rb"D;(\d+)")
# A mark ends with BEL or with ST (ESC backslash).
TERMINATOR = re.compile(rb"\a|\x1b\\")
ALT_SCREEN = re.compile(rb"\x1b\[\?1049h.*?(\x1b\[\?1049l|$)", re.S)
# pyte does not know DCS, SOS, PM, and APC strings (for example the kitty
# graphics queries of yazi). It shows their content as text. Remove them.
CONTROL_STRING = re.compile(rb"\x1b[PX^_].*?(?:\x1b\\|\a)", re.S)
# script(1) writes this line at the end of the log. Match it only there,
# because a command can also show this text.
SCRIPT_DONE = re.compile(rb"\r?\nScript done on [^\n]*\n?\Z")


class Screen(pyte.Screen):
    # pyte 0.8.2 fails on the private form (CSI ? 6 n). Ignore the request.
    def report_device_status(self, *args, **kwargs):
        pass


def render(data, cols):
    data = ALT_SCREEN.sub(b"[full-screen program]\r\n", data)
    data = CONTROL_STRING.sub(b"", data)
    text = data.decode("utf-8", "replace")
    # Wrapped lines also use rows. Make the screen high enough for all rows.
    screen = Screen(cols, text.count("\n") + len(text) // cols + 2)
    pyte.Stream(screen).feed(text)
    lines = [line.rstrip() for line in screen.display]
    while lines and not lines[-1]:
        lines.pop()
    return lines


def show(cmdline, cols, chunks):
    print("$ " + cmdline.decode("utf-8", "replace"))
    print(*render(b"".join(chunks), cols), sep="\n")


def main():
    with open(sys.argv[1], "rb") as f:
        log = f.read()
    ended = SCRIPT_DONE.search(log) is not None
    log = SCRIPT_DONE.sub(b"", log)
    # The command that runs now: (cmdline, cols, output chunks).
    cmd = None
    for part in log.split(MARK)[1:]:
        if t := TERMINATOR.search(part):
            head, body = part[: t.start()], part[t.end() :]
        else:
            head, body = part, b""
        if m := START.fullmatch(head):
            if cmd:
                show(*cmd)
            cmd = (m[2], int(m[1] or 200), [body])
        elif m := END.fullmatch(head):
            # Use only the first D mark after a C mark. The shell
            # integration of the user can write more D marks.
            if cmd:
                show(*cmd)
                print(f"[exit {m[1].decode()}]\n")
                cmd = None
        elif cmd:
            # The shell integration of the user can write more marks
            # during a command. The text after them is command output.
            cmd[2].append(body)
    if cmd:
        show(*cmd)
        if not ended:
            print("[running]")


main()
