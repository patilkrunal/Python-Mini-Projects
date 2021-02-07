#! python3
# pw.py - An insecure password locker program.
# filename masterpassword accntname   gp krunal gmail1

import sys
import pickle
import pyperclip

if len(sys.argv) != 2:
	print("Provide exactly 2 arguments: Eg. <gp> <masterpassword>")
	sys.exit()

master_psswd = sys.argv[1]       # second command line arg as the master-password

if(master_psswd == "krunal"):

	with open(r"E:\STUDIES\PROJECTS\5. My projects\FINISHED PYTHON PROJECTS\password\password.dat", 'br') as readfile:
		info = pickle.load(readfile)

	for accnt_name in info:
		print(accnt_name)
	print("-------------------------")

	accnt_name = input("Enter the account name to get password for: ")

	if accnt_name in info:
		pyperclip.copy(info[accnt_name])
		print('Password for ' + accnt_name + ' copied to clipboard.')
	else:
		print('There is no account named ' + accnt_name)
else:
	print("Wrong Master Password!")