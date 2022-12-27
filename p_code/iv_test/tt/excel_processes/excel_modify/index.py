from openpyxl import Workbook, load_workbook
from change_status_state_styling import change_status_state_styling
from help_f import get_index_and_is_found, get_letter_with_index

from update_row import update_row



ext = '.xlsx'
name = '03.05.2022'
name = name + ext










# data = {
#     'number': '#05111',
#     'type': 'ванюшка',
#     'brand': 'ванюшка',
#     'marked': 'ванюшка',
#     'color': 'ванюшка',
#     'notice': 'ванюшка',
#     'country': 'ванюшка',
#     'size': 'ванюшка',
#     'sm': 'ванюшка',
#     'price': 'ванюшка',
#     'old_price': 'ванюшка',
#     'status': 'Не продано',
#     'state': 'Вживаний',
#     'extra_notice': 'ванюшка'
# }
data = {
    'number': '#05112',
    'type': 'ванюшка',
    'brand': 'ванюшка',
    'marked': 'ванюшка',
    'color': 'ванюшка',
    'notice': 'ванюшка',
    'country': 'ванюшка',
    'size': 'ванюшка',
    'sm': 'ванюшка',
    'price': 'ванюшка',
    'old_price': 'ванюшка',
    'status': 'Не -',
    'state': '--',
    'extra_notice': 'ванюшка'
}



if __name__ == "__main__":
    # remove_f(name=name, what_looking_for='#0511')
    # add_f(name=name, what_looking_for='#05112', data=data)
    pass