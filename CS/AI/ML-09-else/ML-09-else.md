# 其他
## 表征学习
y = Ax

完备正交基
- 固定基底：DCT、小波
- 数据驱动：PCA（主成分分析） EVD/SVD

过完备基
- 稀疏编码：K-SVD、OMP

提升模型表达能力：线性 to 非线性；确定性模型 to 统计模型


### 稀疏表示 | Sparse Representation

L1正则化，一般交叉位置在坐标轴上，可解释性增强


权重变稀疏，可以让可解释性变高

[Indian Buffet Process(印度自助餐过程)介绍-CSDN博客](https://blog.csdn.net/qy20115549/article/details/78532939)
自动学习哪些元可以去掉

高斯分布不适合建立稀疏模型

重尾分布：laplace、混合高斯

复杂信号，在某个基底的表示是稀疏的

### 压缩感知 | Compressive Sensing
解决问题：特定条件下突破奈奎斯特采样定理

$$
\min_{\alpha} \| y - A \Phi \alpha \|_2^2
$$

$$
\| \alpha \|_0 \leq k
$$

0范数：非零元素的个数

$\Phi \cdot A$ 满足RIP principle
$m \approx k \cdot c$ 线性 


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241017153420.png)

规则采样下，每个样本点仅包含局部信息；
随机采样下，每个样本点包含了全局信息。

