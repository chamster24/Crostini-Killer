#!/usr/bin/env python3

# Crostini Killer (Config File Editor)
# Copyright (c) 2026 cHamster24. All rights reserved. Fair use permitted.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. Use at your own risk.

import psutil
import os
import sys
import csv
import time
import subprocess
userinput = None

# ANSI Escape Sequences
fullscreenwipe = "\033c" # also resets colors
clearscreen = "\033[2J" # leaves cursor be

#Read the .csv config file
rawconfig = None
try:
	base_path = os.path.dirname(__file__)
	config_path = os.path.join(base_path, "crostini-killer-config.csv")
	with open(config_path, 'r', newline="") as file:
		rawconfig = list(csv.reader(file))
except Exception:
	print("Error opening file. Are you sure it's in the same folder as this program?\nQuitting...")
	time.sleep(5)
	sys.exit(66)


# Main Process
while True:
  pass

# Script to write it
def savechanges():
  try:
    with open(config_path, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(rawconfig)
    print("Rewrote config file with the latest changes!")
  except Exception:
    print("An error occured while writing to the config file!")
