---
comments: true
---
# 现代控制理论
> 以此笔记致敬DR_CAN，感谢他的无私奉献


!!! note "资源汇总"
    === "学习路径"
        - DR_CAN [现代控制理论系列课程](https://www.bilibili.com/video/BV1yx411u7iX/)+王崇卫笔记
        - 课本阅读
        - 作业题目
        - 课件
        - 历年题目
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


## 总论

首先要理解**状态空间模型**，求传递函数

$$
\begin{aligned}
\dot{x} &= Ax + Bu \\
y &= Cx + Du
\end{aligned}
$$

其中，A是系统矩阵，B是输入矩阵，C是输出矩阵，D是直接传递矩阵；u是输入，y是输出，x是状态

**Open Loop**：其次要理解系统状态矩阵$\mathbf{A}$

- 特征值的实部决定了系统的稳定性，与$|\lambda I - A|$是一样的


**Close Loop**：
了解了稳定性之后，我们就可以通过设计闭环特征矩阵$\mathbf{A_{cl}}$来达到我们想要的效果：这里可以使用线性控制器、LQR来求解合适的K参数

**能控性和能观性**
- 能控性：是否可以从一个点控制到另一个点（不是路径控制）
- 能观性：并不是所有的状态都可以被观测到，所以需要设计观测器来估计系统的状态
- 可以根据observer观测的结果来设计控制器进而控制系统

[现代控制理论串讲 - DR_CAN](https://www.bilibili.com/video/BV1jW411J729/)

[现代控制理论重点概念梳理 - 知乎](https://www.zhihu.com/column/c_1131936304564453376)

[现代控制理论-重点知识汇总\_现代控制理论知识点总结-CSDN博客](https://blog.csdn.net/qq_31274209/article/details/105156993)

[控制理论——一小时从劝退到入门 - 知乎](https://zhuanlan.zhihu.com/p/683044170)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240922170358.png)


=== "反馈控制"
    跑步机上跑步 | 利用系统的输出量以参考数量的偏差进行控制，使系统的输出量与参考量之间的偏差尽可能小
=== "最优控制"
    田径赛跑 | 所谓最优控制就是寻找一个允许控制，使得被控系统在满足各种约束的条件下，使给定的性能指标达到最优

## 离散系统描述

零输入分量： $x(t) = 0,f(0^+) = f(0^-)$
零状态分量： $f^{n}(0^-) = 0$

### 数学模型

#### 采样

就像减肥过程称体重，比如说你每十分钟就测一次体重：这就会产生两个问题
- 体重并不是一个快速响应的系统，需要时间体现变化，会采集到大量重复信息
- 读取这个体重后开始参考制定计划，计划还没有制定出来，就需要进行下一次测量了

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241003142612.png)

#### z变换
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


#### 脉冲传递函数


脉冲传递函数：$G(z) = \frac{Y(z)}{U(z)}$ ，零初始条件下，系统的输出采样函数的z变换和输入采样函数的z变换的比值



零阶保持器： $G_h(s) = \frac{1-e^{-Ts}}{s},G(z) = 1$

trick: 先把$(1-z^{-1})$提出来

$$
G_h(s)\cdot G_p(s) = \frac{1-e^{-Ts}}{s} G_p(s) = (1-z^{-1})(\frac{G_p(s)}{s})
$$


**推导法**

> 一个讲的很好的视频：[离散系统关于脉冲传递函数求法\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1fQ4y1k7p9/)

闭环脉冲传递函数 $\Phi(z) = \frac{C(z)}{R(z)}$,如果前向通道第一个传递函数之前没有采样开关，就没有办法求解，只能求$C(z)$

- $\mathcal{Z}[A(s)B(z)] = A(z)\cdot B(z)$
- $\mathcal{Z}[A(s)B(s)] = AB(z) \ne A(z)B(z)$

要注意 $G_1G_2(z) \ne G_1(z)G_2(z)$

**Mason增益公式法**

回路只要有连在一起，就不能分开算z变换

!!! note "离散系统例子"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240926011136.png)
    控制体重的例子

    如果测体重测得太频繁，那么根本来不及计划


### 控制器设计

#### 模拟化设计



```matlab
s = tf('s');
z = tf('z',0.015);
D = 20*(s+4)/(s+10);
Back = (21.2-20*z^(-1))/(1.15-z^(-1)); %后向差分
zeroholder = c2d(D,0.015); %0阶保持器
Forward = 20*(z-0.94)/(z-0.85); %前向差分
Tustin = (19.16-18.05*z^(-1))/(1-0.86*z^(-1));%双线性变换

k = 8*(1-exp(-0.15))/(1-exp(-0.06));
P_Z = k*(1-z^(-1)*exp(-0.06))/(1-z^(-1)*exp(-0.15));%零极点配置法
step(Back,zeroholder,'--',Forward,'-',Tustin,'r--',P_Z,'y-',D,'g-');
legend;
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009143613.png)

??? note "z域根轨迹设计"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009150404.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009150424.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009150442.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009150510.png)


#### 数字化设计

!!! note "z域解析设计的方法主要有最少拍系统设计、无波纹最少拍系统设计、最小均方差系统设计等"
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009150948.png)

z域解析设计的方法关键是根据性能指标的需要选择合适的闭环脉冲传递函数$\Phi(z)$或闭环误差脉冲传递函数$\Phi_e(z)$。

1. 根据控制系统的性能指标要求和其它约束条件，确定所需的闭环脉冲传递函数 $\Phi(z)$

2. 求广义对象的脉冲传递函数 $G(z)$

$$
\begin{aligned}
G(z) &= \frac{B(z)}{A(z)} = Z\left[H(s)G_c(s)\right] = Z\left[\frac{1 - e^{-Ts}}{S}G_c(s)\right]
\end{aligned}
$$

3. 求取数字控制器的脉冲传递函数 $D(z)$

$$
\begin{aligned}
\Phi(z) &= \frac{D(z)G(z)}{1 + D(z)G(z)} \\
\Rightarrow \quad D(z) &= \frac{1}{G(z)} \cdot \frac{\Phi(z)}{1 - \Phi(z)}
\end{aligned}
$$

4. 根据 $D(z)$ 求取控制算法的递推计算公式

$$
\begin{aligned}
D(z) &= \frac{U(z)}{E(z)} = \frac{\sum_{i=0}^{m} b_i z^{-i}}{1 + \sum_{i=1}^{n} a_i z^{-i}}, \quad (n \geq m)
\end{aligned}
$$

$$
\begin{aligned}
U(z) &= \sum_{i=0}^{m} b_i z^{-i} E(z) - \sum_{i=1}^{n} a_i z^{-i} U(z) \\
\Rightarrow \quad u(k) &= \sum_{i=0}^{m} b_i e(k-i) - \sum_{i=1}^{n} a_i u(k-i)
\end{aligned}
$$

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


## 稳定性

### Lyapunov稳定性定义

**Lyapunov: the origin(equilibrium point at the origin) is stable**（在于有界）

$\forall t_0,\forall\epsilon>0, \exists \delta(t_0,\epsilon): ||x(t_0)||<\delta(t_0,\epsilon) \Rightarrow \forall t\ne t_0 ||x(t)||<\epsilon$

$x(t_0)$是起始点，给定$\epsilon$和$\delta$不会出边界（蓝色线条）

**asymptotically stable**（在于随着时间趋于零）

$\exists \delta(t_0)>0: ||x(t_0)||<\delta(t_0) \Rightarrow \lim_{t\rightarrow\infty}||x(t)|| = 0$

最后会回到原点（棕色线条）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240926012538.png)

### 稳定条件

- 特征根具有负实部
- A的特征值
- z传递函数分布在单位圆内部

引入采样器会降低稳定性

!!! note "trick"
    特征值之和等于矩阵的迹

    特征值之积等于矩阵的行列式

    可以用来迅速判断不稳定的情况

|stability|$\lambda = a+bi$|
|---|---|
|lyapunov| $a \le 0$|
|渐进| $a < 0$|
|不稳定| $a>0$|


### 处理非线性系统
对于一个非线性系统，其状态方程可以表示为：
$$\dot{x} = f(x,t)$$

Lyapunov函数 $V(x)$ 是一个关于系统状态 $x$ 的标量函数，它满足以下条件：
1. $V(x)$ 在系统平衡点 $x^*$ 处取得最小值，即 $V(x^*) = 0$。
2. $V(x)$ 在系统状态空间中是正定的，即对于任意的 $x \neq x^*$，都有 $V(x) > 0$。
3. 系统状态的导数 $\dot{V}(x)$ 在系统平衡点附近是负定的，即对于任意的 $x$ 在平衡点附近，都有 $\dot{V}(x) < 0$。

根据Lyapunov稳定性理论，如果存在一个满足上述条件的Lyapunov函数，那么系统在平衡点 $x^*$ 处是稳定的。如果 $\dot{V}(x)$ 在系统状态空间中始终为负，那么系统在平衡点 $x^*$ 处是渐近稳定的。

!!! tip "寻找v的过程是一门艺术"



PSD(positive simi definate)半正定

NSD(negative semi definate)

PD(positive definate)

ND(negative definate)

### 劳斯判据

### 根轨迹

### 频域方法


## 系统设计
### 状态矩阵（重中之重）
$$
\dot{x} = \mathbf{A_{cl}}x
$$

其中，$\mathbf{A}$ 的特征值$\lambda$

1. $\lambda$的实部决定的了收敛性和收敛速度
2. 如果极点是虚数，必定有共轭，且表示有振动

!!! note "拿到一个系统之后，需要先判定这个系统是不是可控的"


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

通过计算能控矩阵 $\mathbf{CO}$ 的秩，可以判断系统是否能控。如果 $rank(\mathbf{CO}) = n$，则系统是能控的(行满秩)；否则，系统不是能控的。

```matlab
Co = ctrb(A,B) # return the controllability matrix
```

在现实中需要考虑物理因素，所以不一定完全可控

#### 线性控制器



线性控制器：

选定k1和k2 $\rightarrow$ 设计闭环系统$A_{cl}$的特征值 $\rightarrow$ 控制系统表现

lqr 控制器

Q 侧重于系统状态
R 更侧重于控制器输入





??? note "例子"

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241003150854.png)

    === "建立状态空间模型"

        $$
        \begin{cases}
        \dot{x}_1 = \dot{\phi} = x_2 \\
        \dot{x}_2 = \ddot{\phi} = \frac{g}{L} \phi - \frac{1}{L} \ddot\delta= \frac{g}{L} x_1 - u
        \end{cases}
        $$

        其中，$\phi$ 是角度，$\delta$ 是控制输入，$g$ 是重力加速度，$L$ 是摆长。

        $$
        \begin{bmatrix}
        \dot{x}_1 \\
        \dot{x}_2
        \end{bmatrix}=
        \begin{bmatrix}
        0 & 1 \\
        \frac{g}{L} & 0
        \end{bmatrix}
        \begin{bmatrix}
        x_1 \\
        x_2
        \end{bmatrix}
        +
        \begin{bmatrix}
        0 \\
        -1
        \end{bmatrix}
        u
        $$


    === "开环系统"

        $$
        A = \begin{bmatrix}
        0 & 1 \\
        \frac{g}{L} & 0
        \end{bmatrix}, \quad |\lambda I - A| = 0 \implies \lambda^2 - \frac{g}{L} = 0 \implies \lambda = \pm \sqrt{\frac{g}{L}}
        $$

        由于特征值 $\lambda = \pm \sqrt{\frac{g}{L}}$ 是正实数，因此开环系统是不稳定的。

    === "能控性矩阵$Co$"

        $$
        C_0 = \begin{bmatrix} B & AB \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ -1 & 0 \end{bmatrix}
        $$

        $Rank(C_0) =2$,能控

    === "设计线性控制器"

        假设目标是设计一个反馈控制律，使得闭环系统的特征值 $\lambda_1$ 和 $\lambda_2$ 都等于 -1。

        为了实现这个目标，我们选择一个状态反馈控制律 $ u = - [k_1 \quad k_2] \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} $。

        $$
        \dot{x} = \begin{bmatrix} 0 & 1 \\ \frac{g}{L} & 0 \end{bmatrix} x + \begin{bmatrix} 0 \\ -1 \end{bmatrix} [k_1 \quad k_2] \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}= \begin{bmatrix} 0 & 1 \\ \frac{g}{L} + k_2 & 0 \end{bmatrix} x
        $$

        闭环系统的特征方程为：

        $$
        |\lambda I - A_{\text{cl}}| = 0 \implies \lambda^2 - (k_2 \lambda + \frac{g}{L} + k_1) = 0
        $$

        $$
        k_1 = -1 - \frac{g}{L}, \quad k_2 = -2
        $$

        因此，反馈控制律为：

        $$
        u = - [-1 - \frac{g}{L} \quad -2] \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = [1 + \frac{g}{L} \quad 2] \begin{bmatrix} \phi \\ \dot{\phi} \end{bmatrix}
        $$


!!! note "理解u"
    u是控制器的输入，随着系统输出x的变化而变化，所以可以看作是闭环的系统
    
    理论上，u可以随便选，但实际应用当中要考虑执行器的情况。比如自动驾驶场景，输入u是方向盘的角度，就是有界的。



### 能观性
!!! note ""
    Kálmán published several seminal papers during the sixties, which rigorously established what is now known as the state-space representation of dynamical systems. He introduced the formal definition of a system, the notions of controllability and observability
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241003163103.png)

**observer**: 通过系统的输入和输出来估计系统的状态

luenberger observer 龙贝格

卡尔曼滤波器就是随机系统的状态观测器

### 分离原理

最好观测器的收敛速度要比控制器要快

### 根据观测器设计控制器



