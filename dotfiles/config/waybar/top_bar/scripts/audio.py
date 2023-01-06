#!/bin/python3

import json
import subprocess as sp
import sys


volume_str: str = bytes.decode(sp.check_output(["wpctl", "get-volume", "@DEFAULT_SINK@"]))
volume = volume_str[10:].replace("\n", "")
status: str = "muted" if "MUTED" in volume_str else "non-muted"
if status == "muted":
    volume = volume.replace(" [MUTED]", "")

sys.stdout.write(json.dumps({
    "text": volume,
    "alt": status
}) + "\n")
sys.stdout.flush()
