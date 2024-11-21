# Kali Linux配置
!!! note "本篇记录一下Kali Linux的配置"


## 系统烧录
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


## linux安装软件的方式
[deb]
[Appimage](https://cn.linux-console.net/?p=19002)

## 问题

### 图形化界面消失解决方法

```shell title="打开图形化"
startx
```
先试一下这一条指令，如果不行可能是一些包出现了问题


```shell
sudu su
apt-get update 
apt-get upgrade
```

```shell
apt-get clean
apt-get remove xfce4 xfce4-places-plugin
apt-get install x-window-system-core
apt-get install gnome-core
apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin
```



桌面出现了！
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241119103146.png)

### 桌面不显示
!!! bug "建议操作之前请创建快照！！！"

=== "方法1"

    在kali终端执行以下命令：

    ```shell
    sudo metacity --replace      #打开窗口管理器
    ```
    
    如果没有metacity这个命令，就下载一下

    ```shell
    apt-get install metacity          #下载metacity命令
    ```

    下载之后再执行一遍上面那个命令就好了

    但有一个问题：每次打开kali都需要运行一遍上面第1条命令

=== "方法2"

    重装lightdm，命令如下：

    ```shell
    sudo apt-get remove --purge lightdm
    sudo apt-get install lightdm
    ```

## conda环境
[Index of /anaconda/miniconda/ | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/)





## Web软件

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


## Misc 软件

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


## Rev
### strace & ltrace
调试工具
```shell
sudo apt-get install strace ltrace
```