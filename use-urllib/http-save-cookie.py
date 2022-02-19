#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

from cgitb import handler
from urllib import response
import urllib.request, http.cookiejar

filename = "cookie.txt"

cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
