---
comments: true
---
# 网络层 | Network Layer

![网络层](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E7%BD%91%E7%BB%9C%E5%B1%82.svg)

## 原理


### 服务

- 在发送主机和接收主机对之间传送段（segment）
- 在发送端将段封装到数据报中
- 在接收端，将段上交给传输层实体



- 转发：通过单个路口；分组从路由器的输入接口转发到合适的输出接口
- 路由：规划源到目标的路线；全局功能

> 路由：导航路径
>
> 转发：地铁站各个出口，acbd出口就是端口



端到端end to end

源主机到目标主机、best evil尽力而为

> 尽力而为 = 什么都不保证 = 开摆







对于单个数据报的服务:

- 可靠传送
- 延迟保证，如：少于40ms的延迟

对于数据报流的服务:

- 保序数据报传送
- 保证流的最小带宽
- 分组之间的延迟差



### 数据平面 转发 - 本地功能



转发：根据路由表进行分组的转发，决定从路由器输入端口到达的分组如何转发到输出端口

- 转发功能：
  - 传统方式：基于目标地址+转发表
  - SDN方式：基于多个字段+流表

泛洪——一传十十传百

### 控制平面 路由 - 全局功能

> 运行路由选择算法／协议(RIP, OSPF, BGP) 生成路由表

分布式的实现

控制平面计算路由表

- 2个控制平面方法:
  - 传统的路由算法: 在路由器中被实现
  - SDN在远程的服务器中实现



## 数据平面

### `Router` 路由器

> The end-to-end routing process is analogous to a car driver who does not
> use maps but instead prefers to ask for directions.



<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201140806254.png" alt="image-20240201140806254" style="zoom:67%;" />

最长前缀匹配`longest prefix matching`

当给定目标地址查找转发表时，采用最长地址前缀匹配的目标地址表项

#### 输入端口缓存

当交换机构的速率小于输入端口的汇聚速率时， 在输入端口可能要排队

排队延迟以及由于输入缓存溢出造成丢失!

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201140951934.png" alt="image-20240201140951934" style="zoom:50%;" />

packet per minute

#### `fabric`交换结构

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141044080.png" alt="image-20240201141044080" style="zoom:50%;" />

**memory**

- 在CPU直接控制下的交换
- 转发速率被内存的带宽限制(数据报通过BUS两遍)
- 一次只能转发一个分组
- 如果内存带宽为每秒可写进内存或从内存读出最多B个分组，则总的转发吞吐量(分组从输入端口被传送到输出端口的总速率)必然小于B/2

**bus**

- 总线竞争: 交换速度受限于总线带宽

- 1次处理一个分组

**crossbar**

- Banyan（榕树）网络，crossbar(纵横)和其它的互联网络被开发，将多个处理器连接成多处理器

- 当分组从端口A到达，转给端口Y；控制器短接相应的两个总线

- 高级设计：将数据报分片为固定长度的信元，通过交换网络交换



#### `schedule` 调度策略

解决输出链路问题

**FIFO (first in first out) scheduling**

- tail drop: 丢弃刚到达的分组
- priority: 根据优先权丢失/移除分组
- random: 随机地丢弃/移除

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141335251.png" alt="image-20240201141335251" style="zoom:50%;" />

**优先权调度**

发送最高优先权的分组

先传高优先级的队列中的分组，除非没有(红色传完再传绿色)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141445525.png" alt="image-20240201141445525" style="zoom:50%;" />

**Round Robin (RR) scheduling**

循环扫描不同类型的队列, 发送完一类的一个分组，再发送下一个类的一个分组，循环所有类

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141528684.png" alt="image-20240201141528684" style="zoom:50%;" />

**Weighted Fair Queuing (WFQ)**

一般化的Round Robin

在一段时间内，每个队列得到的服务时间是：$\frac{Wi}{\sigma(Wi)} \times t$，和权重成正比

每个类在每一个循环中获得不同权重的服务量

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141703167.png" alt="image-20240201141703167" style="zoom:50%;" />



### IP协议

#### 数据报格式

![image-20240201155758709](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201155758709.png)

![预览大图](https://data.educoder.net/api/attachments/582224)





??? note "各个字段含义"
    （1）**版本`version`**（4 位）：该字段定义 IP 协议版本，负责向处理机所运行的 IP 软件指明此 IP 数据报是哪个版本，所有字段都要按照此版本的协议来解释。如果计算机使用其他版本，则丢弃数据报； <br>
    （2）头部长度`Header Length`（4 位）：该字段定义数据报协议头长度，表示协议头部具有 32 位字长的数量。协议头最小值为 5 ，最大值为 15； <br>
    （3）服务（ 8 位）：该字段定义上层协议对处理当前数据报所期望的服务质量，并对数据报按照重要性级别进行分配。前 3 位成为优先位，后面 4 位成为服务类型，最后 1 位没有定义。这些 8 位字段用于分配优先级、延迟、吞吐量以及可靠性； <br>
    （4）总长度（ 16 位）：该字段定义整个 IP 数据报的字节长度，包括协议头部和数据。其最大值为 65535 字节。以太网协议对能够封装在一个帧中的数据有最小值和最大值的限制（ 46~1500 个字节）； <br>
​    （5）**标识`Identification`**（ 16 位）：该字段包含一个整数，用于识别当前数据报。当数据报分段时，标识字段的值被复制到所有的分段之中。该字段由发送端分配，帮助接收端集中数据报分段； <br>
​    （6）标记`Flags`（ 3 位）：该字段由 3 位字段构成，其中最低位（ MF ）控制分段，存在下一个分段置为 1 ，否则置 0 代表该分段是最后一个分段。中间位（ DF ）指出数据报是否可进行分段，如果为 1 则机器不能将该数据报进行分段。第三位即最高位保留不使用，值为 0； <br>
​    （7）**分段偏移`offset`**（ 13 位）：该字段指出分段数据在源数据报中的相对位置，支持目标 IP 适当重建源数据； <br>
​    （8）**生存时间`Time to live`**（ 8 位）：路过一个路由 TTL-1。若TTL字段减为0 ，则该数据报必须丢弃。 <br>
​    （9）协议（ 8 位）：该字段指出在 IP 处理过程完成之后，有哪种上层协议接收导入数据报。这个字段的值对接收方的网络层了解数据属于哪个协议很有帮助； <br>
​    （10）**校验和`checksum`** （ 16 位）：头部是否出错 <br>
​    （11）源地址（ 32 位）：源主机 IP 地址<br>
​    （12）目的地址（ 32 位）：目标主机 IP 地址<br>





#### 子网

主机与物理链路之间的边界叫作接口( interface)，路由器与它的任意一条链路之间的边界也叫作接口。

**一个IP地址和一个接口相关联**（32位）

- 子网前缀一样

- 收发在子网的内部一跳可达

> 一个子网可以看做一个家庭，一个IP看做一个成员，发到家就行；
>
> 以子网为单位向外通告可达信息

下图中有六个子网

![image-20240426230924516](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426230924516.png)

**子网掩码**







#### CIDR

因特网的地址分配策略被称为无类别域间路由选择(Classless Interdomain Rou ling ,CIDR)

**子网掩码 32位**



因为ABC这样划分容易导致差距过大，B类裕量太多，C类又太少，所以采用

如果是1的话代表是网络号，是0则是主机号

IP号 与 子网掩码进行与操作(&)，那么就可以得到网络号；主机号全为0



#### 分类编址

![image-20240201180932322](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201180932322.png)

全0网络和全1网络不用了

ABC 单播地址、DE 广播地址

=== "A类IP地址"

	1bits网络+2bits主机
	
	网络地址的最高位必须是`0` 地址范围从1.0.0.0 到127.0.0.0)。
	
	可用的A类网络有127个，每个网络能容纳$2^{24}-2 = 16777214$个主机。
	
	>A:0-127，其中0代表任何地址，127为回环测试地址，因此，A类ip地址的实际范围是1-126.其中127.0.0.1是一个特殊的IP地址，表示主机本身，用于本地机器的测试。


=== "B类IP地址"

	2bits网络地址、2bits的主机地址
	
	网络地址的最高位必须是“10”
	
	地址范围从128.0.0.0到191.255.255.255。
	
	可用的B类网络有16382个，每个网络能容纳6万多个主机 。
	
	>B:128-191，其中128.0.0.0和191.255.0.0为保留ip，实际范围是128.1.0.0–191.254.0.0。


=== "C类IP地址"

	3bits网络地址、1bits的主机地址网络地址
	
	最高位必须是“110”。范围从192.0.0.0到223.255.255.255。
	
	C类网络可达209万余个，每个网络能容纳254个主机。
	
	>C:192-223，其中192.0.0.0和223.255.255.0为保留ip，实际范围是192.0.1.0–223.255.254.0


=== "D类IP地址"

	用于多点广播(Multicast)。
	
	D类IP地址第一个字节以“lll0”开始，它是一个专门保留的地址。它并不指向特定的网络，目前这一类地址被用在多点广播(Multicast)中。
	
	多点广播地址用来一次寻址一组计算机，它标识共享同一协议的一组计算机。224.0.0.0到239.255.255.255用于多点广播 。

=== "E类IP地址"

	以“11110”开始，为将来使用保留。240.0.0.0到255.255.255.254，255.255.255.255用于广播地址。



=== "特殊IP地址"

	子网部分全为零 -- 本网络
	
	主机部分全为零 -- 本主机
	
	主机部分全为1 -- 广播地址，这个网络的所有主机
	
	127.x.x.x -- 回路地址、测试地址（属于A类）
	
	>内网地址：永远不会做公用地址，只在局部有意义;路由器不转发
	>A类： 10.  0.0.0 -  10.255.255.255 	MASK	255.  0.0.0
	>B类：172. 16.0.0 - 172. 31.255.255 	MASK  255.255.0.0
	>C类：192.168.0.0 - 192.168.255.255	  MASK	255.255.255.0



#### 分片

> 例子：
>
> 4000B数据 = 20B头部+ 3980数据
>
> MTU为1500B
>
> 把3980拆分成三个独立分组
>
> 第一片：20B+1480B
>
> 第二片：20B+1480B
>
> 第三片：20B+1020B
>
> 以8B为单位计算offset

![image-20240201160531914](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201160531914.png)

MTU从小到大，每转发一次是否都要适应最大长度

由上可知，一个分片最多存储`1480bytes`,若数据大于`1480bytes`则需要分片。设数据大小为`s`，则分片数`k=⌈s/1480⌉`。

### DHCP 动态主机配置协议

![image-20240426231424660](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426231424660.png)

> 显示了连接到子网223.1.2/24的一个DHCP服务器，具有一台提供中继代理服务的路由器，它为连接到子网223.1.1/24和223.1.3/24的到达客户提供DHCP服务。



[DHCP协议详解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/265293856)

目标: 允许主机在加入网络的时候，动态地从服务器那里获得IP地址：

- 可以更新对主机在用IP地址的租用期-租期快到了
- 重新启动时，允许重新使用以前用过的IP地址

DHCP Discover：由客户端发出，用来发现DHCP服务器。广播

DHCP Offer：由DHCP服务器发出，告诉客户端，我可以提供IP地址。广播。因为在子网中可能存在几个DHCP 服务器，该客户也许会发现它处于能在几个提供者之间进行选择的优越位置。

DHCP Request：由客户端发出，告诉对应的DHCP服务器，我需要IP地址。

DHCP ACK：由DHCP服务器发出，提供客户端响应的IP地址。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-52bf53d16bc59ef70312e63a91511246_1440w.webp)

使用UDP进行传输

![image-20240411090326803](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240411090326803.png)

![预览大图](https://data.educoder.net/api/attachments/581836)

- 请求报文：DHCP Discover、DHCP Request、DHCP Release、DHCP Inform 和 DHCP Decline。
- 应答报文：DHCP Offer、DHCP ACK 和 DHCP NAK。

#### DHCP Discover数据包

![img](https://data.educoder.net/api/attachments/581839) ![img](https://data.educoder.net/api/attachments/570102)

#### DHCP Offer数据包

当 DHCP 服务器收到一条 DHCP Discover 数据包时，用一个 DHCP Offerr 包给予客户端响应： ![img](https://data.educoder.net/api/attachments/570097) 发送 DHCP Offer 消息的 DHCP 服务器 IP 是`172.31.159.254`，如下截图： ![img](https://data.educoder.net/api/attachments/985332)

#### DHCP Request包

当 Client 收到了 DHCP Offer 包以后，确认有可以和它交互的 DHCP 服务器存在，于是 Client 发送 Request 数据包，请求分配 IP。此时的源 IP 和目的 IP 依然是`0.0.0.0`和`255.255.255.255`。

#### DHCP ACK包

服务器用 DHCP ACK 包对 DHCP 请求进行响应： ![img](https://data.educoder.net/api/attachments/570099) 

其中服务器发送给客户端的关于此地址的配置信息： ![img](https://data.educoder.net/api/attachments/581844)

#### DHCP Release包

DHCP释放消息（DHCP Release）的目的是通知DHCP服务器客户端不再需要之前所分配的IP地址，以便DHCP服务器可以释放该IP地址并使其能够被其他客户端使用。这通常发生在客户端永久离开网络或不再需要IP地址时



没有ACK消息

If the DHCP Release message from the client is lost, the DHCP server would have to wait until the lease period is over for that IP address until it could reuse it for another client.





### NAT 网络地址转换

`Network Address Translation`

内、外网地址转换，NAT路由器对外界的行为就如同一个具有单IP地址的单一设备。路由器从ISP 的DHCP 服务器得到它的地址，并且路由器运行一个DHCP 服务器，为位于NAT-DHCP 路由器控制的家庭网络地址空间中的计算机提供地址。



#### 原因

- 不需要从ISP分配一块地址，可用一个IP地址用于所有的（局域网）设备--省钱 
- 可以在局域网改变设备的地址情况下而无须通知外界
- 可以改变ISP（地址变化）而不需要改变内部的设备地址
- 局域网内部的设备没有明确的地址，对外是不可见的--安全

#### 操作

NAT 路由器上的一张NAT 转换表( `NAT translation table` ) ，并且在表项
中包含了端口号及IP 地址。

- 外出数据包：替换源地址和端口号为NAT IP地址和新的端口号，目标IP和端口不变

- 记住每个转换替换对（在NAT转换表中）

- 进入数据包：替换目标IP地址和端口号，采用存储在NAT表中的mapping表

![image-20240201204851149](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201204851149.png)

#### 弊端

- 路由器只应该对第3层做信息处理，而这里对端口号（4层）作了处
  理
- 违反了end-to-end 原则
  - 端到端原则：复杂性放到网络边缘；无需借助中转和变换，就可以直接传送到目标主机
  - NAT可能要被一些应用设计者考虑, eg, P2P applications
  - 外网的机器无法主动连接到内网的机器上
- 地址短缺问题可以被IPv6 解决



### IPV6

- 头部40个字节，传输中不允许分片

- 128位IP地址

![image-20240426232040298](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426232040298.png)

#### 报文格式

`Priority`: 标示流中数据报的优先级<br>
`Flow Label`: 标示数据报在一个“flow.”( “flow”的概念没有被严格的定义)<br>
`Next header`: 标示上层协议<br>

`Checksum`: 被移除掉，降低在每一段中的处理速度<br>
`Options`: 允许，但是在头部之外, 被“NextHeader” 字段标示<br>

![image-20240426232120656](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426232120656.png)



#### 通信

IPV4和IPV6之间是双栈协议

使用隧道进行通信

平滑过渡到IPV6的时代

tunneling

> 将IPV4看作大海，IPV6看作小岛，**用船载车**





## 控制平面

### 路由选择算法

#### 全局 `link state`

所有的路由器拥有完整拓扑和边的代价

1. 发现相邻节点,获知对方网络地址

2. 测量到相邻节点的代价(延迟,开销)实测法,发送一个分组要求对方立即响应回送一个ECHO分组

3. 组装一个LS分组,描述它到相邻节点的代价情况

4. 将分组通过扩散的方法发到所有其它路由器；以上4步让每个路由器获得拓扑和边代价
  
5. 通过**Dijkstra**算法找出最短路径（这才是路由算法

#### 分布式 `distance vector`

最短路径是，



定期测量它到相邻节点的代价

定期与相邻节点交换路由表(DV)



**特点：**
好消息传播快，坏消息传播满；

坏消息传得慢——可能形成环路，需要很多次循环才能收敛,重复计算路径

split horizon：不在关公面前耍大刀






解决方案：在传输路由表的时候，不要传输与经过对方节点的距离（不要套娃）

??? note "对比"
  ===	"消息复杂度（DV胜出）"
    - LS: 有n 节点, E 条链路,发送报文O(nE)个；局部的路由信息；全局传播<br>
    - DV: 只和邻居交换信息；全局的路由信息，局部传播<br>


  === "收敛时间（LS胜出）"
    - LS: $O(n^2)$ 算法有可能震荡<br>
    - DV: 收敛较慢；可能存在路由环路；count-to-infinity 问题<br>
      
  === "健壮性: 路由器故障会发生什么（LS胜出）"
    - LS:节点会通告不正确的链路代价；每个节点只计算自己的路由表；错误信息影响较小，局部，路由较健壮<br>
    - DV:节点可能通告对全网所有节点的不正确路径代价距离矢量；每一个节点的路由表可能被其它节点使用；错误可以扩散到全网<br>







路径选择

最长前缀匹配——最精确



路由信息是以子网为单位的

### `Gateway`网关

网关实质上是**一个网络通向其他网络的IP地址**



在没有路由器的情况下，两个网络之间是不能进行TCP/IP通信的，即使是两个网络连接在同一台交换机(或集线器)上，TCP/IP协议也会根据子网掩码(255.255.255.0)判定两个网络中的主机处在不同的网络里。而要实现这两个网络之间的通信，则必须通过网关。如果网络A中的主机发现数据包的目的主机不在本地网络中，就把数据包转发给它自己的网关，再由网关转发给网络B的网关，网络B的网关再转发给网络B的某个主机(如附图所示)。网络B向网络A转发数据包的过程。



通俗解释

> 节选自[魔都狗蛋儿](https://www.zhihu.com/people/modugoudaner)的文章[什么是网关，网关的作用是什么？ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/165142303)

　　假设你的名字叫小不点，你住在一个大院子里，你的邻居有很多小伙伴，在门口传达室还有个看大门的李大爷，李大爷就是你的网关。当你想跟院子里的某个小伙伴玩，只要你在院子里大喊一声他的名字，他听到了就会回应你，并且跑出来跟你玩。


但是你不被允许走出大门，你想与外界发生的一切联系，都必须由门口的李大爷（网关）用电话帮助你联系。假如你想找你的同学小明聊天，小明家住在很远的另外一个院子里，他家的院子里也有一个看门的王大爷（小明的网关）。但是你不知道小明家的电话号码，不过你的班主任老师有一份你们班全体同学的名单和电话号码对照表，**你的老师就是你的DNS服务器**。于是你在家里拨通了门口李大爷的电话，有了下面的对话：

> 简单来讲，你老是就是你的域名服务器，你家小区的看门大爷就是你的网关。

小不点：李大爷，我想找班主任查一下小明的电话号码行吗？
李大爷：好，你等着。（接着李大爷给你的班主任挂了一个电话，问清楚了小明的电话）问到了，他家的号码是211.99.99.99
小不点：太好了！李大爷，我想找小明，你再帮我联系一下小明吧。
李大爷：没问题。（接着李大爷向电话局发出了请求接通小明家电话的请求，最后一关当然是被转接到了小明家那个院子的王大爷那里，然后王大爷把电话给转到小明家）
就这样你和小明取得了联系。

### 内部网关协议

#### RIP

代价低



跳数：16不可达

最多包括25个子网



通告`advertisement`

DV: 在邻居之间每30秒交换通告报文
 定期，而且在改变路由的时候发送通告报文
 每一个通告: 至多AS内部的25个目标网络的

 目标网络+跳数



如果180秒没有收到通告信息-->邻居或者链路失效



以进程方式实现网络层功能，借助传输层udp

RIP 以应用进程的方式实现：route-d (daemon)

通告报文通过UDP报文传送，周期性重复







#### OSPF  Open Shortest Path First

使用LS算法
 LS 分组在网络中（一个AS内部）分发

- 路由计算采用Dijkstra算法

- 通告信息会传遍AS全部（通过泛洪）

- 安全: 所有的OSPF报文都是经过认证的(防止恶意的攻击)

- 允许有多个代价相同的路径存在(在RIP协议中只有一个)

在IP数据报上直接传送OSPF报文(而不是通过UDP和TCP)

网络比较大，分成若干区域

![image-20240215161223409](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240215161223409.png)



### 外部网关协议`Border Gateway Protocol`

> 参考[5.4 ISP之间的路由选择：BGP_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1JV411t7ow?p=37&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

#### 层次路由

满足安全性和管理问题、规模问题

- 自治区内：
- 自治区之间：路由聚集，对外表现成



- `eBGP`: 从相邻的ASes那里获得子网可达信息；转发子网收到的其他AS子网可达信息，将`iBGP`得到的信息通过`eBGP`传出去

- `iBGP`: 将获得的子网可达信息传遍到AS内部的所有路由器



基于距离矢量算法（路径矢量）——不仅仅是距离矢量，还包括到达各个目标网络的详细路径（AS序号的列表）能够避免简单DV算法的路由环路问题

![image-20240215163137452](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240215163137452.png)



#### 报文

2个重要的属性:

- AS-PATH: 前缀的通告所经过的AS列表<br>检测环路；多路径选择<br>在向其它AS转发时，需要将自己的AS号加在路径上<br>
- NEXT-HOP: 从当前AS到下一跳AS有多个链路，在NETX-HOP属性中，告诉对方通过那个IS转发.



使用TCP协议交换BGP报文.

- `OPEN`: 打开TCP连接，认证发送方
- `UPDATE`: 通告新路径(或者撤销原路径)
- `KEEPALIVE`：在没有更新时保持连接，也用于对OPEN请求确认
- `NOTIFICATION`: 报告以前消息的错误，也用来关闭连接

当AS3网关路由器3a向AS2的网关路由器2c通告路径： AS3,X

![image-20240215163635186](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240215163635186.png)





#### 策略

路由器可能获得一个网络前缀的多个路径，路由器必须进行路径的选择，路由选择可以基于：
1. 本地偏好值属性: 偏好策略决定
2. 最短AS-PATH ：AS的跳数
3. 最近的NEXT-HOP路由器:热土豆路由:选择具备最小内部区域代价的网关作为往X的出口（如：2d选择2a，即使往X可能有比较多的AS跳数）：不要操心域间的代价！
4. 附加的判据：使用BGP标示



当一个网关路由器接收到了一个路由通告, 使用输入策略来接受或过滤（accept/decline.）

- 过滤原因例1：不想经过某个AS，转发某些前缀的分组
- 过滤原因例2：已经有了一条往某前缀的偏好路径

策略也决定了是否向它别的邻居通告收到的这个路由信息

### ICMP协议

ICMP通常被认为是lP的一部分，但从体系结构上讲它位于IP之上，因为ICMP报文是承载在IP分组中的。这就是说，ICMP报文是作为IP有效载荷承载的，

ICMP报文有**一个类型字段和一个编码字段**，并且包含引起该ICMP报文首次生成的IP数据报的首部和前8个字节(以便发送方能确定引发该差错的数据报)。

ICMP**消息类型**

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240426224029128.png" alt="image-20240426224029128" style="zoom: 50%;" />



- ICMP 协议在实际传输中的数据包结构：`20 字节 IP 首部 + 8 字节 ICMP 首部 + 1472 字节<数据大小> 38 字节`；
- ICMP报文格式：`IP 首部(20 字节) + 8 位类型 + 8 位代码 + 16 位校验和 + (不同的类型和代码，格式也有所不同)`。

#### ping

众所周知的ping程序发送一个ICMP类型8编码0的报文到指定主机。看到回显(echo)请求，目的主机发回一个类型0编码。的ICMP回显回答

![预览大图](https://data.educoder.net/api/attachments/582265)

#### Traceroute

Traceroute程序允许我们跟踪路由。

!!! note "这里的两个原理还是得仔细想一下"

**如何获得路径**

Traceroute是用ICMP报文来实现的，向目的地主机发送一系列普通的IP数据报。

这些数据报的每个携带了一个具有不可达UDP端口号的UDP报文段。

第一个数据报的TTL为1，第二个的TIL为2，第三个的TTL为3，依次类推。

该源主机也为每个数据报启动定时器。当第n个数据报到达第n台路由器时，第n台路由器观察到这个数据报的TTL正好过期。根据IP协议规则，路由器丢弃该数据报并发送一个ICMP告警报文给源主机(类型11编码0)。该告警报文包含了路由器的名字和它的IP地址。当该ICMP报文返回源主机时，源主机从定时器得到往返时延，从ICMP报文中得到第n台路由器的名字与IP地址。

**什么时候停止？**

Traceroute源主机是怎样知道何时停止发送UDP报文段的呢?前面讲过源主机为它发送的每个报文段的TTL字段加1。因此，这些数据报之一将最终沿着这条路到达目的主机。因为该数据报包含了一个具有不可达端口号的UDP报文段，该目的主机将向源发送一个端口不可达的ICMP报文(类型3编码3)。当源主机收到这个特别的ICMP报文时，知道它不需要再发送另外的探测分组。





### `SDN`

 `software-defined networking`软件定义网络



垂直集成>昂贵、不便于创新的生态
分布式、固化设备功能==网络设备种类繁多

#### 架构

网络操作系统实现控制平面功能

通过南向接口，把流表算出来、改变流表就可以了。这样网络操作系统可以跑各种各样的网络应用

之前每个路由器计算局部地图

网络是可编程的，底层硬件标准化，网络设备软件化

![image-20240201121228823](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201121228823.png)

- 网络设备数据平面和控制平面分离

- 数据平面-分组交换机

  - 将路由器、交换机和目前大多数网络设备的功能进一步抽象成：按照流表（由控制平面设置的控制逻辑）进行PDU（帧、分组）的动作（包括转发、丢弃、拷贝、泛洪、阻塞）
  - 统一化设备功能：SDN交换机（分组交换机），执行控制逻辑

  

- 控制平面-控制器+网络应用

  - 分离、集中
  - 计算和下发控制逻辑：流表

#### OpenFlow `match+action`模式

可以实现路由器、交换机、防火墙、负载均衡设备等功能

基于南向API（例如OpenFlow），SDN控制器访问基于流的交换机

通用转发: 简单的分组处理规则

- 模式: 将分组头部字段和流表进行匹配
- 行动：对于匹配上的分组，可以是丢弃、转发、修改、将匹配的分组发送给控制器
- 优先权`Priority` : 几个模式匹配了，优先采用哪个，消除歧义
- 计数器`Counters`: #bytes 以及#packets

**抽象**

- 路由器
  • match: 最长前缀匹配
  • action: 通过一条链路转发

- 交换机
  • match: 目标MAC地址
  • action: 转发或者泛洪
- **防火墙**
  • match: IP地址和TCP/UDP端口号
  • action: 允许或者禁止
- NAT
  • match: IP地址和端口号
  • action: 重写地址和

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201222746295.png" alt="image-20240201222746295" style="zoom:50%;" />
