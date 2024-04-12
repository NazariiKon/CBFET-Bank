from AccountManager import AccountManager
from AuthenticationManager import AuthenticationManager

def print_main_menu(name, surname):
    print("\033c", end='') # clear console
    print(f"Hi, {name} {surname}")
    print("Welcome to CBFET Bank System")
    print("1. Check Account Balance")
    print("2. Lodge Funds")
    print("3. Withdraw Funds")
    print("4. Change Password")
    print("5. Calculate interest")
    print("6. Print statement")
    print("7. Log out")
    print("8. Quit")
    
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
    
    while True: 
        print_login_menu()
        choice = input()        
        
        match choice: 
            case '1': # Login
                name, surname = get_name_and_surname()
                account = auth_manager.login(name, surname)
                        
            case '2': # Registration
                name, surname = get_name_and_surname()
                account = auth_manager.registration(name, surname)
                        
            case '3': # Exit
                exit()
            case _:
                input("Invalid option. Please try again.")
                continue
                
        if account != None:
            return account
        else: input("This user does not exist") 
        
file_name = 'dictionary.txt'
account_manager = AccountManager(file_name)
while True:
    account = authentication(account_manager)

    while True:
        print_main_menu(account.name, account.surname)
        if(account.password == account.surname): print("You need to change your password!")
        choice = input()

        match choice: 
            case '1': 
                account.check_balance()
            case '2':
                try:
                    amount = float(input("Enter the amount you want to lodge to your account: "))
                except:
                    input("You have entered an incorrect amount")
                    continue
                account.lodge_funds(amount)
                account_manager.update_account_info_in_dictionary(account)

            case '3':
                try:
                    amount = float(input("Enter the amount you want to withdraw from your account: "))
                except:
                    input("You have entered an incorrect amount")
                    continue
                account.withdraw_funds(amount)
                account_manager.update_account_info_in_dictionary(account)

            case '4':
                account.change_password()
                account_manager.update_account_info_in_dictionary(account)
            case '5':
                account.calculate_interest(12)
            case '6':
                account.print_statement()
            case '7':
                break
            case '8':
                exit()
            case _:
                input("Invalid option. Please try again.")
                continue