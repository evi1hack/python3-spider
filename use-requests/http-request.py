#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# r = requests.get("https://www.httpbin.org/")
r = requests.get("https://www.baidu.com/")
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text[:100])
print(r.cookies)


"""
<class 'requests.models.Response'>
200
<class 'str'>
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charse
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>

"""

r1 = requests.get('https://scrape.center/favicon.ico')
# print(r1.text)
# print(r1.content)
with open('favicon.ico', 'wb') as f:
    f.write(r1.content)
