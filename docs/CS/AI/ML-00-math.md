# 00 | Math in ML
!!! note "相关课程"
    === "矩阵论 | 程磊"
        智云链接：[2024秋冬](https://classroom.zju.edu.cn/livingroom?course_id=66128&sub_id=1264000)<br>
        教师：程磊（老师特别有意思hhh）<br>
        上课风格：课前会有同学来帮助回顾上节课的内容，老师推导也特别清楚，会联系到一些与其他课程相关联的例子<br>
        旁听友好<br>

    === "MIT 18.065 | Gilbert Strang"
        链接：<br>
        教师：Gilbert Strang<br>
        还没上过<br>

## Vectors
### Norm | 范数
[什么是范数（norm）？以及L1,L2范数的简单介绍\_l1 norm-CSDN博客](https://blog.csdn.net/qq_37466121/article/details/87855185)


应用：聚类、流行学习、特征学习的重点就是设计一种合理的范数


=== "$L_0$ 范数（也称 0 范数）"

    $$
    \|x\|_0 \stackrel{\text{def}}{=} \text{非零元素的个数}
    $$

=== "$L_1$ 范数（也称和范数或 1 范数）"

    $$
    \|x\|_1 \stackrel{\text{def}}{=} \sum_{i=1}^{m} |x_i| = |x_1| + \cdots + |x_m|
    $$

=== "$L_2$ 范数（常称 Euclidean 范数，有时也称 Frobenius 范数）"

    $$
    \|x\|_2 = \sqrt{(x_1)^2 + \cdots + (x_m)^2}
    $$

=== "$L_\infty$ 范数（也称无穷范数或极大范数"
    
    $$
    \|x\|_\infty = \max\{|x_1|, \cdots, |x_m|\}
    $$
    
    用于worst case control等领域



=== "$L_p$ 范数（也称 Hölder 范数"

    $$
    \|x\|_p = \left(\sum_{i=1}^{m} |x_i|^p\right)^{1/p}, \quad p \geq 1
    $$


=== "随机向量范数"

    $$
    \|x(\xi)\|^2 \stackrel{\text{def}}{=} \mathbb{E}\{x^H(\xi) x(\xi)\}
    $$


### inner Product | 内积

内积把向量降维成为标量




**典范内积**

$$
\langle x, y \rangle = x^H y = \sum_{i=1}^n x_i^* y_i
$$

**加权内积**

$$
\langle x, y \rangle = x^H G y
$$

其中，$G$ 为正定 Hermitian 矩阵（二次型大于零）。

**函数向量内积**

$$
\langle x(t), y(t) \rangle \stackrel{\text{def}}{=} \int_a^b x^*(t) y(t) \, dt
$$

!!! note "DFT 变换"
    $$
    X(f) = \sum_{n=0}^{N-1} x(n) e^{-j \left(\frac{2\pi}{N}\right) n f} = e_N^H x = \langle e_{N-1}, x \rangle
    $$


**夹角定义**

$$
\cos \theta \stackrel{\text{def}}{=} \frac{\langle x, y \rangle}{\sqrt{\langle x, x \rangle} \sqrt{\langle y, y \rangle}} = \frac{\int_a^b x^H(t) y(t) \, dt}{\|x(t)\| \cdot \|y(t)\|}
$$

其中，

$$
\|x(t)\| \stackrel{\text{def}}{=} \left(\int_a^b x^H(t) x(t) \, dt\right)^{1/2}
$$


随机向量内积

$$
\langle x(\xi), y(\xi) \rangle \stackrel{\text{def}}{=} \mathbb{E}\{x^H(\xi) y(\xi)\}
$$




### outer product | 外积（升维）

如果想计算两个向量的正交性

$$
\mathbb{E}\{x(\xi) y^H(\xi)\} = O_{m \times n}
$$

两个向量之间互不含有任何成分，不存在任何相互作用或干扰。



### rotate



### Vector Projection

## 矩阵
### norm
1. **诱导范数（Induced Norm）**：
   - 诱导范数定义为：$\|A\| = \max \{\|Ax\| : x \in K^n, \|x\| = 1 \}$
   - 或者等价地定义为：$\|A\| = \max \left\{ \frac{\|Ax\|}{\|x\|} : x \in K^n, x \neq 0 \right\}$

2. **常用的诱导范数 - p 范数（p-Norm）**：
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


| 性质/指标 | 描述|
|---|---|
| 正定性     | 矩阵的正定性与负定性                       |
| 行列式     | 矩阵的奇异性                              |
| 特征值     | 矩阵的奇异性、正定性和对角元素的结构      |
| 迹         | 矩阵对角元素之和、特征值之和             |
| 秩         | 行（或列）之间的线性无关性、矩阵方程的解空间 |


### quadratic form | 二次型

对于任意一个二次型函数 $f(x_1, \ldots, x_n) = \sum_{i=1}^n \sum_{j=1}^n \alpha_{ij} x_i x_j$，存在许多矩阵 $A$，它们的二次型 $x^T A x = f(x_1, \ldots, x_n)$ 相同。

> 二次型一般用两个sum来表示

**唯一性条件**：
- 只有实对称矩阵或复共轭对称矩阵满足唯一性，即 $x^T A x = f(x_1, \ldots, x_n)$。
- 二次型函数一定是实值函数。


**二次型理论**
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
    x_i^T A x_i > 0 \implies x_i^T \lambda_i x_i > 0 \implies \lambda_i \|x_i\|^2 > 0 \implies \lambda_i > 0
    $$

### determinant

$$
det(AB) = det(A) \cdot det(B)
$$



??? note "$det = \Pi_i^n \lambda_i$"
    矩阵的行列式等于其特征值的乘积<br>
    
    对于一个 $n \times n$ 的方阵 $A$，如果它有 $n$ 个线性无关的特征向量 $v_1, v_2, \ldots, v_n$，那么 $A$ 可以表示为：
    
    $$ 
    A = V \Lambda V^{\mathbf{H}}\\
    det(A) = det(V) \cdot det(\Lambda) \cdot det(V^{\mathbf{H}}) = det(\Lambda) 
    $$
    
    而特征向量矩阵 $V$ 是正交矩阵$V\cdot V^{\mathbf{H}} = I$；所以 $det(V) = 1$
    
    又因为 $det(\Lambda) = \lambda_1 \lambda_2 \cdots \lambda_n$，所以 $A$ 的行列式等于它的特征值的乘积。



### trace
所有特征值之和

$$
tr(A) = \sum_{i=1}^n \lambda_i
$$


### rank
独立的方程的个数;
矩阵中线性无关的行或者列的数目

- $rank(A) = rank(A^T)$
- $rank(A) = rank(A^H)$
- $rank(A) = rank(AA^H)$


### Tensors（todo）



### Eigenvalues | 特征值

$$
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}
$$

$$
det(\mathbf{A} - \lambda \mathbf{I}) = 0
$$

### Eigenvectors | 特征向量


### inverse | 逆矩阵


若 $A$ 和 $B$ 均可逆，则 $(AB)^{-1} = B^{-1}A^{-1}$


#### 矩阵求逆引理

$$
(A + xy^H)^{-1} = A^{-1} - \frac{A^{-1}xy^HA^{-1}}{1 + y^HA^{-1}x}
$$


已经完成了矩阵的求逆，在A的基础上加上一个秩为1矩阵，求解逆矩阵的变化

??? note "应用：自相关矩阵求逆$\hat{R}^{-1}(n)$"

    $\lambda$用来表征遗忘因子;$\lambda$越小，越倾向于线性现在的数据
    
    $$
    (\lambda R + xx^H)^{-1} = \lambda^{-1}R^{-1} - \frac{(\lambda^{-1}R^{-1}x)(\lambda^{-1}R^{-1}x)^H}{1 + \lambda^{-1}x^HR^{-1}x}
    $$


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



#### Moore-Penrose Inverse | 伪逆矩阵

!!! note "构造方法：想要构造成已经学过的方阵的求逆问题"
	都是构造一个方阵

对于方程 $\mathbf{Ax} = \mathbf{b}$,其中$\mathbf{A}_{m\times n}$， $m$代表方程的个数，$n$代表未知数的个数

=== "左逆"

    仅当 $m \geq n$ 时("Tall matrix")，说明这个时候方程的数目大于未知数的个数，方程是过定(overdetermined)的。矩阵 $A$ 可能有**左逆矩阵** 
    
    $$
    A^\dagger_L = \left(A^HA\right)^{-1}A^H
    $$
    
    左逆列满秩的时候一定存在
    
    **超定方程最小二乘解**





=== "右逆"

    仅当 $m \leq n$ 时("fat matrix")，方程数目小于未知数的个数，方程式欠定的。矩阵 $A$ 可能有**右逆矩阵** 
    
    $$
    A^\dagger_R = A^H\left(AA^H\right)^{-1}
    $$
    
    右逆行满秩的时候一定存在
    
    欠定方程最小范数解

**computational demanding**


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

## 矩阵运算
!!! note "要关注矩阵运算对于矩阵维度的影响"

### 矩阵乘法
矩阵乘法的行视角： 每一行都代表不同样本的特征；
左乘行向量相当于对行进行操作


矩阵乘法的列视角：每一列都作为最后结果中的一个成分（采集语音）
右乘列向量相当于对列进行操作

!!! note "鸡尾酒会问题 Blind Signal Seperation"

### 直和

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

### Hadamard product
逐元素相乘

$$
(A_{m\times n} B_{m\times n})_{ij} = a_{ij} b_{ij}
$$

### Kronecker product

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




## 特殊矩阵

### Hermitian 矩阵

复共轭对称矩阵 $R = R^{H}$

- 满足线性关系
- 相关矩阵、协方差矩阵
### 置换矩阵 | permutation matrix
每一行以及每一列只有一个元素为1，其他元素为0




性质
- 右乘是对列重新排列
- 左乘是对行进行重新排列


1. $(P_{m \times n})^T = P_{n \times m}$
2. $P^T P = P P^T = I$，这说明置换矩阵是正交矩阵。
3. $P^T = P^{-1}$


### 广义置换矩阵

$$
G = \begin{bmatrix} 0 & 0 & 0 & 0 & \alpha \\ 0 & 0& \beta  & 0 & 0 \\ 0 & \gamma & 0 & 0 & 0 \\ 0 & 0 & 0 & \lambda & 0 \\ \rho & 0 & 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 0 \end{bmatrix} 
\begin{bmatrix} 
\rho & & & & 0\\
 &\gamma & & & \\
 & &\beta & & \\
& & & \lambda& \\
0& & & & \alpha\\
\end{bmatrix}
$$

一个正方矩阵称为广义置换矩阵，简称 g 矩阵，若其每行和每列有一个并且仅有一个非零元素

G 可写为一个置换矩阵和一个非奇异对角阵的乘积,$G = P\Lambda$

可用于观测数据模型和对信号进行恢复,可用于描述：
- 累加导致信号顺序不确定
- 信号幅度不确定

### 酉矩阵 | Unitary matrix

- 方阵
- $U U^{H} = U^{H} U = I$
- 向量内积、向量范数、向量夹角在酉变换下不变
- 正交矩阵在实数域而酉矩阵在复数域


!!! note "并不是将实数域的Transpose扩展到复数域改成Hermitian"
    | 实向量、实矩阵 | 复向量、复矩阵 |
    |----------------|----------------|
    | $\|x\| = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$ | $\|x\| = \sqrt{\|x_1\|^2 + \|x_2\|^2 + \cdots + \|x_n\|^2}$ |
    | 转置 $A^T = [a_{ji}]$， $(AB)^T = B^T A^T$ | 共轭转置 $A^H = [a_{ji}]$， $(AB)^H = B^H A^H$ |
    | 内积 $(x, y) = x^T y$ | 内积 $(x, y) = x^H y$ |
    | 正交性 $x^T y = 0$ | 正交性 $x^H y = 0$ |
    | 对称矩阵 $A^T = A$ | Hermitian矩阵 $A^H = A$ |
    | 正交矩阵 $Q^T = Q^{-1}$ | 酉矩阵 $U^H = U^{-1}$ |
    | 特征值分解 $A = Q \Lambda Q^{-1} = Q \Lambda Q^T$ | 特征值分解 $A = U \Sigma U^H = U \Sigma U^{-1}$ |
    | 范数的正交不变性 $\|Qx\| = \|x\|$ | 范数的酉不变性 $\|Ux\| = \|x\|$ |
    | 内积的正交不变性 $(Qx, Qy) = (x, y)$ | 内积的酉不变性 $(Ux, Uy) = (x, y)$ |


### 正交矩阵

### 三角矩阵


### 反对称矩阵

### 反对称矩阵 | Skew-Symmetric Matrix

一个矩阵 $A$ 被称为反对称矩阵（Skew-Symmetric Matrix），如果它满足以下条件：

$$
A^T = -A
$$

即矩阵的转置等于其负值。

#### 性质
1. **对角线元素为零**：由于 $a_{ii} = -a_{ii}$，所以对角线上的元素必须为零。
2. **奇数阶反对称矩阵的行列式为零**：因为 $det(A) = det(A^T) = det(-A) = (-1)^n det(A)$，当 $n$ 为奇数时，$det(A) = 0$。
3. **特征值**：反对称矩阵的特征值要么为零，要么是纯虚数。
4. **与正交矩阵的关系**：反对称矩阵可以与正交矩阵结合用于描述旋转等操作。
5. **二次型为0**：$A$ 的二次型为0是 $A$是反对称矩阵的充分必要条件。

!!! note "证明"
    **充分性** ：如果 $A$ 的二次型为零，即对于任意向量 $x$，有 $x^T A x = 0$，则可以推导出 $A^T = -A$，从而证明 $A$ 是反对称矩阵。

    $$
    x^T A x = 0 \implies x^T A^T x = 0 \implies x^T (A + A^T) x = 0
    $$

    由于 $A + A^T$ 是对称矩阵，且对于任意向量 $x$，$x^T (A + A^T) x = 0$，所以 $A + A^T = 0$，即 $A^T = -A$。

    **必要性** ：如果 $A$ 是反对称矩阵，即 $A^T = -A$，则对于任意向量 $x$，有 $x^T A x = 0$。这显然成立，因为：

    $$
    x^T A x = x^T (-A^T) x = -x^T A^T x = -(x^T A x)^T = -x^T A x
    $$

    所以 $2x^T A x = 0$，即 $x^T A x = 0$。

#### 应用
- 在物理中，反对称矩阵常用于描述角速度、旋转等。
- 在计算机图形学中，反对称矩阵用于表示三维空间中的叉积操作。
- 在控制理论中，反对称矩阵用于描述系统的稳定性和对称性。


### 相似矩阵

若存在非奇异矩阵S, 使得$B = S^{-1}AS$，则称为$B$ 相似与$A$

- 相似矩阵的特征值相同，特征向量存在线性变换关系
- $det(B)=det(A)$
- $tr(B)=tr(A)$

### 合同矩阵


### Vandermonde 矩阵

Vandermonde 矩阵的每行或每列的元素组成一个等比数列。

$$
A = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ x_1 & x_2 & \cdots & x_n \\ x_1^2 & x_2^2 & \cdots & x_n^2 \\ \vdots & \vdots & \ddots & \vdots \\ x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1} \end{bmatrix} 
$$

或者写成：

$$
A = \begin{bmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ 1 & x_2 & x_2^2 & \cdots & x_2^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^{n-1} \end{bmatrix} 
$$

若第二行元素各不相同，则矩阵非奇异。




DFT:有限长离散序列，时域离散，频域离散

=== "DFT正变换"
    $X_k = \sum_{n=0}^{N-1} x_n e^{-j \frac{2\pi kn}{N}} = \sum_{n=0}^{N-1} x_n \omega^{nk}$，其中 $k = 0, 1, \ldots, N-1$
    $\hat{x} = F x$

    $F = \begin{bmatrix} 1 & 1 & \cdots & 1 \\ 1 & \omega & \cdots & \omega^{N-1} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & \omega^{N-1} & \cdots & \omega^{(N-1)(N-1)} \end{bmatrix}$，其中 $\omega = e^{-j \frac{2\pi}{N}}$，称为Fourier矩阵
    
    - $F^H F = F F^H = N I$
    - $F^{-1} = \frac{1}{N} F^H = \frac{1}{N} F^*$

=== "DFT逆变换"
    $x = F^{-1} \hat{x} = \frac{1}{N} F^* \hat{x}$

    $$
    \begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_{N-1} \end{bmatrix} = \frac{1}{N} \begin{bmatrix} 1 & 1 & \cdots & 1 \\ 1 & \omega^* & \cdots & (\omega^{N-1})^* \\ \vdots & \vdots & \ddots & \vdots \\ 1 & (\omega^{N-1})^* & \cdots & (\omega^{(N-1)(N-1)})^* \end{bmatrix} \begin{bmatrix} X_0 \\ X_1 \\ \vdots \\ X_{N-1} \end{bmatrix}
    $$
    
    $x_n = \frac{1}{N} \sum_{k=0}^{N-1} X_k e^{j \frac{2\pi kn}{N}}$，其中 $n = 0, 1, \ldots, N-1$

**傅里叶矩阵是一个酉矩阵**


### Hadamard 矩阵

$H_n \in \mathbb{R}^{n \times n}$ 所有元素取+1或者-1，且满足 $H_n H_n^T = H_n^T H_n = nI_n$。

性质
- 只有当 $n = 2^k$ 或者 $n$ 是4的整数倍时，Hadamard矩阵才存在。
- 容易验证 $\frac{1}{\sqrt{n}} H_n$ 为标准正交矩阵。
- $n \times n$ Hadamard矩阵 $H_n$ 的行列式 $\det(H_n) = n^{n/2}$。



规范化的标准正交Hadamard矩阵具有通用构造公式：

$$
\tilde{H}_n = \frac{1}{\sqrt{2}} \begin{bmatrix} \tilde{H}_{n/2} & \tilde{H}_{n/2} \\ \tilde{H}_{n/2} & -\tilde{H}_{n/2} \end{bmatrix}
$$

其中：

$$
\tilde{H}_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

### Toeplitz 矩阵

任何一条对角线的元素取相同值：

$$
A = \begin{bmatrix} a_0 & a_{-1} & a_{-2} & \cdots & a_{-n} \\ a_1 & a_0 & a_{-1} & \cdots & a_{-n+1} \\ a_2 & a_1 & a_0 & \cdots & a_{-n+2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n-1} & a_{n-2} & \cdots & a_0 \end{bmatrix} = [a_{i-j}]_{i,j=0}^n 
$$

对称 Toeplitz 矩阵 $A = [a_{i-j}]_{i,j=0}^n$

若一个复 Toeplitz 矩阵的元素满足复共轭对称关系 $ a_{-i} = a_i^* $，则称为 Hermitian Toeplitz 矩阵：

$$
A = \begin{bmatrix} a_0 & a_1^* & a_2^* & \cdots & a_n^* \\ a_1 & a_0 & a_1^* & \cdots & a_{n-1}^* \\ a_2 & a_1 & a_0 & \cdots & a_{n-2}^* \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n-1} & a_{n-2} & \cdots & a_0 \end{bmatrix} 
$$

??? note "卷积操作是Toplitz矩阵"
    卷积操作 $y = x \ast h$ 可以表示为：

    $$
    y[n] = \sum_{k=0}^{K-1} h[k] \cdot x[n-k] 
    $$


    $y = H \cdot x$
    
    $$ 
    H = \begin{bmatrix} h_0 & 0 & 0 & \cdots & 0 \\ h_1 & h_0 & 0 & \cdots & 0 \\ h_2 & h_1 & h_0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ h_{K-1} & h_{K-2} & h_{K-3} & \cdots & h_0 \end{bmatrix} 
    $$

### Hankel矩阵


正方矩阵 $A \in \mathbb{C}^{(n+1) \times (n+1)}$ 称为 Hankel 矩阵，若：

$$
A = \begin{bmatrix} a_0 & a_1 & a_2 & \cdots & a_n \\ a_1 & a_2 & a_3 & \cdots & a_{n+1} \\ a_2 & a_3 & a_4 & \cdots & a_{n+2} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a_n & a_{n+1} & a_{n+2} & \cdots & a_{2n} \end{bmatrix} 
$$

## 方程求解
奇异的意思是：冗余、重复、线性相关
非奇异的意思是：线性无关

> 参考资料 [线性方程组的最小二乘解和最小范数解 - 一以知行](https://zhuanlan.zhihu.com/p/503664717)

### 最小二乘解



目标是最小化**残差向量** $\mathbf{r} = A \mathbf{x} - \mathbf{b}$的**欧几里得范数**，即

$$
\min_{\mathbf{x}} \| A \mathbf{x} - \mathbf{b} \|_2^2
$$

通过求导并令导数为零，可以得到

$$
2 \cdot A^T (Ax - b) = 0
$$

假设$A^T A$可逆，则最小二乘解为：

$$
\mathbf{x}_{\text{LS}} = (A^T A)^{-1} A^T \mathbf{b}
$$

### 最小范数解



也就是离原点最近的解



**Minimize** $\| x \|$

**Subject to**: $A x = b$

直接给出结论，此时问题的最小范数解是：
$$
x^* = A^T (A A^T)^{-1} b
$$
（注意与上面最小二乘式的区别），下面给出证明。

**证明**：令上述问题的解为 $x^* = A^T (A A^T)^{-1} b$，注意

$$
\begin{align}
\| x \|^2 &= \| (x - x^*) + x^* \|^2\\
&= ((x - x^*) + x^*)^T ((x - x^*) + x^*)\\
&= \| x - x^* \|^2 + \| x^* \|^2 + 2 x^{*T} (x - x^*)
\end{align}
$$

由于
$$
\begin{align}
x^{*T} (x - x^*) &= [A^T (A A^T)^{-1} b]^T [x - A^T (A A^T)^{-1} b]\\
&= b^T (A A^T)^{-1} [A x - (A A^T) (A A^T)^{-1} b]\\
&= b^T (A A^T)^{-1} (b - b)\\
&= 0
\end{align}
$$

故有
$$
\| x \|^2 = \| x - x^* \|^2 + \| x^* \|^2
$$

由于对于所有 $x \neq x^*$，都有 $\| x - x^* \|^2 > 0$ 成立，因此，对于所有 $x \neq x^*$，都有 $\| x \|^2 > \| x^* \|^2$，即 $\| x \| > \| x^* \|$，显然 $x^*$ 是惟一的。证明完毕。



### 向量空间


### 线性映射

线性映射（Linear Mapping）是指满足齐次性（Homogeneity）和叠加性（Additivity）的映射。

$$
T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})
$$

其中，$c_1$ 和 $c_2$ 是任意标量，$\mathbf{u}$ 和 $\mathbf{v}$ 是任意向量。


举例：投影矩阵





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

!!! note "已知了样本数据的A，以及最终评价b，那求解x的过程就是模型训练的过程"


## 矩阵方程

### Lyapunov方程

[线性代数 | 李雅普诺夫方程](https://www.zhihu.com/tardis/zm/art/105326895?source_id=1005)

## 矩阵分解
### LU decomposition

### 相似对角化
[全网最快速的特征向量暴力求法（纯干货技巧）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT411E75Q/?spm_id_from=333.337.top_right_bar_window_history.content.click)

[相似对角化太难算，哈-凯定理怒斩A的n次方！（细节拉满了）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV11P411w716/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

!!! note "求解方法"
     **求特征值**：
    - 计算矩阵 $A$ 的特征值 $\lambda_i$ ，这些特征值将构成对角矩阵 $\Lambda$ 的对角线元素。

    **求特征向量**：
    - 对于每个特征值 $\lambda_i$，求解特征向量 $v_i$，这些特征向量将构成矩阵 $P$ 的列。
    
    **构造对角矩阵和特征向量矩阵**：
    - 对角矩阵 $\Lambda$：
        
    $$
    \Lambda = \begin{bmatrix}
    \lambda_1 & 0 & \cdots & 0 \\
    0 & \lambda_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \lambda_n
    \end{bmatrix}
    $$
        
    - 特征向量矩阵 $P$：
    
    $$
    P = \begin{bmatrix}
    | & | & & | \\
    v_1 & v_2 & \cdots & v_n \\
    | & | & & |
    \end{bmatrix}
    $$
    
    **验证对角化**：
    - 验证 $A = P \Lambda P^{-1}$ 是否成立。



### Eigen decomposition | 特征分解

特征值分解是一种特殊的奇异值分解



### SVD | 奇异值分解

变换 = 旋转和伸缩组合

那么如果想把一个变换表示成为旋转和伸缩的组合，考虑先旋转到坐标轴，再做伸缩，最后再旋转回来，这就是奇异值分解

1.奇异值为非负数
2.奇异值主对角线由小到大排列
3.奇异值是特征值开方

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112996076490296&bvid=BV1ExWxesEVf&cid=500001656999667&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

奇异值分解

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=652439242&bvid=BV1YY4y1U7UX&cid=1024031413&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>


## 求导

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

### 行偏导

### 列偏导（梯度







特例：$y \in R^{m\times 1}$, $\mathbf{A} \in R^{m\times m}$

- $\frac{\partial{\mathbf{A}\mathbf{X}}}{\partial{\mathbf{X}}} = \mathbf{A}^T$
- $\frac{\partial{\mathbf{X}^T\mathbf{A}\mathbf{X}}}{\partial{\mathbf{X}}} = \mathbf{A}^T\mathbf{X} + \mathbf{AX}$



### Higher Order Derivatives

### Taylor Series

### Partial Derivatives


### Gradient

### Hessian Matrix

### Jacobian Matrix（todo）






## Probability
### Random variables


### statistics

[从随机变量到随机向量再到随机矩阵：那个你不一定知道的矩阵高斯分布 - 知乎](https://zhuanlan.zhihu.com/p/26286575)

统计不相关：互协方差矩阵是0矩阵 $C_{xy} = O_{m\times n}$
正交：互相关矩阵式零矩阵 $R_{xy} = O_{m\times n}$

#### 均值向量 (Mean Vector)
对于随机向量 $\mathbf{x}$，其均值向量 $\mu_x$ 定义为：

$$
\mu_x = E\{\mathbf{x}(\xi)\} = \begin{bmatrix} E\{x_1(\xi)\} \\ E\{x_2(\xi)\} \\ \vdots \\ E\{x_m(\xi)\} \end{bmatrix} = \begin{bmatrix} \mu_1 \\ \mu_2 \\ \vdots \\ \mu_m \end{bmatrix}
$$



#### correlation 相关矩阵
**自相关**矩阵 $R_x$ 定义为：

$$
R_x = E\{\mathbf{x}(\xi)\mathbf{x}^H(\xi)\} = \begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1m} \\ r_{21} & r_{22} & \cdots & r_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ r_{m1} & r_{m2} & \cdots & r_{mm} \end{bmatrix}
$$

其中，$\mathbf{x}^H(\xi)$ 表示 $\mathbf{x}(\xi)$ 的共轭转置，$r_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的自相关函数。自相关矩阵是复共轭对称矩阵，即 Hermitian 矩阵。


**互相关**

$$
R_{xy} = E\{\mathbf{x}(\xi)\mathbf{y}^H(\xi)\} = \begin{bmatrix} r_{x_1,y_1} & r_{x_1,y_2} & \cdots & r_{x_1,y_n} \\ r_{x_2,y_1} & r_{x_2,y_2} & \cdots & r_{x_2,y_n} \\ \vdots & \vdots & \ddots & \vdots \\ r_{x_m,y_1} & r_{x_m,y_2} & \cdots & r_{x_m,y_n} \end{bmatrix}
$$

其中，$r_{x_i,y_j}$ 表示 $x_i(\xi)$ 和 $y_j(\xi)$ 之间的互相关函数。


#### Covariance 协方差矩阵 

[如何通俗地解释协方差｜马同学图解数学](https://www.bilibili.com/video/BV1gY4y187TL)

[【什么是自相关矩阵，自协方差矩阵，互相关矩阵，互协方差矩阵？】 - 知乎](https://zhuanlan.zhihu.com/p/447221519)
**自协方差**矩阵 $C_x$ 定义为：

$$
C_x = E\{\left[\mathbf{x}(\xi) - \mu_x\right]\left[\mathbf{x}(\xi) - \mu_x\right]^H\} = \begin{bmatrix} c_{11} & c_{12} & \cdots & c_{1m} \\ c_{21} & c_{22} & \cdots & c_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ c_{m1} & c_{m2} & \cdots & c_{mm} \end{bmatrix}
$$

其中，$c_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的协方差。自协方差矩阵也是复共轭对称矩阵。

$$
\mathbf{C_x} = \mathbf{R_x} - \mathbf{\mu_x} \mathbf{\mu_x}^H
$$


**互协方差**矩阵 $C_{xy}$ 定义为：

$$
C_{xy} = E\{\left[\mathbf{x}(\xi) - \mu_x\right]\left[\mathbf{y}(\xi) - \mu_y\right]^H\} = \begin{bmatrix} c_{x_1,y_1} & c_{x_1,y_2} & \cdots & c_{x_1,y_n} \\ c_{x_2,y_1} & c_{x_2,y_2} & \cdots & c_{x_2,y_n} \\ \vdots & \vdots & \ddots & \vdots \\ c_{x_m,y_1} & c_{x_m,y_2} & \cdots & c_{x_m,y_n} \end{bmatrix}
$$

其中，$c_{x_i,y_j}$ 表示 $x_i(\xi)$ 和 $y_j(\xi)$ 之间的协方差。

#### 相关系数

相关系数矩阵（Correlation Matrix）用于衡量随机向量中各个分量之间的线性相关程度。对于随机向量 $\mathbf{x}$，其相关系数矩阵 $\mathbf{R}_x$ 定义为：

$$\mathbf{R}_x = \begin{bmatrix} 1 & \rho_{12} & \rho_{13} & \cdots & \rho_{1m} \\ \rho_{21} & 1 & \rho_{23} & \cdots & \rho_{2m} \\ \rho_{31} & \rho_{32} & 1 & \cdots & \rho_{3m} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \rho_{m1} & \rho_{m2} & \rho_{m3} & \cdots & 1 \end{bmatrix}$$

其中，$\rho_{ij}$ 表示 $x_i(\xi)$ 和 $x_j(\xi)$ 之间的相关系数，其取值范围为 $[-1, 1]$。具体来说，相关系数 $\rho_{ij}$ 定义为：

$$\rho_{ij} = \frac{E\{[x_i(\xi) - \mu_i][x_j(\xi) - \mu_j]^*\}}{\sqrt{E\{[x_i(\xi) - \mu_i]^2\}}\sqrt{E\{[x_j(\xi) - \mu_j]^2\}}}$$

其中，$\mu_i = E\{x_i(\xi)\}$ 和 $\mu_j = E\{x_j(\xi)\}$ 分别表示 $x_i(\xi)$ 和 $x_j(\xi)$ 的均值，$E\{\cdot\}$ 表示期望操作，$[\cdot]^*$ 表示复共轭。

相关系数矩阵具有以下性质：
1. 对角线上的元素全为1，即 $\rho_{ii} = 1$。
2. 相关系数矩阵是复共轭对称矩阵，即 $\mathbf{R}_x = \mathbf{R}_x^H$。
3. 相关系数矩阵的行列式为1，即 $\det(\mathbf{R}_x) = 1$。



### 高斯随机变量
!!! note "为什么噪声一般建模为高斯"
    中心极限定理：独立同分布的随机变量的和，其分布趋近于高斯分布
### complex normal

### Probability distributions
### Bayes’ Theorem（todo）



### Probability Distributions

## Information theory
### Entropy

不确定性函数$f$是概率$P$的减函数；两个独立符号所产生的不确定性应等于各自不确定性之和，即$f(P1,P2)=f(P1)+f(P2)$，这称为可加性。同时满足这两个条件的函数$f$是对数函数，即$f(P)=\log\frac{1}{P} = -\log P$。


### Kullback–Leibler Divergence（todo）

### Cross-entropy（todo）



## Optimization algorithms


## 名词

### 矩阵与向量

| 中文名         | 英文名                        |
|----------------|-------------------------------|
| 矩阵           | Matrix                        |
| 向量           | Vector                        |
| 转置           | Transpose                     |
| 共轭           | Conjugate                     |
| 导数           | Gradient                      |
| 转置共轭       | Hermitian                     |
| 求逆           | Inverse                       |
| 线性组合       | Linear Combination            |
| 线性无关       | Linear Independence           |
| 奇异性         | Singular                      |
| 向量空间       | Vector Space                  |
| 内积           | Inner Product                 |
| 外积           | Outer Product                 |
| 范数           | Norm                          |
| 行列式         | Determinant                   |
| 特征值         | Eigenvalue                    |
| 迹             | Trace                         |
| 秩             | Rank                          |
| 二次型             | Quadratic Form                |
| 求逆           | Inverse                       |
| 矩阵求逆引理   | Matrix Inverse Lemma          |
| 伪逆           | Pseudo Inverse                |
| 直和           | Direct Sum                    |
| Hadamard积     | Hadamard Product              |
| Kronecker积    | Kronecker Product             |
| 稀疏           | Sparse                        |
| 压缩感知       | Compressive Sensing           |
| Hermitian矩阵  | Hermitian Matrix              |
| 置换矩阵       | Permutation Matrix            |
| 通信矩阵       | Communication Matrix          |
| 广义置换矩阵   | Generalized Permutation Matrix|
| 正交矩阵       | Orthogonal Matrix             |
| 酉矩阵         | Unitary Matrix                |
| 上三角矩阵     | Upper Triangular Matrix       |
| 下三角矩阵     | Lower Triangular Matrix       |
| LU分解         | LU Decomposition              |
| Vandemonde矩阵 | Vandemonde Matrix             |
| 相似矩阵       | Similar Matrix                |

### 概率与统计

| 中文名             | 英文名                        |
|--------------------|-------------------------------|
| 概率密度函数       | Probability Density Function (pdf) |
| 累计分布函数       | Cumulative Distribution Function (cdf) |
| 均值向量           | Mean Vector                   |
| 相关矩阵           | Correlation Matrix            |
| 协方差矩阵         | Covariance Matrix             |


### 信息论

| 中文名             | 英文名                        |
|--------------------|-------------------------------|
| 熵                 | Entropy                       |
| Kullback–Leibler散度 | Kullback–Leibler Divergence   |
| 交叉熵             | Cross-entropy                 |

### 优化算法

| 中文名             | 英文名                        |
|--------------------|-------------------------------|
| 梯度下降           | Gradient Descent              |
| 牛顿法             | Newton's Method               |
| 共轭梯度法         | Conjugate Gradient Method     |
| 拉格朗日乘数法     | Lagrange Multipliers          |
| 约束优化           | Constrained Optimization      |
| 无约束优化         | Unconstrained Optimization    |
