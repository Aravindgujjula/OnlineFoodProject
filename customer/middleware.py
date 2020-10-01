import requests
import json
from geopy.geocoders import Nominatim

myaddress = ""
city = ""

class LocaltionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        send_url = "http://api.ipstack.com/check?access_key=f8847d936deb1c40496b1d6dd89e51b1"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        city1 = geo_json['city']
        latlang = str(latitude) + "," + str(longitude)
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="OnlineFoodOrder")
        location = geolocator.reverse(latlang)

        global myaddress,city
        myaddress = location.address
        city = city1


    def __call__(self, request):
        response = self.get_response(request)
        return response


def returnAddress():
    return myaddress,city