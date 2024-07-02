# Web

=== "静态网页"
    完全“按原样”呈现给浏览器的网页
    - 由 HTML、CSS 和 JavaScript 组成，可能含有图片、视频等静态资源
    - 需要发送给客户端的所有文件都是用户可以查看源代码的

=== "动态网页"
    根据用户的请求动态生成内容的网页
    - 通常由服务器端的程序生成，如 Java、PHP、Python、Node.js 等.也即，需要一个能够运行此种程序的服务器
    - 程序的代码对客户端不可见，客户端只能看到生成的结果（HTML）

=== "网页服务器"
    用于处理 HTTP 请求的软件，例如 Apache、Nginx、IIS 等
    也可以使用 Node.js、Python 等编程语言的库

## 前置科技
**插件**
- Hackbar
- Cookie-Editor
- SwitchOmega

**软件**
- BurpSuite, Kali 自带
- PHPStudy，[安装 phpstudy on Kali](https://blog.csdn.net/weixin_54358903/article/details/127698009)
- sqlmap, Kali 自带


[phpstudy on Kali 搭建小皮面板 配置sqli靶场](https://blog.csdn.net/qq_45301512/article/details/128931564)

按照这个教程可以基本配置成功，需要注意的是配置本地host文件的时候，域名的ip地址是本机
使用`ifconfig`查看本机ip地址


### PHP
[PHP学习路线](https://www.runoob.com/w3cnote/php-learning-recommend.html)

!!! tip "学习路线"
    1. 熟悉HTML/CSS/JS等网页基本元素，完成阶段可自行制作简单的网页，对元素属性相对熟悉。
    2. 理解动态语言的概念和运做机制，熟悉基本的PHP语法。
    3. 学习如何将PHP与HTML结合起来，完成简单的动态页面。
    4. 接触学习MySQL，开始设计数据库。
    5. 不断巩固PHP语法，熟悉大部分的PHP常用函数，理解面向对象编程，MySQL优化，以及一些模板和框架。
    6. 最终完成一个功能齐全的动态站点。




## SQL注入




## XSS跨站脚本攻击

## 侧信道攻击

## CSRF跨站请求伪造


## PHP代码审计

