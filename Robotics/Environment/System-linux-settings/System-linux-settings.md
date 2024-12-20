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

=== "鱼香ros"
    ```shell
    wget http://fishros.com/install -O fishros && bash fishros
    ```

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


### PS1修改

```shell
vim ~/.bashrc
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

## 压缩
```shell title="递归压缩"
zip -r examples.zip examples   # examples为目录
```

```shell title="解压缩"
unzip name.zip
```

```shell title="目录路径来指明压缩包所在的位置"
unzip name.zip -d 当前目录
```

```shell title="如果是压缩包是.tar后缀"
tar xvf name.tar 
```


## 复制 scp

[关于scp传输文件踩过的坑(最全!linux与windows相互传输文件,连接失败,免密登录,连接超时) - 知乎](https://zhuanlan.zhihu.com/p/542926236)


### 基本语法

```shell
scp [可选参数] 源文件 目标文件
```


```shell
# 复制文件
scp local_file remote_username@remote_ip:remote_folder
scp local_file remote_username@remote_ip:remote_file

# 复制目录
scp -r local_folder remote_username@remote_ip:remote_folder
```


- `-r`: 递归复制整个目录
- `-P port`: 指定远程主机的端口号
- `-p`: 保留原文件的修改时间和访问权限
- `-q`: 不显示传输进度条
- `-C`: 允许压缩
- `-v`: 详细方式显示输出

### 示例
```shell
# 复制本地文件到远程服务器
scp file.txt user@192.168.1.100:/home/user/

# 复制远程文件到本地
scp user@192.168.1.100:/home/user/file.txt ./

# 复制整个目录
scp -r local_folder user@192.168.1.100:/home/user/

# 使用特定端口
scp -P 2222 file.txt user@192.168.1.100:/home/user/
```


## 局域网
```shell
apt-get install -y cifs-utils
```
### windows做服务器
[在windows上共享文件夹](https://zhuanlan.zhihu.com/p/402820328)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026225133.png)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026225143.png)

### windows作客户端


如果你是没有打开smb服务，那么继续往下看，打开控制面板进入

点击“启用或关闭windows功能”

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241123092300.png)

把smb的几个都点开，然后点击确定，立即重启

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241123092342.png)


然后直接在explorer中输入ip地址即可。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241123092550.png)


注意输入的格式：
- 不是`smb://156.26.51.55 `
- 而是应该直接`双斜杠+ip地址`，如果有具体的共享的文件夹的话就把路径跟在后面。不需要加smb前缀，也不能用 `//` ，要用 `\\`,然后输入对应的账户和密码就完事了。
> [window10 使用smb连接远程电脑的文件夹[打开smb服务和连接巨坑]-CSDN博客](https://blog.csdn.net/qq_44079295/article/details/120201515)
### linux做服务器——samba

```shell title="安装"
sudo apt install samba
```

```shell title="启动服务"
systemctl start smbd.service

systemctl enable smbd.service

systemctl start nmbd.service

systemctl enable nmbd.service
```

```shell
systemctl status smbd.service
systemctl status nmbd.service
```

```shell title="设置共享文件夹"
net usershare add "共享名" /home/Desktop/文件名 "备注名" Everyone:R guest_ok=y
```

|参数|含义|
|---|---|
|Everyone:R	|设置Everyone用户为只读权限|
|Everyone:F	|设置Everyone用户为可写权限|
|Everyone:D	|设置Everyone用户为拒绝权限|
|guest_ok=y	|允许匿名访问|
|guest_ok=n	|不允许匿名访问|




```shell title="客户端侧安装"
sudo apt install smbclient
```

```shell title="使用命令登录"
smbclinet //ip/name -U xxx
```



> [Linux 上挂载 Samba（Windows & macOS 共享文件夹）的正确姿势 - 知乎](https://zhuanlan.zhihu.com/p/26763026)

!!! tip "注意权限问题"
    1. 设置了当前共享文件夹有可写权限的话，那么需要增加当前文件夹的other的写权限

    2. 设置了匿名访问的话需要设置当前目录以及这个目录的父目录的other的可执行权限

    不然的话，不管使用命令访问还是使用图形界面访问都是会导致**报错没有权限**的问题



### linux作客户端——挂载文件系统

```shell title="举例"
smbclient -L 192.168.1.70 -U lab

Enter lab's password:   #输入密码，不回显
Domain=[WIN7] OS=[Windows 7] Server=[Windows 7]
   #共享点名称#      #类型#      #描述# 
    Sharename       Type      Comment
    ---------       ----      -------
    ADMIN$          Disk      远程管理
    Share               Disk      
    C$              Disk      默认共享
Connection to 192.168.1.70 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND) 
NetBIOS over TCP disabled -- no workgroup available #可能会出现一些错误警告，不过可以列出的话就不用管
```


将 `//<ip>/test` 挂载到 `/mnt/` 目录上，如果不需要认证，则无需指定用户名和密码。

```shell
sudo mount -t cifs //<ip>/test /mnt/test_shared -o dir_mode=0777,file_mode=0777
```

[linux mount挂载文件夹设置权限 - 秋声梧叶 - 博客园](https://www.cnblogs.com/sctrkb/articles/15407736.html)


开机自动挂载（修改 `/etc/fstab` 文件）：

将`//192.168.xx.xx/sharedir`挂载到`/mnt/cifs`上，并指定了用户名和密码;如果不需要认证，可以不指定用户名和密码。
```shell
//192.168.3.4/sharedir /mnt/cifs cifs username=demo,password=demo 0 0
```

然后可以把`/mnt/folder`直接当作linux中的文件夹进行文件的操作


```shell title="解除挂载"
umount /dev/hda2
```

> pywin32库没有安装好 [Python 如何通过Python访问Windows网络上的共享文件夹|极客教程](https://geek-docs.com/python/python-ask-answer/311_python_using_python_how_can_i_access_a_shared_folder_on_windows_network.html)




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


## 用户设置

### 新建用户

```shell title="创建root用户"
sudo passwd root
```

```shell title="创建普通用户"
sudo adduser username
```
```shell title="删除用户"
sudo userdel -r username
```

```shell title="查看密码"
sudo grep bash /etc/passwd
```
### 用户权限

```shell title="给新用户root权限"
sudo usermod -a -G adm username
sudo usermod -a -G sudo username
```

## Q & A

!!! bug "sh: 0: getcwd() failed: No such file or directory"
    一般来说是因为你 cd 到了某个目录之后 rm 了这个目录，这时去执行某些 service 脚本的时候就会报 get cwd 错误。 只需要 cd 到任何一个实际存在的目录下再执行就好了

!!! question "Could not load the Qt platform plugin “xcb“"

    经过一番深入的探索，最终找到了一个有效的解决方案，即通过以下命令安装所有与libxcb相关的库：
    ```shell
    sudo apt install libxcb-*
    ```
    这条命令会安装所有以libxcb为前缀的库，确保系统中所有与XCB相关的依赖项都被正确安装。这一步成功解决了Qt无法加载xcb插件的问题，程序也顺利启动并运行。这表明，问题的根源在于某些关键的XCB依赖项缺失，而通过这种“一网打尽”的方式，我们可以确保所有相关的依赖项都得到满足。

## Java

### `.jar`文件打开方式

1.双击打开

2. 命令行打开x

```shell
java -jar xxx.jar
```

```shell title="后台执行"
java -jar xxx.jar &
```

```shell title="不挂断执行"
nohup java -jar test_jar-1.0-SNAPSHOT.jar &   
```  

nohup 意思是不挂断运行命令，当账户退出或终端关闭时，程序仍然运行。

当用 nohup 命令运行jar包时，缺省情况下该应用的所有输出被重定向到nohup.out的文件中，除非另外指定了输出文件。