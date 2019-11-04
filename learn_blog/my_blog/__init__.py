from flask import Flask

app = Flask(__name__)

# 通过这个设置来一次性引用在config.py中设置的参数
app.config.from_pyfile('config.py')

# 可以使用from_object来引用config文件，注意与上面方法的不同
# import config
# app.config.from_object(config)

# 建立数据库连接
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# 初始化数据库
# 必须引用User和Post模型，否则会找不到这2张表格，无法进行后续操作
# from my_blog.models import User, Post
db.drop_all()
db.create_all()

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