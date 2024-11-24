# Windows 备忘录
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
- 其他：[logi option+](https://www.logitech.com/zh-cn/setup/ergosetup/logi-options.html),[Download WizTree](https://www.diskanalyzer.com/download)

- 卸载工具[Geek Uninstaller - Download](https://geekuninstaller.com/download)
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

### wget
[GNU Wget 1.21.4 for Windows](https://eternallybored.org/misc/wget/)

放在`c:/Windows/System32`文件夹下

### nc (netcat)
[netcat 1.11 for Win32/Win64](https://eternallybored.org/misc/netcat/)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241118214327.png)

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
[词库转换工具下载 imewlconverter](https://github.com/studyzy/imewlconverter/releases/tag/v3.1.1)


[词库搜索-搜狗输入法词库](https://pinyin.sogou.com/dict/search/)

[打造最强「Windows 10」微软拼音输入法 + 600万词库下载 - 小羿](https://xiaoyi.vc/win10-pinyin-diy.html)


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


### onedrive账号解冻方法
超过系统的免费额度，账号会被封禁，被封禁后，桌面端会无法登录，显示错误代码`0x8004def7`
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240814121753.png)


### C盘爆了



#### c盘扩容（开源）
[DiskGenius – 正式版下载|免费下载](https://www.diskgenius.cn/download.php)


[Diskgenius分区把c盘扩大操作方法-百度经验](https://jingyan.baidu.com/article/f7ff0bfc2b07076f26bb13bb.html)

#### 删除无用文件（节流）
- 依次点击：此电脑，右键C盘，属性，清理磁盘，清理系统文件（有时候电脑更新了，旧的安装包不会自动删除，就可能占用十几G）；
- 清空回收站
- **geek卸载软件** 下载geek（[Geek Uninstaller - Download](https://geekuninstaller.com/download)
），找到不用的软件，删除卸载，它能很干净得删除软件，包括所有有关文件夹和注册表，very nice，强推，注意：geek会删除该软件的所有文件夹，如果个人文件保存在这些文件夹里面，需要提前转移，否则将造成资料丢失！！；
- **ccleaner** 下载ccleaner（认准官网，免费版就行），里面的清理注册表，扫描，修复，再扫描，修复，再扫描，修复，重复三次（无须备份）；然后自定义清理，运行清理程序（注意，该操作会导致你在浏览器里面登入的如哔哩哔哩账号这种，会给你下线从而需要重新登入，为了避免，可以仔细看看自定义清理里面勾选了哪些，然后选择性清理就行）；geek卸载不了的软件如VS，SW等，用cc卸载；
- 找到**电脑管家**（无论是啥都行），找到里面的清理垃圾功能，扫描，清理；如果有系统修复啥的，漏洞修复啥的，全部来一遍；
- 下载**treesize**（一定要认准免费版，下载过程中会多次引诱你下载专业版，不要上当，下载的时候看仔细），每次用管理员身份运行，一个一个目录点开看看，是哪个文件夹占了空间，不知道是什么的就去百度一遍看看是什么，怎么删；

!!! note "常见占用内存"
    - wechat 聊天记录及缓存文件及下载的文件
    - 飞书缓存文件
    - conda库文件


#### 移动各种文件（找补）

**移动系统文件夹**

移动桌面、文档、下载等文件夹到其他盘

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240923144021.png)

**移动`.vscode`**


- `ctrl + x `选择以管理员身份运行 cmd
- 剪切原文件`.vscode`到`D:\.`vscode文件夹。
```shell
cmd /c mklink /D "%USERPROFILE%\.vscode" "D:\.vscode\"
```
[vscode修改默认扩展和用户文件夹目录到D盘\_.vscode文件怎么换盘-CSDN博客](https://blog.csdn.net/sg_knight/article/details/130258619)


**移动`TEMP`和`TMP`文件夹**

把`TEMP`和`TMP`文件夹移动到其他盘


**移动大软件**

找到电脑设置、系统、存储，去里面查看C盘安装了哪些大软件，用geek卸载了安装到其他盘。


## 终端 & Powershell

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

### 修改、查看、清除文件信息
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115001953.png)

有时候想要修改文件信息，但是GUI界面没有这样的操作

打开终端界面

[Get-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/get-itemproperty?view=powershell-5.1)
```shell title="查看文件信息"
Get-ItemProperty -Path <path> -Name <property_name>

Get-ItemProperty -Path <path> | Format-List * -Force
```

[Set-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/Set-ItemProperty?view=powershell-5.1)

```shell title="修改文件信息"
Set-ItemProperty -Path <path> -Name <property_name> -Value <value>
```
- `CreationTime` 创建时间
- `LastWriteTime` 最后修改时间
- `LastAccessTime` 最后访问时间

[Remove-ItemProperty](https://learn.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Management/remove-itemproperty?view=powershell-5.1)

```shell title="清除文件信息"
Clear-ItemProperty -Path <path> -Name <property_name>
```

## cursor

[Cursor - The AI Code Editor](https://www.cursor.com/)





[【前端必读】二、使用 Cursor 的基本功能全教程（快捷键及其他功能）\_cursor快捷键-CSDN博客](https://blog.csdn.net/zhouzongxin94/article/details/142550632)


## vscode
### 使用

- F1打开命令面板
- `ctrl + P` 搜索文件名打开文件
- `ctrl + F` 搜索内容
- 搜索工作区内容的快捷键是`Ctrl + Shift + F`，或者在菜单栏中选择 `查看 (View)` -> `搜索 (Search)`



### 卸载

[Windows下彻底删除VSCode\_vscode注册表怎么删除-CSDN博客](https://blog.csdn.net/Zhangguohao666/article/details/105667095)

### 内存占用过大问题

1. 找到文件-首选项-设置：禁用自动保存
2. 找到文件-首选项-设置，搜索`git.enabled`,禁用git
3. 禁用`search.followSymlinks`：控制是否在搜索中跟踪符号链接
4. 按`f1`，输入`developer: open process explorer`，会打开一个任务管理器一样的窗口，查看里面cpu和内存占用最高的进程，然后一个个禁用你的扩展插件，直到cpu和内存占用正常，这样就可以找出耗内存的扩展然后按照你的开发需求更换或者禁用


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

## c环境
[MSVC、MINGW，gcc、g++，qmake、cmake的联系和区别是什么？ - 知乎](https://www.zhihu.com/question/333560253)


### MinGW安装
[Download MinGW - Minimalist GNU for Windows](https://sourceforge.net/projects/mingw/files/latest/download)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241010103943.png)


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241010104231.png)

勾选base 和 g++两个，然后点击左上角的Installation，选择Apply Changes

设置path环境变量，将`....\MinGW\bin`添加到path中

验证安装
```shell
gcc -v
g++ -v

```
> [参考博客:MinGW下载安装教程 傻瓜式操作](https://blog.csdn.net/qq_38196449/article/details/136125995)


### vscode 环境

[VS Code 配置 C/C++ 编程运行环境](https://blog.csdn.net/qq_42417071/article/details/137438374)


安装c/c++插件：
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241010110358.png)




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



## 模拟器

### 雷电模拟器
[雷电安卓模拟器-手游模拟器安卓版\_android手机模拟器电脑版\_雷电模拟器官网](https://www.ldmnq.com/)

可以使用设置墨墨背单词


## ZJU
### 智云课堂
对于录播视频，这就很简单粗暴了，直接找到div class = `cmc-base cmc-video`行并展开，下面有一个`https://vod.cmc.zju.edu.cn/`开头网址


[智云课堂加载不出来解决办法 - CC98论坛](https://www.cc98.org/topic/5902398)


## VLC
将VLC目录加入系统环境变量Path


**快捷键**

`[`减慢速度；`]`加快速度

```shell
vlc <address>
vlc -f <address> # 全屏播放
vlc --rate <speed> <address> # 倍速播放
```


[vlc的命令行使用方式\_vlc用控制台播放音频-CSDN博客](https://blog.csdn.net/fengmm521/article/details/79596447)


https://interactivemeta.cmc.zju.edu.cn/#/studentsrs?course_id=63546&sub_id=1393805&tenant_code=112

https://interactivemeta.cmc.zju.edu.cn/#/replay?course_id=63546&sub_id=1301338&tenant_code=112

course_id 是课程id
sub_id 是章节id
tenant_code 是租户id

sub_id  貌似是根据一定规则进行生成的，不清楚后台的hash算法

但观察发现，有连续


查询`https://classroom.zju.edu.cn/courseapi/v3/multi-search/get-course-detail?course_id=67855&student=<student_id>`即可获得课程详细信息

