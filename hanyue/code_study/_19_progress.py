# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/07/18 15:32

import sys
import time

def progress_one():
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)

def progress_two():
	scale = 50
	print("执行开始，祈祷不报错".center(scale // 2,"-"))
	start = time.perf_counter()
	for i in range(scale + 1):
		a = "*" * i
		b = "." * (scale - i)
		c = (i / scale) * 100
		dur = time.perf_counter() - start
		print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
		time.sleep(0.1)
	print("\n"+"执行结束，万幸".center(scale // 2,"-"))

def progress_three():
	from tqdm import tqdm, trange

	for i in tqdm(range(1, 100)):
	   time.sleep(0.01)

	for i in trange(1, 100):
	   time.sleep(0.01)

	pbar = tqdm(range(1, 100))
	for char in pbar:
		# 设置描述
		pbar.set_description("Processing %s" % char)
		time.sleep(0.01)

	# 一共100个，每次更新1，一共更新100次
	with tqdm(total=100) as pbar:
		for i in range(100):
			pbar.update(1)
			time.sleep(0.01)

	bar = trange(100)
	for i in bar:
		time.sleep(0.01)
		if not (i % 5):
			tqdm.write("Done task %i" % i)



if __name__ == '__main__':
    # progress_one()
	# progress_two()
	progress_three()
