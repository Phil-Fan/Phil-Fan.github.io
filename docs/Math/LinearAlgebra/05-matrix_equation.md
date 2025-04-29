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

## 有无解


奇异的意思是：冗余、重复、线性相关
非奇异的意思是：线性无关




## 方程求解


### 初等行变换和高斯消元法

$$
A x = b \xrightarrow{\text{初等行变换}} x = A^{-1} b
$$

$$
[A, b] \xrightarrow{\text{初等行变换}} [I, A^{-1} b]
$$







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
