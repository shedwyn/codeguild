#CHECK! parse and store the **daily total** data for each day.  
#CHECK! find and print out hte specific date with the most rain.
#CHECK! find and print out the year with the most rain.
#Find and print the day of the year with the most rain on average. 
    #E.g. December 30th has 1" of rain on average.
#Advanced options and other challenges listed at bottom of script

#how do I get from list of lines to dict with MO-DAY as key and 
    #set/list of daytotals for that MO-DAY is value?
        #sort lines on MO-DAY
            #break MO out
                #pad value with ' ' for val that are < maxlen(MO)
        # grab 

        # for x in list:
        #     sort(x[slice of x])
#get data into a dict where MO-DAY is key and there is a set/list 
    #of daytotal values. if I can get this number into one 
    #number instead might be better?
#CALCULATION = run sum, count/len, and avg on set/list 
#sort dict based on highest of CALCULATION
#need output 'For' YEAR1 '-' YEARf,  MO, DAY 'had the most rainfall 
    #on average with ' + AVG 'inches'
#can we look at trend - is rainfall increasing or decreasing for that 
    #day over time?  if so, by what fraction?  apply that fraction 
    #per YEAR for the DIFF of years between USER INPUT year and 
    #CURRENT YEAR.  Output that CALC VAL for user.
        #for this one, set/list must be ordered in order to 
        #follow trend

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
    with urllib.request.urlopen('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain') as weather_import_file:
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

def create_list_days_with_daytotals(rain_date_lines):
    """takes in list of lines, comprehends pairs from lines,  returns list of pairs."""
    date_raintotal_pairs = [transform_line_to_pair(line) for line in rain_date_lines[12:]]
    return date_raintotal_pairs

def create_dict(dates):
    print(pair) 

    dictionarykey = '-'.join(pair[0].split('-')[0:2])
    print(dictionarykey)
    dict_value = pair[1]
    print(dict_value)
    dictionary = {dictionarykey:dict_value}


    return dictionary


def create_monthday_to_daytotals(dates_with_daytotals):
    """takes in list of pairs, sorts on pair[0] split by '-'.  
    returns new list"""
    
dict.setdefault() and collections.defaultdict
    
    #monthdaykey = ['-'.join(pair[0].split('-')[0:2]) for pair in dates_with_daytotals]
    
    # monthday_to_daytotals = {'-'.join(pair[0].split('-')[0:2]).append(pair[1]) if '-'.join(pair[0].split('-')[0:2]) in monthday_to_daytotals else '-'.join(pair[0].split('-')[0:2]):pair[1] for pair in dates_with_daytotals}

    monthday_to_daytotals = {}


    for pair in dates_with_daytotals:
        
        monthdaykey = '-'.join(pair[0].split('-')[0:2])

        
        if monthdaykey not in monthday_to_daytotals:
            monthday_to_daytotals[monthdaykey] = [pair[1]]

        else:
            monthday_to_daytotals[monthdaykey].append(pair[1])

    

    return monthday_to_daytotals



def create_dates_to_daytotals(dates_with_daytotals):
    """takes list of strings.  creates dict of date:daytotal from list.  returns dict"""
    dates_only = [date_rain_pairs[0] for date_rain_pairs in dates_with_daytotals]
    daytotals_only = [date_rain_pairs[1] for date_rain_pairs in dates_with_daytotals]
    dates_to_daytotals = {}
    for pair in dates_with_daytotals:
        dates_to_daytotals[pair[0]] = pair[1]
    return dates_to_daytotals

def convert_date_into_yearonly(pair):
    """takes in list of pairs.  takes pair[0], splits on '-', saves only year.
    returns refurbished pair."""
    splitdate = pair[0].split('-')[2]
    pair = [splitdate, pair[1]]
    
    return pair

def create_years_to_yeartotals(dates_with_daytotals):
    """total all daytotals for each year"""
    #need to breakout pair[0] in list into single key with all values for keys matching
    years_with_daytotals = [convert_date_into_yearonly(pair) for pair in dates_with_daytotals]
    years_to_yeartotals = {}
    for pair in years_with_daytotals:
        if pair[0] not in years_to_yeartotals:
            years_to_yeartotals[pair[0]] = pair[1]
        else:
            years_to_yeartotals[pair[0]] += pair[1]
    return years_to_yeartotals

def find_date_with_max_rain(dictionary_with_raintotals):
    """takes in the dict, sorts on key.  returns keys sorted list"""
    sorted_word_to_counts = sorted(
        dictionary_with_raintotals, 
        key=dictionary_with_raintotals.get, 
        reverse=True
    )
    date_with_max_rain = sorted_word_to_counts[0] + ' had the most rain with ' + str(dictionary_with_raintotals[sorted_word_to_counts[0]] / 100) + ' inches.'
    return date_with_max_rain

def overall_schematic():
    """contains all the functions that run this program.  
    returns None."""
    print('\n\n')
    intro_message()
    rain_date_lines = download_sunnyside_record()
    dates_with_daytotals = create_list_days_with_daytotals(rain_date_lines)
    dates_to_daytotals = create_dates_to_daytotals(dates_with_daytotals)
    years_to_yeartotals = create_years_to_yeartotals(dates_with_daytotals)
    
    monthday_to_daytotals = create_monthday_to_daytotals(dates_with_daytotals)
    print(monthday_to_daytotals)

    

    date_with_max_rain = find_date_with_max_rain(dates_to_daytotals)
    year_with_max_rain = find_date_with_max_rain(years_to_yeartotals)

    print(date_with_max_rain, '\n\n')

    print(year_with_max_rain, '\n\n')

    return None

overall_schematic()




#Allow someone to type in a date in the future and, using the average 
    #value for that day of the year, predict the amount of rain.
#My thoughts:
#How can I change create_dates_to_daytotals(dates_with_daytotals)
    #so it can process year as well?
#How could this program change to make it more functional for a user?
    #ie allowing user to indicate date or year to pull data
#Try breaking list of lists into dict with values as list of 
    #daytotals and year as key.


    #dates_with_daytotals = dates_with_daytotals
    # dates_only = [date_rain_pairs[0].split('-') for date_rain_pairs in dates_with_daytotals]
    # daytotals_only = [date_rain_pairs[1] for date_rain_pairs in dates_with_daytotals]

        # if pair[0].split('-')[0:2] not in monthday_to_daytotals:
        #     monthday_to_daytotals[pair[0].split('-')[0:2]] = []
        #     monthday_to_daytotals
        # else:
        #     monthday_to_daytotals[monthday_to_daytotals[pair[0].split('-')[0:2]]].append(pair1)


    #REALLY NICE PIECE OF CODE:
    #monthday_to_daytotals = {'-'.join(pair[0].split('-')[0:2]): [pair[1]] for pair in dates_with_daytotals}