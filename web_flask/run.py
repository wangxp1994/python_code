# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/21 15:50


from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='statics', static_url_path='/static')
app.debug = True

from views.jquery import jquery

app.register_blueprint(jquery)

from views.main import main

app.register_blueprint(main)

from common import html_str
setattr(__builtins__, "html", html_str.html)

if __name__ == '__main__':
	app.run()
