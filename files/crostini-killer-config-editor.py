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
