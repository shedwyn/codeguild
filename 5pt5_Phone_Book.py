#5pt5_Phone_Book

 #Top level commands:  'add', 'change', 'lookup'.  Take commands \
    #and their inputs until you quit.

 #Advanced:  Allow people to have multiple phone numbes and change \
    #the interface to allow \
    #adding multiple numbers and removing specific numbers.


def prompt_user_for_task():
    """initial prompt to start program, asking user which task they wish to begin \
        returns that response."""
    print('\nWould you like to: add, change, lookup, print*, or quit? \n')
    task_selection_input = input('\nWould you like to ADD (a new name record), \
        CHANGE (an existing record), SEARCH (for an existing record - use to print),\
        or QUIT (the phone book program)?\n')
    return task_selection_input

def prompt_user_for_name():
    """ask user for name to add/find/change.  return that name"""
    input('\nWhat is the name of the person to add/change/find?\n')

    return phone_book_name

def prompt_user_for_number():
    """ask user for number to add/change.  return that number"""

    return number

def add_name_to_phone_book():
    """take in name and insert as a new key into phone book.  return new phone book \
    collection."""

    return phone_book

def add_number_to_phone_book():
    """take in number and phone book number list and add number to list."""

    return phone_book

def find_record_in_phone_book():
    """take in name.  find key name and phone number list.  return both key name 
    and phone number list."""

    return records

def verify_name_in_phone_book():
    """takes in the name user gave and checks to see if the name is in the phone \
    book.  returns message if it is not, or returns name if it is."""
    if name not in phone_book:
        print('name not in phone book.  Try another name')
        ###how will the user exit if they choose###
    else:
        return name

def return_list_of_numbers():
    """takes in a name, finds it in the phone book, returns the list of numbers for that name."""

    return phone_book_number_list

def remove_number_from_phone_book():
    """takes in a phone book list of numbers and a number.  removes the number from the list.  
    returns the new list."""

    return phone_book_number_list

def print_record_to_screen():
    """take in complete phone book record.  print record to screen"""

    print(record)

def process_task_request():
    """take in task_to_do and loop through tasks until user quits.  return quit answer when done"""

    return quit_answer

##BODY OF CODE#################################
###############################################
###############################################

task_to_do = None

print('Welcome\n')

#do I want to make the add process a function, the change process a function and the lookup\
#process a function?

while task_to_do != 'QUIT':

    task_to_do = prompt_user_for_task().upper

    phone_book_task_list = [
    'ADD', 
    'CHANGE', 
    'LOOKUP', 
    'QUIT'
    ]

    if task_to_do in phone_book_task_list:

    phone_book = {}

    phone_book_name = prompt_user_for_name().upper

        while phone_book_name in phone_book:

            if task_to_do == 'ADD':
                prompt_user_for_name()

            elif task_to_do == 'CHANGE':

            elif task_to_do == 'LOOKUP':

        print('That name is not in the phone_book, please try again.\n')

    print('I\'m sorry, that task is not recognized, please try again')


print('Goodbye')


if process_task_request() != exit:



task_counter = 0

while task_counter == 0:

    print('\nWould you like to: add, change, lookup, print*, or quit? \n')
    task_selection_input = input()
    search_or_add_tasks_list = ['add', 'change', 'lookup']

    if task_selection_input in search_or_add_tasks_list:
        print('\nWhat name would you like to add/change/lookup? \n')
        person_name = input()
        if task_selection_input != 'lookup':
            if task_selection_input == 'change' and person_name not in phone_book:
                print('\nThe name you typed is not in the phone book, please try again\n')
            else:
                print('\nWhat is the number for {}? \n'.format(person_name))
                person_number = input()
                phone_book[person_name] = person_number

        elif task_selection_input == 'lookup':
            print('\nThe number for {} is: '.format(person_name), phone_book[person_name])

    elif task_selection_input == 'print':
        print('\nThis will only print to the screen.\n')
        print(phone_book)

    elif task_selection_input == 'quit':
        print('\nGoodbye.')
        task_counter += 1

    else:
        print('\nI\'m sorry, I did not understand what you typed, please try again.\n')

