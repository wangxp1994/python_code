# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/21 18:10

import re

f = open("re_file.txt", 'r', encoding="utf8")
content = f.read()

# re的两种使用方法
# 1
# >>> p = re.compile(r'正则表达式')
# >>> rList = p.findall(content)
# 2
# rList = re.findall(r'正则表达式',content)

# a b c d ...  : 普通元字符
# | : 或
# ^ : 匹配目标字符串的开始位置
# $ : 匹配目标字符串的结束位置
# * : 前面字符出现0次或多次
# + : 前面的一个字符出现1次或多次
# ? : 前面的1个字符出现0次或1次
# {n} : 前面的1个字符出现n次
# {m,n} : 前面的1个字符出现m-n次
# . : 匹配任意1个字符(不包括换行符\n)

# [abc123] : a b c 1 2 3
# [a-z] : 所有小写字母
# [A-Z] : 所有大写字母
# [0-9] : 数字
# [a-zA-Z0-9]_ : 数字,字母,下划线
# [^abc] : 除a b c之外的字符
# \d : 任意1个数字
# \D : 任意1个非数字字符
# \w : 匹配数字,字母,_
# \W : 匹配特殊字符
# \s : 空白字符[ \n\t\v\r]
# \S : 非空白字符
# [\s\S] : 匹配所有字符(包括\n)

# [\u4e00-\u9fa5] : 中文

# re_str = r'[A-Z].*\.'
re_str = r'[.| ]([\u4e00-\u9fa5].*[\u4e00-\u9fa5])'

res = re.findall(re_str, content)

for i in res:
	print(i)

f.close()

