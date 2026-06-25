#!/usr/bin/env python3

# Crostini Killer
# Copyright (c) 2026 cHamster24. All rights reserved. Fair use permitted.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. Use at your own risk.
version = "V1.0.0 PreRelease Alpha Build 16.1.1"

# import psutil # requires pip
import math
import shutil
import os
import sys
import csv
import time
import subprocess
userinput = None

terminal_width, terminal_height = shutil.get_terminal_size()

# ANSI Escape Sequences
ansi_fullscreenwipe = "\033c" # also resets colors (full terminal reset)
ansi_clearscreen = "\033[2J\033[H" # \033[2J wipes screen and \033[H moves cursor to top left

rawconfig = None
# opens the csv and reads it
try:
	base_path = os.path.dirname(__file__)
	config_path = os.path.join(base_path, "crostini-killer-config.csv")
	with open(config_path, 'r', newline="") as file:
		rawconfig = list(csv.reader(file))
except Exception:
	print("Error opening config file. Are you sure it's in the same folder as this program?\nQuitting...")
	time.sleep(5)
	sys.exit(66)

if not rawconfig:
	print("Config file is empty!\nQuitting...")
	time.sleep(5)
	sys.exit(66)

# FUTURE - READS SETTINGS FILE
"""
try:
	base_path = os.path.dirname(__file__)
	settings_path = os.path.join(base_path, "crostini-killer-settings.csv")
	with open(settings_path, 'r', newline="") as file:
		rawsettings = list(csv.reader(file))
except Exception:
	print("Error opening settings file. Are you sure it's in the same folder as this program?\nQuitting...")
	time.sleep(5)
	sys.exit(66)

# add check to see if settings file is malformed
"""

def settingsfileerror(error_details, crash):
	try:
		clearscreen()
	except Exception:
		print("=" * terminal_width)
	input(f"There is an error with the settings file! Check info below:\n\nProgram said: \"{error_details}\"\n\nPress ENTER to quit: ")
	if crash:
		sys.exit(65)

# in future, check if TERMINAL MODE is ON or OFF
settings = {
	"terminal_mode_t/f": False,
	"command_timeout": 10
}

def terminal_mode_true_setup(): # default
	def clearscreen():
		print("=" * terminal_width)
	if terminal_width % 2 == 0:
		def fullscreenwipe():
			print("-+" * (terminal_width // 2))
			print("=" * terminal_width)
			print("-+" * (terminal_width // 2))
	else:
		def fullscreenwipe():
			print(("-+" * math.floor(terminal_width // 2)) + "-")
			print("=" * terminal_width)
			print(("-+" * math.floor(terminal_width // 2)) + "-")

if "terminal_mode_t/f" in settings:
	if settings["terminal_mode_t/f"] == False: #the user wishes the program be in program mode
		def clearscreen():
			print(ansi_clearscreen, end="")
		def fullscreenwipe():
			print(ansi_fullscreenwipe, end="")
	elif settings["terminal_mode_t/f"] == True: # also known as debug mode
		terminal_mode_true_setup()
	else: # invalid value
		settingsfileerror("Missing/non-binary value for terminal_mode; defaulting to True for debug purposes", True)
		terminal_mode_true_setup()
else: # dict pair not in settings list
	settingsfileerror("Missing value for terminal_mode; defaulting to True for debug purposes", True)
	terminal_mode_true_setup()

SET_command_timeout = 10 # default timeout num of secs
if "command_timeout" in settings:
	try:
		if int(settings["command_timeout"]) > 0:
			SET_command_timeout = int(settings["command_timeout"])
		else: # value = 0
			settingsfileerror("command_timeout can't be 0; defaulted to 10 sec", False)
	except (ValueError, TypeError): # invalid value
		settingsfileerror("Missing/non-int value for command_timeout; defaulted to 10 sec", False)
else: # dict pair not in settings list
	settingsfileerror("Missing value for command_timeout; defaulted to 10 sec", False)
	
# writes the data list
data = {}
datakeys = []
for line in rawconfig:
	if line and line[0].strip() != "" and not (str(line[0]).strip()).startswith("#"): # check if it's not a comment line
		if not str(line[0]) in datakeys:
			datakeys.append(str(line[0]))
		try:
			data[str(line[0])] = [str(line[1]), str(line[2])]
		except Exception: # line is "abc,abc"
			try:
				data[str(line[0])] = [str(line[1]), ""]
			except Exception: # line is "abc"
				try:
					data[str(line[0])] = ["", ""]
				except Exception:
					pass #skips doing this line
					"""
						print("Something seems to be wrong with the config file! Please check that formatting is correct.\nQuitting...")
						time.sleep(5)
						sys.exit(65)
					"""

def runcommand(command):
	try:
		subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=int(SET_command_timeout))
		clearscreen()
	except subprocess.CalledProcessError as e:
		input(f"""An error occured while running "subprocess.run({command})". See error below:
\nCommand Failed: {e.cmd}
\nExit Code: {e.returncode}
\nTerminal said: {e.stderr.strip() or "No error output provided."}
\nPress ENTER to continue: """)
	except subprocess.TimeoutExpired:
		clearscreen()
		input(f"The process ran but hang (exceeded {SET_command_timeout} seconds).\n\nPress ENTER to continue: ")		
	except Exception:
		while True:
			clearscreen()
			userinput = input(f"subprocess.run() failed. Using backup os.system()...\n\nPress ENTER to quit, or\nPress Y + ENTER to run \"os.system({command})\"\nPlease enter your input: ")
			if userinput.strip() == "Y":
				print("Using outdated \"os.system()\"...")
				time.sleep(1)
				os.system(command)
				break
			elif userinput.strip() == "N":
				print("Not running \"os.system()\", returning...")
				time.sleep(1)
				break
			else:
				print("Invalid input, please try again!")

# main system process
while True:
	fullscreenwipe()
	print(f"Crostini Killer {version}\n")
	
	message = "\n1. Exit program\n2. Edit config file\n3. Shut down Linux"
	n = 4
	for key in datakeys:
		message = message + str(f"\n{n}. {key}")
		n += 1
	print(message)
	
	while True:
		userinput = input("Select an option: ")
		try: # verifies the input
			userinputint = int(userinput)
			if (userinputint <= (len(datakeys) + 3)) and (userinputint != 0):
				break
			else:
				print("Invalid option. Try again!")
		except Exception:
			print("Invalid option. Try again!")

	index = userinputint - 4
	
	if index == -3: # quit
		clearscreen()
		while True:
			userinput = input("Are you sure you wish to exit? Y/N: ")
			if userinput.upper() == "Y":
				sys.exit()
			elif userinput.upper() == "N":
				print("Returning to menu")
				break
			else:
				print("Invalid response, please retype!\n")
				time.sleep(1)
	elif index == -2: # edit CSV
		clearscreen()
		print("Error - feature not implemented!")
		time.sleep(3)
	elif index == -1: # Alt+F4 Linux
		clearscreen()
		while True:
			userinput = input("Are you sure you wish to shut down Linux? (NOTE: THIS SCRIPT DOES NOT WORK AS INTENDED. IF YOU RUN IT LINUX WON'T OPEN UNTIL YOU RESTART.) Y/N: ")
			if userinput.upper() == "Y":
				print("Now asking Linux to shutdown...")
				runcommand("sudo shutdown -h now")
				time.sleep(10)
				sys.exit()
			elif userinput.upper() == "N":
				print("Returning to menu")
				time.sleep(1)
				break
			else:
				print("Invalid response, please retype!\n")
				time.sleep(1)
				
	else:
		softkill_iscomment = False
		hardkill_iscomment = False
		if (data[datakeys[index]][0]).strip() == "": # assume name of kill program is the same as the pid
			softkill = str(f"pkill {datakeys[index]}")
		elif ((data[datakeys[index]][0]).strip()).startswith("!"): # custom command
			softkill = (((data[datakeys[index]][0]).strip())[1:]).strip()
		elif ((data[datakeys[index]][0]).strip()).startswith("#"): # comment
			softkill_iscomment = True
			softkill = str(f"#CMT'{(((data[datakeys[index]][0]).strip())[1:]).strip()}'")
		else: # set pkill to PID put inside the row
			softkill = str(f"pkill {data[datakeys[index]][0]}")

		if (data[datakeys[index]][1]).strip() == "": # assume name of kill program is the same as the pid
			hardkill = str(f"pkill -9 {datakeys[index]}")
		elif ((data[datakeys[index]][1]).strip()).startswith("!"): # custom command
			hardkill = (((data[datakeys[index]][1]).strip())[1:]).strip()
		elif ((data[datakeys[index]][1]).strip()).startswith("#"): # comment
			hardkill_iscomment = True
			hardkill = str(f"#CMT'{(((data[datakeys[index]][1]).strip())[1:]).strip()}'")
		else: # set pkill to PID put inside the row
			hardkill = str(f"pkill -9 {data[datakeys[index]][1]}")
	

		completed = False
		while True:
			if completed:
				break

			# MAKES the question string
			question = f"Choose how to kill {datakeys[index]}:"
			if softkill_iscomment:
				question += f"\n\n1. Softkill NOT available - comment: {softkill[4:]}"
			else:
				question += f"\n\n1. Softkill (asking it nicely, '{softkill}')"
			if hardkill_iscomment:
				question += f"\n\n2. Hardkill NOT available - comment: {hardkill[4:]}"
			else:
				question += f"\n\n2. Hardkill (tactical nuke, risks losing data, '{hardkill}')"				
			question += "\n\n3. Nevermind, get me out of here (return to menu)\n\nSelect an option: "
			
			clearscreen()
			userinput = input(question)
			try:
				userinputint = int(userinput)
				if userinputint == 1:
					if not softkill_iscomment:
						print(f"Shutting down process (softkill) with command '{softkill}'...")
						runcommand(softkill)
						completed = True
						time.sleep(3)
						break
					else:
						input("You can't choose to run a comment!\nPress ENTER to continue: ")
						
				elif userinputint == 2:		
					if not hardkill_iscomment:
						while True:
							userinput = input("Are you sure you wish to tell Linux to nuke this program? Y/N: ")
							if userinput.upper() == "Y":
								print(f"Hardkilling with command '{hardkill}'...")
								runcommand(hardkill)
								completed = True
								time.sleep(3)
								break
							elif userinput.upper() == "N":
								print("Returning...")
								time.sleep(1.5)
								break
							else:
								input("Invalid response, please retype!\nPress ENTER to continue: ")
					else:
						input("You can't choose to run a comment!\nPress ENTER to continue: ")
						
				elif userinputint == 3:
					print("Returning to menu...")
					time.sleep(1.5)
					completed = True
					break
				else:
					input("Invalid option!\nPress ENTER to continue: ")
			except Exception:
				input("An error occured. Are you sure you entered a number?\nPress ENTER to continue: ")
