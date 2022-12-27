def get_index_and_is_found( what_looking_for, list_of_A_column):
    what_index = 1
    is_found = False
    for i in list_of_A_column:
        i_v = i.value
        # print(i,'i')
        # print(i_v,'i_v')
        # print(i.value)
        if i_v == what_looking_for:
            # print(what_index,'what_index-----')
            # print(i.value)
            # print(i)
            is_found = True
            break
        what_index += 1

    return what_index, is_found


def is_row_empty(list_of_A_column):
    what_index = 2
    is_empty = False
    for i in list_of_A_column[1:]:
        i_v = i.value
        # print(i,'i')
        # print(i_v,'i_v')
        # print(i.value)
        if i_v == None:
            # print('aboba-----------------------')
            # print(what_index,'what_index-----')
            # print(i.value)
            # print(i)
            is_empty = True
            break
        if what_index == 12: break
        what_index += 1
# 12
    return what_index, is_empty

def is_row_not_empty_before_12( what_looking_for, list_of_A_column):
    what_index = 2
    is_not_empty = False
    for i in list_of_A_column[1:]:
        i_v = i.value
        # print(i,'i')
        # print(i_v,'i_v')
        # print(i.value)
        if i_v == what_looking_for:
            # print('aboba-----------------------')
            # print(what_index,'what_index-----')
            # print(i.value)
            # print(i)
            is_not_empty = True
            break
        if what_index == 12: break
        what_index += 1
# 12
    return what_index, is_not_empty


def get_letter_with_index(letter, index):
    return letter.upper() + str(index)