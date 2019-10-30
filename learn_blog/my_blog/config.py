# config.py中可以一次设置很多参数，很方便，然后在__init__中引用

# import os

# SERVER_NAME用来自定义域名，如果将来flask程序在购买的服务器上运行，那么也会购买域名，那么就需要在这里定义一下域名
# SERVER_NAME = 'homehua.com:5000'

# 调试模式
DEBUG = True
HOST = '0.0.0.0'

# session模块需要使用SECRET_KEY，利用os.urandom(24)来产生一个24位的随机字符串
SECRET_KEY = 'dev'

# 不需要重启服务器，自动加载模板，方便调试
TEMPLATE_AUTO_RELOAD = True

# SQLALCHEMY_DATABASE_URI = 'sqlite:///dbpath/database.db' ，定义数据库路径，可以自定义路径dbpath文件夹内；如果不定义路径，则为sqlite:///database.db，就在myblog的文件夹内
SQLALCHEMY_DATABASE_URI = 'sqlite:///dbpath/database.db'

# 这个选项必须要填写，否则就会报错
SQLALCHEMY_TRACK_MODIFICATIONS = False