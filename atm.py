class ATM(object):
    def __init__(self, card_no=None, pin_no=None, method=None):
        self.card_no = card_no
        self.pin_no = pin_no
        self.method = method
    def Methods(self, method, amount):
        if self.method == "Deposit":
            print(amount, " is deposited.")
        elif self.method == "Withdrawal":
            print(amount, " is withdrawn.")

bank_account = ATM("1234", "5678", "Withdrawal")
print(bank_account.Methods(bank_account.method, "500"))