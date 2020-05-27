import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print ('Retrieving ', url)
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read().decode()

    print ('Retrieved', len(data), 'characters')
    json_data = json.loads(data)

    print ('Place id', json_data['results'][0]['place_id'])