# 04 | 布朗运动、维纳过程

## Cheet Sheet
* $\forall\;0\leq s<t\quad X(t)-X(s)\sim N(0,\sigma^2(t-s))$
* 均值函数：$\mu_B(t)=0$
* 方差函数：$D_B(t)=t$
* 自协方差函数：$C_B(t,s) =min(t,s)\qquad t,s>0$
* 自相似性：$\forall\;a\neq0\quad$	{ $\frac1aB(a^2t);t\geq 0$ } 是标准布朗运动。
* $0-\infty$对称性：$\overset{\sim}B(t)=\begin{cases}tB(\frac 1t)\quad t>0\\[2ex]0\qquad\quad t=0\end{cases}$ 	则 { $\overset{\sim}B(t);t\geq0$ } 是标准布朗运动。
* 首次击中时间：$P\left(\max_{s\leq t}B(s)\geq a\right) = P(T_a \leq t) = 2P(B(t)\geq a),\quad a > 0$


## 定义

直线上一质点每隔 $\Delta t$ 等概率向左或向右移动距离 $\Delta x$ ，且每次移动相互独立 ，$X(t)$ 为 $t$ 时刻质点的位置。

**①** $X(t)\sim N(0,\sigma^2)$

**②** $X(0)=0$

**③** $\forall\;0\leq s<t\quad X(t)-X(s)\sim N(0,\sigma^2(t-s))$

一般考虑**标准布朗运动**，即 $B(t)\sim N(0,t)$
$\qquad (\sigma^2=1)$	且 $C_B(t_1,t_2)=min(t_1,t_2)$

## 标准布朗运动的性质

1. 齐次的独立增量过程
2. 正态过程，分布完全由均值函数和自协方差函数确定
3. 数字特征
    * 均值函数：$\mu_B(t)=0$
    * 方差函数：$D_B(t)=t$
    * 自协方差函数：
        
        $$
        \begin{aligned}
        C_B(t,s) &= R_B(t,s) = D_B[\min (s,t)]\\
        &=min(t,s)\qquad t,s>0
        \end{aligned}
        $$


### 布朗运动判定

布朗运动当且仅当它是正态过程，$E(B(t))=0$且$E[B(t)B(s)]=t\wedge s.$


### Markov 性 

$\forall\;t\quad$	{ $B(t+s)-B(t);s\geq 0$ } 是标准布朗运动。

**起点的选取是任意的**


??? note "证明"

    我们证明 $\{B(t); t \geq 0\}$ 是布朗运动。已知 $B(t)$ 是一个均值为 0，协方差函数为

    $$
    R_B(s,t) = \mathbb{E}[B(s)B(t)] = \min(s,t)
    $$

    的随机过程。我们进行如下验证：

    ---

    **(1) 均值与方差**

    $$
    \begin{aligned}
    \mathbb{E}[B(t) - B(s)] &= \mathbb{E}[B(t)] - \mathbb{E}[B(s)] = \mu_B(t) - \mu_B(s) = 0, \\
    \mathbb{E}[(B(t) - B(s))^2] &= \mathbb{E}[B(t)^2] + \mathbb{E}[B(s)^2] - 2\mathbb{E}[B(t)B(s)] \\
    &= R_B(t,t) + R_B(s,s) - 2R_B(t,s) \\
    &= t + s - 2\min(t,s) = |t - s|.
    \end{aligned}
    $$

    因此对于 $0 \leq s < t$，有

    $$
    B(t) - B(s) \sim \mathcal{N}(0, t - s).
    $$

    ---

    **(2) 独立增量**

    设任意的

    $$
    s_1 < t_1 \leq s_2 < t_2,
    $$

    我们计算两个增量的协方差：

    $$
    \begin{aligned}
    \mathbb{E}[(B(t_1) - B(s_1))(B(t_2) - B(s_2))] 
    &= \mathbb{E}[B(t_1)B(t_2)] - \mathbb{E}[B(s_1)B(t_2)] - \mathbb{E}[B(t_1)B(s_2)] + \mathbb{E}[B(s_1)B(s_2)] \\
    &= R_B(t_1, t_2) - R_B(s_1, t_2) - R_B(t_1, s_2) + R_B(s_1, s_2) \\
    &= \min(t_1, t_2) - \min(s_1, t_2) - \min(t_1, s_2) + \min(s_1, s_2) \\
    &= t_1 - s_1 - t_1 + s_1 = 0.
    \end{aligned}
    $$

    因此，增量 $B(t_1) - B(s_1)$ 与 $B(t_2) - B(s_2)$ 互相独立。

    结合 $B(0) = 0$，可知 $\{B(t); t \geq 0\}$ 是**具有独立增量的高斯过程**。

    ---

    **(3) 正态过程**

    对任意整数 $n$ 和时间点

    $$
    0 \leq t_1 < t_2 < \cdots < t_n,
    $$

    考虑随机向量

    $$
    (B(t_1), B(t_2), \ldots, B(t_n)).
    $$

    记增量为

    $$
    X_i = B(t_i) - B(t_{i-1}),\quad i=1,2,\ldots,n,\quad\text{其中 } t_0 := 0,
    $$

    则

    $$
    (B(t_1), B(t_2), \ldots, B(t_n)) = (X_1, X_1 + X_2, \ldots, X_1 + \cdots + X_n),
    $$

    是增量变量 $X_1, X_2, \ldots, X_n$ 的线性组合。

    由于每个增量 $X_i$ 都服从正态分布且两两独立，因此整个向量服从多元正态分布。

    故 $\{B(t); t \geq 0\}$ 是正态过程。

    ---

    **结论：**

    综上所述，$\{B(t); t \geq 0\}$ 是满足以下条件的随机过程：

    * $B(0) = 0$；
    * 有独立增量；
    * 每个增量 $B(t) - B(s) \sim \mathcal{N}(0, t - s)$；
    * 是正态过程。

    因此，$\{B(t); t \geq 0\}$ 是一个布朗运动。 $\blacksquare$


多元正太分布的线性变换依然是正态分布


### 自相似性

$\forall\;a\neq0\quad$	{ $\frac1aB(a^2t);t\geq 0$ } 是标准布朗运动。




布朗运动的**自相似性（self-similarity**是它最核心、最优美的性质之一。在直觉上，它表达的是：

> **把布朗运动放大或缩小，看起来就像是原来的布朗运动。**



自相似性是：

* **分形**的核心特征（布朗运动是随机分形）
* 在金融中解释“不同时间尺度价格走势看起来相似”的数学基础
* 分析长时间行为时简化问题的重要工具



### 0 与 $\infty$ 对称性

令 $\overset{\sim}B(t)=\begin{cases}tB(\frac 1t)\quad t>0\\[2ex]0\qquad\quad t=0\end{cases}$ 	则 { $\overset{\sim}B(t);t\geq0$ } 是标准布朗运动。


> 把布朗运动做“时间倒转 + 振幅缩放”，你又得到了一个标准布朗运动。
>


| 应用领域     | 举例说明|
| -------- | ----------------------------------------------------- |
| **路径分析** | 某些 hitting time 与 maximum/minimum 问题在 0 和 ∞ 对称变换下形式不变 |
| **随机分形** | 说明布朗运动具有尺度不变性，是分形过程                                   |
| **金融建模** | 定价模型中分析小时间步和大时间尺度行为的一致性                               |
| **理论物理** | 在量子场论中，布朗运动模型是路径积分的基础，体现“红外-紫外对称”思想                   |





!!! info "**分形（Fractal）**是一种数学和自然界中常见的结构，它具有**局部和整体相似**的特点，是许多复杂系统的本质特征。"
    虽然“分形”没有一个唯一公认的严格定义，但以下是 Benoît Mandelbrot（曼德博，分形理论之父）给出的**经典定义之一**：

    > **一个几何形状，如果它的 Hausdorff 维数（分形维数）严格大于其拓扑维数，则称为分形。**



    | 图形       | 拓扑维数（整数） | 分形维数（可为小数） |
    | -------- | -------- | ---------- |
    | 直线段      | 1        | 1          |
    | 曼德博集     | 1        | 2          |
    | 柯赫雪花曲线   | 1        | ≈ 1.2619   |
    | 西尔皮斯基三角形 | 1        | ≈ 1.5849   |

    所以“**维数大于形状能容纳的维度**”是分形的关键特征之一。

    ---


    > **一个图形，在放大后细节仍然看起来和整体结构相似，且无限复杂，这种结构叫分形。**

    这种“**局部与整体相似（自相似）**”的性质，在自然界和数学中非常常见。


## 首次击中时

$$
\begin{aligned}
\forall\;a>0\quad F_{T_a}(t)&=P(T_a\leq t)
\end{aligned}
$$



$$
\boxed{P\left(\max_{s\leq t}B(s)\geq a\right) = P(T_a \leq t) = 2P(B(t)\geq a)},\quad \text{对 } a > 0
$$

* $\max_{s\leq t} B(s)$：布朗运动在时间区间 $[0,t]$ 中的最大值
* $T_a = \inf\{s > 0 : B(s) = a\}$：布朗运动首次达到 $a$ 的时间
* $B(t) \sim \mathcal{N}(0,t)$：在时间 $t$ 的布朗运动服从均值 0、方差 $t$ 的正态分布


??? note "直观解释"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250526193135.png)

    > 以价格为例，相当于求价格最高点不低于/不高于
    
    * 左侧：$P(\max_{s\leq t}B(s)\geq a)$：表示“在时间 $t$ 以内，布朗运动是否**曾经**达到过或超过了 $a$”的概率。
    * 中间：$P(T_a \leq t)$：布朗运动首次达到 $a$ 的时间是否**早于或等于** $t$。这两个其实是同一件事：只要在 $[0,t]$ 里最大值超过了 $a$，那么 $T_a \leq t$。
    * 右边：$P(B(t)\geq a)$：布朗运动在**正好**时刻 $t$ 达到 $a$ 或更高的概率。因为布朗运动是对称过程（正态分布对称），所以：

      $$
      P(B(t) \geq a) = P(B(t) \leq -a)
      $$

    * 但我们要的是“**曾经达到** $a$”的概率，远大于“**正好在终点**超过 $a$”的概率，因此乘 2：

      $$
      \boxed{P(\max_{s\leq t}B(s)\geq a) = 2P(B(t)\geq a)}
      $$

    这个结果也叫做 **反射原理（reflection principle）** 的直接推论。


    | 表达式                             | 含义                      |
    | ------------------------------- | ----------------------- |
    | $P(\max_{s\leq t} B(s) \geq a)$ | 布朗运动在 $[0,t]$ 曾超过 a 的概率 |
    | $P(T_a \leq t)$                 | 首次达到 $a$ 的时间早于 $t$ 的概率  |
    | $2P(B(t) \geq a)$               | 利用布朗运动对称性 + 反射原理的结果     |



注意不同的形式：

- 最大值小于$a$的概率

$$
\begin{aligned}
P(\underset{0\leq s\leq t}{max}\,B(s)\leq a)&= 1-2P(B(t)\geq a)=2\Phi(\frac{\mid a\mid}{\sqrt t})
\end{aligned}
$$

- 绝对值的形式：**最小值一定小于0，所以可以直接脱去绝对值符号**

    $X(t)=\mid \underset{0\leq s\leq t}{min}\,B(s)\mid = -\underset{0\leq s\leq t}{max}\,B_1(s)$

    $$
    \begin{aligned}
    F_{X(t)}(y)=&P(X(t)\leq y)\overset{B_1(s)=-B(s)}{\longleftrightarrow}P(\underset{0\leq s\leq t}{max}\,B_1(s)\leq y)\\
    =&1-2P(B_1(t)>y)\\
    =&2\Phi(\frac y{\sqrt t})-1\qquad(t\geq 0)
    \end{aligned}
    $$



- 对称性 
    
    $$
    P(\underset{0\leq s\leq t}{min}\,B(s)\leq -y)=P(\underset{0\leq s\leq t}{max}\,B(s)\geq y)
    $$	

- 换元

$$
\begin{aligned}
P\{\underset{0\leq s\leq t}{max}\,\left[B(s)-B(t)\right]\leq x\}=&P\{\underset{0\leq s\leq t}{max}\,\left[B(t)- B(s)\right]\leq x\},\qquad x>0\\
=&P\{\underset{0\leq s\leq t}{max}\,B(t-s)\leq x\}\\
\overset{u = t-s}\longleftrightarrow &P\{\underset{0\leq u\leq t}{max}\,B(u)\leq x\}\\
=& 1-2P(B(t)\geq x)
\end{aligned}
$$


## 布朗桥运动

$X(t)=B(t)-tB(1)\quad 0\leq t \leq 1$

- $X(0)=X(1)=0$	

- 为正态过程	

- 均值：

    $$
    \mu_X(t) = E[X(t)] = E[B(t) - tB(1)] = E[B(t)] - tE[B(1)] = 0 - t \cdot 0 = 0
    $$

- 协方差（$0 < s < t < 1$）：

    $$
    \begin{aligned}
    C_X(s, t) &= \operatorname{Cov}(X(s), X(t)) \\
    &= \operatorname{Cov}(B(s) - sB(1),\; B(t) - tB(1)) \\
    &= \operatorname{Cov}(B(s), B(t)) - t\operatorname{Cov}(B(s), B(1)) - s\operatorname{Cov}(B(1), B(t)) + st\operatorname{Cov}(B(1), B(1)) \\
    &= \min(s, t) - t\min(s, 1) - s\min(1, t) + st \\
    &= s - t s - s t + s t \\
    &= s(1 - t)
    \end{aligned}
    $$
    

## 例题
1. 方差、协方差的解法
2. 写成增量的形式，增量之间互相独立，就不需要考虑协方差的问题了


### 数字特征计算
!!! example "设 { $B(t);t\geq0$ } 是标准布朗运动，则"

    （1）$B(3)-2B(1)$ 

    服从 $N(0,3)$ 分布（$B(3)-2B(1)=B(3)-B(1)-B(1)\sim N(0,2+1)=N(0,3)$）

    ---

    （2）$Cov(B(3)-2B(1),B(2))$

    $$
    \begin{aligned}
    Cov(B(3)-2B(1),B(2))&=D[B(2)-B(1)]-D[B(1)]=0
    \end{aligned}
    $$

    ---

    （3）$P(B(5.5)>5\mid B(1.1)=3,B(1.5)=1)$

    转化成增量形式进行计算

    $$
    \begin{aligned}
    P(B(5.5)>5\mid B(1.1)=3,B(1.5)=1)&=P(B(5.5)-B(1.5)>4)\\
    &=1-\Phi(2)=0.02
    \end{aligned}
    $$

    ---

    （4）$P(\underset{0\leq t\leq6.25}{max}\,B(t)<2.5)$

    $$
    \begin{aligned}
    P(\underset{0\leq t\leq6.25}{max}\,B(t)<2.5)&=1-P(\underset{0\leq t\leq6.25}{max}\,B(t)\geq2.5)\\
    &=1-2[1-P(B(6.25)<2.5)]\\
    &=2\Phi(1)-1=0.68
    \end{aligned}
    $$


#### 4.21

!!! example "设 $\{B(t);\, t \geq 0\}$ 是标准布朗运动，求："

    (1) $P\{B(3.6) \leq 1 \mid B(1.6) = 0.8,\, B(2.39) = -0.1\}$；

    由布朗运动的独立增量性质，有

    $$
    \begin{align*}
    &P\{B(3.6) \leq 1 \mid B(1.6) = 0.8,\, B(2.39) = -0.1\} \\
    &= P\{B(3.6) - B(2.39) \leq 1 - (-0.1)\} \\
    &= P\{B(3.6) - B(2.39) \leq 1.1\}
    \end{align*}
    $$

    又 $B(3.6) - B(2.39) \sim N(0,\, 3.6 - 2.39 = 1.21)$，因此

    $$
    P\{B(3.6) - B(2.39) \leq 1.1\} = \Phi(1)
    $$

    ---

    (2)$\operatorname{Cov}(B(8) - B(4),\, B(6))$；

    $$
    \begin{align*}
    \operatorname{Cov}(B(8) - B(4),\, B(6)) 
    &= \operatorname{Cov}(B(8),\, B(6)) - \operatorname{Cov}(B(4),\, B(6)) \\
    &= \min\{8, 6\} - \min\{4, 6\} \\
    &= 6 - 4 = 2
    \end{align*}
    $$

    ---

    (3) $D(2B(1) + B(2))$。


    $$
    \begin{align*}
    D(2B(1) + B(2)) 
    &= D(2B(1)) + D(B(2)) + 2\,\operatorname{Cov}(2B(1),\, B(2)) \\
    &= 4D(B(1)) + D(B(2)) + 4\,\operatorname{Cov}(B(1),\, B(2)) \\
    &= 4 \times 1 + 2 + 4 \times 1 \\
    &= 10
    \end{align*}
    $$

### 相似性



!!! example "设$\{B(t),t\geq0\}$是标准布朗运动，求"

    (1) $P\{B(0.5)\leq1|B(1)=1,B(2)=2\}$;




    解：$\{B(t);t\geq0\}$是标准布朗运动.又$B(t)=t\bar{B}(1/t)$, 所以


    $$
    P\{B(0.5)\leq1|B(1)=1,B(2)=2\}\\
    =P\{0.5\bar{B}(2)\leq1|\bar{B}(1)=1,2\bar{B}(0.5)=2\}\\
    =P\{\bar{B}(2)\leq2|\bar{B}(1)=1,\bar{B}(0.5)=1\}\\
    =P\{\bar{B}(2)-\bar{B}(1)\leq1\}=\Phi(1)=0.8413
    $$

    ---

    (2) 在$B(1)=1,B(2)=2$的条件下，$B(0.5)$服从什么分布？

    即是在$\bar{B}(1)=1,\bar{B}(0.5)=1$的条件下，

    $$
    \bar{B}(2)=1+(\bar{B}(2)-\bar{B}(1))\sim N(1,1)
    $$

    所以$B(0.5)=0.5\bar{B}(2)\sim N(0.5,0.25)$.



#### 4.27


!!! example "设 $\{B(t); t \geqslant 0\}$ 是标准布朗运动，计算："

    (1) $P\left(B\left(\frac{1}{10}\right) \geqslant 1.5 \mid B\left(\frac{1}{6}\right) = 2,\, B\left(\frac{1}{4}\right) = 2.4\right)$；

    由布朗运动的自相似性，令 $\widetilde{B}(t) = 12 B\left(\frac{t}{12}\right)$，则有

    $$
    \begin{align*}
    &P\left(B\left(\frac{1}{10}\right) \geqslant 1.5 \mid B\left(\frac{1}{6}\right) = 2,\, B\left(\frac{1}{4}\right) = 2.4\right) \\
    &= P\left(\widetilde{B}(10) \geqslant 15 \mid \widetilde{B}(6) = 12,\, \widetilde{B}(4) = 8\right) \\
    &= P\left(\widetilde{B}(10) - \widetilde{B}(6) \geqslant 3\right) \\
    &= 1 - \Phi(1.5)
    \end{align*}
    $$

    ---

    (2) 在 $B\left(\frac{1}{6}\right) = 2,\, B\left(\frac{1}{4}\right) = 2.4$ 的条件下，求 $B\left(\frac{1}{10}\right)$ 的条件分布。


    因为自相似性，我们要求条件分布，即求$F(B(\frac{1}{10})\leq x| B(\frac{1}{6})=2, B(\frac{1}{4})=2.4)$

    根据自相似性，已知，$\widetilde{B}(6)=12$，$\widetilde{B(4)}=9.6$

    又因为Markov性质，不需要管$\widetilde{B}(4)$，所以

    $$
    \widetilde{B}(10)=\widetilde{B}(10)-\widetilde{B}(6)+12\thicksim N(12,4)
    $$

    所以，这里构造的时候，要构造差值，要注意加上常数会改变均值

    最后使用自相似性质

    $$
    B(\frac{1}{10})\sim\frac{1}{10}\widetilde{B(10)}\sim N(\frac{6}{5},\frac{1}{25})
    $$


### 首次击中时

脑子里回想正态分布pdf的图像

#### 4.29
!!! note "设 $\{B(t); t \geqslant 0\}$ 是标准布朗运动，对任意 $t>0, x>0$"

    (1) $P(|B(t)| \leqslant x)$；

    解
    
    $$
    \begin{align*}
    P(|B(t)| \leqslant x) 
    &= P(-x \leqslant B(t) \leqslant x) \\
    &= 2\Phi\left(\frac{x}{\sqrt{t}}\right) - 1
    \end{align*}
    $$

    --- 

    (2) $P\left(\max_{0 \leqslant s \leqslant t} B(s) - B(t) \leqslant x\right)$

    解

    $$
    \begin{align*}
    &P\left(\max_{0 \leqslant s \leqslant t} B(s) - B(t) \leqslant x\right) \\
    &= P\left(\max_{0 \leqslant s \leqslant t} (B(s) - B(t)) \leqslant x\right) \quad \text{（换元，令 $u = t - s$）} \\
    &= P\left(\max_{0 \leqslant u \leqslant t} B(u) \leqslant x\right) = 1 - P\left(\max_{0 \leqslant u \leqslant t} B(u) \geqslant x\right) \\
    &= 1 - 2P(B(t) > x) \\
    &= 1 - 2\left[1 - \Phi\left(\frac{x}{\sqrt{t}}\right)\right] = 2\Phi\left(\frac{x}{\sqrt{t}}\right) - 1
    \end{align*}
    $$