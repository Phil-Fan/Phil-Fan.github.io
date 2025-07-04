# 06 | 随机过程复习
## Cheet Sheet
### Concept

1. 均值函数$\mu(t) = E\big(X(t)\big)$
2. 方差函数$\sigma^2(t) = E\big(X^{2}(t)\big) - \mu^{2}(t) = C(t,t)$
3. 协方差函数$C(s,t) = E\big(X(s)X(t)\big) - \mu(s)\mu(t)$
4. 相关函数$R(s,t) = E\big(X(s)X(t)\big)$,是协方差函数的第一项


- $\text{Var}(A+B) = \text{Var}(A) + \text{Var}(B) + 2\text{Cov}(A, B)$
- $\text{Var}(A) = \text{Cov}(A, A)$
- $\text{Cov}(A, B) = E(AB) - E(A)E(B)$
- $\text{Var}(A) = E(A^2) - [E(A)]^2$


### Markov


| 字母 | 含义 |
|------|------|
| $X_n$ | $n$ 时刻的状态 |
| $p_{ij}(m,m+n)$ | $m$ 时刻经过$n$步从状态 $i$ 到状态 $j$ 的概率 |
| $\mathbf P$ | 一步转移矩阵 |
| $\mathbf P^{(n)}$ | $k$ 步转移矩阵|
| $C_i$ | 互达等价类 |
| $T$ | 余下状态 |
| $d(i)$ | 状态 $i$ 的周期 |
| $f_{ij}$ | 从状态 $i$ 出发在有限步首次到达状态 $j$ 的概率 |
| $f_{ij}^{(n)}$ | 从状态 $i$ 出发在 $n$ 步首次到达状态 $j$ 的概率（**f联想first，记忆是第一次到达**） |
| $\mathbf\pi$ | 平稳分布向量 |
| $\mu_i$ | 状态 $i$ 的平均回转时间 |
| $n$ | 时间步数 |



1️⃣**转移矩阵** 画出状态转移图，写出一步转移矩阵。**观察**状态转移图：求平稳分布: $\pi = \pi P$（左乘）

- $p_{ij}^{(n)}$:求出$P^{(n)}$后，$p_{ij}^{(n)}$ 为 $P^n$ 的第 $i$ 行第 $j$ 列的元素


2️⃣**等价类** 只要某几个状态两两互达，则为一互达等价类。若任一状态**常返**，则闭；反之不闭。

- 互达等价类的周期、常返性都一样

3️⃣**周期**：对周期的判断则看返回步数的所有可能取值，如果有指向自己的步，则非周期，若出现质数，则**非周期**；反之，周期为其最大公约数。

- $f_{ij}^{(k)}$: 为从状态 $i$ 出发在 $n$ 步首次到达状态 $j$ 的概率:直接数一下有几种情况即可

4️⃣ 若某一状态一旦出去就回不来了，则**暂留**；若还能回来，则**正常返**。
 
5️⃣ 求**平均回转时**可先进行状态分解，在**互达等价类**内部求平稳分布 $\pi$ ，**平均回转时**即倒数。

- 平稳分布 $\pi = \pi P$ （左乘）

6️⃣ 求$n$步转移概率/稳态概率 $\lim p_{AB}^{(n)}$ ，方法同 ⑤ 。若某一状态**暂留**，则 $n$ 步后到该状态的概率/稳态概率为 0 ；反之为$B$状态对应的 $\pi$ 值。

7️⃣求吸收概率/吸收时间：找到吸收态，定义不同吸收态的取值，列出1步之后的方程，求解得到概率。

- 吸收概率不 +1
- 吸收时间/步数 要 +1 
### Poison

| 字母 | 含义 |
| ---- | ---- |
| $N(t)$ | 在时间 $t$ 内发生的"事件"数 |
| $W_n$ | 第 $n$ 个事件发生的时刻 |
| $T_i$ | 第 $i$ 个事件和第 $i-1$ 个事件发生的时间间隔 |

**齐次泊松过程**

$$
\begin{aligned}
P\left[N(t)-N(s)=k\right]&\sim\pi(\lambda(t-s))\\
&=\frac {[\lambda(t-s)]^k·e^{-\lambda(t-s)}}{k!},\quad k=0,1,2,\dots
\end{aligned}
$$

**非齐次泊松过程**:差值变成积分的上下限

$$
\begin{aligned}
P(N(t)-N(s)=k)&\sim \pi(\int_s^{t} \lambda(u) du)
\end{aligned}
$$



**数字特征**

- 均值函数：$\mu_N(t)=E[N(t)]=\lambda t$
- 方差函数：$D_N(t)=D[N(t)]=\lambda t$

- 自相关函数：$C_N(t_1,t_2)=Cov[N(t_1),N(t_2)]=\lambda min(t_1,t_2)+\lambda^2t_1t_2$

- 自协方差函数：$R_N(t_1,t_2)=E[N(t_1)·N(t_2)]=\lambda min(t_1,t_2)$



**求解思路**

1. 泊松过程的合成与分解。应用题比较多，这里要注意分类不重不漏。
   - 一般求条件概率，上下的$e$的指数项可以消去
   - 如果有求解$X\geq m$类型的概率，都是使用$1-P(X<m)$来求解。

2. 独立增量过程，将不独立的变量转化为独立增量。

3. 各种相关分布的结论。指数分布刻画时间，柏松分布刻画计数，参数相同


### Brown


**数字特征**：

* $\forall\;0\leq s<t\quad X(t)-X(s)\sim N(0,\sigma^2(t-s))$
  * 正态分布的pdf，在求特殊分布的时候有用

$$
f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

* 均值函数：$\mu_B(t)=0$
* 方差函数：$D_B(t)=t$
  * $Var(A\pm B) = Cov(A\pm B,A\pm B) = Var(A) + Var(B) \pm 2Cov(A,B)$
* 自协方差函数：$C_B(t,s) =min(t,s)\qquad t,s>0$

**性质**：

* 写成增量的形式，增量之间互相独立

* **马尔科夫性**：$B(t+\tau)-B(\tau)$也是标准布朗
* **自相似性**：$\forall\;a\neq0\quad$	{ $\frac1aB(a^2t);t\geq 0$ } 是标准布朗运动。
* $0-\infty$**对称性**：$\overset{\sim}B(t)=\begin{cases}tB(\frac 1t)\quad t>0\\[2ex]0\qquad\quad t=0\end{cases}$ 	则 { $\overset{\sim}B(t);t\geq0$ } 是标准布朗运动。

> 当遇到条件比现在大的情况 如$P(B(1)>1|B(2)=2)$
> 一般都考虑使用相似或者对称性质进行求解，而不是使用贝叶斯


**特殊分布**：

* 首次击中时间：$P\left(\max_{s\leq t}B(s)\geq a\right) = P(T_a \leq t) = 2P(B(t)\geq a),\quad a > 0$


**布朗桥**

$X(t)=B(t)-tB(1)\quad 0\leq t \leq 1$

- $X(0)=X(1)=0$	（桥的形状）
- 均值：$\mu_X(t)=0$
- 协方差：$C_X(s, t) = s(1 - t),\quad 0 < s < t < 1$

### 平稳

本章题目比较格式化，大概都是这种流程，背公式就行了，对常用的傅立叶变换对要记忆清楚

1. 一般都是第一问算**均值和自相关函数**，然后验证是不是宽平稳过程（有独立的就拆开，没有的利用pdf进行积分）
2. 第二问算**时间均值**和**时间相关函数**，然后验证均值和自相关的各态历经性
3. 求**谱密度**（与傅立叶变换相联系）



**①** 证明是宽平稳过程

- $E[X(t)]$ 为常数
- $R_X$ 为只和 $\tau$ 有关的函数

**②** 均值各态历经

- $\langle X(t)\rangle\equiv\mu_X$ 
- $\lim_{T\rightarrow\infty} \frac1T\int_0^\infty C_x(\tau) d\tau$
- 在 $\underset{\tau\rightarrow+\infty}\lim R_X(\tau)$ 存在的条件下，证明$\underset{\tau\rightarrow+\infty}\lim R_X(\tau)=\mu_X^2$ 

**③** 自相关函数各态历经

- $\langle X(t)X(t+\tau)\rangle\equiv R_X(\tau)$


**④** 功率谱密度：对自相关函数进行傅里叶变换;实、非负、偶函数



$$
\begin{cases}
P_{\xi}(\omega) = \int_{-\infty}^{+\infty} R(\tau) e^{-j\omega\tau} \, \mathrm{d}\tau \\
R(\tau) = \frac{1}{2\pi} \int_{-\infty}^{+\infty} P_{\xi}(\omega) e^{j\omega\tau} \, \mathrm{d}\omega
\end{cases}
$$

- 傅立叶变换的性质：时域相乘等于频域卷积


| 时域 | 频域 |
|------|------|
| $e^{-a\mid\tau\mid}$ | $\frac{2a}{a^2+\omega^2}$ |
| $\frac{sin\omega_0\tau}{\pi\tau}$ | $\begin{cases}1\quad\mid\omega\mid\leq\omega_0\\[2ex]0\quad\mid\omega\mid>\omega_0\end{cases}$ |
| $1$ | $2\pi\delta(\omega)$ |
| $\delta(\tau)$ | $1$ |
| $cos\omega_0\tau$ | $\pi[\delta(\omega+\omega_0)+\delta(\omega-\omega_0)]$ |

## 定义辨析

### 1. **二阶矩过程**
**定义：**
一个随机过程 ${X(t),\ t \in T}$ 是**二阶矩过程**，如果对任意 $t \in T$，存在有限的期望 $\mathbb{E}[X(t)]$ 和方差 $\mathbb{E}[X(t)^2]$，并且协方差 $\mathbb{E}[X(t_1)X(t_2)]$ 存在，对任意 $t_1, t_2 \in T$ 成立。

**公式：**

$$
\begin{aligned}
&\mathbb{E}[X(t)] < \infty \\
&\mathbb{E}[X(t)^2] < \infty \\
&\text{Cov}(X(t_1), X(t_2)) = \mathbb{E}\left[(X(t_1) - \mathbb{E}[X(t_1)])(X(t_2) - \mathbb{E}[X(t_2)])\right]
\end{aligned}
$$

**通俗解释：**
过程中的每个时间点上的随机变量都有期望、方差，并且任意两个时刻之间的相关性（协方差）也定义良好。比如你可以画出时间序列的“均值和协方差图”。

---

### 2. **独立增量过程**

**定义：**
若随机过程 ${X(t),\ t \in T}$ 满足，对于任意时间序列 $t_0 < t_1 < \cdots < t_n$，各增量 $X(t_1)-X(t_0),\ X(t_2)-X(t_1),\ \cdots,\ X(t_n)-X(t_{n-1})$ 是**相互独立**的，则称该过程为**独立增量过程**。

**通俗解释：**
过去的变化不会影响将来的变化。就像你掷骰子，每次的结果和上一次无关。

---

### 3. **平稳增量过程**

**定义：**
如果随机过程 ${X(t),\ t \in T}$ 的任意两个相同长度的时间间隔 $[t, t+h]$、$[s, s+h]$ 的增量 $X(t+h)-X(t)$ 与 $X(s+h)-X(s)$ 具有**相同的分布**，则称其为**平稳增量过程**。

**通俗解释：**
只要时间间隔相同，不管从哪开始，变化的“统计规律”一样，比如掷硬币10次，不管从第1次还是第100次开始。

---

### 4. **独立平稳增量过程**

**定义：**
若一个过程同时满足“独立增量”和“平稳增量”两种性质，则称其为**独立平稳增量过程**。

**通俗解释：**
每段时间的变化都既和其他段无关（独立），又服从相同分布（平稳）。比如泊松过程、布朗运动等。

---

### 5. **正态过程**

若随机过程 ${X(t),\ t \in T}$ 中，任取有限个时刻 $t_1, t_2, \cdots, t_n$，对应的随机向量 $(X(t_1), X(t_2), \cdots, X(t_n))$ 服从多元正态分布，则称其为**正态过程**。

**通俗解释：**
不管你选几个时间点，观测值的联合分布都像正态分布那样平滑。比如布朗运动。

---

### 6. **马尔可夫过程**
**定义：**
马尔可夫过程是随机过程的一种特殊形式，其中**未来状态只依赖当前状态，与过去无关**。即满足马尔可夫性：

$$
P(X(t_{n+1}) \mid X(t_n), \cdots, X(t_0)) = P(X(t_{n+1}) \mid X(t_n))
$$

**通俗解释：**
“忘记过去，只看现在”就能预测未来，比如很多金融模型中的状态转移就是这样。

---

### 7. **Poisson 过程**
**定义：**
泊松过程是一种**独立增量**的随机过程，且单位时间内事件发生次数服从泊松分布，并满足平稳性。记作 ${N(t),\ t \geq 0}$，满足：

- $N(0) = 0$
- 独立增量
- 增量 $N(t + h) - N(t) \sim \mathrm{Poisson}(\lambda h)$

**通俗解释：**
比如一分钟内顾客到来的次数是随机的，而且每段时间之间互不影响。

---

### 8. **Brown**

**定义：**
布朗运动 ${B(t),\ t \geq 0}$ 具有以下性质：

- $B(0) = 0$
- 有独立增量
- 有平稳增量
- $B(t) - B(s) \sim N(0, t - s)$（正态过程）
- 样本路径连续但处处不可导

**通俗解释：**
像分子随机运动一样的过程，每段变化既随机独立又符合正态分布。

---

### 9. **平稳过程**

#### （1）严平稳过程

**定义：**
若随机过程 ${X(t),\ t\in T}$ 满足对任意 $n$、任意 $t_1,\dots,t_n$ 以及任意实数 $h$，有：

$$
(X(t_1),\dots,X(t_n)) \overset{d}{=} (X(t_1 + h),\dots,X(t_n + h))
$$

则称为**严平稳过程**。

**通俗解释**

整体“形状”和统计特征不会因时间移动而改变。

#### （2）宽平稳过程

**定义：**
过程 ${X(t)}$ 满足：

- $\mathbb{E}[X(t)] = \mu$ 为常数；
- 协方差函数 $\text{Cov}(X(t), X(s))$ 只依赖于 $|t - s|$ 而不是 $t$ 或 $s$；

即为**宽平稳过程**。

**通俗解释：**
均值不变，协方差只看“间隔”。更容易处理的平稳概念。


## 逻辑与包含关系总结

我们可以按如下逻辑关系来梳理这些概念之间的联系：

```
     ┌────────────┐
     │二阶矩过程  │
     └────┬───────┘
          │ mu=constant, R sim tau
     ┌────▼──────────┐
     │宽平稳过程       │
     └────────▼──────┘
          │   ｜
     ┌────▼───────┐
     │严平稳过程    │（更强）
     └────────────┘

     ┌────────────┐  ┌────────────────┐
     │ 独立增量过程 │<>│  平稳增量过程    │
     └────┬───────┘  └────┬───────────┘
          │      有交集    │
          │               |
     ┌────▼───────────────▼─────────┐
     │      独立平稳增量过程           │
     └────┬───────────┬─────────────┘
          │           │
      ┌───▼───┐    ┌──▼──────┐
      │Poisson│    │Brownian│
      └───────┘    └─────────┘

      ┌───────────────┐
      │正态过程（广义）│
      └──────┬────────┘
             │
         ┌───▼─────┐
         │Brownian │（是正态过程）
         └─────────┘

      ┌─────────────┐
      │马尔可夫过程 │
      └────┬────────┘
           │包含
      ┌────▼───────┐
      │Poisson、Brown│
      └─────────────┘
```



严平稳过程+二阶矩存在 → 宽平稳过程
宽平稳过程+正态过程→严平稳过程

| 类型                                    | 示例        | 独立增量 | 平稳增量 |
| ------------------------------------- | --------- | ---- | ---- |
| $X(t) = t W(t)$                       | 非平稳缩放布朗运动 | ✅    | ❌    |
| $X(t) = \cos(\omega t) + \epsilon(t)$ | 周期信号 + 噪声 | ❌    | ✅    |
