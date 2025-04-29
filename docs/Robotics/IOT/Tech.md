# 通信技术

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224233412357.png)

| 技术指标       | UWB                              | WiFi                             | ZigBee                          | Cellular（含 NB-IoT/LTE-M）    |
|----------------|----------------------------------|----------------------------------|---------------------------------|-------------------------------|
| **定位精度**   | **厘米级（10-30cm）**            | 米级（1-5米）                   | 米级（1-10米）                 | 10-100米（需 GNSS 辅助）       |
| **传输速率**   | 低（侧重定位，理论可达500Mbps）  | **高（WiFi 6: 1Gbps以上）**     | **低（250kbps）**              | 中（NB-IoT: 250kbps，5G: 10Gbps）|
| **覆盖范围**   | **短（<100米）**                 | 中（50-300米）                  | 短（10-100米）                 | **广域（千米级）**             |
| **功耗**       | 中（待机低，激活时较高）         | **高（需持续供电）**            | **极低（电池寿命数年）**       | 中高（NB-IoT 低，5G 高）       |
| **频段**       | 3.1-10.6GHz                      | 2.4/5/6GHz                      | 2.4GHz/868MHz/915MHz           | 授权频段（如 700MHz-3.5GHz）   |
| **网络拓扑**   | 点对点/星型                      | 星型（AP为中心）                | **网状/自组网**                | 蜂窝基站架构                  |
| **网络容量**   | 低（单网数十节点）               | 中（单AP支持数十设备）          | **高（单网65000节点）**        | 高（5G支持百万设备/km²）       |
| **抗干扰能力** | **强（宽频脉冲抗多径干扰）**     | 弱（2.4GHz频段拥挤）            | 中（DSSS扩频技术）             | 强（动态频段分配）             |
| **安全性**     | **高（脉冲加密，难以截获）**     | 中（依赖WPA3加密）              | 高（AES-128加密）              | 高（SIM卡认证）               |
| **硬件成本**   | **高（专用芯片）**               | 低（高度集成）                  | 低（简单协议栈）               | 中高（需基带芯片+SIM）         |
| **典型场景**   | 高精度定位（工厂、汽车钥匙）     | 高速数据传输（视频、AR/VR）     | 低功耗传感网络（智能家居、农业）| 广域物联网（车联网、智慧城市） |

## NFC

### 介绍

NFC，全称为**近场通信**（Near Field Communication），也称为**近距离无线通信**。它于2003年由**飞利浦**和**索尼**联合研发。[三分钟看懂NFC - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/43135025)

NFC是一种**短距离**、**高频**的无线通信技术，允许电子设备之间进行**非接触式点对点**的数据传输。

### RFID

在讨论NFC时，必须提到其前身RFID。

**RFID**（射频识别，Radio Frequency Identification），也称为电子标签，其工作原理是为物品贴上包含RFID射频部分和天线环路的电路。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-aa539569eb2e245756c3b381f459b357_1440w.webp)

!!! note "RFID在仓储物流中的挑战"
    - 多角度多设备解调复杂
    - 传输距离有限

当携带RFID标签的物品进入特定磁场时，会发出特定频率的信号，阅读器可以获取该物品的信息。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-66f09419c29d831c51389f0503588ffc_1440w.webp)

如果说RFID是一个人戴着胸牌方便别人了解他，那么NFC则是两个人都戴着胸牌，并且可以互相更改胸牌上的信息。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-909bbfcd833d77986097b14819c3f42f_1440w.webp)

尽管NFC和RFID在物理层面相似，但RFID属于**识别技术**，而NFC属于**通信技术**。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-68b289f254b8d6ea9009e018370b7edc_1440w.webp)

NFC兼容索尼的**`FeliCaTM`标准**和**ISO14443 A，B**（即飞利浦的MIFARE标准），简称为**Type A，Type B和Type F**。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-9c54e744634ceeae61c447d2800bd297_1440w.webp)

### 三种工作模式

1. **主动模式**：NFC终端作为读卡器，发出射频场识别和读/写其他NFC设备信息。

   ![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-42b01c8d4bf27423450d09c6ebc28a5e_1440w.webp)

2. **被动模式**：NFC终端模拟成卡，仅在其他设备的射频场中被动响应。

   ![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-f0e1d813851749d6547449f7553fcaea_1440w.webp)

3. **双向模式**：双方NFC终端主动发出射频场建立点对点通信。

### 应用

#### 卡模拟

NFC的早期功能之一是让手机作为公交卡和银行卡使用，减少携带卡片的数量，但由于软件问题，早期未能普及。

#### 文件传输

类似于蓝牙，两台手机开启NFC后靠近即可连接，选择传输或接收文件。


### 小实践



#### NFC + 自动化流程&快捷指令 简化流程操作

NFC作为触发器，然后执行打开浙大钉二维码的操作，[快捷指令下载地址](https://www.icloud.com/shortcuts/38a3b78d869447e194c92a13d27eee20)

需要注意的是，浙大钉工作台有响应时间，所以采取先加载工作台界面，然后再打开浙大钉二维码的方式进行。

```url
# 打开浙大钉工作台
dingtalk://dingtalkclient/action/switchtab?index=2&reload=true
# 打开校园卡二维码
dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fyqfkgl.zju.edu.cn%2F_web%2F_customizes%2Fykt%2Findex3.jsp
```

另外，在钉钉的文档里指出，插入的URL需要做`urlencode`

[一文详解 URLEncode - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/557035152)<br>

[UrlEncode编码和UrlDecode解码-在线URL编码解码工具](http://www.urlencode.com.cn/)<br>

![1c489475f810460c6d9466309484fac](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1c489475f810460c6d9466309484fac.jpg)

使用了URL Scheme 的方法，控制iPhone自动化打开软件

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/175f446d-e2a5-4f60-92bb-2588cd6406ba.png)

**参考网页**

一般直接搜索“APP + URL scheme”关键词，即可找到该scheme的相关信息。

[AppLink的结构 - 钉钉开放平台 (dingtalk.com)](https://open.dingtalk.com/document/isvapp/applink-structure)<br>

[打开普通页面 - 钉钉开放平台 (dingtalk.com)](https://open.dingtalk.com/document/isvapp/applink-open-normal-page)<br>

[打开iOS新世界的大门 | 有趣的URL Scheme - 少数派 (sspai.com)](https://sspai.com/post/81278#!)<br>

[x-callback-URL 的使用方法 - InfoCG](https://www.infocg.cn/jishufenxiang/155012.html)<br>

[开放能力 / 获取小程序链接 / 获取 URL Scheme (qq.com)](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-scheme.html)


#### 把校园卡“变小”



#### NFC音乐墙



## 蓝牙技术

### 介绍
蓝牙（Bluetooth）是一种短距离无线通信技术，工作在2.4GHz频段。

### 发展历史
- 1994年：爱立信发明蓝牙技术
- 1998年：成立蓝牙技术联盟（SIG）
- 2010年：蓝牙4.0（BLE）发布
- 至今：蓝牙5.0/5.1/5.2等版本

### 蓝牙分类
- 传统蓝牙（Classic Bluetooth）
- 低功耗蓝牙（BLE - Bluetooth Low Energy）
- 高速蓝牙（Bluetooth High Speed）

### 蓝牙协议栈

#### 物理层
- 频段：2.4GHz ISM频段
- 调制方式：GFSK
- 跳频：AFH（自适应跳频）

#### 链路层
- 连接建立
- 数据传输
- 安全机制

#### 应用层
- GATT（通用属性配置文件）
- GAP（通用访问配置文件）

### BLE特点
- 低功耗
- 低延迟
- 低成本
- 短距离
- 安全性高

### 开发指南

#### 硬件选型
- 蓝牙芯片
- 天线设计
- 电源管理

#### 软件开发
- 协议栈选择
- API使用
- 调试工具





## **UWB（超宽带技术）**
### 开发历史背景
- **起源**：1960年代源于军事雷达技术，2002年FCC解禁后进入民用领域。
- **标准化**：2007年IEEE 802.15.4a标准纳入UWB，近年因高精度定位需求兴起。

### 技术原理
- **信号特性**：使用纳秒级非正弦波窄脉冲，频宽超500MHz（如3.1-10.6GHz）。
- **定位方法**：基于飞行时间（TOF）、到达时间差（TDOA）或到达角（AOA）实现厘米级定位。

### 常见应用
- **工业**：工厂人员/资产追踪、AGV导航（如特斯拉工厂）。
- **消费电子**：手机无感解锁（如iPhone、小米）、智能家居（自动开启门锁）。
- **汽车**：数字钥匙（如宝马iX）、车内活体检测。
- **医疗**：手术器械追踪、患者定位。

### 优点
- 超高精度（10-30cm），抗多径干扰，穿透性强，低功耗，安全性高（加密脉冲）。

### 缺点
- 覆盖范围短（通常<100米），金属环境性能下降，硬件成本较高。

### 使用场景
- 需要精确定位的场景：仓储物流、矿井安全、自动驾驶汽车、体育训练分析。



## **WiFi（无线局域网技术）**
### 开发历史背景
- **起源**：1997年IEEE发布802.11标准，Wi-Fi联盟推动商业化。
- **演进**：从802.11b（11Mbps）到WiFi 6E（9.6Gbps），频段扩展至6GHz。

### 技术原理
- **频段**：2.4GHz（覆盖广）、5GHz（速率高）、6GHz（WiFi 6E）。
- **架构**：通过无线路由器组网，支持OFDMA和MU-MIMO提升多设备性能。

### 常见应用
- **消费领域**：家庭/办公网络、公共场所热点（如商场、机场）。
- **物联网**：智能家居（摄像头、音箱）、工业设备联网。
- **特殊应用**：WiFi手机（通过VoWiFi拨打长途）、AR/VR数据传输。

### 优点
- 高传输速率（WiFi 6可达1Gbps），普及率高，兼容性强。

### 缺点
- 功耗较高，覆盖受墙体衰减大，安全性依赖加密协议（如WPA3）。

### 使用场景
- 高带宽需求场景：视频流媒体、在线游戏、大型文件传输。



## **ZigBee（低功耗网状网络）**
### 开发历史背景
- **起源**：2003年ZigBee联盟成立，基于IEEE 802.15.4标准。
- **定位**：专为低功耗物联网设计，与蓝牙、WiFi形成互补。

### 技术原理
- **频段**：2.4GHz（全球通用）、915MHz（美洲）、868MHz（欧洲）。
- **组网**：支持星型、树型、网状拓扑，自修复网络，单网络支持65000节点。

### 常见应用
- **智能家居**：灯光控制（Philips Hue）、温控系统。
- **工业**：传感器网络（如工厂环境监测）、智慧农业（土壤湿度监测）。
- **公共设施**：智能路灯、电表远程抄表。

### 优点
- 超低功耗（电池寿命数年），网络容量大，成本低。

### 缺点
- 低速率（250kbps），覆盖范围小（10-100米），穿透性较弱。

### 使用场景
- 低频次数据传输场景：智能电表、农业传感器、仓储环境监测。


## **Cellular（蜂窝网络）**
### 开发历史背景
- **发展历程**：1G（模拟信号）→5G（高速低延迟），覆盖从语音到万物互联。
- **技术分支**：NB-IoT（窄带物联网）、LTE-M（中速率）、5G mMTC（海量连接）。

### 技术原理
- **蜂窝结构**：六边形小区划分，基站动态切换（Handover），频分/码分多址。
- **物联网变种**：NB-IoT（超低功耗，广覆盖）、Cat-M1（支持语音）。

### 常见应用
- **移动通信**：智能手机联网、车联网（V2X）。
- **物联网**：智能城市（智慧路灯）、远程医疗（ECG监测）。
- **紧急通信**：灾害应急网络、海上平台通信。

### 优点
- 广域覆盖（全球漫游），高移动性支持，适合大规模部署。

### 缺点
- 设备成本高（需SIM卡），基站依赖性强，功耗较高（NB-IoT除外）。

### 使用场景
- 移动性要求高的场景：物流追踪、共享设备管理、偏远地区监测。




## NB-IOT

NB使用移动基站

lora使用自己搭建的网关


## Lora
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250220095837125.png)


LoRa（Long Range）是一种低功耗广域网（LPWAN）无线通信技术，由 **Semtech** 公司开发。它使用 **Chirp Spread Spectrum (CSS) 扩频调制**，具有远距离通信、低功耗和强抗干扰能力的特点，适用于 **物联网（IoT）** 应用。

LoRa 适合 **低数据量、远距离、低功耗** 的物联网应用，是 NB-IoT、Zigbee、WiFi 的重要补充。

### 线性啁啾扩频

频率随时间线性上升

如何表示数据？

- 带宽四等分
- 