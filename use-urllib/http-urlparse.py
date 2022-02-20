#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import result
from urllib.parse import urlparse

result = urlparse("https://www.httpbin.org/index.html;user?id=100#comment")
print(type(result))
print(result)

"""
schema://netloc/path;params?query#fragment

ParseResult(scheme='https', netloc='www.httpbin.org', path='/index.html', params='user', query='id=100', fragment='comment')
"""
