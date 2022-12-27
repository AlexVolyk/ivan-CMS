import json
from os import listdir, path


file_open_sign = '~$'
directory_for_search_excel = 'directory_for_parse'
where_to_search = 'excel' #? for parse
parse_extension = '.xlsx'


where_to_save_file = 'directory_for_json'
file_for_json = 'v2.json'


where_to_search_excel = path.join(directory_for_search_excel, where_to_search)
where_to_search_excel = path.normpath(where_to_search_excel)

where_to_search_json = path.join(where_to_save_file, file_for_json)
where_to_search_json = path.normpath(where_to_search_json)

# print(file_for_json,'file_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_jsonfile_for_json')

def init_file():
    ff = open(where_to_search_json, 'w')

    json.dump(init_file_data, ff, indent=4)
    ff.close()








init_file_data = {
    "main_data": [
    ],
    "unique": {
        "arr_type": {
            "data": []
        },
        "arr_brand": {
            "data": []
        },

        "arr_marked": {
            "data": []
        },

        "arr_country": {
            "data": []
        },
        "arr_size": {
            "data": []
        },
        "arr_sm": {
            "data": []
        },

        "arr_status": {
            "data": []
        },
        "arr_state": {
            "data": []
        },

        "arr_date": {
            "data": []
        }
    }
}