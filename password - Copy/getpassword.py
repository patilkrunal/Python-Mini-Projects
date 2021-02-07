# getpassword.py - An insecure password locker program.
# filename masterpassword accntname   <gp> <krunal>

import sys
import pickle

from myFunctions import *

class GetPassword(object):
	def __init__(self, masterpsswd):
		try:
			if(masterpsswd != "krunal"):
				print("Wrong masterpassword!!!")
				sys.exit()
		except IOError as e:
			print(e)
			sys.exit()
		

if __name__ == "__main__":
	gp = GetPassword(sys.argv[1])
	
	get_pswds()
	print("---------------------------------")
	
	accntname = input("Enter the accountname to get password for: ")
	get_pswd(accntname)
