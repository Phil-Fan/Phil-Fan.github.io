---
comments: true
---
# 计网实验探索

使用的工具

- Wireshark
- Burpsuite

## TCP

??? bug "实验注意"
    像Wireshark这种工具，通常显示的都是相对序列号/确认号，而不是实际序列号/确认号，相对序列号/确认号是和TCP会话的初始序列号相关联的。<br>
    比如，在“包1”中，最初的相对序列号的值是0，但是最下方面板中的ASCII码显示真实序列号的值是0xf61c6cbe，转化为10进制为4129057982<br>
	可以选择Wireshark菜单栏中的 **Edit** -> **Preferences** ->**protocols** ->**TCP**，去掉**Relative sequence number**后面勾选框中的√即可<br>



## Clash给手机提供代理

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

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-39f794731fac3c347391bf965fcf9490_1440w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-44103f753f47d507913fe5ab3a66a8c2_1440w.webp)

- 获取IP地址

使用`Win+R`,输入`cmd`,输入`ipconfig`

### 手机端设置

打开iPhone端“文件”——点击右上角三个点——选择“连接服务器”——输入IP地址——点击连接——选择注册用户——输入电脑名称及密码——完成。然后打开“文件”应用，就可以看到共享文件夹了。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-5d3c86fd875daf87211ce71fa8e1f548_1440w.webp)


## Proxy

!!! note "什么是代理"
    代理服务器是一种位于用户和互联网之间的服务器，用于转发用户请求。代理服务器的作用是代替用户发送请求，然后将响应返回给用户。代理服务器可以用于访问被封锁的网站、保护用户隐私、提高访问速度等。

### 正向代理

正向代理（forward proxy）：是一个位于客户端和目标服务器之间的服务器(代理服务器)，为了从目标服务器取得内容，客户端向代理服务器发送一个请求并指定目标，然后代理服务器向目标服务器转交请求并将获得的内容返回给客户端。



这种代理其实在生活中是比较常见的，比如访问外国网站技术，其用到的就是代理技术。



有时候，用户想要访问某国外网站，该网站无法在国内直接访问，但是我们可以访问到一个代理服务器，这个代理服务器可以访问到这个国外网站。这样呢，用户对该国外网站的访问就需要通过代理服务器来转发请求，并且该代理服务器也会将请求的响应再返回给用户。这个上网的过程就是用到了正向代理。


!!! note "正向代理，其实是代理服务器代理了客户端，去和目标服务器进行交互。"
    - 突破访问限制 
    - 提高访问速度
    - 隐藏客户端真实IP

[Clash for Windows 优雅地使用 TUN 模式接管系统流量 · Dejavu's Blog](https://blog.dejavu.moe/posts/cfw-tun/)

[Mythologyli/zju-connect: ZJU RVPN 客户端的 Go 语言实现](https://github.com/Mythologyli/ZJU-Connect)


### 反向代理
反向代理（reverse proxy）：是指以代理服务器来接受internet上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给internet上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。

!!! note "反向代理，其实是代理服务器代理了目标服务器，去和客户端进行交互。"

[终于有人把正向代理和反向代理解释的明明白白了！-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1418457)

## 静态路由

静态路由是一种需要管理员手动配置的特殊路由。静态路由比动态路由使用更少的带宽，并且不占用 CPU 资源来计算和分析路由更新。但是，当网络发生故障或者拓扑发生变化后，静态路由不会自动更新，必须手动重新配置。

[为什么要设置静态路由 - CC98论坛](https://www.cc98.org/topic/5650063)
### 静态路由的组成

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

![111](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/d519771d06acb8610067b01d27799f0.jpg)

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



## 内网穿透
[内网穿透 | Chenshan's Blog](https://chenshan.link/2024/12/05/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/)


## 路由器相关
[恩山无线论坛](https://www.right.com.cn/forum/forum.php)



[紫金港纯小白路由器总结 - CC98论坛](https://www.cc98.org/topic/5177370)
### **L2TP（Layer 2 Tunneling Protocol）**

[分享：玉泉 Windows 有线网 L2TP/IPv6 不死脚本 - CC98论坛](https://www.cc98.org/topic/5150942)

L2TP 是 **第二层隧道协议**，主要用于 **VPN（虚拟专用网络）** 连接，通常与 IPsec 结合使用，以增强安全性。  
特点：
- 仅提供隧道功能，不提供加密，需要结合 **IPSec** 才能实现安全的 VPN 连接。
- 适用于远程访问和站点间 VPN 连接。
- 支持 **PPP（点对点协议）**，可用于认证（如 PAP、CHAP）。
- 性能比 **OpenVPN** 等协议更优，延迟较低。

### **OpenWrt**

[openwrt配置IPv6 NAT（2024） - CC98论坛](https://www.cc98.org/topic/5962343)
[搬到1舍后终于用上了IPV6 relay！！(附Redmi AC2100 OpenWrt固件) - CC98论坛](https://www.cc98.org/topic/5372458)

[紫金港 OpenWrt & Adguard Home 配置小总结 - CC98论坛](https://www.cc98.org/topic/5208534)

[Openwrt配置合集——编译、l2tp、静态路由、IPV6(NAT6、Relay) - CC98论坛](https://www.cc98.org/topic/5076895)


[OpenWrt 路由器 MacVLAN+MWAN3 有线网多拨超详细指南 - CC98论坛](https://www.cc98.org/topic/5575720)
**OpenWrt** 是一个 **基于 Linux 的嵌入式路由器操作系统**，支持许多 **路由器和嵌入式设备**。  
特点：
- **开源**，可自定义路由器功能，如防火墙、QoS、VPN。
- **强大的软件包管理**，可安装 OpenVPN、L2TP、Shadowsocks、AdGuardHome 等。
- **支持 IPv6**，能方便地进行 IPv6 隧道或原生 IPv6 连接。
- **适合高级用户和开发者**，支持 Shell、Lua、Python 等编程语言。

### **Padavan**

[浙大校园网Padavan固件路由器配置教程 - CC98论坛](https://www.cc98.org/topic/5213173)

[Padavan IPV6设置终结帖（RedMi AC2100） - CC98论坛](https://www.cc98.org/topic/5040118)

**Padavan** 是一个专门为 **MTK（联发科）路由器** 设计的 **第三方固件**，基于 ASUSWRT（华硕官方固件）进行改进，支持某些 **小米、华硕、斐讯** 路由器。  
特点：
- **轻量化、稳定、高效**，比 OpenWrt 更适合日常使用。
- **支持 IPv6、VPN（L2TP/PPTP）、Shadowsocks/V2Ray/SSR 代理**。
- **Web UI 友好**，适合普通用户配置。
- **不支持扩展软件包**，不像 OpenWrt 那样可自由安装插件。

### **IPv6（Internet Protocol Version 6）**
IPv6 是 **互联网协议的第六版**，用于替代 IPv4，解决地址耗尽问题。  
特点：
- **地址空间大**，使用 128 位地址，可提供几乎无限的 IP。
- **无 NAT（网络地址转换）**，设备可直接全球互联。
- **内置安全性**，支持 **IPSec**，增强安全性。
- **支持自动配置（SLAAC 和 DHCPv6）**，减少网络管理复杂度。
[校网 IPv6 终极指南 - CC98论坛](https://www.cc98.org/topic/5344325)
[有线IPv6环境下基于DNS64/NAT64突破外网出口限速的方法 - CC98论坛](https://www.cc98.org/topic/5108856)

[学校网络架构升级，l2tp和ipv6出了点问题 - CC98论坛](https://www.cc98.org/topic/5945388)

## NAS
[NAS / 硬路由：从入门到入门（网络存储 / Debian 方案 / 校园网认证 / Tailscale / Jellyfin / SMB / WebDAV / Docker / Immich 等） - CC98论坛](https://www.cc98.org/topic/5966741)