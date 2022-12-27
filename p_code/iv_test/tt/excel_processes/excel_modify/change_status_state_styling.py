from .help_f import get_letter_with_index
from .styling_f import get_sold_or_not_styles, get_product_evaluation_styles

def change_status_state_styling(ws, what_index_2):
    L_column_and_index = get_letter_with_index('L', what_index_2)
    value_sold_unsold = ws[L_column_and_index].value
    L_bg_style, L_color_style, L_is_found = get_sold_or_not_styles(value_sold_unsold)

    M_column_and_index = get_letter_with_index('M', what_index_2)
    value_product_evaluation = ws[M_column_and_index].value
    M_bg_style, M_color_style, M_is_found = get_product_evaluation_styles(value_product_evaluation)


    if L_is_found:
        ws[L_column_and_index].fill = L_bg_style
        ws[L_column_and_index].font = L_color_style


    if M_is_found:
        ws[M_column_and_index].fill = M_bg_style
        ws[M_column_and_index].font = M_color_style

