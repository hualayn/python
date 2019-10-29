from flask import Flask

app = Flask(__name__)

# 通过这个设置来一次性引用在config.py中设置的参数
app.config.from_pyfile('config.py')

# 初始化数据库，建立表格
from my_blog.db import init_db
init_db()

# 使用蓝图（blueprint），使整个代码的布局更加清晰
import my_blog.blog
import my_blog.auth
app.register_blueprint(blog.bp)
app.register_blueprint(auth.bp)

# app.add_url_rule("/", endpoint="index")

# @app.errorhandler(404)定义错误返回值，404代表返回错误代码，如果404错误则执行page_not_found(e)函数，其中参数e不可缺省
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('error/404.html'), 404
#
# @app.errorhandler(500)
# def page_not_found(e):
#     return render_template('error/404.html'), 500