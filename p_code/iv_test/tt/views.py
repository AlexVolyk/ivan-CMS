import math
from os import listdir
from django.shortcuts import render, HttpResponse
import json
# from .ulib import init_products, init_unique

from .models import Brand, Country, Date, Footwear, Size, Sm, Type, Marked, Status, State
# Create your views here.
# print(listdir('.'))


def addd(request):
    init_unique()

    # print()
    return HttpResponse('addd')




# def addp(request):
#     return HttpResponse('pass')


def addp(request):
    init_products()


    return HttpResponse('addp')






def init_unique():
    # print(listdir())
    p = './directory_for_json/v2.json'
    file = open(p)

    # file = open('./v2.json')
    file = json.load(file)
    f = file['unique']

    type_p = f['arr_type']['data']
    for t in type_p:
        # print(t)
        Type.objects.create(name=t)

    brands = f['arr_brand']['data']
    for b in brands:
        Brand.objects.create(name=b)

    marked = f['arr_marked']['data']
    for m in marked:
        Marked.objects.create(name=m)

    countries = f['arr_country']['data']
    for c in countries:
        Country.objects.create(name=c)

    sizes = f['arr_size']['data']
    for s in sizes:
        Size.objects.create(size=s)

    sms = f['arr_sm']['data']
    for s in sms:
        Sm.objects.create(sm=s)
    
    status = f['arr_status']['data']
    for s in status:
        Status.objects.create(name=s)


    state = f['arr_state']['data']
    for s in state:
        State.objects.create(name=s)


    dates = f['arr_date']['data']
    for d in dates:
        # print(d,'d')
        Date.objects.create(date=d)

def init_products():
    p = './directory_for_json/v2.json'
    file = open(p)
    # file = open('./v2.json')
    file = json.load(file)
    ff = file['main_data']
    fa = ff
    for i in fa:

        for j in i['data']:

            number = j[0]
            # print(number,'numbernumbernumbernumbernumbernumbernumber')
            # print(i['date'],"i['date']i['date']i['date']i['date']")

            # print(j[1],'j[1]j[1]j[1]j[1]j[1]j[1]j[1]j[1]j[1]j[1]')

            type_p = j[1].strip() if type(j[1]) == str else None
            brand = j[2].strip() if  type(j[2]) == str else None
            marked = j[3].strip() if  type(j[3]) == str else None
            color = j[4] if  type(j[4]) == str else None
            notice = j[5] if  type(j[5]) == str else None
            # print(j[5],'==============')
            if type(j[6]) == str:
                # print(j[6],'-------------------', type(j[6]))
                j[6] = str(j[6]).strip()
            else:
                j[6] = None
            country = j[6]
            # country = j[5] if math.isnan(j[5]) == False else None
            # size = j[6] if math.isnan(j[6]) == False else None
            if type(j[7]) == int:
                j[7] = str(j[7]).strip()
            elif type(j[7]) == str:
                # print(j[7],'-------------------', type(j[7]))
                j[7] = str(j[7]).strip()
            else:
                j[7] = None
            size = j[7]
            # print(j[7],'j[7]')
            # if type(j[7]) == int:
            #     # j[7] = j[7].strip()
            #     j[7] = str(j[7])
            # print(j[7],'j[7]j[7]j[7]j[7]j[7]j[7]j[7]j[7]j[7]j[7]')

            if type(j[8]) == int:
                j[8] = str(j[8]).strip()
            elif type(j[8]) == str:
                # print(j[8],'-------------------', type(j[8]))
                j[8] = str(j[8]).strip()
            else:
                j[8] = None
            sm = j[8]

            # sm = j[7] if math.isnan(j[7]) == False else None
            # print(j[11],'====')
            price = j[9] if math.isnan(j[9]) == False else None
            old_price = j[10] if math.isnan(j[10]) == False else None
            status = j[11]
            state = j[12]
            extra_notice = j[13] if type(j[13]) == str else None
            date = i['date'] if type(i['date']) == str else None

            # print('----')
            # print(number)
            # print(type_p)
            # print(brand)
            # print(marked)
            # print(color)
            # print(notice)
            # print(country)

            # print(size)
            # print(sm)
            # print(price)
            # print(old_price)
            # print(status)
            # print(state)
            # print(extra_notice)
            # print('====')



            ft = Footwear()
            ft.number = number

            if type_p is not None:
                ft.type_p = Type.objects.get(name=type_p)

            if brand is not None:
                ft.brand = Brand.objects.get(name=brand)

            if marked is not None:
                ft.marked = Marked.objects.get(name=marked)

            if color is not None:
                ft.color = color

            if notice is not None:
                ft.notice = notice

            if country is not None:
                ft.country = Country.objects.get(name=country)

            if size is not None:
                ft.size = Size.objects.get(size=size)

            if sm is not None:
                ft.sm = Sm.objects.get(sm=sm)

            if price is not None:
                ft.price = price

            if old_price is not None:
                ft.old_price = old_price

            if status is not None:
                ft.status = Status.objects.get(name=status)

            if state is not None:
                ft.state = State.objects.get(name=state)

            if extra_notice is not None:
                ft.extra_notice = Extra_notice.objects.get(name=extra_notice)

            if date is not None:
                ft.date = Date.objects.get(date=date)
            ft.save()