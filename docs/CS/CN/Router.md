# Router


## 资料链接


[恩山无线论坛](https://www.right.com.cn/forum/forum.php)

https://github.com/SuLingGG

[紫金港纯小白路由器总结 - CC98论坛](https://www.cc98.org/topic/5177370)


## 环境配置
### **L2TP（Layer 2 Tunneling Protocol）**

[分享：玉泉 Windows 有线网 L2TP/IPv6 不死脚本 - CC98论坛](https://www.cc98.org/topic/5150942)

L2TP 是 **第二层隧道协议**，主要用于 **VPN（虚拟专用网络）** 连接，通常与 IPsec 结合使用，以增强安全性。  
特点：
- 仅提供隧道功能，不提供加密，需要结合 **IPSec** 才能实现安全的 VPN 连接。
- 适用于远程访问和站点间 VPN 连接。
- 支持 **PPP（点对点协议）**，可用于认证（如 PAP、CHAP）。
- 性能比 **OpenVPN** 等协议更优，延迟较低。






### LAN和WAN接口

路由器通常有两种主要的网络接口类型：LAN（Local Area Network，局域网）和WAN（Wide Area Network，广域网）。

#### LAN接口
- LAN接口用于连接**内部网络设备**，如电脑、手机、打印机等
- 通常有多个LAN端口（如4个RJ45接口）
- 默认分配私有IP地址（如192.168.1.x）
- 内置DHCP服务器，可自动为连接设备分配IP地址
- 支持有线（以太网）和无线（WiFi）连接
- 通常配置为网关，IP地址如192.168.1.1

#### WAN接口
- WAN接口用于连接**外部网络**（如运营商网络）
- 通常只有1个WAN端口
- 获取公网IP地址（由ISP分配）
- 负责NAT（网络地址转换）功能
- 处理内外网络之间的数据转发
- 可配置为DHCP客户端、静态IP或PPPoE等模式

#### 工作原理
1. WAN口连接互联网，获取公网IP
2. LAN口为内网设备提供私有IP
3. 路由器通过NAT技术，使内网设备共享WAN口的公网IP访问互联网
4. 同时提供防火墙功能，保护内网安全


### 固件 - Breed
Breed是一个适用于多种路由器的Bootloader（引导加载程序）：

- 功能特点：
  - 提供Web界面进行固件刷写
  - 支持固件备份和恢复
  - 可以修改MAC地址和其他参数
  - 具有故障恢复功能
  - 支持多种型号的路由器

- 优势：
  - 操作简单直观
  - 刷机失败的风险较低
  - 可以防止路由器变砖
  - 支持多种固件格式

!!! note "路由器坏块"
    路由器就像一台小电脑，它的存储器（类似于硬盘）有时会出现坏掉的区域，这些坏掉的区域叫做"坏块"。坏块主要是由于频繁更新系统、电压不稳定或者硬件本身老化等原因造成的。

    如果路由器出现坏块，可能会导致路由器无法正常开机、系统不稳定等问题。遇到这种情况，我们可以先用检测工具看看坏块的数量，如果坏块太多的话就需要考虑换新路由器了。平时使用时，尽量不要频繁更新系统，并且要使用稳定的电源，这样可以减少坏块产生的机会。

    ```html title="NAND坏块检查"
    http://192.168.31.1/cgi-bin/luci/;stok=CCCCCCCCCCC/api/misystem/set_config_iotdev?bssid=Xiaomi&user_id=longdike&ssid=%0A%5B%20-z%20%22%24(dmesg%20%7C%20grep%20ESMT)%22%20%5D%20%26%26%20B%3D%22Toshiba%22%20%7C%7C%20B%3D%22ESMT%22%0Auci%20set%20wireless.%24(uci%20show%20wireless%20%7C%20awk%20-F%20'.'%20'%2Fwl1%2F%20%7Bprint%20%242%7D').ssid%3D%22%24B%20%24(dmesg%20%7C%20awk%20'%2FBad%2F%20%7Bprint%20%245%7D')%22%0A%2Fetc%2Finit.d%2Fnetwork%20restart%0A
    ```

    运行代码后，你路由器的2.4g WiFi名称会改名成：比如  "ESMT"，"Toshiba"，"Toshiba 90 768"。 90和768是坏块。 如果ESMT或者Toshiba后面没数字，那恭喜你，没有坏块！！！



### **固件 - OpenWrt**

以Redmi AC2100为例，使用OpenWrt固件，配置IPv6 NAT。

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=786429754&bvid=BV1114y1X7TA&cid=1211226722&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>

第一步，上电，连接网线（可以连接宿舍里面的网口，也可以将LAN口和WAN口直接连接起来），等待启动。进入管理后台 `192.168.31.1`, 更改网络名称以及密码

第二步，在，刷入降级固件。等待5-7min，重新进入网络。发现固件已经降级。观察浏览器界面，可以发现url部分有 `stok=xxxxxxxx`字样，记录stok字段

第三步，刷入不死固件。

在浏览器中输入下面的url，将CCCCC部分替换成为自己的stok字段

```html title="不死固件刷入"
http://192.168.31.1/cgi-bin/luci/;stok=CCCCCCCCCCCCCCCC/api/misystem/set_config_iotdev?bssid=Xiaomi&user_id=longdike&ssid=%0Acd%20%2Ftmp%0Acurl%20-o%20B%20-O%20https%3A%2F%2Fbreed.hackpascal.net%2Fr1286%2520%255b2020-10-09%255d%2Fbreed-mt7621-xiaomi-r3g.bin%20-k%20-g%0A%5B%20-z%20%22%24(sha256sum%20B%20%7C%20grep%20242d42eb5f5aaa67ddc9c1baf1acdf58d289e3f792adfdd77b589b9dc71eff85)%22%20%5D%20%7C%7C%20mtd%20-r%20write%20B%20Bootloader%0A
```

发现路由器指示灯由蓝色变为橙色，再变为蓝色，说明固件刷入成功。

需要断电，按住reset不动在开电10秒后松开reset。这样才能进入Breed后台。等到蓝色灯光闪烁的时候

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250318100853158.png)


!!! note "这里应该需要一个有网口的电脑"

使用网线连接路由器LAN口与电脑网口，设置电脑自动获取ip地址

```shell title="win + R 输入，进入网络管理"
ncpa.cpl
```


[【0608-精简稳定版OpenWrt】红米＆小米AC2100|多拨|超频|SmartDNS|IPV6，附刷机教程-小米无线路由器及小米网络设备-恩山无线论坛](https://www.right.com.cn/forum/thread-4027477-1-1.html)


[openwrt配置IPv6 NAT（2024） - CC98论坛](https://www.cc98.org/topic/5962343)
[搬到1舍后终于用上了IPV6 relay！！(附Redmi AC2100 OpenWrt固件) - CC98论坛](https://www.cc98.org/topic/5372458)

[紫金港 OpenWrt & Adguard Home 配置小总结 - CC98论坛](https://www.cc98.org/topic/5208534)
[OpenWrt@玉泉，从编译到日常使用的入门指南 - CC98论坛](https://www.cc98.org/topic/4957730/1#1)
[Openwrt配置合集——编译、l2tp、静态路由、IPV6(NAT6、Relay) - CC98论坛](https://www.cc98.org/topic/5076895)


[OpenWrt 路由器 MacVLAN+MWAN3 有线网多拨超详细指南 - CC98论坛](https://www.cc98.org/topic/5575720)
**OpenWrt** 是一个 **基于 Linux 的嵌入式路由器操作系统**，支持许多 **路由器和嵌入式设备**。  
特点：
- **开源**，可自定义路由器功能，如防火墙、QoS、VPN。
- **强大的软件包管理**，可安装 OpenVPN、L2TP、Shadowsocks、AdGuardHome 等。
- **支持 IPv6**，能方便地进行 IPv6 隧道或原生 IPv6 连接。
- **适合高级用户和开发者**，支持 Shell、Lua、Python 等编程语言。

### 固件 - Padavan

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

### 软路由


## NAS
[NAS / 硬路由：从入门到入门（网络存储 / Debian 方案 / 校园网认证 / Tailscale / Jellyfin / SMB / WebDAV / Docker / Immich 等） - CC98论坛](https://www.cc98.org/topic/5966741)‘


## BT & PT


## 