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

    def __init__(self, url=None, parse_str=None, headers=None, **kwargs):
        self.__dict__.update({k:v for k,v in locals().items() if k not in ["self", "kwargs"]})
        self.__dict__.update(kwargs)
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
            "re": self.parseHtmlByRe
        }
        html_dict[html_method](**kwargs)
        parse_dict[parse_method]()

    def getHtmlByRequest(self, url=None, headers=None, **kwargs):
        if not url:
            url = self.url
        if not headers:
            headers = self.headers

        res = requests.get(url=url, headers=self.headers)
        res.encoding = "utf8"
        self.html = BeautifulSoup(res.content).prettify()
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
    s = Spider()
    print(s("https://www.baidu.com/", Host="www.baidu.com"))





