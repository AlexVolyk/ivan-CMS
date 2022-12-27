from .run_v1 import run_v1


def messages_wrapper(f):
    first = 'Proccess started parse_json_for_statistic'.capitalize()
    first = '------------%s============\n' % (first)
    print(first)
    
    f()
    
    last = 'Proccess ended parse_json_for_statistic'.capitalize()
    last = '------------%s============\n' % (last)
    print(last)


def v1f():
    f = run_v1
    messages_wrapper(f)
