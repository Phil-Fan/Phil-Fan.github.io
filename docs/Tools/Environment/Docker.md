# Docker

[Docker Compose - 安装和基本使用\_docker-compose 安装-CSDN博客](https://blog.csdn.net/Que_art/article/details/135192479)

=== "Docker Compose（容器编排工具）"

    定义：Docker Compose 是一个用于定义和运行多容器 Docker 应用的工具。

    功能：
    - **多容器管理**：允许用户在一个YAML文件中定义和管理多个容器
    - **服务编排**：配置容器间的网络和依赖关系
    - **一键部署**：使用docker-compose up命令启动、停止和

=== "Docker（容器平台）"

    定义：一个开放源代码的容器化平台，允许开发者将应用及其依赖打包进轻量级、可移植的容器中。

    - **容器化**：将应用和其运行环境封装在一个容器中
    - **镜像管理**：创建、存储和分发容器镜像
    - **容器运行**：可以运行在任何支持Docker的环境中

## 安装
### linux

查看是否安装成功

```shell
[root@localhost ~]# docker-compose --version
Docker Compose version v2.16.0
```

#### 换源
```shell
sudo vim /etc/docker/daemon.json
```
插入下面的句子，最后不要加逗号
```
{
    "registry-mirrors": ["https://dockerhub.icu"]
}
```


### windows
[【从零开始】Docker Desktop：听说你小子要玩我-阿里云开发者社区](https://developer.aliyun.com/article/1601101)

1. [官网](https://www.docker.com/products/docker-desktop/)下载 
2. 安装
3. 重启一下电脑，这步可能会遇到什么用户组的问题，先重启。我重启以后问题消失

```shell title="查看是否安装成功"
docker --version
```
4. 修改镜像源

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241219162658.png)
```json title="镜像源设置"
{
  "registry-mirrors": [
    "https://docker.hpcloud.cloud",
    "https://docker.m.daocloud.io",
    "https://docker.unsee.tech",
    "https://docker.1panel.live",
    "http://mirrors.ustc.edu.cn",
    "https://docker.chenby.cn",
    "http://mirror.azure.cn",
    "https://dockerpull.org",
    "https://dockerhub.icu",
    "https://hub.rat.dev"
  ]
}
```
### 常规操作

上传文件：点击`files`在右键选择`import`选择文件夹即可，上传以后重启服务


## 使用



### 文档

!!! note "文档结构"

    === "说明"

      - version：指定 Compose 文件格式yaml的规则版本，版本决定可用的配置选项
      - service：定义了应用中的服务，每个服务可以使用不同的镜像、环境设置和依赖关系
        - web：自己构建的镜像
          - build：用于构建镜像，指定构建镜像的 dockerfile 的上下文路径
          - ports：映射容器和宿主机的端口
          - volumes：挂载本地目录到指定容器目录，用于数据持久化或在容器之间共享数据
          - links：与redis服务连接
      - redis：构建指定镜像redis
      - image：从指定的镜像中启动容器，可以是存储仓库、标签以及镜像 ID
      - volumes：用于数据持久化和共享的数据卷定义，常用于数据库存储、配置文件、日志等数据的持久化

    === "实例"

        ```yml
        version: "3.9"
        services:
            web:
            build: .
            ports:
                - "8000:5000"
            volumes:
                - .:/code
                - logvolume01:/var/log
            links:
                - redis
            redis:
            image: redis
        volumes:
        logvolume01: {}
        ```


```shell
docker-compose up
```