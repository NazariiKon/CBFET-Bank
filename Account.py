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
            self.balance -= amount
            input(f"${amount} has been withdrawn. New balance is: ${self.balance}")
            self.check_interest()
        else:
            input("Insufficient funds.")
