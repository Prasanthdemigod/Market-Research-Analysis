import requests
import json

app_id = 'gNg5_Cw1dIfl4sw4LrvTfQ' # client ID
app_secret = 'mv2A2hZhrX2tLaH2TSqiEKXw8bsfX6HygknRFngMkwyGqmpI4rXmd6IMGprtkc9b' # client token
data = {'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret}
token = requests.post('https://api.yelp.com/oauth2/token', data=data)
access_token = token.json()['access_token']
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'bearer %s' % access_token}
params = {'location': 'San Bruno',
          'term': 'Japanese Restaurant',
          'pricing_filter': '1, 2',
          'sort_by': 'rating'
         }

resp = requests.get(url=url, params=params, headers=headers)

import pprint
#pprint.pprint(resp.json()['businesses'])

json_data = resp.json()

print json_data

with open('/home/prashanth/yelp/ydata.json', 'w') as outfile:
	json.dump(json_data, outfile)
