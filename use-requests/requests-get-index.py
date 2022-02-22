#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, re

r= requests.get('https://ssr1.scrape.center/')
pattern =re.compile('<h2.*?>(.*?)</h2>', re.S)
titles = re.findall(pattern, r.text)
print(titles)