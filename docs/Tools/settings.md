# 环境配置

## 如何复制Phil Fan的工作环境

### 效率软件

- 日程 - 滴答清单
- Markdown - Typora
- 图片： HoneyView，PicGo（图床）
- 视频：QQ影音
- 思维导图: Xmind
- 计时：ManicTime
- 绘图：Draw.io, Geogebra
- PDF阅读：Adobe Acrobat
- 云同步：百度网盘、阿里网盘
- 即时通讯：TIM，WeChat，飞书，腾讯会议，钉钉
- 压缩：Bandzip
- 浏览器：Edge
- 翻译：欧陆词典

### 专业软件

- Coding: VSC, PyCharm, WebStorm
- 环境：python，R，VMware，anaconda，git
- 数据：Tableau，excel，origin
- 文献：Zotero
- word，小恐龙公文助手
- latex：overleaf


- [foldersize](https://foldersize.sourceforge.net/?utm_source=appinn.com)
### 设计软件

- Adobe: AI,PS,PR,剪映
- powerpoint，okplus，Canva




## windows

电脑

[AirPods Pro2蓝牙耳机连接win10电脑有杂音、不稳定问题 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/641213713)


### win+G 录屏
xGameBar对我来说没什么用，但是虚拟机中需要使用到这个快捷键，所以将win下这个快捷键禁用

`win+I`进入设置，搜索Game Bar

关闭里边选项即可。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240706192241.png)

### 显示器相关

#### 如何修复Type-C接口

当我的type-c接口插了一段时间以后，接口就会出现松动的情况

用针头将两侧的钩子撑开，就可以解决一定问题



> 以下图片来自[USB TYPE C                             拆解以及USB3.1规范详解 (lulian.cn)](https://www.lulian.cn/news/88-cn.html)

![USB Type C接头拆解图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1540889232305758.jpg)

![USB Type C接头拆解图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1540889232965453.jpg)

**盒盖不息屏**

设置里搜“关闭盖子”

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-debea2bfb9bc1c5d7449c2a6c7080dfd_720w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-79a54efe642a46bd24107b2a97f160d1_720w.webp)



**Windows +A**进入消息中心

![image-20240429090307137](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090307137.png)

![image-20240429090336993](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090336993.png)

打开显示设置，调节分辨率

![image-20240429090404258](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090404258.png)



### 环境变量

#### 使用命令行调用不同版本的python

在系统路径path（高级系统系统设置——环境变量）中加入python.exe所在目录（打开文件所在位置——属性——打开文件所在位置）（因为是快捷方式，所以需要先找到快捷方式所在目录，再找到原exe文件所在位置）

**注：应考虑到优先级的问题，将想要通过命令行直接进入的python版本所对应的路径放在上面**





#### 如何用命令行直接打开软件

省流：建立一个文件夹保存快捷方式，将文件夹路径添加到PATH环境变量

首先你要创建一个文件夹，存储程序的快捷方式



- 右键点击计算机图标，选择属性，选择高级系统设置，高级->选择环境变量

- 编辑用户变量下的PATH复制存储快捷方式文件夹的路径

备注：快捷方式可以自定义名称，在CMD中输入名称就行了

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201221085949893.png)

高级系统设置 - 环境变量

![image-20240422084315579](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422084315579.png)

## `Vimium`配置

[使用 Vimium 获得更舒适的网页阅读体验 - 少数派 (sspai.com)](https://sspai.com/post/57091#!)

## `pytorch`

```shell
import torch # 如果pytorch安装成功即可导入
print(torch.cuda.is_available()) # 查看CUDA是否可用
print(torch.cuda.device_count()) # 查看可用的CUDA数量
print(torch.version.cuda) # 查看CUDA的版本号

# 查看CUDA的版本
nvcc -V
nvcc --version

# 查看CUDA版本
nvidia-smi
```



## `conda`

[conda换地址](https://blog.csdn.net/chengjinpei/article/details/119835339)


清华镜像地址：`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/`




下载之后
```shell
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
```

[conda 使用指南](https://blog.csdn.net/miracleoa/article/details/106115730)

激活
```shell
source ~/anaconda3/bin/activate
```




```shell
# 切换盘符
cd /d d:

conda --version
conda -V #获取版本号

# 1. 创建虚拟环境
conda create -n your_env_name(虚拟环境名称) python==xx(想要创建的虚拟环境的python版本号)
 
# 在指定的位置创建虚拟环境
conda create -p /PATH/TO/path
conda env list # 查看所有的conda虚拟环境  
conda list # 检查安装
 
# 2. 激活虚拟环境
conda activate name
conda deactivate
conda env remove -n flowers
 
# 5. 安装包
conda install package_name(包名)
conda install scrapy==1.3 # 安装指定版本的包
conda install -n 环境名 包名 # 在conda指定的某个环境中安装包
 
# 6. 跳过安装失败的包，继续安装
# conda方式
while read requirement; do conda install --yes $requirement; done < requirements.txt
 
# pip方式
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```

导出
```
conda list -e > requirements.txt
```

导入安装
```
conda install --yes --file requirements.txt
```

导出 yml 文件方式
```
conda env export > freeze.yml
```

安装
```
conda env create -f freeze.yml
```


## `Pycharm`

### 申请学生权限



语言设置为中文

setting-plugin-chinese





### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你Pycharm远程连接服务器端项目进行本地开发调试！...-CSDN博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)





## 搜狗输入法

搜狗输入法老是出现快捷键冲突或是占用热键的情况

所以进入设置界面 - 按键 - ban掉系统功能快捷键

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201218111624799.png)

![image-20240619085926633](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240619085926633.png)

## vscode

**markdown 插件 —— Markdown Preview Enhanced**

设置一个`picgo`的快捷键，我这里设置的是`ctrl + alt + P`

截图之后直接按就可以将图片上传到图床，并将连接复制到剪贴板

**vim插件 —— vim**


**copy as markdown**

[chorme下载地址](https://microsoftedge.microsoft.com/addons/detail/copy-as-markdown/cbbdkefgbfifiljnnklfhnhcnlmpglpd)

解决链接复制之后只有url没有标题的问题


## Kali
### 换源
[apt 换源](https://www.cnblogs.com/u-damowang1/p/14729017.html)


[The big list of Vim-like software (reversed.top)](https://reversed.top/2014-08-13/big-list-of-vim-like-software/)

```shell
vim /etc/apt/sources.list
```

```
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


### SSH
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




### 软件安装
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

1. 用kali内嵌的浏览器搜索vscode，下载vscode的.deb格式的安装包
2. 在终端中输入 `sudo dpkg -i code_1.72.1-1665423861_amd64.deb` 进行解压包
3. 在vscode软件上点击鼠标右键，点击 `Edit Application`
4. 有个Command选项，输入 `/usr/share/code/code --unity-launch %F --no-sandbox` 即可，再点击保存。




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

> └─# vol.py       
> Volatility Foundation Volatility Framework 2.6.1
> ERROR   : volatility.debug    : You must specify something to do (try -h)

### docker 
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
#### 文档

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

#### 使用

```shell
docker-compose up
```