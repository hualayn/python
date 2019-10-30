from my_blog import app

# import sqlite3
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.Text, nullable=False)
    createdtime = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    posts = db.relationship('Post', backref='user')

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    committime = db.Column(db.TIMESTAMP, nullable=False, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

def init_db():
    # db.drop_all()
    db.create_all()
    # print(db.create_all())

# def init_db():
#     try:
#         con = sqlite3.connect('database.db')
#         cur = con.cursor()
#
#         # #初始化表格，如果存在这些表则删除
#         # sql = "drop table if exists users"
#         # cur.execute(sql)
#
#         # sql = "drop table if exists posts"
#         # cur.execute(sql)
#
#         # sql = '''
#         #     create table users(
#         #     id integer primary key autoincrement,
#         #     name varchar(16) unique not null ,
#         #     password text not null
#         #     )
#         #     '''
#         # cur.execute(sql)
#         #
#         # sql = '''
#         #         create table posts(
#         #         id integer primary key autoincrement,
#         #         title varchar(50) unique not null ,
#         #         content text not null ,
#         #         author_id integer not null,
#         #         committime timestamp not null default current_timestamp,
#         #         foreign key (author_id) references users (id)
#         #         )
#         #         '''
#         # cur.execute(sql)
#
#         cur.close()
#         con.close()
#     except Exception as e:
#         print(e)

# 如果没有dict_factory这个函数，那么将返回一个list的值，使用起来非常不方便
# def dict_factory(cursor, row):
#     d = {}
#     for index, col in enumerate(cursor.description):
#         d[col[0]] = row[index]
#     return d
#
# def search_user_name(username):
#     try:
#         con = sqlite3.connect('database.db')
#         con.row_factory = dict_factory
#         cur = con.cursor()
#         sql = " select * from users where name=? "
#         user = cur.execute(sql, (username,)).fetchone() #这里u返回值是一个tunple（元组）
#         cur.close()
#         con.close()
#         if user:
#             return user
#     except Exception as e:
#         print(e)
#
# def search_user_id(id):
#     try:
#         con = sqlite3.connect('database.db')
#         con.row_factory = dict_factory
#         cur = con.cursor()
#         sql = " select * from users where id=? "
#         user = cur.execute(sql, (id,)).fetchone() #这里u返回值是一个tunple（元组）
#         cur.close()
#         con.close()
#         if user:
#             return user
#     except Exception as e:
#         print(e)

# def show_posts():
#     try:
#         con = sqlite3.connect('database.db')
#         con.row_factory = dict_factory # 指定工厂方法，官方给出的将list返回为字典的方法
#         cur = con.cursor()
#         sql = " select * from posts "
#         u = cur.execute(sql).fetchall() # 如果不进行转换，那么这里的u返回值是一个list；现在返回的是一个字典列表
#
#         # 可以通过打印来验证一下
#         # print(u)
#
#         cur.close()
#         con.close()
#
#         if u:
#             # print(u)
#             return u #将返回一个字典列表
#
#     except Exception as e:
#         print(e)

# def add_user(name, password):
#     try:
#         con = sqlite3.connect('database.db')
#         cur = con.cursor()
#         sql = '''
#         insert into users(name, password)
#         values
#         (?, ?)
#         '''
#         cur.execute(sql, (name, generate_password_hash(password), ))
#         con.commit()
#         cur.close()
#         con.close()
#     except Exception as e:
#         con.rollback()
#         print(e)

# def add_post(title, content, author_id):
#     try:
#         con = sqlite3.connect('database.db')
#         cur = con.cursor()
#         sql = '''
#         insert into posts ( title, content, author_id )
#         values
#         (?, ?, ?)
#         '''
#         cur.execute(sql, (title, content, author_id, ))
#         con.commit()
#         cur.close()
#         con.close()
#     except Exception as e:
#         con.rollback()
#         print(e)

# init_db()
# db.drop_all()
# db.create_all()
# print(show_posts())
# add_post('test_title', 'test_content', 1)