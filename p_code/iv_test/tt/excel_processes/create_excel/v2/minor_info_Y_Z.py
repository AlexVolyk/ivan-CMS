from .variables import Y_titles, Z_data
from .set_letters import set_Y_titles, set_Z
from .help_f import get_numbers_for_excel


def minor_info_Y_Z(sh, mode=False, data=False, date=False):
    dataa = None
    da = []
    date = date if date else None 

    if data and date and mode:
        dataa = data['Y_Z_data']
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
            is_title = data['Y_Z_data'][0][0] == 'К-сть пар'
            if is_title:
                Z_data[1] = ''

    else:
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
        set_Y_titles(sh, i, data=Y_titles)
        if da:
            set_Z(sh, i, data=da)
