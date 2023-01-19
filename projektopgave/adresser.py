# https://requests.readthedocs.io/en/latest/user/quickstart/

import requests

# Adresse data

# https://dataforsyningen.dk/data/4729

api_url = 'https://api.dataforsyningen.dk/'
endpoint = 'adresser'

params = {
    'vejnavn'       : 'Telegrafvej',
    'husnr'         : '9',
    'postnrnavn'    :  'Ballerup',
    'struktur'      : 'mini',
    }

respons = requests.get(api_url+endpoint, params)

print(respons)
print("Response status:", respons.status_code)

if respons.status_code == 200:
    print(respons.json())
    rjson = respons.json()[0]
    print("Latitude (bredde):", rjson['x'])
    print("Longitude (længde):", rjson['y'])