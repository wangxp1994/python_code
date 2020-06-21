# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/20 14:29
import os
import requests
from spider import Spider

url = "http://127.0.0.1:8000/review/up"
savePath = "C:\\Users\\Administrator\\Desktop\\彼岸\\"
xpath_str = "//input[@name='csrfmiddlewaretoken']/@value"

def upOne(name):
	sp = Spider(
		url = url,
		parse_str = xpath_str
	)
	sp()
	value = sp.result[0]
	files = {
		"file": (name, open(savePath + name, 'rb'), "image/jpeg")
	}

	data = {
		"words":name,
		"csrfmiddlewaretoken":value
	}

	cookie = ''
	for name, value in sp.res.cookies.items():
		cookie += '{0}={1};'.format(name, value)

	sp.headers.update({
		"Cookie": cookie,
	})
	requests.post(url=url, headers=sp.headers, files=files, data=data)

if __name__ == '__main__':
	listdir = os.listdir(savePath)

	for i in listdir:
		upOne(i)