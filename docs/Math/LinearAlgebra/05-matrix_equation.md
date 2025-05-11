# 05 | 矩阵方程

## 问题阐释

对于方程组

$$
\begin{cases}
a_{11}x_{1}+a_{12}x_{2}+\cdots+a_{1n}x_{n}=b_{1}\\
a_{21}x_{1}+a_{22}x_{2}+\cdots+a_{2n}x_{n}=b_{2}\\
\vdots \\
a_{m1}x_{1}+a_{m2}x_{2}+\cdots+a_{mn}x_{n}=b_{m}
\end{cases}
$$


$$
Ax=b
$$

其中

$$
\begin{aligned}
&A=\begin{bmatrix}a_{11}&\cdots&a_{1n}\\\vdots&\ddots&\vdots\\a_{m1}&\cdots&a_{mn}\end{bmatrix}\quad x=\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}\quad b=\begin{bmatrix}b_1\\\vdots\\b_m\end{bmatrix}
\end{aligned}
$$

我们的目的：

- 有解的方程去求解
- 无解的方程近似解

!!! example "例子"
    $$
    Ax = b
    $$

    denote 
    
    - $A_{m\times n}$ 数据矩阵，例如每个学生的表现（他们的分数、作业、幻灯片、考试）
    - $x_{n\times 1}$ 是权重向量（未知），例如作业、幻灯片、考试的重要程度
    - $b_{m\times 1}$ 是观测向量（已知），例如学生的最终成绩


    如果把输入输出层看作神经元，那么矩阵方程可以看作是神经网络的线性层


    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250511210010.png)

## 有无解


奇异的意思是：冗余、重复、线性相关

非奇异的意思是：线性无关

关注 $m,n,rank(A)$ 之间的关系

- $m>n$ 超定，瘦高型矩阵,约束比变量多
- $m=n$ 方阵
- $m<n$ 欠定，矮胖型矩阵

> 秩的含义是：线性无关的行（列）向量的最大个数

**从矩阵的column view理解**

- $\text{rank}([A, b])> \text{rank}(A)$ : $b$无法被A的列向量线性表示，无解
- $\text{rank}([A, b]) = \text{rank}(A)$ : $b$可以被A的列向量线性表示，有解
  - $\text{rank}(A) = n$ : 唯一解
  - $\text{rank}(A) < n$ : 无穷多解


**机械臂的例子理解**

- 关节空间：关节的角度（旋转关节）或位移（移动关节）
- 笛卡尔空间：末端执行器的位置和姿态

对于机械臂来说，操作空间维度相当于$m$，关节数目相当于$n$（自变量数目）

- 超定：$m>n$，约束比变量多，无解
- 欠定：$m<n$，关节很多，维度比较低，有很多组解



## 方程求解

!!! note "在机器学习当中，已知了样本数据的$A$，以及最终评价$b$，那求解$x$的过程就是模型训练的过程"

### 初等行变换和高斯消元法

$$
A x = b \xrightarrow{\text{初等行变换}} x = A^{-1} b
$$

$$
[A, b] \xrightarrow{\text{初等行变换}} [I, A^{-1} b]
$$







> 参考资料 [线性方程组的最小二乘解和最小范数解 - 一以知行](https://zhuanlan.zhihu.com/p/503664717)


### 矩阵求逆

若 $A$ 和 $B$ 均可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$

性质（对于可逆的正方矩阵A和B）：

- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^{*})^{-1} = (A^{-1})^{*}$
- $(A^{\mathrm{T}})^{-1} = (A^{-1})^{\mathrm{T}}$
- $(A^{\mathrm{H}})^{-1} = (A^{-1})^{\mathrm{H}}$


#### 矩阵求逆引理


background： 在许多实际问题中，经常会遇到这样的问题：已知一个矩阵$A$的逆矩阵$A^{-1}$ ,当矩阵$A$产生了一个非常小的变化得到$A+\Delta$时，通过已知的$A^{-1}$，如何简单的求出$(A+\Delta)^{-1}$?

$$
(A + xy^H)^{-1} = A^{-1} - \frac{A^{-1}xy^HA^{-1}}{1 + y^HA^{-1}x}
$$

作用：已经完成了矩阵的求逆，在A的基础上加上一个秩为1矩阵，求解逆矩阵的变化

应用：

- 自相关矩阵和协方差矩阵估计的更新
- 最小二乘法



!!! warning "证明 todox"
    $$
    \begin{aligned}
    A^{-1} + X              & = (A + BCD)^{-1} \\
    (A + BCD)(A^{-1} + X)   & = I(I\text{为单位阵}) \\
    I + AX + BCDA^{-1} + BCDX & = I \\
    AX + BCDA^{-1} + BCDX   & = 0\text{(0为 0矩阵)} \\
    (A + BCD)X + BCDA^{-1}  & = 0 \\
    X                      & = -(A + BCD)^{-1}BCDA^{-1} \\
    X                      & = -[B(B^{-1}A + CD)]^{-1}BCDA^{-1} \\
    X                      & = -(B^{-1}A + CD)^{-1}CDA^{-1} \\
    X                      & = -[C(C^{-1}B^{-1}A + D)]^{-1}CDA^{-1} \\
    X                      & = -(C^{-1}B^{-1}A + D)^{-1}DA^{-1} \\
    X                      & = -[(C^{-1}B^{-1} + DA^{-1})A]^{-1}DA^{-1} \\
    X                      & = -A^{-1}(C^{-1}B^{-1} + DA^{-1})^{-1}DA^{-1} \\
    X                      & = -A^{-1}[(C^{-1} + DA^{-1}B)B^{-1}]^{-1}DA^{-1} \\
    X                      & = -A^{-1}B(C^{-1} + DA^{-1}B)^{-1}DA^{-1}
    \end{aligned}
    $$


!!! note "应用：自相关矩阵求逆$\hat{R}^{-1}(n)$"

    $\lambda$用来表征遗忘因子;$\lambda$越小，越倾向于相信现在的数据
    
    $$
    (\lambda R + xx^H)^{-1} = \lambda^{-1}R^{-1} - \frac{(\lambda^{-1}R^{-1}x)(\lambda^{-1}R^{-1}x)^H}{1 + \lambda^{-1}x^HR^{-1}x}
    $$

    如果每次全量计算，时间复杂度很高，computational demanding

    改写成递推形式

    $$
    \begin{align*}
    \hat{R}(n) &= \sum_{j=0}^{n} \lambda^{n-j} x(j)x^H(j)\\
    \hat{R}(n) &= \lambda \hat{R}(n-1) + x(n)x^H(n)\\
    \hat{R}^{-1}(n) &= \lambda^{-1}\hat{R}^{-1}(n-1) - g(n)g^H(n)
    \end{align*}
    $$
    
    更新公式
    
    $$
    \begin{align*}
    \bar{g}(n) &= \lambda^{-1}\hat{R}^{-1}(n-1)x(n)\\
    \bar{\alpha}(n) &= 1 + g^H(n)x(n)\\
    g(n) &= \bar{g}(n)/\bar{\alpha}(n)
    \end{align*}
    $$



#### 左右逆矩阵

对于方程 $\mathbf{Ax} = \mathbf{b}$,其中$\mathbf{A}_{m\times n}$， $m$代表方程的个数，$n$代表未知数的个数


!!! note "构造方法：想要构造成已经学过的方阵的求逆问题"
    我们已经知道如何求解方阵的逆矩阵，所以如果想求解非方阵的逆矩阵，需要构造一个方阵

    所以，通过构造方阵的办法，我们很容易就可以求解非方阵的逆矩阵


=== "左逆"

    仅当 $m \geq n$ 时("Tall matrix")，说明这个时候方程的数目大于未知数的个数，方程是过定(overdetermined)的。矩阵 $A$ 可能有**左逆矩阵** 
    
    $$
    A^\dagger_L = \left(A^HA\right)^{-1}A^H
    $$
    
    左逆列满秩的时候一定存在，即$rank(A) = n$

    证明：当$rank(A) = n$时，$A^H A$ is invertible
    
    **超定方程最小二乘解**





=== "右逆"

    仅当 $m \leq n$ 时("fat matrix")，方程数目小于未知数的个数，方程式欠定的。矩阵 $A$ 可能有**右逆矩阵** 
    
    $$
    A^\dagger_R = A^H\left(AA^H\right)^{-1}
    $$
    
    右逆行满秩的时候一定存在
    
    欠定方程最小范数解


#### Moore-Penrose Inverse | 伪逆矩阵

令 $A$ 是任意 $m \times n$ 矩阵，称矩阵 $A^\dagger$ 是 $A$ 的广义逆矩阵，若 $A^\dagger$ 满足以下四个条件（常称 Moore-Penrose 条件）：

1. $AA^\dagger A = A;$
2. $A^\dagger AA^\dagger = A^\dagger;$
3. $AA^\dagger$ 为 Hermitian 矩阵，即 $AA^\dagger = (AA^\dagger)^\mathrm{H};$
4. $A^\dagger A$ 为 Hermitian 矩阵，即 $A^\dagger A = (A^\dagger A)^\mathrm{H}.$



### cramer法则



### 复矩阵方程求解

$$
(A_r + jA_i)(x_r + jx_i) = b_r + jb_i
$$

$$
\begin{bmatrix} A_r & -A_i \\ A_i & A_r \end{bmatrix} \begin{bmatrix} x_r \\ x_i \end{bmatrix} = \begin{bmatrix} b_r \\ b_i \end{bmatrix}
$$

$$
\begin{bmatrix} A_r & -A_i & b_r \\ A_i & A_r & b_i \end{bmatrix} \xrightarrow{\text{初等行变换}} \begin{bmatrix} I_n & O_n & x_r \\ O_n & I_n & x_i \end{bmatrix}
$$

其中，$A_r$ 和 $A_i$ 是矩阵 $A$ 的实部和虚部，$b_r$ 和 $b_i$ 是向量 $b$ 的实部和虚部，$I_n$ 和 $O_n$ 分别是 $n \times n$ 的单位矩阵和零矩阵，$x_r$ 和 $x_i$ 是向量 $x$ 的实部和虚部。

相当于把复数乘法做了简单的拆分，转换成了矩阵的形式



## 最小二乘解（Least Squares Solution）


### OLS - 优化视角

超定方程组，无解

$$
Ax \approx b
$$

引入一个残差向量$\Delta b$

$$
Ax  = b + \Delta b
$$




目标是最小化**残差向量** $\Delta b = Ax - b$的**欧几里得范数**，即

$$
\begin{align*}
\min_{\mathbf{x}} \| A \mathbf{x} - \mathbf{b} \|_2^2 &= (Ax - b)^T(Ax - b)\\
&= x^TA^TAx - x^TA^Tb - b^TAx + b^Tb
\end{align*}
$$

通过求导并令导数为零，可以得到

$$
\nabla f(x) = 2 \cdot A^T (Ax - b) = 0\\
\nabla^2 f(x) = 2 \cdot A^TA
$$

Hessian矩阵是正定的，所以$f(x)$是凸函数，因此平稳点（导数为0的点）就是全局最小值点


- $A^T A$可逆：$A_{m\times n}$中$m \geq n$，且$rank(A) = n$,直接求逆

    $$
    \mathbf{x}_{\text{LS}} = (A^T A)^{-1} A^T \mathbf{b}
    $$

- $rank(A) < n$,$m\geq n$，求伪逆矩阵 Moore-Penrose Inverse

    $$
    \mathbf{x}_{\text{LS}} = (A^T A)^{\dagger} A^T \mathbf{b}
    $$

- $rank(A) = m<n$,  不可辨识




#### Gussian-Markov定理

$$
Ax = b + \epsilon
$$

噪声$\epsilon$满足

$$
\begin{align*}
\mathbb{E}(\epsilon) &= 0\\
Cov(\epsilon) &= \mathbb{E}[\epsilon \epsilon^T] = \sigma^2 I
\end{align*}
$$

> 内含的假设：误差的干扰源是独立的


$$
\hat{x}_{LS} = (A^T A)^{-1} A^T b
$$

**OLS最小二乘估计是$x$的最小方差无偏估计**

即满足

$$
\begin{align*}
\mathbb{E}[\hat{x}_{LS}] &= \mathbb{E}\left[(A^T A)^{-1} A^T b\right] \\
&= (A^T A)^{-1} A^T \mathbb{E}(Ax - \epsilon) \\
&= (A^T A)^{-1} A^T A x \\
&= x\\
Var(\hat{x}_{LS}) &\leq Var(\tilde{x})
\end{align*}
$$





### OLS - 统计视角

!!! note "OLS和MLE在高斯噪声的条件下是等价的"

!!! note "观测出模型的假设非常关键，给人判定模型好坏的一个直观的方法"

首先定义拟合误差:

$$
Az-b=e
$$

其中e服从白噪声高斯分布:

$$
p(e)=N(e|C,\sigma^{2}I) \text{ 正比于 } \exp\left[-\frac{1}{\sigma^{2}}\mathrm{e}^{\mathrm{H}}e\right]
$$

因此条件概率可以写作:

$$
p(b|Az)=p(b-Az)=p(e) \text{ 正比于 } \exp\left[-\frac{1}{\sigma^2}\mathrm{e}^\mathrm{H}e\right]
$$

根据极大似然估计,我们需要找到一个z使得$p(b|Az)$最大:

$$
\begin{aligned}
\max(p(b|Az)) &\Leftrightarrow \max\ln(\exp\left[-\frac{1}{\sigma^2}\mathrm{e}^\mathrm{H}e\right]) \\
&= \max\left[-\frac{1}{\sigma^2}\mathrm{e}^\mathrm{H}e\right] \\
&= -\frac{1}{\sigma^2}\|Az-b\|_2^2 \\
&\Leftrightarrow \min\left\|Az-b\right\|_2^2
\end{aligned}
$$


conditional pdf 对b

likelihood function 对z


建模假设：模型的预测能力是比较好的，没有outlier（超出$3\sigma$的离群值），比如上课一次不来，作业一次不交，考试考100分。


### DLS - 最小数据二乘



假设数据矩阵$A$存在误差（比如记录样本数据的时候写错了）

$$
A = A_0 + E \\
E_{ij} \stackrel{\text{i.i.d.}}{\sim} N(0, \sigma^2)
$$




使用校正量$\Delta A$来表示误差,即考察下面的约束优化问题 

$$
\begin{align*}
\min \quad & ||\Delta A||^2_F\\
s.t. \quad &\left[ A + \Delta A \right] x = b 
\end{align*}
$$

> underlying idea: 每个数据的误差不会特别大

!!! note "Frobenius 范数 $(p=2)$是矩阵元素范数的一种，平方和的平方根"
    $$
    \|A\|_F \stackrel{\text{def}}{=} \left( \sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2 \right)^{1/2} = \sqrt{\text{trace}(AA^H)}
    $$

对于有约束问题，写出拉格朗日函数

$$
\begin{align*}
L(A, \lambda) &= \|A\|_F^2 + \lambda^H \left[(A + \Delta A)x - b\right]\\
&= Trace(AA^H) + \lambda^H \left[(A + \Delta A)x - b\right]
\end{align*}
$$

求导数并令导数为0

$$
\begin{align*}
\frac{\partial L(A, \lambda)}{\partial \Delta A} &= \Delta A^H + \lambda x^H = 0\\
\frac{\partial L(A, \lambda)}{\partial \lambda^H} &= (A + \Delta A)x - b = 0
\end{align*}
$$

可以解出

$$
\Delta A = - \frac{(Ax-b)x^H}{x^H x}\quad \lambda = \frac{Ax-b}{x^H x}
$$


把$\Delta A$和$\lambda$代入$L(A, \lambda)$，得到

$$
L(\Delta A, \lambda,x) = \frac{(Ax-b)^H (Ax-b)}{x^H x}
$$

变成了一个无约束的优化问题

$$
\min_x J(x) =\frac{(Ax-b)^H (Ax-b)}{x^H x}
$$

- 方法1:使用梯度下降法求解$x^{t+1} = x^t - \eta \nabla J(x^t)$
- 方法2:这是一个分式优化的问题(Fractional Programming)，2018 IEEE TSP







### TLS - 总体最小二乘



$$
\begin{align*}
\min_{\Delta A, \Delta b,x} \quad & ||\Delta A||^2_F + ||\Delta b||^2\\
s.t. \quad &\left[ A + \Delta A \right] x = b + \Delta b
\end{align*}
$$

写成分块矩阵的形式

$$
\begin{bmatrix}A & b\end{bmatrix}\begin{bmatrix} x \\ -1 \end{bmatrix} +\begin{bmatrix} \Delta A & \Delta b \end{bmatrix} \begin{bmatrix} x \\ -1 \end{bmatrix} = 0
$$

$$
(\mathbf{B} + \mathbf{D}) z = 0
$$


所以原始问题可以写成

$$
\begin{align*}
\min_{\Delta A, \Delta b,x} \quad & \|\Delta A\|^2_F + \|\Delta b\|^2 \\
&= \left\|\begin{bmatrix} \Delta A & \Delta b \end{bmatrix}\right\|^2_F \\
&= \|\mathbf{D}\|_F^2 \\
\text{s.t.} \quad   &(\mathbf{B} + \mathbf{D})z = 0
\end{align*}
$$

可以看出，TLS是DLS在$b = 0$的特殊情况

$$
\min_{z} \frac{(Bz-0)^H (Bz-0)}{z^H z}= \min_{z} \frac{z^H B^H B z}{z^H z}
$$

两个二次型相除

- Rayleigh商，有闭式解








### Tikhonov正则化 - 优化视角


- 解决过拟合
- 解决病态问题，提高数值稳定性


- 代价函数对应的是likelihood
- 正则项对应的是prior


### Tikhonov正则化 - 统计视角


### 应用 - 稀疏表示和压缩感知






## 最小范数解



最小范数解是离原点最近的解

$$
\begin{align*}
&\text{Minimize:} \quad \| x \| \\
&\text{Subject to:} \quad A x = b
\end{align*}
$$

直接给出结论，此时问题的最小范数解是：

$$
x^* = A^T (A A^T)^{-1} b
$$


!!! note "证明"
    令上述问题的解为 $x^* = A^T (A A^T)^{-1} b$，注意

    $$
    \begin{align*}
    \| x \|^2 &= \| (x - x^*) + x^* \|^2\\
    &= ((x - x^*) + x^*)^T ((x - x^*) + x^*)\\
    &= \| x - x^* \|^2 + \| x^* \|^2 + 2 x^{*T} (x - x^*)
    \end{align*}
    $$

    由于

    $$
    \begin{align*}
    x^{*T} (x - x^*) &= [A^T (A A^T)^{-1} b]^T [x - A^T (A A^T)^{-1} b]\\
    &= b^T (A A^T)^{-1} [A x - (A A^T) (A A^T)^{-1} b]\\
    &= b^T (A A^T)^{-1} (b - b)\\
    &= 0
    \end{align*}
    $$

    故有

    $$
    \| x \|^2 = \| x - x^* \|^2 + \| x^* \|^2
    $$

    由于对于所有 $x \neq x^*$，都有 $\| x - x^* \|^2 > 0$ 成立，因此，对于所有 $x \neq x^*$，都有 $\| x \|^2 > \| x^* \|^2$，即 $\| x \| > \| x^* \|$，显然 $x^*$ 是惟一的。证明完毕。








## 矩阵方程

### Lyapunov方程

[线性代数 | 李雅普诺夫方程](https://www.zhihu.com/tardis/zm/art/105326895?source_id=1005)
