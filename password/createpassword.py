#! python3
# pw.py - An secure password creator program.
# filename accntname   cp gmail1

import pickle
import random
import sys

info = {}

# with open(r'C:\Users\krunal\Desktop\Python\password\password.asdasd', 'br') as readfile:
# 	info = pickle.load(readfile)

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_password = 8
# accnt_name = {[], [], []}
accnt_name = sys.argv[1]  # second command line arg as the account name




username = input("Enter login id: ")
info[accnt_name[0]] = username

choice = int(input("1. Add existing password: \t2. Create a new password:\n Choice: "))
if choice == 1:
	pswd1 = input("Enter existing password: ")
	pswd2 = input("Re-enter existing password: ")
	if pswd1 == pswd2:
		info[accnt_name[1]] = pswd1
elif choice == 2:
	password = "".join(random.sample(s, len_password))
	info[accnt_name[1]] = password

# append mode
with open(r"E:\STUDIES\PROJECTS\5. My projects\FINISHED PYTHON PROJECTS\password\password.dat", 'a') as filewrite:
	pickle.dump(info, filewrite, protocol=2)
	filewrite.write("\n")


print('Username & Password for ' + accnt_name + ' saved successfully!')



# how to run this file
# win + R to open run cmd
# type just two commands
# cp accountname
# copy filepath of cp.bat in environment variables
