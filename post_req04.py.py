#!/usr/bin/python

import requests
from pprint import pprint as pp
import os

from requests.api import post

url         = 'https://pastebin.com/api/api_post.php'
url2        = 'https://pastebin.com/api/api_post.php'
payload     = "{'username': 'jose', 'email':'jose@jose.com'}"
api_key     = os.getenv('PASTEBIN_KEY')

parameters  = {'api_dev_key': api_key,
               'api_option': 'paste',
               'api_paste_code': payload,
               'api_paste_format': 'python'}

post_req    = requests.post(url2, data=parameters)

status_req  = post_req.status_code

if status_req == 200:
    print('You got a successful POST request')
    print(f'The URL to check your POST: {post_req.text}')
else:
    print(status_req)
    print(api_key)
    print(post_req)
    