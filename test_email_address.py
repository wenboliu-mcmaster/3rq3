class Email:

    def email_update(self,old,new):
        return None
    def email_format_valid(self,symbols):
        return None
    def email_change_valid(self,symbols):
        return None

def test_email_format_invalid():
    email=Email()
    unaccepted_symbol=[
        ',',
        '!',
        "$"
    ]
    for items in unaccepted_symbol:
        assert email.email_format_valid(items)==False," these are the invalid  symbols"
def test_email_format_valid():
    email=Email()
    required_symbols=[
        ".",
        '@',
    ]
    for items in required_symbols:
        assert email.email_format_valid(items)==True,"these are required symbols for emails to be valid"
def test_new_email():
    email=Email()
    old="liu123@gmail.com"
    new="liu.@gmaill.com"
    assert email.email_update(old,new)==new, "the old email address will be updated by new one"


