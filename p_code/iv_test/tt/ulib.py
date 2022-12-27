# import json
# import math
from os import listdir, makedirs, path

from .excel_processes.create_excel.v2.run_v2 import run_v2
from .excel_processes.excel_modify.modify_f import add_f, remove_f
# from tt.models import Type, Brand, Marked, Country, Size, Sm, Status, State, Extra_notice, Date, Footwear 


def get_year(string):
    year = str(string).split(' ')
    year = year[0]
    year = year.split('.')
    year = year[year.__len__() - 1] if year.__len__() > 0 else year[0]

    return year

def create_year_direction(root_dir, year):
    makedirs(root_dir+'/'+ year)


def get_data_obj(
    number,
    type_p,
    brand,
    marked,
    color,
    notice,
    country,
    size,
    sm,
    price,
    old_price,
    status,
    state,
    extra_notice,
    date,
    ):
    type_p = type_p.name if not type_p == None else None
    brand = brand.name if not brand == None else None
    country = country.name if not country == None else None
    size = size.size if not size == None else None
    sm = sm.sm if not sm == None else None
    date = date.date if not date == None else None
    marked = marked.name if not marked == None else None
    status = status.name if not status == None else None
    state = state.name if not state == None else None


    data = {
    'number': number,
    'type': type_p,
    'brand': brand,
    'marked': marked,
    'color': color,
    'notice': notice,
    'country': country,
    'size': size,
    'sm': sm,
    'price': price,
    'old_price': old_price,
    'status': status,
    'state': state,
    'extra_notice': extra_notice,
    'date': date
}
    # print(data)
    return data
        

def create_or_add_date_folder_file(date):
    # print(date, 'date')
    # print('++++++++++++++++', listdir('./'))

    # print('----------------', listdir('../'))

    root_dir = '../excel'
    date_name = date
    
    # print(path.exists('../excel'))

    excel_list = listdir(root_dir)
    year = get_year(date_name)
    # print(year)
    if not year in excel_list:
        # print('directory not exists')
        # print('creating directory and file')
        
        create_year_direction(root_dir, year)
        direct = path.join(root_dir, year)
        create_file(date=date_name, direct=direct)
        pass

    else:
        # print('creating file in directory')
        direct = path.join(root_dir, year)
        # print(listdir(direct),'----')
        if not date_name + '.xlsx' in listdir(direct):
            # print('noo')
            create_file(date=date_name, direct=direct)
        pass



def create_file(date, direct):
    run_v2(create_one=True, date=date, direct=direct, mode=False)
    # print('create .xlsx file file headers for files')



def add_update_row(data):
    # print(data)
    # raise Exception("Sorry, bruh. you are excuse")
    root_dir = '../excel'
    what_looking_for = data['number']
    date = data['date']
    year = get_year(date)

    name = path.join(root_dir, year, date)
    name = name + '.xlsx'
    name = path.normpath(name)
    add_f(
        name=name,
        what_looking_for=what_looking_for,
        data=data
        )
    pass


def remove_by_number(number, date):
    year = get_year(date)
    root_dir = '../excel'
    what_looking_for = number

    # print(year)
    # print(date)
    name = path.join(root_dir, str(year), str(date))
    print(name)

    name = name + '.xlsx'
    # print(name)

    name = path.normpath(name)
    # print(name)
    remove_f(name=name, what_looking_for=what_looking_for)
    pass




