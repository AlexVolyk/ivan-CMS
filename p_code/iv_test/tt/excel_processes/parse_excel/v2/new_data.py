import math


def new_data(n_data):
    n_data = list(set(n_data))
    data = []
    for i in n_data:
        if type(i) == str or math.isnan(i) == False:

            if type(i) == int or type(i) == float:
                data.append(str(i))

            else:
                if type(i) == str:
                    i = i.strip()
                    data.append(i)

                    # if i.__len__() > 0:
                    # data.append(i)
                else:
                    data.append(i)
    data = list(set(data))
    return data