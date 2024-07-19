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




## bug

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


## 读取溢出漏洞

## 代码注入




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


rbp : base pointer，指向栈底（最高）
rsp: stack pointer，指向栈顶（最低）

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