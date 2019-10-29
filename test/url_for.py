from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return url_for('my_list', page=1, count=2)
    # url_for返回视图函数对应的路径，后面的参数传递给url，如果这个参数在返回视图函数中定义，name以path的方式放到url中，如果没有定义，
    # 则以查询字符串的方式返回在url中

@app.route('/post/list/<page>/')
def my_list(page):
    return ''

if __name__ == '__main__':
    app.run(debug=True)
