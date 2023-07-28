"""
This code gets the size of a file in bytes and human-readable format.

"""

def get_file_size(filename):
 """
 Gets the size of a file in human-readable format.

 Args:
  filename: The path to the file.

 Returns:
  The size of the file in human-readable format.
 """

 with open(filename, "rb") as f:
  size = f.read()
 return get_string_size(size)

def get_file_size_b(filename):
 """
 Gets the size of a file in bytes.

 Args:
  filename: The path to the file.

 Returns:
  The size of the file in bytes.
 """

 with open(filename, "rb") as f:
  size = f.read()
 return get_string_size_b(size)

def get_string_size(size):
 """
 Gets the size of a string in human-readable format.

 Args:
  size: The string to get the size of.

 Returns:
  The size of the string in human-readable format.
 """

 bytes = len(size)
 if bytes < 1024:
  return f"{round(bytes, 2)} B"
 else:
  bytes = bytes / 1024
  if bytes < 1024:
   return f"{round(bytes, 2)} KB"
  else:
   bytes = bytes / 1024
   if bytes < 1024:
    return f"{round(bytes, 2)} MB"
   else:
    bytes = bytes / 1024
    return f"{round(bytes, 2)} GB"

def get_string_size_b(size):
 """
 Gets the size of a string in bytes.

 Args:
  size: The string to get the size of.

 Returns:
  The size of the string in bytes.
 """

 return len(size)

if __name__ == "__main__":
 filename = "Silent Night.m4a"
 size = get_file_size(filename)
 print(size)
 size_b = get_file_size_b(filename)
 print(size_b)
