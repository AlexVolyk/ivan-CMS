# from parse_json_for_statistic import v1f as parse_for_statistic
from parse_json_for_statistic.v1f import v1f as parse_for_statistic
from statistic_to_excel.v1f import v1f as statistic_excel

if __name__ == '__main__':
    parse_for_statistic()
    statistic_excel()
