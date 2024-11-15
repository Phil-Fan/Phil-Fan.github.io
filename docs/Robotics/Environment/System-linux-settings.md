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
### VMware 无法复制问题的解决 

### 安装VMware Tools选项显示灰色的正确解决办法  

1.关闭虚拟机；  

2.在虚拟机设置分别设置CD/DVD、CD/DVD2和软盘为自动检测三个步骤；  

3.再重启虚拟机，灰色字即点亮。 

4.重新安装vmware-tools  

- 虚拟机无法打开

> 虚拟机使用的是此版本 [VMware](https://so.csdn.net/so/search?q=VMware&spm=1001.2101.3001.7020) Workstation 不支持的硬件版本。
> 模块“Upgrade”启动失败。

打开`.vmx`文件，修改` virtualHW.version = "19"`一行至` virtualHW.version = "16"` 



## 系统烧录



## 系统配置

### 换源


```shell
lsb_release -a
uname -a
```

```shell
vim /etc/apt/sources.list
```

!!! tip "注意换源的时候注意备份之前的"
    ```shell
    sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
    ```

20.04版本的源

=== "清华源"
    [ubuntu | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

    ```shell
    # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```

=== "aliyun源"
    [ubuntu镜像\_ubuntu下载地址\_ubuntu安装教程-阿里巴巴开源镜像站](https://developer.aliyun.com/mirror/ubuntu)

    ```shell
    deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
    deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
    deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
    ```

=== "ustc源"

    ```
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
    deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
    ```


=== "zju"

    ```shell
    deb https://mirrors.zju.edu.cn/ubuntu/ focal main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
    deb https://mirrors.zju.edu.cn/ubuntu/ focal-security main restricted universe multiverse
    ```
    
=== "鱼香ros"
    ```shell
    wget http://fishros.com/install -O fishros && . fishros
    ```

```shell
sudo apt-get update
sudo apt-get upgrade
```


!!! failure "404"
    [Ubuntu 换源后仍然报错：404、没有 Release 文件\_没有release文件所以禁用-CSDN博客](https://blog.csdn.net/ys743276112/article/details/127436835)
    [sudo apt-get update 命令出现没有Release文件问题解决\_debian apt get update 没有release 文件-CSDN博客](https://blog.csdn.net/A18040554844/article/details/110099737)

    另外的解决方法，拉取https问题
    ```shell
    sudo apt install apt-transport-https
    sudo apt install ca-certificates
    ```
### 中文系统
在系統中添加中文語言，既可以顯示中文，也可以輸入中文。

### 分辨率

```shell
xrandr
xrandr -s 1280x768
xrandr -s 1 #(1是顺序号，即xrandr给出的2560ｘ1600。)
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914102150.png)



在`/boot/grub/`下的`menu.lst`文件

先cat menu.lst 查看文件内容。
```shell
gedit menu.lst
vim menu.lst
```
等都可以改。其中这个vga=788就是控制你的分辨率与色彩模式的，你可以把它改成你的显示器支持的你喜欢的任意模式。

[linux 下更改分辨率](https://blog.csdn.net/SueMagic/article/details/89399959)


!!! failure "无法获得锁 /var/lib/dpkg/lock-frontend - open "
    ```shell
    ps -e | grep apt
    ```

    ```
    > 3209 ? 00:00:00 apt.systemd.dai
    > 3213 ? 00:00:00 apt.systemd.dai
    ```
    
    杀死进程并切换到sudo权限[完美解决“无法获得锁 /var/lib/dpkg/lock-frontend - open (11: 资源暂时不可用)无法获取 dpkg 前端锁 (/var/lib/dpkg/lock-f”的问题](https://blog.csdn.net/diaodaa/article/details/104516036)

### 查看系统信息

查看cpu信息
```bash
cat /proc/cpuinfo
```

查看系统架构
```bash
uname - a
```
[x86-64、amd64、arm、aarch64 都是些什么？-CSDN博客](https://blog.csdn.net/qq_24433609/article/details/125991550)


```
sudo !4
```
执行历史记录中第4条命令

### 更改密码

```shell
passwd
```
更改其他用户密码
```shell
sudo passwd username
```

更改root密码
```shell
sudo passwd root
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

### 新立得 

```shell
sudo apt install -y synaptic
```
### nano
常见操作

|操作|快捷键|
|---|---|
|保存|`Ctrl + O`|
|退出|`Ctrl + X`|
|删除|`Ctrl + K`|


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
sudo apt install net-tools
```

```shell
ifconfig
```

```shell
sudo apt-get install openssh-server
ssh user@remote
ssh -X ldz@192.168.0.1  # 带图形化界面
ssh -p 1234 ldz@192.168.0.1 # 指定端口
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

```shell
ssh-keygen -t rsa
```
然后根据提示一步步的按enter键即可（其中有一个提示是要求设置私钥口`passphrase`，不设置则为空，这里看心情吧，如果不放心私钥的安全可以设置一下）

执行结束以后会在`/home/当前用户` 目录下生成一个 `.ssh` 文件夹,其中包含私钥文件 `id_rsa` 和公钥文件 `id_rsa.pub`。

ssh-copy-id会将公钥写到远程主机的 `~/.ssh/authorized_key` 文件中

```shell
ssh-copy-id name@ip
```

注意，windows的cmd中不能直接执行ssh-copy-id命令，可以使用git bash或者其他linux终端工具

当出现
> Number of key(s) added: 1
> Now try logging into the machine, with:   "ssh 'HAHA@127.0.0.1'" and check to make sure that only the key(s) you wanted were added.

说明配置成功！


[深入理解\~/.ssh/config和/etc/ssh/ssh\_config配置文件-百度开发者中心](https://developer.baidu.com/article/details/2922032)

!!! failure "错误与解决方法"
    === "WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!"
        警告：远程主机标识已更改！

        此报错是由于远程的主机的公钥发生了变化导致的。 ssh服务是通过公钥和私钥来进行连接的，它会把每个曾经访问过计算机或服务器的公钥（public key），记录在~/.ssh/known_hosts 中，当下次访问曾经访问过的计算机或服务器时，ssh就会核对公钥，如果和上次记录的不同，OpenSSH会发出警告。

        ```shell title="解决方法"
        ssh-keygen -R XX.XX.XX.XX 
        ```
    
    === "连接IPV6地址"
        ```shell
        ssh -6 user@ipv6
        ```

### conda
[conda换地址](https://blog.csdn.net/chengjinpei/article/details/119835339)


清华镜像地址：`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/`

按照你系统的架构选择合适的下载
```shell
uname -m
```

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```
下载后执行得到的文件
```shell
bash Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```

一路点enter和yes，最后重启终端，得到带有`(base)`的提示符，说明安装成功


### nomachine
## 外设与硬件
### 蓝牙操作

打开系统蓝牙
```shell
systemctl status bluetooth
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914224410.png)
```shell
sudo service bluetooth start
```

```shell
sudo /etc/init.d/bluetooth restart
```

```shell title="管理界面"
bluetoothctl
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914224418.png)
输入以下命令
```shell
list 
scan on 
devices
power on
agent on 
default-agent
pair yourDeviceMAC
```

其中pair后面跟上扫描出的键盘的MAC地址，根据提示输入密码，显示配对成功，此时，在桌面的设置界面“我的设备”中可以看到蓝牙中键盘为已配对状态，但此时可能依然无法成功连接。


## 网络

### 连接wifi

```shell    
sudo vim /etc/netplan/50-cloud-init.yaml
```

```yaml
network:
  ethernets:
    enp2s0:
      dhcp4: true
  wifis:
    wlan0:
      dhcp4: true
      access-points:
        "<ssid>":
          password: "<passowrd>"
  version: 2
```


设置好之后退出，重启网络
```shell
sudo netplan apply
```

1.该编辑文件中**不能出现制表符**，要不然会有问题；在执行后面的命令会报错；

2.改文件的编辑必须严格按照格式来，**是分层的**，用空格来退格

[启动 netplan-wpa-wlan0.sevice 失败：未找到单元 netplan-wpa-wlan0.service - ubuntu](https://askoverflow.dev/ubuntu/question/1291424/failed-to-start-netplan-wpa-wlan0-sevice-unit-netplan-wpa-wlan0-service-not-fou/)
!!! tip "注意事项"
    出现类似错误：`line8 column 6:cloud not find expected` 提示是**冒号：后面没加空格**

    出现类似错误：`netplan found character that cannot start any token`，提示是没有按五个层次写配置文档，一定要**下一层比上一层多空一格或以上。**

    出现类似错误： `Invalid YAML: inconsistent indentation:`  #缩进不对，就是**每一层没有严格缩进**


```shell
sudo apt install net-tools wireless-tools network-manager
```
### 校网验证
`net2.zju.edu.cn`


[QSCTech/zjunet: Command Line Scripts for ZJU (VPN / WLAN / DNS)](https://github.com/QSCTech/zjunet)

w3m之类的命令行浏览器试试

[比较简单的ubuntu 18.04 有线连接校园网的方法 - CC98论坛](https://www.cc98.org/topic/4899317/1#1)


### 路由
[静态路由](https://blog.csdn.net/u010521062/article/details/114067036)

[Linux 配置静态IP](https://www.cnblogs.com/chy18883701161/p/12396035.html)




### 内网穿透
[校园网内登录寝室电脑远程桌面和ssh连接WSL - 知乎](https://zhuanlan.zhihu.com/p/627393030)
[干货 | 在校园网中用ssh连接宿舍电脑](https://kegalas.top/p/%E5%B9%B2%E8%B4%A7-%E5%9C%A8%E6%A0%A1%E5%9B%AD%E7%BD%91%E4%B8%AD%E7%94%A8ssh%E8%BF%9E%E6%8E%A5%E5%AE%BF%E8%88%8D%E7%94%B5%E8%84%91/)

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


## Q & A

> sh: 0: getcwd() failed: No such file or directory

一般来说是因为你 cd 到了某个目录之后 rm 了这个目录，这时去执行某些 service 脚本的时候就会报 get cwd 错误。 只需要 cd 到任何一个实际存在的目录下再执行就好了

