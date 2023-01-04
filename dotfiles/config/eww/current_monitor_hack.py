#!/bin/python3

import subprocess as sp
from os import path


monitors_output: list[str] = bytes.decode(sp.check_output(["hyprctl", "monitors"])).split("\n")

line_num: int = 0
for line_i, line in enumerate(monitors_output):
    if "focused: yes" in line:
        line_num = line_i - 7
        break

line = monitors_output[line_num]
start = line.find("ID ") + 3
end = -2

ID = int(line[start:end])

yuck_file_path = path.join(path.dirname(__file__), "eww.yuck")

yuck_contents = open(yuck_file_path).read().split("\n")
line_with_monitor: int = 0
for line_i, line in enumerate(yuck_contents):
    if ":monitor" in line:
        line_with_monitor = line_i

yuck_contents[line_with_monitor] = f":monitor {ID}"

_yuck_contents = ""

for line in yuck_contents:
    _yuck_contents += line + "\n"

open(yuck_file_path, "w").write(_yuck_contents)
