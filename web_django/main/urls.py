# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/08 14:58

from django.conf.urls import url

from main.views import index

urlpatterns = [
    url(r'', index),
]