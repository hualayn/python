# 安装supervisor
##### 官方文档http://www.supervisord.org/，安装前请仔细阅读

- 安装
pip install supervisor  
将安装在python或者python3的文件夹下

- 安装配置文件
	- 在python/bin文件夹内，找到echo_supervisord_conf，输入命令： echo_supervisord_conf > /etc/supervisord.conf，将生成配置文件supervisord.conf
	- 在supervisord.conf文件内添加如下内容：  
	 
			[include]  
			files = /etc/supervisord.d/文件名.ini  

	- 配置“文件名.ini”，例如： 
	   
			#项目名  
			[program:blog]  
			#脚本目录  
			directory=/opt/bin  
			#脚本执行命令  
			command=/usr/bin/python /opt/bin/test.py  

			#supervisor启动的时候是否随着同时启动，默认True  
			autostart=true  
			#当程序exit的时候，这个program不会自动重启,默认unexpected，
			设置子进程挂掉后自动重启的情况，有三个选项，false,unexpected和true。
			如果为false的时候，无论什么情况下，都不会被重新启动，如果为unexpected，
			只有当进程的退出码不在下面的exitcodes里面定义的
			autorestart=false  
			#这个选项是子进程启动多少秒之后，此时状态如果是running，则我们认为启动成功了。默认值为1
			startsecs=1  

			#脚本运行的用户身份   
			user = test  

			#日志输出   
			stderr_logfile=/tmp/blog_stderr.log   
			stdout_logfile=/tmp/blog_stdout.log   
			#把stderr重定向到stdout，默认 false  
			redirect_stderr = true  
			#stdout日志文件大小，默认 50MB  
			stdout_logfile_maxbytes = 20M  
			#stdout日志文件备份数  
			stdout_logfile_backups = 20  

	- 修改supervisord.conf文件（官方建议）  
	把/tmp文件夹修改为另一个文件夹，比如/usr/run/supervisor文件夹内，然后在这个文件夹内创建文件  
	touch supervisor.sock   
    ##### 注意，如果不需要使用http的方式管理supervisor，那么[supervisorctl]里的/tmp文件夹就不用修改  


	- 为了方便，可以创建一个软连接到python下的supervisord和supervisorctl  
	ln -s /dir/to/path/supervisord /usr/local/bin  
	ln -s /dir/to/path/supervisorctl /usr/local/bin

- 启动supervisord  
	supervisord  
	supervisorctl start  

- supervisordctl常用命令

		supervisorctl stop program_name  # 停止某一个进程，program_name 为 [program:x] 里的 x

		supervisorctl start program_name  # 启动某个进程

		supervisorctl restart program_name  # 重启某个进程

		supervisorctl stop groupworker:  # 结束所有属于名为 groupworker 这个分组的进程 (start，restart 同理)

		supervisorctl stop groupworker:name1  # 结束 groupworker:name1 这个进程 (start，restart 同理)

		supervisorctl stop all  # 停止全部进程，注：start、restartUnlinking stale socket /tmp/supervisor.sock
		、stop 都不会载入最新的配置文件

		supervisorctl reload  # 载入最新的配置文件，停止原有进程并按新的配置启动、管理所有进程

		supervisorctl update  # 根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启


