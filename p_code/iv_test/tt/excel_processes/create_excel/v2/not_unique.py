
import json
from os import listdir

# print(
# listdir('./directory_for_json/v222.json')
# )
p = 'directory_for_json/v222.json'
file = open(p)

# file = open('../pandas xlsl/data.json')
file = json.load(file)

main_data = file['main_data']


not_unique = {}

for i in main_data:

    for j in i['data']:
        num = j[0]
        print(j)
        if num in not_unique:
            not_unique[num].append(i['date'])
        else: 
            not_unique[num] = [i['date']]

for i in not_unique:
    if not_unique[i].__len__() > 1:
        print(not_unique[i], i,'===========')
        pass
