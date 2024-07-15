# gdb
[【Linux】GDB保姆级调试指南（什么是GDB？GDB如何使用？）\_linux gdb标准输入-CSDN博客](https://blog.csdn.net/weixin_45031801/article/details/134399664)


## 原理
### 调试模式
○ 调试器执行模式
○ attach 模式
○ remote 模式



## gdb 插件
[hugsy/gef: GEF (GDB Enhanced Features)](https://github.com/hugsy/gef)
[gdb exhanced features(GEF)工具的使用](https://www.cnblogs.com/liulianzhen99/articles/17824258.html)

```shell
# 安装
git clone https://github.com/hugsy/gef
cp gef/gef.py ~/.gdbinit-gef.py
echo source ~/.gdbinit-gef.py >> ~/.gdbinit
# 调用gef，直接通过gdb命令就会默认加载gef插件
gdb
# 就会出现带gef>的界面了
gef➤
```
## 使用方法

○ 执行断点
○ 硬件断点
○ 查看寄存器 / 内存
○ set 修改寄存器 / 内存

```shell
run
start 在main之前临时断点

continue

step / s #单步

info register
info proc mapping

disassemble main/ disass main #反汇编

breakpoint *0x4005a0 #断点
b *0x4005a0
```

### 快捷指令
enter 重复指令
### 断点
b(breakpoint) + 行号 —— 在那一行打断点

b 源文件：函数名 —— 在该函数的第一行打上断点

b 源文件：行号 —— 在该源文件中的这行加上一个断点吧

d(delete) + 当前要删除断点的编号 —— 删除一个断点【不可以d + 行号】

若当前没有跳出过gdb，则断点的编号会持续累加

d + breakpoints —— 删除所有的断点

disable b(breakpoints) —— 使所有断点无效【默认缺省】

enable b(breakpoints) —— 使所有断点有效【默认缺省】

disable b(breakpoint) + 编号 —— 使一个断点无效【禁用断点】

enable b(breakpoint) + 编号 —— 使一个断点有效【开启断点】

相当于VS中的空断点

enable breakpount —— 使一个断点有效【开启断电】


### 查看类
l(list) 行号/函数名 —— 显示对应的code，每次10行

info b —— 查看断点的信息
breakpoint already hit 1 time【此断点被命中一次】

bt —— 看到底层函数调用的过程【函数压栈】

p(print) 变量名 —— 打印变量值

display —— 跟踪查看一个变量，每次停下来都显示它的值【变量/结构体…】

undisplay + 变量名编号 —— 取消对先前设置的那些变量的跟踪

### 运行类
r(run) —— F5【无断点直接运行、有断点从第一个断点处开始运行】

n(next) —— 逐过程【相当于F10，为了查找是哪个函数出错了】

s(step) —— 逐语句【相当于F11，】


set var —— 修改变量的值

until + 行号 —— 进行指定位置跳转，执行完区间代码

finish —— 在一个函数内部，执行到当前函数返回，然后停下来等待命令

c(continue) —— 从一个断点处，直接运行至下一个断点处【VS下不断按F5】

### 编程







