# MacOS
## 基础
mac默认使用zsh


## 快捷键

- 空格预览文件
- 按住Comm
- and+空格，打开“聚焦“
- fn+backspace = del
- command+q 退出应用程序
- command + [ 返回上一级
- command + ] 前往下一级
- command + control + 空格 ： emoji
- shift + option + b：颜文字
- 使用声调打字：tab

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1851423987&bvid=BV1mW421w7Jw&cid=1457785582&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>

```shell title="open Finder in terminal"
open .
```


## 触控板
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1550039500&bvid=BV12y421e7t2&cid=1428208208&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=90% height=600px></iframe>

两指左滑 - 通知中心


## 文件管理

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1304948465&bvid=BV1XM4m1k7hg&cid=1556194945&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1905750778&bvid=BV1LS411N723&cid=1594491744&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=90% height=600px></iframe>
## 小技巧
同时重命名多个文件
- 拆字法打字


## 软件配置指南

鼠标反转： 自然滚动去掉

!!! info "可以在[macked](https://macked.app)这个网站上下载到一些破解的软件"
    有能力还是支持正版

### 软件已损坏？怎么解决

```shell title="信任开发者"
sudo spctl --master-disable
```

```shell title="放行picgo"
xattr -cr /Applications/xxx.app
```


### homebrew
首先需要配置好vpn

```shell title="安装homebrew"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```shell title="系统会跳出三个指令让你执行，类似于"
echo >> /Users/philfan/.zprofile
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/philfan/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

```shell title="验证安装"
brew help
```


### cli工具

```shell title="wget 安装"
brew install wget
```

### vscode

`ctl + ~` 打开终端:注意是英文状态下面


**Shift + Command + P** 打开设置，输入 `shell command` 找到`Shell Command: Install ‘code’ command in PATH`


### xcode

[Xcode on the Mac App Store](https://apps.apple.com/us/app/xcode/id497799835?mt=12)

```shell
xcode-select --install
```

显示 command line tools are already installed

### ssh

### git

### jenkins
[Jenkins](https://www.jenkins.io/)


```shell
brew install jenkins
```
### paragon： NTFS读写

在使用硬盘传数据的时候，老是报`错误代码 -50`，搜了一下才发现mac原生是不支持NTFS文件系统的

!!! info "什么是NTFS"
    NTFS（New Technology File System）是由微软开发的一种文件系统，最早在 Windows NT 操作系统中引入。它是 Windows 系统的默认文件系统，用于存储和检索硬盘上的数据。

官网地址

[Microsoft NTFS for Mac | Paragon Software](https://www.paragon-software.com/home/ntfs-mac/)


搜了一下发现希捷的官网有一个免费的版本

[Paragon 驱动程序 | Seagate 中国](https://www.seagate.com/cn/zh/support/software/paragon/)


### NVM

[nvm-sh/nvm](https://github.com/nvm-sh/nvm): Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions


```shell
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```

```shell
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" --no-use # This loads nvm, without auto-using the default version
```

```shell title="验证"
nvm -vx
```

### node

使用NVM进行管理

```shell
nvm install stable
```

```shell
npm install -g tldr
npm install -g typescript
npm install -g @vue/cli
npm install -g vuepress
npm install -g @angular/cli
npm install -g eslint
npm install -g gitbook-cli
npm install -g lodash
```

### creative cloud

201： 说明是网络问题

- PS
- AI
- Acrobat
- LR


### picgo
[Release 2.3.1 · Molunerfinn/PicGo](https://github.com/Molunerfinn/PicGo/releases/tag/v2.3.1)

下载之后进行dwg的安装，因为 PicGo 没有签名，所以会被 macOS 的安全检查所拦下,安装后会显示已经损坏，这个时候需要根据[PicGo/FAQ.md](https://github.com/Molunerfinn/PicGo/blob/dev/FAQ.md)中的方法进行操作

```shell title="信任开发者"
sudo spctl --master-disable
```

```shell title="放行picgo"
xattr -cr /Applications/PicGo.app
```

### docker

### typora

### jetbrains
ZJU有企业账号，在校网环境下面登陆


### wps
zju有企业账号，SSO登陆输入ZJU，验证登陆即可


### qq音乐歌单导入apple music

1. 获取 qq 音乐的歌单 id
2. 通过 id 获取歌单曲目
3. 通过 [Tune My Music](https://www.tunemymusic.com/zh-CN/transfer) 向 apple music 导入歌单曲目


> 参考文章：[将 QQ 音乐的歌单导入 apple music - 知乎](https://zhuanlan.zhihu.com/p/666443150)

### adobe系列

### bandzip

[Bandizip (Mac) - 如何在Mac上更改默认应用程序](https://www.bandisoft.com/bandizip.mac/howto/default-app-changer/)

```shell title="设置为访达扩展"
pluginkit -e "use" -i "com.bandisoft.mac.bandizip.findersyncextension"
```


## 效率工具

### icloud 软件 + icloud书签实现edge和safari的同步

rt，在windows上下载[icloud](icloud.en.uptodown.com/windows/download)软件，安装后登录icloud账号，再在edge上下载[icloud书签](https://microsoftedge.microsoft.com/addons/detail/icloud-%E4%B9%A6%E7%AD%BE/lbfbbhdljlmhnpbcdcajkdanonpgbhlh)插件，安装后登录icloud账号，即可实现edge和safari的同步

### Aifred：better 聚焦

[Mac效率神器Alfred系列教程---Alfred概述 - 知乎](https://zhuanlan.zhihu.com/p/33199992)

### Iterm2：更nb的终端
[iTerm2安装配置使用指南——保姆级 - 知乎](https://zhuanlan.zhihu.com/p/550022490)

设置启动热键

第一步：preference -> keys ->Create a Dedicated Hotkey Window
第二步骤：设置Hotkey，我设置和Linux差不多布局的command（Ctrl+Alt+T）



```shell title="oh my zsh"
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```


```shell title="声明高亮插件zsh-syntax-highlighting"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

```shell
#编辑配置文件
vim ~/.zshrc

#在最后一行增加下面的代码
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 

#退出编辑后执行使配置生效
source ~/.zshrc 
```

### spectacle： 窗口移动

[Carthage/Carthage: A simple, decentralized dependency manager for Cocoa](https://github.com/Carthage/Carthage?tab=readme-ov-file#installing-carthage)

```shell
brew install carthage
```

[spectacle](https://github.com/eczarny/spectacle/releases/tag/1.2)

下载release即可，需要安装一个环境，按步骤来即可


### Vanilla： 隐藏菜单栏


按住 Command 键同时拖动应用图标 进入相应区域，就完成了对应用图标的隐藏 / 显示设置，这要比 Bartender 便捷高效许多。

[Vanilla，精简 Mac 菜单栏应用图标，小巧轻量还免费丨App+1 - 少数派](https://sspai.com/post/39036)

### [Scroll Reverser ](https://pilotmoon.com/scrollreverser/) 调整滚轮方向

### Open in Terminal： finder打开终端

[OpenInTerminal/Resources/README-Config.md at master · Ji4n1ng/OpenInTerminal](https://github.com/Ji4n1ng/OpenInTerminal/blob/master/Resources/README-Config.md)

```shell title="输入这个指令，查找插件的uid"
pluginkit -mAD -p com.apple.FinderSync -vvv
```

```shell title="把-u 后边的参数换成你显示的uid即可"
pluginkit -e "use" -u "C21A713E-0EED-4E97-8DB2-5B9EA96A1F28"
```

需要在访达上面自定义工具栏，然后添加open in terminal

在软件里面也可以设置快捷键打开

## safari 使用指南


## latex


```shell
brew install mactex --cask
```

等着就完事了


## Apple Script

- 系统自带的“脚本编辑器”
- vscode中`code runner`插件

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=887179224&bvid=BV1NK4y1T7wA&cid=311009872&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>

> 参考资料
> [AppleScript 入门：探索 macOS 自动化 - 少数派](https://sspai.com/post/46912)
> [kevin-funderburg/AppleScripts: My collection of AppleScripts I've developed or acquired over the years.](https://github.com/kevin-funderburg/AppleScripts)

## conda 环境

[Miniconda — Anaconda documentation](https://docs.anaconda.com/miniconda/)
[miniconda下载 m1/m2](https://repo.anaconda.com/minpiconda/Miniconda3-latest-MacOSX-arm64.sh)
[MAC OS m2安装和卸载miniconda - 知乎](https://zhuanlan.zhihu.com/p/619566718)
安装
```shell
# 文件名是自己下载的sh文件，-p后面填安装路径
# -b 表示将环境变量自动写入到～/.bash文件中
sh Miniconda3-latest-MacOSX-arm64.sh -b -p ~/miniconda3
```

前往安装地址，打开终端
```shell
source /bin/activate
```

执行
```shell
conda init zsh #zsh执行这个命令
或者
conda init bash #bash执行这个命令
```


```shell title="加入路径"
vim ~/.zshrc
export PATH=/yourpath/anaconda3/bin:$PATH
source ~/.zshrc
```
注意：上面的”/yourpath”要替换成你自己的Anaconda安装目录。
按esc退出编辑模式，保存文件并退出（输入”:wq”回车）

### 换conda源

=== "THU"
    ```shell
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/fastai/
    conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
    conda config --append channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
    
    # 搜索时显示通道地址
    conda config --set show_channel_urls yes
    ```

=== "ustc源"
    ```shell
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
    conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
    
    conda config --set show_channel_urls yes
    ```
### 换pip源
解决方案：将配置好国内源的`pip.conf`文件, 放在 `~/Library/Application Support/pip` 中。

可能有的新用户发现自己的文件夹中没有pip文件夹，不慌，新建就行！

```shell
command + 空格            #  打开聚焦搜索
输入 ~/Library/Application Support       # 找到Application Support文件夹
```


在`Application Support`这个文件夹里面建一个pip 文件夹;
在新建的pip文件夹下建一个`pip.conf`文件。

在`pip.conf`文件中输入以下内容，保存并退出。
```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
```

### 卸载

（1）使用 Anaconda-Clean 包删除所有与 conda 相关的文件和目录
```shell
conda activate your_conda_env_name
conda install anaconda-clean
anaconda-clean # add `--yes` to avoid being prompted to delete each one

#注：如果这一步之行不成功，可以直接跳过
```

（2） 删除整个目录（直接删掉安装文件就可）
```shell
rm -rf ~/miniconda3
```

（3） 删除将 conda 路径添加到PATH环境变量的行（或者注释掉）

注：其实只之行第二步就可，后边这两步为了再次安装时，环境冲突，所以删干净
```shell
vi ~/.bashrc
# -> Search for conda and delete the lines containing it
# -> If you're not sure if the line belongs to conda, comment it instead of deleting it just to be safe
source ~/.bashrc
```
```shell
vi ~/.zshrc
# -> Search for conda and delete the lines containing it
# -> If you're not sure if the line belongs to conda, comment it instead of deleting it just to be safe
source ~/.zshrc
```

（4） 删除配置文件
```shell
rm -rf ~/.condarc
#注：自己找一下~/.conda 开头的文件，删掉
```


### vscode 的python环境
安装插件
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240919133706.png)

F1 -> Python: Select Interpreter -> 选择你的环境

或者右下角有个环境选择，右键把选择编辑器勾上


