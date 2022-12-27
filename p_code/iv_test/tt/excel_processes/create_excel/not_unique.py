
import json
from os import listdir

# print(listdir('../p_code/directory_for_json/v2.json'))
p = '../p_code/directory_for_json/v2.json'
file = open(p)

# file = open('../pandas xlsl/data.json')
file = json.load(file)

main_data = file['main_data']

print('start')


testData = [
    {
        'data': [
            ['22']
        ],
        'date': 'd1'
    },
    {
        'data': [
            ['22']
        ],
        'date': 'd2'
    },
    {
        'data': [
            ['1']
        ],
        'date': 'd3'
    },
    {
        'data': [
            ['22']
        ],
        'date': 'd5'
    }
]


not_unique = {}

for i in main_data:

    for j in i['data']:
        num = j[0]
        if num in not_unique:
            not_unique[num].append(i['date'])
        else: 
            not_unique[num] = [i['date']]

for i in not_unique:
    if not_unique[i].__len__() > 1:
        print(not_unique[i], i)

print('end')
