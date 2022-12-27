import math
# from unittest.mock import NonCallableMock
# import pandas as pd
import xlsxwriter as xlsw
from os import makedirs, path
# import openpyxl as opxl


from help_f import get_json, get_numbers_for_excel
from paths_f import get_date_for_directory, is_directory_exists, is_file_exists
# from variables import S_data, U_titles, main_characters, main_titles, O_titles, V_W_titles, S_titles, Y_titles, V_data, W_data, Z_data, Q_data
from variables import main_characters, main_titles, R_titles, S_data, U_titles, V_W_titles, V_data, W_data,  Y_titles, Z_data



def set_product_heads(sh, main_length, main_head_style):
    first = [1]
    for i in first:
        for j in main_length:
            if i == 1:
                place = main_characters[j-1] + str(i)
                value = main_titles[j-1]
                sh.write(place, value, main_head_style)


def set_main(sh, mode=False, data=False, main_head_style=None):
    main_length = get_numbers_for_excel(main_characters)

    set_product_heads(sh, main_length, main_head_style)

    if mode and data:
        # data = data[1]['data']
        data = data['data']

        extra_plus = 2
        data_length = get_numbers_for_excel(data, extra_plus)
        # print('-----------------------',data, '=====================')
        # print('-----------------------',data.__len__(), '=====================')


        for i in data_length:

            data[i-2].insert(3, '')
            data[i-2].append('Продано')
            data[i-2].append('Хороший')
            data[i-2].append('хороший бо чоткий')
            # data[i] = 
            # print(data_length, '****************************')
            # print(data_length.__len__(), '****************************')

            for j in main_length:
                # print(data[i], '====data[i]====')
                # print(data[i-2], '====data[i-2][j-1]====')

                # value = NonCallableMock
                # print(i, j)
                value = data[i-2][j-1]

                # print(value, '----------value----------')
                # print(i,'iiiiiiiiiiiii')
                # print(j,'jjjjjjjjjjjjj')
                # print(data[j-1],'[j-1][j-1][j-1][j-1][j-1][j-1]')
                # print(data[i-2],'[i-2][i-2][i-2][i-2][i-2][i-2]')

                # value = data[i-2][j-1]
                # print(value, '----------value----------')

                # if j == main_length.__len__():
                #     if i % 2 == 0:
                #         value = 'Не продано'
                #     else:
                #         value = 'Продано'
                # else:
                #     print(value, '----------value----------')
                #     print(i,'iiiiiiiiiiiii')
                #     # print(data[j-1],'[j-1][j-1][j-1][j-1][j-1][j-1]')
                #     print(data[i-2],'[i-2][i-2][i-2][i-2][i-2][i-2]')

                #     print(j,'jjjjjjjjjjjjj')
                #     value = data[i-2][j-1]
                # print(value, '----------value----------')
                    

                place = main_characters[j-1] + str(i)
                if type(value) == float and math.isnan(value) == True:
                    value = ''
                sh.write(place, value)


# def set_main(sh, mode=False, data=False, main_head_style=None):
#     main_length = get_numbers_for_excel(main_characters)
#     first = [1]
#     for i in first:
#         for j in main_length:
#             if i == 1:
#                 place = main_characters[j-1] + str(i)
#                 value = main_titles[j-1]
#                 sh.write(place, value, main_head_style)

#     if mode and data:
#         # data = data[1]['data']
#         data = data['data']

#         extra_plus = 2
#         data_length = get_numbers_for_excel(data, extra_plus)

#         for i in data_length:
#             for j in main_length:
#                 value = NonCallableMock
#                 if j == main_length.__len__():
#                     if i % 2 == 0:
#                         value = 'Не продано'
#                     else:
#                         value = 'Продано'
#                 else:
#                     value = data[i-2][j-1]
#                 place = main_characters[j-1] + str(i)
#                 if type(value) == float and math.isnan(value) == True:
#                     value = ''
#                 sh.write(place, value)


# def main_price_info_O_Q(sh, mode=False, data=False, profit_style=None, actual_profit_style=None):
#     d = Q_data

#     main_price_info_length = get_numbers_for_excel(O_titles)

#     for i in main_price_info_length:
#         place = 'O'+str(i)
#         value = O_titles[i-1]
#         sh.write(place, value)
#         # if mode:
#         set_Q(sh, i, profit_style, actual_profit_style, data=d, title=value)

def main_price_info_R_S(sh, mode=False, data=False, profit_style=None, actual_profit_style=None):
    # d = Q_data

    d = S_data
    main_price_info_length = get_numbers_for_excel(R_titles)

    for i in main_price_info_length:
        place = 'R'+str(i)
        value = R_titles[i-1]
        # print(value)
        sh.write(place, value)
        # if mode:
        # set_Q(sh, i, profit_style, actual_profit_style, data=d, title=value)
        set_S(sh, i, profit_style, actual_profit_style, data=d, title=value)



# def set_Q(sh, i, profit_style, actual_profit_style, data, title):
#     place = 'Q'+str(i)
#     value = data[i-1]
#     if title == 'Виторг':
#         sh.write(place, value, profit_style)

#     elif title == 'Дійсний виторг':
#         sh.write(place, value, actual_profit_style)

#     else:
#         sh.write(place, value)

def set_S(sh, i, profit_style, actual_profit_style, data, title):
    place = 'S'+str(i)
    value = data[i-1]
    # print(value)
    if title == 'Виторг':
        sh.write(place, value, profit_style)

    elif title == 'Дійсний виторг':
        sh.write(place, value, actual_profit_style)

    else:
        sh.write(place, value)


# def minor_price_info_S_V_W(sh, mode=False, data=False):
#     minor_price_info_length = get_numbers_for_excel(S_titles)
#     # print(minor_price_info_length,'minor_price_info_length')
#     for i in minor_price_info_length:
#         place = 'S' + str(i)
#         value = S_titles[i-1]
#         sh.write(place, value)
#         if i == 2:
#             sh.write('V'+str(1), V_W_titles[0])
#             sh.write('W'+str(1), V_W_titles[1])

#         # if mode and i > 1:
#         if i > 1:
#             set_V(sh, i)
#             set_W(sh, i)

def minor_price_info_U_V_W(sh, mode=False, data=False):
    minor_price_info_length = get_numbers_for_excel(U_titles)
    # print(minor_price_info_length,'minor_price_info_length')
    for i in minor_price_info_length:
        place = 'U' + str(i)
        value = U_titles[i-1]
        sh.write(place, value)
        if i == 2:
            sh.write('V'+str(1), V_W_titles[0])
            sh.write('W'+str(1), V_W_titles[1])

        # if mode and i > 1:
        if i > 1:
            set_V(sh, i)
            set_W(sh, i)


def set_V(sh, i):
    place = 'V'+str(i)
    value = V_data[i-2]
    sh.write(place, value)


def set_W(sh, i):
    place = 'W'+str(i)
    value = W_data[i-2]
    sh.write(place, value)


# * DONE
def minor_info_Y_Z(sh, mode=False, data=False, date=False):
    # print(data[1].keys())
    dataa = None
    date = date if date else None 
    da = []

    if data and date and mode:
        # date = data[1]['date']
        # dataa = data[1]['M_N_info']
        dataa = data['M_N_info']
        # print(dataa, '------------b\n')

        dataa = list(dataa[0:3])


        dataa = [['', date]] + dataa
        # print(date)
        c = 0
        # print(dataa, '------------a\n')
        while c < 3:
            Z_data[c] = dataa[c][1]
            c += 1
        if date == 'Старі':
            if data['M_N_info'][0][0] == 'К-сть пар':
                Z_data[1] = ''

    else:
        # print('teher')
        c = 0
        while c < 3:
            if c == 0:
                Z_data[c] = date
            else:
                Z_data[c] = ''
            c += 1


    minor_info_length = get_numbers_for_excel(Y_titles)

    da = Z_data
    # print(da, 'da')
    for i in minor_info_length:
        sh.write('Y'+str(i), Y_titles[i-1])
        if da:
            set_Z(sh, i, data=da)


def set_Z(sh, i, data):
    # print(i, data[i-1])
    place = 'Z'+str(i)
    value = data[i-1]

    if type(value) == float and math.isnan(value): value = ''

    sh.write(place, value)


def init_fields(sh, mode, data, date, main_head_style, profit_style, actual_profit_style):
    # if mode:
    #     json_data = get_json()['main_data']
    #     data = json_data
        # print(json_data[0]['date'])
    main_price_info_R_S(sh, mode, data, profit_style, actual_profit_style)
    minor_price_info_U_V_W(sh, mode, data)



    set_main(sh, mode, data, main_head_style)
    minor_info_Y_Z(sh, mode, data, date)

    # main_price_info_O_Q(sh, mode, data, profit_style, actual_profit_style)
    # minor_price_info_S_V_W(sh, mode, data)


def create_file(filename, mode, data, date):
    wb = xlsw.Workbook(filename)
    sh = wb.add_worksheet()

    main_head_style = wb.add_format()
    profit_style = wb.add_format()
    actual_profit_style = wb.add_format()


    main_head_style.set_bg_color('#FFC000')
    profit_style.set_bg_color('#00B050')
    actual_profit_style.set_bg_color('#92D050')

    init_fields(
        sh,
        mode,
        data,
        date,
        main_head_style,
        profit_style,
        actual_profit_style
    )

    wb.close()




json_file = 'data'
data = get_json(json_file)
data = data['main_data']



mode = True
directory = 'excel'
if not path.exists(directory):
    makedirs(directory)

for i in data:
    name = i['date']
    n = get_date_for_directory(name)
    d = directory + '/' + n
    is_directory = is_directory_exists(d)
    if not is_directory:
        makedirs(d)
    file_name, is_file = is_file_exists(name, directory=d)
    if not is_file:
        data = i
        date = name
        create_file(filename=file_name, mode=mode, data=data, date=date)