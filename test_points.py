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
    assert point.display_balance()==0,  " all user shall start with 0 points "
def test_points_increase():
    point = Points()
    point.deposit(100)
    assert point.display_balance()==100, "after order of $100, the points shall increase by 100"
def test_points_reddem():
    point = Points()
    point.redeem(50)
    assert point.display_balance()==-50," after redemption of #50, the points shall decrease by 50"

