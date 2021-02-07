#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# import send2trash
import os


def function():
	for folderName, subfolders, filenames in os.walk('C:\\Users\\krunal\\Desktop\\Python\\password'):
		print(f'the current folder is {folderName}')
		
		for subfolder in subfolders:
			print(f'Subfolder of {folderName}: {subfolder}')
			
		for filename in filenames:
			print(f'file inside {folderName}: {filename}')
		print('')


if __name__ == '__main__':
		function()
