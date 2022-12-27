import json
import math
from os import listdir, path, remove


def message_inner(msg):
    msg = '------------%s============\n' % (msg)
    print(msg)

def get_json():
    # print(listdir('.'))
    # l_d = listdir('./excel_processes/parse_excel')
    # print(l_d)
    p = './directory_for_json/v2.json'

    # p = 'v2.json'
    f = open(p, 'r')
    json_data = json.load(f)
    f.close()
    # print(json_data)
    return json_data

def save_data_in_json_file(statistic_obj):
    # p = 'statistic.json'
    p = './directory_for_json/statistic.json'
    if path.exists(p):
        remove(p)
    f = open(p, 'w')
    # data = json.load(statistic_obj)
    json.dump(statistic_obj, f, indent=4)
    f.close()


def get_month(date):
    month = str(date)
    if not month == 'Старі':
        month = month.split(' ')[0]
        month = month.split('.')
        # print(month)
        month = month[1]


    return month


def get_year(date):
    year = str(date)
    # print(year,'year')
    year = year.split(' ')[0]
    # print(year)
    # print(year.split('.'))
    # print(year.split('.')[])
    year = year.split('.')
    year = year[year.__len__() - 1]

    return year

def validate_nan_or_not(value):
    return value if not math.isnan(value) else 0