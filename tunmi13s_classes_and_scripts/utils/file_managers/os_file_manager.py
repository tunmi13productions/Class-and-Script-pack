import os
import shutil


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
    return os.path.isfile(path)


def find_recursive(path, wildcard="*.*"):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if wildcard in file or wildcard == "*.*":
                files.append(os.path.join(r, file))

    return files


def find_files(path):
    list = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            list.append(f)
    return list


def find_directories(path):
    l = []
    for each in os.listdir(path):
        if os.path.isdir(os.path.join(path, each)):
            l.append(each)

    return l


def file_copy(path, dest, overwrite=False):
    if overwrite == False:
        if os.path.isfile(path):
            pass
        return False
    else:
        shutil.copy(path, dest)
        return True


def file_delete(path):
    if os.path.isfile(path):
        os.remove(path)
        return True
    else:
        return False


def file_put_contents(filename, content, mode="a"):
    f = open(filename, mode)
    f.write(content)
    f.close()


def file_get_contents(filename, mode="rb"):
    ret = ""
    f = open(filename, mode)
    ret = f.read()
    f.close()
    return ret
