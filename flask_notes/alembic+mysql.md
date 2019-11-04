# alembic + mysql  

- 安装alembic
    - 进入虚拟环境，输入命令：  
    
            pip install alembic

    - 命令行cd到工程目录，输入命令
            
            alembic init alembic  
    
    第一个alembic是命令，所以alembic命令都需要先输入alembic才可以运行    
    第二个alembic是生成的文件夹名称，可以自己更改  

    这样就生成了alembic数据版本库

- 设置alembic  
    - 修改alembic.ini    
        打开alembic.ini文件，在sqlalchemy.url中输入数据库连接用户名、密码、地址、端口和数据库名称  
        示例如下（需事先安装mysql，以及pymysql插件，并在mysql中建立数据库）：  

                sqlalchemy.url = mysql+pymysql://root:root@localhost/数据库名?charset=utf8



    - 修改env.py文件（在原有工程文件中，已经建立了数据库连接）   
        主要是修改 target_metadata  
        示例如下：

            import sys,os
            sys.path.append(os.path.dirname(os.path.dirname(__file__)))
            import models #数据库连接在models.py文件中，必须引入，否则报错找不到model，所以还是把工程用__init__转成一个包方便
            target_metadata = models.Base.metadata

- 使用alembic  
    一般命令：  

        alembic revision --autogeneration -m "messages"

        alembic upgrade head

- 注意事项  
    这个网上的教程还是比较多的，比较容易实现  
    有什么不清楚的，网上搜一下基本能找到答案  

    在修改env.py文件中，如果是采用__init__的方式，将工程文件转为一个包，那么引入更加方便

        import 工程文件名.models

    这样就可以了 