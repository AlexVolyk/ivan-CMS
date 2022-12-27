import json
from os import listdir


def get_json():
    # print(listdir('./'))
    json_file = 'v2.json'
    d = './directory_for_json'
    # print(listdir('./excel_processes/parse_excel'),'-------------')
    # p = './excel_processes/parse_excel'
    file = open('%s/%s' % (d,json_file))
    file = json.load(file)
    # file = 'ss'
    return file
    
def get_numbers_for_excel(list_range, extra_plus=1):
    num = []
    plus_num = extra_plus

    for i in range(list_range.__len__()):
        num.append(i+plus_num)
    return num