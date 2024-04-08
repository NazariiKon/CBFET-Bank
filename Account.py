class Account:
    name = ""
    surname = ""
    number = ""
    balance = 0.0
    interest_rate = 2
    password = ""


    def __init__(self, *args):
        self.name, self.surname, self.number, self.balance, self.interest_rate, self.password = args
        self.balance = float(self.balance)
        self.interest_rate = int(self.interest_rate)
        
    def check_balance(self):
        input(f"Your current balance is: ${self.balance}")
        
    def check_interest(self):
        if self.balance > 5000:
            self.interest_rate = 4
        else:
            self.interest_rate = 2
        input(f"Your interest is: {self.interest_rate}")

        
    def lodge_funds(self, amount):
        if amount > 0:
            self.balance += amount
            input(f"${amount} has been added to your account. New balance is: ${self.balance}")
            self.check_interest()
        else:
            input("Invalid amount entered.")
            
    def withdraw_funds(self, amount):
        if self.balance >= amount:
            if amount > 0:
                self.balance -= amount
                input(f"${amount} has been withdrawn. New balance is: ${self.balance}")
                self.check_interest()
            else:
                input("Invalid amount entered.")
        else:
            input("Insufficient funds.")
            
    def change_password(self):
        for attempts in range(3):
                password = input("Enter your password: ")
                if password == self.password:
                    new_password = input("Enter your new password: ")
                    confirm_password = input("Comfirm your new password: ")
                    if new_password == confirm_password:
                        self.password = new_password
                        return
                    else:
                        print("Passwords do not match.")
                else:
                    print(f"The password's wrong. You have {2 - attempts} attempts left.")  
        exit()

    def calculate_interest(self, months):
        balance = self.balance
        for month in range(months):
            interest = balance * (self.interest_rate / 100) / months  # Вычисляем ежемесячный процент
            balance += interest
            input(f"Mounth {month + 1}: Balance = {balance:.2f}")

    def print_statement(self):
        input(f"Name: {self.name}\nSurname: {self.surname}\nAccount number: {self.number}\nBalance: {self.balance}\nInterest rate: {self.interest_rate}")
