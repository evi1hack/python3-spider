#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get("http://www.httpbin.org/get")
print(r.text)
r = requests.post("http://www.httpbin.org/post")
print(r)
r = requests.put("http://www.httpbin.org/put")
print(r)
r = requests.delete("http://www.httpbin.org/delete")
print(r)
r = requests.patch("http://www.httpbin.org/patch")
print(r)
