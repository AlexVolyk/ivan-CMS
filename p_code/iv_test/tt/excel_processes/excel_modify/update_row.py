from .help_f import get_letter_with_index


def update_row(ws, data, what_index, what_looking_for):
    d = data
    ws[get_letter_with_index('A', what_index)] = what_looking_for
    ws[get_letter_with_index('B', what_index)] = d['type']
    ws[get_letter_with_index('C', what_index)] = d['brand']
    ws[get_letter_with_index('D', what_index)] = d['marked']
    ws[get_letter_with_index('E', what_index)] = d['color']
    ws[get_letter_with_index('F', what_index)] = d['notice']
    ws[get_letter_with_index('G', what_index)] = d['country']
    ws[get_letter_with_index('H', what_index)] = d['size']
    ws[get_letter_with_index('I', what_index)] = d['sm']
    ws[get_letter_with_index('J', what_index)] = d['price']
    ws[get_letter_with_index('K', what_index)] = d['old_price']
    ws[get_letter_with_index('L', what_index)] = d['status']
    ws[get_letter_with_index('M', what_index)] = d['state']
    ws[get_letter_with_index('N', what_index)] = d['extra_notice']
