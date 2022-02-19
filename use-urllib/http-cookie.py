#!/usr/bin/env python3
# coding:utf-8

from cgitb import handler
import http.cookiejar, urllib.request
from urllib import response

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("https://www.baidu.com")

for item in cookie:
    print(item.name + " = " + item.value)
