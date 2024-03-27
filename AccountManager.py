import os
import random
from Account import Account

class AccountManager: 
    file_name = ""
    accounts = []
    def __init__(self, name):
        self.file_name = name
        self.accounts = self.read_accounts_from_dictionary()

    
    def create_account(self, name, surname):
        account = Account(name, surname, random.randint(10000000000000000000, 99999999999999999999), 0, 2, surname)
        self.write_account_to_file(account)
        return account

    def read_accounts_from_dictionary(self):
        accounts = []
        with open(self.file_name, 'r') as file:
            for line in file:
                data = line.strip().split() 
                if len(data) >= 6:
                    accounts.append(Account(*data))
        return accounts
    
    def write_account_to_file(self, account): 
        with open(self.file_name, 'w') as file:
            for var_name, var_value in account.__dict__.items():
                if not var_name.startswith('__'):
                    file.write(f"{var_value} ")
        file.close()    

    def search_account(self, name, surname):
        for account in self.accounts:
            if account.name == name:
                if account.surname == surname:
                    return account
        
        return None
        