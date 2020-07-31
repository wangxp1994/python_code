# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/21 16:10

from common.utils import *
from flask import Blueprint, url_for, request, redirect
from flask import render_template

jquery = Blueprint('jquery', __name__)


# 首页
@jquery.route('/jquery/')
def index(name="寂寞沙洲冷"):
	return html['jquery_index'].format(name)


# url的两种传参
@jquery.route('/jquery/show_params_first/<one>/<int:two>')  # 类型:int float string path uuid
def show_params_first(one, two):
	return html['jquery_params'].format(one, type_re(one), two, type_re(two))


@jquery.route('/jquery/show_params_second')  # 类型:int float string path uuid
def show_params_second():
	one = request.args.get("one")
	two = request.args.get("two")

	return html['jquery_params'].format(one, type_re(one), two, type_re(two))

# url_for示例
@jquery.route('/jquery/url_for_demo')
def url_for_demo():
	url_show = url_for("jquery.show_params_second", one="Love", two="Forever")
	return redirect(url_show)

# request测试
@jquery.route('/jquery/request_demo')
def request_demo():
	s = html['request_demo'].format(
		request.path, request.full_path, request.host, request.host_url,
		request.base_url, request.url, request.url_root
	)
	print(s)
	return s.replace("\n", "<br>")

