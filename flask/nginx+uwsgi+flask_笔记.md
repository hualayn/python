时间：2019.10.19

<h1>主题：nginx+uwsgi+flask建站笔记</h1>

## 一、flask

"""
    flask是个轻型web框架，可以用来发布小型的网站，于是决心试一下。
	我是centos7，自带python2.7版本，升级至python3，安装了pip等工具。
	
	按照https://dormousehole.readthedocs.io/en/latest/installation.html#python进行安装：
"""

- ### 虚拟环境
建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。

为什么要使用虚拟环境？随着你的 Python 项目越来越多，你会发现不同的项目会需要 不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。

虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。

Python 3 内置了用于创建虚拟环境的 venv 模块。如果你使用的是较新的 Python 版本，那么请接着阅读本文下面的内容。

- ### 创建一个虚拟环境
创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 venv 文件夹：

$ mkdir myproject<br>
$ cd myproject<br>
$ python3 -m venv venv<br>

- <h3>激活虚拟环境</h3>
在开始工作前，先要激活相应的虚拟环境：

$ . venv/bin/activate

- ### 安装 Flask
在已激活的虚拟环境中可以使用如下命令安装 Flask：

$ pip install Flask<br>
Flask 现在已经安装完毕。

- ### 调试
### 一个最小的应用
一个最小的应用看起来像这样:

#####代码示例

>from flask import Flask<br>
>app = Flask(\_\_name\_\_)<br>
>@app.route('/')<br>
>def hello_world():<br>
>    return 'Hello World!'<br>

>if \_\_name\_\_ == '\_\_main\_\_':<br>
>    app.run()

把它保存成 hello.py (或者类似的文件)，然后用 Python 解释器运行它。确保你的应用不叫做 flask.py， 因为这会与 Flask 本身冲突。

>$ python hello.py
> \* Running on http://127.0.0.1:5000/<br>
现在浏览 http://127.0.0.1:5000/，你会看到你的 Hello World 问候。<br>
**(注意防火墙应开启相应端口)**
---

## 二、uwsgi

uWSGI 也是部署 Flask 的途径之一,类似的部署途径还有 nginx 、 lighttpd 和 cherokee 。其他部署途径的信息参见 FastCGI 和 独立 WSGI 容器 。使用 uWSGI 协议来部署 WSGI 应用的先决条件是 需要一个 uWSGI 服务器。 uWSGI 既是一个协议也是一个服务器。如果作为一个服务器， 它可以服务于 uWSGI 、 FastCGI 和 HTTP 协议。

最流行的 uWSGI 服务器是 uwsgi ，本文将使用它来举例，请先安装它。

pip install uwsgi (注意在激活虚拟环境情况下安装uwsgi)

##### 代码示例：<br>
[uwsgi]<br>
socket = 127.0.0.1:8000<br>
\#由于外部还要嵌套Nginx，这里可以使用socket进行通信，如果Nginx和uwsgi部署在同一台机器上，直接使用127.0.0.1<br>
\#如果外部直接通过uwsgi访问服务，需将socket改为http-socket或者http，将127.0.0.1改为0.0.0.0<br>
chdir = /path/to/yourproject<br>
\#项目目录<br>
virtualenv =/path/to/venv<br>
\#虚拟环境所在路径<br>
wsgi-file = flask_web.py<br>
\#编写flask代码的py文件<br>
callable = app<br>
\#Flask应用对象<br>
plugin = python<br>
daemonize = /path/to/uwsgi.log<br>
\#进程会在后台运行，并输出日志<br>
pidfile = /path/to/uwsgi.pid<br>

- ### 调试

将socket = 127.0.0.1:8000<br>
改为http = :8000(这样就可以通过浏览器直接访问)

通过uwsgi启动flask应用时，运行：

uwsgi --ini uwsgi.ini

看看能否打开hello页面

---

## 三、nginx

- ### 安装

原想简单通过yum install nginx安装nginx服务器，但提示需要perl还有什么libpre模块无法安装。因此在网上搜索了wget 安装的方法：（不在python虚拟环境下）

#####代码示例

wget http://nginx.org/download/nginx-1.12.2.tar.gz

tar -zxvf nginx-1.12.2.tar.gz

./configure

make

make install

- ### 设置

安装位置在/urs/local/nginx，配置文件为/usr/local/nginx/conf/nginx.conf,vim打开nginx.conf，修改如下：

 server { <br>
 36         listen 8000; \#修改端口号，可随意<br>
 37         server_name localhost;<br>
 38<br>
 39         #charset koi8-r;<br>
 40<br>
 41         #access_log  logs/host.access.log  main;<br>
 42        # location / { try_files $uri @myproject; }<br>
 43         location / {<br>
 44            # root   html;<br>
 45            # index  index.html index.htm;<br>
 46             include uwsgi_params; \# 导入uwsgi参数<br>
 47             uwsgi_pass 127.0.0.1:5000; \# 设置uwsgi接口，与上面uwsgi设置的接口一致<br>
        }<br>

- ### 调试

启动nginx：<br>
./usr/local/nginx/sbin/nginx

接着启动uwsgi:<br>(虚拟环境下，因为uwsgi安装在虚拟环境里)<br>
uwsgi uwsgi.ini

最后，在浏览器内输入：http://ip地址:8000(nginx.conf设置的端口号),如果显示"hello,world"即表示设置成功。
