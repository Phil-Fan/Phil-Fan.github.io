# PWN
## 简介
!!! note "PWN"
  PWN = Find the Bugs + Exploit them
  
  - 阅读源代码，找到程序的漏洞
  - 本地运行并触发该 bug
  - 与远端交互、触发 bug 并获取 flag

- 赛题文件
    - 往往需要逆向
    - 漏洞描述 (diff)
- 赛题环境
  - libc and ld
  - Dockerfile
  - "good challenge should issue everything you needed to run and test it"
- 赛题远程
  - 快速将命令行文本程序搭建为 TCP 服务（别在 host 上直接跑服务）

## 环境准备
### WebsocketReflectorX
[WebsocketReflectorX](https://github.com/XDSEC/WebSocketReflectorX/releases)
下载appimage拖动到虚拟机中即可使用

- 下载安装打开后在链接框内填入 wss:// 链接地址
- “连接情况”页面会给出一个 `127.0.0.1:<port>` 的结果
- 在命令行通过你熟悉的 `nc 127.0.0.1 <port>` 进行连接即可

!!! note "注意`ip` & `port`之间是空格，不是冒号！！！"


### websocat
[Release v1.13.0 · vi/websocat](https://github.com/vi/websocat/releases/tag/v1.13.0)


[websocat.aarch64-unknown-linux-musl下载链接](https://github.com/vi/websocat/releases/download/v1.13.0/websocat.aarch64-unknown-linux-musl)

使用 websocat 程序直接通过 CLI 连接

安装后直接在命令行输入 websocat -b wss://... 即可进行交互


LD_PRELOAD=./libc.so.6 ./ld-linux-x86-64.so.2 ./login_me

## 基础知识
### 数据类型



### 做题流程
- 使用checksec检查ELF文件保护开启的状态
- IDApro逆向分析程序漏洞（逻辑复杂的可以使用动态调试）
- 编写python的exp脚本进行攻击
  - （若攻击不成功）进行GDB动态调试，查找原因
  - （若攻击成功）获取flag，编写Writeup



### 常见错误
!!! note "it's hard to define a bug"




- **C/C++ language**:memory corruption bugs
- **Clear exploitation aim**: code execution
- **Naive program**: usually terminal program

prepare函数



```c
void prepare(){
    setvbuf(stdin,0LL,2,0LL);
    setvbuf(stdout,0LL,2,0LL);
    alerm(60);
}
```

## pwntools 包

[关于 pwntools — pwntools 3.12.0dev 文档](https://pwntools-docs-zh.readthedocs.io/zh-cn/dev/about.html)

[[Tools]Pwn中用于远程交互的库函数总结\_python pwn remote函数、-CSDN博客](https://blog.csdn.net/DARKNOTES/article/details/124282024)


通过 pwntools 进行编程
```bash
pip install --upgrade pwntools
```

可以下载ipython包
```bash
pip install ipython
```

```python
from pwn import *
context.log_level = 'debug' # 输出调试信息
context.arch = 'amd64' # 指定架构
```

### 连接
```python
p = process('./login_me) #运行本地程序
p.close()# 关闭进程

# 指定libc进行访问,第一个是loader，第二个是libc的路径
p = process(['./ld-2.23.so','./test'], env = {'LD_PRELOAD' : './libc-2.23.so'})


p = remote('ip',port, typ='协议\协议簇') # 运行远端程序
```

另外在[这个仓库](https://gist.github.com/frankli0324/795162a14be988a01e0efa0531f7ac5a)中，作者给出了websocket的连接方式

```bash
pip3 install pwntools-tube-websocket
```


```python title="usage.py"
from pwn import *
from wstube import websocket

a = websocket('wss://echo.websocket.events')
print(a.recv())
for i in range(3):
    a.send(b'test')
    print(a.recv(2))
    print(a.recv(2))
a.sendline(b'test')
print(a.recv())
a.send(b'12345asdfg')
print(a.recvregex(b'[0-9]{5}'))
print(a.recv())
a.close()
```




### 远程侦听
```python
client = listen(port).wait_for_connection()
```

### 创建交互Shell
```python
host.interactive()
# 当然，你也可以与本地的shell连接
sh = process('/bin/sh')
sh.interactive()
```



### 收信息
```python
p.recv()
username = b"user"
p.recv()
#  接收n字节数据,一定时间后超时
bytes = host.recv(n, timeout = default)
# 换行结束接收,keepends=False不保留结尾的\n
bytes = host.recvline(keepends=True)
# 接收直至分隔符delim
bytes = host.recvuntil(delim,drop=Fasle)
# 接收模式匹配的字符串
bytes = host.recvregex(pattern)
# 接收直到超时或EOF
bytes = host.recvrepeat(timeout = default)
# 接收数据直到EOF
bytes = host.recvall() 
# 清空缓冲区未接收的数据
host.clean()
```


### 发送信息
```python
# 发送一段数据
host.send(bytes)
# 发送数据加一个换行
host.sendline(bytes)
host.sendafter(b"Receive:",b"Send:")
```

### ssh连接
```python
# 创建连接
shell = ssh(host='ip', user='root', port=port, password=password)
# 可以在该SSH连接开启进程
s = ssh(host='example.pwnme')
sh = s.process('/bin/sh', env={'PS1':''})
sh.sendline(b'echo Hello; exit')
sh.recvall() # 或者sh.recvline()
输出：b'Hello\n'
```

### 汇编器
```python
code = asm('mov eax, 0')
```

pwntools 的 shellcraft包
[pwnlib.shellcraft — Shellcode generation — pwntools 4.12.0 documentation](https://docs.pwntools.com/en/stable/shellcraft.html)

### 常见错误

```
BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
```

查看链接网址后提示在**每个字符串前面加上b**即不会出现错误警告

python3有八个字节的byte，所以它每次都会报这样的错误：




## 读取溢出漏洞

## 代码注入

[智云链接](https://interactivemeta.cmc.zju.edu.cn/#/replay?course_id=63047&sub_id=1213370&tenant_code=112)


### 命令注入
直接注入，类似于sql注入
利用shell的语法特性，通过注入命令来执行代码

比如说



### shell code 注入

[Shellcodes database for study cases](https://shell-storm.org/shellcode/index.html)

`mmap`linux的一个系统调用，从真实内存映射一块虚拟内存区域，返回一个指向该区域的指针。

!!! note "间接调用是比较危险的"
    直接调用类似于`call puts`直接指向puts的地址

    间接调用`call rcx`，调用的地址放在rcx寄存器中，容易被劫持


- 间接
- 搭配控制流劫持的利用方式


## 栈上的缓冲区溢出

栈是先进后出的列表，栈的增长是**高地址向低地址**溢出。作用是用来放每个函数独立于自己的临时变量，然后起到一个作用域的约束作用。
- 需要两个指针：栈指针SP，stack pointer；栈帧指针，frame pointer。
- 提供两个元语：push & pop
- 每一次push都会减小栈指针，把值存进去

??? note "寄存器"
=== "数据寄存器"
  数据寄存器主要用来保存操作数和运算结果等信息，从而节省读取操作数所需占用总线和访问存储器的时间。`RAX`、`RBX`、`RCX`、`RDX`和`EAX`、`EBX`、`ECX`、`EDX`以及`AX`、`BX`、`CX`、`DX`分别称为64位、32位、16位数据寄存器(通用寄存器)。

=== "变址寄存器"
  变址寄存器主要用于存放存储单元在段内的偏移量，用它们可实现多种存储器操作数的寻址方式，为以不同的地址形式访问存储单元提供方便。<br>
  变址寄存器不可分割成8位寄存器。作为通用寄存器，也可存储算术逻辑运算的操作数和运算结果。变址寄存器它们可作一般的存储器指针使用。在字符串操作指令的执行过程中，对它们有特定的要求，而且还具有特殊的功能。<br>
  寄存器RSI、RDI和ESI、EDI和SI、DI分别称为64位、32位、16位变址寄存器(Index Register)。

=== "指针寄存器"
  指针寄存器主要用于存放堆栈内存储单元的偏移量，用它们可实现多种存储器操作数的寻址方式，为以不同的地址形式访问存储单元提供方便。<br>
  指针寄存器不可分割成8位寄存器。作为通用寄存器，也可存储算术逻辑运算的操作数和运算结果。
  寄存器`RBP`、`RSP`和`EBP`、`ESP`和BP、SP称分别为64位、32位、16位指针寄存器(PointerRegister)。

指令寄存器它们主要用于访问堆栈内的存储单元，并且规定：

（1）BP为基指针(BasePointer)寄存器，用它可直接存取堆栈中的数据；
（2）SP为堆栈指针(StackPointer)寄存器，用它只可访问栈顶。


rbp : base pointer，指向栈底（最高）
rsp: stack pointer，指向栈顶（最低）

> 栈就像叠盘子，最先放的盘子最后取出来

### 函数的传参过程
> [汇编角度深刻理解函数调用](https://www.bilibili.com/video/BV1RS4y1B75v)
>
> [画草图 + gdb + C语言 + 汇编语言 带你理解 栈帧 ！！！！](https://www.bilibili.com/video/BV1kG4y1R7K)
>
> [CPU眼里的：{函数括号} | 栈帧 | 堆栈 | 栈变量](https://www.bilibili.com/video/BV1FY411J7s7)


函数的参数传递：从右向左
出栈的顺序，从左向右

栈帧为了区别不同函数，栈的地址本质还是连在一起的

1. 保存上一个函数的栈帧指针
2. 从右向左传参

```asm
push rbp ; 将原来rbp的地址入栈
mov rbp, rsp ; 这个时候rbp=rsp
```

创建局部变量，rsp增加

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240720010617.png)

!!! note "局部变量为什么要初始化"
    创建局部变量的时候就是基于栈的，如果不进行初始化，那么这个变量还是原来这个内存地址上的值，是不确定的。

- 溢出破坏局部变量
- 溢出破坏存储的栈帧指针
- 溢出破坏存储的返回地址

保护方法：每次进入栈的时候，放一个随机变量，出栈的时候检测随机变量是否被修改（这种方法可以通过维护特定位置为常量进行绕过）

保护方法：使用两个栈，一个维护危险的变量；

可以劫持函数的返回地址，实现在函数间的任意跳转


https://classroom.zju.edu.cn/livingroom?course_id=54544&sub_id=1011516&tenant_code=112

[CTF PWN练习之返回地址覆盖 - FreeBuf网络安全行业门户](https://www.freebuf.com/articles/network/267051.html)

[pwn lab 2: ROP / FSB - CTF101-Labs-2024](https://courses.zjusec.com/topic/pwn-lab2/#task-1-20)

[pwn lab 3: glibc heap exploitation - CTF101-Labs-2024](https://courses.zjusec.com/topic/pwn-lab3/)



!!! example "以`login_me`为例题"
```shell
gdb ./login_me
start
p main
```

```shell
gef➤  p main
$2 = {int (int, char **)} 0x555555555647 <main>
```
所以在 `0x555555555647`下断点

```shell
b *0x555555555647
``` 

```
0x55555555564b <main+0004>      push   rbp
0x55555555564c <main+0005>      mov    rbp, rsp
0x55555555564f <main+0008>      add    rsp, 0xffffffffffffff80
```

第一步是保护rbp，第二步是保护rsp，第三步是创建一个0x80大的临时变量空间；
> 所以这样看的话 rbp-0x70和rsp+0x10是指向同一个地址

先`pop rbp`会把当前的rbp位置返回给rsp指针，实现栈的抬升

ret的时候，先把`old rbp`返给`rbp`
并把ret地址返回给运行PC

!!! tip "实现保护的一个方法"
  在`ret address`和`old rbp`之前加入一个随机值，每次出入栈时候，检查随机值是否有变化


shallow stack: 用微型的buffer存储，临时变量在另一个栈上面，怎么也不会溢出了


### PIE保护

!!! note "Check PIE"
    通过`checksec`命令来检查