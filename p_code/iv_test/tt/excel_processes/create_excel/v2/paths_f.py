from os import path


def is_file_exists(name, directory):
    directory = directory + '/'
    ext = '.xlsx'
    file_name = directory + name + ext

    is_file = path.exists(file_name)
    return file_name, is_file

def is_directory_exists(directory):
    return path.exists(directory)

def get_date_for_directory(name):
    name = list(name.split(' '))
    name = str(name[0])
    if '.' in name:
        name = name.split('.')
        name_arr_index = name.__len__() - 1
        name = name[name_arr_index]
        name = str(name)
    return name