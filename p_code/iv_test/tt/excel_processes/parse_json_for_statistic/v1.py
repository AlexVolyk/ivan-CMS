# from create_statistic import create_statistic

# from help_f import get_json
from run_v1 import run_v1


# if __name__ == '__main__':

    # run_v1()
    # create_statistic()
    # # json_data = get_json()['main_data']
    # # total_money = 0
    # ever_valid_bargain = 0  # дійсний виторг +
    # ever_bargain = 0  # виторг +
    # ever_the_rest_of_goods = 0  # залишок товару + (сума)
    # ever_unsold_goods = 0  # залишилось пар + (кількість пар не проданих)
    # ever_sold_goods = 0 # кількість проданих пар

    # ever_sum = 0  # сума
    # ever_sum_of_deliver = 0  # сума доставки
    # ever_total__sum_sum_of_deliver = 0  # сума доставки + сума
    # ever_total_goods = 0 # загальна кількість пар
    #     # print(i['R_S_data'][0]) #Всього
    #     # print(i['R_S_data'][1]) #виторг
    #     # print(i['R_S_data'][4]) #уже продано
    #     # print(i['R_S_data'][5]) #дійсний виторг
    #     # print(i['R_S_data'][6]) #залишок товару
    #     # print(i['R_S_data'][9]) #кількість проданих пар
    #     # print(i['R_S_data'][10]) #залишилось пар

    #     ever_sum += y_z[0][1] if not math.isnan(y_z[0][1]) else 0
    #     ever_sum_of_deliver += y_z[1][1] if not math.isnan(y_z[1][1]) else 0
    #     ever_total__sum_sum_of_deliver += y_z[2][1] if not math.isnan(y_z[2][1]) else 0

    #     # print(i['Y_Z_data'][0]) #сума
    #     # print(i['Y_Z_data'][1]) #сума доставки
    #     # print(i['Y_Z_data'][2]) #всього сума + сума доставки
    #     # print(i['Y_Z_data'][3]) #кількість пар




from .run_v1 import run_v1
def messages_wrapper(f):
    first = 'Proccess started parse_json_for_statistic'.capitalize()
    first = '------------%s============\n' % (first)
    print(first)

    f()
    last = 'Proccess ended parse_json_for_statistic'.capitalize()
    last = '------------%s============\n' % (last)
    
    print(last)
if __name__ == '__main__':
    f = run_v1
    messages_wrapper(f)







#! можна взять данні по рокам
#! можна взять данні по місяцям




