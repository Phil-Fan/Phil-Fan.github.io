# 01 | 基础


## Vectors
### Norm | 范数
[什么是范数（norm）？以及L1,L2范数的简单介绍\_l1 norm-CSDN博客](https://blog.csdn.net/qq_37466121/article/details/87855185)


应用：聚类、流行学习、特征学习的重点就是设计一种合理的范数


=== "$L_0$ 范数"
    指的是非零元素的个数

    $$
    \|x\|_0 \stackrel{\text{def}}{=} \text{非零元素的个数}
    $$

=== "$L_1$ 范数"
    绝对值的和

    $$
    \|x\|_1 \stackrel{\text{def}}{=} \sum_{i=1}^{m} |x_i| = |x_1| + \cdots + |x_m|
    $$

=== "$L_2$ 范数"
    Euclidean norm，Frobenius norm

    $$
    \|x\|_2 = \sqrt{(x_1)^2 + \cdots + (x_m)^2}
    $$

=== "$L_\infty$ 范数"
    无穷范数

    $$
    \|x\|_\infty = \max\{|x_1|, \cdots, |x_m|\}
    $$
    
    用于worst case control等领域

    $$
    e = \begin{pmatrix} e_1 \\ \vdots \\ e_m \end{pmatrix}
    $$

    $$
    L_{\infty} = max\{|e_1|,|e_2|,\dots,|e_m|\}
    $$

    控制目标：控制最坏情况

    $$
    \mathop{min}_e ||e||_{\infty}
    $$


=== "$L_p$ 范数"
    Hölder 范数

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




## 特殊矩阵

### 对角矩阵


### 幂次矩阵

- 幂等矩阵的特征值为0或1
- 幂等矩阵的行列式为1
- 幂等矩阵的迹为矩阵的秩
- 幂等矩阵的逆矩阵为幂等矩阵
- 幂等矩阵的秩为矩阵的秩
- 幂等矩阵的特征值为1


**幂零矩阵**

- 幂零矩阵的特征值为0
- 幂零矩阵的行列式为0
- 幂零矩阵的迹为0
- 幂零矩阵的逆矩阵不存在

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
