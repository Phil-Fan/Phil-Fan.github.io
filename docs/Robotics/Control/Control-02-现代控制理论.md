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

### z变换
- 留数法
- 超前滞后定理


\[
\mathcal{Z}\{x[n-k]\} = z^{-k}X(z)
\]

\[
\mathcal{Z}\{x[n+k]\} = z^{k}X(z) - \sum_{i=0}^{k-1} x[i]z^{k-i-1}
\]

- 初值定理、终值定理

$$
x[0] = \lim_{z \to \infty} X(z)
$$

$$
\lim_{n \to \infty} x[n] = \lim_{z \to 1} (z-1)X(z)
$$


- 差分方程求解

!!! note "要注意微分方程的离散化 x(t)变成x(nT)才可以"


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

!!! note "离散系统例子"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240926011136.png)
    控制体重的例子

    如果测体重测得太频繁，那么根本来不及计划

## 状态空间法

状态空间是一组将输入、输出、状态联系在一起的一阶微分方程。

$$
\begin{aligned}
\dot{x} &= Ax + Bu \\
y &= Cx + Du
\end{aligned}
$$

$$
G(z) = C(zI-A)^{-1}B + D
$$

A的特征值就是$G(s)$的极点



!!! note "状态空间与极点的关系"
  - **特征向量:** $Av = \lambda v$ 在一条直线上
  - 对角化的方法
  - $P^{-1}A P = \Lambda$
  - $\dot{X} = AX,X = PY,\dot{Y} = \Lambda Y$

### 使用phase图进行分析

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240926011802.png)

### matlab分析

```matlab
A = [0 1; -.5 -.5]
B = [1;0]
C = [1 0]
sys = ss(A,B,C)
sys_d = c2d(sys,0,1)
```



### 状态空间的解（定量）

**递推法求解**


---
**$\mathscr{z}$变换**

$$
\begin{aligned}
\dot{x} &= Ax + Bu \\
y &= Cx + Du
\end{aligned}
$$

对上式$\mathscr{z}$变换

$$
X(\mathscr{z})=(\mathscr{z}I-A)^{-1}\mathscr{z}x(0)+(\mathscr{z}I-A)^{-1}BU(\mathscr{z})
$$

求得

$$
\Phi(k) = A^k = \mathscr{Z}^{-1}[(\mathscr{z}I-A)^{-1}\mathscr{z}]\\
\sum^{k-1}_{i=1}A^{k-i-1}Bu(i) = [(\mathscr{z}I-A)^{-1}BU(\mathscr{z})]
$$


---

**连续方程求解**




解可以写成

$$
\vec{x(t)} = \Phi(t-t_0) \vec{x(t_0)} + \int_{t_0}^t \Phi(t-\tau) B \vec{u(t)}d\tau
$$

其中第一项状态转移矩阵(State Transition Matrix) $\Phi(t-t_0) = e^{\mathbf{A}(t-t_0)}$ 描述了系统在没有输入的情况下，从初始状态开始的演化.第二项是一个卷积，描述输入与输出的关系

$$
x(k+1) = G(T)x(k) + H(T)u(k)
$$

其中

$$
G(T) = e^{AT},H(T) = \int^T_0 e^{A\tau}Bd\tau
$$

!!! note "计算转移矩阵$e^{AT}$"
    - 泰勒+化简
    - Laplace
    - 矩阵A对角化
    - Cayley-hamilton


??? tip "推导"

    $$
    \frac{d\vec{x(t)}}{dt} = Ax + Bu
    $$

    左右同乘以$e^{-At}$，移项得到：

    $$
    e^{-At} \frac{d\vec{x(t)}}{dt} - e^{-At}A\vec{x(t)} = e^{-At}B\vec{u(t)}
    $$

    $$
    \frac{d}{dt}(e^{-At}\vec{x(t)}) = e^{-At}B\vec{u(t)}
    $$

    对上式两边积分：

    $$
    e^{-At}\vec{x(t)} |_{t_0}^t  = \int_{0}^{t}e^{-A\tau}B\vec{u(\tau)}d\tau
    $$





## 能控能观性（定性）
### 能控性
是否可以从一个点控制到另一个点（不是轨迹控制）


$$
\mathbf{CO} = \begin{bmatrix}
B & AB & A^2B & \cdots & A^{n-1}B
\end{bmatrix}
$$

- $A$ 是系统矩阵。
- $B$ 是输入矩阵。
- $n$ 是系统的状态变量的维数。

通过计算能控矩阵 $\mathbf{CO}$ 的秩，可以判断系统是否能控。如果 $rank(\mathbf{CO}) = n$，则系统是能控的；否则，系统不是能控的。



### 能观性


## 系统的稳定性与李亚普诺夫稳定性(Lyapunov)

### 定义

Lyapunov: the origin(equilibrium point at the origin) is stable

$\forall t_0,\forall\epsilon>0,\exist \delta(t_0,\epsilon): ||x(t_0)||<\delta(t_0,\epsilon) \Rightarrow \forall t\ne t_0 ||x(t)||<\epsilon$

不会出边界（蓝色线条）

asympotically stable

$\exist\delta(t_0)>0: ||x(t_0)||<\delta(t_0) \Rightarrow \lim_{t\rightarrow\infty}||x(t)|| = 0$

最后会回到原点（棕色线条）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240926012538.png)

### 稳定条件

- 特征根具有负实部
- A的特征值
- z传递函数分布在单位圆内部

引入采样器会降低稳定性


### 劳斯判据

### 根轨迹

### 频域方法


## 极点配置、镇定、解耦

## 最优控制
