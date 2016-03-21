#5pt5_Phone_Book

 #Top level commands:  'add', 'change', 'lookup'.  Take commands \
    #and their inputs until you quit.

 #Advanced:  Allow people to have multiple phone numbes and change \
    #the interface to allow \
    #adding multiple numbers and removing specific numbers.

#add button
#edit button
#search field

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

