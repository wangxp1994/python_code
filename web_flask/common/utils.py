# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/07/01 9:46

import re


def type_re(obj):
	str_ = str(type(obj))
	return re.findall("'(\w+)'", str_)[0]