# Linux 系统设置

!!! note "这一篇主要记录在配置linux时候遇到的一些问题和解决方案"

## VMware

【VMware Workstation 17】
VMware Workstation v17.x 永久许可证激活密钥：
```
MC60H-DWHD5-H80U9-6V85M-8280D
4A4RR-813DK-M81A9-4U35H-06KND
NZ4RR-FTK5H-H81C1-Q30QH-1V2LA
JU090-6039P-08409-8J0QH-2YR7F
4Y09U-AJK97-089Z0-A3054-83KLA
```
## 系统配置

### 中文系统

### 分辨率
[linux 下更改分辨率](https://blog.csdn.net/SueMagic/article/details/89399959)



## 查看系统信息

查看cpu信息
```bash
cat /proc/cpuinfo
```
## 通用软件

```shell
apt-get install git
apt-get install vim
```


- tldr：简易版man手册
- fd-find：人性化的find
- rg(ripgrep)：快速搜索
- fzf ： 模糊搜索


### terminator

[terminator](https://blog.csdn.net/learning_tortosie/article/details/102581261)

```shell
sudo apt-get install terminator
```
!!! bug "设置为默认终端"

|开启or关闭快捷键|	作用|
|---|---|
|`Ctrl + Shift + O`|	水平分割终端（分成上下两个窗口）|
|`Ctrl + Shift + E`|	垂直分割终端（分成左右两个窗口）|
|`Ctrl + Shift + W`|	关闭当前终端|
|`Ctrl + Shift + X`|	放大（还原）当前终端|
|`Ctrl + Shift + G`|	清屏|
|`Ctrl + Shift + Q`|	关闭所有终端（退出程序）|
|`Ctrl + Shift + T`|	开一个新终端|


|快捷键|	作用|
|---|---|
|`alt+方向键` or `ctrl+TAB`|切换窗口|
|`ctrl shift +`|加字号|
|`F11`|全屏|
|`super(win) + g`|group,将不同窗口打包，指令可以广播|
|`Super+Shift+g`|取消分组|
|`ctrl+shift+f`|搜索命令|
|`Ctrl+Shift+c`|复制指令|
|`Ctrl+Shift+v`|粘贴指令|
|`Ctrl+Shift+X`|    将分割的某一个窗口放大至全屏使用|
|`Ctrl+Shift+Z`|    从放大至全屏的某一窗口回到多窗格界面|

### vscode
[vscode on Kali](https://blog.csdn.net/CM_STC89C52/article/details/127296320)

1. 用内嵌的浏览器搜索vscode，下载vscode的.deb格式的安装包
2. 在终端中输入 `sudo dpkg -i code_1.72.1-1665423861_amd64.deb` 进行解压包
3. 在vscode软件上点击鼠标右键，点击 `Edit Application`
4. 有个Command选项，输入 `/usr/share/code/code --unity-launch %F --no-sandbox` 即可，再点击保存。

### SSH
```shell
sudo apt-get install openssh-server
ssh user@remote
```



```shell
vim /etc/ssh/sshd_config

```

- 第33行:将 PermitRootLogin without-password（第33行） 改为 PermitRootLogin yes 并去掉前面的注释符号（#） 
- 第57行:#PasswordAuthentication yes(第57行)的注释去掉，如果是no就改为yes
- 保存

```shell
service ssh restart
```

**验证安装**
```shell
service ssh status
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240711175232.png)

**开机自启动**

```shell
update-rc.d ssh enable
```

**配置免密登陆**




## 外设与硬件
### 蓝牙操作



## 网络

### 连接wifi
### 路由
[静态路由](https://blog.csdn.net/u010521062/article/details/114067036)

[Linux 配置静态IP - chy_18883701161 - 博客园 (cnblogs.com)](https://www.cnblogs.com/chy18883701161/p/12396035.html#:~:text=配置静态IP 1 （1）先切换到网络管理的目录 cd %2Fetc%2Fsysconfig%2Fnetwork-scripts 看一下网络配置的文件： ls -l,8之前的版本，下面2条指令任一条都可以，都是重启network服务： service network restart systemctl restart network.service )





- fishros
- 虚拟机无法打开

> 虚拟机使用的是此版本 [VMware](https://so.csdn.net/so/search?q=VMware&spm=1001.2101.3001.7020) Workstation 不支持的硬件版本。
> 模块“Upgrade”启动失败。

打开`.vmx`文件，修改` virtualHW.version = "19"`一行至` virtualHW.version = "16"` 





## docker 
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

查看是否安装成功
```shell
[root@localhost ~]# docker-compose --version
Docker Compose version v2.16.0
```

### 换源
```shell
sudo vim /etc/docker/daemon.json
```
插入下面的句子，最后不要加逗号
```
{
    "registry-mirrors": ["https://dockerhub.icu"]
}
```
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

### 使用

```shell
docker-compose up
```



## Kali
### 系统烧录
!!! note "准备"
    - 下载[kali](https://www.kali.org/get-kali/#kali-platforms) 也可以在镜像站上下载[ZJU Mirror](https://mirror.zju.edu.cn/)
    - 下载烧录工具[Etcher](https://etcher.balena.io/#download-etcher)
    - 准备sd卡
    - 准备读卡器
    - 电脑

### 换源
[apt 换源](https://www.cnblogs.com/u-damowang1/p/14729017.html)


[The big list of Vim-like software (reversed.top)](https://reversed.top/2014-08-13/big-list-of-vim-like-software/)

```shell
vim /etc/apt/sources.list
```

[Kali Linux | ZJU Mirror](https://mirrors.zju.edu.cn/docs/kali/)
```
# zju source
deb https://mirrors.zju.edu.cn/kali kali-rolling main non-free contrib
#deb-src https://mirrors.zju.edu.cn/kali kali-rolling main non-free contrib

#中科大
deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib

#阿里云
deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib

#清华大学
deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
```

```shell
apt-get update
apt-get upgrade
```


### linux安装软件的方式
[deb]
[Appimage](https://cn.linux-console.net/?p=19002)








### phpstudy

[phpstudy on Kali](https://blog.csdn.net/weixin_54358903/article/details/127698009)

phpStudy是一个PHP调试环境的程序集成包。该程序包集成最新的Apache+PHP+MySQL+phpMyAdmin+ZendOptimizer，一次性安装，无须配置即可使用，是非常方便、好用的PHP调试环境。


```shell
wget -O install.sh https://notdocker.xp.cn/install.sh && sudo bash install.sh
```

```shell
phpstudy start # 启动
```

[ncat](https://nmap.org/ncat/)

```shell
sudo apt-get install ncat
```

### dirsearch

```
sudo apt-get install dirsearch
```

有很多依赖是没有安装的，这里手动安装一下

要注意`defusedxml`这个库不叫`defusexml`,安装带d的这一版才可以
```
pip install requests_ntlm
pip install defusedxml
pip install bs4
pip install jinja2
pip install colorama
```

### 菜刀 weevely
[weevely3下载](https://github.com/epinna/weevely3/archive/master.zip)

```shell
cd weevely3/
sudo pip install -r requirements.txt --upgrade
```

### 中国蚁剑
[中国蚁剑(antSword)下载、安装、使用教程-CSDN博客](https://blog.csdn.net/weixin_42474304/article/details/116376746)

[AntSwordProject/AntSword-Loader: AntSword 加载器](https://github.com/AntSwordProject/AntSword-Loader?tab=readme-ov-file)

[官方文档](https://www.yuque.com/antswordproject/antsword)

### 文件泄露分析

#### GitHack 

[lijiejie/GitHack: A \`.git\` folder disclosure exploit](https://github.com/lijiejie/GitHack)

```shell
GitHack.py http://www.example.com/.git/
```

#### dvcs-ripper
[dvcs-ripper](https://github.com/kost/dvcs-ripper#dvcs-ripper)

依赖安装
```shell
sudo apt-get install perl libio-socket-ssl-perl libdbd-sqlite3-perl libclass-dbi-perl libio-all-lwp-perl

sudo apt-get install libparallel-forkmanager-perl libredis-perl libalgorithm-combinatorics-perl

sudo apt-get install cvs subversion git bzr mercurial
```

使用方法

```shell
rip-git.pl -s -v -u http://www.example.com/.git/
```

### php

[Kali Linux 添加 add-apt-repository | Silearner](https://blog.chaos.run/dreams/kali-linux-ppa/index.html)

```shell 
File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 129, in lpppa
    self._lpppa = self.lpteam.getPPAByName(name=self.ppaname)
                  ^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 116, in lpteam
    self._lpteam = self.lp.people(self.teamname)
                   ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'people'
```
遇到的问题


```shell
pip install launchpadlib
```

发现是ppa.py文件的问题，所以修改一下文件导入的路径

```shell
find / | grep launchpadlib
```

```shell
import sys
sys.path.append(r'这里填入上一步搜出来的路径')
```

### nodejs
[nodejs on Kali](https://www.cnblogs.com/hirak0/p/16133730.html)
按照这个安装即可

```shell
wget  https://nodejs.org/dist/v16.14.2/node-v16.14.2-linux-x64.tar.xz

tar -xvf node-v16.14.2-linux-x64.tar.xz

mv node-v16.14.2-linux-x64 nodejs

sudo mv nodejs/ /usr/local/sbin/
```

创建软链接的方式
```shell
sudo ln -s /usr/local/sbin/nodejs/bin/node /usr/local/bin/
sudo ln -s /usr/local/sbin/nodejs/bin/npm /usr/local/bin/
```
很奇怪这里不输入绝对路径会有错误

### strace & ltrace
调试工具
```shell
sudo apt-get install strace ltrace
```

### Stegsolve
[在Kali Linux中下载工具Stegsolve - 平静的雨田 - 博客园](https://www.cnblogs.com/hardcoreYutian/p/10613036.html)

[linux 解决 " command not found: shopt "的 "\~/.bashrc" 配置问题-CSDN博客](https://blog.csdn.net/qq_36148847/article/details/79261067)

1. 安装[java环境](https://www.oracle.com/java/technologies/downloads/?er=221886)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240710122150.png)

```shell
tar -xzvf jdk-12_linux-x64_bin.tar.gz
mv jdk /opt
cd /opt/jdk
```

2. 设置环境变量，这里不要用`.bashrc`，而是`.zshrc`


```shell
gedit ~/.zshrc
export JAVA_HOME=/opt/jdk
export CLASSPATH=.:${JAVA_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

```shell
source ~/.zshrc
```

验证安装成功
```shell
java -version
```
出现类似于下面的文字即成功
>Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
>java version "22.0.1" 2024-04-16
>Java(TM) SE Runtime Environment (build 22.0.1+8-16)
>Java HotSpot(TM) 64-Bit Server VM (build 22.0.1+8-16, mixed mode, sharing)


前往[github库](https://github.com/Giotino/stegsolve/releases)，下载软件
```
wget https://github.com/Giotino/stegsolve/releases/download/v1.4/StegSolve-1.4.jar
mv StegSolve-1.4.jar StegSolve
```

直接使用
```
java -jar StegSolve
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240710122852.png)

!!! bug "若执行`source ~/.bashrc`会报错"
    [bash - shopt command not found in .bashrc after shell updation - Stack Overflow](https://stackoverflow.com/questions/26616003/shopt-command-not-found-in-bashrc-after-shell-updation)

    ```shell
    /home/amerrnath/.bashrc:17: command not found: shopt 
    /home/amerrnath/.bashrc:25: command not found: shopt 
    /home/amerrnath/.bashrc:109: command not found: shopt 
    /usr/share/bash-completion/bash_completion:35: parse error near `]]'
    ```
### 其他隐写工具

- steghide
steghide不支持png格式的隐写，zsteg支持png。
```shell
apt install steghide
```

- zsteg
[安装](https://blog.csdn.net/Amherstieae/article/details/107512398)

### go环境搭建
[参考](https://blog.csdn.net/single_g_l/article/details/123244435)
[go中文](https://studygolang.com/dl)

```shell
wget https://studygolang.com/dl/golang/go1.22.5.linux-amd64.tar.gz
tar -xzvf go1.22.5.linux-amd64.tar.gz
rm go1.22.5.linux-amd64.tar.gz
```

```shell
mv ./go /usr/local
```

**配置环境变量**

在`/home`目录下新建go目录（文件名随意），然后在go目录下分别新建三个目录：
- src ---- 里面每一个子目录，就是一个包。包内是Go的源码文件
- pkg ---- 编译后生成的，包的目标文件
- bin ---- 生成的可执行文件。


`vim ~/.zshrc` 编辑文件
 
 
在文件末尾中添加
```shell
export PATH=$PATH:/usr/local/go/bin   //  将 /usr/local/go/bin 目录添加至PATH环境变量
export GOPATH=/home/go                // 设置GOPATH环境变量
```

```shell
source ~/.zshrc
```

**验证安装**

```shell
$ go version
go version go1.22.5 linux/amd64

$ go
Go is a tool for managing Go source code.
Usage:
	go <command> [arguments]
```

### geth
[Downloads | go-ethereum](https://geth.ethereum.org/downloads)

下载后解压
```
tar -xzvf geth-linux-amd64-1.14.6-aadddf3a.tar.gz
cd geth-linux-amd64-1.14.6-aadddf3a
```

移动到对应位置`\usr\local`

```shell
cd /usr/local
mkdir geth
```

```shell
mv geth /usr/local/geth
vim ~/.zshrc
```

**示例**

下载学长给到的范例

```shell
geth attach http://localhost:8545
```
出现

```shell                
Welcome to the Geth JavaScript console!

instance: Geth/v1.13.4-stable-3f907d6a/linux-amd64/go1.21.3
at block: 345 (Sat Jul 13 2024 08:38:08 GMT-0400 (EDT))
 modules: eth:1.0 net:1.0 personal:1.0 rpc:1.0 web3:1.0

To exit, press ctrl-d or type exit
> 
```


### volatility
[内存取证-volatility工具的使用 （史上更全教程，更全命令）\_volatility内存取证-CSDN博客](https://blog.csdn.net/m0_68012373/article/details/127419463)


是一个内存取证的工具，依赖python2版本
所以先使用conda构建一个基于python2的环境
```shell
conda create -n vol python=2.7
conda activate vol
```

#### 安装依赖

**crypto**
```shell
pip install pycryptodome
```

**distorm3**
[vext01/distorm3: distorm3](https://github.com/vext01/distorm3)
下载源码后，进入到对应文件夹
```shell
cd distorm3
python setup.py install
```

#### 安装
[volatilityfoundation/volatility: An advanced memory forensics framework](https://github.com/volatilityfoundation/volatility)
下载源码
```shell
cd volatility
python setup.py install
```


**验证**

```shell
vol.py
```

```
> └─# vol.py       
> Volatility Foundation Volatility Framework 2.6.1
> ERROR   : volatility.debug    : You must specify something to do (try -h)
```