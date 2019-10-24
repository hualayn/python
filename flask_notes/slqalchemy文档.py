# 安装模块
pip install Flask-SQLalchemy
pip install SQLAlchemy

# 引入模块
from flask_sqlalchemy import SQLAlchemy

# 配置数据库地址
# 数据库地址参数名:SQLALCHEMY_DATABASE_URI
# mysql://flask_blog:123456@localhost/blog_db,mysql是数据库类型,flask_blog是数据库用户名, 123456是用户密码，blog_db是数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_blog:123456@localhost/blog_db'

#配置数据库修改(track 什么东东，设置为False关闭)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db是一个数据库对象，是SQLAlchemy的一个继承类,app是文件路径
db = SQLAlchemy(app)

#建立数据库模型，需要继承db.Model
class Author(db.Model):
    # 定义表名
    __tablename__ = 'authors'

    # 定义字段
    # db.Column表示为一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 表示和Book模型发生关联，增加了一个books属性
    # backref='author',表示author是Book的属性
    books = db.relationship('Book', backref='author')

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # db.ForeignKey(role
    # s.id)表示是外键
    author_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

if __name__ == '__main__': #程序初始化时的操作
    #删除所有数据库
    db.drop_all()

    #创建新数据库
    db.create_all()

    app.run()

##############################################################################
# 引入hello模块内所有类，方法等
from hello import *

# Role实例，字段name 赋值admin
role = Role(name='admin')

#将赋值插入数据库,需传递参数
db.session.add(role)

#提交数据库，不需要传递参数
db.session.commit()

#修改参数
role.name = 'admin2'

#提交数据库
db.session.commit()

#删除参数
db.session.delete(role)

#提交数据库
db.session.commit()

##########################################
