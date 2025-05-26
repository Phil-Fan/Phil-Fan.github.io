# 04 | 布朗运动

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



**②** 设 { $B(t);t\geq0$ } 是标准布朗运动，则

（1）$B(3)-2B(1)$ 服从 $N(0,3)$ 分布（$B(3)-2B(1)=B(3)-B(1)-B(1)\sim N(0,2+1)=N(0,3)$）

（2）$Cov(B(3)-2B(1),B(2))=D[B(2)-B(1)]-D[B(1)]=0$

（3）$P(B(5.5)>5\mid B(1.1)=3,B(1.5)=1)=P(B(5.5)-B(1.5)>4)=1-\Phi(2)=0.02$

（4）$P(\underset{0\leq t\leq6.25}{max}\,B(t)<2.5)=1-P(\underset{0\leq t\leq6.25}{max}\,B(t)\geq2.5)=1-2[1-P(B(6.25)<2.5)]=2\Phi(1)-1=0.68$

## 解题方式

