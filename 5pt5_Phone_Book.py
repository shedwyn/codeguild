#5pt5_Phone_Book

 #Top level commands:  'add', 'change', 'lookup'.  Take commands \
    #and their inputs until you quit.

 #Advanced:  Allow people to have multiple phone numbes and change \
    #the interface to allow \
    #adding multiple numbers and removing specific numbers.

#add button
#edit button
#search field


def prompt_user_for_task():
    """initial prompt to start program, asking user which task they wish to begin \
        returns that response."""

    return task_to_do

####next function is probably multiple functions, not one
def process_task():
    """take in task_to_do response and run appropriate function/method on response"""




    return answer

#########################

def prompt_user_for_name():
    """ask user for name to add/find/change.  return that name"""

    return name

def prompt_user_for_number():
    """ask user for number to add/change.  return that number"""

    return number

def add_name_to_phone_book():
    """take in name and insert into list of records.  return new phone book \
    collection."""

    return phone_book

def add_number_to_phone_book():
    """take in name and number and insert into phone book.  return new phone \
    book collection."""

    return phone_book

def find_record_in_phone_book():
    """take in name.  find in phone_book.  return answer."""

    return records

def no_name_error_message():
    """triggered when the name is not in the phone book.  returns \
    prompt_user_for_name"""

def print_record_to_screen():
    """take in complete phone book record.  print record to screen"""

    print(record)


phone_book = {}
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

