# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/28 10:17

import re
import json
from multiprocessing import Manager, Process

from spider import Spider


# 用东方财富网, 抓取持仓信息
def getPositions(id):
	nUrl = "http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jjcc&code={}&topline=10&year=2020".format(id)
	sp = Spider(url=nUrl, parse_str='//tr/td[@class="tol"]/a/text()')
	sp()
	return sp


# 基金大全
def getFund1():
	res_list = []
	url = "http://www.southmoney.com/jijin/jijindaquan/"
	xpath_str = "//tr/td[@class]/a/text()"
	sp = Spider(url=url, parse_str=xpath_str)
	sp()
	for i in sp.result:
		ii = re.findall('\d{6}', i)
		if not ii:
			continue
		res_list.append(ii[0])

	return res_list


# 基金大全
def getFund2():
	res_list = []
	url = "http://fund.eastmoney.com/js/fundcode_search.js"
	re_str = '\["\d{6}","\w+","\w+","\w+","\w+"\]'
	sp = Spider(url=url, parse_str=re_str, parse_method="re")
	sp()
	for i in sp.result:
		ii = i[1:-1].replace('"', '')
		ii = ii.split(",")

		if ii[3] == "混合型":
			res_list.append(ii[0])

	return res_list


def save(dic):
	js = json.dumps(dic)

	with open("1.json", "w", encoding="utf8") as f:
		f.writelines(js + '\n')


def parse():
	f = open("1.json")
	dic = json.loads(f.read())
	l = sorted(dic, key=lambda x: dic[x], reverse=True)

	for i in l:
		print(i, dic[i])


def one_process(dic, fund_list, done_list):
	for fund in fund_list:
		if fund in done_list:
			continue
		done_list.append(fund)

		sp = getPositions(fund)
		for stock in sp.result:
			stock_ = stock.strip()
			if stock_ in dic:
				dic[stock_] += 1
			else:
				dic[stock_] = 1

		print(fund)

def work():
	fund_list = getFund2()
	done_list = Manager().list()
	dic = Manager().dict()

	process_list = []
	for i in range(10):
		p = Process(target=one_process, args=(dic, fund_list, done_list))
		process_list.append(p)
		p.start()

	for p in process_list:
		p.join()

	dic = dict(**dic)
	save(dic)


if __name__ == '__main__':
	# work()
	parse()