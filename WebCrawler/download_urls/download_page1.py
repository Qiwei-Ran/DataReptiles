#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import itertools
import urlparse
import Queue
import robotparser
from throttle import Throttle


# 下载网页
def download(url, headers, proxy, num_retries=2, data=None):
    print 'Downloading: %s' % url
    request = urllib2.Request(url, data, headers)  # 构建请求request对象
    opener = urllib2.build_opener()  # 构建一个打开url的对象，打开器

    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}  # 代理参数，使用代理协议
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)  # 使用请求打开页面
        html = response.read()  # 读取web内容
        code = response.code  # 获取状态码
    except urllib2.URLError as e:
        print 'url error:', e.reason
        html = ''

        if hasattr(e, 'code'):  # 根据错误的代码来进行重试
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                return download(url, headers, proxy, num_retries - 1, data=None)  # 参数不变，只是重试减1
        else:
            code = None
    return html


# 爬取站点地图的url（正则搜索下载的文件中的url）
def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<a href="(.*?)">', sitemap)
    print "ok"
    for link in links:
        print "url: %s" % link


# 正则获取下载的Master网页中的字url,列表
def get_link(html):
    """
    :param html: A web page code.
    :return: list of url
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


# 判断俩url网络位置是否一样
def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc


# 解析根站点url文件，判断哪些url不可爬
def get_robots(url):
    """
    :param url:
    :return: Return rp对象
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp


def normalize(seed_url, link):
    link, _ = urlparse.urldefrag(link)
    return urlparse.urljoin(seed_url, link)


# 从get_link中取得的url中。，筛选自己想要的url并下载
# 增加爬网页深度的功能,深度就是允许下载重复的完全相同的url地址的次数，也就是避免类似日历一样的爬虫陷阱
def link_crawler(seed_url, link_regex=None, delay=10, headers=None, max_depth=2, max_urls=1, user_agent='wswp',
                 proxy=None, num_retries=1):
    """
    :param seed_url: a list of master url
    :param link_regex: you wanna filter the url
    :return: a list of contain master_url and sub url
    """
    crawl_queue = Queue.deque([seed_url])  # 还需要被爬取的url， 类似一个列表
    seen = {seed_url: 0}  # 用于存储根url深度，默认为0，以及其他子url的深度
    num_urls = 0  # 跟踪已经下载的url的数量
    # robots file parse for get really url
    rp = get_robots(seed_url)
    # 生成延时器对象
    throttle = Throttle(delay)
    # 请求头字典
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent  # 将自定义的用户请求头添加到字典中

    while crawl_queue:  # 只要crawl_queue没被pop从后向前取完，就执行循环
        url = crawl_queue.pop()  # 只取最新的url，由append而来的,取一次少一次。本次爬取的url
        if rp.can_fetch(user_agent, url):  # 判断是否可爬，如果是False是不能爬的
            throttle.wait(url)  # 进行限时，10秒
            html = download(url, headers, proxy=proxy, num_retries=num_retries)  # 下载网页

            links = []  # 用来存储匹配到的子url
            depth = seen[url]  # 取seen这个字典的url的值，其值为深度数字。url为本次爬取的url，取得是本次url的深度值
            if depth != max_depth:  # 控制深度来决定加入待爬队列中的链接深度，没达到深度就可以往crawl_queue里append
                if link_regex:
                    links.extend(link for link in get_link(html) if re.match(link_regex, link))  # 将子url扩展到列表

                for link in links:  # 遍历links列表中的url
                    link = normalize(seed_url, link)  # 将url碎片与根url拼接成完整的链接
                    if link not in seen:  # 有一个新link， 原url深度+1并赋值给link的深度。可以记录该条link是url的第几层，或者第几个次子链接
                        seen[link] = depth + 1  # 深度，url与link之间的相似度，如相似度一样，就表示重复，深度为+1。存下次要下载的深度值
                        if same_domain(seed_url, url):  # 判断domain是否一样，即是域名+端口
                            crawl_queue.append(link)  # 将链接加到待爬的队列中

            # 该link链接是根链接的一个子链接，将子链接加到待爬的队列中，然后num_urls通过控制总的下载次数，来确定爬多少个url，也就是深度
            num_urls += 1  # 控制下载次数
            if num_urls == max_urls:  # 控制循环的次数
                break
        else:
            print 'Blocked by robots.txt:', url
    print seen


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1,
                 user_agent='GoodCrawler')

    '''
    url = 'http://example.webscraping.com'
    link_crawler(url, '/places/default/(index|view)/')
    '''

    '''
    url = 'http://example.webscraping.com'
    url = 'http://httpstat.us/500'
    # url = 'http://www.meetup.com'
    download(url)
    '''

    '''
    url = 'http://example.webscraping.com/sitemap.xml'
    crawl_sitemap(url)
    '''

    '''
    max_errors = 5
    num_errors = 0
    for page_num in itertools.count(1):
        url = url = 'http://example.webscraping.com/places/default/view/%d' % page_num
        html = download(url)
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                print '空白'
                break
        else:
            num_errors = 0
            print 'ok'
            pass
    '''
