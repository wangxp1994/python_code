
import requests
from lxml import etree
import xlwt
import re

class LSXXspider:
    def __init__(self):

        # 拼接起始网址
        self.baseUrl = "http://cbs.cau.edu.cn"
        # 开始爬取的第一个网址
        self.url = "http://cbs.cau.edu.cn/col/col31715/index.html"
        # xpath先定义
        self.x1 = '//li/a/@href'
        self.x2 = '//tr/td[@align]/text()'


        # 邮箱的正则表达式
        self.reg_str = r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+'
        # 操作表格
        self.wbk = xlwt.Workbook()
        self.pen = self.wbk.add_sheet(u"Sheet1")
        # 请求头信息
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0;Trident/4.0)'}

    # 得到网页
    def getHtml(self, url):
        res = requests.get(url=url, headers=self.headers) 
        return res.content

    # 使用xpath获取内容
    def getInfo(self, html, xpath_str):
        html = etree.HTML(html)
        result = html.xpath(xpath_str)
        return result

    # 使用正则表达式获取邮箱
    def getEmail(self, html):
        try:
            result = re.findall(self.reg_str, html)
            return result[0]
        except:
            return "待查"

    # 数据清洗
    def clean(self, name, email):

        return name.strip(), email.strip()

    def lstClean(self, lst):
        lst2 = []
        for u in lst:
            if u.startswith("/art/"):
                u = self.baseUrl + u
                lst2.append(u)
        return lst2


    def workOn(self):
        # 表格首行
        self.pen.write(0, 0, "老师姓名")
        self.pen.write(0, 1, "邮箱")
        # 解析首页名字中网址        
        content = self.getHtml(self.url)
        lst = self.getInfo(content, self.x1)
        lst = self.lstClean(lst)


        n = 1
        for u in lst:
            # 获取老师信息详情页
            url = u

            content = self.getHtml(url)
            # 获取老师名字
            name = self.getInfo(content, self.x2)[0]
            # 获取老师邮箱
            email = self.getEmail(content)
            # 数据清洗
            name, email = self.clean(name, email)
            # 添加到表格中
            if name and email:
                self.pen.write(n, 0, name)
                self.pen.write(n, 1, email)
                print(n+1, name, u)
                n += 1

        # 保存表格
        self.wbk.save("test.xls")

if __name__ == "__main__":
    lsxx = LSXXspider()
    lsxx.workOn()
    print("That's OK!")