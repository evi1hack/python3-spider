#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTTPError

from urllib import request, error, response

try:
    # response = request.urlopen("https://httpbin.org/404")
    response = request.urlopen("https://httpbin.org/get")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfully!")
