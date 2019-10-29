'''
时间：2019.10.22
跟着黑马程序员的老师，实现简单图书管理的程序
首先看一遍视频，对整个程序的实现有初步的印象(思路，步骤，注意要点)
其次，再根据视频，编写代码，加深印象
对flask以及它的一些组件，编程的思维有初步的概念
养成良好的编程思维习惯
熟悉编程规范
在看完视频以后，给我这个初学者最大的感受：
1. 对初学者还是比较友好的，老师的讲解很细致，上手容易；
2. 前端、后端清晰，前端负责页面的显示，后端理清逻辑思路，注重逻辑实现，对培养良好的编程思维有好处
3. 在后端逻辑实现方面，先引入需要的组件，再编写相关的对象方法，最后组织逻辑实现。
以上就是我学习完视频后的一点心得，如果要进阶更高级的内容，还需要不断努力。
'''

# 从flask引入模块:
# Flask -->
# render_template --> 渲染模板
# request --> 请求网页
# flash --> 消息闪现
from flask import Flask, render_template, flash, redirect, url_for

# 从flask_wtf 引入 FlaskForm, 处理表单
from flask_wtf import FlaskForm

# 从whforms 引入模块:
# StringField --> 文本
# PasswordField --> 密码
# SubmitField --> 提交
from wtforms import StringField, SubmitField

# 从wtforms.validators 引入
# DataRequired --> 验证内容不为空
# EqualTo --> 内容相等(一致)
from wtforms.validators import DataRequired

# 引入数据库模块
from flask_sqlalchemy import SQLAlchemy

# 通过Flask(__name__)定义路径
app = Flask(__name__)

# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_blog:123456@localhost/blog_db'

#配置数据库修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db是一个数据库对象
db = SQLAlchemy(app)

'''
在数据库中创建相关表格，这里需要的是2张表
1. 角色(管理员/用户)
2. 用户
'''

#数据库模型，需要继承db.Model
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
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

# 创建表单类
app.secret_key = 'dev'

class AddBookForm(FlaskForm):
    author = StringField('作者:', validators=[DataRequired()])
    book = StringField('书籍:', validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/', methods=['GET', 'POST'])
def index():
    add_book_form = AddBookForm()
    error = None

    if add_book_form.validate_on_submit():
        author_name = add_book_form.author.data
        book_name = add_book_form.book.data

        author = Author.query.filter_by(name=author_name).first()

        if author:
            book = Book.query.filter_by(name=book_name).first()

            if book:
                error = '已有本书'

            else:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()

                except Exception as e:
                    error = '提交书籍失败'
                    db.session.rollback()

        else:
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()

            except Exception as e:
                error = '提交作者和书籍失败'
                db.session.rollback()

    if not error == None:
        flash(error)

    authors = Author.query.all()

    return render_template('index.html', authors=authors, form=add_book_form)

# 删除书籍，路由需要接受参数，由<参数>来传递
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    error = None
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            error = '删除书籍出错'
            db.session.rollback()
    else:
        error = '未找到书籍'

    flash(error)

    # return redirect()重定向
    #url_for('index'):传入视图函数名，返回该视图函数对应的路由地址
    return redirect(url_for('index'))

@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    author = Author.query.get(author_id)
    error = None

    if author:
        try:
            Book.query.filter_by(author_id=author.id).delete()

            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            error = '删除作者出错'
            db.session.rollback()
    else:
        error = '未找到作者'

    flash(error)

    # return redirect()重定向
    #url_for('index'):传入视图函数名，返回该视图函数对应的路由地址
    return redirect(url_for('index'))

if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    app.run(host='0.0.0.0')