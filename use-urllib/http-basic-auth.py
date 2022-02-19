#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cgitb import reset
from operator import imod
from unittest import result
from urllib.request import (
    HTTPPasswordMgrWithDefaultRealm,
    HTTPBasicAuthHandler,
    build_opener,
)
from urllib.error import URLError

username = "admin"
password = "admin"
url = "https://ssr3.scrape.center/"

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)


try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    # print(result.getheaders())
    if result.status == 200:
        print(username, password)
except URLError as e:
    print(e.reason)
