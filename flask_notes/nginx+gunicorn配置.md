# gunicorn
- 首先安装gunicorn
在虚拟环境下安装：pip install gunicorn
另外还可以安装gevent：pip install gevent

- 简单启动gunicorn  
gunicorn app:app 第一个app是工程文件名，第二个app是这个工程文件下的app.run()里的这个app，所以第二个app一般不需要修改

- 下面的启动方式稍微复杂点：  
gunicorn -w 4 -b 127.0.0.1:8000 app:app -w代表worker，4代表4个进程 -b代表地址，127.0.0.1:8000 服务器地址：端口号

- 还可以使用config文件来配置，需要放在工程文件同级的文件夹中  
gunicorn -c gconfig.py app:app  gconfig.py文件名可以自动定义，也可以修改为自己喜欢的名字，如gconfig.conf

- 一般的config文件配置如下：  
gunicorn.conf  

并行工作进程数，按照实际电脑配置，推荐数量 核心×2  
workers = 2  
指定每个工作者的线程数，按照实际配置，太高也不需要  
threads = 1  
监听内网端口5000  
bind = '127.0.0.1:5000'  
设置守护进程,将进程交给supervisor管理  
daemon = 'false'  
工作模式协程  
worker_class = 'gevent'  
设置最大并发量  
worker_connections = 2000  
设置进程文件目录  
pidfile = '/var/run/gunicorn.pid'  
设置访问日志和错误信息日志路径，需要事先创建文件，否则报错  
accesslog = '/var/log/gunicorn_acess.log'  
errorlog = '/var/log/gunicorn_error.log'  
设置日志记录水平  
loglevel = 'warning'  

# nginx配置
- 找到nginx.conf文件（实际安装位置跟版本有关，我的在/urs/local/nginx/conf文件夹），对下面部分进行修改  
server {  
    listen 80;  
    server_name  localhost;  
    charset utf-8;  
    client_max_body_size 200m;  
    access_log  /var/log/nginx/build-access.log;  
    error_log  /var/log/nginx/build-err.log;  
    location = /favicon.ico { access_log off; log_not_found off; }  
    location /static/ {  
        \#静态文件如js，css的存放目录  
        alias /home/build/build/static/;  
    }  
    location / {  
        proxy_pass http://127.0.0.1:5000; \# 这里要配合gunicorn启动文件使用  
        proxy_redirect     off;  
        proxy_set_header   Host                 $http_host;  
        proxy_set_header   X-Real-IP            $remote_addr;  
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;  
        proxy_set_header   X-Forwarded-Proto    $scheme;  
    }  
}  

# 启动nginx服务  
- 视nginx安装位置不同，在nginx安装目录下，命令行输入  
./nginx  

- 重启nginx服务  
./nginx -s reload  

- 注意  
- 先启动nginx，再启动gunicorn  

- gunicorn是多线程工作的，如果flask项目中，设置了os.urandom()，那么会因为每次请求不同，线程不同，导致session不同  