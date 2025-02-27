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