# 引入蓝图模块
from flask import Blueprint
from flask import render_template

#实例
bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    return render_template('blog/index.html/')

