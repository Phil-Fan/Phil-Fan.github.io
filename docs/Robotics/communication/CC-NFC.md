# NFC及其应用

## 介绍

[三分钟看懂NFC - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/43135025)

NFC，全称是**Near Field Communication**，即“**近场通信**”，也叫“**近距离无线通信**”。

它诞生于2003年，由**飞利浦**和**索尼**这两个移动设备巨头联合研发。



NFC是一种**短距离**的**高频**无线通信技术，允许电子设备之间进行**非接触式点对点**数据传输。

**短距离、高频、非接触式、点对点**。

### RFID

说到NFC，就不得不谈谈它的大哥，也就是RFID。



**RFID**，Radio Frequency Identification，即**射频识别**，又名电子标签。

顾名思义，RFID的工作原理就是给一件件物品上贴上一个包含RFID射频部分和天线环路的RFID电路。





![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-aa539569eb2e245756c3b381f459b357_1440w.webp)





携带该标签的物品进入人为设置的特定磁场后，会发出特定频率的信号，阅读器就可获得之前该物品被写入的信息。

这有点像工作人员脖子上挂的胸牌，而你就是他的主管，当他进入你的视线，你就可以知道他的姓名职业等信息，还可以改写他胸牌的内容。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-66f09419c29d831c51389f0503588ffc_1440w.webp)

如果说RFID是一个人戴着胸牌方便别人了解他，那么NFC就是两个人都戴着胸牌，而且他们可以在看到对方后任意更改胸牌上的内容，改变对方接收到的信息。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-909bbfcd833d77986097b14819c3f42f_1440w.webp)

NFC与RFID在物理层面看上去很相似，但实际上是两个完全不同的领域，因为RFID本质上属于**识别技术**，而NFC属于**通信技术**。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-68b289f254b8d6ea9009e018370b7edc_1440w.webp)

NFC诞生之初，就兼容了索尼公司的**`FeliCaTM`标准**，以及**ISO14443 A，B**，也就是**飞利浦的MIFARE标准。**在业界简称为**Type A，Type B和Type F，**其中A，B为`Mifare`标准，F为`Felica`标准。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-9c54e744634ceeae61c447d2800bd297_1440w.webp)





###  三种工作模式

**1.主动模式**

在主动模式下NFC终端可以作为一个读卡器，发出射频场去识别和读/写别的NFC设备信息。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-42b01c8d4bf27423450d09c6ebc28a5e_1440w.webp)

主动通信模式

**2.被动模式**

这个模式正好和主动模式相反，此时NFC终端则被模拟成一张卡，它只在其他设备发出的射频场中被动响应，被读/写信息。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-f0e1d813851749d6547449f7553fcaea_1440w.webp)

**3.双向模式**

在此模式下NFC终端双方都主动发出射频场来建立点对点的通信。相当于两个NFC设备都处于主动模式。

## 应用

### 卡模拟

这是NFC最早的功能之一

让手机可以作为公交卡和银行卡使用，可以大大减少现在出行所需要携带卡片的数量。但是，由于软件问题，这个功能在早期始终无法普及。

### **文件传输**

类似于手机蓝牙，在两台手机都将NFC功能开启后，将手机靠近即可建立连接，之后就可选择传输或接收文件。



## 小实践



### NFC + 自动化流程&快捷指令 简化流程操作

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

[开放能力 / 获取小程序链接 / 获取 URL Scheme (qq.com)](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/url-scheme.html)<br>

### 把校园卡“变小”



### 制作自己的NFC卡片

### NFC音乐墙

