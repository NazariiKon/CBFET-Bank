from AccountManager import AccountManager
from AuthenticationManager import AuthenticationManager

def print_main_menu():
    print("\033c", end='') # clear console
    print("\nWelcome to CBFET Bank System")
    print("1. Check Account Balance")
    print("2. Lodge Funds")
    print("3. Withdraw Funds")
    print("4. Change Password")
    print("5. Quit")

def print_login_menu():
    print("\033c", end='') # clear console
    print("Welcome!")
    print("1. Login\n2. Registration\n3. Quit")

def get_name_and_surname():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    return name, surname

def authentication(account_manager):
    auth_manager = AuthenticationManager(account_manager)
    while(True):
        print_login_menu()
        choice = input()
        
        match choice: 
            case '1': # Login
                name, surname = get_name_and_surname()
                account = auth_manager.login(name, surname)
                if account != None:
                    pass
                else: 
                    print("This user does not exist")
                    
            case '2': # Registration
                name, surname = get_name_and_surname()
                account = auth_manager.registration(name, surname)
                if account != None:
                    pass
                else: 
                    print("Something wrong with registration.")
                    
            case '3': # Exit
                exit()
            case _:
                print("Invalid option. Please try again.")


file_name = 'dictionary.txt'
account_manager = AccountManager(file_name)
authentication(account_manager)
