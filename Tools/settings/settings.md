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


### 如何让你的win11不再智障

#### 恢复win10开始菜单风格
![恢复win10开始菜单风格](https://cn.windows-office.net/common-images/classic-start-menu-in-windows-11-5189891/4cb15e48c390243f8252fb1dc1.jpg)

从任务栏中选择搜索按钮并输入`regedit`。



当注册表编辑器出现时，选择打开。

通过从左窗格中展开文件夹来导航至此处：

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`

右键单击左窗格中的高级，然后选择新建> DWORD（32 位）值。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240722095029.png)


输入此值作为新值的名称，然后按 Enter 保存它。

`Start_ShowClassicMode`

双击相同的值并将数据更改为1，然后选择确定。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240722095039.png)

重启你的电脑。重新启动 Windows 11 的最快方法是右键单击“开始”按钮，然后选择关机或注销>重新启动。注销并重新登录也可以。


#### 任务栏自定义
[如何调整 Windows 11 任务栏位置、对齐方式，及自定义任务栏](https://www.sysgeek.cn/windows-11-taskbar-customize/)

#### 右键菜单调整
[【Windows】Win11右键恢复完整右键菜单\_windows 11 classic context menu-CSDN博客](https://blog.csdn.net/u012153104/article/details/130195590)


使用快捷键`Win+X`，然后点击`Windows终端（管理员）`以打开管理员权限的命令提示符。

第一步

```shell
reg add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

如果操作成功，命令提示符会显示“操作成功完成”消息。


第二步，重启资源管理器进程。

```shell
taskkill /f /im explorer.exe
```

```shell
start explorer.exe
```


### 电脑蓝屏
查看错误原因

蓝屏以后先重启



#### 排查方法———WinDBG查看.dmp文件
[查找/分析Windows蓝屏DMP文件\_蓝屏文件在哪个文件夹-CSDN博客](https://blog.csdn.net/pzhier/article/details/102593562#)



下载WinDBG[64位](https://link.csdn.net/?target=https%3A%2F%2Fdownload.microsoft.com%2Fdownload%2FA%2F6%2FA%2FA6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D%2Fsetup%2FWinSDKDebuggingTools_amd64%2Fdbg_amd64.msi)


1. 运行Windbg，然后按Ctrl+S或从文件菜单中打开符号表设置窗；
2. 将符号表地址：`SRV*C:\Symbols*http://msdl.microsoft.com/download/symbols` 粘贴在输入框中，确定。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240720005545.png)


可使用`Ctrl+D`快捷键来打开一个dmp文件，或者点击WinDbg界面上的`File=>Open Crash Dump`按钮，来打开一个dmp文件。第一次打开dmp文件时，可能会收到如下提示，出现这个提示时，勾选`Don’t ask again in this WinDbg session`，然后点否即可

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240720005606.png)

!!! tip "打开第二个DMP文件"
    如果在打开第二个DMP文件时，可能因为上一个分析记录未清除，导致无法直接分析下一个dmp文件，可以使用快捷键`Shift+F5`来关闭上一个DMP的分析记录。


打开之后首先查看两点

- 第一个关键信息：`Probably caused by:`
- 第二个关键信息：找到并点击`！analyze –v `， 从弹出的内容中查找 `BUGCHECK_STR:`
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240720010134.png)


[Windows Bug Check Code Reference](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-code-reference2)



#### memory_management
[只要看直播或者b站视频就容易蓝屏 NGA玩家社区](https://ngabbs.com/read.php?tid=36810975&rand=354)

[在看B站时突然蓝屏，报错 VIDEO\_xxx，蓝屏上面还有B站横幅。 - Microsoft Community](https://answers.microsoft.com/zh-hans/windows/forum/all/%E5%9C%A8%E7%9C%8Bb%E7%AB%99%E6%97%B6%E7%AA%81/1c6e5719-545b-4f6e-9f39-5dfa49e218dc)



### 显示器相关

#### 如何修复Type-C接口

当我的type-c接口插了一段时间以后，接口就会出现松动的情况

用针头将两侧的钩子撑开，就可以解决一定问题



> 以下图片来自[USB TYPE C拆解以及USB3.1规范详解 (lulian.cn)](https://www.lulian.cn/news/88-cn.html)

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


### `conda`环境导出与导入
导出
```bash
conda list -e > requirements.txt
```

导入安装
```bash
conda install --yes --file requirements.txt
```

导出 yml 文件方式
```bash
conda env export > freeze.yml
```

安装
```bash
conda env create -f freeze.yml
```

### pip 导出环境

1. 导出结果含有路径
导出结果会存在路径，生成的requirements.txt文件在当前目录下。
```shell
pip freezen > requirements.txt
```

2. 导出不带路径的
生成的requirements.txt文件在当前目录下。
```shell
pip list --format=freeze > requirement.txt
```
生成requirements.txt，pip freeze会将当前PC环境下所有的安装包都进行生成,再进行安装的时候会全部安装很多没有的包.此方法要注意。

安装requirements文件的pip源的包
```shell
pip install -r requirements.txt
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



