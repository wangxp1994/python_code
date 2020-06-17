# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/08 15:03

from django.conf.urls import url
from django.urls import path, re_path

from .views import *

urlpatterns = [
	# 指定views的参数和参数类型
	path(r'date/<int:year>/<int:month>/<int:day>/<words>', date_views),
	# 正则表达式匹配 使用较复杂
	re_path(r'birday/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<words>[\u4e00-\u9fa5]+)', birday_views),

	# 文件上传下载测试
	path(r'download/<filename>', download_views),
	path(r'picture/<filename>', picture_views),
	path(r'delete/<filename>', delete_views),
	path(r'update/<filename>', update_views),
	path(r'up', up_views),

	url(r'', index_views),
	url(r'^index/$', index_views),
]