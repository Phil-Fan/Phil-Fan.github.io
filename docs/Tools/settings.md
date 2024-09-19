# 环境配置
!!! note "前言"
    这一篇的目的是记录一些常用的软件的安装与使用，以及一些常见的问题的解决方案。遇到重复的问题不至于反复搜索。
    另外也是为了在特殊环境下，可以迅速的切换到另一台设备进行工作，不至于项目停滞。

## 如何复制Phil Fan的工作环境

### 效率软件

!!! note "以下顺序为安装顺序"

- 浏览器：[Edge](https://www.microsoft.com/zh-cn/edge/download)
- 日程: [滴答清单(付费)](https://dida365.com/download?language=zh_CN)
- 网络相关：[Clash for windows](https://www.clash.la/archives/748/)
  [v2rayN](https://github.com/2dust/v2rayN/releases),[下载 .NET 8.0 Desktop Runtime (v8.0.8) - Windows x64 Installer](https://dotnet.microsoft.com/zh-cn/download/dotnet/thank-you/runtime-desktop-8.0.8-windows-x64-installer?cid=getdotnetcore)
- 压缩：[Bandzip](https://www.bandisoft.com/bandizip/)
- 图片： [bandView](https://www.bandisoft.com/bandiview/)，[PicGo（图床）](https://github.com/Molunerfinn/PicGo/releases),[honeycam(动图)](https://www.bandisoft.com/honeycam/)
- 多媒体：[VLC media player](https://www.videolan.org/vlc/index.zh_CN.html),QQ影音
- 思维导图: [Xmind(付费)](https://xmind.cn/download/)，xmind zen 绿色版；首选项设置 深色主题 `alt+s`:概要 `ctrl + l`:方程
- 即时通讯：[TIM](https://tim.qq.com/download.html)，[WeChat](https://weixin.qq.com/)，[飞书](https://www.feishu.cn/download/)，[腾讯会议](https://meeting.tencent.com/download/)，[钉钉](https://page.dingtalk.com/wow/z/dingtalk/simple/ddhomedownload#/),[微信文件传输网页版](https://filehelper.weixin.qq.com/)
- 使用时长统计：[ManicTime](https://www.manictime.com/download/windows)
- PDF阅读：Adobe Acrobat(adobe处下载),[pdfedit](http://pdfedit.cz/en/download.html)
- Markdown: [Typora](https://typoraio.cn/)
- 云同步(付费)：[百度网盘](https://pan.baidu.com/download#win)、[阿里网盘](https://www.alipan.com/)
- 下载：[utorrent](https://file.cc98.org/v2-upload/il0glpvw.zip)


- 翻译：[欧陆词典](https://www.eudic.net/v4/en/app/download),欧陆词典文件
- 音乐：QQ音乐
- 其他：[logi option+](https://www.logitech.com/zh-cn/setup/ergosetup/logi-options.html),[foldersize(快速测文件夹大小)](https://foldersize.sourceforge.net/?utm_source=appinn.com)

### 专业软件

- Coding: [VSC](https://code.visualstudio.com/Download),PyCharm, WebStorm
- Environment:[miniconda(smaller)](https://docs.anaconda.com/miniconda/)/[anaconda](https://www.anaconda.com/download)
[git](https://git-scm.com/download/win),R,VMware
- 文献：[Zotero](https://www.zotero.org/download/)
- latex：texlive,[overleaf](https://www.overleaf.com)
- 绘图：ppt,Draw.io, ai,ps,Geogebra,python
- 数据：excel，Tableau，origin
- word，[小恐龙公文助手](https://xkonglong.com/xkl_wordaddin/)
- 驯化windows dism++ [Releases · Chuyu-Team/Dism-Multi-language](https://github.com/Chuyu-Team/Dism-Multi-language/releases)
- 音乐：[Sibelius(西贝柳斯)打谱软件](https://sibelius.mairuan.com/)

### 设计软件

- [Adobe](https://www.adobe.com/cn/):AI,PS,PR,[剪映](https://www.capcut.cn/)
- powerpoint,okplus,[Canva](https://www.canva.cn/)



## windows

电脑

[AirPods Pro2蓝牙耳机连接win10电脑有杂音、不稳定问题 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/641213713)

### Edge
#### `Vimium`配置

[使用 Vimium 获得更舒适的网页阅读体验 - 少数派 (sspai.com)](https://sspai.com/post/57091#!)

### 查看系统架构
`win+R`输入`cmd`，输入`wmic os get osarchitecture`查看系统架构

或者输入`dxdiag`查看系统信息

或者输入`systeminfo`查看,系统类型字段就可以看出来了
### win+G 录屏
xGameBar对我来说没什么用，但是虚拟机中需要使用到这个快捷键，所以将win下这个快捷键禁用

`win+I`进入设置，搜索Game Bar

关闭里边选项即可。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240706192241.png)

### 搜狗输入法

搜狗输入法老是出现快捷键冲突或是占用热键的情况

所以进入设置界面 - 按键 - ban掉系统功能快捷键

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201218111624799.png)

![image-20240619085926633](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240619085926633.png)
### 驯服自带输入法

- **自定义短语**

输入法内置了大多数常用的短语，但我们依然可以进行自定义导入，以满足自身行业的特殊词汇需求。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240816114002.png)
- **专业词典**

专业词典选项会被大部分人忽略——因为它看起来默认开启，但没有完全启用。

- **「V模式」**
  
颇有意思，v键进入后，可快速输入中文年月日时间以及公式运算等。

例如，你输入“`v123`”，在按a选择，呈现的结果就是“一百二十三”

`v12:55`，对应：十二时五十五分/ 12时55分 / 十二分五十五秒 等

`v1989.08.12`，对应：1989年08月12/  一九八九年八月十二日 等
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240816114019.png)

- **「U模式」**

则方便用户输入一些特殊符号。如win笔记本键盘上并不存在的「」，就可以在输入 uubd 后找到。

- **其他**
  
输入sjx，可以得到三角形 △ ▲
输入slh，可以得到省略号
输入pzh，可以得到中文破折号

- **emoji、颜文字与符号面板**
  
微软内置了emoji方案、颜文字、符号面板，使用 `Ctrl + Shift + B` 即可唤出。
[一些小技巧，让你的 Win 10 内置输入法更好用 - 少数派](https://sspai.com/post/52101#!)

### 如何让你的win11不再智障
- 驯化windows的软件**dism++** ，内置了很多小功能  [Releases · Chuyu-Team/Dism-Multi-language](https://github.com/Chuyu-Team/Dism-Multi-language/releases)


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
#### 恢复win10开始菜单风格
![恢复win10开始菜单风格](https://cn.windows-office.net/common-images/classic-start-menu-in-windows-11-5189891/4cb15e48c390243f8252fb1dc1.jpg)

从任务栏中选择搜索按钮并输入`regedit`。



当注册表编辑器出现时，选择打开。

通过从左窗格中展开文件夹来导航至此处：

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced`

右键单击左窗格中的高级，然后选择新建> DWORD（32 位）值。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240722095029.png)


输入`Start_ShowClassicMode`作为新值的名称，然后按 Enter 保存它。双击并将数据更改为1，然后选择确定。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240722095039.png)

重启。


#### 任务栏自定义
[如何调整 Windows 11 任务栏位置、对齐方式，及自定义任务栏](https://www.sysgeek.cn/windows-11-taskbar-customize/)




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

#### 盒盖不息屏

设置里搜“关闭盖子”

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-debea2bfb9bc1c5d7449c2a6c7080dfd_720w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-79a54efe642a46bd24107b2a97f160d1_720w.webp)


#### 投屏方式
**Windows +A**进入消息中心

![image-20240429090307137](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090307137.png)

![image-20240429090336993](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090336993.png)

打开显示设置，调节分辨率

![image-20240429090404258](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090404258.png)



### 环境变量

#### python
如果设置了环境变量，却打不开python，可以尝试将python的路径放在最前面

#### 如何用命令行直接打开软件

省流：建立一个文件夹保存快捷方式，将文件夹路径添加到PATH环境变量

首先你要创建一个文件夹，存储程序的快捷方式



- 右键点击计算机图标，选择属性，选择高级系统设置，高级->选择环境变量

- 编辑用户变量下的PATH复制存储快捷方式文件夹的路径

备注：快捷方式可以自定义名称，在CMD中输入名称就行了

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201221085949893.png)

高级系统设置 - 环境变量

![image-20240422084315579](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422084315579.png)

### win 终端

快捷打开终端
1. `win + R`，输入`cmd`
2. `win + X`，选择`Windows Terminal`

常用命令

1. 删除文件：`del` 文件名
2. 查看ip命令：`ipconfig`
3. 清屏：  `clear`    (cmd窗口清屏用cls)
4. 查看列表(list)：`ls`  （cmd窗口用dir） 
5. 切换目录：`cd xxx`    直接切换到xxx文件夹
6. 切换盘符：`d:`    切换到D盘；`cd /d D:\Code`直接切换到D盘下的Code文件夹；但要注意，如果是在C盘下，直接输入`cd /d`是无法切换的

??? failure "无法加载WindowsPowerShell\profile.ps1"
    [完美解决无法加载文件 WindowsPowerShell\profile.ps1系统编译问题-CSDN博客](https://blog.csdn.net/weixin_41194129/article/details/140538410)
    1. 按`Win + X` 键,`Windows PowerShell (Admin)`
    2. 使用命令 `Get-ExecutionPolicy -List`
    3. 更改执行策略：为了允许运行脚本，你可以将执行策略更改为 RemoteSigned 或 Unrestricted。
    ```shell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    如果你需要为所有用户设置执行策略，可以使用 -Scope LocalMachine 参数：
    ```shell
    Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
    ```
    4. 选择`Y`确认更改
    5. 重新打开终端
    6. 验证执行策略是否更改成功
    ```shell title="路径改为本地报错时候显示的路径"
    Get-Item "C:\Users\Administrator\Documents\WindowsPowerShell\profile.ps1" | Format-List * -Force
    ```

### 网络相关

#### 查看wifi密码

#### clash忘记关了解决方案
- `win+x` 点击网络连接
- 点击高级网络设置，“Internet选项”
- 点击“连接”弹窗的“局域网设置”
- 取消代理服务器这里的对勾

### 账户相关

#### 密码

`win+x` - 设置 - 账户 - 登录选项 - 设置PIN和指纹登陆


### onedrive
### onedrive账号解冻方法
超过系统的免费额度，账号会被封禁，被封禁后，桌面端会无法登录，显示错误代码`0x8004def7`
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240814121753.png)


## conda



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




[conda 使用指南](https://blog.csdn.net/miracleoa/article/details/106115730)

!!! note " conda 和 pip 的区别"
    [Anaconda | Understanding Conda and Pip](https://www.anaconda.com/blog/understanding-conda-and-pip)

    ||conda|pip|
    |---|---|---|
    |manages|binaries|	wheel or source|
    |can require compilers|	no|	yes|
    |package types|	any	|Python-only|
    |create environment|yes, built-in|no, requires virtualenv or venv|
    |dependency checks|	yes|no|
    |package sources|Anaconda repo and cloud|PyPI|


### conda的环境变量配置
在安装目录下的`\Scripts`文件夹下

### pip

查看某个包所有的版本
```shell
pip index versions <package>
```

安装指定版本的包

```shell
pip install <package>==<version>
```

#### 使用命令行调用不同版本的python

在系统路径path（高级系统系统设置——环境变量）中加入python.exe所在目录（打开文件所在位置——属性——打开文件所在位置）（因为是快捷方式，所以需要先找到快捷方式所在目录，再找到原exe文件所在位置）

**注：应考虑到优先级的问题，将想要通过命令行直接进入的python版本所对应的路径放在上面**


### 使用

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

# 7. 卸载包
conda remove -n <package_name> --all
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


## Pytorch

### CUDA
!!! note "什么是CUDA"
    通俗地说，CUDA是一种协助“CPU任务分发+GPU并行处理”的编程模型/平台，用于加速GPU和CPU之间的计算。
    
    也就是说CUDA通过CPU任务分发和GPU并行处理的方式，把计算任务通过CPU分发给GPU进行并行计算加速。而GPU并行计算的能力需要CUDA借助其自带的编程接口和工具，比如C/C++语言来编写并行计算程序，并通过CUDA编译器将程序转化为可以在英NVIDIA GPU上执行的机器码快速运行。
                        
查看cuda支持版本，`win+R`输入`cmd`输入`nvidia-smi.exe`

下载地址[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829195225.png)

点击符合的版本选择下载，直接安装。注意安装路径要装在自己记得住的地方下，要预留好空间，最好不要装在C盘。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829195549.png)

**安装验证方法：**

1. cmd中输入`nvcc -V`，有信息说明成功
2. 安装路径下`\extras\demo_suite\deviceQuery.exe`，运行这个文件，有`PASS`说明成功（查询一下本机的gpu设备
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829200019.png)
3. 安装路径下`\extras\demo_suite\bandwidthTest.exe`，运行这个文件，有`PASS`说明成功
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829200006.png)

[Installation Guide Windows :: CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/archive/11.6.0/cuda-installation-guide-microsoft-windows/index.html#system-requirements)

### cuDNN安装
cuDNN是NVIDIA CUDA®深度神经网络库，用于GPU加速的深度神经网络。它提供了高度优化的实现，包括前向和反向卷积、池化层、归一化和激活层等标准例程

安装网站[cuDNN Archive | NVIDIA Developer](https://developer.nvidia.com/rdp/cudnn-archive)

找到符合自己上面CUDA安装版本的cuDNN版本，下载解压，将解压后的文件夹中的`bin`、`include`、`lib\x64`文件夹中的文件复制到CUDA的安装目录中对应的文件夹中。

注意这一步需要注册一下NVIDIA的账号


### Pytorch 安装


```shell title="查看CUDA版本"
nvidia-smi
```

```shell title="查看CUDA的版本"
nvcc -V
nvcc --version
```

装了python3.9，我的CUDA版本是10.2，在[Previous PyTorch Versions | PyTorch](https://pytorch.org/get-started/previous-versions/)这个网站上可以找到各个版本对应的下载链接

```shell title="CUDA=10.2"
pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu102/torch_stable.html
```

!!! failure "numpy报错"
    安装好torch之后，numpy会报错

    ```
    UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at  ..\torch\csrc\utils\tensor_numpy.cpp:68.)
    _dtype_to_storage = {data_type(0).dtype: data_type for data_type in _storages}
    ```

    **解决方法：** 将numpy版本降低为非>2.0.0的版本，之后就能成功导入了。
    ```shell
    pip uninstall numpy
    pip install numpy==1.26
    ```



```python title="测试是否可用"
import torch # 如果pytorch安装成功即可导入
print(torch.cuda.is_available()) # 查看CUDA是否可用
print(torch.cuda.device_count()) # 查看可用的CUDA数量
print(torch.version.cuda) # 查看CUDA的版本号
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240903112501.png)





## Pycharm

### 申请学生权限



语言设置为中文

setting-plugin-chinese





### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你Pycharm远程连接服务器端项目进行本地开发调试！...-CSDN博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)







## vscode
### 使用

- F1打开命令面板
- `ctrl + P` 搜索文件名打开文件
- `ctrl + F` 搜索内容
- 搜索工作区内容的快捷键是`Ctrl + Shift + F`，或者在菜单栏中选择 `查看 (View)` -> `搜索 (Search)`

### 插件
**markdown 插件 —— Markdown Preview Enhanced**

设置一个`picgo`的快捷键，我这里设置的是`ctrl + alt + P`

截图之后直接按就可以将图片上传到图床，并将连接复制到剪贴板

**vim插件 —— vim**


**copy as markdown**

[chorme下载地址](https://microsoftedge.microsoft.com/addons/detail/copy-as-markdown/cbbdkefgbfifiljnnklfhnhcnlmpglpd)

解决链接复制之后只有url没有标题的问题

### 安装

把vscode安装路径下的`bin\`文件夹添加到环境变量中，就可以实现命令行操作
- `code .` 打开当前文件夹
- `code filename` 打开文件

### PlatformIO
PlatformIO is a cross-platform, cross-architecture, multiple framework, professional tool for embedded systems engineers and for software developers who write applications for embedded products.


[VSCode 下 PlatformIO 的安装教程-CSDN博客](https://blog.csdn.net/qq_40018676/article/details/128680677)


## Mail
### 我使用的邮箱
- zju邮箱
- 126邮箱
- gmail
- qq邮箱
- outlook邮箱

### pop3

### IMAP


#### outlook 添加浙大邮箱
- “IMAP”则接收服务器： `imap.zju.edu.cn` 端口`143`，勾选SSL端口：993；
- “POP3”则接受服务器： `pop3.zju.edu.cn` 端口`110`，勾选SSL端口：995；
- 发送服务器都为：`smtp.zju.edu.cn` 端口：`25`，勾选SSL端口：994 。
- 在“登录信息”的“用户名”填写完整邮箱地址，如`test@zju.edu.cn`
- 密码处填写邮箱密码

#### 添加qq邮箱
在qq邮箱设置处开启IMAP/SMTP服务，需要绑定手机号，然后手机发验证短信
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240814123902.png)
发完验证短信后，会有一个授权码，这个授权码就是密码