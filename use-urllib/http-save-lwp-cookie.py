#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cgitb import handler
from urllib import response
import urllib.request, http.cookiejar

filename = "lwp-cookie.txt"

# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)  # LWP格式 cookie
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("https://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
