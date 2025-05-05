# 02 | 矩阵运算




## 单个矩阵
!!! note "要关注矩阵运算对于矩阵维度的影响"

| 性质/指标 | 描述|
|---|---|
| 二次型     | 矩阵的正定性与负定性                       |
| 行列式     | 矩阵的奇异性                              |
| 特征值     | 矩阵的奇异性、正定性和对角元素的结构      |
| 迹         | 矩阵对角元素之和、特征值之和             |
| 秩         | 行（或列）之间的线性无关性、矩阵方程的适定性 |



### Conjugate
- 共轭性质：$(A+B)^{*} = A^{*} + B^{*}$


### Transpose


- 转置性质：$(A+B)^{\mathrm{T}} = A^{\mathrm{T}} + B^{\mathrm{T}}$，$(AB)^{\mathrm{T}} = B^{\mathrm{T}}A^{\mathrm{T}}$



#### Hermitian转置（共轭转置/ Hermitian伴随/ Hermitian共轭）

$A^\text{H} = \begin{bmatrix} a_{11}^* & a_{21}^* & \cdots & a_{m1}^* \\ a_{12}^* & a_{22}^* & \cdots & a_{m2}^* \\ \vdots & \vdots & \ddots & \vdots \\ a_{1n}^* & a_{2n}^* & \cdots & a_{mn}^* \end{bmatrix}$

$A^\text{H} = (A^*)^\text{T} = (A^\text{T})^*$

- Hermitian转置性质：$(A+B)^{\mathrm{H}} = A^{\mathrm{H}} + B^{\mathrm{H}}$，$(AB)^{\mathrm{H}} = B^{\mathrm{H}}A^{\mathrm{H}}$

- Hermitian矩阵性质：对于任意矩阵$A$，矩阵$B = A^{\mathrm{H}}A$都是Hermitian矩阵。



### Inverse


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


### norm

#### 诱导范数（Induced Norm）
- 诱导范数定义为：$\|A\| = \max \{\|Ax\| : x \in K^n, \|x\| = 1 \}$
- 或者等价地定义为：$\|A\| = \max \left\{ \frac{\|Ax\|}{\|x\|} : x \in K^n, x \neq 0 \right\}$

**常用的诱导范数 - p 范数（p-Norm）**：
   - p 范数定义为：$\|A\|_p = \max_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$

=== "当 $p = 1$"
    得到绝对列和范数
    列的绝对值和的最大值

    $$ 
    \|A\|_1 = \max_{1 \leq j \leq n} \sum_{i=1}^m |a_{ij}| 
    $$

=== "$p = 2$"
    得到矩阵的最大奇异值（Spectral Norm）

    $$
    \|A\|_2 = \|A\|_{\text{spec}} 
    $$

=== "$p = \infty$"
    得到绝对行和范数（Absolute Row Sum Norm）
    
    $$ 
    \|A\|_{\infty} = \max_{1 \leq i \leq m} \sum_{j=1}^n |a_{ij}| 
    $$



#### “元素形式” 范数

$$
\|A\|_p \stackrel{\text{def}}{=}\left(\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|^p\right)^{1/p}
$$

1. $L_1$ 范数 (和范数) $(p=1)$，绝对值的和

   $$
   \|A\|_1 \stackrel{\text{def}}{=} \sum_{i=1}^m \sum_{j=1}^n |a_{ij}|
   $$

2. Frobenius 范数 $(p=2)$，平方和的平方根
   
   $$
   \|A\|_F \stackrel{\text{def}}{=} \left( \sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2 \right)^{1/2}
   $$

3. 最大范数 (max norm) 即 $p=\infty$ 的 $p$ 范数, 定义为

   $$
   \|A\|_{\infty} = \max_{i=1,\cdots,m; j=1,\cdots,n} \{|a_{ij}|\}
   $$


### quadratic form | 二次型

对于任意一个二次型函数 $f(x_1, \ldots, x_n) = \sum_{i=1}^n \sum_{j=1}^n \alpha_{ij} x_i x_j$，存在许多矩阵 $A$，它们的二次型 $x^T A x = f(x_1, \ldots, x_n)$ 相同。

> 二次型一般用两个sum来表示

**唯一性条件**

- 只有实对称矩阵或复共轭对称矩阵满足唯一性，即 $x^T A x = f(x_1, \ldots, x_n)$。
- 二次型函数一定是实值函数。


**二次型理论**：二次型刻画矩阵的正定性

- $\mathbf{H(f)}$负定，有极大值： 奇数阶主子式为负数，偶数阶为正数
- $\mathbf{H(f)}$正定，有极小值：顺序主子式都为正数
- $\mathbf{H(f)}$不定，鞍点：特征值有正有负
- $\mathbf{H(f)}$不可逆，无法判断：特征值有0

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/b05544056c037bc56f9070e45533f02.jpg" alt="b05544056c037bc56f9070e45533f02" style="zoom: 33%;" />



!!! note "正定的理解"
    假设 $\mathbf{A}x = m$, 则 $\langle x,m \rangle = x^{\mathbf{H}} m = x^{\mathbf{H}} \mathbf{A} x$

    所以正定意味着x,m夹角小于90度
    
    任意输入，输出偏离都不会太大，都是一个锐角
    
    正定的话，所有特征值都大于零
    
    $$
    \begin{align*}
    &x_i^T A x_i > 0 \\
    &\Rightarrow x_i^T \lambda_i x_i > 0 \\
    &\Rightarrow \lambda_i \|x_i\|^2 > 0 \\
    &\Rightarrow \lambda_i > 0
    \end{align*}
    $$


### Eigenvalues | 特征值

满足以下方程的$\lambda$称为特征值

第一定义

$$
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}
$$

第二定义

$$
det(\mathbf{A} - \lambda \mathbf{I}) = 0
$$


**特征值和正定性**

- 特征值为正，矩阵正定
- 特征值非负，矩阵半正定
- 特征值为负，矩阵负定
- 特征值非正，矩阵半负定
- 特征值有正有负，矩阵不定

**性质**

$$
det(A) \leq \prod_{i=1}^n \lambda_i
$$

$$
tr(A) \leq \sum_{i=1}^n \lambda_i
$$



### Trace | 迹
所有特征值之和

$$
tr(A) = \sum_{i=1}^n \lambda_i
$$


### Eigenvectors | 特征向量


### Determinant | 行列式

$$
det(AB) = det(A) \cdot det(B)
$$

#### 求值

??? note "$det = \Pi_i^n \lambda_i$"
    矩阵的行列式等于其特征值的乘积<br>
    
    对于一个 $n \times n$ 的方阵 $A$，如果它有 $n$ 个线性无关的特征向量 $v_1, v_2, \ldots, v_n$，那么 $A$ 可以表示为：
    
    $$ 
    A = V \Lambda V^{\mathbf{H}}\\
    det(A) = det(V) \cdot det(\Lambda) \cdot det(V^{\mathbf{H}}) = det(\Lambda) 
    $$
    
    而特征向量矩阵 $V$ 是正交矩阵$V\cdot V^{\mathbf{H}} = I$；所以 $det(V) = 1$
    
    又因为 $det(\Lambda) = \lambda_1 \lambda_2 \cdots \lambda_n$，所以 $A$ 的行列式等于它的特征值的乘积。


**行列式与奇异性**

- $\exists \lambda_i = 0$，行列式为0，矩阵奇异
- $\forall \lambda_i \neq 0$，行列式不为0，矩阵非奇异


#### 常用方法




### rank
独立的方程的个数;
矩阵中线性无关的行或者列的数目

- $rank(A) = rank(A^T)$
- $rank(A) = rank(A^H)$
- $rank(A) = rank(AA^H)$


### Tensors（todo）






### Matrix Norms

三维到二维的变换 $T : \mathbb{R}^3 \mapsto \mathbb{R}^2$

$$
T_1(x) = \begin{bmatrix} x_1 + x_2 \\ x_1 - x_2 \end{bmatrix}, \quad \text{其中}, \quad x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
$$

$$
T_2(x) = \begin{bmatrix} x_1 - x_2 \\ x_2 + x_3 \end{bmatrix}, \quad \text{其中}, \quad x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
$$

正交投影算子 $w = T(x)$

$$
\begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
$$

## 矩阵之间

!!! attention "关注矩阵运算是如何改变矩阵的维度的"

### 矩阵乘法
矩阵乘法的行视角： 每一行都代表不同样本的特征；
左乘行向量相当于对行进行操作


矩阵乘法的列视角：每一列都作为最后结果中的一个成分（采集语音）
右乘列向量相当于对列进行操作

!!! note "鸡尾酒会问题 Blind Signal Seperation"


$$
\begin{aligned}&\mathbf{A}(\mathbf{BC})=(\mathbf{AB})\mathbf{C}\\&(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{AC}+\mathbf{BC}\\&A(B+C)=AB+AC\\&\alpha(\mathbf{A}+\mathbf{B})=\alpha\mathbf{A}+\alpha\mathbf{B}\end{aligned}
$$


### 直和 - 对角块拼接

矩阵的维度是变大的

$m \times m$ 矩阵 $A$ 与 $n \times n$ 矩阵 $B$ 的直和（direct sum）记作 $A \oplus B$，它是一个 $(m + n) \times (m + n)$ 矩阵，定义为：

$$
A \oplus B = 
\begin{bmatrix}
A & O_{m \times n} \\
O_{n \times m} & B
\end{bmatrix}
$$

其中，$O_{m \times n}$ 和 $O_{n \times m}$ 分别表示 $m \times n$ 和 $n \times m$ 的零矩阵。

**block diagonal matrix**

- 不满足交换律
- 满足结合律

### Hadamard product - 逐元素相乘

$$
(A_{m\times n} B_{m\times n})_{ij} = a_{ij} b_{ij}
$$

### Kronecker product - 元素乘矩阵

- 应用：雷达、信号处理

每个元素都乘一个矩阵

=== "右 Kronecker 积"

    $m \times n$ 矩阵 $A = [a_{11}, \cdots, a_{mn}]$ 和 $p \times q$ 矩阵 $B$ 的右 Kronecker 积记作 $A \otimes B$，是一个 $mp \times nq$ 矩阵，定义为
    
    $$
    A \otimes B = [a_{ij}B]_{m \times n}^{p \times q} = \begin{bmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{bmatrix}
    $$

=== "左 Kronecker 积"

    $m \times n$ 矩阵 $A$ 和 $p \times q$ 矩阵 $B = [b_{11}, \cdots, b_{pq}]$ 的左 Kronecker 积 $A \otimes B$ 是一个 $mp \times nq$ 矩阵，定义为
    
    $$
    [A \otimes B]_{\text{left}} = [Ab_{ij}]_{m \times n}^{p \times q} = [b_{ij}A]_{p \times q}^{m \times n} = \begin{bmatrix} Ab_{11} & Ab_{12} & \cdots & Ab_{1q} \\ Ab_{21} & Ab_{22} & \cdots & Ab_{2q} \\ \vdots & \vdots & \ddots & \vdots \\ Ab_{p1} & Ab_{p2} & \cdots & Ab_{pq} \end{bmatrix}
    $$

显然，无论左或右 Kronecker 积都是一一映射：$\mathbb{R}^{m \times n} \times \mathbb{R}^{p \times q} \rightarrow \mathbb{R}^{mp \times nq}$



??? note "Kronecker积的例子"

    $$
    A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix},B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
    $$
    
    $$
    A \otimes B = \begin{bmatrix} 1 \cdot B & 2 \cdot B \\ 3 \cdot B & 4 \cdot B \end{bmatrix}
    $$


    $$
    A \otimes B = \begin{bmatrix} \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix} & \begin{bmatrix} 10 & 12 \\ 14 & 16 \end{bmatrix} \\ \begin{bmatrix} 15 & 18 \\ 21 & 24 \end{bmatrix} & \begin{bmatrix} 20 & 24 \\ 28 & 32 \end{bmatrix} \end{bmatrix}
    $$

### 向量化和矩阵化

motivation: 如何把一张图或者一个视频变成一个向量，送到神经网络中

按列堆栈：

$$
A = \begin{bmatrix}
| & | & & | \\
a_1 & a_2 & \cdots & a_n \\
| & | & & |
\end{bmatrix}\quad  \text{vec}(A) = \begin{bmatrix} a_1 \\ \vdots \\ a_n \end{bmatrix}
$$


按行堆栈：

$$
A = \begin{bmatrix}
—— & a_1 & —— \\
—— & a_2 & —— \\
—— & \cdots& —— \\
—— & a_n & —— \\
\end{bmatrix}\quad \text{rvec}(A) = \begin{bmatrix} -a_{1}-,- a_{2}-, \ldots, -a_{n}- \end{bmatrix}
$$



!!! example "向量化和矩阵化"

    Consider a matrix $A$:

    $$
    A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
    $$

    The vectorization of $A$ by stacking its columns is:

    $$
    \text{vec}(A) = \begin{bmatrix} 1 \\ 3 \\ 2 \\ 4 \end{bmatrix}
    $$


    The vectorization of $A$ by stacking its rows is:

    $$
    \text{rvec}(A) = \begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}
    $$

In numpy, this can be achieved using:


```python   
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A.flatten(order='F')) # 按列堆栈 1,3,2,4
print(A.flatten(order='C')) # 按行堆栈 1,2,3,4
```

```python title="按列堆栈和按行堆栈演示"
import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)

print(A.reshape(-1, order='F'))# 按列堆栈 1,3,2,4
print(A.reshape(1, -1))# 按行堆栈 1,2,3,4
```












## 微分
### 变元与函数

$\boldsymbol{x}=[x_1,\cdots,x_m]^{\mathrm{T}}\in\mathbb{R}^m$ 为实向量变元；

$\boldsymbol{X}=[\boldsymbol{x}_1,\cdots,\boldsymbol{x}_n]\in\mathbb{R}^{m\times n}$ 为实矩阵变元；


根据输入输出的类型不同，我们可以把函数分为以下几种：




| 输入\输出 | 输入为向量 $\boldsymbol{x}\in\mathbb{R}^m$ | 输入为矩阵 $\boldsymbol{X}\in\mathbb{R}^{m\times n}$ |
|---|---|---|
| 标量输出 | $f(\boldsymbol{x})\in\mathbb{R}$，记作 $f:\mathbb{R}^m\to\mathbb{R}$ <br> 例：向量的范数 | $f(\boldsymbol{X})\in\mathbb{R}$，记作 $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ <br> 例：矩阵的迹 |
| 向量输出 | $f(\boldsymbol{x})\in\mathbb{R}^p$，记作 $f:\mathbb{R}^m\to\mathbb{R}^p$ <br> 例：卷积、傅立叶变换 | $f(\boldsymbol{X})\in\mathbb{R}^p$，记作 $f:\mathbb{R}^{m\times n}\to\mathbb{R}^p$ |
| 矩阵输出 | $\boldsymbol{F}(\boldsymbol{x})\in\mathbb{R}^{p\times q}$，记作 $\boldsymbol{F}:\mathbb{R}^m\to\mathbb{R}^{p\times q}$ <br> 例：vandermonde矩阵、confusion matrix | $\boldsymbol{F}(\boldsymbol{X})\in\mathbb{R}^{p\times q}$，记作 $\boldsymbol{F}:\mathbb{R}^{m\times n}\to\mathbb{R}^{p\times q}$ <br> 例：输入是猫狗图，输出是猫狗分类结果 |

微分与积分：element-wise
$$
\frac{\mathrm{d} \mathbf{A}}{\mathrm{d} t} = \mathbf{\dot{A}} = \begin{bmatrix} \frac{\mathrm{d} a_{11}}{\mathrm{d} t} & \frac{\mathrm{d} a_{12}}{\mathrm{d} t} & \cdots & \frac{\mathrm{d} a_{1n}}{\mathrm{d} t} \\ \frac{\mathrm{d} a_{21}}{\mathrm{d} t} & \frac{\mathrm{d} a_{22}}{\mathrm{d} t} & \cdots & \frac{\mathrm{d} a_{2n}}{\mathrm{d} t} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\mathrm{d} a_{m1}}{\mathrm{d} t} & \frac{\mathrm{d} a_{m2}}{\mathrm{d} t} & \cdots & \frac{\mathrm{d} a_{mn}}{\mathrm{d} t} \end{bmatrix}
$$

$$
\int \mathbf{A} \mathrm{d} t = \begin{bmatrix} \int a_{11} \mathrm{d} t & \int a_{12} \mathrm{d} t & \cdots & \int a_{1n} \mathrm{d} t \\ \int a_{21} \mathrm{d} t & \int a_{22} \mathrm{d} t & \cdots & \int a_{2n} \mathrm{d} t \\ \vdots & \vdots & \ddots & \vdots \\ \int a_{m1} \mathrm{d} t & \int a_{m2} \mathrm{d} t & \cdots & \int a_{mn} \mathrm{d} t \end{bmatrix}
$$

矩阵求导的链式法则

$$
\frac{\mathrm{d}}{\mathrm{d} t} (\mathbf{A} \mathbf{B}) = \frac{\mathrm{d} \mathbf{A}}{\mathrm{d} t} \mathbf{B} + \mathbf{A} \frac{\mathrm{d} \mathbf{B}}{\mathrm{d} t}
$$

### 标量函数&向量变元 - 行偏导

行偏导算子

$$
\begin{align*}
\mathrm{D}_{x}&\overset{\mathrm{def}}{\operatorname*{=}}\frac{\partial}{\partial {x^{\mathrm{T}}}_{1\times m}}=\left[\frac{\partial}{\partial x_{1}},\cdots,\frac{\partial}{\partial x_{m}}\right]_{1\times m}\\
\mathrm{D}_{\boldsymbol{x}}f(\boldsymbol{x})&=\frac{\partial f(\boldsymbol{x})}{\partial\boldsymbol{x}^{\mathrm{T}}}=\left[\frac{\partial f(\boldsymbol{x})}{\partial x_{1}},\cdots,\frac{\partial f(\boldsymbol{x})}{\partial x_{m}}\right]
\end{align*}
$$



!!! example "行偏导"

    $$
    \begin{aligned}
    f(x)&=x^{T}x\\
    D_{x}f(x)&=\frac{\partial f(x)}{\partial x^{T}}=[\frac{\partial f(x)}{\partial x_{1}}\cdots\frac{\partial f(x)}{\partial x_{m}}]\\
    &=[\frac{\partial x^{T}x}{\partial x_{1}}\cdots\frac{\partial x^{T}x}{\partial x_{m}}]\\
    &=[2x_{1}\cdots2x_{m}]=2x^{T}\end{aligned}
    $$

### 标量函数&矩阵变元 - 行偏导
如果变元是矩阵，也可以写出行偏导

$$
\begin{aligned}
&\mathrm{D}_{\mathrm{vec}\boldsymbol{X}}f(\boldsymbol{X})=\frac{\partial f(\boldsymbol{X})}{\partial\mathrm{vec}^{\mathrm{T}}(\boldsymbol{X})}=\left[\frac{\partial f(\boldsymbol{X})}{\partial x_{11}},\cdots,\frac{\partial f(\boldsymbol{X})}{\partial x_{m1}},\cdots,\frac{\partial f(\boldsymbol{X})}{\partial x_{1n}},\cdots,\frac{\partial f(\boldsymbol{X})}{\partial x_{mn}}\right]_{1\times mn}\\
&\mathrm{D}_{\mathrm{vec}\boldsymbol{X}}f(\boldsymbol{X})=\mathrm{rvec}(\mathrm{D}_{\boldsymbol{X}}f(\boldsymbol{X}))=\left(\mathrm{vec}(\mathrm{D}_{\boldsymbol{X}}^{\mathbf{T}}f(\boldsymbol{X}))\right)^{\mathbf{T}}
\end{aligned}
$$

所以求行偏导的结果相当于把雅可比矩阵给行向量化了


### 标量函数&矩阵变元 - Jacobian Matrix

$f(X)$ 关于矩阵变元 $X$ 的 Jacobian 矩阵

$X \in \mathbb{R}^{m \times n}$

$$
D_X f(X) = \frac{\partial f(X)}{\partial X^T} = \begin{bmatrix} \frac{\partial f(X)}{\partial x_{11}} & \ldots & \frac{\partial f(X)}{\partial x_{m1}} \\ \vdots & \ddots & \vdots \\ \frac{\partial f(X)}{\partial x_{1n}} & \ldots & \frac{\partial f(X)}{\partial x_{mn}} \end{bmatrix} \in \mathbb{R}^{n \times m}
$$




### 矩阵函数&矩阵变元 - Jacobian Matrix


$$
\mathrm{D}_{\boldsymbol{X}}\boldsymbol{F}(\boldsymbol{X})\overset{\mathrm{def}}{\operatorname*{=}}\frac{\partial\mathrm{vec}(\boldsymbol{F}(\boldsymbol{X}))}{\partial(\mathrm{vec}\boldsymbol{X})^{\mathrm{T}}}\in\mathbb{R}^{pq\times mn}
$$

思路：

- 把矩阵函数列向量化$vec(\mathbf{F}(\mathbf{X})) =vec\begin{bmatrix}\mathbf{F}_{1} & \mathbf{F}_{2} & \cdots & \mathbf{F}_{q} \end{bmatrix}$
- 列向量化之后，相当于把矩阵函数的每一个元素展开成了一个列向量，然后相当于标量对于矩阵求行偏导


$$
\begin{aligned}
&\mathrm{D}_{\boldsymbol{X}}\boldsymbol{F}(\boldsymbol{X})=\begin{bmatrix}\frac{\partial f_{11}}{\partial(vecX)^{\mathrm{T}}}\\\vdots\\\frac{\partial f_{p1}}{\partial(vecX)^{\mathrm{T}}}\\\vdots\\\frac{\partial f_{1q}}{\partial(vecX)^{\mathrm{T}}}\\\vdots\\\frac{\partial f_{pq}}{\partial(vecX)^{\mathrm{T}}}\end{bmatrix}
=\begin{bmatrix}\frac{\partial f_{11}}{\partial x_{11}}&\cdots&\frac{\partial f_{11}}{\partial x_{m1}}&\cdots&\frac{\partial f_{11}}{\partial x_{1n}}&\cdots&\frac{\partial f_{11}}{\partial x_{mn}}\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\frac{\partial f_{p1}}{\partial x_{11}}&\cdots&\frac{\partial f_{p1}}{\partial x_{m1}}&\cdots&\frac{\partial f_{p1}}{\partial x_{1n}}&\cdots&\frac{\partial f_{p1}}{\partial x_{mn}}\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\frac{\partial f_{1q}}{\partial x_{11}}&\cdots&\frac{\partial f_{1q}}{\partial x_{m1}}&\cdots&\frac{\partial f_{1q}}{\partial x_{1n}}&\cdots&\frac{\partial f_{1q}}{\partial x_{mn}}\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\vdots&\vdots&\vdots&\vdots&\vdots&\vdots\\\frac{\partial f_{pq}}{\partial x_{11}}&\cdots&\frac{\partial f_{pq}}{\partial x_{m1}}&\cdots&\frac{\partial f_{pq}}{\partial x_{1n}}&\cdots&\frac{\partial f_{pq}}{\partial x_{mn}}\end{bmatrix}
\end{aligned}
$$


### 列向量

$m\times1$列向量偏导算子即梯度算子记作$\nabla_{\boldsymbol{x}}$,定义为

$$\nabla_{x}\stackrel{\mathrm{def}}{=}\frac{\partial}{\partial x_{m\times1}}=\left[\frac{\partial}{\partial x_{1}},\cdots,\frac{\partial}{\partial x_{m}}\right]^{\mathrm{T}}$$


$$
\nabla_{\boldsymbol{x}}f(\boldsymbol{x})\stackrel{\mathrm{def}}{=}\left[\frac{\partial f(\boldsymbol{x})}{\partial x_{1}},\cdots,\frac{\partial f(\boldsymbol{x})}{\partial x_{m}}\right]^{\mathrm{T}}=\frac{\partial f(\boldsymbol{x})}{\partial\boldsymbol{x}}
$$

!!! example "求导"
    $$
    f(x) = x^{T}x = \sum_{i=1}^{n}x_{i}^{2}
    $$

    $$
    \nabla_{x}f(x) = \begin{bmatrix} \frac{\partial \sum_{i=1}^{n}x_{i}^{2}}{\partial x_{1}} \\ \vdots \\ \frac{\partial \sum_{i=1}^{n}x_{i}^{2}}{\partial x_{n}} \end{bmatrix} = \begin{bmatrix} 2x_{1} \\ \vdots \\ 2x_{n} \end{bmatrix} = 2x
    $$



### 记忆公式


特例：$y \in R^{m\times 1}$, $\mathbf{A} \in R^{m\times m}$

- $\frac{\partial{\mathbf{A}\mathbf{X}}}{\partial{\mathbf{X}}} = \mathbf{A}^T$
- $\frac{\partial{\mathbf{X}^T\mathbf{A}\mathbf{X}}}{\partial{\mathbf{X}}} = \mathbf{A}^T\mathbf{X} + \mathbf{AX}$

### 计算法则



### Higher Order Derivatives

### Taylor Series

### Partial Derivatives


### Gradient

### Hessian Matrix

### Jacobian Matrix（todo）



## 积分



$$
\int\mathbf{A}\mathrm{d}t=\begin{bmatrix}\int a_{11}\mathrm{d}t&\int a_{12}\mathrm{d}t&\cdots&\int a_{1n}\mathrm{d}t\\\int a_{21}\mathrm{d}t&\int a_{22}\mathrm{d}t&\cdots&\int a_{2n}\mathrm{d}t\\\vdots&\vdots&\ddots&\vdots\\\int a_{m1}\mathrm{d}t&\int a_{m2}\mathrm{d}t&\cdots&\int a_{mn}\mathrm{d}t\end{bmatrix}
$$