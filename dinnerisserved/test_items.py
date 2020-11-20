from dinnerisserved.menuitem import MenuItem
from dinnerisserved.cart import Cart


def test_add_item_to_cart():
    cart = Cart()
    assert len(cart) == 0, "the cart should start out empty"

    item = MenuItem("steak")
    cart.add_item(item)

    assert len(cart) == 1, "the cart should contain exactly 1 item"


def test_add_invalid_item_to_cart():
    cart = Cart()
    assert len(cart) == 0, "the cart should start out empty"

    item = MenuItem("steak")
    item.invalidate_item()
    cart.add_item(item)

    assert len(cart) == 0, "the cart should not add an invalid item"


def test_adding_invalid_item_sends_error():
    cart = Cart()
    assert len(cart) == 0, "the cart should start out empty"

    item = MenuItem("steak")
    item.invalidate_item()
    message = cart.add_item(item)

    assert message == "this item is invalid!", "should have received an invalid message"


def test_adding_multiple_items_to_cart():
    cart = Cart()
    assert len(cart) == 0, "the cart should start out empty"

    items = [MenuItem("steak"), MenuItem("potatoes"), MenuItem("side of greens")]
    cart.add_items(items)
    assert len(cart) == 3, "the cart should now have 3 items"

    new_item = MenuItem("ketchup")
    cart.add_item(new_item)
    assert len(cart) == 4, "including ketchup, we should have 4 items"
