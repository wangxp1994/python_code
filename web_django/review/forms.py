# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/17 16:38
from django import forms


class PictureModelForm():
	pass


class PictureUpForm(forms.Form):
	words = forms.CharField(
		max_length=50,
		label="标签",
	)
	file = forms.ImageField(
		label="图片",
	)
