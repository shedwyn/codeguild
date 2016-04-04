#ATM

# import random

class BankAccount:
    
    # def create_account(bank_records):

    # """takes in bank_records, generates new ID and creates blank
    # bank_record for new customer"""
    # #bank_records = bank_records
    # max_keyval_in_bank_rec = 1001 + 10

    # account_id = max_keyval_in_bank_rec

    # print(account_id)
    # return account_id
    def acct_setup(acct_name, bal):
        acct_name.bal = bal
        acct_name.name = str(acct_name).capitalize()

    
    def create_acct(acct_name):
        """takes in acct_name, sets up account, returns bal"""
        print('How much is the initial deposit?\n')
        new_dep = input('Amount: $')
        BankAccount.acct_setup(acct_name, new_dep)
        return acct_name.bal

    def lookup_balance(acct_name):
        """takes in acct_name, returns account balance"""
        print('The account balance is $', acct_name.bal)
        BankAccount.prompt_for_selection(acct_name)
        return acct_name.bal

    def increase_balance(acct_name):
        """takes in acct_name, asks for deposit amt, adds to current bal.
        returns new bal"""
        print('The balance of your account is ${}'.format(acct_name.bal))
        print('How much would you like to deposit?\n')
        deposit = int(input('Amount:  '))
        new_bal = acct_name.bal + deposit
        BankAccount.update_account_balance(acct_name, new_bal)
        BankAccount.lookup_balance(acct_name)
        return acct_name.bal

    def check_funds(acct_name, withdrawal):
        """takes in acct_name and withdrawal, compares to balance, returns
        answer"""
        if withdrawal > acct_name.bal:
            print('Sorry, you have insufficient funds for this transaction.')
            BankAccount.decrease_balance(acct_name)
        
        return None

    def decrease_balance(acct_name):
        """takes in acct_name, asks for withdraw amt, adds to current bal.
        returns new bal"""
        print(
            'Your current balance is ${}.'.format(acct_name.bal), 
            'How much would you like to withdraw?\n'
        )
        withdrawal = int(input('Amount:  '))

        if withdrawal > acct_name.bal:
            print('Sorry, you have insufficient funds for this transaction.')
            BankAccount.decrease_balance(acct_name)

        #BankAccount.check_funds(acct_name, withdrawal)
        new_bal = acct_name.bal - withdrawal
        BankAccount.update_account_balance(acct_name, new_bal)
        BankAccount.lookup_balance(acct_name)
        return acct_name.bal

    def process_interest(acct_name):
        """takes in acct_name, calculates interest & adds to bal, 
        returns new bal"""
        print('The balance of this account is ${}'.format(acct_name.bal))
        new_bal = acct_name.bal * 1.05
        BankAccount.update_account_balance(acct_name, new_bal)
        BankAccount.lookup_balance(acct_name)

        return acct_name.bal

    def prompt_for_selection(acct_name):
        """take name, give options, redirect to appropriate menu.  return name"""
        print(
            'Choose from these options by number.',
            '1 = BALANCE, 2 = DEPOSIT, 3 = WITHDRAWAL, 4 = INTEREST, or ' + 
            '5 = EXIT'
        )
        selection = int(input('Your selection:'))
        if selection == 1:

            BankAccount.lookup_balance(acct_name)

        elif selection == 2:

            BankAccount.increase_balance(acct_name)

        elif selection == 3:

            BankAccount.decrease_balance(acct_name)

        elif selection == 4:

            BankAccount.process_interest(acct_name)

        return None

    def update_account_balance(acct_name, new_bal):
        """takes in new_bal, updates account bal, returns bal"""
        
        BankAccount.acct_setup(acct_name, new_bal)

        return None


def prompt_user_for_name():
    print('Please enter the name you want to look up:\n')
    acct_name = input('Name:  ').lower()
    print('\n')
    return acct_name  

def prompt_for_retype(acct_dbase):
    """takes nothing.  asks for user to re-enter name.  returns name"""
    print('Please enter the name again.')
    acct_name = input('Name:  ').lower()
    check_for_acct(acct_name, acct_dbase)

    return acct_name

def pull_balance_from_record(user_name, acct_dbase):
    """takes name, gets balance from dictionary.  returns bal"""

    acct_bal = acct_dbase[user_name]

    return acct_bal

def check_for_acct(user_name, acct_dbase):#does this belong in the class
    """take in user_name, redirect appropriately, return None."""
    
    acct_name = user_name + '_acct'

    if user_name in acct_dbase:
        acct_bal = pull_balance_from_record(user_name, acct_dbase)
        acct_name = BankAccount()
        BankAccount.acct_setup(acct_name, acct_bal)
        
    elif user_name not in acct_dbase:
        print(
            'Is this a new account?  Or did you mistype?'
        )
        retype_ans = input('Type "new" or "error":  ').lower()
        if retype_ans == 'new':
            BankAccount.create_acct(acct_name)

        else:
            prompt_for_retype(acct_dbase)

    return acct_name   


def update_acct_dbase(name, bal, acct_dbase):
    """takes in name and bal, replaces existing bal.  returns acct_dbase"""
    acct_dbase[name] = bal
    return acct_dbase

def exit_program(name, bal, acct_dbase):
    """takes in nothing, exists program.  returns None"""
    print(acct_dbase)
    update_acct_dbase(name, bal, acct_dbase)

    print(acct_dbase)

    print('\nGoodbye!\n')

    return None

def overall_schematic():
    """takes in nothing, just collects classes & functions"""
    acct_dbase = {'erin':500.00, 'glenn':400.00, 'ralph':600.00, 'arta': 250.00}

    print('\n\n\nWelcome to Your Bloodsucking Bank.\n\n\n')

    user_name = prompt_user_for_name()

    #acct_name = user_name + '_acct'
  
    acct_name = check_for_acct(user_name, acct_dbase)
    
    BankAccount.prompt_for_selection(acct_name)


    #return to program here

    exit_program(user_name, acct_name.bal, acct_dbase)
    print('Name:', user_name.capitalize(), 'AcctBal:', acct_name.bal, 'Dbase:', acct_dbase)


    print('\nGoodbye!\n')

    return None

#********************  run code area **********************************

overall_schematic()



#output = transaction(s) this instance, balance for account

#****************ADVANCED********************ADVANCED*********************

#Add randomizer that prints different messages when you deposit or 
        #withdraw from a list of possible messages


    # pat = BankAccount()
    # pat.acct_setup(578)
    # gloria = BankAccount()
    # gloria.acct_setup(450)




# def create_account(bank_records):

#     """takes in bank_records, generates new ID and creates blank
#     bank_record for new customer"""
#     #bank_records = bank_records
#     max_keyval_in_bank_rec = 1001 + 10

#     account_id = max_keyval_in_bank_rec

#     print(account_id)
#     return account_id

# def prompt_for_account_num():
#     """takes nothing, returns user_input"""
    
#     return input('Please enter your 4 digitaccount number:')

# def prompt_and_format_user_input(bank_records):
#     """prompts user for account id, if no account, account is created
#     returns account_id"""
#     print('\nPlease enter your account number, if you do not have an account',\
#         'please enter "None" and an account number will be created for you.'
#     )

#     account_id = prompt_for_account_num()

#     if account_id not in bank_records.keys():
#         print('\nThat account is not found, please re-enter 4 digit account number: ')
#         account_id = prompt_for_account_num()

#     elif int(account_id) == ValueError:
#         createaccount()
    
#     # else:
#     #     IndividualAccount(account_id)

#     return int(account_id)

#transactionID auto gen two part with date, trans num for that date, will 
    #"print" list of all transactions that happened on that date.  Even 
    #more advanced - transaction id that.


#***************  scrap heap *******************  scrap heap *************


    # def prompt_for_selection(acct_name):
    # """take name, give options, redirect to appropriate menu.  return None"""
    # print(
    #     'Choose from these options by number.',
    #     '1 = BALANCE, 2 = DEPOSIT, 3 = WITHDRAWAL, 4 = INTEREST, or ' + 
    #     '5 = EXIT'
    # )
    # selection = int(input('Your selection:'))
    # if selection == 1:

    #     BankAccount.lookup_balance(acct_name)

    # elif selection == 2:

    #     BankAccount.increase_balance(acct_name)

    # elif selection == 3:

    #     BankAccount.decrease_balance(acct_name)

    # elif selection == 4:

    #     BankAccount.process_interest(acct_name)

    # return None
