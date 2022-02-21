#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get("https://www.httpbin.org/get")
print(r.text)

"""
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "www.httpbin.org", 
    "User-Agent": "python-requests/2.27.1", 
    "X-Amzn-Trace-Id": "Root=1-6213b13c-10643ccc0602005357f9ec93"
  }, 
  "origin": "101.32.xxx.xxx", 
  "url": "https://www.httpbin.org/get"
}
"""

data = {"name": "testName", "age": 26}

r = requests.get("https://httpbin.org/get", params=data)
print(r.text)
