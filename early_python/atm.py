import random


class BankAccount:
    
    def __init__(self, bal, user_name):
        self.bal = bal
        self.name = str(user_name).capitalize()

    def create_acct(self, user_name):
        """takes in self, sets up account, returns bal"""
        print('How much is the initial deposit?\n')
        new_dep = input('Amount: $')
        BankAccount.acct_setup(self, new_dep, user_name)
        return self.bal

    def lookup_balance(self):
        """takes in self, returns account balance"""
        print('The account balance is $', self.bal)
        BankAccount.prompt_for_selection(self)
        return self.bal

    def increase_balance(self):
        """takes in self, asks for deposit amt, adds to current bal.
        returns new bal"""
        print('The balance of your account is ${}'.format(self.bal))
        print('How much would you like to deposit?\n')
        deposit = int(input('Amount:  '))
        fee = BankAccount.charge_fee(self)
        new_bal = self.bal + deposit - fee
        self.bal = new_bal
        #  BankAccount.update_account_balance(self, new_bal, self.name)
        BankAccount.lookup_balance(self)
        return self.bal

    def check_funds(self, withdrawal):
        """takes in self and withdrawal, compares to balance, returns
        None"""
        if withdrawal > self.bal:
            print('Sorry, you have insufficient funds for this transaction.')
            BankAccount.decrease_balance(self)
        
        return None

    def decrease_balance(self):
        """takes in self, asks for withdraw amt, adds to current bal.
        returns new bal"""
        print(
            'Your current balance is ${}.'.format(self.bal), 
            'How much would you like to withdraw?\n'
        )
        withdrawal = int(input('Amount:  '))

        if withdrawal > self.bal:
            print('Sorry, you have insufficient funds for this transaction.')
            BankAccount.decrease_balance(self)

        fee = BankAccount.charge_fee(self)
        new_bal = self.bal - withdrawal - fee
        self.bal = new_bal
        #  BankAccount.update_account_balance(self, new_bal, self.name)
        BankAccount.lookup_balance(self)
        return self.bal

    def process_interest(self):
        """takes in self, calculates interest & adds to bal, 
        returns new bal"""
        print('The balance of this account is ${}'.format(self.bal))
        new_bal = self.bal * 1.05
        self.bal = new_bal
        #  BankAccount.update_account_balance(self, new_bal)
        BankAccount.lookup_balance(self)

        return self.bal

    def get_standing(self):
        standing = self.bal >= 1000
        return standing   

    def charge_fee(self):
        if BankAccount.get_standing(self):
            
            fee = 0
            
        else:
            fee = 5 
            print(
                'As your account balance is under $1000, you have been' + 
                ' charged a ${} fee for this transaction'.format(fee)
            )        
        return fee

    def prompt_for_selection(self):
        """take name, give options, redirect to appropriate menu.  return name"""
        print(
            'Choose from these options by number:',
            '\n1 = BALANCE', 
            '\n2 = DEPOSIT', 
            '\n3 = WITHDRAWAL', 
            '\n4 = INTEREST', 
            '\n5 = EXIT'
        )
        selection = int(input('Your selection:'))
        if selection == 1:

            BankAccount.lookup_balance(self)

        elif selection == 2:

            BankAccount.increase_balance(self)

        elif selection == 3:

            BankAccount.decrease_balance(self)

        elif selection == 4:

            BankAccount.process_interest(self)

        elif selection == 5:

            BankAccount.get_standing(self)

        return None

    def update_account_balance(self, new_bal, user_name):
        """takes in new_bal, updates account bal, returns bal"""
        
        BankAccount.acct_setup(self, new_bal)

        return None


def prompt_user_for_name():
    print('Please enter the name you want to look up:\n')
    user_name = input('Name:  ').lower()
    print()
    return user_name  

def prompt_for_retype(acct_dbase):
    """takes nothing.  asks for user to re-enter name.  returns name"""
    print('Please enter the name again.')
    user_name = input('Name:  ').lower()
    check_for_acct(user_name, acct_dbase)

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
        BankAccount.acct_setup(acct_name, acct_bal, user_name)
        
    elif user_name not in acct_dbase:
        print(
            'Is this a new account?  Or did you mistype?'
        )
        retype_ans = input('Type "new" or "error":  ').lower()
        if retype_ans == 'new':
            BankAccount.create_acct(acct_name, user_name)

        else:
            prompt_for_retype(acct_dbase)

    return acct_name   

def update_acct_dbase(name, bal, acct_dbase):
    """takes in name and bal, replaces existing bal.  returns acct_dbase"""
    acct_dbase[name] = bal
    return acct_dbase

def exit_program(name, bal, acct_dbase):
    """takes in nothing, exists program.  returns None"""
    update_acct_dbase(name, bal, acct_dbase)

    print('\nGoodbye!\n')

    return None

fetch_acct_file

def create_acct_dbase(acct_file):
    """takes in acct_file, formats into key:val dict, returns dict"""




    return acct_dbase

def fetch_acct_data():
    """takes in nothing, gets acct data, returns file as formated dict"""


    create_acct_dbase(acct_file)



    return acct_file

def overall_schematic():
    """takes in nothing, just collects classes & functions"""

    acct_dbase = {'erin':500.00, 'glenn':400.00, 'ralph':600.00, 'arta': 250.00}
    #  acct_dbase = fetch_acct_data
    print('\n\n\nWelcome to Your Bloodsucking Bank.\n\n\n')

    
    user_name = prompt_user_for_name()

    

    check_for_acct(account, user_name, acct_dbase)
    BankAccount.prompt_for_selection(acct_name)
    #return to program here
    exit_program(user_name, acct_name.bal, acct_dbase)
    print('Name:', user_name.capitalize(), 'AcctBal:', acct_name.bal, 'Dbase:', acct_dbase)

    return None


overall_schematic()