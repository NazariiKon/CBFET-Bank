class Account:
    first_name = ""
    second_name = ""
    account_number = ""
    account_balance = 0
    interst_rate = 2
    password = ""


    def __init__(self, *args):
        self.first_name, self.second_name, self.account_number, self.account_balance, self.interest_rate, self.password = args
