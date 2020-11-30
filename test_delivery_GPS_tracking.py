from test_password import User_name
class GPS_Tracking:

    def update_GPS_tracking(self,order_number):
        return None
#this is to test requirement 6.2 GPS Tracking

def test_GPS_tracking():
    order_number = 123
    order_gps=GPS_Tracking()

    assert order_gps.update_GPS_tracking(order_number)==True," GPS tracking update progress"
