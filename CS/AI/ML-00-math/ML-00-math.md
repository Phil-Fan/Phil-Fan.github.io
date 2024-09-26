# 00 | Math in ML


## Linear algebra

矩阵：Matrix
向量：Vector
转置：Transpose
共轭：Conjugate
导数：Gradient
转置共轭：Hermitian
求逆：Inverse
线性组合：Linear Combination 

线性无关：Linear Independece 
奇异性：Singular 
向量空间：Vector Space
内积：inner product
外积：outer product
范数： norm

概率密度函数：probabiity density function (pdf)
累计分布函数： cumulative distribution function (cdf)
均值向量：mean vector 
相关矩阵：correlation matrix
协方差矩阵：covariance matrix
自相关：auto-correlation
互相关：cross-correlation
二次型 ： quadratic form
行列式：determinant
特征值： eigenvalue
迹：trace
秩：rank
求逆：inverse

相似对角化：
[全网最快速的特征向量暴力求法（纯干货技巧）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1aT411E75Q/?spm_id_from=333.337.top_right_bar_window_history.content.click)
[相似对角化太难算，哈-凯定理怒斩A的n次方！（细节拉满了）\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV11P411w716/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

!!! note "求解方法"
     **求特征值**：
    - 计算矩阵 \( A \) 的特征值 \(\lambda_i\)（\(i = 1, 2, \ldots, n\)），这些特征值将构成对角矩阵 \( \Lambda \) 的对角线元素。

    **求特征向量**：
    - 对于每个特征值 \(\lambda_i\)，求解特征向量 \( v_i \)，这些特征向量将构成矩阵 \( P \) 的列。

    **构造对角矩阵和特征向量矩阵**：
    - 对角矩阵 \( \Lambda \)：
        
        \[
        \Lambda = \begin{bmatrix}
        \lambda_1 & 0 & \cdots & 0 \\
        0 & \lambda_2 & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & \lambda_n
        \end{bmatrix}
        \]
        
    - 特征向量矩阵 \( P \)：
  
        \[
        P = \begin{bmatrix}
        | & | & & | \\
        v_1 & v_2 & \cdots & v_n \\
        | & | & & |
        \end{bmatrix}
        \]

    **验证对角化**：
    - 验证 \( A = P \Lambda P^{-1} \) 是否成立。



矩阵求逆引理：matrix inverse lemma
伪逆：pseudo inverse 
直和：direct sum
Hadamard积： Hadamard product 
Kronecker 积：Kronecker product 
稀疏：sparse 
压缩感知：compressive sensing 


Hermitian matrix
Permutation matrix
Communication matrix
Generalized permutation matrix 
Scale and permutation ambiguities 
Orthogonal matrix
Unitary matrix
Upper triangular matrix
Lower  triangular matrix 
LU decomposition 
Vandemonde matrix 
Similar matrix (with respect to eigenvalues/vectors -> the same determinant and trace)
### Vectors
#### Norm
[什么是范数（norm）？以及L1,L2范数的简单介绍\_l1 norm-CSDN博客](https://blog.csdn.net/qq_37466121/article/details/87855185)

#### Dot Product
#### rotate
#### Vector Projection

### 矩阵


#### determinant

#### trace

#### Rank

#### Tensors（todo）





#### inverse

#### Pseudo-Inverse（todo）



#### Matrix Norms

#### Hadamard product（todo）


### 矩阵分解
#### Eigen decomposition


#### SVD | Singular Value Decomposition（todo）


#### 矩阵求导


## Differential calculus
### Higher Order Derivatives

### Taylor Series

### Partial Derivatives


### Gradient

### Hessian Matrix

### Jacobian Matrix（todo）






## Probability
### Random variables
### Probability distributions
### Bayes’ Theorem（todo）

### 统计量
#### Expected Value
#### Variance
#### Covariance & Correlation

### Probability Distributions

## Information theory
### Entropy

### Kullback–Leibler Divergence（todo）

### Cross-entropy（todo）



## Optimization algorithms