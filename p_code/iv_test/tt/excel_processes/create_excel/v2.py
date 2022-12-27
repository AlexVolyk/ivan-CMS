# from .v2.run_v2 import run_v2
from v2.run_v2 import run_v2

def messages_wrapper(f):
    first = 'Proccess started create_excel'.capitalize()
    first = '------------%s============\n' % (first)
    print(first)
    
    f()
    
    last = 'Proccess ended create_excel'.capitalize()
    last = '------------%s============\n' % (last)
    print(last)


def v2f():
    f = run_v2
    messages_wrapper(f)


if __name__ == '__main__':
    f = run_v2
    messages_wrapper(f)
    # msg = 'Proccess started'.capitalize()
    # msg = '------------%s============' % (msg)
    # print(msg)
    # run_v2()