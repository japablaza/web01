#!/usr/bin/python

import requests
from pprint import pprint as pp
import json

pp(requests.__version__)
pp(requests.__copyright__)

sw_url      = 'http://swapi.dev/api/starships/9/'
url         = 'https://www.metaweather.com/api/location/2487956/2018/11/28'
get_request = requests.get(url)
status_code = get_request.status_code
data        = json.loads(get_request.text)
# pp(data)
pp(get_request.is_redirect)
sw_request  = requests.get(sw_url)
ship9       = sw_request.text
pp(ship9)
