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

r = requests.get("https://httpbin.org/get")
print(type(r.text))
print(r.json())
print(type(r.json()))

"""
<class 'str'>
{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.27.1', 'X-Amzn-Trace-Id': 'Root=1-621439f6-64b84a4508d718e15154c815'}, 'origin': '112.21.27.79', 'url': 'https://httpbin.org/get'}
<class 'dict'>
"""
