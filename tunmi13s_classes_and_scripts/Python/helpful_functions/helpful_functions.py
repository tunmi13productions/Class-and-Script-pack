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

def convert_ms(ms):
	"""Converts milliseconds into a readable format. NOTE: This function is rather messy, but it does the job quite well. Also note that the calculation of days is set to 30, since it's not always possible to know how many exact days a month will have.
		Parameters:
			ms(int): The milliseconds to be converted.
	"""
	if ms < 1000: return "No time at all."
	final = ""
	secs = round(ms/1000,0)
	mins = round(secs/60)
	secs%=60
	secs = round(secs)
	hours = round(mins/60)
	mins%=60
	mins = round(mins)
	days = round(hours/24)
	hours%=24
	hours = round(hours)
	weeks = round(days/7)
	days%=7
	days = round(days)
	months = round(weeks/4)
	weeks%=4
	weeks = round(weeks)
	years = round(months/12)
	months%=12
	months = round(months)
	if years > 0:
		if years == 1: final+=strs(year)+" year. "
		else: final+=str(years)+" years. "
	if months > 0:
		if months == 1: final+=str(months)+" month. "
		else: final+=str(months)+" months. "
	if weeks > 0:
		if weeks == 1: final+=str(weeks)+" week. "
		else: final+=str(weeks)+" weeks. "
	if days > 0:
		if days == 1: final+=str(days)+" day. "
		else: final+=str(days)+" days. "
	if hours > 0:
		if hours == 1: final+=str(hours)+" hour. "
		else: final+=str(hours)+" hours. "
	if mins > 0:
		if mins == 1: final+=str(mins)+" minute. "
		else: final+=str(mins)+" minutes. "
	if secs > 0:
		if secs == 1: final+=str(secs)+" second."
		else: final+=str(secs)+" seconds."
	return final
