from ..v2.new_data import new_data



def format_main_data(data, A_N_data, file_name_date, R_S_data, U_V_W_data, Y_Z_data):
    data['main_data'].append({
        'data': A_N_data,
        'date': file_name_date,
        # 'date': sheet,
        'R_S_data': R_S_data,
        'U_V_W_data': U_V_W_data,
        'Y_Z_data': Y_Z_data,
    })
    return data


def format_unique_data(data, file_name_date, arr_type, arr_brand, arr_marked, arr_country, arr_size, arr_sm, arr_status, arr_state):
    types = data['unique']['arr_type']['data']
    brands = data['unique']['arr_brand']['data']

    marked = data['unique']['arr_marked']['data']

    countries = data['unique']['arr_country']['data']
    sizes = data['unique']['arr_size']['data']
    sms = data['unique']['arr_sm']['data']

    status = data['unique']['arr_status']['data']
    state = data['unique']['arr_state']['data']


    file_name_date = [file_name_date]
    date = data['unique']['arr_date']['data']


    data['unique']['arr_type']['data'] = new_data(types + arr_type)
    data['unique']['arr_brand']['data'] = new_data(brands + arr_brand)

    data['unique']['arr_marked']['data'] = new_data(marked + arr_marked)

    data['unique']['arr_country']['data'] = new_data(countries + arr_country)
    data['unique']['arr_size']['data'] = new_data(sizes + arr_size)
    data['unique']['arr_sm']['data'] = new_data(sms + arr_sm)

    data['unique']['arr_status']['data'] = new_data(status + arr_status)
    data['unique']['arr_state']['data'] = new_data(state + arr_state)

    data['unique']['arr_date']['data'] = new_data(date + file_name_date)
    return data
