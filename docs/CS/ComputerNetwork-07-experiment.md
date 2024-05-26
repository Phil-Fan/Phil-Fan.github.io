# 计网实验以及探索



## TCP

??? bug "实验注意"
    像Wireshark这种工具，通常显示的都是相对序列号/确认号，而不是实际序列号/确认号，相对序列号/确认号是和TCP会话的初始序列号相关联的。<br>
    比如，在“包1”中，最初的相对序列号的值是0，但是最下方面板中的ASCII码显示真实序列号的值是0xf61c6cbe，转化为10进制为4129057982<br>
	可以选择Wireshark菜单栏中的 **Edit** -> **Preferences** ->**protocols** ->**TCP**，去掉**Relative sequence number**后面勾选框中的√即可<br>
    ![img](https://img-blog.csdn.net/20140725092301017?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTE5ODgxMDI5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)<br>



## Clash给手机提供代理

[使用Clash For Windows与Windows热点共享让你的所有移动设备科学上网 - CC98论坛](https://www.cc98.org/topic/5667186)

1. 确定电脑可以通过clash进行正常连接，或者能通过SSR连接

2. 打开Clash的`Allow Lan` ，这一步是为了让Clash允许局域网连接（在SSR中，则是允许来自局域网的连接）

3. 电脑进入`cmd`，输入`ipconfig`找到电脑自己的IPv4地址，例如`192.168.127.1`

   这里192.168是C类IP，是内网中返回的

4. 看看Clash界面的Port是多少，不用管那个Socks Port。例如，Port是`1125`

   在SSR中，是看本地端口，例如，本地端口是1125

5. 手机或其它设备先连接上电脑win10的自带热点，进入手机 **WiFi** 的详细设置界面

6. 把选项 **代理** 从 **无** 改成 **手动** ，选项 **主机名** 设置为`192.168.127.1`，选项 **代理服务器端口** 改为`1125`，确认即可

   <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/Screenshot%202024-02-02%20at%2000.24.51.jpeg.png" alt="Screenshot 2024-02-02 at 00.24.51.jpeg" style="zoom: 25%;" />

   <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/Screenshot%202024-02-02%20at%2000.25.19.jpeg.png" alt="Screenshot 2024-02-02 at 00.25.19.jpeg" style="zoom: 25%;" />

## 使用“共享文件夹”实现iPhone与PC间文件快速传输

> 参考文献：[如何通过“共享文件夹”实现iPhone与PC间文件快速传输](https://zhuanlan.zhihu.com/p/145540093)

### PC端设置

- 设置读取/写入权限

（1）考虑到信息安全问题，建议将共享用户数量限制为1，根据使用情况自行设定。

（2）完全控制权限慎选。

![img](https://pic1.zhimg.com/80/v2-39f794731fac3c347391bf965fcf9490_1440w.webp)

![img](https://pic3.zhimg.com/80/v2-44103f753f47d507913fe5ab3a66a8c2_1440w.webp)

- 获取IP地址

使用`Win+R`,输入`cmd`,输入`ipconfig`

### 手机端设置

打开iPhone端“文件”——点击右上角三个点——选择“连接服务器”——输入IP地址——点击连接——选择注册用户——输入电脑名称及密码——完成。然后打开“文件”应用，就可以看到共享文件夹了。

![img](https://pic1.zhimg.com/80/v2-5d3c86fd875daf87211ce71fa8e1f548_1440w.webp)



## 静态路由的配置 | 使用GNS3模拟

![预览大图](https://data.educoder.net/api/attachments/510529)

1.路由器的三种模式及切换 

2.路由器配置 IP； 

3.PC 机配置 IP 和网关。



### 路由器的配置

当打开路由器的设备控制台 Console 进行操作时，有三种操作模式。分别是：

- R1 >：用户模式
- R1# ：特权模式
- R1(config)# ：全局配置模式

#### 模式间切换：

1.用户模式（ > ）切换到特权模式（ # ）：使用命令 `enable` 并回车。 

2.特权模式（ # ）切换到全局配置模式（（ config ）#）：使用命令 `config terminal` 并回车：

![img](https://data.educoder.net/api/attachments/510601)

其中，命令可以简写，也可以简写后按 tab 健补全：

![img](https://data.educoder.net/api/attachments/510602)

`exit `返回上一级，`end` 直接退回到特权模式：

![img](https://data.educoder.net/api/attachments/510615)

#### 路由器节点 IP 配置

![预览大图](https://data.educoder.net/api/attachments/878525)

![预览大图](https://data.educoder.net/api/attachments/510574)

```
R1 ( config ) # interface f0/0     ----进入接口
R1 ( config-if ) # ip address 10.0.0.2 255.255.255.0  ----配置 IP 地址
R1 ( config-if ) # no shutdown   ----开启接口

R1 ( config-if ) # end			---- 退出全局配置模式
R1 # write					---- 保存配置
R1 # show ip interface brief  ---- 查看 ip 配置
```

![write](https://data.educoder.net/api/attachments/542779)

![查看ip配置](https://data.educoder.net/api/attachments/510622)

### PC 机配置 IP 和网关

以 PC1 为例，选中 PC1 ，鼠标右键选择 Start：

![img](https://data.educoder.net/api/attachments/878605)

然后鼠标右键选择 console ，打开控制台：

![img](https://data.educoder.net/api/attachments/510640)

使用命令

```shell
ip X.X.X.X（ PC 机 IP 地址） X.X.X.X（网关地址）
save ---- 保存配置
show ip ---- 查看配置
```

![img](https://data.educoder.net/api/attachments/510642)

可以使用 show ip 命令查看 PC 机上配置的 IP 地址：

![img](https://data.educoder.net/api/attachments/510673)

通过 save 保存配置：

![img](https://data.educoder.net/api/attachments/542782)

### 静态路由

静态路由是一种需要管理员手动配置的特殊路由。静态路由比动态路由使用更少的带宽，并且不占用 CPU 资源来计算和分析路由更新。但是，当网络发生故障或者拓扑发生变化后，静态路由不会自动更新，必须手动重新配置。

#### 静态路由的组成

静态路由主要包括 5 个主要的参数：目的 IP 地址和子网掩码、出接口和下一跳 IP 地址、优先级。

1、目的 IP 地址/子网掩码

目的 IP 地址就是路由要到达的目的主机或者目的网络的 IP 地址，子网掩码就是目的地址所对应的子网掩码。当目的地址和子网掩码全为 0 的时候，表示静态缺省路由（默认路由）。

2、出接口和下一跳地址

根据不同的出接口类型，在配置静态路由的时候，可以选择出接口的方式，也可以指定下一跳 IP 地址，还可以同时指定出接口和下一跳 IP 地址。

- 对于点对点类型的接口，只需指定出接口。当然，也可以同时指定下一跳 IP 地址，但这时已没有意义。
- 对于 NBMA 类型的接口，只需配置下一跳 IP 地址，当然，也可以同时指定出接口。
- 对于广播类型的接口和 VT（ virtual-template ）接口，必须指定下一跳 IP 地址，有些情况下还需要指定出接口。

3、静态路由的优先级

对于不同的静态路由，可以为它们配置不同的优先级。优先级值越小表示静态路由的优先级越高。配置到达相同目的地的多条静态路由，如果指定相同的优先级，则可实现负载分担；如果指定不同优先级，则可以实现路由备份。

![image-20240307090222479](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240307090222479.png)

![预览大图](https://data.educoder.net/api/attachments/519532)

## 对zdty体测预约进行抓包分析

一个平平无奇的周日晚上，在上课的PhilFan收到Fufu在群里发的消息

~~"zdty真垃圾，都是明文传"~~

顺带传了一张预约好的体测照片，不过这个时间段不是还没有开放咩？？

于是PhilFan决定稍微抓抓看，~~看看有多垃圾~~，复习以下刚学到的HTTP抓包技能。~~（世界是一个巨大的草台班子~~


另外需要注意的是，现在已经没有必要使用代码进行预约了，因为app预约也不麻烦（就是玩一下hhh



!!! note "**以下行为均以学习计网知识为目的，模仿带来的任何风险由使用者自己承担，请注意保护好自己的隐私信息**"



### 第一步——如何抓包手机APP

- 第一种是用电脑给手机提供热点，相当于电脑当作了手机的流量来源，直接在电脑上使用抓包工具（如`wireshark`等）进行分析即可。

  ![image-20240318085112013](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318085112013.png)

- 第二种我也没有试过，直接使用手机端的抓包APP进行分析。



### 第二步——找到对应的报文

打开wireshark，选择HTTP进行筛选

为了不抓到其他无关信息，还是**尽量关一下其他网站和APP**

打开zdty，体测预约，看到类似如下信息说明可以抓到

![image-20240318082144366](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318082144366.png)

以4月12日体测为例，点开体测预约，我们发现有一个报文

![image-20240318082347175](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318082347175.png)

> **由课上知识我们知道**：
>
> HTTP报文由请求行、请求头、空白行(`\r\n`)、请求体
>
> 请求行由三部分构成：第一部分说明请求类型为 get 方法请求，第二部分（用/分开）是资源 URL，第三部分说明使用的是 HTTP1.1 版本。

很奇怪的是，这里我们看到这个GET请求的URL，直接将token和日期什么的进行明文传递了。

（朴素认知下，这是不是意味着只要嗅探到你的浙大体艺预约报文，就可以获得你的token，~~进而可以取消你的预约~~）

![image-20240318082934711](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318082934711.png)

分析上图我们可以发现请求头的一些信息，重复刚才的步骤多次可以找到一定规律

- id:3325（应该是体测时间的排序，且相邻时间数字也是相邻的）
- testDate：体测的日期
- timeSolt：体测的时间段
- jToken：不太懂具体是什么作用，推测是进行用户的识别
- __：不清楚具体作用，推测为时间戳。

再试着点一次预约，我们发现了一个新的报文

![image-20240318083929415](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318083929415.png)

分析这个请求的URL，发现多了几个参数

- testPointName：紫金港田径场体测中心（应该是体测地点，~~也可以改成快乐星球~~
- tel：你的电话
- periodId：学年，这次应该是2024

其实到找到你的token，知道你要预约的时间段和年份，就可以抓了。

??? bug "没有搞懂的地方"
	浙大体艺是用什么框架<br>
	token,cookie,session,cache的区别
### 第三步——使用代码进行报文模拟

这一步其实就没有什么难度了

相当于你只需要知道这个URL，对这个URL发GET请求就可以了

~~询问gpt就行了~~

- 使用curl命令
- 使用PowerShell 
- 使用Python的`request`库即可

注意要将刚才的信息抓下来填好

```python
# 示例
import requests

BASE_URL = "http://tyys.zju.edu.cn"
JSESSIONID = ""
JTOKEN = ""
TEL = ""

def schedule_appointment(schedule_id, test_date, time_slot_id, test_point_name="快乐星球", test_option_id="", period_id="2024"):

    url = f"{BASE_URL}/pft/app/schedule/student/event/submit"
    params = {
        "scheduleId": schedule_id,
        "testPointName": test_point_name,
        "testDate": test_date,
        "timeSoltId": time_slot_id,
        "testOptionId": test_option_id,
        "tel": TEL,
        "periodId": period_id,
        "jToken": JTOKEN,
    }
    cookies = {
        "JSESSIONID": JSESSIONID
    }
    response = requests.get(url, params=params, cookies=cookies)
    print(response.status_code)
    print(response.text)
    
# Example usage
schedule_appointment("3322", "2024-04-12", "13:30-14:00")
```

可以发现，我的体测地点变成了快乐星球（😂

![d519771d06acb8610067b01d27799f0](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/d519771d06acb8610067b01d27799f0.jpg)

同理，可以抓到取消预约的URL

其中`scheduledId`参数需要获取"我的预约"列表，再抓取响应报文获得

```python
def cancel_appointment(scheduled_id):
    url = f"{BASE_URL}/pft/app/schedule/student/my/undo"
    params = {
        "scheduledId": scheduled_id,
        "jToken": JTOKEN
    }
    response = requests.get(url, params=params)
    print(response.status_code)
```

## Kali配置与使用

[Kali Linux | Penetration Testing and Ethical Hacking Linux Distribution](https://www.kali.org/)

[Kali虚拟机安装，设置中文等详细教程，Linux最新免镜像版_kali安装中文语言包-CSDN博客](https://blog.csdn.net/l2872253606/article/details/123592717)





### Nmap

Nmap有四种基本功能：「端口扫描」、「主机探测」、「服务识别」和「系统识别」

#### 端口扫描

```
nmap 192.168.1.1
nmap 192.168.1.1 -p-
nmap 192.168.1.1 -p 22
nmap ip/子网掩码 //网段扫描

nmap ip -p 端口号
nmap ip -p 范围
```



> 例题
>
> 访问本题请通过本地运行 ssh user@10.214.160.13 -p 10802 -D 10899 -N，并输入密码 sbus 来开启在本机 10899 端口的 SOCKS5 服务，以下所有域名均应在 SOCSK5 代理后才可访问(可以使用 proxychains4 等工具)。 对于无法直接将域名传入代理服务、必须事先解析的工具，这里提供题目中域名的IP: zju.tools(192.168.192.3), attackme.zjupy.trade(192.168.192.8) AAA web5 端口扫描与目录爆破 (part1)
>
> Q: 如何拿到flag? A:  1. 请扫描 zju.tools 服务器, 找出这台服务器上ssh的端口    ps:显然我没有把ssh开在标准端口, 以及, 为了不给zjutools服务器带来太大压力orz, 请在9000~11000之间扫   2. 请访问 http://192.168.192.8:[part1扫描出来的端口号]





Nmap所识别的6个端口状态。

open(开放的)

应用程序正在该端口接收TCP 连接或者UDP报文。发现这一点常常是端口扫描 的主要目标。安全意识强的人们知道每个开放的端口 都是攻击的入口。攻击者或者入侵测试者想要发现开放的端口。 而管理员则试图关闭它们或者用防火墙保护它们以免妨碍了合法用户。 非安全扫描可能对开放的端口也感兴趣，因为它们显示了网络上那些服务可供使用。

closed(关闭的)

关闭的端口对于Nmap也是可访问的(它接受Nmap的探测报文并作出响应)， 但没有应用程序在其上监听。 它们可以显示该IP地址上(主机发现，或者ping扫描)的主机正在运行up 也对部分操作系统探测有所帮助。 因为关闭的关口是可访问的，也许过会儿值得再扫描一下，可能一些又开放了。 系统管理员可能会考虑用防火墙封锁这样的端口。 那样他们就会被显示为被过滤的状态，下面讨论。

filtered(被过滤的)

由于包过滤阻止探测报文到达端口， Nmap无法确定该端口是否开放。过滤可能来自专业的防火墙设备，路由器规则 或者主机上的软件防火墙。这样的端口让攻击者感觉很挫折，因为它们几乎不提供 任何信息。有时候它们响应ICMP错误消息如类型3代码13 (无法到达目标: 通信被管理员禁止)，但更普遍的是过滤器只是丢弃探测帧， 不做任何响应。 这迫使Nmap重试若干次以访万一探测包是由于网络阻塞丢弃的。 这使得扫描速度明显变慢。

unfiltered(未被过滤的)

未被过滤状态意味着端口可访问，但Nmap不能确定它是开放还是关闭。 只有用于映射防火墙规则集的ACK扫描才会把端口分类到这种状态。 用其它类型的扫描如窗口扫描，SYN扫描，或者FIN扫描来扫描未被过滤的端口可以帮助确定 端口是否开放。

open|filtered(开放或者被过滤的)

当无法确定端口是开放还是被过滤的，Nmap就把该端口划分成 这种状态。开放的端口不响应就是一个例子。没有响应也可能意味着报文过滤器丢弃 了探测报文或者它引发的任何响应。因此Nmap无法确定该端口是开放的还是被过滤的。 UDP，IP协议， FIN，Null，和Xmas扫描可能把端口归入此类。

closed|filtered(关闭或者被过滤的)

该状态用于Nmap不能确定端口是关闭的还是被过滤的。 它只可能出现在IPID Idle扫描中。
