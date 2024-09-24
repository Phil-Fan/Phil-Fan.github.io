# 04 | SVM 支持向量机


SVM：optimize the margin
在所有0 error的情况下，选择最大的margin, 使得模型更加鲁棒

non-linear SVM: kernel trick

$\Phi: x \rightarrow \phi(x)$


对抗样本攻击：增加鲁棒性，减少泛化性


计算每个点到决策边界的距离$\gamma$

- Maximum Margin Classifier:数据集最小的margin
目的就是要找到一个决策边界，使得margin最大

为什么使用这种方法
- 裕度更高，容错性更好
- 如果margin越大，对于噪声的容忍度越高

## 核函数

## 求解
### 对偶问题
### KKT条件
### SMO算法

### 替代损失函数
loss+正则化项
constrain:
## 回归


## 图模型

