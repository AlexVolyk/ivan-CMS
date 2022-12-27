import json
from os import listdir
import pandas as pd


from ..v2.format_json import format_main_data, format_unique_data
from ..v2.get_main_data import get_main_data
from ..v2.file_data import file_for_json, where_to_search_json

def file_read_write(path_normalize, file_name_date):
    file = pd.read_excel(path_normalize)
    get_main_data_VARIABLES = get_main_data(file)

    major_data = get_main_data_VARIABLES[0]
    minor_data = get_main_data_VARIABLES[1]

    A_N_data = major_data[0]
    R_S_data = major_data[1]
    U_V_W_data = major_data[2]
    Y_Z_data = major_data[3]

    arr_type = minor_data[0]
    arr_brand = minor_data[1]
    arr_marked = minor_data[2]
    # arr_color = minor_data[1]
    arr_country = minor_data[3]
    arr_size = minor_data[4]
    arr_sm = minor_data[5]
    arr_status = minor_data[6]
    arr_state = minor_data[7]

    # print('../'+file_for_json,'file_for_json')
    # print(listdir('./parse_excel'))
    with open(where_to_search_json, "r+") as fi:

        data = json.load(fi)
        # print(data)
        data = format_main_data(
            data,
            A_N_data,
            file_name_date,
            R_S_data,
            U_V_W_data,
            Y_Z_data
        )

        # print(file_name_date,'========')
        data = format_unique_data(
            data,
            file_name_date,
            arr_type,
            arr_brand,
            arr_marked,
            arr_country,
            arr_size,
            arr_sm,
            arr_status,
            arr_state
        )

        data.update()
        fi.seek(0)
        json.dump(data, fi, indent=4)
        fi.close()
