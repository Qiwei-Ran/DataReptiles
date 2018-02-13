#!/usr/bin/env python
# -*-coding:utf-8-*-

import re
from WebCrawler.download_urls.download_page1 import download

# FIELDS = {'area', 'population', 'iso', 'country'}
FIELDS = {'area'}


def regrex_grab(url):
    html = download(url, headers={}, proxy=None)
    # result = re.findall('<td class="w2p_fw">(.*?)</td>', html)
    # print result[1]

    results = {}
    for filed in FIELDS:
        results[filed] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % filed, html).groups()[0]
    return results


if __name__ == '__main__':
    url = 'http://example.webscraping.com/places/default/view/Gambia-81'
    print regrex_grab(url)
