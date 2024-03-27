from AccountManager import AccountManager
account_manager = AccountManager('dictionary.txt')

file_name = 'dictionary.txt'
print("Welcome!")
print("1. Login\n2. Registration\n3. Quit")
accounts = account_manager.read_accounts_from_dictionary()
menu = input()

match menu:
    case '1':
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        password = input("Enter your password: ")
    case '2':
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        new_account = account_manager.create_account(name, surname)
    case '3':
        exit()