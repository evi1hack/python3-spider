#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import response
import requests
import logging
import re
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)

BASE_URL = "https://ssr1.scrape.center"
TOTAL_PAGE = 10


# 爬取列表页
def scrape_index(page):
    index_url = f"{BASE_URL}/page/{page}"
    return scrape_page(index_url)


# 页面爬取方法
def scrape_page(url):
    logging.info("scraping %s ...", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error(
            "get invalid status code %s while scraoing %s", response.status_code, url
        )
    except requests.RequestException:
        logging.error("error on scraping %s", url, exc_info=True)


# 解析列表页
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info("get detail url %s", detail_url)
        yield detail_url


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        logging.info("detail urls %s", list(detail_urls))


if __name__ == "__main__":
    main()
