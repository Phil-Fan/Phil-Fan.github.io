# Crawler
##  request


### telnet

[(27条消息) telnet 使用教程（新手篇）及问题集锦_冰夏之夜影的博客-CSDN博客](https://blog.csdn.net/u011561335/article/details/84781236)

[(27条消息) Windows 10操作系统上使用telnet命令（图文）_windows telnet命令_沉默的墨小鱼的博客-CSDN博客](https://blog.csdn.net/m0_46015143/article/details/119379275)

[教你用telnet命令检测端口状态，所有端口映射问题，一招解决_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1VK4y1V7f2/?spm_id_from=333.337.search-card.all.click&vd_source=bf5a9eaf9e79a7d744cd3934132c0d2f)



### 一些常见的术语

- **URI:** A system for identifying pieces of information on the network.
- **HTTP Methods:** The protocol currently contains 8 methods for requesting a URI: , , , , , , , . In this article we focused on the most commonly used one: `OPTIONS``GET``HEAD``POST``PUT``DELETE``TRACE``CONNECT``GET`
- **HTTP Headers:** The headers are additional data sent by the user agent to give more context about the transaction going on between the client and the server. Some of them will help the server reply in the most appropriate way.


！！！！[python中requests库使用方法详解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/137649301)

- headers 

[最全常用User-Agent - 腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1678894)

[(27条消息) 怎么查看自己浏览器的User-Agent_查看user-agent_S1901的博客-CSDN博客](https://blog.csdn.net/S1901/article/details/117231979)

[(27条消息) python 爬虫之 爬取网页并保存（简单基础知识）_爬取网页head部分并保存到_黎明之道的博客-CSDN博客](https://blog.csdn.net/sjjsaaaa/article/details/111144872)

- 状态码



### 遇到的问题

- 如何使用F12开发者工具查看想要的数据：包括网络，元素使用方法：查了好多博客，大概学会了使用方法

- 字符串生成字典：利用json函数      [Python 如何将字符串转为字典 - VincentZhu - 博客园 (cnblogs.com)](https://www.cnblogs.com/OnlyDreams/p/7850920.html)
- request抛异常： 学习try-except异常处理方法
- 如何检测输入的是否为正确网址
  - 想法：是否包含com cn www ; 提前验证是否可以登录； 用正则表达式匹配(但不知道有的网址或许没有com或者www怎么处理)
- request中 text()输出的格式不一：有的很整齐有换行，有的是一整行

- 编码格式不对： `encodeing = 'UTF-8'`



## beautiful soup 库

BeautifulSoup这个库

http://beautifulsoup.readthedocs.org/zh_CN/latest

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230318004805420.png" alt="image-20230318004805420" style="zoom:50%;" />

[(1 封私信) bearer token到底是什么？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/305585277)





## Scrapy 框架

### 学习路径

[Scrapy 入门教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/scrapy-detail.html)

[01.Scrapy框架简介_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1QY411F7Vt?p=2&vd_source=c22bb8d123dbc6430c3057dc8d2701b4)

![img](https://www.runoob.com/wp-content/uploads/2018/10/8c591d54457bb033812a2b0364011e9c_articlex.png)

## 反爬

###  反爬虫手段

- ip
- 登录
- 验证码

### 反反爬手段

- 伪装IP地址的方法：
  1. 使用代理服务器：代理服务器可以将你的请求转发到目标网站，从而隐藏你的真实IP地址。你可以通过购买代理服务器或者使用免费的代理服务器来实现伪装IP地址。
  1. 使用TOR网络：TOR网络是一种匿名网络，可以隐藏你的IP地址，让你在互联网上匿名浏览。你可以通过下载TOR浏览器来使用TOR网络，从而实现伪装IP地址。
  1. 修改Hosts文件：你可以手动修改Hosts文件，将目标网站的域名解析到一个不存在的IP地址上，从而达到伪装IP地址的效果。


- 获取免费的代理

[国内高匿HTTP免费代理IP - 快代理 (kuaidaili.com)](https://www.kuaidaili.com/free/intr)

[(27条消息) 【爬虫进阶】常见的反爬手段和解决方法（建议收藏）_总结反爬虫的目的和常用手段_ZSYL的博客-CSDN博客](https://blog.csdn.net/qq_46092061/article/details/119807084)


