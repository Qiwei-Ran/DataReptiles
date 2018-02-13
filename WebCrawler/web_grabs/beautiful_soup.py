#!/usr/bin/env python
# -*-coding:utf-8-*-

from bs4 import BeautifulSoup
from WebCrawler.download_urls.download_page1 import download
import lxml.html


def bs4_test():
    """test
    """
    broken_html = '<ul class=country><li>Area<li>Population</url>'
    soup = BeautifulSoup(broken_html, 'html.parser')  # 补全修复标签
    fixed_html = soup.prettify()  # 优化标签显示方式
    print fixed_html


def bs4_get_area(url):
    html = download(url, headers={}, proxy=None)
    soup = BeautifulSoup(html, 'html.parser')
    tr = soup.find(attrs={'id': 'places_area__row'})
    td = tr.find(attrs={'class': 'w2p_fw'})
    area = td.text
    print area


def lxml_test(broken_url):
    tree = lxml.html.fromstring(broken_url)  # parse the HTML,填补缺陷
    fixed_html = lxml.html.tostring(tree, pretty_print=True)  # 转换为字符串，优美输出
    print fixed_html


def lxml_get_area(url):
    html = download(url, headers={}, proxy=None)
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]  # tr/td位标签，#是ID,.是class, >表示子标签
    area = td.text_content()  # 选取内容
    return area


if __name__ == '__main__':
    # bs4_test()

    url = 'http://example.webscraping.com/places/default/view/Gambia-81'
    result = lxml_get_area(url)
    print result
    '''
    broken_url = '<ul class=country><li>Area<li>Population</url>'
    lxml_test(broken_url)
    '''

    '''
    url = 'http://example.webscraping.com/places/default/view/Gambia-81'
    bs4_get_area(url)
    '''
