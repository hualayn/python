- 连接数据库, linux命令行下

        mysql -u用户名 -p密码

- 显示数据库，mysql界面下(下同)

        show databases;

- 使用数据库

        use 数据库;

- 创建数据库

        create database 数据库;

- 删除数据库

        drop database 数据库;

- 显示所有表格

        show tables;

- 显示表格数据结构
        desc 表名;  
        或者 describe 表名;

- 显示表头(跟上面作用差不多)

        show columns from 表名

- 创建表格
        
        create table 表名(列名 数据类型 [not null] [primary key],列名 数据类型 [not null],..);

- 删除表

        drop table 表名;

- 更改表名
        
        rename table 旧表名 to 新表名;

- 显示表格内容
        
        select * from 表名;

- 显示表格特定参数内容

        select * from 表名 where 键名 = 参数;

- 增加表内容 插入数据

        insert  into  表名(列名，列名...)values(值，值...);

- 修改列中的一条记录

        update  表名  set   列=值   where   列=值;

- 删除列中的一条记录
        
        delete  from  表名   where   列=值;



- 创建用户
 
    - 基本语句
    
            CREATE USER 'username'[@'host'] IDENTIFIED BY 'password';

    - eg. 常见 local_user 用户可以在所有主机登录，密码为 123456
    
            CREATE USER 'local_user' IDENTIFIED BY '123456';

    - eg. 创建 local_user 只允许在本地登录
    
            CREATE USER 'local_user'@'localhost' IDENTIFIED BY '123456';


- 查看用户权限(单引号可以省略)
    
    - 可以通过查询 user 表获取 语法格式为
    
            SELECT  privileges|* FROM user WHERE `user` = 'username';

    - eg. 查看 local_user 的权限
    
            SELECT * FROM user WHERE `user` = 'local_user';

    - 也可以用 SHOW GRANTS 查看(默认是SHOW GRANTS FOR 'username'@'%',因此，如果要查询本地登录权限,必须加上@localhost;)
    
            SHOW GRANTS FOR 'username' [@localhost];

    - eg.
    
            SHOW GRANTS FOR local_user;


- 赋予用户权限
    - 语法格式
    
            GRANT privileges ON database.table TO 'username'@'host' [IDENTIFIED BY 'password'];

    - eg. 赋予 local_user 在所有主机的所有权限，但不包含给其他账号赋予权限的权限
            
            GRANT all ON *.* TO 'local_user'@'%';

    - 刷新权限 权限更新后刷新才会起作用
    
            FLUSH PRIVILEGES;

    ##### GRANT命令说明：
        priveleges (权限列表),可以是all, 表示所有权限，也可以是select,update等权限，多个权限的名词,相互之间用逗号分开。  
        ON 用来指定权限针对哪些库和表。格式为数据库 .表名 ，点号前面用来指定数据库名，点号后面用来指定表名，*.* 表示所有数据库所有表。  
        TO 表示将权限赋予某个用户, 格式为username@host，@前面为用户名，@后面接限制的主机，可以是IP、IP段、域名以及%，%表示任何地方。 

        * 注意：这里%有的版本不包括本地，以前碰到过给某个用户设置了%允许任何地方登录，但是在本地登录不了，这个和版本有关系，遇到这个问题再加一个localhost的用户就可以了。


        IDENTIFIED BY 指定用户的登录密码,该项可以省略(某些版本下回报错，必须省略)。
        WITH GRANT OPTION 这个选项表示该用户可以将自己拥有的权限授权给别人。注意：经常有人在创建操作用户的时候不指定WITH GRANT OPTION选项导致后来该用户不能使用GRANT命令创建用户或者给其它用户授权。  
        备注：可以使用GRANT重复给用户添加权限，权限叠加，比如你先给用户添加一个select权限，然后又给用户添加一个insert权限，那么该用户就同时拥有了select和insert权限。  


        * 授权原则说明：  
        只授予能满足需要的最小权限，防止用户干坏事。比如用户只是需要查询，那就只给select权限就可以了，不要给用户赋予update、insert或者delete权限。  
        创建用户的时候限制用户的登录主机，一般是限制成指定IP或者内网IP段。  
        初始化数据库的时候删除没有密码的用户。安装完数据库的时候会自动创建一些用户，这些用户默认没有密码。
        为每个用户设置满足密码复杂度的密码。  
        定期清理不需要的用户。回收权限或者删除用户。  


- 收回用户权限

    + 语法格式
    
            REVOKE privileges ON database.table FROM 'username'@'host';

            + eg. 收回 local_user 的写入和更新权限
            
                    REVOKE insert,update ON *.* FROM 'local_user'@'%';


    + 删除用户
        - 语法格式
        
                DROP USER 'username'@'host';

        - eg. 删除本地用户 local_user
        
                DROP USER 'local_user'@'localhost';