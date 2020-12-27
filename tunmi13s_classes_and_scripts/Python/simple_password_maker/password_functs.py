import random
from random import randrange
def generate_alphanumeric_password(length = 10):
	ret = ""
	generation = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
	for i in range(length):
		g = randrange(len(generation))
		ret += generation[g]
	return ret

def generate_alphanumeric_password_plus(length = 10):
	ret = ""
	generation = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./!@#$%^&*()_+<>?-=`~|"
	for i in range(length):
		g = randrange(len(generation))
		ret += generation[g]
	return ret

def generate_numeric_password(length = 10):
	ret = ""
	generation = "1234567890"
	for i in range(length):
		g = randrange(len(generation))
		ret+=generation[g]
	return ret

def generate_alphabetic_password(length = 10):
	ret = ""
	generation = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(length):
		g = randrange(len(generation))
		ret+=generation[g]
	return ret
