# 03 ｜ 泊松过程

## 独立增量过程

$\forall\;n\geq2$ 且 $n\in Z$ 与 $t_0<t_1<\dots<t_n$ ，增量 $X(t_1)-X(t_0),X(t_2)-X(t_1),\dots,X(t_n)-X(t_{n-1})$ 相互独立。

若 $\forall\;0\leq s<t$ ，增量 $X(t)-X(s)$ 的分布只依赖于 $t-s$ ，则为平稳独立增量过程。

## 齐次泊松过程

定义 $N(t)$ 表示 $(0,t\,]$ 内发生的"事件"数。

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda$ 的**齐次泊松过程**，则

**①** $N(0)=0$

**②** { $N(t);t\leq0$ } 为独立增量过程

**③** 对于 $\forall\;0\leq s<t$ ，有 $P(N(t)-N(s)=k)=\frac {[\lambda(t-s)]^k·e^{-\lambda(t-s)}}{k!},\quad k=0,1,2,\dots,$

**④** 对于 $\forall\;t>s\quad n\leq m\quad P(N_s=m\mid N_t=n)=C_n^m(\frac st)^m·(1-\frac st)^{n-m}$

​												$P(N_t=n\mid N_s=m)=P(N(t)-N(s)=n-m)$

### 均值函数

$\mu_N(t)=E[N(t)]=\lambda t$

### 方差函数

$D_N(t)=D[N(t)]=\lambda t$

### 自相关函数

$R_N(t_1,t_2)=E[N(t_1)·N(t_2)]=\lambda min(t_1,t_2)$

### 自协方差函数

$C_N(t_1,t_2)=Cov[N(t_1),N(t_2)]=\lambda min(t_1,t_2)+\lambda^2t_1t_2$

### 泊松过程的合成

若 { $X(t);t\leq0$ } 与 { $Y(t);t\leq0$ } 是相互独立的分别具有强度 $\lambda_1$ 和 $\lambda_2$ 的泊松过程，

则 { $N(t)=X(t)+Y(t);t\leq0$ } 是强度为 $\lambda_1+\lambda_2$ 的泊松过程。

### 泊松过程的分解

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda$ 的**泊松过程**，且对于事件 $N$ ，其中类型 $X$ 发生的概率为 $p$ ，类型 $Y$ 发生的概率为 $1-p$ ，则 { $X(t);t\leq0$ } 与 { $Y(t);t\leq0$ } 是相互独立的分别具有强度 $\lambda p$ 和 $\lambda (1-p)$ 的泊松过程。

### 与泊松分布相关的若干分布

**①** $W_n$ 是第 $n$ 个事件发生的时刻。

​	$F_{W_n}(t)=P(W_n\leq t)=P(N(t)\geq n)=1-\sum_{k=0}^{n-1}\frac{(\lambda t)^k e^{-\lambda t}}{k!}$

​	$f_{W_n(t)}=\frac{\lambda(\lambda t)^{n-1}}{(n-1)!}$

**②** $T_i=W_i-W_{i-1}$ 为第 $i$ 个事件和第 $i-1$ 个事件发生的时间间隔，则 $\forall\;i\quad T_i$ 均服从均值为 $\frac1\lambda$ 的指数分布。

​	$F_{T_i}(t)=P(T_i\leq t)=1-P(T_i>t)=1-P(N(t)<1)=1-P(N(t)=0)=1-e^{-\lambda t}$

**③** 若已知 $(0,t\,]$ 内恰好有一事件发生，则此事件的发生时刻在 $(0,t\,]$ 内均匀分布。

​	$P(T_1\leq s\mid N(t)=1)=\frac st\qquad 0<s\leq t$

## 非齐次泊松过程

$\lambda$ 不再为常数，而是 $t$ 的函数。

若计数过程 { $N(t);t\leq0$ } 是强度为 $\lambda(t)$ 的**非齐次泊松过程**，则

**①** $N(0)=0$

**②** { $N(t);t\leq0$ } 为独立增量过程

**③** 对于 $\forall\;0\leq s<t$ ，有$P(N(t)-N(s)=k)=\frac {[\int_s^t\lambda(u)du]^k·e^{-\int_s^t\lambda(u)du}}{k!},\quad k=0,1,2,\dots,$

**④** 均值函数 $E[N(t)]=\int_0^t \lambda(u)du$
