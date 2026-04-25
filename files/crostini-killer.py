#!/usr/bin/env python3

# Crostini Killer
# Copyright (c) 2026 cHamster24. All rights reserved. Fair use permitted.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. Use at your own risk.
version = "V1.0.0 PreRelease Alpha Build 11"

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

rawconfig = None
# opens the csv and reads it
try:
	base_path = os.path.dirname(__file__)
	config_path = os.path.join(base_path, "crostini-killer-config.csv")
	with open(config_path, 'r', newline="") as file:
		rawconfig = list(csv.reader(file))
except Exception:
	print("Error opening file. Are you sure it's in the same folder as this program?\nQuitting...")
	time.sleep(5)
	sys.exit(66)

if not rawconfig:
	print("Config file is empty!\nQuitting...")
	time.sleep(5)
	sys.exit(66)

# writes the data list
data = {}
datakeys = []
for line in rawconfig:
	if line and not str(line[0])[0] == "#":
		if not str(line[0]) in datakeys:
			datakeys.append(str(line[0]))
		try:
			data[str(line[0])] = [str(line[1]), str(line[2])]
		except Exception:
			print("Something seems to be wrong with the config file! Check that formatting is correct.\nQuitting...")
			time.sleep(5)
			sys.exit(65)

def runcommand(command):
	timeout = 10
	try:
		subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=int(timeout)) # in future, timeout will be a user selected variable in a sys config file
	except subprocess.CalledProcessError as e:
		input(f"""An error occured while running "subprocess.run({command})". See error below:
\nCommand Failed: {e.cmd}
Exit Code: {e.returncode}
Terminal said: {e.stderr.strip() or "No error output provided."}
\nPress ENTER to continue: """)
	except subprocess.TimeoutExpired:
		input(f"The process ran but hang (exceeded {timeout} seconds).\n\nPress ENTER to continue: ")		
	except Exception:
		userinput = input("subprocess.run() failed. Using backup os.system()... PRESS ENTER TO QUIT, PRESS ANY KEY + ENTER TO RUN \"os.system()\"")
		if userinput.strip() != "":
			print("Using outdated \"os.system()\"")
			time.sleep(1)
			os.system(command)
		else:
			print("Not running \"os.system()\", returning...")
			time.sleep(1)

# main system process
while True:
	print(fullscreenwipe, end="")
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
		print(clearscreen)
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
		print(clearscreen)
		print("Error - feature not implemented!")
		time.sleep(3)
	elif index == -1: # Alt+F4 Linux
		print(clearscreen)
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
		softkill = data[datakeys[index]][0]
		hardkill = data[datakeys[index]][1]

		completed = False
		while True:
			if completed:
				break
			userinput = input(f"Choose how to kill {datakeys[index]}:\n\n1. Softkill (asking it nicely, '{softkill}')\n\n2. Hardkill (tactical nuke, risks loosing data, '{hardkill}')\n\n3. Nevermind, get me out of here (return to menu)\n\nSelect an option: ")
			try:
				userinputint = int(userinput)
				if (userinputint <= 2) and (userinputint != 0):
					if userinputint == 1:
						print(f"Shutting down process (softkill) with command '{softkill}'...")
						runcommand(softkill)
						completed = True
						time.sleep(3)
						break
						
					else:
						while True:
							userinput = input("Are you sure you wish to tell Linux to nuke this program? Y/N: ")
							if userinput.upper() == "Y":
								print(f"Hardkilling with command '{hardkill}'...")
								runcommand(hardkill)
								completed = True
								time.sleep(3)
								break
							elif userinput.upper() == "N":
								print("Returning")
								time.sleep(1)
								break
							else:
								print("Invalid response, please retype!\n")
								time.sleep(1)
				elif userinputint == 3:
					print("Returning to menu")
					time.sleep(1)
					break
				else:
					print("Invalid option!\n")
					time.sleep(1)
			except Exception:
				print("An error occured.")
				time.sleep(1)
