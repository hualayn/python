# flask_migration + sqlite
##### 文件tree如下：  

         D:.
            │  manage.py
            │
            ├─flask_script_demo
            │  │  config.py
            │  │  models.py
            │  │  __init__.py
            │  │
            │  └─db
            │     └─  database.db
            │  
            └─migrations
                │  alembic.ini
                │  env.py
                │  README
                │  script.py.mako
                └─ versions


- 安装flask_migration  
    - 虚拟环境中，输入命令（flask_migrate需要flask_script支持，所以也要装flask_script模块）：

            pip install Flask-Script  
            pip install Flask-Migrate # 因为Flask-Migrate依赖alembic，alembic会自动安装

    - 在manage.py中引入相关模块
        
            from flask_script import Manager
            from flask_migrate import Migrate, MigrateCommand
            manager = Manager(app)  
            Migrate(app, db)  # 如果没有app和db，那么需要从工程文件中引入
            manager.add_command("db", MigrateCommand)

    - 在命令行，切换到工程文件夹下，输入命令：

            python manage.py db init

        这样就会在工程文件夹下建立migrations数据版本库

- 设置  
    + 同样需要先设置alembic.ini文件，添加在[alembic]下  

            sqlalchemy.url = sqlite:///绝对路径\db\database.db

    + 设置evnv.py文件  
        先把以下这段注释掉：

            # config.set_main_option(
            #     'sqlalchemy.url', current_app.config.get(
            #         'SQLALCHEMY_DATABASE_URI').replace('%', '%%'))
            # target_metadata = current_app.extensions['migrate'].db.metadata

        添加代码  

            from alembic import db
            target_metadata = db.metadata

- 使用
    基本命令  

            python manage.py db migrate

            python manage.py db upgrade

            python manage.py db --help

- 注意事项
    + SQLite 仅仅支持 ALTER TABLE 语句的一部分功能  
        用 ALTER TABLE 语句来更改一个表的名字，也可向表中增加一个字段（列）  
        但是我们不能删除一个已经存在的字段  
        或者更改一个已经存在的字段的名称、数据类型、限定符等等

        ##### 如果想修改的话，那么就必须重新建表，定义字段，然后再将需要的内容从旧表中复制过来，删除旧表

    + 另外，需熟悉sqlite的特性及操作    
        如过设置了id设置了autoincrement，那么就会自动新建一个sqlite_sequence的系统表，记录表名和自增长序号  
        此表除非删除整个数据库，否则无法删除（当然，如果觉得不碍眼也行）