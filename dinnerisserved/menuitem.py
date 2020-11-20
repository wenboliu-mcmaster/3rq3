class MenuItem:
    def __init__(self, name):
        self.name = name
        self.valid = True

    def invalidate_item(self):
        self.valid = False
