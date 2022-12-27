from parse_excel.v2f import v2f as parse_f
from create_excel.v2f import v2f as create_f


# def messages_wrapper(f1,f2):
    # first = 'Proccess started parse_create'.capitalize()
    # first = '------------%s============\n' % (first)
    # f1()
    # f2()
    # last = 'Proccess ended parse_create'.capitalize()
    # last = '------------%s============\n' % (last)

if __name__ == '__main__':
    # msg = 'Proccess started'.capitalize()
    # msg = '------------%s============' % (msg)
    # print('aboba')
    # f1 = parse_f
    # f2 = create_f
    # messages_wrapper(f1,f2)
    parse_f()
    create_f()
    # run_v2()