# 传输层 | `Transport Layer`

!!! bug
	TCP和UDP 的c语言实现



## 原理

进程与进程之间 以message为单位的通讯

### 复用、解复用

段 段的头部取出来

字节流的服务，不保证段与段之间的标识

传输协议运行在端系统
发送方：将应用层的报文分成报文段，然后传递给网络层
接收方：将报文段重组成报文，然后传递给应用层

传输层使用同一个socket为指定的台做传输

> 两个家庭互相寄信的例子
>
> 把源端的信件一团交给postman
>
> 送到目标邮箱，从信箱里吧信件分装 -->解复用

### RDT 可靠数据传递

IP是不可靠的，TCP可以变成可靠的

在下层服务不可靠的情况下，向上保证可靠

![image-20240130233920207](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130233920207.png)

FSM 有限状态机

引起状态变迁的事件 and 状态变迁时采取的动作

相应和激励

上层元语+本层动作+下层服务



### 停止等待协议

#### Rdt1.0: 在可靠信道上的可靠数据传输

下层信道完全可靠

发送方和接收方的FSM

发送方将数据发送到下层信道

接收方从下层信道接收数据



#### Rdt2.0：具有比特差错的信道

下层信道可能会出错：将分组中的比特翻转（01互换）、用校验和来检测

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131000805343.png" alt="image-20240131000805343" style="zoom:50%;" />

问题：怎样从差错中恢复：

确认(ACK)：接收方确认 - 什么都不做
否定确认( NAK): 接收方声明出错，发送方重传分组

#### rdt2.1 ACK/NAK出错（停等协议

加入分组序号

对于发送方：每个分组中加入序号，不是ACK就重新发

接受方：检验和正确发送ACK，再判断序号；检验和错误发送NAK

!!! note
	用一位表示分组的序号
	没有确认的确认，如果下一次传了不同的分组，说明确认已经被发送方收到

#### rdt2.2：FREE NAK 无NAK的协议

> 郑老师有趣的例子：
>
> ：你说这个人漂不漂亮
>
> ：她很老实

对ACK做编号，对前一个分组ACK相当于当前分组反向确认



#### rdt3.0：具有比特差错和分组丢失的信道

发送方**超时重传**

重传时间略大约正常往返的时间

停等协议在信道容量大的时候效率较低

> 理解
> 合肥到北京高速公路：一个车过了到了北京才允许下一个车进入高速；但高速可以容纳很多车

adaptive 动态超时时间设置：过早超时可以运行，但效率低

![image-20240131010457267](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131010457267.png)



### 流水线协议 `GBN`&`SR`

未得到对方确认，不停打分组，用多个bit表示分组



回退N步(GBN)和选择重传(SR)



滑动窗口(slide window)协议

| 发送缓冲区 |        | 协议名称         | 最大n     |
| ---------- | ------ | ---------------- | --------- |
| SW = 1     | RW = 1 | stop and waiting |           |
| SW > 1     | RW = 1 | GBN              | $2^n -1$  |
| SW > 1     | RW > 1 | SR               | $2^{n-1}$ |

发送缓冲区
  形式：内存中的一个区域，落入缓冲区的分组可以发送

发送窗口是发送缓冲区的一个子集

![image-20240131011636831](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131011636831.png)

每发送一个分组，前沿前移一个单位

得到确认一个分组，后沿前移一个单位，不能够超过前沿

缓冲区大小：最大前沿-最小后沿



GBN go back n - 接收方缓冲区为1；顺序到来最高的发确认，累积确认；只维护一个定时器

SR selective repeat - 非累积确认；对到来的分组逐一确认；维护每一个点的定时器



异常情况

- 传送分组在传送中丢失或出错
- 接收方确认没有收到

GBN 回到最小次序的分组，go back 到没有确认的点，重新发送后续

SR 单独发送没有收到的

![image-20240131015308004](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131015308004.png)

![image-20240131015418519](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131015418519.png)

滑动窗口的滑动，低序号到来，高序号提前到来要缓存





#### 适用范围

- 出错率低：比较适合GBN，出错非常罕见，没有必要用复杂的SR，为罕见的事件做日常的准备和复杂处理
- 链路容量大（延迟大、带宽大）：比较适合SR而不是GBN，一点出错代价太大



### 拥塞控制 | `congestion control`

太多的数据需要网络传输，超过了网络的处理能力



#### 表现：丢失；延迟

分组丢失(路由器缓冲区溢出)

分组经历比较长的延迟(在路由器的队列中排队)

不加控制，加速拥塞

> 选中一条数据报，点击**统计（ Statistic s）-> TCP 流图形->时间序列（ Stevens ）**，观察图形。判断此文件中是否有重传的区段（序列号一直增大则无，反之则有）



#### 原因

- 场景1

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131191801624.png" alt="image-20240131191801624" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131191657334.png" alt="image-20240131191657334" style="zoom:50%;" />

- 场景2：有限缓存；超时重传的比例增加

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131191831998.png" alt="image-20240131191831998" style="zoom:50%;" />

- 场景3：被抛弃的分组在拥塞的时候已经穿过了一个或若干个路由

![image-20240131192304829](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131192304829.png)







#### 代价

- 延迟高

- 拥塞的时候灌入速率要快

> 开洗衣店，需要返工比例高，洗衣服的速度提高才能保证完成任务

- 发出了很多没有必要的，因为超时而重传的分组，加速拥塞

- 当分组丢失时，任何“关于这个分组的上游传输能力”都被浪费了





#### 控制手段

- 网络提供信息给端系统，控制速率

- 端系统自己判断；段超时、收到冗余ACK



`ABR: available bit rate`:

“弹性服务”

- “轻载”：发送方使用可用带宽
- 发送方拥塞：速度限制到一个最小保障速率上



`RM` (资源管理) 信元:

网络是否发生拥塞的标志位

 由发送端发送,在数据信元中间隔插入
 RM信元中的比特被交换机设置(“网络辅助”)

- `NI bit: no increase inrate` (轻微拥塞)速率不要增加了

- `CI bit: congestion indication` 拥塞指示 
- ER (explicit rate)字段：发送端发送速度因此是最低的可支持速率

通过反馈方式让源主机知道最小的带宽





## 协议 Protocol

### UDP

**User Datagram Protocol [RFC 768]（用户数据报协议）**

实时性

可靠性和实时性的对立统一

无连接、不可靠、无流量控制、无拥塞控制

**不需要握手**，头部占比小开销小，简单



应用于：

- 流媒体（丢失不敏感，速率敏感、应用可控制传输速率）
- DNS
- SNMP

#### 报文

1. **8字节头部**——2字节源端口号、2字节目的端口号、数据长度（包括头部）、校验和EDC。
2. **报文部分**——校验和出错后全部丢掉。

以`datagram`为单位

- 源ip + port 

- 发送报文

- 目标ip + port

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130231654238.png" alt="image-20240130231654238" style="zoom:50%;" />



细分网络层的服务 

变成进程到进程

不可靠变成了可靠

![image-20240130231125338](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130231125338.png)

![预览大图](https://data.educoder.net/api/attachments/581703)

#### UDP校验和

[UDP的校验和计算](https://blog.csdn.net/ethan0ly/article/details/119047714)

[关于UDP的检验和计算](https://www.cnblogs.com/roccoshi/p/13033014.html)

![预览大图](https://data.educoder.net/api/attachments/581700)

发送方：

- 将报文段的内容视为16比特的整数
- 校验和：报文段的加法和（1的补运算）
- 发送方将校验和放在

接收方：

- 计算接收到的报文段的校验和

- 检查计算出的校验和与校验和字段的内容是否相等：

  - 不相等–--检测到差错

  - 相等–--没有检测到差错，但也许还是有差错残存错误

注意：当数字相加时，在最高位的进位要回卷，再加到结果上



??? bug
    发送方取反
    校验范围+校验和
    如果结果16bit全是1，则不出现错误；否则出现错误

#### 区别

UDP 和 TCP 协议的主要区别是两者在如何实现信息的可靠传递方面不同。

TCP 协议中包含了专门的传递保证机制，当数据接收方收到发送方传来的信息时，会自动向发送方发出确认消息。发送方只有在接收到该确认消息之后才继续传送其它信息，否则将一直等待直到收到确认信息为止。

与 TCP 不同，UDP 协议并不提供数据传送的保证机制。如果在从发送方到接收方的传递过程中出现数据包的丢失，协议本身并不能做出任何检测或提示。因此，通常人们把 UDP 协议称为不可靠的传输协议。


### TCP

传输控制协议 **reliable**:不重复、不乱序、不丢失、不出错



#### TCP报文

`packet`为单位

`socket`是一个整数 记录四元组：本地ip+port 对方ip+port 进程PID



message + 本地port + 对方 port 形成TCP数据报

再加上本地 ip + 对方ip 形成IP数据报文

![预览大图](https://data.educoder.net/api/attachments/581054)

-  复用

![image-20240130220235305](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130220235305.png)

- 解复用

![image-20240130230254626](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130230254626.png)



![image-20240130231052510](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240130231052510.png)

#### 超长报文

??? note "注意"
	字节流的服务，不提供报文的界限，需要靠应用进程自己维护 





![MTU 与 MSS](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1282f9ef4d00f3cf14ccfba9aef7f7c6.png)

![image-20240131121759203](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131121759203.png)



MTU 最大交换单元：一个网络包的最大长度，以太网中一般为 1500 字节；

MSS 最大报文段：除去 IP 和 TCP 头部之后，一个网络包所能容纳的 TCP 数据的最大长度；



在以太网中，最大传输单元（MTU）为 1500 个字节，在一个 IP 包中，去除 IP 包头的 20 个字节，可以传输的最大数据长度为 1480 个字节。在 TCP 包中，去除 20 个 TCP 包头，**可以传输的最大数据段为 1460 个字节**。因此，当数据超过最大数据长度时，将对该数据进行分片处理，在 IP 包头中会看到有多个片在传输，但标识号是相同的，表示是同一个数据包。 

HTML 文件相当长时，例如： 4861 字节太大，一个 TCP 数据包不能容纳。因此，单个 HTTP 响应消息由 TCP 分成几个部分，每个部分包含在单独的 TCP 报文段中，如下图：长度为 4861 的报文被分为长度分别为 1440，1440，1440，541 的 4 个 TCP 段，编号分别为 8715，8716，8718，8719 。

![image-20240220112530054](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240220112530054.png)

- 序号：数据部分第一个字节在整个字节流的偏移量`offset`进行编号

- 确认号：`ACK number `累计确认；例如ACK555表示554及之前都已经收到，表示对number及以后字节的期待

> TCP's error-recovery mechanism is probably best categorized as a hybrid of GBN  and SR protocol

乱序报文段处理没有规定

???+note "为什么IP层有分片，TCP还要分段"
	[动图图解 | TCP/IP到底是怎么分片的？-CSDN博客](https://blog.csdn.net/coderising/article/details/118384130)<br>
	[TCP的分片](https://blog.csdn.net/nswdiphone6/article/details/115695003)<br>
	因为 IP 层本身没有超时重传机制，它由传输层的 TCP 来负责超时和重传。<br>
    当接收方发现 TCP 报文（头部 + 数据）的某一片丢失后，则不会响应 ACK 给对方，那么发送方的 TCP 在超时后，就会重发「整个 TCP 报文（头部 + 数据）」。<br>
    因此，由 IP 层进行分片传输，是非常没有效率的。<br>
    所以，为了达到最佳的传输效能 TCP 协议在建立连接的时候通常要协商双方的 MSS 值，当 TCP 层发现数据超过 MSS 时，则就先会进行分片，当然由它形成的 IP 包的长度也就不会大于 MTU ，自然也就不用 IP 分片了。<br>
    ![握手阶段协商 MSS](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/b30d3cb43b0f1561c93b6e2df7ac561b.png)<br>
    经过 TCP 层分片后，如果一个 TCP 分片丢失后，进行重发时也是以 MSS 为单位，而不用重传所有的分片，大大增加了重传的效率。<br>





#### 建立连接(三次握手)

双方知道和对方通信；要准备一些必要的资源

[TCP的三次握手详解](https://blog.csdn.net/weixin_48684274/article/details/108263608)

> 发送方：老铁，可以听得到我说话吗，老铁。
>
> 接收方：可以听到，你听得到吗？
>
> 发送方：听到了，那我开始说正事了。

![预览大图](https://data.educoder.net/api/attachments/566278)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202008271630393.png)

**第一次握手**

探测是否可以进行通信，告诉客户端 `seq X`

客户端将标志位 SYN 置为 1 ，随机产生一个值`SEQ = X`，并将该数据包发送给服务器，客户机进入 SYN_SENT 状态，等待服务器确认；

![预览大图](https://data.educoder.net/api/attachments/581480)

**第二次握手**

是接收方返回给发送方的，可以明确一些信息;
确认X，告诉服务器`seq Y`；相当于把确认和`seq Y` 捎带发送了

服务器收到数据包后由标志位`SYN = 1`，知道客户端请求建立连接，服务器将标志位 SYN 和 ACK 都置为 1 ，`ACK = X + 1`，随机产生一个值`SEQ = Y`，并将该数据包发送给客户端以确认连接请求，服务器进入 `SYN_RCVD` 状态；

![预览大图](https://data.educoder.net/api/attachments/581484)

**第三次握手** 

确认`seq Y`，Y是server维护的滑动窗口的下沿；和数据传递同步进行

客户端收到确认后，检查 ACK 是否为`X + 1`，ACK 是否为 1 ，如果正确则将标志位 ACK 置为 1 ，`ACK = Y + 1`，并将该数据包发送给服务器，服务器检查 ACK 是否为`K + 1`，ACK 是否为 1 ，如果正确则连接建立成功，客户端和服务器进入 ESTABLISHED 状态。

![预览大图](https://data.educoder.net/api/attachments/581485)

握手过程中传送的包里不包含数据，三次握手完毕后，客户端与服务器才正式开始传送数据。理想状态下，TCP 连接一旦建立，在通信双方中的任何一方主动关闭连接之前，TCP 连接都将被一直保持下去。



服务器把老的连接当成新的连接

初始序号的选择；与时钟的第一个32位有关；

![预览大图](https://data.educoder.net/api/attachments/581058)

???+note "重要字段"
    1. **序号(sequence number)**：seq序号，占32位，用来标识从TCP源端向目的端发送的字节流，发起方发送数据时对此进行标记。 <br>
    2. **确认号（acknowledgement number）**：ack序号，占32位，只有ACK标志位为1时，确认序号字段才有效，ack=seq+1。 <br>
    3. **标志位（Flags）**：共6个，即URG、ACK、PSH、RST、SYN、FIN等。具体含义如下： <br>
        - `SYN`：发起一个新连接。 <br>
        - `ACK`：确认序号有效。（为了与**确认号ack**区分开，我们用大写表示）只有当 `ACK=1` 时，确认号字段才有效；当 `ACK=0` 时，确认号无效。 <br>
        - `RST`：重置连接。<br>
        - `FIN`：释放一个连接。<br>
        - `PSH`：接收方应该尽快将这个报文交给应用层。<br>
        - `URG`：紧急指针（urgent pointer）有效。<br>
        - `CWR`：(拥塞窗口减小)缓存区已满或者拥挤，通信双方都应该降低传输的速率。<br>



??? bug "实验注意"
    像Wireshark这种工具，通常显示的都是相对序列号/确认号，而不是实际序列号/确认号，相对序列号/确认号是和TCP会话的初始序列号相关联的。<br>
    比如，在“包1”中，最初的相对序列号的值是0，但是最下方面板中的ASCII码显示真实序列号的值是0xf61c6cbe，转化为10进制为4129057982<br>
	可以选择Wireshark菜单栏中的 **Edit** -> **Preferences** ->**protocols** ->**TCP**，去掉**Relative sequence number**后面勾选框中的√即可<br>
    ![img](https://img-blog.csdn.net/20140725092301017?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTE5ODgxMDI5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)<br>



#### 关闭连接(四次挥手)

分成两个方向分别拆除；

连接释放是不可靠的

 启动一个定时器，如果定时器结束之前没有数据传递，那么通信就真正关闭了

![image-20240131191317844](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131191317844.png)





#### 超时定时器

设置不合理效率较低，重复发送

- 如果比较集中，就可以设置一个具体的数值，例如$\mu + 4\sigma$​处；如局域网
- 如果数值不确定，那么adaptive动态调整；定期测量往返延时

`adam`算法一阶动量计算

$$
EstimatedRTT = (1-\alpha) \times EstimatedRTT + \alpha\times SampleRTT 
$$

- 指数加权移动平均
- 过去样本的影响呈指数衰减
- 推荐值：$\alpha = 0.125$



重发像SR，把最老的段重传；

累积确认





快速重传

最小的ACK没有收到，接收方三次收到比期望序号大的ACK，这个时候即使没有到预定的超时重传时间，也要重传

![image-20240131171424313](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131171424313.png)

![image-20240131171617244](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131171617244.png)

#### 流量控制 | Flow control

!!! note "**遏制发送方的速率**"

捎带

接收方控制发送方，不让发送方发送的太多、太快以至于让接收方的缓冲区溢出

TCP 通过让发送方维护一个称为接收窗口(`receive window`)的变量来提供流量控制





反馈机制

![image-20240131180153804](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131180153804.png)

**接收方**

接收方在其向发送方的TCP段头部的`rwnd`字段“通告”其空闲`buffer`大小

缓存中的可用的空间

$$
V = RcvWindow = RcvBuffer-[LastByteRcvd - LastByteRead]
$$
![image-20240131180428780](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131180428780.png)

**发送方**

- 限制未确认(`inflight`)字节的个数≤接收方发送过来的`rwnd` 值

- 保证接收方不会被淹没

$$
LastByteSent - LastByteAcked \geq rwnd
$$



问题：TCP只在有数据发或者确认的时候才发报文，所以当B的`rcvd = 0`时候，A无法知道

为了解决这个问题， TCP 规范中要求:当主机 B 的接收窗口为0 时，主机 A 继续发送只有一个字节数据的报文段。这些报文段将会被接收方确认。最终缓存将开始清空，并且确认报文里将包含一个非0 的`rvnd`值。



??? note "UDP"
	UDP没有流量控制，多发的包将丢失




#### 拥塞控制 | Congestion control

TCP/IP 复杂性放在网络边缘，靠端系统感知

TCP 拥塞控制常常被称为加性培、乘性减(`Additive-Increase Multiplicative-Decrease , AIMD`)

##### **如何检测拥塞**

- 某个段超时了（丢失事件）：拥塞
  - 超时时间到，某个段的确认没有来
    原因1：网络拥塞（某个路由器缓冲区没空间了，被丢弃）**概率大**
    原因2：出错被丢弃了（各级错误，没有通过校验，被丢弃）**概率小**
- 有关某个段的3次重复ACK：轻微拥塞



##### 控制策略

维持一个拥塞窗口的值：`CongWin`动态的，是感知到的网络拥塞程度的函数

发送端限制已发送但是未确认的数据量（的上限）:
$$
LastByteSent-LastByteAcked \le CongWin
$$

$$
rate = \frac{CongWin}{RTT}
$$

 `MSS`最大报文段

> 老师的神奇例子：
>
> 我家有很多酒，测老哥酒量；第一天喝1两，啥事没有；第二天2两，洒洒水啦；第三天4，第四天8两，都莫有问题；
>
> 第五天，1斤6两干趴了。下次就从警戒值8两（16两的一半）开始一点点加
>
> 喝醉——超时
>
> 微醺——3个冗余ACK，进入拥塞避免

- 当$CongWin＜Threshold$, 发送端处于`SS`, 窗口指数性增长.

- 当$CongWin>Threshold$, 发送端处于`CA`, 窗口线性增长.

- 当收到三个重复的ACKs,`Threshold`设置成`CongWin/2`（快速重传）

  $CongWin=Threshold+3$

- 当超时事件发生时`timeout`, $Threshold=CongWin/2$,$CongWin=1 MSS$，进入SS阶段

> SS `slow start`阶段：加倍增加的阶段（每个 RTT)——慢启动阶段
> CA `congestion-avoidance`阶段：线性增加的阶段（每个 RTT)——拥塞避免阶段

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131220146619.png" alt="image-20240131220146619" style="zoom: 67%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131220206546.png" alt="image-20240131220206546" style="zoom: 50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240328091444848.png" alt="image-20240328091444848" style="zoom:50%;" />

发送端控制发送但是未确认的量同时也不能够超过接收窗口，满足流量控制要求
$$
SendWin=min \{ CongWin, RecvWin \}
$$

同时满足拥塞控制和流量控制要求

![image-20240131215546305](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131215546305.png)



吞吐量

$$
T = \frac{\frac{w}{2} + w}{2 \cdot RTT} = \frac{3w}{4\cdot RTT}
$$



TCP 连接的吞吐量公式
$$
平均吞吐量 = \frac{1.22 \times MSS}{RTT \sqrt{L}}
$$
该公式作为丢包率(`L`) 往返时间(`RTT`)和最大报文段长度(`MSS`) 的函数

**TCP Cubic**



##### 公平性

如果K个TCP会话分享一个链路带宽为R的瓶颈，每一个会话的有效带宽为R/K

![image-20240131220718321](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131220718321.png)



-

**证明**

随机选一个点，进入CA阶段，向白线靠近

超时之后，会减少到一半，重复这个过程

之后会逐渐趋近于X=Y这条线路

![image-20240131221103041](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240131221103041.png)
