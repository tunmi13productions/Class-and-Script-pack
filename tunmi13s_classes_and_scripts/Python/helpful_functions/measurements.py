#Used for basic measurements, whether for leisure or other purposes.
#This is split into sections to easily decipher what things are meant for.
import math
#***Metrics
def in_to_ft(inches,round_val = 1):
	"""Converts the specified amount of inches into feet.
		Parameters:
			inches (can be a float, double, or int): The inches that you would like to convert.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	return round(inches/12,round_val)
def ft_to_in(feet,round_val = 1):
	"""Converts the specified amount of feet into inches.
		Parameters:
			feet (can be a float, double, or int): The feet that you would like to convert.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	return round(inches*12,round_val)
def cm_to_in(cm,round_val = 1):
	"""Converts the specified amount of inches into centimeters (cm).
		Parameters:
			cm (can be a float, double, or int): The inches that you would like to convert.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	return round(0.39*cm,round_val)
def get_area(length,width,round_val):
	"""Retrieves the area of a quadrilateral.
		Parameters:
			length (can be a float, double, or int): The length of the quadrilateral.
			width (can be a float, double, or int): The width of the quadrilateral.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	return round(length*width,round_val)
def get_volume(length,width,height,round_val):
	"""Retrieves the volume of a box.
		Parameters:
			length (can be a float, double, or int): The length of the box.
			width (can be a float, double, or int): The width of the box.
			height (can be a float, double, or int): The height of the box.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	return round(length*width*height,round_val)
#***Weather
def celsius_to_fahrenheit(c,round_val = 1):
	"""Converts the temperature in degrees Celsius into degrees Fahrenheit.
		Parameters:
			c (can be a float, double, or int): The celsius value that you would like to convert.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	fh = (c*1.8)+32
	return round(fh,round_val)
def fahrenheit_to_celsius(f,round_val = 1):
	"""Converts the temperature in degrees Fahrenheit into degrees Celsius.
		Parameters:
			f (can be a float, double, or int): The Fahrenheit value that you would like to convert.
			round_val (int): The amount to round to. 1 is the default, which means it will return a number rounded to the nearest tenth. Any number after that will round to that decimal. For example, setting round_val to 1 would generate something like 20.3, 2 would be 20.35, etc.
	"""
	cs = (f-32)/1.8
	return round(cs,round_val)
#***Planes, for game maps and such.
def get_1d_distance(d1,d2):
	return abs(d1-d2)
def get_2d_distance(x1,y1,x2,y2):
	x_val = get_1d_distance(x1,x2)
	y_val = get_1d_distance(y1,y2)
	return math.sqrt(x * x + y * y)
def get_3d_distance(x1, y1, z1, x2, y2, z2):
	x = get_1d_distance(x1, x2)
	y = get_1d_distance(y1, y2)
	z = get_1d_distance(z1, z2)
	return sqrt(x * x + y * y + z * z)
