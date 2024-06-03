import os

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
    size = os.path.getsize(filename)
    if size < 1024:
        return f"{size} bytes"
    elif size < pow(1024, 2):
        return f"{round(size/1024, 2)} KB"
    elif size < pow(1024, 3):
        return f"{round(size/(pow(1024,2)), 2)} MB"
    elif size < pow(1024, 4):
        return f"{round(size/(pow(1024,3)), 2)} GB"


def get_file_size_b(filename):
    """
    Gets the size of a file in bytes.

    Args:
     filename: The path to the file.

    Returns:
     The size of the file in bytes.
    """
    return os.path.getsize(filename)


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
