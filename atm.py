#ATM

import random

def prompt_user_for_name():
    print('Whose Account do you wish to look up?\n', 
        'Arta, Glenn, Gloria, Pat, or Ralph\n'
    )
    input('Your Selection:  ')
    print('\n')

class BankAccount:
    
    # def create_account(bank_records):

    # """takes in bank_records, generates new ID and creates blank
    # bank_record for new customer"""
    # #bank_records = bank_records
    # max_keyval_in_bank_rec = 1001 + 10

    # account_id = max_keyval_in_bank_rec

    # print(account_id)
    # return account_id
    def acct_setup(self, bal):
        self.bal = bal


    def lookup_balance(self):

        return bal

    def increase_balance():

        return

    def decrease_balance():

        return

    def process_interest():

        return
    
def overall_schematic():
    """takes in nothing, just collects classes & functions"""
    


    glenn = BankAccount()
    glenn.acct_setup(200) 
    arta = BankAccount()
    arta.acct_setup(500)
    ralph = BankAccount()
    ralph.acct_setup(350)

    acct_name = prompt_user_for_name()




    #IndividualAccount()

    return 


overall_schematic()







#output = transaction(s) this instance, balance for account

#****************ADVANCED********************ADVANCED*********************

    # pat = BankAccount()
    # pat.acct_setup(578)
    # gloria = BankAccount()
    # gloria.acct_setup(450)


def create_account(bank_records):

    """takes in bank_records, generates new ID and creates blank
    bank_record for new customer"""
    #bank_records = bank_records
    max_keyval_in_bank_rec = 1001 + 10

    account_id = max_keyval_in_bank_rec

    print(account_id)
    return account_id

def prompt_for_account_num():
    """takes nothing, returns user_input"""
    
    return input('Please enter your 4 digitaccount number:')

def prompt_and_format_user_input(bank_records):
    """prompts user for account id, if no account, account is created
    returns account_id"""
    print('\nPlease enter your account number, if you do not have an account',\
        'please enter "None" and an account number will be created for you.'
    )

    account_id = prompt_for_account_num()

    if account_id not in bank_records.keys():
        print('\nThat account is not found, please re-enter 4 digit account number: ')
        account_id = prompt_for_account_num()

    elif int(account_id) == ValueError:
        createaccount()
    
    # else:
    #     IndividualAccount(account_id)

    return int(account_id)

#transactionID auto gen two part with date, trans num for that date, will 
    #"print" list of all transactions that happened on that date.  Even 
    #more advanced - transaction id that.