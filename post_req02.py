#!/usr/bin/python 


import requests
from pprint import pprint as pp


url         = 'https://httpbin.org/post'

files       = {'files': open('test.txt', 'rb')}
values      = {'upload_file' : 'test.txt', 'OUT':'csv'}

# print(files)

post_req    = requests.post(url, files=files,data=values)

status_req  = post_req.status_code
content_req = post_req.text

print(status_req)
pp(content_req)