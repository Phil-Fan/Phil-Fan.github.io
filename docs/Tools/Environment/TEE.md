# 可信执行环境 TEE

可信计算（Trusted Computing）是一项旨在提高计算机系统和网络安全性的重要技术架构。其核心目标是通过在硬件层面建立一个信任根（Root of Trust）并由此扩展出一套安全策略，确保数据的完整性和行为的预期性，保护系统不受恶意软件和攻击者的威胁。其中，可信执行环境（Trusted Execution Environment, TEE）是可信计算的一个重要组成部分，广泛应用于金融服务、物联网安全、云计算、数字版权保护、身份认证和区块链等实际业务场景。


## 环境配置

我是在jetson orin NX上进行配置的，是arm的aarch64架构。

使用如下指令安装搭建时所需要的工具和库：
```cmd
apt install -y \
android-tools-adb \
android-tools-fastboot \
autoconf \
automake \
bc \
bison \
build-essential \
ccache \
cpio \
cscope \
curl \
device-tree-compiler \
expect \
flex \
ftp-upload \
gdisk \
git \
iasl \
libattr1-dev \
libcap-ng-dev \
libfdt-dev \
libftdi-dev \
libglib2.0-dev \
libgmp3-dev \
libhidapi-dev \
libmpc-dev \
libncurses5-dev \
libpixman-1-dev \
libslirp-dev \
libssl-dev \
libtool \
make \
mtools \
netcat \
ninja-build \
python-is-python3 \
python3-crypto \
python3-cryptography \
python3-pip \
python3-pyelftools \
python3-serial \
rsync \
unzip \
uuid-dev \
wget \
xdg-utils \
xterm \
xz-utils \
zlib1g-dev
```

```shell title="创建目录"
mkdir open-tee
cd open-tee
```

```shell title="安装repo"
apt install install repo

curl https://storage.googleapis.com/git-repo-downloads/repo > ./repo
```
这里不一定能下载下来，可以手动下载一下

```shell title="初始化"
repo init -u https://github.com/OP-TEE/manifest.git -m default.xml --repo-url=https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -b 4.7.0
```

```shell title="同步"
repo sync -j8
```

```shell
chmod +x build/br-ext/scripts/make_def_config.py
cd build
make -f toolchain.mk toolchains
```

> make: *** [toolchain.mk:141: /home/nesc/philfan_exp/open-tee/build/../toolchains/aarch64/.done] Error 126
> 报了Error 126：权限被拒绝，所以需要给权限


准备好toolchain和源代码后，开始编译工程，具体指令如下：
```cmd
make -f qemu.mk all
```


按如下指令启动qemu并运行OP-TEE：
```cmd
make run
```


## 遇到的问题与解决措施

```
rdate.c:(.text.rdate_main+0xd2): undefined reference to `stime'
date.c:(.text.date_main+0x1a8): undefined reference to `stime'
```

busybox在glibc 2.31版本后，修改了`stime`函数，所以需要按照其[busybox - BusyBox: The Swiss Army Knife of Embedded Linux](https://git.busybox.net/busybox/commit/?id=d3539be8f27b8cbfdfee460fe08299158f08bcd9)进行修改。

```
sudo apt install gcc-arm-linux-gnueabihf libc6-dev-armhf-cross

make mrproper
cd open-tee/build
make -f qemu.mk all
```


### 2
```
error: ‘%s’ directive output may be truncated writing up to 255 bytes into a region of size 246 [-Werror=format-truncation=]
cc1: all warnings being treated as errors
```
