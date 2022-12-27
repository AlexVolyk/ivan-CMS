from .variables import U_titles, V_W_titles, V_data, W_data
from .set_letters import set_U_titles, set_V, set_W
from .help_f import get_numbers_for_excel


def minor_price_info_U_V_W(sh, mode=False, data=False):
    minor_price_info_length = get_numbers_for_excel(U_titles)
    # print(minor_price_info_length,'minor_price_info_length')
    for i in minor_price_info_length:
        set_U_titles(sh, i, data=U_titles)

        if i == 2:
            sh.write('V'+str(1), V_W_titles[0])
            sh.write('W'+str(1), V_W_titles[1])

        if i > 1:
            set_V(sh, i, data=V_data)
            set_W(sh, i, data=W_data)