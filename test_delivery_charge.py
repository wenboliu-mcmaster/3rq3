class Delivery_order:
    def __init__(self,total_amount,subtotal_amount):
        self.total_amount=total_amount
        self.subtotal_amount=subtotal_amount
    def verify_delivery_order_valid(self):
        return 0
    def verify_delivery_charge(self):
        return 0
delivery_order=Delivery_order(106,101)
#this is to test requirement 6.2.2 	Delivery charges:
def test_deliverycharge():
    assert delivery_order.verify_delivery_charge()==delivery_order.total_amount-delivery_order.subtotal_amount," delivery cahrge should always be added"
def test_deliverycharge_amount():
    assert delivery_order.verify_delivery_charge()==5 ,  "delivery charge should be $5"








