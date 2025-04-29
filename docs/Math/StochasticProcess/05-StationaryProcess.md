# 05 | 平稳过程

## 严平稳过程

{ $X(t);t\in T$ } 中所有 $X_t$ 同分布， 且 $\forall\;n\geq2\quad(X_{t_1},X_{t_2},\dots,X_{t_n},)$ 的分布仅与时间差 $t_i-t_{i-1}$ 有关，而与起始时间 $t_1$ 无关。

## 宽平稳过程

存在二阶矩的严平稳过程。平稳过程均指**宽平稳过程**。

### 均值函数

$\mu_X(t)=E[X(t)]=E[X(0)]\overset{记为}\Longrightarrow\mu_X\;(常数)$

### 方差函数

$D[X(t)]=R_X(0)-\mu_X^2\;(常数)$

### 自相关函数

$E[X(t)X(t+\tau)]=E[X(0)X(\tau)]=R_X(\tau)\;(为时间差的函数)$

$E[X^2(t)]=R_X(0)\;(常数)$

$E[X_{t_1}X_{t_2}]=R_X(t_2-t_1)$

### 自协方差函数

$C_X(\tau)=R_X(\tau)-\mu_X^2$

### 平稳相关

若 { $X(t);t\in T$ }、{ $Y(t);t\in T$ } 是两个平稳过程，$X(t),Y(t)$ 的互相关函数也为时间差 $\tau$ 的函数$\overset{记为}\Longrightarrow R_{XY}(\tau)$

称 $X(t),Y(t)$ 是平稳相关/联合（宽）平稳的。

**①** $R_X(0)=E[X^2(t)]=\psi_X^2\geq0$

**②** $R_X(-\tau)=R_X(\tau)\quad(偶函数)\qquad R_{XY}(-\tau)=R_{YX}(\tau)\quad(非奇非偶)$

**③** $\mid R_X(\tau)\mid\leq R_X(0)\qquad\qquad\quad\mid C_X(\tau)\mid\leq C_X(0)=\sigma_X^2$

 	$\mid R_{XY}(\tau)\mid^2\leq R_X(0)R_Y(0)\quad\mid C_{XY}(\tau)\mid^2\leq C_X(0)C_Y(0),$

​	相关/协方差函数在时间差 $\tau$ 为 0 时取得最大值。

**④** $R_X(\tau)$ 是非负定的，即 $\forall\;t_1,t_2,\dots,t_n\in T$ 和 $\forall\;a_1,a_2,\dots,a_n\in R$ ，有$\sum_{i,j=1}^n R_X(t_i-t_j)a_ia_j\geq0$

**⑤** { $X(t);t\in T$ } 是周期为 $T_0$ 的平稳过程 $\Leftrightarrow$ $R_X(t)$ 是周期为 $T_0$ 的函数。

## 各态历经性

### 时间均值

$<X(t)>=\underset{T\rightarrow+\infty}\lim\frac 1{2T}\int_{-T}^TX(t)dt$

$<X_n>=\underset{N\rightarrow+\infty}\lim \frac 1N\sum_{n=1}^NX_n$

### 时间相关函数

$<X(t)X(t+\tau)>=\underset{T\rightarrow+\infty}\lim\frac 1{2T}\int_{-T}^TX(t)X(t+\tau)dt$

$<X_nX_{n+m}>=\underset{N\rightarrow+\infty}\lim \frac 1N\sum_{n=1}^NX_nX_{n+m}$

### 各态历经性

**均值具有各态历经性：**$P(<X(t)>=\mu_X)=1$ / $P(<X_n>=\mu_X)=1$		（即时间均值恒等于均值函数）

**自相关函数具有各态历经性：**$\forall\;\tau\quad P(<X(t)X(t+\tau)>=R_X(\tau))=1$		（即时间相关函数恒等于自相关函数）

**各态历经过程：**均值和自相关函数都具有各态历经性。

### 均值各态历经定理

在 $\underset{\tau\rightarrow+\infty}\lim R_X(\tau)$ 存在的条件下，若 $\underset{\tau\rightarrow+\infty}\lim R_X(\tau)=\mu_X^2$ ，则**均值具有各态历经性**，反之不具有。

## 平稳过程的功率谱密度

### 谱密度

$S_X(\omega)$ 是 $\omega$ 的非负实偶函数，与自相关函数 $R_X(\tau)$ 是一对 $Fourier$ 变换对。

$S_X(\omega)=\int_{-\infty}^{+\infty}R_X(\tau)e^{-i\omega\tau}d\tau$

$R_X(\tau)=\frac1{2\pi}\int_{-\infty}^{+\infty}S_X(\omega)e^{i\omega\tau}d\omega$

统称**维纳-辛钦公式**。

因为 $S_X\;R_X$ 都是实偶函数，所以 $R_X\overset{F}\longleftrightarrow S_X\quad S_X\overset{F}\longleftrightarrow 2\pi R_X$

### 常用 $Fourier$ 变换对

**①** $e^{-a\mid\tau\mid}\overset{F}\longleftrightarrow\frac{2a}{a^2+\omega^2}$

**②** $\begin{cases}1-\frac{\mid\tau\mid}{T}\quad\mid\tau\mid\leq T\\[2ex]0\quad\mid\tau\mid>T\end{cases}\overset{F}\longleftrightarrow(\frac{sin(\omega T/2)}{\omega T/2})^2$

**③** $\frac{sin\omega_0\tau}{\pi\tau}\overset{F}\longleftrightarrow\begin{cases}1\quad\mid\omega\mid\leq\omega_0\\[2ex]0\quad\mid\omega\mid>\omega_0\end{cases}$

**④** $1\overset{F}\longleftrightarrow2\pi\delta(\omega)$

**⑤** $\delta(\tau)\overset{F}\longleftrightarrow1$

**⑥** $cos\omega_0\tau\overset{F}\longleftrightarrow\pi[\delta(\omega+\omega_0)+\delta(\omega-\omega_0)]$



**⑦** $R_X(\tau)cos\omega_0\tau\overset{F}\longleftrightarrow\frac12[S_X(\omega+\omega_0)+S_X(\omega-\omega_0)]$

## 例题

设 { $X(t);-\infty<t<\infty$ } 是宽平稳过程，$X(t)=Acos(t+2\pi B)$ ，$A,B$ 独立且服从 $(0,1)$ 上的均匀分布，

$E[A]=\frac12\quad D[A]=\frac1{12}\quad E[A^2]=E^2[A]+D[A]=\frac 13$

则

（1）均值函数 $\mu_X=E[Acos(2\pi B)]=0$

（2）自相关函数 $R_X(\tau)=E[X(0)X(\tau)]=E[A^2]·E[cos(2\pi B)·cos(\tau+2\pi B)]=\frac{cos\tau}{6}$

（3）谱密度 $S_X(\omega)=\frac\pi6[(\omega+1)+(\omega-1)]$

（4）时间均值 $<X(t)>=\underset{T\rightarrow+\infty}\lim\frac 1{2T}\int_{-T}^TX(t)dt=\underset{T\rightarrow+\infty}\lim\frac{AsinTcos(2\pi B)}T\equiv\mu_X$ ，具有各态历经性。

（5）时间相关函数 $<X(t)X(t+\tau)>=\underset{T\rightarrow+\infty}\lim\frac 1{2T}\int_{-T}^TX(t)X(t+\tau)dt=\frac{A^2cos\tau}2\neq R_X(\tau)$ ，不具有各态历经性。

（6）综合（4）（5），$X(t)$ 不是各态历经过程。

## 解题方式

**①** 证明是宽平稳过程，只需证 $E[X(t)]$ 为常数且 $R_X$ 为只和 $\tau$ 有关的函数。

**②** 证明是各态历经过程，只需证 $<X(t)>\equiv\mu_X$ 且 $<X(t)X(t+\tau)>\equiv R_X(\tau)$

**③** 在 $\underset{\tau\rightarrow+\infty}\lim R_X(\tau)$ 存在的条件下，证明均值具有各态历经性，也可转而证 $\underset{\tau\rightarrow+\infty}\lim R_X(\tau)=\mu_X^2$ 
