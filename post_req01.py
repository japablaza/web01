#!/usr/bin/python 

import requests
from pprint import pprint as pp


url             = 'https://en.wikipedia.org/w/index.php'
url2            = 'https://en.wikipedia.org/wiki/Main_page'
data            = {'search': 'Skillsoft'}

post_req        = requests.post(url, data)

status_reques   = post_req.status_code
status_req_type = type(status_reques)
content_body    = post_req.text

# pp(content_body)

with open('skillsoft3.html', 'wb') as file:
    for lineas in post_req.iter_content(chunk_size=10000):
        file.write(lineas)