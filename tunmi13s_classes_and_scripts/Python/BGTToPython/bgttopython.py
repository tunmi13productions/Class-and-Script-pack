#This modjule holds a lot of the BGT functions that you all know and love. Keep in mind that not all functions are covered.
import time
import pygame
import sys
import os
import shutil
import pyperclip
from random import randint
from math import *
#This function takes the time.sleep() function and makes it take millisecond values. So you can do wait(5), and it will automatically be divided to output to time.sleep() as 0.005.
def wait(milliseconds = 5):
	time.sleep(milliseconds/1000)

#All your directory and file management functions.
def directory_create(path):
	try:
		os.mkdir(path)
		return True
	except:
		return False
def directory_delete(path):
	try:
		os.rmdir(path)
		return True
	except:
		return False
def directory_exists(path):
	return os.path.isdir(path)
def file_exists(path):
	return os.isfile(path)
def find_files(dest):
	list = []
	for f in os.listdirs(dest):
		if os.dest.isfile(f): list.append(f)
	return f
def find_directories(dest):
	list = []
	for f in os.listdirs(dest):
		if os.dest.isdir(f): list.append(f)
	return f
def file_delete(path):
	if os.path.isfile(path):
		os.remove(path)
		return True
	else:
		return False
def file_copy(path,dest,overwrite=False):
	if not overwrite and os.path.isfile(path):
		return False
	else:
		shutil.copy(path,dest)
		return True

#Clipboard functions
def clipboard_copy_text(the_string):
	try:
		pyperclip.copy(the_string)
		return True
	except:
		return False

def clipboard_read_text():
	return pyperclip.paste()

#Other useful things that I just threw in here.
def get_file(path):
	if os.isfile(path):
		f = open(path,"rb")
		ret = f.read()
		f.close()
		return ret
	else: return ""

def edit_file(path,mode,data):
	f = open(path,mode)
	f.write(data)
	f.close()

#Mathematical operations.
def absolute(value1,value2):
	return abs(value1,value2)
def random(value1,value2):
	return randint(value1,value2)
def power(base,exponent):
	return base**exponent
def square_root(value):
	return sqrt(value)
def percentage(value1,value2):
	new_value = (value1/value2)*100
	return new_value
