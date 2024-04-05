#This file manager uses pathlib instead of OS for file handling.

import shutil
from pathlib import Path

def directory_create(path):
    try:
        Path(path).mkdir()
        return True
    except Exception as e:
        print(e)
        return False

def directory_delete(path, force = False):
    if force:
        try:
            shutil.rmtree(path)
            return True
        except Exception as e:
            print(e)
            return False
    else:
        try:
            Path(path).rmdir()
            return True
        except Exception as e:
            print(e)
            return False

def directory_exists(path):
    return Path(path).is_dir()

def file_exists(path):
    return Path(path).is_file()

def find_recursive(path, wildcard="*.*"):
    files = []
    for file in Path(path).rglob(wildcard):
        files.append(file)
    return files

def find_files(path):
    files = []
    for file in Path(path).iterdir():
        if file.is_file():
            files.append(file.name)
    return files

def find_directories(path):
    dirs = []
    for dir in Path(path).iterdir():
        if dir.is_dir():
            dirs.append(dir.name)
    return dirs

def file_copy(path, dest, overwrite=False):
    if overwrite == False:
        if Path(dest).is_file():
            return False
    shutil.copy(path, dest)
    return True

def file_delete(path):
    try:
        Path(path).unlink()
        return True
    except Exception as e:
        print(e)
        return False

def file_put_contents(filename, content, mode="a"):
    with open(filename, mode) as f:
        f.write(content)

def file_get_contents(filename, mode="r"):
    with open(filename, mode) as f:
        return f.read()

def get_file_name(path):
    return Path(path).name
