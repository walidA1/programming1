import requests

auth_details = ('wavzaly@gmail.com', 'BUzy418n3IeT2CnfNbOOM8Qb_Wpz86LeMkWDWzUL4M4iWNvcJEFfkw')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

response = requests.get(api_url, auth=auth_details)
print(response.text)

