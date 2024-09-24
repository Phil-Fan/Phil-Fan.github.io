# 现代控制理论

!!! note "资源汇总"
    === "历年卷"
        - [2023-2024 秋冬 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5748670)
        - [2023-2024 秋 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5748295)
        - [2022-2023 秋 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5454547)
        - [2021-2022 秋 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5197292)
        - [2019-2020 春夏 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/4960302/1#1)
        - [2019-2020 春夏 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/4856718)
        - [2020 回忆卷](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5040332)
    === "A4"
        - [A4 梁毅浩](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5197981)
        - [A4 Healor](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5826788)
        - [A4 Rainbow0](http://www-cc98-org-s.webvpn.zju.edu.cn:8001/topic/5658322)

[现代控制理论重点概念梳理 - 知乎](https://www.zhihu.com/column/c_1131936304564453376)

[现代控制理论-重点知识汇总\_现代控制理论知识点总结-CSDN博客](https://blog.csdn.net/qq_31274209/article/details/105156993)

[控制理论——一小时从劝退到入门 - 知乎](https://zhuanlan.zhihu.com/p/683044170)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240922170358.png)


反馈控制：跑步机上跑步 | 利用系统的输出量以参考数量的偏差进行控制，使系统的输出量与参考量之间的偏差尽可能小
最优控制：田径赛跑 | 所谓最优控制就是寻找一个允许控制，使得被控系统在满足各种约束的条件下，使给定的性能指标达到最优
## 离散系统描述

零输入分量： $x(t) = 0,f(0^+) = f(0^-)$
零状态分量： $f^{n}(0^-) = 0$

### 脉冲传递函数


脉冲传递函数：$G(z) = \frac{Y(z)}{U(z)}$ ，零初始条件下，系统的输出采样函数的z变换和输入采样函数的z变换的比值



零阶保持器： $G_h(s) = \frac{1-e^{-Ts}}{s},G(z) = 1$

trick: 先把$(1-z^{-1})$提出来

$$
G_h(s)\cdot G_p(s) = \frac{1-e^{-Ts}}{s} G_p(s) = (1-z^{-1})(\frac{G_p(s)}{s})
$$


#### 推导法

> 一个讲的很好的视频：[离散系统关于脉冲传递函数求法\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1fQ4y1k7p9/)

闭环脉冲传递函数 $\Phi(z) = \frac{C(z)}{R(z)}$,如果前向通道第一个传递函数之前没有采样开关，就没有办法求解，只能求$C(z)$

- $\mathcal{Z}[A(s)B(z)] = A(z)\cdot B(z)$
- $\mathcal{Z}[A(s)B(s)] = AB(z) \ne A(z)B(z)$

要注意 $G_1G_2(z) \ne G_1(z)G_2(z)$

#### Mason增益公式法
回路只要有连在一起，就不能分开算z变换

## 状态空间法

## 状态空间的解（定量）

## 能控能观性（定性）

## 系统的稳定性与李亚普诺夫稳定性

## 极点配置、镇定、解耦

## 最优控制
