# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/08 14:44
from django.http import HttpResponse
from django.shortcuts import render


def index_views(request):
	# return HttpResponse("web_django index")
	return render(request, 'index.html')