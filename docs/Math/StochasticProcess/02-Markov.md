# 02 ｜ 马尔可夫链

## Markov 性

以现在预测将来，结果与过去无关，**即过去与将来相互独立**。

## 转移概率

$m$ 时处于状态 $i$ 的条件下，到 $n$ 时转移到状态 $j$ 的概率 $P(X_n=j\mid X_m=i)\overset{记为}\Longrightarrow p_{ij}(m,n)$ 。

## 转移矩阵

**①** 各元素非负	**②** 各行元素之和为 1

## 时齐 Markov 链

若 $\forall\;i,j\quad P(X_{n+1}=j\mid X_n=i)$ 不依赖于 $n$ ，则称 {$X_n$} 是**时齐的 $Markov$ 链**

### 一步转移概率

$P(X_{n+1}=j\mid X_n=i)\overset{记为}\Longrightarrow p_{ij}$

### 一步转移矩阵

$\mathbf P=[\;p_{ij}\;]_{I\times I}$

### $m$ 步转移概率

$P(X_{n+m}=j\mid X_n=i)\overset{记为}\Longrightarrow p_{ij}^{(m)}$

### $m$ 步转移矩阵

 $\mathbf P^m=[\;p^{(m)}_{ij}\;]_{I\times I}$ 

## C-K方程

$\forall\;m,n,l\geq0\quad i,j\in I\qquad p_{ij}(m,m+n+l)=\sum_kp_{ik}(m,m+n)·p_{kj}(m+n,m+n+l)$

**①** $\forall\;n\geq1\quad P(X_n=j)=\sum_iP(X_0=i)·p_{ij}^{(n)}$	。

**②** $\forall\;n_1<n_2<\dots<n_k\quad P(X_{n_1}=i_1,\dots,X_{n_k}=i_k,)=P(X_{n_1}=i_1)·p_{i_1i_2}^{(n_2-n_1)}\dots p_{i_{k-1}i_k}^{(n_k-n_{k-1})}$

时齐 $Markov$ 链的有限维分布完全由**初始分布**与**一步转移矩阵**决定。

## 常返和暂留

定义

 $\tau_i=min(n\geq1;X_n=i)$ 为首次击中状态 $i$ 的时间（首中时）。

$f_{ij}^{(n)}$ 为从状态 $i$ 出发在 $n$ 步首次击中状态 $j$ 的概率。

$f_{ij}=P(\tau_j<\infty\mid X_0=i)$ 为从状态 $i$ 出发在有限步能够击中状态 $j$ 的概率，显然有 $f_{ij}=\sum f_{ij}^{(n)}$ 。

### 常返

从状态 $i$ 出发能在有限时间内返回状态 $i$ ，即 $P(\tau_i<\infty\mid X_o=i)=1$ 。

### 暂留

不满足**常返**的。

### 平均回转时

$\mu_i=\sum nf_{ii}^{(n)}=\begin{cases}<\infty\qquad正常返\\[2ex]=\infty\qquad零常返\end{cases}$

## 状态空间的划分

### 可达

 $i$ 能到达 $j$ 。$i\searrow j$ 。

### 互达

 $i$ 能到达 $j$ 且 $j$ 能到达 $i$ 。$i\leftrightarrow j$ 。有 $d(i)=d(j)$ 且各状态有**相同的周期性与常返性**。

$\forall\;i\;j$ 互达 $\Leftrightarrow$ $Markov$ 链**不可约**

### 互达等价类

所有处于同一互达状态的集合。状态空间可分为不交的**互达等价类**的并集。

### 闭集

一旦进入此互达等价类中的状态便不再进入非该互达等价类的其他状态。

### 周期

$d(i)$ 为所有返回步数可能取值的最大公约数。

**①** $i$ 非周期 $\Leftrightarrow$ $d(i)=1$ 。	**②** $i$ 遍历 $\Leftrightarrow$ $i$ 非周期正常返。	**③** { $X_n$ } 遍历 $\Leftrightarrow$ { $X_n$ } 不可约非周期正常返。

## 平稳分布

$\mathbf\pi=(\pi_1,\pi_2,\pi_3,\dots,\pi_n)$ 代表稳态时各个状态的含量。满足 **①** $\mathbf\pi=\mathbf P\mathbf\pi$ （$\mathbf P$ 为一步转移矩阵）**②** $\sum\pi_i=1$

### 不可约 $Markov$ 链的性质

**①** 若 { $X_n$ } 正常返，则 $\pi$ 存在且唯一，$\pi_i=\frac 1{\mu_i}$ 。

**②** 若 { $X_n$ } 遍历，则 $\forall\;i\;j\quad \underset{{n\rightarrow\infty}}\lim P_{ij}^{(n)}=\pi_j\quad\rightarrow\quad \underset{{n\rightarrow\infty}}\lim P(X_n=j)=\pi_j$ 。

**③** 若状态空间有限，则 { $X_n$ } 正常返。

### 可约 $Markov$ 链的性质

**①** $i$ 的互达等价类不闭 $\rightarrow$ $i$ 暂留， $i$ 常返 $\rightarrow$ $i$ 的互达等价类关闭。

**②** $i$ 的互达等价类是有限闭集 $\rightarrow$ $i$ 正常返。

**③** 若 $j$ 暂留或零常返，则 $\forall\;i\quad\underset{{n\rightarrow\infty}}\lim p_{ij}^{(n)}=0$

### 有限 $Markov$ 链的状态分解

可将状态空间分解为所有不交的互达等价类 $C_i$ 与余下状态 $T$ 的并集，则 $C_i$ 中各状态正常返，$T$ 中各状态暂留。则将 { $X_n$ } 限制在 $C_i$ 上得到一个不可约正常返的 $Markov$ 链，其满足 $\pi_i=\frac 1{\mu_i}$ 。

## 吸收概率与平均吸收时间

### 先走一步法

设状态 $a$ 为吸收态，$P_i$ 为状态 $i$ 进入状态 $a$ 的概率/时间，则 $P_b=\sum p_{bc_i}·P_{c_i}$ （求平均步数需 +1）

其中 $p_{bc_i}$ 为一步转移概率。

## 例题

设 { $X_n\;;\;n\geq0$ } 是时齐的 $Markov$ 链，状态空间 $I$ = {1,2,3,4,5,6}，一步转移概率为：$p_{11}=p_{54}=p_{62}=0.4$ ，$p_{12}=p_{56}=p_{65}=0.6$ ，$p_{21}=p_{34}=p_{43}=1$ 。

则

（1）所有互达等价类为  $C_1$={1,2}	$C_2$={3,4}	$C_3$={5,6}	其中 $C_1\; C_2$ 是闭的。

（2）$d(1)=d(2)=1\quad d(3)=d(4)=d(5)=d(6)=2$	即状态 1、2非周期。

（3）状态 1、2、3、4 正常返，状态 5、6 暂留。

（4）$\because\pi=(\frac58,\frac38,\frac12,\frac12)$	$\therefore(\mu_1,\mu_2,\mu_3,\mu_4)=(\frac85,\frac83,2,2)$

（5）$\underset{{n\rightarrow\infty}}\lim p_{12}^{(n)}=\pi_2=\frac38$	$\underset{{n\rightarrow\infty}}\lim p_{55}^{(n)}=0$

（6）$\underset{{n\rightarrow\infty}}\lim P(X_n=3)=\pi_3=\frac12$	$\underset{{n\rightarrow\infty}}\lim P(X_n=6)=0$

## 解题方式

**①** 画出状态转移图，写出一步转移矩阵。**观察**状态转移图：

**②** 只要某几个状态两两互达，则为一互达等价类。若任一状态**常返**，则闭；反之不闭。

**③** 对周期的判断则看返回步数的所有可能取值，若出现质数，则**非周期**；反之，周期为其最大公约数。

**④** 若某一状态一旦出去就回不来了，则**暂留**；若还能回来，则**正常返**。

**⑤** 求**平均回转时**可先进行状态分解，在**互达等价类**内部求平稳分布 $\pi$ ，**平均回转时**即倒数。

**⑥** 求 $n$ 步转移概率/稳态概率，方法同 ⑤ 。若某一状态**暂留**，则 $n$ 步后到该状态的概率/稳态概率为 0 ；反之为对应的 $\pi$ 值。
