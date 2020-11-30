
from test_delivery_charge import Delivery_order
from test_points import Points
from test_address import Address_Book

class Cart:

    def calculate_subtotal_before_tax(self):
        return 0
    def calculate_total_amount(self):
        return 0
    def change_status(self):
        return None
    def delivery_status(self):
        return None
class Tip:
    def add_tip_10_percent(self,total):
        return None
cart=Cart()
delivery_order = Delivery_order(cart.calculate_subtotal_before_tax(), cart.calculate_total_amount())
point=Points
def test_tip_amount():
    tip=Tip()
    assert tip.add_tip_10_percent(100)==10," tip amount should be 10% of toal amount if it is selected"

def test_cart_amount_valid():

    assert delivery_order.verify_delivery_order_valid()," delivery order amount before tax must be more than valid"
def test_points_deposit():
    assert cart.change_status()," after carts cleared, status shall change"
def test_added_delivery_charge():

    cart.calculate_total_amount()
    assert cart.delivery_status()==True," after delivery charge added to cart, order status change to delivery"













