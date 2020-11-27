import math
class Password:


  def password_strength_test(self,entry_password):
      if len(entry_password)<8:
          print ("please enter valid length at least 8")
          return False

  def password_alpha_test(self,entry_password):
      return False
  def password_digit_test(self,entry_password):
      return False
def test_password_strength():
    password = Password()
    assert password.password_strength_test('123456')==False," the password should have length of at least 8"
    assert password.password_alpha_test('123456')==False, "the password should have alphabet"
    assert password.password_digit_test("abcdefghjj")==False, 'the password should have digit'
