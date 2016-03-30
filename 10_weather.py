#CHECK! parse and store the **daily total** data for each day.  
#find and print out hte specific date with the most rain.
#find and print out the year with the most rain.

import urllib.request

def intro_message():
    """prints brief message explaining parameters"""
    print (
        'This program uses the Sunnyside record as of the current date.\n' +
        'Therefore, if you run it on a different day you will ' +
        'return different information'
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

def find_date_with_max_rain(dates_to_daytotals):
    """takes in the dict, sorts on key.  returns keys sorted list"""
    sorted_word_to_counts = sorted(
        dates_to_daytotals, 
        key=dates_to_daytotals.get, 
        reverse=True
    )
    date_with_max_rain = sorted_word_to_counts[0] + ' had the most rain with ' + str(dates_to_daytotals[sorted_word_to_counts[0]] / 100) + ' inches.'
    return date_with_max_rain

def convert_date_into_yearonly(pair):
    """takes in list of pairs.  takes pair[0], splits on '-', saves only year.
    returns refurbished pair."""
    splitdate = pair[0].split('-')[2]
    pair = [splitdate, pair[1]]
    
    return pair

def sum_year_totals():  #START HERE!
    """total all daytotals for each year"""
    #need to breakout pair[0] in list into single key with all values for keys matching
    dictionary = {}
    for pair in otherdictionary
        if otherdictionary[pair[0]] not in dictionary[]:
            dictionary[pair[0]] = otherdictionary[pair[0]]
        else:
            dictionary[pair[0]] = dictionary[pair[0]] + otherdictionary[pair[0]]

print(convert_date_into_yearonly(['01-OCT-2011', 293]))

# def split_dates_into_years(date_raintotal_pairs):
#     """takes in list of pairs, convert first item of pair to year only.  return list of pairs."""
#     for pair in date_raintotal_pairs

#     return year_raintotal_pairs

def overall_schematic():
    """contains all the functions that run this program.  
    returns None."""
    print('\n\n')
    intro_message()
    rain_date_lines = download_sunnyside_record()
    dates_with_daytotals = comprehend_date_raintotal_pairs(rain_date_lines)
    dates_to_daytotals = create_dates_to_daytotals(dates_with_daytotals)
    date_with_max_rain =find_date_with_max_rain(dates_to_daytotals)

    print('\n\n', date_with_max_rain, '\n\n')


   
    # create another list with lists of dates that end with same
    #     year and related daily total(s)

    #     find count of the daily totals within each list in that
    #         list and print that total with the associated year 
    #         from the outer dict
    #         list = [keyyear:[10, 5, 7, 0, 23], keyyear2:[5, 8, 9, 22, 0]]


    # find max()

    return dates_to_daytotals


overall_schematic()




