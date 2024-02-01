# 网络层 | Network Layer



## 原理

### 服务

- 在发送主机和接收主机对之间
  传送段（segment）
- 在发送端将段封装到数据报中
- 在接收端，将段上交给传输层
  实体



- 转发：通过单个路口；分组从路由器的输入接口转发到合适的输出接口
- 路由：规划源到目标的路线；全局功能

> 路由：导航路径
>
> 转发：地铁站各个出口，acbd出口就是端口

端到端end to end

源主机到目标主机、best evil尽力而为

> 尽力而为 = 什么都不保证 = 开摆

IP没有连接建立的功能





对于单个数据报的服务:

- 可靠传送
- 延迟保证，如：少于40ms的延迟

对于数据报流的服务:

- 保序数据报传送
- 保证流的最小带宽
- 分组之间的延迟差

![image-20240201121705007](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201121705007.png)



### 数据平面 转发 - 本地功能

本地，每个路由器功能

数据平面根据路由表对数据进行转发

决定从路由器输入端口到达的分组如何转发到输出端口

- 转发功能：
  - 传统方式：基于目标地址+转发表
  - SDN方式：基于多个字段+流表

泛洪——一传十十传百

### 控制平面 路由 - 全局功能

分布式的实现

控制平面计算路由表

- 2个控制平面方法:
  - 传统的路由算法: 在路由器中被实现
  - SDN在远程的服务器中实现



cisco思科



## `Router` 路由器

路由：运行路由选择算法／协议(RIP, OSPF, BGP)-生成路由表

转发：从输入到输出链路交换数据报-根据路由表进行分组的转发

MAC地址，英文全称：`Media Access Control Address`，也叫物理地址、硬件地由网络设备制造商生产时烧录在网卡中



<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201140806254.png" alt="image-20240201140806254" style="zoom:67%;" />

最长前缀匹配`longest prefix matching`

当给定目标地址查找转发表时，采用最长地址前
缀匹配的目标地址表项

### 输入端口缓存

当交换机构的速率小于输入端口的汇聚速率时， 在输入端口可能要排队

排队延迟以及由于输入缓存溢出造成丢失!

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201140951934.png" alt="image-20240201140951934" style="zoom:50%;" />

packet per minute

### `fabric`交换结构

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141044080.png" alt="image-20240201141044080" style="zoom:50%;" />

- memory

在CPU直接控制下的交换
转发速率被内存的带宽限制(数据报通过BUS两遍)
一次只能转发一个分组

- bus

总线竞争: 交换速度受限于总线带宽

1次处理一个分组

- crossbar

Banyan（榕树）网络，crossbar(纵横)和其它的互联网络被开发，将多个处理器连接成多处理器

当分组从端口A到达，转给端口Y；控制器短接相应的两个总线

高级设计：将数据报分片为固定长度的信元，通过交换网络交换



### schedule 调度策略

#### FIFO (first in first out) scheduling

- tail drop: 丢弃刚到达的分组
- priority: 根据优先权丢失/移除分组
- random: 随机地丢弃/移除

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141335251.png" alt="image-20240201141335251" style="zoom:50%;" />

#### 优先权调度

发送最高优先权的分组

先传高优先级的队列中的分组，除非没有(红色传完再传绿色)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141445525.png" alt="image-20240201141445525" style="zoom:50%;" />

#### Round Robin (RR) scheduling

循环扫描不同类型的队列, 发送完一类的一个分组，再发送下一个类的一个分组，循环所有类

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141528684.png" alt="image-20240201141528684" style="zoom:50%;" />

#### Weighted Fair Queuing (WFQ)

一般化的Round Robin

在一段时间内，每个队列得到的服务时间是：$\frac{Wi}{\sigma(Wi)} \times t$，和权重成正比

每个类在每一个循环中获得不同权重的服务量

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201141703167.png" alt="image-20240201141703167" style="zoom:50%;" />

## 网络层协议

### IP协议

地址约定



#### 数据报格式

#### 分片

#### IPV4

#### IPV6

分组处理约定

message

字段头部（head）路过一个路由 TTL -1

减到0的时候，可能路由有问题





### ICMP协议

报告错误

`ping`形成ICMP 



### 路由协议

路径选择

IRP

OSPF

BGP

### `NAT`

`Network Address Translation`网络地址转换

## `SDN`

 `software-defined networking`软件定义网络

网络操作系统实现控制平面功能

通过南向接口

把流表算出来

改变流表就可以了

仅仅改变控制器上的网络应用就可以了

之前每个路由器计算局部地图

现在：领导算出来全局地图下发

`packet switch`

![image-20240201121228823](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240201121228823.png)