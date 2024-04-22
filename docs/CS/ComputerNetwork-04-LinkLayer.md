# 链路层与局域网 | `Link Layer`

## 链路层服务原理

> 链路层：一个节点把**帧**通过链路传送到另外一个节点
>
> 网络层：端到端 
>
> 传输层：区分进程、不可靠变成可靠
>
> 应用层：交换报文，形成网络应用

**广域网使用单点连接**

**局域网使用多点连接**

在子网的内部实现点到点point to point 



**网卡NIC**实现链路层和相应物理层的功能

![image-20240217114915691](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217114915691.png)

### 服务1：成帧

- 节点 `node`
- 链路 `link`
- 帧 `frame`PDU

在帧头部使用“MAC”（物理）地址来标示源和目的







### 服务2：检错和纠错

**在相邻两个节点之间完成可靠数据传递**

- 低差错率，不控制

- 高差错率，上层代价大所以要控制



#### EDC 差错检测和纠正位

单bit奇偶校验:
检测单个bit级错误



2维奇偶校验：
检测和纠正单个bit错误

无法检验对偶错误

#### CRC（循环冗余校验）

[[CRC校验\]手算与直观演示动画](https://www.bilibili.com/video/BV1V4411Z7VA/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

1. 模二运算（异或）

2. 使用位串的方式约定一个多项式，r次方，r+1位

4. 发送方sender 有D位，向左移动R位补零

   接收方用位串除以（从左往右按位异或）多项式得到余数R，即为校验
   $$
   \begin{align}
   &D\cdot 2^r\oplus R = n\cdot G\\
   &\Rightarrow D\cdot 2^r\oplus R \oplus R = n\cdot G \oplus R\\
   &\Rightarrow D\cdot 2^r = n\cdot G \oplus R\\
    &\therefore R= remainder[\frac{D\cdot 2^r}{G}]
    \end{align}
   $$

    例子：

   $$
    \begin{align}
   
    &D = 101110\\
   
    &G = 1001(r=3)\\
   
    &R = D<<3/G = remainder[\frac{101110000}{1001}] = 011
   
    \end{align}
   $$

CRC检错性能描述

- 能够检查出所有的1bit错误
- 能够检查出所有的双bits的错误
- 能够检查出所有长度$=r$或者$<r $位的错误
- 出现长度为$r+1$的突发错误，检查不出的概率是$\frac{1}{2^{r-1}}$
- 现长度大于r+1的突发错误，检查不出的概率$\frac{1}{2^r}$

### 服务3：全双工、半双工

半双工：双向传输，一次一个方向

全双工：双向传输，同时收发



## 多点接入 MAP

 MAC `media access control`

设计一个分布式算法，协调各个节点对信道访问和使用

**存在问题**：碰撞问题，广域网多点连接碰撞代价特别大

2个或更多节点同时传送: 冲突（`collision`）



必要条件：
1. 当一个节点要发送时，可以R速率发送.
2. 当M个节点要发送，每个可以以R/M的平均速率发送
3. 完全分布的:没有特殊节点协调发送；没有时钟和时隙的同步
4. 简单



### 信道划分 

- 把信道划分成小片（时间、频率、编码）
- 分配片给每个节点专用

TDMA: time division multiple access 分时

FDMA: frequency division multiple access 分频 （类似鲸鱼蝙蝠不同频率

CDMA (code division multiple access) 分码 （类似方言

### 随机访问

- 信道不划分，允许冲突
- **如何检测冲突**
- **冲突后恢复**



#### 时隙ALOHA

时隙`slot`

所有节点在信 道上保持同步

在有限信道发，检测冲突，如果有碰撞，下一时隙按照概率p进行发送（服从二项分布）

信道状态：**碰撞的C、空闲的E、成功的S**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217123812413.png" alt="image-20240217123812413" style="zoom:50%;" />

##### 优点

-  节点可以以信道带宽全速连续传输
-  高度分布：仅需要节点之间在时隙上的同步
-  简单

##### 缺点

- 存在冲突，浪费时隙

- 即使有帧要发送，仍然有可能存在空闲的时隙

- 节点检测冲突的时间<帧传输的时间；必须传完 

  > 鸡蛋坏了也要吃完

-  需要时钟上同步

##### 效率分析

当有很多节点，每个节点有很多帧要发送时，x%的时隙是成功传输帧的时隙

最大效率 
$$
f(N,P) = N\cdot P (1-P)^{N-1}\\
f_{max} = 37.5\%
$$



#### Pure ALOHA

任何时间有帧形成，就将帧放出去

- 简单，无需时间同步

![image-20240217124359578](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217124359578.png)

frame time 

bit time

**效率低于时隙ALOHA**
$$
\begin{align}
f(N,P) &= N\cdot P (1-P)^{N-1} \cdot(1-P)^{N-1} 
\\
&= N  \cdot P\cdot (1-P)^{2(N-1)} \\
f_{max} &= 17.5\%
\end{align}
$$



#### CSMA

> 说之前听一下别人是否再说话，不要打断别人正在进行的说话!

如果侦听到信道空闲，传送整个帧

如果侦听到信道忙，推迟传送

监听信道直至信道空闲位置`carrier sense`

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217125439610.png" alt="image-20240217125439610" style="zoom:50%;" />

- **仍然会发生冲突**(局部探知全局情况不可靠)

各个节点通过局部sense得到全局状态，最远两个节点的时间越长，冲突可能性就越大

整个冲突帧的传输时间都被浪费了，是无效的传输(红黄区域)





#### CSMA/CD（Ethernet）

`collision detection` 冲突检测

> 一边发送，一边监听，检测到冲突就停止发送



**过程分析**

1. 适配器获取数据报，创建帧

2. 发送前：侦听信道CS<br>
  1)闲：开始传送帧<br>
  2)忙：一直等到闲再发送<br>

3. 发送过程中，冲突检测CD<br>
  1)没有冲突：成功<br>
  2)检测到冲突：放弃,之后尝试重发<br>

4. 发送方适配器检测到冲突，除放弃外，还**发送一个Jam信号**，所有听到冲突的适配器也是如此；防止冲突太短听不到；

5. `exponential backoff`二进制指数退避算法<br>

  如果放弃，适配器进入指数退避状态在第m次失败后，适配器随机选择一个${0,1,2,\dots,2^m-1}$中选择K<br>

  等待$K*512$位时，然后转到步骤2<br>

  等待时间增加了<br>

> "了不得啦，这里有冲突啊啊啊啊"    
>
> 强化冲突：让所有站点都知道冲突
>
> 第一次碰撞：在$\{0,1\}$中选择K，延时$K*512$位时
>
> 第二次：在$\{0,1,2,3\}$$\{0,1\}$中选择K，延时$K*512$位时

CSMA/CD 

碰撞窗口最大是1024

 

**效率分析**

| 量          | 含义                       |
| ----------- | -------------------------- |
| $T_{prop}$  | LAN上2个节点的最大传播延迟 |
| $t_{trans}$ | 传输最大帧的时间           |

$$
efficiency = \frac{1}{1+5T_{prop}/t_{trans}}
$$

效率变为1

- 当$T_{prop}$ 变成0时
- 当$t_{trans}$​ 变成无穷大时(某个节点800T，一旦抓住信道就不放手了)
- 比ALOHA更好的性能，而且简单，廉价，分布式!



#### CSMA/CA(WLAN) 

`collision avoidance` 冲突避免

有基础设施`infrastructure`

![image-20240418000656125](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240418000656125.png)

802.11: **没有冲突检测，做不了CD**

- 无法检测冲突：自身信号远远大于其他节点信号；有衰减
- 即使能CD：不冲突 != 成功<br>
  - 无法CD，一旦发送一股脑全部发送完毕，不CD<br>
  - 为了避免无CD带来的信道利用率低的问题，事前进行冲突避免<br>

- 冲突也有可能是成功的

![image-20240418001217281](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240418001217281.png)



无线链路特性，需要每帧确认；例如：由于隐藏终端问题，在接收端可能形成干扰,接收方没有正确地收到。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240418001048962.png" alt="image-20240418001048962" style="zoom:33%;" />





??? +note "2个站点有数据帧需要发送，第三个节点正在发送"
=== "WLAN CA"
    - 无法CD，一旦发送就必须发完，如冲突信道浪费严重，代价高昂
    - 思想：尽量事先避免冲突（抛骰子），而不是在发生冲突时放弃然后重发
    - 听到发送的站点，分别选择随机值，回退到0发送
      - 不同的随机值，一个站点会胜利
      - 失败站点会冻结计数器，当胜利节点发完再发

=== "LAN CD"
    让2者听完第三个节点发完，立即发送
        冲突：放弃当前的发送，避免了信道的浪费无用于冲突帧的发送
        代价不昂贵
        

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217160017462.png" alt="image-20240217160017462" style="zoom:50%;" />

无法完全避免冲突

request to send 

clear to send

只有单向冲突，通过预约和管理解决冲突

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217160450274.png" alt="image-20240217160450274" style="zoom:50%;" />



#### 线缆接入网络

下行CMTS一个

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217160813735.png" alt="image-20240217160813735" style="zoom:50%;" />

多个40Mbps 下行(广播)信道,FDM
	下行：通过FDM分成若干信道，互联网、数字电视等
	互联网信道：只有1个CMTS在其上传输
多个30 Mbps上行的信道,FDM
	多路访问：所有用户使用；接着TDM分成微时隙
	部分时隙：分配；部分时隙：竞争；

`DOCSIS: data over cable service interface spec`







### 依次轮流 Taking Turns

- 节点依次轮流
- 但是有很多数据传输的节点可以获得较长的信道使
  用权

#### 论询:

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217161518137.png" alt="image-20240217161518137" style="zoom:25%;" />

主节点邀请从节点依次传送



**缺点:**

- 轮询开销：轮询本身消耗信道带宽
- 等待时间：每个节点需等到主节点轮询后开始传输，即使只有一个节点，也需要等到轮询一周后才能够发送
- **单点故障**：master故障，整个系统失效



#### 令牌传递:

> 击鼓传花

控制令牌(`token`)循环从一个节点到下一个节点传递

令牌报文：**特殊的帧**，1是令牌，0是数据

谁发，绕网一周后，谁接受



**缺点:**

- 令牌开销：本身消耗带宽
- 延迟：只有等到抓住令牌，才可传输
- 单点故障(token)：令牌丢失系统级故障，整个系统无法传输
- 复杂机制重新生成令牌







## LAN `Local Area Network`

### MAC `medium access control`

前n-1跳：用于使数据报到达目的IP子网；最后一跳：到达子网中的目标节点

LAN（MAC/物理/以太网）地址:

MAC地址，48bit；**FF-FF-FF-FF 广播地址**

MAC地址由IEEE管理和分配，制造商购入MAC地址空间（保证唯一性）





??? note "IP地址分层，mac地址在一个平面"

- 网卡在生产时不知道被用于哪个网络，因此给网卡一个唯一的标示，用于区分一个网络内部不同的网卡即可

=== "分离好处"
	a) 网卡坏了，ip不变，可以捆绑到另外一个网卡的mac上<br>
	b) 物理网络还可以除IP之外支持其他网络层协议，链路协议为任意上层网络协议， 如IPX等<br>

=== "捆绑的问题"
	a) 如果仅仅使用IP地址，不用mac地址，那么它仅支持IP协议<br>
	b) 每次上电都要重新写入网卡IP地址；<br>
	c) 另外一个选择就是不使用任何地址；不用MAC地址，则每到来一个帧都要上传到IP层次，由它判断是不是需要接受，干扰一次<br>





LAN中，“不碰” = 成功

条件是 $帧>= 2\tau$​



### ARP: `Address Resolution Protocol`

> 完成IP地址到MAC地址的转换；
>
> 从而完成把分组封装帧，从一个网卡发送到另一个网卡

在LAN上的每个IP节点都有一个ARP表

广播查询，缓存，20min

- ARP表：包括一些LAN节点IP/MAC地址的映射`< IP address; MAC address; TTL >`
  TTL时间是指地址映射失效的时间;典型是20min

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217163640456.png" alt="image-20240217163640456" style="zoom: 50%;" />



### Ethernet

最主流的LAN技术：98%占有率；廉价；带宽不断提升



使用同轴电缆链接

![image-20240418090302357](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240418090302357.png)

**总线**

在上个世纪90年代中期很流行

- 所有节点在一个碰撞域内，**任意时刻只允许一个节点发送**，降低利用率
- 可靠性差，如果介质破损，形成反射，误认为是冲突，总是冲突

**星型**

目前最主流

连接选择: hub 或者switch；现在一般是交换机在中心

![image-20240418090518781](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240418090518781.png)



发送方适配器在以太网帧中封装IP数据报

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217165121174.png" alt="image-20240217165121174" style="zoom:50%;" />

- 前导码：用来同步接收方和发送方的时钟
- 无连接：帧传输前，发送方和接收方之间没有握手（本身可靠性较高
- 不可靠：接收方适配器不发送ACKs或NAKs给发送方

使用MAC协议：CSMA/CD 二进制指数退避算法



- 相同的MAC协议（介质访问控制）和帧结构

- 不同的速率：2 Mbps、10 Mbps 、100 Mbps 、1Gbps、10G bps
- 不同的物理层标准
- 不同的物理层媒介：光纤，同轴电缆和双绞线







#### 以太帧类型

以太帧有很多种类型。不同类型的帧具有不同的格式和 MTU 值。但在同种物理媒体上都可同时存在。

1. 以太网第二版或者称之为 Ethernet II 帧，DIX 帧，是最常见的帧类型。并通常直接被 IP 协议使用；
2. Novell 的非标准 IEEE 802.3 帧变种；
3. IEEE 802.2 逻辑链路控制（LLC) 帧；
4. 子网接入协议（SNAP）帧。

### WLAN 802.11





### 链路层的设备

#### Hub集线器

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217173640472.png" alt="image-20240217173640472" style="zoom:50%;" />

高负载下性能差



#### 交换机

高负载下性能可以

**链路层设备**：扮演主动角色（端口执行以太网协议），对帧进行存储转发

**透明**：主机对交换机的存在可以不关心；通过交换机相联的各节点好像这些站点是直接相联的一样

**即插即用，自学习**：交换机无需配置





- 主机有一个专用和直接到交换机的连接

- 交换机缓存到来的帧

- 对每个帧进入的链路使用以太网协议，没有碰撞；全双工

- MAC协议在其中的作用弱化了



**交换表**

MAC地址 + 对应端口 + 时戳

即插即用，**自学习**

| `MAC addr` | interface | TTL  |
| ---------- | --------- | ---- |
| A          | 1         | 60   |
|            |           |      |

- 当接收到帧，交换机学习到发送站点所在的端口（网段），记录源目标MAC和端口在交换表中（软状态维护机制

> 有人发了个包裹给你，又告诉你目标地址是对方，可以不把包裹发回去

- 不知道其位置在哪：泛洪<br>
- 转发：知道目标A对应的链路：选择性发送到那个端口<br>

**交换机可以级联**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217175712364.png" alt="image-20240217175712364" style="zoom:50%;" />

有生成树算法，每个时刻工作的只有一颗树，防止广播式传播

### VLANS

带有VLAN功能的交换机（们）可以被配置成：一个物理LAN基础设施，虚拟成多个LANs

如果有多个交换机，希望它们相连并且共享VLANs信息

- 方法1：各交换机每个VLAN一个端口和另外交换机相应；VLAN端口相连->扩展性问题
- `trunk port`干线端口: 多个交换机共享定义的VLAN，在它们之间传输帧

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217180329788.png" alt="image-20240217180329788" style="zoom:50%;" />

## 数据中心网络

负载均衡器: 应用层路由

- 接受外部的客户端请求
- 将请求导入到数据中心内部
- 返回结果给外部客户端(对于客户端隐藏数据中心的内部结构)



在交换机之间，机器阵列之间有丰富的互连措施:

- 在阵列之间增加吞吐(多个可能的路由路径)
- 通过冗余度增加可靠性