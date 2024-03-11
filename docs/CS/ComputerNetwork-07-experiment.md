# 计网实验以及探索



## Clash给手机提供代理

[使用Clash For Windows与Windows热点共享让你的所有移动设备科学上网 - CC98论坛](https://www.cc98.org/topic/5667186)

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

![img](https://pic1.zhimg.com/80/v2-39f794731fac3c347391bf965fcf9490_1440w.webp)

![img](https://pic3.zhimg.com/80/v2-44103f753f47d507913fe5ab3a66a8c2_1440w.webp)

- 获取IP地址

使用`Win+R`,输入`cmd`,输入`ipconfig`

### 手机端设置

打开iPhone端“文件”——点击右上角三个点——选择“连接服务器”——输入IP地址——点击连接——选择注册用户——输入电脑名称及密码——完成。然后打开“文件”应用，就可以看到共享文件夹了。

![img](https://pic1.zhimg.com/80/v2-5d3c86fd875daf87211ce71fa8e1f548_1440w.webp)



## 静态路由的配置 | 使用GNS3模拟

![预览大图](https://data.educoder.net/api/attachments/510529)

1.路由器的三种模式及切换 

2.路由器配置 IP； 

3.PC 机配置 IP 和网关。



### 路由器的配置

当打开路由器的设备控制台 Console 进行操作时，有三种操作模式。分别是：

- R1 >：用户模式
- R1# ：特权模式
- R1(config)# ：全局配置模式

#### 模式间切换：

1.用户模式（ > ）切换到特权模式（ # ）：使用命令 `enable` 并回车。 

2.特权模式（ # ）切换到全局配置模式（（ config ）#）：使用命令 `config terminal` 并回车：

![img](https://data.educoder.net/api/attachments/510601)

其中，命令可以简写，也可以简写后按 tab 健补全：

![img](https://data.educoder.net/api/attachments/510602)

`exit `返回上一级，`end` 直接退回到特权模式：

![img](https://data.educoder.net/api/attachments/510615)

#### 路由器节点 IP 配置

![预览大图](https://data.educoder.net/api/attachments/878525)

![预览大图](https://data.educoder.net/api/attachments/510574)

```
R1 ( config ) # interface f0/0     ----进入接口
R1 ( config-if ) # ip address 10.0.0.2 255.255.255.0  ----配置 IP 地址
R1 ( config-if ) # no shutdown   ----开启接口

R1 ( config-if ) # end			---- 退出全局配置模式
R1 # write					---- 保存配置
R1 # show ip interface brief  ---- 查看 ip 配置
```

![write](https://data.educoder.net/api/attachments/542779)

![查看ip配置](https://data.educoder.net/api/attachments/510622)

### PC 机配置 IP 和网关

以 PC1 为例，选中 PC1 ，鼠标右键选择 Start：

![img](https://data.educoder.net/api/attachments/878605)

然后鼠标右键选择 console ，打开控制台：

![img](https://data.educoder.net/api/attachments/510640)

使用命令

```shell
ip X.X.X.X（ PC 机 IP 地址） X.X.X.X（网关地址）
save ---- 保存配置
show ip ---- 查看配置
```

![img](https://data.educoder.net/api/attachments/510642)

可以使用 show ip 命令查看 PC 机上配置的 IP 地址：

![img](https://data.educoder.net/api/attachments/510673)

通过 save 保存配置：

![img](https://data.educoder.net/api/attachments/542782)

### 静态路由

静态路由是一种需要管理员手动配置的特殊路由。静态路由比动态路由使用更少的带宽，并且不占用 CPU 资源来计算和分析路由更新。但是，当网络发生故障或者拓扑发生变化后，静态路由不会自动更新，必须手动重新配置。

#### 静态路由的组成

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

![预览大图](https://data.educoder.net/api/attachments/519532)