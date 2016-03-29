#CHECK! parse and store the **daily total** data for each day.  
#find and print out hte specific date with the most rain.
#find and print out the year with the most rain.

import urllib.request

def intro_message():
    """prints brief message explaining parameters"""
    print (
        'This program uses the Sunnyside record as of the current date.\n' +
        'Therefore, if you run it on a different day you will ' +
        'return different information\n\n'
    )
    return None

def download_sunnyside_record():
    """opens weather record, imports as utf-8 list of string 
    lines.  returns that list."""
    with urllib.request.urlopen('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain') as weather_import_file:
        rain_date_lines = [byte_line.decode('utf-8')for byte_line in weather_import_file]
    return rain_date_lines      

def convert_listpair_item_to_int(pair):
    """takes in string, replaces hyphens with '0', returns string"""
    date = pair[0]
    daytotal = pair[1]
    if daytotal != '-':
        daytotal = int(daytotal)
    else:
        daytotal = int('0')
    pair = [date, daytotal]
    return pair

def transform_line_to_pair(line):
    """takes in line, splits into pair of indexes 0 & 2.  returns pair"""
    month_total_single_pair = line.split()[0:2]
    month_total_single_pair_with_ints = convert_listpair_item_to_int(month_total_single_pair)
    return month_total_single_pair_with_ints

def comprehend_date_raintotal_pairs(rain_date_lines):
    """takes in list of lines, comprehends pairs from lines,  returns list of pairs."""
    date_raintotal_pairs = [transform_line_to_pair(line) for line in rain_date_lines[12:]]
    return date_raintotal_pairs

def create_dates_to_daytotals(dates_with_daytotals):
    """takes list of strings.  creates dict of date:daytotal from list.  returns dict"""
    dates_only = [date_rain_pairs[0] for date_rain_pairs in dates_with_daytotals]
    daytotals_only = [date_rain_pairs[1] for date_rain_pairs in dates_with_daytotals]
    dates_to_daytotals = {}
    for pair in dates_with_daytotals:
        dates_to_daytotals[pair[0]] = pair[1]
    return dates_to_daytotals

def overall_schematic(date):
    """contains all the functions that run this program.  
    returns None."""
    intro_message()
    rain_date_lines = download_sunnyside_record()
    dates_with_daytotals = comprehend_date_raintotal_pairs(rain_date_lines)
    dates_to_daytotals = create_dates_to_daytotals(dates_with_daytotals)
    max_val = max(dates_to_daytotals.key()) + ' had the most rain with ' max(dates_to_daytotals.values()) + ' inches')
    print(max_val)
    print(dates_to_daytotals[date])

    
    # remove date and daily total
    #     sunnyside_record_today[0] + sunnyside_record_today[1]
    #     date, daily_total 
    
    # find max(daily_total) in list
    #     return with associated date

    # create another list with lists of dates that end with same
    #     year and related daily total(s)

    #     find count of the daily totals within each list in that
    #         list and print that total with the associated year 
    #         from the outer dict
    #         list = [keyyear:[10, 5, 7, 0, 23], keyyear2:[5, 8, 9, 22, 0]]


    # find max()

    return dates_to_daytotals


overall_schematic('01-OCT-2011')




