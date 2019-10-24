# 安装模块
pip install Flask-WTF

# 导入模块
from flask_wtf import FlaskForm

#导入验证模块
from wtforms.validators import DataRequired

# 从wtforms导入
from wtforms import StringField, PasswordField, SubmitField

# 创建表单类，继承FlaskForm类
app.secret_key = 'aaa'

class BookForm(FlaskForm):
    author = StringField('作者:', validators=[DataRequired()])
    book_name = StringField('书籍:', validators=[DataRequired()])
    submit = SubmitField('提交')