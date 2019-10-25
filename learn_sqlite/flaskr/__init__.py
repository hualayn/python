from flask import Flask
from flaskr import blog

app = Flask(__name__)

'''
逻辑思路：

1. 创建数据库连接
    a. 初始化数据库，建立2张表，users，articles，这2张表要有关联属性
    
2. 查询相关数据库内容，并在主页中显示

3. 登录用户，进行数据的添加，修改，删除
'''

app.register_blueprint(blog.bp)







