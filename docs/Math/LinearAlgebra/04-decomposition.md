# 04 | 矩阵分解


## LDU decomposition
- L: lower triangular matrix
- D: diagonal matrix
- U: upper triangular matrix


```matlab
A = [1 2 3; 4 5 6; 7 8 9];
[L, D, U] = ldu(A);
```






## 相似对角化
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



## Eigen Value Decomposition | 特征分解

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

$$
A = U \Lambda U^{-1}
$$





## SVD | 奇异值分解

变换 = 旋转和伸缩组合

那么如果想把一个变换表示成为旋转和伸缩的组合，考虑先旋转到坐标轴，再做伸缩，最后再旋转回来，这就是奇异值分解

1.奇异值为非负数
2.奇异值主对角线由小到大排列
3.奇异值是特征值开方

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112996076490296&bvid=BV1ExWxesEVf&cid=500001656999667&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

奇异值分解

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=652439242&bvid=BV1YY4y1U7UX&cid=1024031413&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

## 张量CP分解

张量分解是矩阵分解的推广，矩阵是2阶张量，向量是1阶张量，标量是0阶张量







