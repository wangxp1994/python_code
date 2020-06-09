# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/08 15:03

from django.conf.urls import url

from url_test.views import *

urlpatterns = [
	url(r'^index/$', index),
    url(r'', index),
]