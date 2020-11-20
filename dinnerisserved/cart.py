class Cart:
    def __init__(self):
        self.cart = []

    def __len__(self):
        return len(self.cart)

    def add_item(self, item):
        if item.valid:
            self.cart.append(item)
        else:
            return "this item is invalid!"

    def add_items(self, items):
        for item in items:
            self.cart.append(item)
