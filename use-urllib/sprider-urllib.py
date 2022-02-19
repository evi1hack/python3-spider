#!/usr/bin/env python3
# coding=utf-8

import urllib.request

response = urllib.request.urlopen("https://www.python.org")
# print(response.read().decode('utf-8'))

print("数据类型:", type(response))
print("\n")
print("状态码:", response.status)
print("\n")
print("headers:", response.getheaders())
print("\n")
print("Server:", response.getheader("Server"))

# response1 = urllib.request.urlopen()
