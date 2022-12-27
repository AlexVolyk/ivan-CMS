
#! relocate to the above file


from cmath import isnan
import math


main_range = []
for i in range(14):
    main_range.append(i)


def to_lower_case(value):
    return value.lower()


def get_A_N_column(A_N_data, i):
    return A_N_data[i].to_list()


def get_Y_Z_column(Y_Z_data, i):
    return Y_Z_data[i].to_list()


def get_R_S_column(R_S_data, i):
    return R_S_data[i].to_list()


def get_U_V_W_column(U_V_W_data, i):
    return U_V_W_data[i].to_list()


def get_safe_length(arr_number):
    n_arr_number = []
    for i in arr_number:
        if type(i) == str:
            # print(i)
            n_arr_number.append(i)

    return n_arr_number.__len__()


def get_do_safe(values_list, SAFE_LENGTH):
    return values_list[: SAFE_LENGTH]


def get_A_N_data(A_N_data):
    arr_number = []
    arr_type = []
    arr_brand = []

    arr_marked = []

    arr_color = []
    arr_notice = []
    arr_country = []
    arr_size = []
    arr_sm = []
    arr_price = []
    arr_old_price = []

    arr_status = []
    arr_state = []
    arr_extra_notice = []

    headers = {
        'number': 'Номер',
        'type': 'Вид',
        'brand': 'Бренд',

        'marked': 'Маркування',

        'color': 'Колір',
        'notice': 'Примітка',
        'country': 'Країна',
        'size': 'Розмір',
        'sm': 'СМ',
        'price': 'Ціна',
        'old_price': 'Стара ціна',

        'status': 'Статус',
        'state': 'Стан',
        'extra_notice': 'Екстра примітка',
    }

    for i in A_N_data:
        if to_lower_case(str(i)) == to_lower_case(headers['number']):
            arr_number = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['type']):
            arr_type = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['brand']):
            arr_brand = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['marked']):
            arr_marked = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['color']):
            arr_color = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['notice']):
            arr_notice = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['country']):
            arr_country = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['size']):
            arr_size = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['sm']):
            arr_sm = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['price']):
            arr_price = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['old_price']):
            arr_old_price = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['status']):
            arr_status = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['state']):
            arr_state = get_A_N_column(A_N_data, i)

        elif to_lower_case(str(i)) == to_lower_case(headers['extra_notice']):
            arr_extra_notice = get_A_N_column(A_N_data, i)

    # SAFE_LENGTH = get_safe_length(arr_number)
    SAFE_LENGTH = arr_number.__len__()

    arr_number = get_do_safe(arr_number, SAFE_LENGTH)
    # if arr_number.__len__() < 14:
    #     print(arr_number,'number')
    arr_type = get_do_safe(arr_type, SAFE_LENGTH)
    arr_brand = get_do_safe(arr_brand, SAFE_LENGTH)

    arr_marked = get_do_safe(arr_marked, SAFE_LENGTH)

    arr_color = get_do_safe(arr_color, SAFE_LENGTH)
    arr_notice = get_do_safe(arr_notice, SAFE_LENGTH)
    arr_country = get_do_safe(arr_country, SAFE_LENGTH)
    arr_size = get_do_safe(arr_size, SAFE_LENGTH)
    arr_sm = get_do_safe(arr_sm, SAFE_LENGTH)
    arr_price = get_do_safe(arr_price, SAFE_LENGTH)

    arr_old_price = get_do_safe(arr_old_price, SAFE_LENGTH)

    arr_status = get_do_safe(arr_status, SAFE_LENGTH)
    arr_state = get_do_safe(arr_state, SAFE_LENGTH)
    arr_extra_notice = get_do_safe(arr_extra_notice, SAFE_LENGTH)

    # print(arr_price)
    # S_2_total_price = 0
    # for i in arr_price:
    #     if not math.isnan(i):
    #         S_2_total_price += i
    # print(total_price)

    # print(arr_number.__len__(), 'arr_number.__len__()')
    # print(arr_type.__len__(), 'arr_type.__len__()')
    # print(arr_brand.__len__(), 'arr_brand.__len__()')
    # print(arr_marked.__len__(), 'arr_marked.__len__()')

    # print(arr_color.__len__(), 'arr_color.__len__()')
    # print(arr_notice.__len__(), 'arr_notice.__len__()')
    # print(arr_country.__len__(), 'arr_country.__len__()')
    # print(arr_size.__len__(), 'arr_size.__len__()')
    # print(arr_sm.__len__(), 'arr_sm.__len__()')
    # print(arr_price.__len__(), 'arr_price.__len__()')
    # print(arr_old_price.__len__(), 'arr_old_price.__len__()')

    # print(arr_status.__len__(), 'arr_status.__len__()')
    # print(arr_state.__len__(), 'arr_state.__len__()')
    # print(arr_extra_notice.__len__(), 'arr_extra_notice.__len__()')
    # return [
    # arr_number,
    # arr_type,
    # arr_brand,
    # arr_marked,
    # arr_color,
    # arr_notice,
    # arr_country,
    # arr_size,
    # arr_sm,
    # arr_price,
    # arr_old_price,
    # arr_status,
    # arr_state,
    # arr_extra_notice,
    # ]

    A_N_zip = list(
        zip(
            arr_number,
            arr_type,
            arr_brand,
            arr_marked,
            arr_color,
            arr_notice,
            arr_country,
            arr_size,
            arr_sm,
            arr_price,
            arr_old_price,
            arr_status,
            arr_state,
            arr_extra_notice,
        )
    )

    n_A_N_zip = []
    # if A_N_zip.__len__() < 14:
    #     print(A_N_zip,'A_N_zip')
    # print(A_N_zip,'+++++')
    for i in A_N_zip:
        # print(i[0])

        if type(i[0]) == str:
            # print(i[0])
            n_A_N_zip.append(i)

    A_N_zip = n_A_N_zip

    # if A_N_zip.__len__() < 14:
    #     print(A_N_zip,'A_N_zip++')

    S_2_total_price = 0
    # print(A_)
    for i in A_N_zip:
        # print(i,'-----')
        if not math.isnan(i[9]):
            S_2_total_price += i[9]
    
    
    

    Z_5_total_quantity = A_N_zip.__len__()

    return [
        [
            A_N_zip, 
            S_2_total_price, 
            Z_5_total_quantity
        ],
        [
            arr_type,
            arr_brand,
            arr_marked,
            # arr_color,
            arr_country,
            arr_size,
            arr_sm,
            arr_status,
            arr_state,
        ]
    ]


def get_Y_Z_zip(Y_Z_data):
    #! can be intergation about changing [nan] >>> [''](empty string)
    # print(Y_Z_data)
    count = 0
    zip1 = []
    zip2 = []
    for col in Y_Z_data:

        if count == 0:
            zip1 = get_Y_Z_column(Y_Z_data, i=col)
        else:
            zip2 = get_Y_Z_column(Y_Z_data, i=col)
        count += 1

    # print(zip1, 'zip1')
    # print(zip2, 'zip2')
    Z_4_price_of_deliver_and_total_price = 0
    if not math.isnan(zip2[0]) and not math.isnan(zip2[1]):
        a = int(zip2[0]) + int(zip2[1])
        zip2[2] = a
        Z_4_price_of_deliver_and_total_price = a
    Y_Z_zip = list(zip(zip1, zip2))

    n_l = []
    for i in Y_Z_zip:
        n_l.append(list(i))
    Y_Z_zip = n_l
    # print(Y_Z_zip, 'Y_Z_zip')

    return Y_Z_zip, Z_4_price_of_deliver_and_total_price


def get_U_V_W_zip(U_V_W_data):
    #! can be intergation about changing [nan] >>> [''](empty string)
    # print(U_V_W_data)
    count = 0
    zip1 = []
    zip2 = []
    zip3 = []
    for col in U_V_W_data:

        if count == 0:
            zip1 = get_U_V_W_column(U_V_W_data, i=col)
        elif count == 1:
            zip2 = get_U_V_W_column(U_V_W_data, i=col)
        else:
            zip3 = get_U_V_W_column(U_V_W_data, i=col)
        count += 1

    # print(zip1, 'zip1-')
    # print(zip2, 'zip2-')
    # print(zip3, 'zip3-')

    U_V_W_zip = list(zip(zip1, zip2, zip3))
    # print(U_V_W_zip, 'U_V_W_zip')

    n_l = []
    for i in U_V_W_zip:
        n_l.append(list(i))

    U_V_W_zip = n_l
    return U_V_W_zip


def get_R_S(R_S_data):
    count = 0
    zip1 = []
    zip2 = []

    for col in R_S_data:

        if count == 0:
            zip1 = get_R_S_column(R_S_data, i=col)
        else:
            zip2 = get_R_S_column(R_S_data, i=col)
        count += 1

    # print(zip1, 'zip1')
    # print(zip2, 'zip2')

    R_S_zip = list(zip(zip1, zip2))

    n_l = []
    for i in R_S_zip:
        n_l.append(list(i))

    R_S_zip = n_l
    # print(R_S_zip, 'R_S_zip')

    return R_S_zip


def get_main_data(file):
    # print(file.iloc[:9, [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]])
    A_N_data = file.iloc[:, main_range]
    # print(A_N_data, 
    # A_N_data)
    R_S_data = file.iloc[: 11, [17, 18]]
    # print(R_S_data, 'R_S_data')

    U_V_W_data = file.iloc[: 3, [20, 21, 22]]
    # print(U_V_W_data, 'U_V_W_data')

    Y_Z_data = file.iloc[: 4, [24, 25]]
    # print(Y_Z_data, 'Y_Z_data')

    # A_N_data, S_2_total_price, Z_5_total_quantity 
    A_N_response_list = get_A_N_data(A_N_data)
    A_N_major = A_N_response_list[0]
    A_N_minor = A_N_response_list[1]

    A_N_data = A_N_major[0]
    S_2_total_price = A_N_major[1]
    Z_5_total_quantity = A_N_major[2]


    arr_type = A_N_minor[0]
    arr_brand = A_N_minor[1]
    arr_marked = A_N_minor[2]
    # arr_color = A_N_minor[]
    arr_country = A_N_minor[3]
    arr_size = A_N_minor[4]
    arr_sm = A_N_minor[5]
    arr_status = A_N_minor[6]
    arr_state = A_N_minor[7]


    Y_Z_data, Z_4_price_of_deliver_and_total_price = get_Y_Z_zip(Y_Z_data)

    R_S_data = get_R_S(R_S_data)
    U_V_W_data = get_U_V_W_zip(U_V_W_data)
    # print(R_S_data, 'R_S_data')
    # print(U_V_W_data, 'U_V_W_data')

    
    # print()
    # print(Y_Z_data, 'Y_Z_data')
    total_quantity = A_N_data.__len__()
    S_5_sold_price = 0
    S_9_sold_quantity = 0
    for i in A_N_data:
        if i[11] == 'Продано':
            S_9_sold_quantity += 1
            if not math.isnan(i[9]):
                S_5_sold_price += i[9]

    # if A_N_data.__len__() < 14: print(A_N_data,'A_N_data'); print(total_quantity, 'total_quantity')
    Y_Z_data[3][1] = total_quantity

    # print(S_9_sold_quantity, 'S_9_sold_quantity')
    # print(Z_5_total_quantity,'Z_5_total_quantity')


    # print(S_5_sold_price, 'S_5_sold_price')
    # print(S_9_sold_quantity, 'S_9_sold_quantity')

    S_3_proceeds = S_2_total_price - Z_4_price_of_deliver_and_total_price
    S_7_not_sold = S_2_total_price - S_5_sold_price
    S_10_sold_quantity = Z_5_total_quantity - S_9_sold_quantity

    # print(Z_5_total_quantity,'Z_5_total_quantity')
    # print(Z_4_price_of_deliver_and_total_price,'Z_4_price_of_deliver_and_total_price')

    # print(S_2_total_price,'S_2_total_price')
    # print(Z_5_total_quantity,'Z_5_total_quantity')

    V_2 = 0
    V_3 = 0
    if not Z_4_price_of_deliver_and_total_price == 0 and not Z_5_total_quantity == 0:
        V_2 = Z_4_price_of_deliver_and_total_price / Z_5_total_quantity 

    if not S_2_total_price == 0 and not Z_5_total_quantity == 0:
        V_3 = S_2_total_price / Z_5_total_quantity

    V_4 = V_3 - V_2

    W_2 = V_2 * S_9_sold_quantity
    W_3 = V_3 * S_9_sold_quantity
    W_4 = W_3 - W_2

    S_6_real_procceds = S_5_sold_price - W_2

    U_V_W_data[0][1] = V_2
    U_V_W_data[0][2] = W_2
    U_V_W_data[1][1] = V_3
    U_V_W_data[1][2] = W_3
    U_V_W_data[2][1] = V_4
    U_V_W_data[2][2] = W_4

    R_S_data[0][1] = S_2_total_price
    R_S_data[1][1] = S_3_proceeds
    R_S_data[4][1] = S_5_sold_price
    R_S_data[5][1] = S_6_real_procceds
    R_S_data[6][1] = S_7_not_sold
    R_S_data[9][1] = S_9_sold_quantity
    R_S_data[10][1] = S_10_sold_quantity

    # print(R_S_data,'R_S_data')

    # print(U_V_W_data,'U_V_W_data')


    # # print(arr_number.__len__(), 'arr_number.__len__()')
    # # print(arr_type.__len__(), 'arr_type.__len__()')
    # # print(arr_brand.__len__(), 'arr_brand.__len__()')
    # # print(arr_color.__len__(), 'arr_color.__len__()')
    # # print(arr_notice.__len__(), 'arr_notice.__len__()')
    # # print(arr_country.__len__(), 'arr_country.__len__()')
    # # print(arr_size.__len__(), 'arr_size.__len__()')
    # # print(arr_sm.__len__(), 'arr_sm.__len__()')
    # # print(arr_price.__len__(), 'arr_price.__len__()')
    # # print(arr_old_price.__len__(), 'arr_old_price.__len__()')


    return [
        [
            A_N_data,
            R_S_data,
            U_V_W_data,
            Y_Z_data
        ],
        [
            arr_type,
            arr_brand,
            arr_marked,
            # arr_color,
            arr_country,
            arr_size,
            arr_sm,
            arr_status,
            arr_state,
        ]
    ]
