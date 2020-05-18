import requests
from lxml import etree

class BZspider(object):

    def __init__(self):
        self.headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}        
        self.baseurl = "http://pic.netbian.com/4kmeinv/"

        self.url1 = 'http://pic.netbian.com'

        self.xpStr1 = '//ul[@class="clearfix"]/li/a/@href'
        self.xpStr2 = '//div[@class="photo-pic"]/a/img/@src'

        self.dir = "复习//19_05_09//壁纸下载//"
    
    def getParsePage(self,url,xpStr=None,img=False):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"

        if img:
            return res.content

        html = res.text       

        parseHtml = etree.HTML(html)
        rList = parseHtml.xpath(xpStr)

        return rList


    def saveImg(self,content,name):
        with open(self.dir+name,"wb") as f:
            f.write(content)
        print(name+"已经保存")

    def workOn(self,m1,m2):
        for n in range(m1,m2):
            baseurl = self.baseurl
            if n>1:
                baseurl += "/index_{}.html".format(n)
                
            lst1 = self.getParsePage(baseurl,self.xpStr1)

            for u in lst1:
                url = self.url1 + u
                imgUrl = self.getParsePage(url,xpStr=self.xpStr2)[0]
                
                content = self.getParsePage(self.url1+imgUrl,img=True) 

                name = imgUrl.split("/")[-1]

                self.saveImg(content,name)       

if __name__=="__main__":
    bz = BZspider()
    bz.workOn(1,5)