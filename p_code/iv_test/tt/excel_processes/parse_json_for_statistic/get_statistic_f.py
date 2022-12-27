from .help_f import validate_nan_or_not


def set_total_statistic(obj, r_s, y_z):
    bargin = r_s[1][1]
    bargin = validate_nan_or_not(bargin)
    
    valid_bargin = r_s[5][1]
    valid_bargin = validate_nan_or_not(valid_bargin)

    the_rest_of_goods = r_s[6][1]
    the_rest_of_goods = validate_nan_or_not(the_rest_of_goods)
    
    sold_goods = r_s[9][1]
    sold_goods = validate_nan_or_not(sold_goods)

    unsold_goods = r_s[10][1]
    unsold_goods = validate_nan_or_not(unsold_goods)




    if not 'bargin' in obj:
        obj['bargin'] = bargin
    else: 
        obj['bargin'] += bargin

    if not 'valid_bargin' in obj:
        obj['valid_bargin'] = valid_bargin
    else: 
        obj['valid_bargin'] += valid_bargin


    if not 'the_rest_of_goods' in obj:
        obj['the_rest_of_goods'] = the_rest_of_goods
    else: 
        obj['the_rest_of_goods'] += the_rest_of_goods

    if not 'sold_goods' in obj:
        obj['sold_goods'] = sold_goods
    else: 
        obj['sold_goods'] += sold_goods

    if not 'unsold_goods' in obj:
        obj['unsold_goods'] = unsold_goods
    else: 
        obj['unsold_goods'] += unsold_goods




    summ = y_z[0][1]
    summ = validate_nan_or_not(summ)

    sum_of_deliver = y_z[1][1]
    sum_of_deliver = validate_nan_or_not(sum_of_deliver)

    total__sum_sum_of_deliver = y_z[2][1]
    total__sum_sum_of_deliver = validate_nan_or_not(total__sum_sum_of_deliver)

    total_goods = y_z[3][1]
    total_goods = validate_nan_or_not(total_goods)


    if not 'summ' in obj:
        obj['summ'] = summ
    else: 
        obj['summ'] += summ


    if not 'sum_of_deliver' in obj:
        obj['sum_of_deliver'] = sum_of_deliver
    else: 
        obj['sum_of_deliver'] += sum_of_deliver


    if not 'total__sum_sum_of_deliver' in obj:
        obj['total__sum_sum_of_deliver'] = total__sum_sum_of_deliver
    else: 
        obj['total__sum_sum_of_deliver'] += total__sum_sum_of_deliver

    if not 'total_goods' in obj:
        obj['total_goods'] = total_goods
    else: 
        obj['total_goods'] += total_goods


def set_year_statistic(obj, year, r_s, y_z):



    bargin = r_s[1][1]
    bargin = validate_nan_or_not(bargin)
    
    valid_bargin = r_s[5][1]
    valid_bargin = validate_nan_or_not(valid_bargin)

    the_rest_of_goods = r_s[6][1]
    the_rest_of_goods = validate_nan_or_not(the_rest_of_goods)
    
    sold_goods = r_s[9][1]
    sold_goods = validate_nan_or_not(sold_goods)

    unsold_goods = r_s[10][1]
    unsold_goods = validate_nan_or_not(unsold_goods)




    if not 'bargin' in obj[year]['year']:
        obj[year]['year']['bargin'] = bargin
    else: 
        obj[year]['year']['bargin'] += bargin

    if not 'valid_bargin' in obj[year]['year']:
        obj[year]['year']['valid_bargin'] = valid_bargin
    else: 
        obj[year]['year']['valid_bargin'] += valid_bargin


    if not 'the_rest_of_goods' in obj[year]['year']:
        obj[year]['year']['the_rest_of_goods'] = the_rest_of_goods
    else: 
        obj[year]['year']['the_rest_of_goods'] += the_rest_of_goods

    if not 'sold_goods' in obj[year]['year']:
        obj[year]['year']['sold_goods'] = sold_goods
    else: 
        obj[year]['year']['sold_goods'] += sold_goods

    if not 'unsold_goods' in obj[year]['year']:
        obj[year]['year']['unsold_goods'] = unsold_goods
    else: 
        obj[year]['year']['unsold_goods'] += unsold_goods




    summ = y_z[0][1]
    summ = validate_nan_or_not(summ)

    sum_of_deliver = y_z[1][1]
    sum_of_deliver = validate_nan_or_not(sum_of_deliver)

    total__sum_sum_of_deliver = y_z[2][1]
    total__sum_sum_of_deliver = validate_nan_or_not(total__sum_sum_of_deliver)

    total_goods = y_z[3][1]
    total_goods = validate_nan_or_not(total_goods)


    if not 'summ' in obj[year]['year']:
        obj[year]['year']['summ'] = summ
    else: 
        obj[year]['year']['summ'] += summ


    if not 'sum_of_deliver' in obj[year]['year']:
        obj[year]['year']['sum_of_deliver'] = sum_of_deliver
    else: 
        obj[year]['year']['sum_of_deliver'] += sum_of_deliver


    if not 'total__sum_sum_of_deliver' in obj[year]['year']:
        obj[year]['year']['total__sum_sum_of_deliver'] = total__sum_sum_of_deliver
    else: 
        obj[year]['year']['total__sum_sum_of_deliver'] += total__sum_sum_of_deliver

    if not 'total_goods' in obj[year]['year']:
        obj[year]['year']['total_goods'] = total_goods
    else: 
        obj[year]['year']['total_goods'] += total_goods


def set_month_statistic(obj, year, month, r_s, y_z):

    bargin = r_s[1][1]
    bargin = validate_nan_or_not(bargin)
    
    valid_bargin = r_s[5][1]
    valid_bargin = validate_nan_or_not(valid_bargin)

    the_rest_of_goods = r_s[6][1]
    the_rest_of_goods = validate_nan_or_not(the_rest_of_goods)
    
    sold_goods = r_s[9][1]
    sold_goods = validate_nan_or_not(sold_goods)

    unsold_goods = r_s[10][1]
    unsold_goods = validate_nan_or_not(unsold_goods)


    if not 'bargin' in obj[year]['month'][month]:
        obj[year]['month'][month]['bargin'] = bargin
    else: 
        obj[year]['month'][month]['bargin'] += bargin


    if not 'valid_bargin' in obj[year]['month'][month]:
        obj[year]['month'][month]['valid_bargin'] = valid_bargin
    else: 
        obj[year]['month'][month]['valid_bargin'] += valid_bargin


    if not 'the_rest_of_goods' in obj[year]['month'][month]:
        obj[year]['month'][month]['the_rest_of_goods'] = the_rest_of_goods
    else: 
        obj[year]['month'][month]['the_rest_of_goods'] += the_rest_of_goods


    if not 'sold_goods' in obj[year]['month'][month]:
        obj[year]['month'][month]['sold_goods'] = sold_goods
    else: 
        obj[year]['month'][month]['sold_goods'] += sold_goods


    if not 'unsold_goods' in obj[year]['month'][month]:
        obj[year]['month'][month]['unsold_goods'] = unsold_goods
    else: 
        obj[year]['month'][month]['unsold_goods'] += unsold_goods





    summ = y_z[0][1]
    summ = validate_nan_or_not(summ)

    sum_of_deliver = y_z[1][1]
    sum_of_deliver = validate_nan_or_not(sum_of_deliver)

    total__sum_sum_of_deliver = y_z[2][1]
    total__sum_sum_of_deliver = validate_nan_or_not(total__sum_sum_of_deliver)

    total_goods = y_z[3][1]
    total_goods = validate_nan_or_not(total_goods)


    if not 'summ' in obj[year]['month'][month]:
        obj[year]['month'][month]['summ'] = summ
    else: 
        obj[year]['month'][month]['summ'] += summ


    if not 'sum_of_deliver' in obj[year]['month'][month]:
        obj[year]['month'][month]['sum_of_deliver'] = sum_of_deliver
    else: 
        obj[year]['month'][month]['sum_of_deliver'] += sum_of_deliver


    if not 'total__sum_sum_of_deliver' in obj[year]['month'][month]:
        obj[year]['month'][month]['total__sum_sum_of_deliver'] = total__sum_sum_of_deliver
    else: 
        obj[year]['month'][month]['total__sum_sum_of_deliver'] += total__sum_sum_of_deliver


    if not 'total_goods' in obj[year]['month'][month]:
        obj[year]['month'][month]['total_goods'] = total_goods
    else: 
        obj[year]['month'][month]['total_goods'] += total_goods
