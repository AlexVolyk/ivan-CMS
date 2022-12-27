import json
from .get_statistic_f import set_month_statistic, set_total_statistic, set_year_statistic
from .help_f import get_json, get_month, get_year, message_inner, save_data_in_json_file


def run_v1():
    json_data = get_json()['main_data']
    statistic = {}

    total_statistic= {}

    statistic_obj = {}

    for i in json_data:
        # print(i['date'])
        # print(i['data'])
        # r_s = i['R_S_data']
        r_s = i['R_S_data']
        y_z = i['Y_Z_data']

        date = i['date']
        year = get_year(date)
        if not year in statistic:
            statistic[year] = {}

            message_inner('%s obj created' % (year))

        month = get_month(date)

        if not 'month' in statistic[year]:
            statistic[year]['month'] = {}

            message_inner('month in year obj created')

            
        if not 'year' in statistic[year]:
            statistic[year]['year'] = {}

            message_inner('year in year obj created')

        
        if not year == 'Старі' and not month in statistic[year]['month']:
            statistic[year]['month'][month] = {}

            message_inner('%s in year >> month obj created' % (month))


        if not year == 'Старі':
            set_month_statistic(statistic, year, month, r_s, y_z)
            pass
        set_year_statistic(statistic, year, r_s, y_z)
        set_total_statistic(total_statistic,r_s, y_z)
    statistic_obj['total_statistic'] = total_statistic
    statistic_obj['statistic'] = statistic


    message_inner('statistic json created successfully')

    save_data_in_json_file(statistic_obj)