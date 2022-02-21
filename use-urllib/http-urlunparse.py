#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import result
from urllib.parse import urlunparse, urlsplit, urlunsplit

data = ["https", "www.baidu.com", "index.html", "user", "a=1", "comment"]
print(urlunparse(data))

# url 构造
# https://www.baidu.com/index.html;user?a=1#comment

# url 拆分
result = urlsplit("https://www.baidu.com/index.html;user?a=1#comment")
print(result)

# SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='a=1', fragment='comment')

data1 = ["https", "www.baidu.com", "index.html", "a=1", "comment"]
print(urlunsplit(data1))