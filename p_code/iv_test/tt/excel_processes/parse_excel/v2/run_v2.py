from os import listdir, path

from ..v2.file_read_write import file_read_write
from ..v2.file_data import init_file, file_open_sign, parse_extension, where_to_search_excel


def run_v2():

    # print(listdir('./directory_for_parse'),'===================')
    # print(listdir('../directory_for_parse'))
    # print(listdir('.'))
    # print(where_to_search_excel,'where_to_search_excel', listdir(where_to_search_excel),'------------')
    if path.exists(where_to_search_excel):
            list_dir = listdir(where_to_search_excel)
            
            # print(list_dir)
            # print(listdir('./excel_processes/parse_excel/excel2'),'-----------------')
            # print(where_to_search)
            if list_dir.__len__() > 0:
                msg = 'initialization of json file started parse_excel'
                print('------------%s============' % (msg))
                
                init_file()

                msg = 'initialization of json ended file parse_excel'
                print('------------%s============' % (msg))

                msg = 'STARTED parsing parse_excel'
                print('------------%s============' % (msg))
                for i in list_dir:
                    # print
                    p = "%s/%s" % (where_to_search_excel, i)
                    nest_directory = listdir(p)
                    for j in nest_directory:

                        file_name_date = j.replace(parse_extension, '')
                        file_name_date = file_name_date.strip()
                        # print(i,'i')
                        # print(j,'j')
                        # print(file_name_date,'file_name_date')

                        path_to_file = path.join(p, j)
                        print(path_to_file,'---')
                        if not file_open_sign in path_to_file and parse_extension in path_to_file:
                            # print(path.normpath(path_to_file))
                            path_normalize = path.normpath(path_to_file)
                            file_read_write(path_normalize, file_name_date)
                            
                msg = 'DONE parsing parse_excel'
                print('------------%s============' % (msg))

            else:
                msg = 'directory [%s] has 0 directory parse_excel' % (where_to_search_excel)
                print('------------%s============' % (msg))

    else:
        msg = 'directory [%s] not exists parse_excel' % (where_to_search_excel)
        print('------------%s============' % (msg))