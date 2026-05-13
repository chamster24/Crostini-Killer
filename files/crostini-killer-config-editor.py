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
import curses
userinput = None
keylist = []

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


# Script to write the changes
def savechanges(): #add making a temp file, and using that temp file to replace the directory instead
	try:
		with open(config_path, "w", newline="") as file:
			writer = csv.writer(file)
			writer.writerows(rawconfig)
			print("Rewrote config file with the latest changes!")
	except Exception:
		print("An error occured while writing to the config file!")
		
# Define main processes
def readcsv():
	pass

def editcsv():
	global keylist
	# Add script to move the edit cursor to the latest
	curses.filter()
	stdscr = curses.initscr()
	stdscr.keypad(True)

	try:
		while True:
			ch = stdscr.getch()
			if ch == curses.KEY_UP:
				if not "UP" in keylist:
					keylist.append("UP")
			else:
				if "UP" in keylist:
					keylist.remove("UP")
			if ch == curses.KEY_DOWN:
				if not "DN" in keylist:
					keylist.append("DN")
			else:
				if "DN" in keylist:
					keylist.remove("DN")
			if ch == curses.KEY_LEFT:
				if not "LT" in keylist:
					keylist.append("LT")
			else:
				if "LT" in keylist:
					keylist.remove("LT")
			if ch == curses.KEY_RIGHT:
				if not "RT" in keylist:
					keylist.append("RT")
			else:
				if "RT" in keylist:
					keylist.remove("RT")
            		if ch == curses.ESCAPE:
				print("Quitting...")
				time.sleep(1.5)
                break
	finally:
	        # 3. Clean up
	        curses.endwin()

def help():
	print("No Help Documentation Yet")
	time.sleep(3)

def quitprogram():
	userinput = input("Are you sure you want to quit?\nPress 'Y' and then press enter to quit.\nPress any other key and enter to return to program.")
	if userinput.upper() == "Y":
		print("Leaving config editor.")
		time.sleep(3)
		quit()
	else:
		print("Returning.")
		time.sleep(2)

# Main Process
while True:
	print(clearscreen)
	print("Crostini Killer Config File Editor\n----------")
	userinput = input("- Menu -\n1. Read CSV config file\n2. Edit CSV config file\n3. Help on this program\n4. Quit")
	if userinput.isdigit() and int(userinput) == 1:
		readcsv()
	elif userinput.isdigit() and int(userinput) == 2:
		editcsv()	
	elif userinput.isdigit() and int(userinput) == 3:
		help()
	elif userinput.isdigit() and int(userinput) == 4:
		quitprogram()
	else:
		print("Invalid input. Try again.")
		time.sleep(1.5)

