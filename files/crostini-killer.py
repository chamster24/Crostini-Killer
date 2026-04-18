#!/usr/bin/env python3

# Crostini Killer
# Copyright (c) 2026 cHamster24. All rights reserved. Fair use permitted.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. Use at your own risk.
version = "V1.0.0 PreRelease Alpha Build 6"

import psutil
import os
import sys
import csv
import time
userinput = None

rawconfig = None
# opens the csv and reads it
with open("crostini-killer-config.csv", 'r', newline="") as file:
	rawconfig = list(csv.reader(file))

# writes the data list
data = {}
datakeys = []
for line in rawconfig:
	if not str(line[0])[0] == "#":
		if not str(line[0]) in datakeys:
			datakeys.append(str(line[0]))
		try:
			data[str(line[0])] = [str(line[1]), str(line[2])]
		except Exception:
			pass

# main system process
while True:
	print(f"Crostini Killer {version}")
	
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
		while True:
			userinput = input("Are you sure you wish to exit? Y/N: (NOTE: THIS SCRIPT DOES NOT WORK AS INTENDED. IF YOU RUN IT LINUX WON'T OPEN UNTIL YOU RESTART.) ")
			if userinput.upper() == "Y":
				sys.exit()
			elif userinput.upper() == "N":
				print("Returning to menu")
				break
			else:
				print("Invalid response, please retype!")
	elif index == -2: # edit CSV
		print("Error - feature not implemented!")
	elif index == -1: # Alt+F4 Linux
		while True:
			userinput = input("Are you sure you wish to shut down Linux? Y/N: ")
			if userinput.upper() == "Y":
				print("Now asking Linux to shutdown...")
				os.system("sudo shutdown -h now")
				time.sleep(10)
				sys.exit()
			elif userinput.upper() == "N":
				print("Returning to menu")
				time.sleep(1)
				break
			else:
				print("Invalid response, please retype!")
				
	else:
		softkill = data[datakeys[index]][0]
		hardkill = data[datakeys[index]][1]

		completed = False
		while True:
			if completed:
				break
			userinput = input(f"Choose how to kill {datakeys[index]}:\n\n1. Softkill (asking it nicely, '{softkill}')\n\n2. Hardkill (tactical nuke, risks loosing data, '{hardkill}')\n\n3. Nevermind, get me out of here (return to menu)")
			try:
				userinputint = int(userinput)
				if (userinputint <= 2) and (userinputint != 0):
					if userinputint == 1:
						print(f"Shutting down process (softkill) with command '{softkill}'...")
						os.system(softkill)
						completed = True
						time.sleep(3)
						break
						
					else:
						while True:
							userinput = input("Are you sure you wish to tell Linux to nuke this program? Y/N: ")
							if userinput.upper() == "Y":
								print(f"Hardkilling with command '{hardkill}'...")
								os.system(hardkill)
								completed = True
								time.sleep(3)
								break
							elif userinput.upper() == "N":
								print("Returning")
								time.sleep(1)
								break
							else:
								print("Invalid response, please retype!")
				elif userinputint == 3:
					print("Returning to menu")
					time.sleep(1)
					break
				else:
					print("Invalid option!")
					time.sleep(0.5)
			except Exception:
				print("Error - Potentially invalid option")
				time.sleep(0.5)
