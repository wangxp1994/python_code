# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/20 11:33

from spider import Spider
from multiprocessing import Process

# 保存路径
savePath = "C:\\Users\\Administrator\\Desktop\\彼岸\\"
# 首页
url_base = "http://pic.netbian.com/e/search/result/index.php?page=1&searchid=1224"

xpath_first = "//ul[@class='clearfix']/li/a"
url_second = "http://pic.netbian.com"
xpath_second = "//a[@id='img']/img/@src"
xpath_page = "//div[@class='page']/a/text()"
url_base = url_base.replace('page=1', 'page={}')


# 抓取index页
def getFirstSpider(page, parse_str):
	url_first = url_base.format(page)
	sp = Spider(
		url=url_first,
		parse_str=parse_str
	)
	sp()
	return sp


# 抓取info页
def getSecondSpider(href):
	sp = Spider(
		url=url_second + href,
		parse_str=xpath_second
	)
	sp()
	return sp


# 保存时名字异常,修改名字
def parseName(name):
	name = list(name)
	newName = []
	for i in name:
		if i.isalpha():
			newName.append(i)
	return "".join(newName)


def spiderMain(start, end):
	for page in range(start, end):
		sp1 = getFirstSpider(page, xpath_first)
		for ele in sp1.result:
			name = ele.xpath("b/text()")[0].strip()
			href = ele.xpath("@href")[0]

			sp2 = getSecondSpider(href)

			url = "http://pic.netbian.com/" + sp2.result[0]
			sp2.url = url
			sp2.getHtmlByRequest(beautiful=False)
			try:
				sp2.saveBytes(name="{}.jpg".format(name), path=savePath)
			except OSError:
				name = parseName(name)
				sp2.saveBytes(name="{}.jpg".format(name), path=savePath)

			print(name, "	>>> 已保存")


def run():
	sp_page = getFirstSpider(1, xpath_page)
	# 总页码数
	pageMax = int(sp_page.result[-2].strip())

	for i in range(1, pageMax, 100):
		end = i + 100
		if end > pageMax:
			end = pageMax + 1
		p = Process(target=spiderMain, args=(i, end,))
		p.start()




if __name__ == '__main__':
	run()
