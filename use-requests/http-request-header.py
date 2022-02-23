#!/usr/bin/env python
# coding=utf-8

import requests

header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}

r = requests.get('https://ssr1.scrape.center/', headers=header)
# print(r.text)
data = {'name':'tesName', 'age':20}
r1 = requests.post('https://www.httpbin.org/post', data=data)
print(r1.text)
