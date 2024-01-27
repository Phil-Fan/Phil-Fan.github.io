# `Intro`

???+note "各学院开课信息"

    查询CC98近4年有关计网的帖子，总结如下


    === "电气学院"
    
        [2023-2024冬 计算机网络与通信（电院） 期末考试回忆 - CC98论坛](https://www.cc98.org/topic/5799608)
    
        [【教程】推荐一个计算机网络小白向视频 - CC98论坛](https://www.cc98.org/topic/5793620)
    
        [大鹏鸟 - 杨春节老师视角](https://www.cc98.org/topic/5671695)
    
    === "光电   - 《数据通信与计算机网络》"
    
        [22-23期末回忆卷](https://www.cc98.org/topic/5596764)
    
        [21-22春回忆卷](https://www.cc98.org/topic/5301579)
    
        [知识点整理](https://www.cc98.org/topic/5301549)
    
        [20-21回忆卷](https://www.cc98.org/topic/5069360)
    
        [21-22春回忆卷](https://www.cc98.org/topic/5301512)
    
        [22春-管院回忆卷](https://www.cc98.org/topic/5300823)


         期末40
         大作业30
         小作业交两次：第三周第五周交，占30
    
    === "计院"
    
        高分刷王道
    
        [咸鱼喧笔记](https://www.yuque.com/xianyuxuan/coding/gez9yl)
    
        [计算机网络（计网） 2023-2024 回忆卷 - CC98论坛](https://www.cc98.org/topic/5799341)
    
        [计算机网络1-OSI模型 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/Networking/计算机网络1-OSI模型/)
    
        [大三上cs课程经验和资料分享（操作系统、计算机网络、计算机体系结构、汇编与接口、数值分析） - CC98论坛](https://www.cc98.org/topic/5807213)
    
        [计院《计算机网络》复习笔记和选课排雷 - CC98论坛](https://www.cc98.org/topic/5031095)
    
        [《计算机网络》的习题、实验内容、习题和实验的成绩、参考资料 请看本帖子-new - CC98论坛](https://www.cc98.org/topic/4987967)
    
    === "USTC"
    
    === "CS144"
    
        [计算机网络学习总结（中科大计网 & Stanford CS144） - CC98论坛](https://www.cc98.org/topic/5686337)





!!! abstract

​	本笔记基于USTC郑铨老师《计算机网络》课程




## 基本概念

![image-20240122233225413](https://gitee.com/philfan/my-images/raw/master/image-20240122233225413.png)

网络：节点、边的拓扑结构







Bit 信息论中信息量的单位

bit rate 性能指标 

单位 b/s kb/s Mb/s Gb/s



bandwidth 信号具有的频带宽度

数字信道能传送的最高数据率

bit/s



delay 时延

链路bps

$发送时延 = \frac{数据长度}{发送速率}$

$传播时延 = \frac{信道长度}{信道传播速率}$

总时延 = 发送时延+传播时延+处理时延+排队时延



时延带宽积

信道利用率 - 某信道有多少被利用

排队论，信道利用率增大，时延就增大

![image-20240122214414552](https://gitee.com/philfan/my-images/raw/master/image-20240122214414552.png)

- 功能和服务

每一层向上一层提供服务

- 实例

http htp pop3

internet 网络的网络

tier

### internet

- 节点

主机节点：

数据交换节点：转发数据 圆形

链路层交换机、网络层路由器、其它层负载均衡设备



- 边的分类

接入链路

骨干链路



- 协议

  



一个角度

互联网是通过互联设备连在一起的网络的网络

另一个角度

互联网是分布式的互联网进程+为分布式应用提供服务的基础设施

api应用程序接口 socket api



有连接的服务

无连接的服务







主机host=端系统end system

通信链路：传输速率=带宽bps

分组交换设备：转发packets



### 网络边缘 edge

网络应用是网络存在的理由

分布式的应用



- CS模式client-server（主从模式）可扩展性 非线性下降

- 对等模式 peer-peer  请求和提供资源的端变多了、分布式的、迅雷



面向连接的交互方式：交互前分配资源

有连接









### 网络核心 core

数据交换，类似源主机和目标主机之间接入了开关

#### 电路交换

电话网

独享资源、不共享；可以保证性能

没有数据发送资源就会浪费

线路建立的时间长

可靠性不高



##### 分类 分成piece

频分 FDM frequency division multiplexing

时分 TDM time division multiplexing 时隙slot

波分 光纤通讯 WDM wave division multiplexing

![image-20240123105422145](https://gitee.com/philfan/my-images/raw/master/image-20240123105422145.png)

![image-20240123105704164](https://gitee.com/philfan/my-images/raw/master/image-20240123105704164.png)

 每个bit到达接收端都需要有传播延时





#### 分组交换

分成一个个单位packet，传到相邻路由器hop；

经过每一个节点，存储转发

使用链路全部带宽

资源是按需使用、共享性（支持用户多）



延时：排队时间、存储时间

排队：到达速度》输出速率 

缓存用完了会抛弃分组



过度使用会造成网络拥塞





没有固定模式 统计多路复用

![image-20240123113304652](https://gitee.com/philfan/my-images/raw/master/image-20240123113304652.png)

流量强度的网络不可行，所以是0-9



##### 分类

- 数据报网络 datagram - 无连接

不需要握手，每次跳跃都携带目标完整地址，



- 虚电路网络

需要维护呼叫状态

信令





### 网络接入 access

边缘接到核心上

带宽bps bits per second

共享/专用

 



#### 住宅接入：

##### modem

将数据调制在音频信号上、要解调

调幅度、频率、相位

带宽太窄

不需要重新铺基础设施



##### DSL：digital subscriber line



##### 有线电视公司

双向改造

共享带宽



同轴电缆

带宽非对称



##### 电力线可以调制上网



![image-20240123122045769](https://gitee.com/philfan/my-images/raw/master/image-20240123122045769.png)

#### 公司

![image-20240123122830511](https://gitee.com/philfan/my-images/raw/master/image-20240123122830511.png)



点对点连接

总线

环形

星形



#### 无线接入



WAN(Wide Area Network)

LAN(Local Area Network)

MAN(Metropolitan Area Network)

PAN(Personal Area Network)

#### 物理媒体

导引型媒体

![image-20240123123058357](https://gitee.com/philfan/my-images/raw/master/image-20240123123058357.png)

![image-20240123123111306](https://gitee.com/philfan/my-images/raw/master/image-20240123123111306.png)

高琨

单模光纤

多模光纤

光缆



有型介质传的远



非导引型媒体

强度 平方反比，迅速衰减

![image-20240123123348917](https://gitee.com/philfan/my-images/raw/master/image-20240123123348917.png)



### internet结构和ISP



ISP: internet service provider

全连接 scalibity可扩展性差

ICP: internet content provider

谷歌

数据中心机房 离isp较近

![image-20240123235809673](https://gitee.com/philfan/my-images/raw/master/image-20240123235809673.png)

internet结构

tier1 

tier2

regional isp

local isp



### 分组延时、丢失和吞吐量

 延时的原因：输出能力小于到达速率

（用火车过桥来理解）



Traceroute检测程序



#### 节点处理延时



#### 排队延时

流量强度$I = \frac{La}{R}$

L(bits) a到达平均速率，R链路带宽（bps）

流量强度为1，延时无穷大





#### 传输延时：

#### $T = \frac{L}{R}$,L是分组长度，R是链路带宽



#### 传播延时

#### $t = \frac{d}{s}$

`d`链路长度 `s`媒体传播速度

AB距离很远的话，传播延时不能忽略

信道容量

![image-20240125175620523](https://gitee.com/philfan/my-images/raw/master/image-20240125175620523.png)







分组丢失原因

缓冲区有限

满队列后，分组会丢失

丢失可能重传也可能不重传



丢失以后，如果链路是可靠的会由上层重传  



吞吐量 源端和目标端传输速率（有效的





### 协议层次network protocol

计算机采取分层的方式，下层实现功能，每一层通过层间接口向上层服务





#### 服务 垂直层面

底层实体向上层实体提供通信的能力



通过原语`primitive` 来操作

提供什么服务 告诉要使用什么服务



#### 协议 水平层面

对等层的实体`peer entity`在通信过程中遵守的规则集合

报文格式语法、语义、次序、采取的动作

本层协议实现需要依靠下层服务，是为了给上层提供更好的服务



`DU: data unit` 数据单元 

`SAP`服务访问点 区分是哪个上层用户 

`IDU:interface data unit`

`SDU: service data unit`上层传的数据

`PDU: protocol data unit` 协议数据单元 SDU + head

`ICI: interface control information` 

![image-20240125201420011](https://gitee.com/philfan/my-images/raw/master/image-20240125201420011.png)

![image-20240125201113691](https://gitee.com/philfan/my-images/raw/master/image-20240125201113691.png)

套接字





![image-20240125202826044](https://gitee.com/philfan/my-images/raw/master/image-20240125202826044.png)

链路层以帧为单位，相邻两点

网络层端到端传输，源主机到目标主机，以分组为单位

传输层，进程到进程区分，把网络层不可靠服务变成可靠的服务



路由：全局找路





![image-20240125202836339](https://gitee.com/philfan/my-images/raw/master/image-20240125202836339.png)



TCP/IP:应用层、运输层、网际层、网络接口层

OSI：应用层、表示层、会话层、运输层、数据链路层、物理层







## 

