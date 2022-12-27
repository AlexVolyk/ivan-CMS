from .run_v1 import run_v1



def messages_wrapper(f):
    first = 'Proccess started statistic_to_excel'.capitalize()
    first = '------------%s============\n' % (first)
    print(first)

    f()

    last = 'Proccess ended statistic_to_excel'.capitalize()
    last = '------------%s============\n' % (last)
    print(last)


if __name__ == '__main__':
    f = run_v1
    messages_wrapper(f)