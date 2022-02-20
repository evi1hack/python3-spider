#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, error, response

try:
    response = request.urlopen("http://httpbin.org/404")
except error.URLError as e:
    print(e.reason)
