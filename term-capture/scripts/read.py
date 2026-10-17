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
ALT_SCREEN = re.compile(rb"\x1b\[\?1049h.*?(\x1b\[\?1049l|$)", re.S)
# script(1) writes this line at the end of the log.
SCRIPT_DONE = re.compile(rb"\r?\nScript done on .*", re.S)


class Screen(pyte.Screen):
    # pyte 0.8.2 fails on the private form (CSI ? 6 n). Ignore the request.
    def report_device_status(self, *args, **kwargs):
        pass


def render(data, cols):
    data = ALT_SCREEN.sub(b"[full-screen program]\r\n", data)
    text = data.decode("utf-8", "replace")
    # Wrapped lines also use rows. Make the screen high enough for all rows.
    screen = Screen(cols, text.count("\n") + len(text) // cols + 2)
    pyte.Stream(screen).feed(text)
    lines = [line.rstrip() for line in screen.display]
    while lines and not lines[-1]:
        lines.pop()
    return lines


def main():
    with open(sys.argv[1], "rb") as f:
        log = f.read()
    ended = SCRIPT_DONE.search(log) is not None
    log = SCRIPT_DONE.sub(b"", log)
    running = False
    for part in log.split(MARK)[1:]:
        head, _, body = part.partition(b"\a")
        if m := START.fullmatch(head):
            print("$ " + m[2].decode("utf-8", "replace"))
            print(*render(body, int(m[1] or 200)), sep="\n")
            running = True
        elif m := END.fullmatch(head):
            print(f"[exit {m[1].decode()}]\n")
            running = False
    if running and not ended:
        print("[running]")


main()
