#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unicodedata import category
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


# 页面爬取方法
def scrape_page(url):

    logging.info("scraping %s ...", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error(
            "get invalid status code %s while scraping %s", response.status_code, url
        )
    except requests.RequestException:
        logging.error("error on scraping %s", url, exc_info=True)


# 爬取列表页
def scrape_index(page):
    index_url = f"{BASE_URL}/page/{page}"
    return scrape_page(index_url)


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


# 爬取详情页
def scrape_detail(url):
    return scrape_page(url)  # 返回详情页HTML


# 解析详情页
def parse_detail(html):
    # 定义正则规则
    cover_pattern = re.compile(
        'class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S
    )
    name_pattern = re.compile('<h2.*?class="m-b-sm">(.*?)</h2>')
    categories_pattern = re.compile(
        "<button.*?category.*?<span>(.*?)</span>.*?</button>", re.S
    )
    published_at_pattern = re.compile("(\d{4}-\d{2}-\d{2})\s?上映")
    drama_pattern = re.compile("<div.*?drama.*?>.*?<p.*?>(.*?)</p>", re.S)

    score_pattern = re.compile("<p.*?score.*?>(.*?)</p>", re.S)

    # 使用re提取
    cover = (
        re.search(cover_pattern, html).group(1).strip()
        if re.search(cover_pattern, html)
        else None
    )
    name = (
        re.search(name_pattern, html).group(1).strip()
        if re.search(name_pattern, html)
        else None
    )
    categories = (
        re.findall(categories_pattern, html)
        if re.findall(categories_pattern, html)
        else []
    )
    published_at = (
        re.search(published_at_pattern, html).group(1)
        if re.search(published_at_pattern, html)
        else None
    )
    drama = (
        re.search(drama_pattern, html).group(1).strip()
        if re.search(drama_pattern, html)
        else None
    )
    score = (
        float(re.search(score_pattern, html).group(1).strip())
        if re.search(score_pattern, html)
        else None
    )

    return {
        "cover": cover,
        "name": name,
        "categories": categories,
        "published_at": published_at,
        "drama": drama,
        "score": score,
    }


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_html = scrape_index(page)
        detail_urls = parse_index(index_html)
        # logging.info("detail urls %s", list(detail_urls))
        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)
            data = parse_detail(detail_html)
            logging.info("get detail data %s", data)


if __name__ == "__main__":
    main()
