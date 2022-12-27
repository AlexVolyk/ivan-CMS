import xlsxwriter as xlsw

from .init_fields_data import init_fields_data


def create_file(filename, mode, data, date):
    wb = xlsw.Workbook(filename)
    sh = wb.add_worksheet()

    main_head_style = wb.add_format()
    main_head_style.set_bg_color('#FFC000')
    
    profit_style = wb.add_format()
    profit_style.set_bg_color('#00B050')

    
    actual_profit_style = wb.add_format()
    actual_profit_style.set_bg_color('#92D050')


    sold_status_style = wb.add_format()
    sold_status_style.set_bg_color('#C6EFCE')
    sold_status_style.set_color('#006100')


    not_sold_status_style = wb.add_format()
    not_sold_status_style.set_bg_color('#FFEB9C')
    not_sold_status_style.set_color('#9C5700')


    new_state_style = wb.add_format()
    new_state_style.set_bg_color('#C6EFCE')
    new_state_style.set_color('#006100')


    good_state_style = wb.add_format()
    good_state_style.set_bg_color('#E2EFDA')
    good_state_style.set_color('#006100')


    damaged_state_style = wb.add_format()
    damaged_state_style.set_bg_color('#FFC7CE')
    damaged_state_style.set_color('#9C0006')


    used_state_style = wb.add_format()
    used_state_style.set_bg_color('#F4B084')
    used_state_style.set_color('#9C0006')







    init_fields_data(
        sh,
        mode,
        data,
        date,
        main_head_style,
        profit_style,
        actual_profit_style,
        sold_status_style,
        not_sold_status_style,
        new_state_style,
        good_state_style,
        damaged_state_style,
        used_state_style
    )

    wb.close()

