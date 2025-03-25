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
### ZJU-Rule
[新的ZJU-Rule解决方案 - CC98论坛](https://www.cc98.org/topic/5769136/1#1)


原ZJU-Rule的公共服务已经停止了，但是我们仍然可以使用一些基于[subconverter](https://github.com/tindy2013/subconverter)的公共订阅转换  

**请注意，使用公共的订阅转换服务不能保证节点信息不被泄漏**  

下面以 [acl4ssr](https://acl4ssr-sub.github.io/) 为例介绍具体怎么使用：  

1. 打开订阅转换网页  
2. 在远程配置（**不是后端地址**）输入`https://raw.githubusercontent.com/SubConv/ZJU-Rule/main/Clash/config/ZJU.ini`，并点击下拉栏中的地址  
    ![](https://file.cc98.org/v2-upload/2023-12-06/odb0wqux.webp)  
3. 如果用 [acl4ssr](https://acl4ssr-sub.github.io/) 的话，有个后端地址选项，并不是所有后端口可用，自己试试看  
4. 剩下的用法就和正常订阅转换没啥区别了


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

公网：人人都可以访问

内网：需要特定的网络才可以访问

内网穿透就是将内网的服务暴露给公网访问


[1Panel 文档](https://1panel.cn/docs/installation/online_installation/)

```shell title="安装1Panel,ubuntu"
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
```

配置镜像加速选择`y`

使用`1pcl`命令行工具进行管理，[命令行工具 - 1Panel 文档](https://1panel.cn/docs/installation/cli/)

!!! note "如果使用的是云服务器，需要配置安全组规则"
    在安全组当中，选择添加规则

    - 目的：`20410/20410`
    - 源：`0.0.0.0/0`

    然后点保存即可，不需要重启云服务器，保存后自动生效。

下载安装包


```shell title="解压"
tar -zxvf frp_0.61.2_linux_amd64.tar.gz
```

```shell title="进入目录"
cd frp_0.61.2_linux_amd64
```

```shell title="编辑frps.toml"
vim frps.toml
```

```toml title="frps.toml"
bindPort = 7000      # 服务端与客户端通信端口
# vhostHTTPPort = 80   # 如果客户端需要使用http服务，在这里配置代理端口

auth.token = "token"                    # 身份验证令牌，frpc要与frps一致

# Server Dashboard，可以查看frp服务状态以及统计信息
webServer.addr = "0.0.0.0"              # 后台管理地址
webServer.port = 7500                   # 后台管理端口
webServer.user = "admin"                # 后台登录用户名
webServer.password = "admin"            # 后台登录密码
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250318114804586.png)

访问公网ip的7500端口，可以查看frp服务状态以及统计信息

!!! note "注意这里需要在aliyun控制台的安全组中添加7000和7500端口"

接下来配置客户端侧（frpc = frp client）

```shell title="后台运行"
#服务器端
nohup ./frps -c frps.toml &

#客户端
nohup ./frpc -c frpc.toml &
```

```shell title="开机自启动"
sudo vi /etc/rc.local  

#自行修改为绝对路径
nohup /root/frp/frpc -c /root/frp/frpc.toml &
```

[error unmarshaling JSON: while decoding JSON: json: cannot unmarshal string into Go value of type v1.ServerConfig · Issue #3657 · fatedier/frp](https://github.com/fatedier/frp/issues/3657)


| **场景**                     | **代理类型** | **本地端口** | **远程端口** | **用途** |
|------------------------------|-------------|--------------|--------------|----------|
| 远程 SSH 访问                | TCP         | 22           | 6000         | 远程 SSH 进内网服务器 |
| 内网 Web 服务器访问          | HTTP        | 8080         | 8081         | 访问本地网站 |
| 访问家中 NAS / 服务器        | TCP         | 445/5005     | 4445/5055    | 远程访问 SMB 或 WebDAV |
| 远程数据库访问               | TCP         | 3306/5432    | 13306/15432  | 远程连接 MySQL / PostgreSQL |
| 远程桌面（RDP）              | TCP         | 3389         | 13389        | 远程控制 Windows |
| 远程管理 Docker API          | TCP         | 2375         | 12375        | 远程管理 Docker |


[内网穿透 | Chenshan's Blog](https://chenshan.link/2024/12/05/%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F/)


### DDNS


方案一:直接使用群晖的DDNS功能,将IP直接映射到域名上,配合路由器的端口转发功能就能完全实现设备直连
方案二:如果家里是使用软路由的,就使用动态DNS这个插件也是可以实现IP映射到域名上,再配置好端口转发就能实现设备直连
方案三:购买云端服务器,使用配置好FRP,电脑端配置好frp,也可以实现内网穿透(但是这个方案并不是最好的,因为购买的云端服务器有个通病,就是公用网络,因此经常网络波动很大,提现效果比较差,需要自行需优化网络)
方案四:购买云端服务器,使用开源项目rustdesk,服务器安装好rustdesk的中转服务器,在电脑中配置好rustdesk客户端,就能实现像是向日葵的功能(这种也可以配置到手机中Rustdesk已经是全平台适用了,除了苹果手机无法被控制但是可以控制别的设备,安卓,window都能实现控制与被控制)


## WebDAV

WebDAV（**Web Distributed Authoring and Versioning**）是一种基于 **HTTP 协议**的扩展协议，主要用于实现远程文件管理和协作编辑。它允许用户通过互联网直接对服务器上的文件进行读写、编辑、移动和版本控制，就像一个本地文件系统一样。

---

### **核心功能**
1. **远程文件管理**  
   - 直接在服务器上创建/删除/移动文件或文件夹。
   - 支持文件属性（如创建时间、权限）的读写。

2. **协作编辑**  
   - **文件锁机制**：防止多人同时修改同一文件导致冲突。
   - 支持文件版本控制（需配合扩展协议如 DeltaV）。

3. **跨平台访问**  
   - 可通过浏览器、操作系统（如映射为网络驱动器）或专用客户端访问。

---

### **典型应用场景**
| 场景               | 说明                                                                 |
|--------------------|----------------------------------------------------------------------|
| 云存储同步         | Nextcloud、OwnCloud 等私有云通过 WebDAV 提供文件访问。               |
| 文档协作           | Microsoft Office 直接编辑 WebDAV 服务器上的文件。                    |
| 网站内容管理       | 通过 WebDAV 直接管理网站服务器上的文件（如 WordPress 插件支持）。    |
| 跨设备文件共享     | 手机/电脑通过 WebDAV 客户端（如 Solid Explorer）访问远程文件。       |

