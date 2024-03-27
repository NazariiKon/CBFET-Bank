class AuthenticationManager:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def _password_entry(account_password):
        password = input("Enter your password: ")
        if password == account_password:
            return True
        else: False

    def login(self, name, surname):
        account = self.account_manager.search_account(name, surname)
        if account != None:
            for attempts in range(3):
                if self._password_entry(account.password):
                    break
                else:
                    print(f"The password's wrong. You have {2 - attempts} attempts left.")  
                exit()

        return account
    
    def registration(self, name, surname):
        return self.account_manager.create_account(name, surname)
