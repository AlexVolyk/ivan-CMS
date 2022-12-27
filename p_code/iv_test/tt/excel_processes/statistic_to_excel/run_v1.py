from os import mkdir, path, listdir

from .create_file import create_month_file, create_total_file, create_year_file
from .help_f import get_json, message_inner



def run_v1():
    data = get_json()

    if data.__len__() > 0:
        total_statistic_data = data['total_statistic']
        statistic_data = data['statistic']
        # print(data, 'data')


        directory = '../statistic'
        if not path.exists(directory):
            mkdir(directory)
            message_inner('%s folder created' % directory)


        total_statistic_obj = total_statistic_data


        create_total_file(directory, total_statistic_obj)
        message_inner('total_statistic created')



        for i in statistic_data:
            year_statistic_obj = statistic_data[i]['year']

            if not path.exists(directory + '/' + i):
                mkdir(directory + '/' + i)
                message_inner('%s folder created' % i)

            year_path_name_directory = path.join(directory,i)
            create_year_file(year_path_name_directory, i, year_statistic_obj)
            message_inner('%s file created' % i)




            month_statistic_data = statistic_data[i]['month']

            for j in month_statistic_data:
                month_statistic_obj = month_statistic_data[j]

                if not path.exists(year_path_name_directory + '/' + j):
                    mkdir(year_path_name_directory + '/' + j)
                    message_inner('%s folder created' % j)


                create_month_file(year_path_name_directory, j, month_statistic_obj)
                message_inner('%s file created' % j)


        message_inner('statistic files created successfully')

    else:
        message_inner('no objects for statistic')