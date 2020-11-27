
class Address_Book:
    def postcode_check(self,postcode):
        if postcode== 'L5M':
            return False


def address_check():
    address=Address_Book()
    assert address.postcode_check('L5M')==True
