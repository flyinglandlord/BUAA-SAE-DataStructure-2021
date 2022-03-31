import urllib.request
from html.parser import HTMLParser
import pandas as pd
import openpyxl


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.sheet = []
        self.row = []
        self.entry = []
        self.tr = False
        self.td = False
        self.p = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.tr = True
            self.row = []
        elif tag == 'td':
            self.entry = []
            self.td = True
        elif tag == 'p':
            self.p = True

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.tr = False
            self.sheet.append(self.row)
        elif tag == 'td':
            tmp = ''
            for i in self.entry:
                tmp += i
            self.row.append(tmp)
            self.td = False
        elif tag == 'p':
            self.p = False

    def handle_data(self, data):
        if self.tr and self.td and self.p:
            self.entry.append(data.strip())


if __name__ == '__main__':
    URL = # URL here

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
              'Cookie' : # Your cookie here
              }

    request = urllib.request.Request(URL, headers=header)
    re = urllib.request.urlopen(request).read()

    print(re)