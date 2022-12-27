from .v2.run_v2 import run_v2


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