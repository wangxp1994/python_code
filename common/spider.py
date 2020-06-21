# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/05/18 10:42


import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from faker import Faker

skt = Faker("zh_CN")

class Spider(object):

    def __init__(self, url=None, headers=None, html_method="request",
                 parse_method="xpath", parse_str=None):
        self.__dict__.update({k:v for k,v in locals().items() if k != "self"})
        if not self.headers:
            self.headers = {
                "User-Agent": skt.chrome()
            }

    def __call__(self, html_method=None, parse_method=None, **kwargs):
        if not html_method:
            html_method = self.html_method
        if not parse_method:
            parse_method = self.parse_method

        html_dict = {
            "request": self.getHtmlByRequest
        }
        parse_dict = {
            "xpath": self.parseHtmlByXpath,
            "re": self.parseHtmlByRe,
        }
        html_dict[html_method](**kwargs)
        parse_dict[parse_method]()

    def __str__(self):
        return self.html

    def save(self, name='spider.html', path='../'):
        with open(path + name, 'w', encoding='utf8') as f:
            f.write(self.html)

    def saveBytes(self, name='file.x', path='../'):
        with open(path + name, 'wb') as f:
            f.write(self.html)

    def getHtmlByRequest(self, url=None, headers=None, beautiful=True, **kwargs):
        if not url:
            url = self.url
        if not headers:
            headers = self.headers

        headers.update(kwargs.get('params', {}))

        self.res = requests.get(url=url, headers=headers, ) # verify=False
        self.res.encoding = "utf8"
        self.html = self.res.content

        if beautiful:
            self.html = BeautifulSoup(self.res.content).prettify()
        return self.html

    def parseHtmlByXpath(self, parse_str=None, html=None):
        if not parse_str:
            parse_str = self.parse_str
        if not html:
            html = self.html

        etree_html = etree.HTML(html)
        self.result = etree_html.xpath(parse_str)
        return self.result

    def parseHtmlByRe(self, parse_str=None, html=None):
        if not parse_str:
            parse_str = self.parse_str
        if not html:
            html = self.html
        self.result = re.findall(parse_str, html)
        return self.result

if __name__ == '__main__':
    s = Spider(url="https://www.baidu.com/?tn=21002492_30_hao_pg")
    s.getHtmlByRequest()
    print(s)
    s.save()




