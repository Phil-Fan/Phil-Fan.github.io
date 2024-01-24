# E：一只爬虫

[TOC]







## 安装库

本次项目共用到以下库

```py
import json
import re
import time

from bs4 import BeautifulSoup
import request
import openpyxl
```



## Task python

在寒假中预习了一点点python的基础语法，写过两三个有意思的小项目，但操作并不熟练，而爬虫需要对python掌握比较熟练，

所以在第一晚（3.17晚），我按照期末复习的c的经验，参照翁恺老师的`mo`平台，在之前笔记的基础上，整理了一份python语法小册子（附录: ./python笔记.pd）

并制作了一个任务完成学习路径大纲





##  Task1 request

首先，我按照报名表的推荐先看了三个阅读文档



### telnet

[(27条消息) telnet 使用教程（新手篇）及问题集锦_冰夏之夜影的博客-CSDN博客](https://blog.csdn.net/u011561335/article/details/84781236)

[(27条消息) Windows 10操作系统上使用telnet命令（图文）_windows telnet命令_沉默的墨小鱼的博客-CSDN博客](https://blog.csdn.net/m0_46015143/article/details/119379275)

[教你用telnet命令检测端口状态，所有端口映射问题，一招解决_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1VK4y1V7f2/?spm_id_from=333.337.search-card.all.click&vd_source=bf5a9eaf9e79a7d744cd3934132c0d2f)



### 一些常见的术语

- **URI:** A system for identifying pieces of information on the network.
- **HTTP Methods:** The protocol currently contains 8 methods for requesting a URI: , , , , , , , . In this article we focused on the most commonly used one: `OPTIONS``GET``HEAD``POST``PUT``DELETE``TRACE``CONNECT``GET`
- **HTTP Headers:** The headers are additional data sent by the user agent to give more context about the transaction going on between the client and the server. Some of them will help the server reply in the most appropriate way.



### http协议

[Dev.Opera — HTTP — 应用程序级协议](https://dev.opera.com/articles/http-basic-introduction/)

[URL与URI，有联系有区别？ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/38120321)

[【秒懂】https协议原理_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1g34y1C7nk/?spm_id_from=333.788.recommend_more_video.1&vd_source=bf5a9eaf9e79a7d744cd3934132c0d2f)

[【03-理论课】什么是HTTP请求和响应？_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1d54y1g7db?p=4&vd_source=bf5a9eaf9e79a7d744cd3934132c0d2f)

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230317000407361.png" alt="image-20230317000407361" style="zoom:50%;" />

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230317000547921.png" alt="image-20230317000547921" style="zoom: 50%;" />



- 公钥加密，私钥解密

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230317000919721.png" alt="image-20230317000919721" style="zoom:50%;" />

- 私钥签名

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230317001042136.png" alt="image-20230317001042136" style="zoom:50%;" />

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230317002849138.png" alt="image-20230317002849138" style="zoom:50%;" />



## Task1-bonus 模拟登陆

我之前对前端的了解并不多，所以这次也学到了很多知识

up主Genji的公开课算是小小白了解一个大概的挺好的课程，学习了最基础的课程

[【00-先导课】爆肝两个月！拜托三连了！这绝对是全B站最用心（没有之一）的Python+爬虫公开课程，从入门到（不）入狱 ！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1d54y1g7db?p=1&vd_source=bf5a9eaf9e79a7d744cd3934132c0d2f)



### Requests库

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



### beautiful soup 库

BeautifulSoup这个库

http://beautifulsoup.readthedocs.org/zh_CN/latest

<img src="https://gitee.com/philfan/my-images/raw/master/image-20230318004805420.png" alt="image-20230318004805420" style="zoom:50%;" />

[(1 封私信) bearer token到底是什么？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/305585277)





## Scrapy 框架

### 学习路径

[Scrapy 入门教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/scrapy-detail.html)

[01.Scrapy框架简介_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1QY411F7Vt?p=2&vd_source=c22bb8d123dbc6430c3057dc8d2701b4)

![img](https://www.runoob.com/wp-content/uploads/2018/10/8c591d54457bb033812a2b0364011e9c_articlex.png)



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



### 遇到的问题

- 虚拟环境的安装

- scrapy文件下不同文件间的引用问题：需要设置根目录

  ```py
  from demospider.items import MovieItem
  ```

  

- 类型错误导致报错，

- 导入库时候：先导入标准库，再导入三方库，再导入自定义

- 子类的重写要和父类长得一样就不会报错

- 钩子方法-》函数回调callback

- 管道配置：数字小的先执行，数字大的后执行

  ```py
  def open_spider ->开始需要干什么
  def close_spider -> 结束需要做什么
  def process_item -> 拿到每条数据做什么
  ```

- `self.parse()` 和 `self.parse` 前者是执行 后者是地址!!!!不要搞反了（查了20min的bug

  !!!!!!!!!!!!!!!!!!!!!!!!!



- 中间插了个广告，而浏览器内置的广告拦截器会让这个地方网址直接加载不出来，爬的时候导致报错

​			解决方案：判定读到的URL中是否包含BV号，如果没有就跳过	



- `url`合并问题，用``urljoin`函数

​		[urllib.parse — Parse URLs into components — Python 3.11.2 documentation](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse)

- 最后到了一个困扰了我很久的问题，就是页面分析的问题

  页面的源代码和在F12中查看的元素中并不一样，可能是有

selector的css选择器

[CSS 选择器参考手册 (w3school.com.cn)](https://www.w3school.com.cn/cssref/css_selectors.asp)



关键词中文转换



视频分p问题

bvid、aid、cid的问题



- 有没有更快捷的方法可以获取到准确的点赞投币数字呢

这个请求头的返回 包含了这个准确值

[(27条消息) Python实现对Bilibili视频点赞等信息的爬取_Samue1Zhu的博客-CSDN博客](https://blog.csdn.net/Samue1_Zhu/article/details/106230610)



中文编码问题

[urllib.parse — Parse URLs into components — Python 3.11.2 documentation](https://docs.python.org/3/library/urllib.parse.html)

Crawled (200)

第一页和第二页网页元素不一样

```css
(首页)#i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div > div.video.i_wrapper.search-all-list > div.video-list.row > div:nth-child(1) 
(非)#i_cecream > div > div:nth-child(2) > div.search-content--gray.search-content > div > div > div.video-list.row > div:nth-child(2)
```





bvid获取

[BiliBili的bvid查询cid | 叉叉白 (xxwhite.com)](https://blog.xxwhite.com/2020/03230.bilibili-bvid.html#解释)

[哔哩哔哩开放平台 (bilibili.com)](https://openhome.bilibili.com/)