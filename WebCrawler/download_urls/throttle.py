#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse
import datetime
import time


class Throttle:
    """
    this is a class will implement the time delay for crawler.
    """

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        # 距离上次执行的时间，如果小于delay时间，表示还在睡眠中。睡眠完后执行该程序，然后更新时间，然后再睡眠
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now()
