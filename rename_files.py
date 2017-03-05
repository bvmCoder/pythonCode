import os
# operating system
# get file names in a folder in Python
# get the files from here
# https://s3.amazonaws.com/udacity-hosted-downloads/ud036/prank.zip
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir("/Users/bp/Documents/takeBreakProgram/prank")
	# for windows os.listdir(r"c:\oop\prank") r for row path
	# print(file_list)
	saved_path = os.getcwd()
	print(saved_path)
	os.chdir("/Users/bp/Documents/takeBreakProgram/prank")
	#(2) for each file, rename fileName
	# use file_name.translate function
	for file_name in file_list:
		print("Old Name of the File:-" + file_name)
		print("New Name of the File:-" + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)


rename_files()

'''
	What would happen if
	1) We try to rename a file that does not exist
	2) We try to rename a file to a name that already exists in the folder

	we have to learn the concept called exception
'''