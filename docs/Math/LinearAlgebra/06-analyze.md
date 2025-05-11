# 06 | 特征分析


为什么要研究特征分析？


给系统一个很好的表征

找到复杂信号的简单表达






## 线性空间



## 基与坐标

### 正交化


我们可以采集到很多信号，可以用均值、协方差来表征


但是，信号可能是耦合关联的，这说明有冗余信息

我们希望建立一个向量组，元素和元素之间是无关的，协方差矩阵是对角矩阵







### 线性映射

线性映射（Linear Mapping）是指满足齐次性（Homogeneity）和叠加性（Additivity）的映射。

$$
T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})
$$

其中，$c_1$ 和 $c_2$ 是任意标量，$\mathbf{u}$ 和 $\mathbf{v}$ 是任意向量。


举例：投影矩阵

!!! example "正交投影矩阵"

    平面，向y轴投影

    $$
    \omega = T(\begin{bmatrix} x \\ y \end{bmatrix})
    $$

    $$
    T = \begin{bmatrix} 0&0\\0&1 \end{bmatrix}
    $$


## 特征值

对于方阵$A$，满足以下方程的$\lambda$称为特征值

第一定义

$$
\mathbf{A} \mathbf{v} = \lambda \mathbf{v}
$$

第二定义

$$
det(\mathbf{A} - \lambda \mathbf{I}) = 0
$$


- $A = A^H$，特征值为实数
- 同一特征值的重复次数称为代数重数
- 特征值的个数称为几何重数

**特征值和正定性**

- 特征值为正，矩阵正定
- 特征值非负，矩阵半正定
- 特征值为负，矩阵负定
- 特征值非正，矩阵半负定
- 特征值有正有负，矩阵不定

**性质**

$$
det(A) = \prod_{i=1}^n \lambda_i
$$

$$
tr(A) = \sum_{i=1}^n \lambda_i
$$


所有特征值的集合 矩阵的谱 spectrum

$$
\lambda(A) = \{\lambda_1, \lambda_2, \cdots, \lambda_n\}
$$

$$
\rho(A) = \max_{i=1,2,\cdots,n} |\lambda_i| = |(\lambda(A))|_{L_{\infty}}
$$

特征值的模


### 矩阵多项式

$$
A\nu = \lambda \nu
$$

$$
A^2\nu = A(A\nu) = A(\lambda \nu) = \lambda (A\nu) = \lambda^2 \nu
$$

$$
A^k\nu = \lambda^k \nu
$$



$$
e^A = I + A + \frac{A^2}{2!} + \cdots + \frac{A^k}{k!} + \cdots
$$

$$
[e^A] \nu = \sum_{k=0}^{\infty} \frac{A^k}{k!} \nu = \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} \nu = e^{\lambda} \nu
$$



### Cayley-Hamilton定理 - 求逆

$$
P_n A^n + P_{n-1}A^{n-1} + \cdots + P_1A + P_0I = 0
$$

- $P_n$来自$P(x) = det(xI - A)$


同乘$A^{-1}$

$$
P_n A^{n-1} + P_{n-1}A^{n-2} + \cdots + P_1I + P_0A^{-1} = 0
$$

$$
A^{-1} = -\frac{1}{P_0}(P_n A^{n-1} + P_{n-1}A^{n-2} + \cdots + P_1I)
$$

















## 特征向量

