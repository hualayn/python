时间：2019.10.19

#主题：nginx+uwsgi+flask建站笔记
##flask
"""
    flask是个轻型web框架，可以用来发布小型的网站，于是决心试一下。
	我是centos7，自带python2.7版本，升级至python3，安装了pip等工具。
	
	按照https://dormousehole.readthedocs.io/en/latest/installation.html#python进行安装：
"""
- ###虚拟环境
建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。

为什么要使用虚拟环境？随着你的 Python 项目越来越多，你会发现不同的项目会需要 不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。

虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。

Python 3 内置了用于创建虚拟环境的 venv 模块。如果你使用的是较新的 Python 版本，那么请接着阅读本文下面的内容。

- <h2>创建一个虚拟环境</h2>
创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 venv 文件夹：

$ mkdir myproject<br>
$ cd myproject<br>
$ python3 -m venv venv<br>

- ###激活虚拟环境
在开始工作前，先要激活相应的虚拟环境：

$ . venv/bin/activate

- ###安装 Flask###
在已激活的虚拟环境中可以使用如下命令安装 Flask：

$ pip install Flask
Flask 现在已经安装完毕。

- ###调试
###一个最小的应用
一个最小的应用看起来像这样:

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
把它保存成 hello.py (或者类似的文件)，然后用 Python 解释器运行它。确保你的应用不叫做 flask.py， 因为这会与 Flask 本身冲突。

$ python hello.py
 * Running on http://127.0.0.1:5000/
现在浏览 http://127.0.0.1:5000/，你会看到你的 Hello World 问候。
**(注意防火墙应开启相应端口)**
---
##uwsgi

