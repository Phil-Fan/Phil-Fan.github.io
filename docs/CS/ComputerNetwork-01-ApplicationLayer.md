# 应用层 | Application Layer

交换应用报文

应用层协议最多

> Everything over IP

![image-20240129142527888](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129142527888.png)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129142544296.png" alt="image-20240129142544296" style="zoom:50%;" />



- 互联网杀手级应用

网络流量占用多且可以吸引用户

![img](https://static-cms.aa-cdn.net/wp-content/uploads/2019/12/Decade_Top_Apps_DL-1024x805.png)

![img](https://static-cms.aa-cdn.net/wp-content/uploads/2019/12/Decade_Top_Apps_Rev-1024x805.png)





## 原理

### 传输层服务模型

#### 标示 寻址

SAP

- 唯一的IP地址（主机是哪个）
- 采用的传输层协议 TCP/UDP
- 端口号 PortNumber（16bit 65536）

HTTP:80

Mail: TCP25

FTP: TCP2



#### 层间的信息

- 层间接口

报文SDU

谁发的：IP+port（TCP/UDP）

发给谁：IP+port

- 传输层实体对报文封装

源端口号，目标端口号，数据

IP交给下方





#### socket(IP:port)套接字

- TCP - `Transmission Control Protocol`

  四元组 我ip+port 对方ip+port

记忆了一个会话关系，不必要每次都有

建立了一个socket的映射

> 经常和朋友寄件，只要知道你经常寄的信息（socket）的代码，顺丰就可以直接寄走

- UDP - `User Datagram Protocol`

  二元组 本地ip+port

使得穿过层间的信息量最少

UDP套接字指定了应用所在的端结点（end point）

发送报文必须指定对方的ip+port

> 不经常寄件，需要提供自己的地址和对方的地址



如何使用

### 网络应用体系架构

#### Client-Server

服务器在固定端口一直运行，固定ip

服务器是中心，资源在服务器

可扩展性较差，CS模式断崖式下降



#### Peer-to-Peer

迅雷

又可以充当服务器，又可以充当用户

请求节点增加的同时，提供服务的节点也在增加



管理困难的多

#### 混合式

Napster

P2P分发mp3音乐



即时通信，服务器相当于做一个指挥



### 衡量指标

- 数据丢失率：可靠性的

- 吞吐

- 延迟：打电话、游戏 

- 安全性

#### 安全性 - SSL

`Secure Sockets Layer` 安全套接层

跑在TCP之上，在应用层实现

私密性、数据完整性、服务器的认证、报文的完整性

`https`



### 传输层提供的服务

#### UDP

不可靠 无连接



TCP

可靠、流量控制、拥塞控制、面向连接







## 网络应用实例

协议：报文格式语法、语义、次序、采取的动作

### WEB & HTTP

URL `Uniform Resource Locator`统一资源定位符

协议名 用户 口令 主机名 路径名 端口



web页有对象组成，通过URL对每个对象进行引用

HTTP超文本传输协议

web的应用层协议；TCP之上；CS模式





S1属于守护进程（waiting socket），监视80端口，客户端有请求时候经过握手建立连接socket

无状态服务器



#### 持续与非持续HTTP

HTTP1.1

TCP建立连接-》HTTP请求-》连接不关闭可以多次请求

![image-20240129150803208](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129150803208.png)

#### 响应时间

RTT `round trip time`

一个RTT发起TCP连接

一个2RTT发起and接受HTTP请求

文件传输时间：2RTT+传输文件



流水线方式，一个请求还没有接受回复就发出下一个请求

同步和异步

#### 报文

请求、相应

参考文章：[HTTP请求报文和响应报文格式](https://zhuanlan.zhihu.com/p/346408612)

请求行、请求头、空白行、请求体

```http
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
User-agent: Mozilla/4.0
Connection: close
Accept-language:fr
```

#####请求报文

- 请求方法

`GET`和`POST`是最常见的HTTP方法，除此以外还包括`DELETE`、`HEAD`、`OPTIONS`、`PUT`、`TRACE`

- URL地址
- 协议名称和版本号

???+abstract "请求报文头"
    - Client-IP：提供了运行客户端的机器的IP地址
    - From：提供了客户端用户的E-mail地址
    - Host：给出了接收请求的服务器的主机名和端口号
    - Referer：提供了包含当前请求URI的文档的URL
    - UA-Color：提供了与客户端显示器的显示颜色有关的信息
    - UA-CPU：给出了客户端CPU的类型或制造商
    - UA-OS：给出了运行在客户端机器上的操作系统名称及版本
    - User-Agent：将发起请求的应用程序名称告知服务器
    - Accept：告诉服务器能够发送哪些媒体类型
    - Accept-Charset：告诉服务器能够发送哪些字符集
    - Accept-Encoding：告诉服务器能够发送哪些编码方式
    - Accept-Language：告诉服务器能够发送哪些语言
    - Expect：允许客户端列出某请求所要求的服务器行为
    - Range：如果服务器支持范围请求，就请求资源的指定范围
    - Cookie：客户端用它向服务器传送数据
    - Cookie2：用来说明请求端支持的cookie版本

<img src="https://pic3.zhimg.com/80/v2-98df69e7e8fccd46bfe03cc473784766_1440w.webp" alt="img" style="zoom: 50%;" />

##### 响应报文

- 报文协议及版本；
- [状态码及状态描述](https://mp.weixin.qq.com/s/xxxS5qG244F6L10Y_ZxyGQ)

```HTTP
description:
200: OK
301: Moved Permanently
400: Bad Request
404: Not Found
505: HTTP Version Not Supported
```

| 状态码 |           类别            |        原因        |
| :----: | :-----------------------: | :----------------: |
|  1xx   | `Informational`信息状态码 |      正在处理      |
|  2xx   |    `Success`成功状态码    |      正常处理      |
|  3xx   |    `Redirection`重定向    |    需要附加操作    |
|  4xx   | `Client Error`客户端错误  | 请求出错，无法处理 |
|  5xx   |      `Server Error`       |   server处理出错   |



- 响应报文头

???+abstract "响应报文头"
    - Age：(从最初创建开始)响应持续时间
    - Public：服务器为其资源支持的请求方法列表
    - Retry-After：如果资源不可用的话，在此日期或时间重试
    - Server：服务器应用程序软件的名称和版本
    - Title：对HTML文档来说，就是HTML文档的源端给出的标题
    - Warning：比原因短语更详细一些的警告报文
    - Accept-Ranges：对此资源来说，服务器可接受的范围类型
    - Vary：服务器会根据这些首部的内容挑选出最适合的资源版本发送给客户端
    - Proxy-Authenticate：来自代理的对客户端的质询列表
    - Set-Cookie：在客户端设置数据，以便服务器对客户端进行标识
    - Set-Cookie2：与Set-Cookie类似
    - WWW-Authenticate：来自服务器的对客户端的质询列表

![img](https://pic2.zhimg.com/80/v2-2f86d3626184a4fc8b8fed6008419055_1440w.webp)

!!!+notice "TCP不维护报文长度，需要HTTP自己去断句"



#### 工具

CLI - Telnet

软件 - Wireshark

python - request库



#### `cookies`用户-服务器状态 

大多数门户网站使用

1) 在HTTP响应报文中有一个cookie的首部行
2) 在HTTP请求报文含有一个cookie的首部行
3) 在用户端系统中保留有一个cookie文件，由用户的浏览器管理
4) 在Web站点有一个后端数据库



隐私问题

#### `cache` - Web缓存

对用户：快 减小响应时间

服务器：减小web服务器载荷

网络：网络压力更小

<img src="https://pic2.zhimg.com/v2-d3f67aa0f739d24d75728e7c7e96b79d_r.jpg" alt="计算机网络——应用层 - 知乎" style="zoom:25%;" />

session\token

![image-20240129160059732](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129160059732.png)

解决办法

- 更快的接入链路：花钱多

- 安装本地缓存

  - 本地访问 $t_1$ 概率$P_1$

  - 远程访问$t_2$ 概率$P_2$

    总延时

    $$
    \begin{align}
    T &= P_1\cdot t_1 + P_2 \cdot t_2\\
    t &= \frac{I}{1-I}\frac{L}{R}\\
    I &= \frac{aL}{R}
    \end{align}
    $$
    

![image-20240129160659497](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129160659497.png)

![image-20240129160713797](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129160713797.png)

- `conditional GET`

- 存在问题：如果本地缓存版本落后于远端

  解决：`If-modified-since: <date>`

  向主机请求最后修改，如果被修改再发送一遍；没有被修改则就发一个没有修改的头部即可

  Server
  
```http
HTTP/1.0 304 Not Modified
```

```http
HTTP/1.0 200 Modified
```



### FTP

![image-20240129163627900](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129163627900.png)

有状态、双通道

- 向远程主机上传输文件或从远程主机接收文件

- 客户/服务器模式

- ftp服务器：端口号为21

- 控制命令的发出和数据的传输在不同的TCP下进行。

  <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129165011533.png" alt="image-20240129165011533" style="zoom:50%;" />

### Email

#### **SMTP** | 发送邮件协议 

用户代理 ——> 消息队列 ——>放到指定用户mailbox目录

使用TCPport:25

传输三阶段：握手、传报文（ASCII码）、关闭

![image-20240129165741501](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129165741501.png)

特点

- 使用持久连接
- 要求报文均为ASCII编码
- SMTP服务器使用`CRLF.CRLF`决定报文尾部
- 可以有多个附件

报文

- 首部：`To`,`From`,`Subject`
- 主体

##### 多媒体扩展 MIME(mitimedia mail extension)

base64编码

​	

#### 接收邮件协议

与邮箱服务器建立连接——>查询——>下载

##### POP3 `Post Office Protocol`

邮局访问协议

区分收件发件

下载并删除、下载并保留

无状态



##### IMAP `Internet Mail Access
Protocol`

Internet邮件访问协议

提供**远程目录维护**

有状态的



##### HTTP

可以用于文件上下载、收发邮件





### DNS | `Domain Name System`

[什么是DNS？ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/186028919)

[DNS详解，权威DNS，递归DNS，转发DNS，公共DNS_230.10.2.5-CSDN博客](https://blog.csdn.net/yangfanacc/article/details/42099913)

不是给人用的，是给其他应用提供的

IP 标示&寻址

#### 作用

- 提供域名到IP地址的转换

- 规范名字（主机1-12）到别名的转换 `host aliasing`
- 邮件父母器别名到正规名字转换 `Mail server aliasing`
- 负载均衡`Load Distribution`



一个平面？？



#### 方法

- 分层、基于域的命名
- 分布式数据库、树状关系
- 运行在UDP:53应用服务

!!!+note "互联网的复杂性"
	互联网的核心内容建立在互联网边缘的端系统应用之上



- 资源记录`resource records`

RR格式: (domain_name, ttl, type,class,Value)
`Domain_name`: 域名
`Ttl: time to live` : 生存时间(权威，缓冲记录)
`Class` 类别：对于Internet，值为IN
`Value` 值：可以是数字，域名或ASCII串
`Type` 类别：资源记录的类型—见下页

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240129232745663.png" alt="image-20240129232745663" style="zoom:80%;" />

缓存为了性能	TTL（默认2天）

删除为了一致性



##### 报文

报文首部

- 标识符（ID）：16位（订单编号）

- flags:

  - 查询/应答

  - 希望递归

  - 递归可用

  - 应答为权威

#### 结构

层次树状结构

- 顶级域`top lever domain`

.com .edu .gov .net .org .web 

.cn .us .nl .jp

- 子域`subdomain`

树叶就是主机

全球有13个根服务器



域与物理网络无关
 域遵从组织界限，而不是物理网络;是逻辑

- 一个域的主机可以不在一个网络
- 一个网络的主机不一定在一个域

##### 分类

**1.权威DNS：**

权威DNS是经过上一级授权对域名进行解析的服务器，同时它可以把解析授权转授给其他人，如COM顶级服务器可以授权[http://dns.com](https://link.zhihu.com/?target=http%3A//dns.com)这个域名的的权威服务器为[http://NS.ABC.COM](https://link.zhihu.com/?target=http%3A//NS.ABC.COM)，同时[http://NS.ABC.COM](https://link.zhihu.com/?target=http%3A//NS.ABC.COM)还可以把授权转授给[http://NS.DDD.COM](https://link.zhihu.com/?target=http%3A//NS.DDD.COM)，这样[http://NS.DDD.COM](https://link.zhihu.com/?target=http%3A//NS.DDD.COM)就成了[http://ABC.COM](https://link.zhihu.com/?target=http%3A//ABC.COM)实际上的权威服务器了。

**2.递归DNS:**

负责接受用户对任意域名查询，并返回结果给用户。

递归DNS可以缓存结果以避免重复向上查询。我们平时使用最多的就是这类DNS，他对公众开放服务，一般由网络运营商提供，你本地电脑上设置的DNS就是这类DNS。

**3.转发DNS:**

负责接受用户查询，并返回结果给用户。但这个结果不是按标准的域名解析过程得到的，而是直接把递归DNS的结果转发给用户。比如我们用的路由器里面的DNS就是这一类，用路由器的朋友可以看下本地电脑的DNS一般都是192.168.1.1。

#### 区域`zone`

- 区域的划分有区域管理者自己决定

- 将DNS名字空间划分为互不相交的区域，每个区域都是
  树的一部分

  

-  名字服务器：

  - 每个区域都有一个名字服务器：维护着它所管辖区域的权威信息
    (authoritative record)
  -  名字服务器允许被放置在区域之外，以保障可靠性



#### 工作过程

- 应用调用解析器(resolver)
- 解析器作为客户向Name Server发出查询报文
  （封装在UDP段中）

- Name Server返回响应报文(name/ip)

Local Name Server(预先配置好的)

- 目标名字在Local Name Server中
  情况1：查询的名字在该区域内部
  情况2：缓存(cashing)

- 当与本地名字服务器不能解析
  名字时，联系根名字服务器
  顺着根-TLD 一直找到权威名
  字服务器

##### 递归查询

根服务器负担太重

##### 迭代查询

根（及各级域名）服务器返回的不是查询结果，而是下一个NS的地址

最后由权威名字服务器给出解析结果

“我不知道这个名字，但可以向这个服务器请求”

##### 增删改

与树的操作相类似



### 攻击

**DDoS 攻击**

- 对根服务器进行流量轰炸
  攻击：发送大量ping
   没有成功

  - 原因１：根目录服务器配置了流量过滤器，防火墙

  - 原因２：Local DNS 服务器缓存了TLD服务器的IP地址,因此无需查询根服务器

- 向TLD服务器流量轰炸攻击发送大量查询，可能更危险

  - 效果一般，大部分DNS缓存了TLD

重定向攻击

- 中间人攻击
- 截获查询，伪造回答，从而攻击
  某个（DNS回答指定的IP）站点
- DNS中毒：发送伪造的应答给DNS服务器，希望它能够缓存这个虚假的结果
  技术上较困难：分布式截获和伪造

- 利用DNS基础设施进行DDoS
  - 伪造某个IP进行查询， 攻击这个目标IP
  - 查询放大

### P2P应用

#### 时间

![image-20240130004433432](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130004433432.png)

线性增加



![image-20240130004451304](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130004451304.png)

不是线性增加





如何定位所需资源
如何处理对等方的加入与离开



#### 非结构化P2P

`overlay` peer节点之间的覆盖网

- 集中化目录

上线时候向集中化目录进行注册，维护peer节点与资源列表

**问题**：单点故障、性能瓶颈、侵犯版权

- 完全分布式 - Gnutella

图式网络

建立`overlay`，泛洪`flooding`查询；BFS+记忆化搜索（TTL）



向所有邻居发出ping，邻居返回pong



- 混合体 KaZaA

组内集中式，组长分布式

| 文件 | 描述     | Hash                  |
| ---- | -------- | --------------------- |
|      | 匹配描述 | vid，元信息的唯一标识 |

BT

`bitmap`,定期泛洪交换

![image-20240130101612770](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130101612770.png)





- Peer加入torrent:

位图中全是0，随机请求其他节点的块；

4个bit后开始稀缺优先；`tit for tat`原则；可以更有利于网络的维护

扰动churn: peer节点可能会上线或者下线

一旦一个peer拥有整个文件，它会（自私的）离开或者保留（利他主义）在torrent中



`tracking server` 进行peer列表的维护

有限疏通：两个周期下载带宽大的排在前面（优先队列）；第三个周期在请求中随机选择

作为

#### 结构化 P2P（一致性哈希`consistent hash`）

参考了知乎网友写的[一致性哈希科普](https://zhuanlan.zhihu.com/p/129049724)

把ip地址hash值作为唯一标识

按照hash大小组成一个环；有序拓扑

每个用户维护和上一个id之间的文件



查询效率高，副本数量少



### `CDN:content distribution network`

如何保证超高数量并发服务

China Cash 中国蓝讯

内容访问加速

over the top 在边缘系统实现



#### 视频与编码

视频：固定速度显示的图像序列

网络视频特点：

- 高码率：>10x于音频,高的网络带宽需求
- 可以被压缩
- 90%以上的网络流量是视频

数字化图像：像素的阵列每个像素被若干bits表示

编码：使用图像内和图像间的冗余来降低编码的比特数

- 空间冗余(图像内)
- 时间冗余(相邻的图像间)

`CBR`: (`constant bitrate`): 以固定速率编码
`VBR`: (`variable bitrate`): 视频编码速率随时间的变化而变化

例子:

- MPEG 1 (CD-ROM) 1.5Mbps
- MPEG2 (DVD) 3-6 Mbps
- MPEG4 (often used in Internet, < 1 Mbps)
- AVS

#### 流化服务`streaming`

边下边看

##### `DASH: Dynamic,Adaptive Streaming over HTTP`

服务器:

- 将视频文件分割成多个块
- 每个块独立存储，编码于不同码率（8-10种）
- 告示文件（`manifest file`）: 提供不同块的**URL**

客户端:
- 先获取告示文件
- 周期性地测量服务器到客户端的带宽
- 查询告示文件,在一个时刻请求一个块，HTTP头部指定字节范围
- 根据带宽和缓冲选择编码块

 选择1: 单个的、大的超级服务中心“megaserver”

- 跳数较多，受限于小带宽
- 单个视频很多拷贝
- 单点故障、周围拥塞

`STB:set top box`机顶盒

#### CDN部署

ISP购买CDN服务

部署了很多的cache节点，云解析重定向后跳数较少



部署策略

- `enter deep`部署在`local ISP`

- `bring home`部署在关键位置，数据中心机房



点网页，CDN重定向，由缓存节点提供服务

通过DNS实现选择最优的节点

![image-20240130123254230](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130123254230.png)

## Socket API

传输层提供的服务——原语就是SocketAPI

socket: 分布式应用进程之间的门，传输层协议提供的端到端服务接口

### TCP socket

![SOCKET_API](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/socket_api.png)

服务器先运行 

--> 建立socket,返回整数 `welcome socket`

-->和本地端口捆绑

-->等待用户收发

-->返回`connection socket`

-->关闭socket



电脑打开多个QQ

使用一个IP和端口号

但是每个QQ功能可以独立使用、互不影响



#### 具体实现

PF `Protocol Family`协议簇

AF `Address Family`地址簇

inet = internet



如果本地没有指定端口，就调用隐式的

- `socket()`返回的是一个整数

[socket编程（一）：一个服务器服务一个客户端](https://voidint.github.io/post/socket/one_server_one_client/)

[socket编程（二）：每个进程服务一个连接](https://voidint.github.io/post/socket/one_process_per_connection/)

[TCP的socket详解_tcpsocket-CSDN博客](https://blog.csdn.net/weixin_41752434/article/details/116002194)

### UDP socket

建立socket

bind socket

读取socket

![image-20240130143354086](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130143354086.png)
