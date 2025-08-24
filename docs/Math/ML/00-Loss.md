# Loss


损失为什么求平均：更好调学习率，相当于学习率之和梯度有关，和batch size没有关系

每次算梯度的时候要记得清零，不然会做累加


### l1 loss
不常用绝对差值而用平方损失：不好求导

有不平滑性，可能不稳定

离远点较远的时候，不一定希望有一个很大的梯度
### l2 loss


### Huber Robust loss

## softmax
- 不仅对硬分类感兴趣，还对软分类（概率）感兴趣

直接使用实数对应不太合适，所以使用向量来代表分类

### 为什么使用
- 线性有可能有负数，概率应该是非负的
- 概率之和需要为1

### 梯度推导
    
给定输入 $\mathbf{x} = [x_1, x_2, \dots, x_n]$，softmax 输出为：

$$
\hat{y}_i = g(\cdot)= \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}
\quad\text{for } i=1,\dots,n
$$


分两种情况讨论：

$$
\begin{aligned}
i = j \; \text{时}\qquad&
\frac{\partial \hat{y}_i}{\partial x_i}
= \frac{d}{d x_i} \left( \frac{e^{x_i}}{\sum_k e^{x_k}} \right)=\frac{e^{x_i}\sum_k e^{x_k}-e^{x_i}e^{x_i}}{(\sum_k e^{x_k})^2}
= \hat{y}_i \left(1 - \hat{y}_i\right)\\
i \ne j \; \text{时}\qquad&
\frac{\partial \hat{y}_i}{\partial x_j}
= \frac{d}{d x_j} \left( \frac{e^{x_i}}{\sum_k e^{x_k}} \right)=-\frac{e^{x_i}e^{x_j}}{(\sum_k e^{x_k})^2}
= - \hat{y}_i \hat{y}_j\\
\end{aligned}
$$

综上

$$
\boxed{
\frac{\partial \hat{y}_i}{\partial x_j} = \hat{y}_i (\delta_{ij} - \hat{y}_j)
}
$$

其中 $\delta_{ij}$ 是 Kronecker delta：$\delta_{ij} =
\begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \ne j
\end{cases}$

**写成矩阵形式（Jacobian）：**

记 softmax 输出为 $\mathbf{\hat{y}} = [\hat{y}_1, \dots, \hat{y}_n]^\top$，则：

$$
\boxed{
\mathbf{J}_{\text{softmax}} = \text{diag}(\mathbf{\hat{y}}) - \mathbf{\hat{y}} \mathbf{\hat{y}}^\top
}
$$

* $\text{diag}(\mathbf{\hat{y}})$ 是对角矩阵，对角线为 $\hat{y}_i$
* $\mathbf{\hat{y}} \mathbf{\hat{y}}^\top$ 是外积，得到一个 rank-1 矩阵

!!! note "梯度消失的推导"

    然后我们来看softmax的梯度。不妨简记softmax函数为 $g(\cdot)$，softmax得到的分布向量 $\hat{\mathbf{y}} = g(\mathbf{x})$ 对输入 $\mathbf{x}$ 的梯度为：

    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} = \text{diag}(\hat{\mathbf{y}}) - \hat{\mathbf{y}} \hat{\mathbf{y}}^\top \quad \in \mathbb{R}^{d \times d}
    $$

    把这个矩阵展开：

    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} = \begin{bmatrix}
    \hat{y}_1 & 0 & \cdots & 0 \\
    0 & \hat{y}_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \hat{y}_d
    \end{bmatrix} - \begin{bmatrix}
    \hat{y}_1^2 & \hat{y}_1 \hat{y}_2 & \cdots & \hat{y}_1 \hat{y}_d \\
    \hat{y}_2 \hat{y}_1 & \hat{y}_2^2 & \cdots & \hat{y}_2 \hat{y}_d \\
    \vdots & \vdots & \ddots & \vdots \\
    \hat{y}_d \hat{y}_1 & \hat{y}_d \hat{y}_2 & \cdots & \hat{y}_d^2
    \end{bmatrix}
    $$

    根据前面的讨论，当输入 $\mathbf{x}$ 的元素均较大时，softmax会把大部分概率分布分配给最大的元素，假设我们的输入数量级很大，最大的元素是 $x_1$，那么就将产生一个接近one-hot的向量 $\hat{\mathbf{y}} \approx [1, 0, \cdots, 0]^{\top}$，此时上面的矩阵变为如下形式：

    $$
    \frac{\partial g(\mathbf{x})}{\partial \mathbf{x}} \approx \begin{bmatrix}
    1 & 0 & \cdots & 0 \\
    0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & 0
    \end{bmatrix} - \begin{bmatrix}
    1 & 0 & \cdots & 0 \\
    0 & 0 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & 0
    \end{bmatrix} = \mathbf{0}
    $$

    也就是说，在输入的数量级很大时，梯度消失为0，造成参数更新困难。


### 交叉熵



信息论：

信息量 ： 不确定-》确定的难度

可以理解为惊异程度，不确定度更大，则信息量更大

系统的熵

$$
H[P] = \sum_j - P(j) \log P(j).
$$



$$
H(P):=E(P_f)\\
=\sum_{i=1}^mp_i\cdot f(p_i)=\sum_{i=1}^mp_i(-\log_2p_i)=-\sum_{i=1}^mp_i\cdot\log_2p_i
$$


### 交叉熵 + softmax 的梯度推导





* softmax 函数记为：

$$
g(\mathbf{x}) = \left[\frac{e^{x_1}}{\sum_k e^{x_k}}, \dots, \frac{e^{x_n}}{\sum_k e^{x_k}} \right]^\top = \hat{\mathbf{y}}
$$

$$
\frac{\partial \hat{y}_i}{\partial x_j} = \hat{y}_i (\delta_{ij} - \hat{y}_j)\qquad \delta_{ij} =
\begin{cases}
1 & \text{if } i = j \\
0 & \text{if } i \ne j
\end{cases}
$$

* 交叉熵损失函数定义为：

$$
\mathcal{L}(\hat{\mathbf{y}}, \mathbf{y}) = -\sum_{i=1}^n y_i \log \hat{y}_i
$$

$$
\frac{\partial \mathcal{L}}{\partial \hat{\mathbf{y}}} = \left( -\frac{y_i}{\hat{y}_i} \right)
$$

* 整体函数组合为：

$$
\boxed{y = \mathcal{L}(g(\mathbf{x}))}
$$






根据链式法则：

$$
\begin{aligned}
\frac{\partial y}{\partial x_j}  &=  \sum_i \frac{\partial \mathcal{L}}{\partial \hat{y}_i} \cdot \frac{\partial \hat{y}_i}{\partial x_j}\\
&= \sum_i \left( -\frac{y_i}{\hat{y}_i} \right) \cdot \left( \hat{y}_i (\delta_{ij} - \hat{y}_j) \right)\\
&= \sum_i \left( -y_i (\delta_{ij} - \hat{y}_j) \right)\\
&= -y_j + \hat{y}_j
\end{aligned}
$$

即

$$
\frac{\partial \mathcal{L}(g(\mathbf{x}))}{\partial x_j} = \hat{y}_j - y_j
$$

写成矩阵形式

$$
\boxed{
\nabla_{\mathbf{x}} \mathcal{L}(g(\mathbf{x})) = \hat{\mathbf{y}} - \mathbf{y}
}
$$



### KL散度

交叉熵

衡量两个概率的区别

我们可以把交叉熵想象为“主观概率为$Q$的观察者在看到根据概率$P$生成的数据时的预期惊异”。 

（i）最大化观测数据的似然；
（ii）最小化传达标签所需的惊异。

