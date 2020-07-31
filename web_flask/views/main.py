# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/21 16:19

from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return html['main_index']