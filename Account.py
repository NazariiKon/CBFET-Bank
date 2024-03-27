class Account:
    name = ""
    surname = ""
    number = ""
    balance = 0
    interst_rate = 2
    password = ""


    def __init__(self, *args):
        self.name, self.surname, self.number, self.balance, self.interest_rate, self.password = args
