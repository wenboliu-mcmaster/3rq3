class Points:
    def __init__(self):
        self.balance=0
    def deposit(self,sale_amount):
        self.balance=self.balance +sale_amount

    def redeem(self,credit):
        self.balance=self.balance-credit
    def display_balance(self):
        return self.balance

def test_points():
    point=Points()
    point.deposit(100)
    assert point.display_balance()==100
    point.redeem(50)
    assert point.display_balance()==50

