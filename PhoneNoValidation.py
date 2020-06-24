#! python 3
import re

def isPhoneNumber(no):
	# if len(no)!=12:
	# 	return False
	# for i in range(0,3):
	# 	if not no[i].isdecimal():
	# 		return False
	# if no[3]!='-':
	# 	return False
	# for i in range(4,7):
	# 	if not no[i].isdecimal():
	# 		return False
	# if no[7]!='-':
	# 	return False
	# for i in range(8,12):
	# 	if not no[i].isdecimal():
	# 		return False
	# return True
# -------------------------------------------------------
# 	phoneNoRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# 	mo = phoneNoRegex.search(no)
# 	print(mo.group(0))
# 	print(mo.group(1))
# 	print(mo.group(2))
# 	# print(mo.group(3))
#
# 	areaCode, mainNumber, lastNumber = mo.groups()
# 	print(areaCode)
# 	print(mainNumber)
# 	print(lastNumber)
# ------------------------------------------------------------
# 	phoneNoRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# 	# mo = phoneNoRegex.search(no)
# 	mo = phoneNoRegex.findall(no)
# 	print(mo)
# --------------------------------------------------------------
	phoneRegex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?              # area code
		(\s|-|\.)?                      # separator
		\d{3}                           # first 3 digits
		(\s|-|\.)                       # separator
		\d{4}                           # last 4 digits
		(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
	)''', re.VERBOSE)


if __name__ == '__main__':
	# no = input()
	no = "My number is 123-555-4242. Cell: 415-555-9999 Work: 212-555-0000"
	isPhoneNumber(no)