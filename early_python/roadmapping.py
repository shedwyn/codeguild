# For this sort of problem, you'll want to iteratively visit cities
    #you know you can access while updating:
# 1. Cities you can access.
# 1. Cities you've been to.
# 1. Cities you haven't been to.
# ​
# * Let the user enter a city.
# Print out all the cities connected to that city.
# * Let the user enter a city.
# Print out all cities that could be reached through two hops.

def intro_statement():
    print('Road Mapping Assignment\n\n')
    return None

def prompt_user_for_city():
    print(
        'Choose one of the following cities to map:\n',
        'Albany, Boston, New York, Philadelphia, or Portland.\n'
    )
    city_to_map = input('Your choice:  ')
    print('\n')
    return city_to_map

def extract_hoppable_cities_set(city_to_accessible_cities, city):
    """takes in named city and dictionary.  extracts and returns the city set"""
    hopcities_for_city = city_to_accessible_cities[city]
    return hopcities_for_city

def print_hopcities_for_city(city_to_accessible_cities, city_to_map):
    #city_to_map = city_to_map
    #city_to_accessible_cities = city_to_accessible_cities

    hopcities_for_city = extract_hoppable_cities_set(city_to_accessible_cities, city_to_map)

    print(
        'You may "single hop" from',
        city_to_map,
        'to the following cities:\n',
        '    -',
        ', '.join(hopcities_for_city)
    )

    for city in hopcities_for_city:
        hopcities_for_subcity = extract_hoppable_cities_set(city_to_accessible_cities, city)
        print(
            '    - you may also travel through', city, 'to the following cities:\n',
            '    -' , ', '.join(hopcities_for_subcity)
        )

    # for city in city_to_accessible_cities[city_to_map]:
    #     print(city)

    return None




def overall_schematic():
    intro_statement()
    city_to_map = prompt_user_for_city()
    print_hopcities_for_city(city_to_accessible_cities, city_to_map)

    return None



city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

overall_schematic()


# want user input of city to result in string
# 'from'  inputcity 'you can hop to' 'set values 
    #for city_to_accessible_cities[inputcity]''


