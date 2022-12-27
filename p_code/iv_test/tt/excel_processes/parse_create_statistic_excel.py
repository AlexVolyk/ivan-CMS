from parse_excel.v2f import v2f as parse_f
from create_excel.v2f import v2f as create_f


from parse_json_for_statistic.v1f import v1f as parse_for_statistic
from statistic_to_excel.v1f import v1f as statistic_excel

if __name__ == '__main__':
    #? create json excel for creatin excel with data
    parse_f()
    create_f()

    #? create statistic json from json for excel for creatin statistic excel
    parse_for_statistic()
    statistic_excel()