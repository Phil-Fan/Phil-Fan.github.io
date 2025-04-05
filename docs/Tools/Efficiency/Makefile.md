# Makefile


## 环境安装

### windows下
[Index of /gnu/make](https://ftp.gnu.org/gnu/make/)

下载最新版的安装包，然后解压

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250306141532912.png)

命令行进入到make的安装文件夹下，需要先有安装mingw-w64，然后在命令行中执行：

```shell
build_w32.bat gcc
```

会生成一个文件名为`gnumake.exe`，位于当前目录下的`GccRel`文件夹。

环境变量添加GccRel文件夹即可

## Makefile


## CMake