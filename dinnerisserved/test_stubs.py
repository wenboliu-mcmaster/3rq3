from dinnerisserved.discount import Discount

# Requirement: discount of 5% is applied when 5 or more items are in cart
# Requirement: sljakdflkj
def test_discount_five_percent():
    discount = Discount()
    calculated_discount = discount.calculate_discount(5)

    assert calculated_discount == 0.05, "discount should be 5%!"

# Requirement: discount of 10% is applied when 15 or more items are in cart
def test_discount_ten_percent():
    discount = Discount()
    calculated_discount = discount.calculate_discount(15)

    assert calculated_discount == 0.1, "discount should be 10%!"
