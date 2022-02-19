#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import socket
# import urllib.parse
# import urllib.request
# import urllib.error

from urllib import parse, request, response

# data = bytes(urllib.parse.urlencode({'name': 'testName','password': 'passw0rd'}), encoding='utf-8')
# response = urllib.request.urlopen('http://www.httpbin.org/post', data=data)

# print(response.read().decode('utf-8'))

# print(response.read())


# try:
#     response = urllib.request.urlopen('http://www.httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e: //捕获超时异常
#     if isinstance(e.reason, socket.error): //判断是否为超时异常
#         print("TIME OUT")

url = "https://www.httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Host": "www.httpbin.org",
}
dict = {"name": "testName"}
data = bytes(parse.urlencode(dict), encoding="utf-8")
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))



