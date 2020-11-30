from test_password import User_name
class Menu:

    def modify_menu(self):
        return None
    def acess_control(self,user_name):
        return None
menu=Menu()
# this is to test requirement of 6.1 Administor authority
def test_administor_access_control():

    administor=User_name()
    assert menu.acess_control(administor)==True," only administor is allowed to modify menu acess"
def test_regular_user_access():
    kitch_staff=User_name()
    assert menu.acess_control(kitch_staff)==False,"kitchen staff is not allowed to modify nemu"




