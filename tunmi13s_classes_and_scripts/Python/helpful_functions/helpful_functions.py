#Helpful Functions, tunmi13 productions
#This script contains a lot of helpful functions I have created, mostly for myself, but I figured other people would have a use for them.
#As I continue to create more projects and require special functions, I will try to add them here in case others need them to.
#Enjoy.

import os

def get_file(path,mode="rb"):
	"""Gets the file specified. Returns the file contents on success, or a blank string on error.
		Parameters:
			path (str): The path of the file, such as C:\test.txt.
			mode(str): The mode to read the file. Examples are rb and r. This is set to rb by default.
	"""
	if not os.path.isfile(path): return ""
	else:
		with open(path,mode) as temp:
			return temp.read()

def write_file(path,contents,mode = "wb",overwrite = True):
	"""This writes to a file. If the path leads to a non-existing file, the file is created automatically. If the overwrite boolean is True, and the file is there, it returns False, since you specified that overwrite should be False, therefore acting like a check to see if the file exists.
		Parameters:
			path (str): The path to find the file. Again, if the file doesn't exist, it will be created.
			mode (str): The mode to write to the file. Example modes are w, wb, a, and ab. This is set to wb by default.
			overwrite (bool): A boolean specifying whether the file should be overwritten if it exists. If this is False, and the file exists, it returns False.
	"""
	if os.path.isfile(path) and not overwrite: return False
	else:
		with open(path,mode) as temp:
			temp.write(contents)
			return True

def lister(list):
	"""This function converts a list into a readable format. For example, providing a list that has 1, 2, 3, will be returned as 1, 2, and 3. If the list is blank, it will return a blank string, and if the list only has one element, it will return just that element.
		Parameters:
			list (list): The list to be converted.
	"""
	if len(list) == 0: return ""
	if len(list) == 1: return list[len(list)-1]
	final = ""
	for i in range(0,len(list)):
		if i == len(list)-1: final += "and "+str(list[i])
		else: final += str(list[i])+", "
	return final

def list_to_linear(the_list):
	"""This converts a list into a linear format. Useful for making files that refer to a list and need to be converted into something the file can write.
		Parameters:
			the_list (list): The list to be converted.
	"""
	if len(the_list) == 0: return ""
	final = ""
	for i in range(0,len(the_list)):
		final += the_list[i]+"\n"
	return final

def linear_to_list(the_string):
	"""This converts a linear string back into a list format. Useful for reading linear files and then converting them back to lists.
		Parameters:
			the_string (str): The string to be converted.
	"""
	if len(the_string) == 0: return ""
	final = the_string.split("\n")
	return final

