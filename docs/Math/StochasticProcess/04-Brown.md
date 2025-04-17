# 布朗运动

## 定义

直线上一质点每隔 $\Delta t$ 等概率向左或向右移动距离 $\Delta x$ ，且每次移动相互独立 ，$X(t)$ 为 $t$ 时刻质点的位置。

**①** $X(t)\sim N(0,\sigma^2)$

**②** $X(0)=0$

**③** $\forall\;0\leq s<t\quad X(t)-X(s)\sim N(0,\sigma^2(t-s))$

一般考虑**标准布朗运动**，即 $B(t)\sim N(0,t)\qquad (\sigma^2=1)$	且 $C_B(t_1,t_2)=min(t_1,t_2)$

## 标准布朗运动的性质

**$Markov$ 性：** $\forall\;t\quad$	{ $B(t+s)-B(t);s\geq 0$ } 是标准布朗运动。

**自相似性：** $\forall\;a\neq0\quad$	{ $\frac1aB(a^2t);t\geq 0$ } 是标准布朗运动。

**0 与 $\infty$ 对称性：** 令 $\overset{\sim}B(t)=\begin{cases}tB(\frac 1t)\quad t>0\\[2ex]0\qquad\quad t=0\end{cases}$ 	则 { $\overset{\sim}B(t);t\geq0$ } 是标准布朗运动。

## 相关分布

**①** $T_a$ 是首次击中 $a$ 的时间。

​	$\forall\;a>0\quad F_{T_a}(t)=P(T_a\leq t)=\underline {P(\underset{0\leq s\leq t}{max}\,B(s)\geq a)=2P(B(t)\geq a)}=2[1-\Phi(\frac{\mid a\mid}{\sqrt t})]$

**②** $X(t)=\mid \underset{0\leq s\leq t}{min}\,B(s)\mid$

​	$F_{X(t)}(y)=P(X(t)\leq y)\overset{B_1(s)=-B(s)}{====}P(\underset{0\leq s\leq t}{max}\,B_1(s)\leq y)=1-2P(B_1(t)>y)=2\Phi(\frac y{\sqrt t})-1\qquad(t\geq 0)$

**③** $P(\underset{0\leq s\leq t}{min}\,B(s)\leq -y)=P(\underset{0\leq s\leq t}{max}\,B(s)\geq y)$	（对称性）

## 布朗桥运动

$X(t)=B(t)-tB(1)\quad 0\leq t \leq 1$

**①** $X(0)=X(1)=0$	**②** 为正态过程	**③** $\mu_X(t)=0$ 且 $\forall\;0<s<t<1\quad C_X(s,t)=s(1-t)$

## 例题

**①** 用 $N(t)$ 表示在 $(0,t\,]$ 小时内收到的短信数目。设 { $N(t);t\leq0$ } 是强度为 $\lambda=5$ 条的泊松过程，且每条短信独立地以概率 0.6 是垃圾短信。

设垃圾短信的数目为 $N_1(t)$ ，正常短信的数目为 $N_2(t)$ 。

 { $N_1(t);t\leq0$ } 是强度为 $\lambda p=5\times0.6=3$ 条的泊松过程，{ $N_2(t);t\leq0$ } 是强度为 $\lambda (1-p)=5\times0.4=2$ 条的泊松过程。

则

（1）1 小时内收到 2 条短信的概率为 $P(N(1)=2)=\frac {5^2·e^{-5}}{2!}=\frac {25}2e^{-5}$

（2）1 小时内收到的垃圾短信数目为 2 条的概率为 $P(N_1(1)=2)=\frac {3^2·e^{-3}}{2!}=\frac92e^{-3}$

（3）若已知 3 小时内恰好收到一条短信，则这条短信是在第 2 个小时内收到的概率为

​		$P(N(2)-N(1)=1\mid N(3)=1)=\frac{P(N(3)-N(2)+N(1)=0,N(2)-N(1)=1)}{P(N(3)=1)}=\frac{{P(N(3)-N(2)=0}·P(N(2)-N(1)=1)·P{(N(1)=0)}}{P(N(3)=1)}=\frac{e^{-5}·5e^{-5}·e^{-5}}{15e^{-15}}=\frac 13$

（4）1 小时内至少收到 1 条短信，且在 3 小时内恰好收到两条短信的概率为 

​		$P(N(3)-N(1)=1,N(1)=1)+P(N(3)-N(1)=0,N(1)=2)=10e^{-10}·5e^{-5}+e^{-10}·\frac{5^2}{2!}e^{-5}=62.5e^{-15}$

（5）若已知 1 小时内至多收到 2 条短信，则至少有 1 条垃圾短信的概率为

​		$P(N_1(1)\geq1\mid N(1)\leq2)=\frac{P(N_1(1)=1,N(1)\leq2)+P(N_1(1)=2,N(1)\leq2)}{P(N(1)\leq2)}=\frac{P(N_1(1)=1,N_2(1)=1)+P(N_1(1)=1,N_2(1)=0)+P(N_1(1)=2,N_2(1)=0)}{P(N(1)\leq2)}$

​										$=\frac{e^{-5}·(3\times2+3+3^2/2)}{e^{-5}·(1+5+12.5)}=\frac {27}{37}$

**②** 设 { $B(t);t\geq0$ } 是标准布朗运动，则

（1）$B(3)-2B(1)$ 服从 $N(0,3)$ 分布（$B(3)-2B(1)=B(3)-B(1)-B(1)\sim N(0,2+1)=N(0,3)$）

（2）$Cov(B(3)-2B(1),B(2))=D[B(2)-B(1)]-D[B(1)]=0$

（3）$P(B(5.5)>5\mid B(1.1)=3,B(1.5)=1)=P(B(5.5)-B(1.5)>4)=1-\Phi(2)=0.02$

（4）$P(\underset{0\leq t\leq6.25}{max}\,B(t)<2.5)=1-P(\underset{0\leq t\leq6.25}{max}\,B(t)\geq2.5)=1-2[1-P(B(6.25)<2.5)]=2\Phi(1)-1=0.68$

## 解题方式

**①** 泊松过程的合成与分解。

**②** 一定要将不独立的变量转化为独立增量。

**③** 布朗运动的 $Markov$ 性。

**④** 各种相关分布的结论。
