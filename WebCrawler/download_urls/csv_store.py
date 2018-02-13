import re
import lxml.html
from download_page1 import download
import csv


class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'country')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())

            print 'ok'
            self.writer.writerow(row)


# scrape_callback(url, html) is equal with scrape_callback.__call__(url, html)
def scrape_callback(url, html):
    fields = {'area'}
    print 'start'
    if re.search('/view/', url):
        print 're matching'
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[
                   0].text_content() for field in fields]
        print url, row


if __name__ == '__main__':
    url = 'http://example.webscraping.com/places/default/view/Gambia-81'
    html = download(url, headers={}, proxy=None)
    scrape_callback = ScrapeCallback()
    scrape_callback.__call__(url, html)
    # scrape_callback(url, html)
