import math
class Password:


  def password_strength_test(self,entry_password):
      return None
#      if len(entry_password)<8:
#          print ("please enter valid length at least 8")
#         return False

  def password_alpha_test(self,entry_password):

      return False
  def password_digit_test(self,entry_password):
      return False
def test_password_strength():
    password = Password()
    entry_password=[
        '12345698000',
        'asdfgh23344',
        'none3345gh',
    ]

    for entry in entry_password:
        if len(entry)>9:
            assert password.password_strength_test(entry) == True," password format should have a length of more than 9"
def test_password_alph():
    password = Password()
    entry_password=[

        'asdfgh23344',
        'none3345gh',
    ]
    for entry in entry_password:
        assert password.password_alpha_test(entry) == True," password format should has at least 1 alphabetic"
def test_password_digit():
    password = Password()
    entry_password = [

        'asdfgh23344',
        'none3345gh',
    ]
    for entry in entry_password:
        assert password.password_digit_test(entry), "password format should have at least 1 digit"


##    assert password.password_strength_test('123456')==False," the password should have length of at least 8"
#    assert password.password_alpha_test('123456')==False, "the password should have alphabet"
 #   assert password.password_digit_test("abcdefghjj")==False, 'the password should have digit'
