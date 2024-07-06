# PWN
## 简介

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

[WebsocketReflectorX](https://github.com/XDSEC/WebSocketReflectorX/releases)
下载appimage拖动到虚拟机中即可使用

- 下载安装打开后在链接框内填入 wss:// 链接地址
- “连接情况”页面会给出一个 `127.0.0.1:<port>` 的结果
- 在命令行通过你熟悉的 `nc 127.0.0.1 <port>` 进行连接即可




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

!!! bug "b"是什么意思""

学一下汇编把lab0那个题做掉


通过 pwntools 进行编程
```
from pwn import *
context.log_level = 'debug'
context.arch = 'amd64'
p = process('./login_me)
p.recv()
p.sendline
```


## 代码注入

### 命令注入
直接注入

### shell code 注入
- 间接
- 搭配控制流劫持的利用方式

栈的增长是高地址向低地址溢出
- 每一次push都会减小栈指针，把值存进去
