# get_number
from .set_letters import set_product_heads_from_A_to_N, set_from_A_to_N
# get_numbers_for_excel
from .help_f import get_numbers_for_excel
from .variables import main_characters, main_titles
# set_product_heads_from_A_to_N


def set_main(
    sh,
    mode=False,
    data=False,
    main_head_style=False,
    sold_status_style=False,
    not_sold_status_style=False,
    new_state_style=False,
    good_state_style=False,
    damaged_state_style=False,
    used_state_style=False,
):
    main_length = get_numbers_for_excel(main_characters)

    set_product_heads_from_A_to_N(
        sh, main_characters, main_titles, main_length, main_head_style)

    if mode and data:
        data = data['data']

        extra_plus = 2
        data_length = get_numbers_for_excel(data, extra_plus)
        # print('-----------------------',data, '=====================')
        # print('-----------------------',data.__len__(), '=====================')

        for i in data_length:
            # print(data)
            # data[i-2].insert(3, '')
            # data[i-2].append('Продано')
            # data[i-2].append('Хороший')
            # data[i-2].append('хороший бо чоткий')
            # print(data_length, '****************************')
            # print(data_length.__len__(), '****************************')

            for j in main_length:
                # print(data[i], '====data[i]====')
                # print(data[i-2], '====data[i-2][j-1]====')
                set_from_A_to_N(
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
                    )
