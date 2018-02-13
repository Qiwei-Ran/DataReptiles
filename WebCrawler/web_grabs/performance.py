#!/usr/bin/env python
# -*- coding:utf-8 -*-


import lxml.html
from bs4 import BeautifulSoup
from WebCrawler.download_urls.download_page1 import download
import time
import re

NUM_ITERATIONS = 1000
FIELDS = {'area'}


def regrex_grab(html):
    results = {}
    for filed in FIELDS:
        results[filed] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % filed, html).groups()[0]
    return results


def lxml_get_area(html):
    results = {}
    tree = lxml.html.fromstring(html)
    for field in FIELDS:
        results[field] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[
            0].text_content()  # tr/td位标签，#是ID,.是class, >表示子标签
    return results


def bs4_get_area(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_%s__row' % field).find('td', class_='w2p_fw').text
    print results


def performance(html):
    # noinspection SpellCheckingInspection
    for name, scraper in [('Regular', regrex_grab), ('Lxml', lxml_get_area), ('bs4', lxml_get_area)]:
        start = time.time()
        for i in range(NUM_ITERATIONS):
            if scraper == regrex_grab:
                re.purge()
            result = scraper(html)
            assert (result['area'] == '11,300 square kilometres'), 'area 不一致'
        end = time.time()
        print '%s: %.2f seconds' % (name, end - start)


if __name__ == '__main__':
    url = 'http://example.webscraping.com/places/default/view/Gambia-81'
    html = download(url, headers={}, proxy=None)
    performance(html)
