# MacOS 备忘录
## 基础
mac默认使用zsh


## 快捷键

- 空格预览文件
- 按住Command+空格，打开“聚焦“
- fn+backspace = del
- 

## 小技巧
同时重命名多个文件
- 拆字法打字


## 软件配置指南

鼠标反转： 自然滚动去掉

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

## 效率工具
### Aifred：better 聚焦

[Mac效率神器Alfred系列教程---Alfred概述 - 知乎](https://zhuanlan.zhihu.com/p/33199992)

### Iterm2：更nb的终端
[iTerm2安装配置使用指南——保姆级 - 知乎](https://zhuanlan.zhihu.com/p/550022490)


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




## latex


```shell
brew install mactex --cask
```

等着就完事了


## conda 环境

[Miniconda — Anaconda documentation](https://docs.anaconda.com/miniconda/)
[miniconda下载 m1/m2](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh)
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


