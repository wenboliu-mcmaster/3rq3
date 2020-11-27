
class Address_Book:
    def postcode_check(self,postcode):
        return None

def test_address_check():

    valid_Address_postcode = [
        'L5M0P3',
        'L5M0P4',
        'L5M0P2',
    ]
    address = Address_Book()
    for postcode in valid_Address_postcode:

        assert address.postcode_check(postcode)==True,'The address is within 10km radius of store'

def test_address_check_invalidaddress():
    invalid_address_postcode = [
        'L4M0O1',
        'L3M0P2',
    ]
    address = Address_Book()
    for postcode in invalid_address_postcode:
        assert address.postcode_check(postcode)==False," the address is out of 10km radius of store"