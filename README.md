# flask_-Microfilm
基于python语言flask框架开发的微电影网站及后台管理



涉及到的技术: Linux、Python3、MySQL、html5、Flask、Nginx、Docker、Redis

Flask框架的特点：Flask扩展丰富，冗余度小，可自由选择组合各种插件，性能优越，相比其它web框架十分轻量级，其优雅的设计哲学易于学习和掌握，小型项目快速开发，大项目毫无压力。

Flask:使用post与get请求、上传文件、cookie获取与响应、404处理,使用模板自定义、定义过滤器、定义全局上下文处理器,使用flask-wtf定义表单模型、字段类型、字段验证、视图处理表单、模板使用表单,使用flask-sqlachemy定义数据库模型、添加数据、修改数据、查询数据、删除数据、数据库时间、数据迁移

视频技术:jwplayer播放器插件、Dplayer播放器插件、flv、MP4视频格式支持

#### 运行项目
```

在安装docker以及docker-compose的情况下
git clone https://github.com/baimawen/flask_-Microfilm.git && cd flask_-Microfilm

docker-compose build #构建镜像
docker-compose up # 启动

```
模块划分:
  - 前台(home)
    - 会员登陆及注册
    - 会员中心
    - 电影播放
    - 电影评论
    - 收藏电影
  - 后台(admin)
    - 管理员登陆
    - 修改密码
    - 标签管理
    - 电影管理
    - 上映预告管理
    - 会员评论
    - 评论管理

目录分析:
  - 前台
    - 数据模型: models.py
    - 表单处理: home/forms.py
    - 模板目录: templates/home
  - 后台
    - 数据模型: models.py
    - 表单处理: admin/forms.py
    - 模板目录: templates/admin
    - 静态目录: static
  - 入口启动脚本: manage.py
  - 项目APP: app
  - 初始化文件: __init__.py
  - 数据模型文件: models.py
  
### Ubuntu安装Docker
```
# step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# Step 3: 写入软件源信息
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# Step 4: 更新并安装 Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce

注意：其他注意事项在下面的注释中
# 安装指定版本的Docker-CE:
# Step 1: 查找Docker-CE的版本:
# apt-cache madison docker-ce
#   docker-ce | 17.03.1~ce-0~ubuntu-xenial | http://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
#   docker-ce | 17.03.0~ce-0~ubuntu-xenial | http://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
# Step 2: 安装指定版本的Docker-CE: (VERSION 例如上面的 17.03.1~ce-0~ubuntu-xenial)
# sudo apt-get -y install docker-ce=[VERSION]

# 通过经典网络、VPC网络内网安装时，用以下命令替换Step 2、Step 3中的命令
# 经典网络：
# curl -fsSL http://mirrors.aliyuncs.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyuncs.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# VPC网络：
# curl -fsSL http://mirrors.cloud.aliyuncs.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] http://mirrors.cloud.aliyuncs.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
```

### Centos7安装Docker
```
# step 1: 安装必要的一些系统工具
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
# Step 2: 添加软件源信息
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# Step 3: 更新并安装 Docker-CE
sudo yum makecache fast
sudo yum -y install docker-ce
# Step 4: 开启Docker服务
sudo service docker start

注意：其他注意事项在下面的注释中
# 官方软件源默认启用了最新的软件，您可以通过编辑软件源的方式获取各个版本的软件包。例如官方并没有将测试版本的软件源置为可用，你可以通过以下方式开启。同理可以开启各种测试版本等。
# vim /etc/yum.repos.d/docker-ce.repo
#   将 [docker-ce-test] 下方的 enabled=0 修改为 enabled=1
#
# 安装指定版本的Docker-CE:
# Step 1: 查找Docker-CE的版本:
# yum list docker-ce.x86_64 --showduplicates | sort -r
#   Loading mirror speeds from cached hostfile
#   Loaded plugins: branch, fastestmirror, langpacks
#   docker-ce.x86_64            17.03.1.ce-1.el7.centos            docker-ce-stable
#   docker-ce.x86_64            17.03.1.ce-1.el7.centos            @docker-ce-stable
#   docker-ce.x86_64            17.03.0.ce-1.el7.centos            docker-ce-stable
#   Available Packages
# Step2 : 安装指定版本的Docker-CE: (VERSION 例如上面的 17.03.0.ce.1-1.el7.centos)
# sudo yum -y install docker-ce-[VERSION]
# 注意：在某些版本之后，docker-ce安装出现了其他依赖包，如果安装失败的话请关注错误信息。例如 docker-ce 17.03 之后，需要先安装 docker-ce-selinux。
# yum list docker-ce-selinux- --showduplicates | sort -r
# sudo yum -y install docker-ce-selinux-[VERSION]

# 通过经典网络、VPC网络内网安装时，用以下命令替换Step 2中的命令
# 经典网络：
# sudo yum-config-manager --add-repo http://mirrors.aliyuncs.com/docker-ce/linux/centos/docker-ce.repo
# VPC网络：
# sudo yum-config-manager --add-repo http://mirrors.could.aliyuncs.com/docker-ce/linux/centos/docker-ce.repo
```

### 快速安装docker-compose
```
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```


### nginx配置上传文件大小限制
client_max_body_size 1024M; 上传文件大小限制

sendfile on; 设置为on表示启动高效传输文件的模式

keepalive_timeout 1800;保持连接的时间，默认65s
