# createpassword.py - An secure password creator program.
# filename accntname   
# $ <cp> <gmail1>

import random
import sys
from myFunctions import *

LETTER_DICT = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
PSWD_LEN = 8


class CreatePassword(object):
	def __init__(self, accntname):
		self.accntname = accntname 		# second commandline arg as the account name

	def accountname(self):
		return self.accntname

	def username(self):
		username = input("Enter username: ")
		return username

	def password(self):
		password = ""
		choice = int(input("1. Add existing password: \t2. Create a new password:\n Choice: "))
		if choice == 1:
			while 1:
				pswd1 = input("Enter existing password: ")
				pswd2 = input("Re-enter existing password: ")

				if pswd1 != pswd2:
					print("Passwords mismatch! Enter password again...")
				else:
					password = pswd1
					break
		elif choice == 2:
			password = "".join(random.sample(LETTER_DICT, PSWD_LEN))
		
		return password	

if __name__ == "__main__":
	cp = CreatePassword(sys.argv[1])

	add_pswd(cp.accountname(), cp.username(), cp.password())
