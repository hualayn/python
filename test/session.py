# 导入session模块
from flask import Flask, session
import os

# 引入timedelta模块，用来指定session生命周期
from datetime import timedelta



app = Flask(__name__)

# session必须定义SECRET_KEY，这里使用os.urandom(24)产生随机的SECRET KEY，24表示随机数长度是24位
app.config['SECRET_KEY'] = os.urandom(24)


'''
用app.config['PERMANENT_SESSION_LIFETIME']和datetime模块，规定session的生命周期为2小时
（必须有session.permanent = True语句，否则，这个session的生命周期还是默认的‘回话结束时就过期’）
'''
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

@app.route('/')
def hello_world():

    # session的操作类似一个字典
    session['username'] = 'test_name'

    # session.permanent中permanent属性表示session的生命周期，session.permanent = True代表是31天
    session.permanent = True
    return 'hello,world'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or '没有session'

if __name__ == '__main__':
    app.run(debug=True)