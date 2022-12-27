def count_nested_folders(n, nested_folders):

    if not n in nested_folders:
        nested_folders[n] = 1

    elif n in nested_folders:
        nested_folders[n] = nested_folders[n] + 1

    return nested_folders

def get_nested_folders_count(nested_folders):
    count = 0

    for i in nested_folders:
        count += 1

    return count

def get_list_folder_and_file_count(nested_folders):
    list_folder_and_file_count = []

    for i in nested_folders:
        list_folder_and_file_count.append([i, nested_folders[i]])
        
    return list_folder_and_file_count


def create_folder_and_folder_file_count(list_folder_and_file_count):
    data_string = ''

    for i in list_folder_and_file_count:
        folder = i[0]
        count = i[1]
        count = str(count)
        data_string += ' %s >>> %s ,' % (folder, count)
        
    return data_string[: data_string.__len__() - 1]



def get_file_statistic(nested_folders):
    nested_folders_count = get_nested_folders_count(nested_folders)
    list_folder_and_file_count = get_list_folder_and_file_count(nested_folders)
    data_string = create_folder_and_folder_file_count(list_folder_and_file_count)
    return nested_folders_count, data_string


def get_successfully_message(nested_folders, data_json_length):
        nested_folders_count, data_string = get_file_statistic(nested_folders)
        first = 'proccess done successfully create_excel'.capitalize()
        first = decorate(first)


        msg = '%s nested folders and %s files were created. \n [%s] \n' % (nested_folders_count, data_json_length, data_string)

        last = 'proccess end successfully create_excel'.capitalize()
        last = decorate(last)

        msg = first + msg + last

        return msg

def decorate(msg=''):
    return '------------%s============\n' % msg
