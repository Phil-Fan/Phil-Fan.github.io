# 文件

## 打开文件

```py
fileobj = open(filename,mode)
```

- `fileobj`是`open()`返回的文件对象
- `filename`是该文件的文件名
- `mode`是指明文件类型和操作的字符串
  - `mode`的第一个字母表明对其的操作
  - `mode`的第二个字母是文件类型：
    - `t`（可省略）代表文本类型文件
    - `b`代表二进制类型文件

| 文件打开模式 | 含义                                              |
| ------------ | ------------------------------------------------- |
| `"r"`        | read只读模式(默认)                                |
| `"w"`        | write覆盖写模式(不存在则新创建；存在则重写新内容) |
| `"a"`        | append追加模式(不存在则新创建；存在则只追加内容)  |
| `"x"`        | create创建写模式(不存在则新创建；存在则出错)      |
| `"+"`        | 与 r/w/a/x 一起使用，增加读写功能                 |
| `"t"`        | 文本类型                                          |
| `"b"`        | 二进制类型                                        |

## 文件读写函数

```py
## 文件迭代器
f = open("1.txt","r")
for i in f:
	XXXX
```



| 名称                  | 含义                                                         |
| --------------------- | ------------------------------------------------------------ |
| `open()`              | 打开文件                                                     |
| `read(size)`          | 从文件读取长度为size的字符串，如果未给定或为负则读取所有内容 |
| `readline()`          | 读取整行，返回字符串                                         |
| `readlines()`         | 读取所有行并返回列表                                         |
| `write(s)`            | 把字符串s的内容写入文件                                      |
| `writelines(s)`       | 向文件写入一个元素为字符串的列表，如果需要换行则要自己加入每行的换行符 |
| `seek(off, whence=0)` | 设置文件当前位置                                             |
| `tell()`              | 返回文件读写的当前位置                                       |
| `close()`             | 关闭文件。关闭后文件不能再进行读写操作                       |

## 文字编码

- ANSI编码：
  - Windows常用的编码
- UTF-8编码：
  - UTF-8 是缺省编码格式
- 中文编码：
  - GB2312，GBK
- Windows可在cmd下用`chcp`命令查看
- 默认会以本地编码打开文件
- 打开编码为GBK的文件： `open(<文件名>，<模式>，encoding='GBK')`

## 重定向

- `sys.stdin` 标准输入
- `sys.stdout` 标准输出
- `sys.stderr` 标准错误输出

```py
import sys
s=sys.stdin.readlines() #从文件读入变为从键盘输入 
print(s)
```

## 文件与异常

```py
try:
    f = open('xxx')
except:
    print('fail to open')
finally:
    f.close()
```

- with 方法

```py
with open("１.txt") as file:
    data = file.read()
    
With open('1.txt') as f1, open('2.txt') as  f2:
    do something
```

- 紧跟`with`后面的表达式被求值后，将调用返回对象的`__enter__()`，然后将函数的返回值赋值给`as`后面的变量
- 当`with`后面的代码块全部被执行完之后，将调用前面返回对象的`__exit__()`方法


