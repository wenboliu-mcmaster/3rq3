import math
class Password:
  def password_strength_test(self,entry_password):
      return None
  def password_alpha_test(self,entry_password):
      return False
  def password_digit_test(self,entry_password):
      return False
class User_name:
    def __init__(self):
        self.name={}

    def validate_user(self,items):
        return None
    def modify_address(self,address):
        return None
    def modify_password(self,password):
        return None
    def forget_password(self,email):
        return None
user_name = User_name()
# this is to test requirement 6.1.2	 Create your profile
def test_validate_user_password():
    valid_user_password={'liuwenbo':'abc1234567','hellohellohello':'123456fghd'}
    for item in valid_user_password:
        assert user_name.validate_user(item)==True,"valid user name and password shall pass"
def test_invalidate_user_password():
    invalid_user_password={'liuwenbo':'none','hellohellohello':'none'}
    for item in invalid_user_password:
        assert user_name.validate_user(item)==False, "invalid user name and password shall not pass"
# this is to test requirement 6.1.3	Modify your profile
def test_modify_address():
    new_address='3050 erin center blvd mississauga L5M0P5'
    assert user_name.modify_address(new_address)==new_address," new address should be saved"
# this is to test requirement 6.1.4 Forget Password
def test_mofify_password():
    new_password="123456789asdfcv"
    assert user_name.modify_password(new_password)==new_password,"new password should be saved"
# this is to test requirement 6.1.5  password reset
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





