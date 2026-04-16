# System killer

import psutil
import os
import sys
import csv
userinput = None

rawconfig = None
with open("task-killer-config.csv",  'r', newline="") as file:
	rawconfig = list(csv.reader(file))

data = {}
datakeys = []
for line in rawconfig:
	if not str(line[0])[0] == "*":
		if not str(line[0]) in datakeys:
			datakeys.append(str(line[0]))
		try:
			data[str(line[0])] = [str(line[1]), str(line[2])]
		except Exception:
			pass

while True:
	print("System Killer 1.0")
	
	message = "1. Edit config file\n2. Exit program\n3. Shut down Linux"
	n = 4
	for key in datakeys:
		message = message + str(f"\n{n}. {key}")
		n += 1
	print(message)
	
	while True:
		userinput = input("Select an option: ")
		try:
			userinputint = int(userinput)
			if (userinputint <= (len(datakeys) + 3)) and (userinputint != 0):
				break
			else:
				print("Invalid option. Try again!")
		except Exception:
			print("Invalid option. Try again!")

	index = userinputint - 4
	if index == -3:
		print("Error - feature not implemented!")
	elif index == -2:
		while True:
			userinput = input("Are you sure you wish to exit? Y/N: ")
			if userinput.upper() == "Y":
				sys.exit()
			elif userinput.upper() == "N":
				print("Returning to menu")
				break
			else:
				print("Invalid response, please retype!")
	elif index == -1:
		while True:
			userinput = input("Are you sure you wish to shut down Linux? Y/N: ")
			if userinput.upper() == "Y":
				print("Now asking Linux to shutdown...")
				os.system("shutdown -h now")
			elif userinput.upper() == "N":
				print("Returning to menu")
				break
			else:
				print("Invalid response, please retype!")
				
	else:
		softkill = data[datakeys[index]][0]
		hardkill = data[datakeys[index]][1]
		while True:
			userinput = input(f"Choose how to kill {datakeys[index]}:\n\n1. Softkill (asking it nicely)\n\n2. Hardkill (nuke)\n\n3. Nevermind, get me out of here (return to menu)")
			try: 
				userinputint = int(userinput)
				if (userinputint <= 2) and (userinputint != 0):
					if userinputint == 1:
						print(f"Softkilling with command '{softkill}'...")
						os.system(softkill)
						break
						
					else:
						while True:
							userinput = input("Are you sure you wish to hardkill this program? Y/N: ")
							if userinput.upper() == "Y":
								print(f"Hardkilling with command '{hardkill}'...")
								os.system(hardkill)
								break
							elif userinput.upper() == "N":
								print("Returning")
								break
							else:
								print("Invalid response, please retype!")
				elif userinputint == 3:
					print("Returning to menu")
					break
				else:
					print("Invalid option!")
			except Exception:
				print("Invalid option!")
