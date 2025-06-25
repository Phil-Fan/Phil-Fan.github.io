# 04 | 矩阵分解


## LDU decomposition
- L: lower triangular matrix
- D: diagonal matrix
- U: upper triangular matrix


```matlab
A = [1 2 3; 4 5 6; 7 8 9];
[L, D, U] = ldu(A);
```




## 正交变换

标准正交变换：最后变换后的向量的协方差矩阵是对角矩阵


高度相关的向量进行解相关操作


迷向圆变换：最后变换后的向量的协方差矩阵是单位矩阵

随机向量不仅变成了独立的，能量还是1，想当于是白噪声


## EVD | 特征分解

处理的一般是 

$$
A = U \Sigma U^H
$$

- U拿出来之后，可以用来降维；
- 可以用来去相关

绕不开的操作是求解协方差矩阵


特征值分解是一种特殊的奇异值分解


$$
\begin{cases}
Au_1 = \lambda_1 u_1 \\
Au_2 = \lambda_2 u_2 \\
\vdots \\
Au_n = \lambda_n u_n
\end{cases}
$$

写成矩阵形式

$$
A \begin{bmatrix}
u_1 & u_2 & \cdots & u_n
\end{bmatrix} = \begin{bmatrix}
\lambda_1 u_1 & \lambda_2 u_2 & \cdots & \lambda_n u_n
\end{bmatrix} = \begin{bmatrix}
u_1 & u_2 & \cdots & u_n
\end{bmatrix} \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

使用特征向量矩阵$U$表示

$$
A U=  U \Lambda
$$


### Hermitian矩阵特征分解

设 $X$ 是一个 $n \times n$ 的 Hermitian 矩阵, 特征值分解 (Eigenvalue Decomposition, EVD) 可以写成:

$$
X = U \Sigma U^H = [u_1 \quad u_2 \cdots \quad u_n] \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix} \begin{bmatrix}
u_1^H \\
u_2^H \\
\vdots \\
u_n^H
\end{bmatrix} = \sum_{i=1}^{n} \lambda_i u_i u_i^H
$$

这里:
$u_1, u_2, ..., u_n$ 是矩阵的特征向量; $\lambda_1, \lambda_2, ..., \lambda_n$ 是矩阵的特征值


### PCA | 主成分分析

线性降维写成矩阵乘法形式：

$$
\Phi x_n=z_n
$$

- 投影矩阵：$\Phi\in R^M\times D$
- 原始数据向量：$\mathbf{x}_n\in R^{D\times1}$
- 降维后的向量：$\mathbf{z}_n\in R^M\times1$


**主成分分析(PCA):**


PCA 是一种基于特征分解的统计技术，用于简化数据集的复杂性，同时保留尽可能多的方差 (信息)。它通过找到数据集中方差最大的方向 (主成分),将高维数据投影到这些方向上，实现降维。



对于样本 $\{x_n\}_{n=1}^N$，PCA 的步骤如下：

1. **计算数据均值向量（或中心化）：**
   
   $$
   \mu = \frac{1}{N} \sum_{n=1}^N x_n
   $$

2. **估计协方差矩阵：**
   
   $$
   \widehat{C} = \frac{1}{N-1} \sum_{n=1}^N (x_n - \mu)(x_n - \mu)^H
   $$

3. **对协方差矩阵 $\widehat{C}$ 进行特征值分解EVD：**
   
   $$
   \widehat{C} = U \Sigma U^H
   $$
   
   或者写为
   
   $$
   \widehat{C} = [u_1 \quad u_2 \cdots \quad u_n]
   \begin{bmatrix}
   \lambda_1 & 0 & \cdots & 0 \\
   0 & \lambda_2 & \cdots & 0 \\
   \vdots & \vdots & \ddots & \vdots \\
   0 & 0 & \cdots & \lambda_n
   \end{bmatrix}
   \begin{bmatrix}
   u_1^H \\
   u_2^H \\
   \vdots \\
   u_n^H
   \end{bmatrix}
   $$
   
   其中 $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$。

4. **降维：**  
   若从 $D$ 维降到 $M$ 维，则选择最大的前 $M$ 个特征值对应的特征向量，构成投影矩阵：
   
   $$
   \Phi_{M \times D} \triangleq
   \begin{bmatrix}
   u_1^H \\
   u_2^H \\
   \vdots \\
   u_M^H
   \end{bmatrix}
   $$

---

核心思想：降维后，数据方差最大


上述过程等价于求解二次型的有约束极值问题：

$$
\begin{aligned}
&\text{证明：} \\
&\text{假设 } M=1, \\
&\quad Var(z_n) = E[(z_n - \overline{z_n})(z_n - \overline{z_n})^H] \\
&\quad = E\left[(\Phi_1^H x_n - \Phi_1^H \overline{x}_n)(x_n^H \Phi_1 - \overline{x_n^H} \Phi_1)\right] \\
&\quad = \Phi_1^H E\left[(x_n - \overline{x}_n)(x_n^H - \overline{x_n^H})\right] \Phi_1 \\
&\quad = \Phi_1^H C \Phi_1 \\
&\text{约束优化问题：} \\
&\quad \max_{\Phi_1} \Phi_1^H C \Phi_1 \\
&\quad \text{Subject to} \quad \Phi_1^H \Phi_1 = 1
\end{aligned}
$$

这个问题可以通过拉格朗日乘数法求解。构造拉格朗日函数：

$$
f(\Phi_1) \triangleq \Phi_1^H C \Phi_1 + \lambda (1 - \Phi_1^H \Phi_1)
$$

对 $f(\Phi_1)$ 关于 $\Phi_1$ 求导并令其为零：

$$
C \Phi_1 = \lambda \Phi_1
$$

即 $\Phi_1$ 是 $C$ 的一个特征向量。此时：

$$
f(\Phi_1) = \Phi_1^H C \Phi_1 = \lambda \Phi_1^H \Phi_1 = \lambda
$$

因此，取最大的特征值 $\lambda_1$ 时 $f(\Phi_1)$ 最大，此时 $\Phi_1$ 为最大特征值对应的特征向量 $\mathbf{u}_1$。

### 计算方法

[全网最快速的特征向量暴力求法（纯干货技巧）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT411E75Q/?spm_id_from=333.337.top_right_bar_window_history.content.click)

[相似对角化太难算，哈-凯定理怒斩A的n次方！（细节拉满了）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV11P411w716/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)


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



## SVD | 奇异值分解

如何对非方阵进行分解？



$$
A = [a_1 \quad a_2 \quad \cdots \quad a_n] \in \mathbb{R}^{m \times n}\\
A = U \Sigma V^H
$$


- $U^HU = UU^H = I$     左奇异向量
- $V^HV = VV^H = I$     右奇异向量
- $\Sigma$ 对角线上的元素是奇异值，不是方阵


### 性质


### 含义




变换 = 旋转和伸缩组合

那么如果想把一个变换表示成为旋转和伸缩的组合，考虑先旋转到坐标轴，再做伸缩，最后再旋转回来，这就是奇异值分解

1.奇异值为非负数
2.奇异值主对角线由小到大排列
3.奇异值是特征值开方

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112996076490296&bvid=BV1ExWxesEVf&cid=500001656999667&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

奇异值分解

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=652439242&bvid=BV1YY4y1U7UX&cid=1024031413&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>


作用：求解逆矩阵、伪逆矩阵

### 截断SVD

```
svd(Y,'econ')
```

econ: economic mode





### 计算方法

注意，奇异值的定义中就是大于0的

### 应用1 - 求伪逆矩阵


### 应用2 - 求范数

酉矩阵不改变向量的范数


### 应用3 - 图像降噪


### 应用4 - 数据压缩

截断SVD



最优逼近定理

需求: $P \leq r$, rank-P 矩阵 $\hat{Y}$,使得$Y$与$\hat{Y}$最接近

$$
\min_{\hat{Y}} ||Y - \hat{Y}||_F^2 \quad \text{or} \quad \min_{\hat{Y}} ||Y - \hat{Y}||_2^2
s.t. rank(\hat{Y})= P
$$

定理：

把截断SVD的前p个分量取出来


有效秩的确定（超参数调优的问题）

SNR较大的时候，使用拐点图

- 归一化奇异值方法
- 范数方法

SNR较低，贝叶斯低秩分解






## 张量CP分解

张量分解是矩阵分解的推广，矩阵是2阶张量，向量是1阶张量，标量是0阶张量







