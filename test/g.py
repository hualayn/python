# 全局保存对象g，专门用来存储开发者自己定义的一些数据，方便在整个flask程序中使用，而不用专门去传递函数

from flask import Flask, request, g
from instance import log_a, log_b, log_c
app = Flask(__name__)



@app.route('/')
def hello_world():
    username = request.args.get('username')
    g.username = username # 为全局对象g.username赋值
    log_a()
    log_b()
    log_c()
    return 'hello,world'



if __name__ == '__main__':
    app.run(debug=True)
