import json
from os import listdir



def message_inner(msg):
    msg = '------------%s============\n' % (msg)
    print(msg)

def get_json():
    p = './directory_for_json/statistic.json'
    f = open(p, 'r')
    json_data = json.load(f)
    f.close()
    return json_data