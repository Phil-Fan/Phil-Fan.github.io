# 软件使用

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

## 抓包 - Wireshark


## 抓包 - Charles


Charles的主要功能：

- 截取Http 和 Https 网络封包
- 支持重发网络请求，方便后端调试
- 支持修改网络请求参数
- 支持网络请求的截获并动态修改
- 支持模拟慢速网络


### 配置
[Download a Free Trial of Charles • Charles Web Debugging Proxy](https://www.charlesproxy.com/download/)

### IOS手机抓包

[charles对iOS手机的https进行抓包（图文教程）\_charles怎么抓ios手机包-CSDN博客](https://blog.csdn.net/weixin_43837268/article/details/121938674)

## 抓包 - Burpsuite

Burp Suite 是一个集成化的渗透测试工具，它包含了多个用于攻击和分析 Web 应用程序的工具。主要功能包括：

### 主要功能

1. **Proxy（代理）**
   - 拦截并修改客户端和服务器之间的请求和响应
   - 支持 HTTP/HTTPS 流量分析
   - 可以手动修改、转发或丢弃请求

2. **Scanner（扫描器）**
   - 自动扫描 Web 应用程序漏洞
   - 检测常见安全问题如 SQL 注入、XSS 等
   - 生成详细的漏洞报告

3. **Repeater（中继器）**
   - 手动修改和重发 HTTP 请求
   - 分析服务器响应
   - 测试不同参数对响应的影响

4. **Intruder（入侵）**
   - 自动化攻击测试
   - 支持多种攻击模式
   - 可用于暴力破解、模糊测试等

### 使用步骤

1. 配置浏览器代理为 Burp Suite（默认 127.0.0.1:8080）
2. 安装 Burp 的 CA 证书以拦截 HTTPS 流量
3. 开启拦截功能，观察和分析 HTTP/HTTPS 请求
4. 根据需要使用不同模块进行测试



