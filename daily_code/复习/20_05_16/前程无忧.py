# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/5/16 13:50

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

base_url = "https://search.51job.com/list/180200,000000,0000,00,9,99," \
           "%25E5%25B5%258C%25E5%2585%25A5%25E5%25BC%258F%25E8%25BD%25AF%25E4%25BB%25B6%25E5%25BC%2580%25E5%258F" \
           "%2591,2,{}.html?lang=c&postchannel=0000&workyear=04&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

# 获取节点的xpath
x_str = r'//div[@class="dw_table"]/div[@class="el"]'

# 获取公司地址的re
re_str = """<p class="fp">
        <span class="label">
         上班地址：
        </span>
        (.*)
       </p>
"""

# 获取网页
def getHtml(url):
    res = requests.get(url=url, headers=headers)
    res.encoding = "utf8"
    html = res.content
    html = BeautifulSoup(html).prettify()
    return html

# xpath解析
def getEle(html, x_str):
    html = etree.HTML(html)
    result = html.xpath(x_str1)
    return result

# 爬取网页
def work():
    global headers
    lst = []
    for i in range(1, 5):
        url = base_url.format(i)
        html = getHtml(url)
        eles = getEle(html, x_str1)

        for ele in eles:
            job = ele.xpath(r"p/span/a/text()")[0].strip()
            comp = ele.xpath(r"span/a/text()")[0].strip()
            money = ele.xpath(r'span[@class="t4"]/text()')[0].strip()

            c_url = ele.xpath(r"p/span/a/@href")[0].strip()
            headers['Referer'] = url
            c_html = getHtml(c_url)
            try:
                add = re.findall(re_, c_html)[0]
            except:
                add = "-------"
            print(job, comp, add, money)
            lst.append([job, comp, add, money])
    save(lst)

# 保存为txt
def save(lst):
    s = ""
    for i in lst:
        string = "**".join(i)
        string += "\n"
        s += string
    with open("test.txt", "a", encoding="utf8") as f:
        f.write(s)

# 保存到表格
def work2():
    import  xlwt
    fname = "前程无忧-武汉嵌入式开发岗位.xls"
    wbk = xlwt.Workbook()
    pen = wbk.add_sheet("1-3年")
    writeExcel(pen, "1-3.txt")
    wbk.save(fname)

# 表格编写
def writeExcel(pen, name):
    with open(name, "r", encoding="utf-8") as f:
        lst = f.readlines()

    pen.write(0, 0, "编号")
    pen.write(0, 1, "岗位")
    pen.write(0, 2, "公司")
    pen.write(0, 3, "地址")
    pen.write(0, 4, "薪资范围")

    for n, i in enumerate(lst, 1):
        ii = i.split("**")
        pen.write(n, 0, n)
        pen.write(n, 1, ii[0])
        pen.write(n, 2, ii[1])
        pen.write(n, 3, ii[2])
        pen.write(n, 4, ii[3])


if __name__ == '__main__':
    work()
    work2()





