import math

def set_product_heads_from_A_to_N(sh, main_characters, main_titles, main_length, main_head_style):
    first = [1]
    for i in first:
        for j in main_length:
            if i == 1:
                place = main_characters[j-1] + str(i)
                value = main_titles[j-1]
                sh.write(place, value, main_head_style)

def set_from_A_to_N(
                    sh,
                    i,
                    j,
                    data,
                    main_characters,
                    sold_status_style,
                    not_sold_status_style,
                    new_state_style,
                    good_state_style,
                    damaged_state_style,
                    used_state_style,
):
    value = data[i-2][j-1]
    place = main_characters[j-1] + str(i)
    style = None
    if type(value) == float and math.isnan(value) == True:
        value = ''

    if value == 'Продано':
        style = sold_status_style

    elif value == 'Не продано':
        style = not_sold_status_style

    elif value == 'Новий':
        style = new_state_style

    elif value == 'Хороший':
        style = good_state_style

    elif value == 'Вживаний':
        style = used_state_style

    elif value == 'Пошкоджений':
        style = damaged_state_style

    sh.write(place, value, style)

def set_R_titles(sh, i, value):
    place = 'R'+str(i)
    sh.write(place, value)


def set_S(sh, i, profit_style, actual_profit_style, data, title):
    place = 'S'+str(i)
    value = data[i-1]
    if title == 'Виторг':
        sh.write(place, value, profit_style)

    elif title == 'Дійсний виторг':
        sh.write(place, value, actual_profit_style)

    else:
        sh.write(place, value)

def set_U_titles(sh, i, data):
    place = 'U' + str(i)
    value = data[i-1]
    sh.write(place, value)


def set_V(sh, i, data):
    place = 'V'+str(i)
    value = data[i-2]
    sh.write(place, value)


def set_W(sh, i, data):
    place = 'W'+str(i)
    value = data[i-2]
    sh.write(place, value)


def set_Y_titles(sh, i, data):
    sh.write('Y'+str(i), data[i-1])


def set_Z(sh, i, data):
    # print(i, data[i-1])
    place = 'Z'+str(i)
    value = data[i-1]

    if type(value) == float and math.isnan(value): value = ''

    sh.write(place, value)