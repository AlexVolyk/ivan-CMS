from os import listdir, makedirs, path
from .create_file import create_file
from .folders_file_statistic import count_nested_folders, get_successfully_message


from .help_f import get_json
from .paths_f import get_date_for_directory, is_directory_exists, is_file_exists


def run_v2(create_one=False, mode=True, date=False, direct=False):
    # print('aboooba')
    # print(listdir('../'), '===============')
    # print(listdir('../../'), '=-=--=-=-=--=-=')

    if not create_one:
        # print('yee')
        directory = '../excel'
        # print(listdir('..'))

        data = get_json()
        data = data['main_data']
        nested_folders = {}

        if not path.exists(directory):
            makedirs(directory)

        data_json_length = data.__len__()
        is_allowed_length = True if data_json_length > 0 else False

        if is_allowed_length:
            for i in data:
                name = i['date']

                n = get_date_for_directory(name)
                d = directory + '/' + n
                is_directory = is_directory_exists(d)

                nested_folders = count_nested_folders(n, nested_folders)
                if not is_directory:
                    makedirs(d)

                file_name, is_file = is_file_exists(name, directory=d)

                # if not is_file:
                data = i
                date = name
                create_file(filename=file_name, mode=mode,
                            data=data, date=date)

                msg = '%s created' % file_name
                print('------------%s============' % (msg))

            msg = get_successfully_message(nested_folders, data_json_length)
            print(msg)
        else:
            # msg = 'this length of [data] field in [%s] is not higher than 0. Current length is %s' % (
            #     json_file, data_json_length)
            # msg = msg.capitalize()
            # print('------------%s============' % (msg))
            msg = 'this length of [data] is not higher than 0. Current length is %s' % (
                data_json_length)
            msg = msg.capitalize()
            print('------------%s============' % (msg))
    else:
        ext = '.xlsx'
        # print(listdir(direct))
        file_name = direct + '/' + date + ext
        file_name = path.normpath(file_name)
        # print('here')
        # print('file_name', file_name)
        # print(date, '223.22.2022,---------------')
        create_file(filename=file_name, mode=mode, data=False, date=date)

