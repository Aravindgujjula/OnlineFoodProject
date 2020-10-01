# import requests
# import json
#
#
# send_url = "http://api.ipstack.com/check?access_key=f8847d936deb1c40496b1d6dd89e51b1"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city1 = geo_json['city']
#
#
# print(city1)

import random

res = random.randint(100000,999999)

print(res)