# 并行工作进程数
workers = 5

# 每个工作者的线程数
threads = 2

# 工作模式协程
#worker_class = "gevent"

#监听内网端口8888
bind = "0.0.0.0:8000"

# 设置访问日志和错误信息日志路径
accesslog = '/var/log/gunicorn_access.log'
errorlog = '/var/log/gunicorn_error.log'

# 设置日志级别
loglevel = 'warning'