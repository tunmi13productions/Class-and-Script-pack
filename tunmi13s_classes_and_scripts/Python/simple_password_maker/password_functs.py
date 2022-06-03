import string
from random import choice

def generate_alphanumeric_password(length = 10):
	password_characters = string.ascii_letters + string.digits
	ret="".join(choice(password_characters) for i in range(length))
	return ret

def generate_alphanumeric_password_plus(length = 10):
	password_characters = string.ascii_letters + string.digits + string.punctuation
	ret="".join(choice(password_characters) for i in range(length))
	return ret

def generate_numeric_password(length = 10):
	password_characters = string.digits
	ret="".join(choice(password_characters) for i in range(length))
	return ret

def generate_alphabetic_password(length = 10):
	password_characters = string.ascii_letters
	ret="".join(choice(password_characters) for i in range(length))
	return ret
