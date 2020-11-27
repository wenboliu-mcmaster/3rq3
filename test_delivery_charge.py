class Delivery_order:
    def __init__(self,total_amount,subtotal_amount):
        self.total_amount=total_amount
        self.subtotal_amount=subtotal_amount

    def verify_delivery_charge(self):
        return None
def test_delivery_charge():
    delivery_order=Delivery_order(106,101)

    assert delivery_order.verify_delivery_charge()==delivery_order.total_amount-delivery_order.subtotal_amount," delivery cahrge should always be added"
def verify_delivery_charge_amount():
    delivery_order=Delivery_order
    assert delivery_order.verify_delivery_charge()==5 ,  "delivery charge should be $5"






