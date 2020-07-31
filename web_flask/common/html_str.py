# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/21 20:15

html = {

	"main_index" : """
		<h1>flask 首页</h1>
		<h3><a href='/jquery/'>jquery</a></h3>
		""",


	"jquery_index": """
		<h1>Hello! jQuery  >>>  {}</h1>
		<h3><a href='/jquery/show_params_first/1/1'>show_params_first</a></h3>
		<h3><a href='/jquery/show_params_second?one=1&two=2'>show_params_second</a></h3>
		<h3><a href='/jquery/url_for_demo'>url_for_demo</a></h3>
		<h3><a href='/jquery/request_demo'>request_demo</a></h3>
		
		""",


	"jquery_params": """
		<a href='/jquery/'>jquery</a></h3>
		<br>
		<h3>one = {}, type(one) = {}</h3><h3>two = {}, type(two) = {}</h3>
		""",


	"request_demo": """
		path = {}, 
		full_path = {}, 
		host = {}, 
		host_url = {}, 
		base_url = {}, 
		url = {}, 
		url_root = {}
		"""

}