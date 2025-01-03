# 07 | 降维
- dimensionality reduction tries to transform high-demensional data into a low-dimensioanl space while preserving the data structure.
- data might lie on low-dimensional manifolds.



![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241022172142.png)
维数诅咒

## MDS | Multiple dimensional Scaling


第一步——求解距离矩阵D

```python
def get_distance_matrix(data):
	expand_ = data[:, np.newaxis, :]
	repeat1 = np.repeat(expand_, data.shape[0], axis=1)
	repeat2 = np.swapaxes(repeat1, 0, 1)
	D = np.linalg.norm(repeat1 - repeat2, ord=2, axis=-1, keepdims=True).squeeze(-1)
	return D
```

第二步——求解内积矩阵B

```python
def get_matrix_B(D):
	assert D.shape[0] == D.shape[1]
	DD = np.square(D)
	sum_ = np.sum(DD, axis=1) / D.shape[0]
	Di = np.repeat(sum_[:, np.newaxis], D.shape[0], axis=1)
	Dj = np.repeat(sum_[np.newaxis, :], D.shape[0], axis=0)
	Dij = np.sum(DD) / ((D.shape[0])**2) * np.ones([D.shape[0], D.shape[0]])
	B = (Di + Dj - DD- Dij) / 2
	return B
```

第三步——求解Z矩阵

$B = Z^T Z$

```python
def MDS(data, n=2):
	D = get_distance_matrix(data)
	B = get_matrix_B(D)
	B_value, B_vector = np.linalg.eigh(B)
	Be_sort = np.argsort(-B_value)
	B_value = B_value[Be_sort]               # 降序排列的特征值
	B_vector = B_vector[:,Be_sort]           # 降序排列的特征值对应的特征向量
	Bez = np.diag(B_value[0:n])
	Bvz = B_vector[:, 0:n]
	Z = np.dot(np.sqrt(Bez), Bvz.T).T
	return Z
```
[多维缩放(MDS)算法的详细推导及Python实现\_多维缩放算法证明 知乎-CSDN博客](https://blog.csdn.net/weixin_38053887/article/details/104700192)
## PCA
[降维技巧 | 导论与流形学习：1/5 ](https://www.bilibili.com/video/BV1aF4m1u789)

第一阶段找了一个新的坐标系来表示数据，这个新的坐标系不是随便找的，是要求能最大限度的看出每个轴上的数据变化大小

第二阶段在新坐标系下取前k个变化最大的轴上的数据（最大特征值对应的轴），从而实现降维。

[一文让你彻底搞懂主成成分分析PCA的原理及代码实现(超详细推导)\_pca主成分分析图解释-CSDN博客](https://blog.csdn.net/MoreAction_/article/details/107463336)

[如何直观地理解「协方差矩阵」？](https://www.zhihu.com/tardis/zm/art/37609917?source_id=1005)

[【数据降维-第4篇】多维尺度变换（MDS）快速理解，及MATLAB实现 - 知乎](https://zhuanlan.zhihu.com/p/618906910)

[利用PCA降维的手工计算实例\_给定如下数据,采用pca计算降维时所用的特征向量-CSDN博客](https://blog.csdn.net/dugudaibo/article/details/78931825)
### kernel PCA
PCA 和SVD的关系：


SVD：

$$
A = US V^T
$$


U是特征向量，S是特征值，V是特征向量



协方差矩阵告诉我们变量的方差和联合方向


## 流形学习
### LLE
原始空间到子空间


## 度量学习

### 距离

欧式距离：在每个方向上同等重要；有缘千里来相会；无缘对面手难牵

马氏距离：

### NCA | Neighborhood Components Analysis