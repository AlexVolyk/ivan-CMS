from .variables import S_data, R_titles
from .set_letters import set_R_titles, set_S
from .help_f import get_numbers_for_excel


def main_price_info_R_S(sh, mode=False, data=False, profit_style=None, actual_profit_style=None):

    d = S_data
    main_price_info_length = get_numbers_for_excel(R_titles)


    for i in main_price_info_length:
        value = R_titles[i-1]
        set_R_titles(sh, i, value)
        set_S(sh, i, profit_style, actual_profit_style, data=d, title=value)
