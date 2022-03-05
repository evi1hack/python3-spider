#!/usr/bin/env python
# coding=utf-8

import httpx

response = httpx.get('https://www.httpbin.org/get')
print(response.status_code)
print(response.text)