# 03 | 无约束 数值解法

> [梯度下降法、牛顿法和拟牛顿法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/37524275)


<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521193045743.png" alt="image-20240521193045743" style="zoom:50%;" />


有三个核心的点需要考虑：

- 迭代方向
- 步长
- 终止条件

## 初始点

- 全0
- 全随机
- 


## 迭代方向

### 一阶 - GD - 迭代初期

下降最快的方向是负梯度方向

性质：最优步长的时候 $\nabla f(x^{k+1}) \perp \nabla f(x^{(k)})$

优点：计算量小，适用于迭代初期

缺点：之字形的迭代路径，接近极值点的时候更严重

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-dd6ce242d10f41e2f20e15dfce22cd52_720w.webp)



!!! note "注意"
	梯度下降不一定能够找到全局的最优解，有可能是一个局部最优解。当然，如果损失函数是凸函数，梯度下降法得到的解就一定是全局最优解。



梯度下降算法：

输入：目标函数 $f(x)$ ，梯度函数 $g(x)=\nabla f(x)$ ，计算精度 $\varepsilon$

输出： $f(x)$ 的极小点 $x^*$

1. 取初值 $x^{(0)} \in R^n$ ，置 $k=0$
2. 计算 $f\left(x^{(k)}\right)$
3. 计算梯度 $g_{k}=g\left(x^{(k)}\right)$ ，当 $\left\|g_{k}\right\|<\varepsilon$ 时，停止迭代，令 $x^{*}=x^{(k)}$ ；否则，令

$$
\boldsymbol{p}_{k}=-\boldsymbol{g}\left(\boldsymbol{x}^{(k)}\right), \text { 求 } \lambda_{k} \text { ，使 }
$$

$$
f\left(\boldsymbol{x}^{(k)}+\lambda_{k} \boldsymbol{p}_{k}\right)=\min _{\lambda \geq 0} f\left(\boldsymbol{x}^{(k)}+\lambda \boldsymbol{p}_{k}\right)
$$

4. 置 $x^{(k+1)}=x^{(k)}+\lambda_{k} p_{k}$ ，计算 $f\left(x^{(k+1)}\right)$
5. 若 $\left|f\left(x^{(k+1)}\right)-f\left(x^{(k)}\right)\right|<\varepsilon$ 或 $\left\|x^{(k+1)}-x^{(k)}\right\|<\varepsilon$ 时，停止迭代，令 $x^{*}=x^{k+1}$
6. 否则，置 $k=k+1$ ，转3。



!!! note "极小值附近的等值面是椭球面"

$X^T \cdot \mathbf{H} \cdot X = c$

- 如果$\mathbf{H}$是对角矩阵，则显然是椭圆
- 如果不是的话，相似对角化以后$X^TM^T \ \Lambda\mathbf{}\ M X = c$


### improve GD


problem with GD
- Slow at plateaus
- get stuck at saddle points
#### Mini-batch Gradient Descent


#### Stochastic Gradient Descent | 随机梯度下降
Although this method is very fast, it may cause significant fluctuations in the loss function

#### Momentum
Gradient descent with momentum uses the momentum of the
gradient for parameter optimization

Movement = Negative of Gradient + Momentum
[优化算法之Gradient descent with momentum - 知乎](https://zhuanlan.zhihu.com/p/34240246)

#### Nesterov Accelerated Momentum
[比Momentum更快：揭开Nesterov Accelerated Gradient的真面目 - 知乎](https://zhuanlan.zhihu.com/p/22810533)

#### Adam | Adaptive Moment Estimation





### 二阶 - 牛顿法 - 极值点附近

* 设计思想：近似为二次问题。

$$
\begin{align}
f(x) \approx f\left(x^{(k)}\right)+\nabla f\left(x^{(k)}\right)^{T}\left(x-x^{(k)}\right)+\frac{1}{2}\left(x-x^{(k)}\right)^{T} \nabla^{2} f\left(x^{(k)}\right)\left(x-x^{(k)}\right) 
\end{align}
$$



函数$f(x)$有极值的必要条件是在极值点处一阶导数为0，即梯度向量为0。特别的当$H(x^{(k)})$是正定矩阵时，函数$f(x(k))$的极值为极小值。

我们为了得到一阶导数为0的点，可以用到牛顿法求解方程方法。根据二阶泰勒展开，对 ∇𝑓(𝑥) 在 𝑥(𝑘) 进行展开得（也可以对上述泰勒公式再进行求导）

$\nabla f(x) \approx g_k+H_k\left(x-x^{(k)}\right) \approx 0$


$$
\begin{align}
迭代公式  \Longrightarrow x^{(k+1)} \approx x^{(k)}-H_k^{-1} g_k\\
迭代方向  \Longrightarrow p^{(k)}=-H_k^{-1} g_k \quad 牛顿方向 \\
其中，g_k = g(x{(k)} = \nabla f\left(x^{(k)}\right)\\
\end{align}
$$

优点：极值点附近收敛速率快。

A缺点：计算量大，需要求二阶导数和Hessian矩阵逆。

远离极值点时，不一定是下降方向，需采用进一步修正。



!!! note "为什么收敛快"
	至于为什么牛顿法收敛更快，通俗来说梯度下降法每次只从你当前所处位置选一个坡度最大的方向走一步，牛顿法在选择方向时，不仅会考虑坡度是否够大，还会考虑你走了一步之后，坡度是否会变得更大。所以，可以说牛顿法比梯度下降法看得更远一点，能更快地走到最底部。





* 设$A$为对称矩阵，二次函数 $f(x)=\frac{1}{2} x^T A x+b^T x+c$
* 驻点方程: $\nabla f(x)=Ax+b=0$
	+ 有解: $\text{rank} A=\text{rank}[A \quad b]$
	+ 无解: $\text{rank} A \neq \text{rank}[A \quad b]$
* Hessian矩阵: $\nabla^2 f(x)=A$​



例: 抛物面

* (1) $A>0$ 椭球面: $x^*=A^{-1} b$ 唯一极小点
* (2) $A \geq 0 \quad \& \quad \text{rank} A<n$ 椭球柱面/平行超平面:无穷多个极小点
* (3) $A \leq 0$ (降维) 椭球面: 无界解（极大点）
* (4) $A$ 不定 (高维) 马鞍面: $f(x)=x_1^2-x_2^2$ 无界解（鞍点解）


### 修正牛顿法 - 解决数值稳定性问题
**Levenberg-Marquardt修正**

* 设计思想: 将 $\nabla^2 f\left(x^{(k)}\right)$ 变为正定矩阵, 保证$p$是下降方向
* L-M修正方向: $p^{(k)}=-\left[\nabla^2 f\left(x^{(k)}\right)+\mu_{k} I\right]^{-1} \nabla f\left(x^{(k)}\right)$
* $x^{(k+1)}=x^{(k)}-\left[\nabla^2 f\left(x^{(k)}\right)+\mu_{k} I\right]^{-1} \nabla f\left(x^{(k)}\right)$
* $\mu_{k}>\left|\lambda_{\text {min }}\right| \quad \lambda_{\text {min }} \text { 为 } \nabla^2 f\left(x^{(k)}\right) \text { 最小负特征值 }$
* $\mu \rightarrow 0$ : 牛顿法
* $\mu \rightarrow \infty$ : 最速下降法
* 如果不求特征值，可以从较小的 $\mu$ 值试探



### 二阶 - 拟牛顿法

在牛顿法的迭代中，需要计算海森矩阵的逆矩阵 $\boldsymbol{H}^{-1}$ ，这一计算比较复杂，考虑用一个 $n$ 阶矩阵 $\boldsymbol{G}_{k}=\boldsymbol{G}\left(x^{(k)}\right)$ 来近似代替 $\boldsymbol{H}_{k}^{-1}=\boldsymbol{H}^{-1}\left(x^{(k)}\right)$ 。这就是拟牛顿法的基本想法。

要找到近似的替代矩阵，必定要和 $\boldsymbol{H}_{k}$ 有类似的性质。先看下牛顿法迭代中海森矩阵 $\boldsymbol{H}_{k}$ 满足的条件。首先 $\boldsymbol{H}_{k}$ 满足以下关系：

在$x^{k+1}$处进行展开

$$
\nabla f(x)=g_{k+1}+\boldsymbol{H}_{k+1}\left(x-x^{(k+1)}\right)
$$

 将$\boldsymbol{x}=\boldsymbol{x}^{k}$代入

$$
g_{k}-g_{k+1}=\boldsymbol{H}_{k+1}\left(x^{(k)}-x^{(k+1)}\right)
$$

记 $y_{k}=g_{k+1}-g_{k}, \delta_{k}=x^{(k+1)}-x^{k}$ ，则

$$
\begin{aligned}
y_{k} & =\boldsymbol{H}_{k+1} \delta_{k} \\
\delta_{k}& = \boldsymbol{H}_{k+1}^{-1} y_{k} \quad 拟牛顿条件(Secant\ equation)
\end{aligned}
$$



其次，如果 $H_k$ 是正定的（$H_k^{-1}$ 也是正定的），那么保证牛顿法的搜索方向 $p_k$ 是下降方向。这是因为搜索方向是 $p_k = -H_k^{-1}g_k$。

由

$$
x^{(k+1)} = x^{(k)} - H_k^{-1}g_k
$$

有

$$
x = x^{(k)} - \lambda H_k^{-1}g_k = x^{(k)} + \lambda p_k
$$

则 $f(x)$ 在 $x^{(k)}$ 的泰勒展开可近似为

$$
\begin{align}
f(x) = f\left(x^{(k)}\right) - \lambda g_k^T H_k^{-1} g_k
\end{align}
$$

由于 $H_k^{-1}$ 正定，故 $g_k^T H_k^{-1} g_k > 0$。当 $\lambda$ 为一个充分小的正数时，有 $f(x) < f\left(x^{(k)}\right)$，即搜索方向 $p_k$ 是下降方向。

因此拟牛顿法将 $G_k$ 作为 $H_k^{-1}$ 近似。要求 $G_k$ 满足同样的条件下，首先，每次迭代矩阵 $G_k$ 是正定时，$G_k$ 满足下面的拟牛顿条件：

$$
\begin{align}
G_{k+1} y_k = \delta_k
\end{align}
$$

按照拟牛顿条件，在每次迭代中可以选择更新矩阵 $G_{k+1}$​：

$$
\begin{align}
G_{k+1} = G_k + \Delta G_k
\end{align}
$$


### DFP算法

在DFP（Davidon-Fletcher-Powell）算法中，我们选择 $G_k$ 作为 $H_k^{-1}$ 的近似。假设在每次迭代中，矩阵 $G_{k+1}$ 由 $G_k$ 加上两个附加项构成：

$$
G_{k+1} = G_k + P_k + Q_k
$$

其中，$P_k$ 和 $Q_k$ 是待定矩阵。那么，

$$
G_{k+1}y_k = G_k y_k + P_k y_k + Q_k y_k
$$

为了使 $G_{k+1}$ 满足拟牛顿条件，我们希望 $P_k$ 和 $Q_k$ 满足以下条件：

$$
\begin{aligned}
&P_k y_k = \delta_k \\
&Q_k y_k = -G_k y_k
\end{aligned}
$$

因此，我们可以这样选择：

$$
\begin{aligned}
&P_k = \frac{\delta_k \delta_k^T}{\delta_k^T y_k} \\
&Q_k = -\frac{\delta_k y_k^T G_k}{y_k^T G_k y_k}
\end{aligned}
$$

这将导致矩阵 $G_{k+1}$ 的迭代公式为：

$$
G_{k+1} = G_k + \frac{\delta_k \delta_k^T}{\delta_k^T y_k} - \frac{\delta_k y_k^T G_k}{y_k^T G_k y_k}
$$

如果初始矩阵 $G_0$ 是正定的，那么可以证明在迭代过程中每个矩阵 $G_k$ 也都是正定的。



可以证明: 

- 当目标函数为严格凸二次函数时, 可经有限步迭代收敛于极值（二次终止性）。为什么不是1步?





### 共轭梯度法

> 参考文献：[共轭梯度法的简单直观理解-CSDN博客](https://blog.csdn.net/weixin_43940314/article/details/121125847)

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/4cb1ad1b7f5d4100b19e51a63eddedee.png)

为什么会走出这一Z形线呢？因为梯度下降的方向恰好与f垂直，也就是说和等高线垂直。沿着垂直于等高线的方向，一定能让函数减小，也就是最快地下了一个台阶。但是最快下台阶并不意味着最快到达目标位置（即最优解），因为你最终的目标并不是直对着台阶的。

为了修正这一路线，采用另一个方向：即共轭向量的方向。

对照梯度下降法，每次向下走的方向不是梯度了，而是专门的一个方向$\vec{d}$除此之外和梯度下降法几乎一样。


共轭向量$p_i^T A p_j = 0$,其中A是一个对称正定矩阵。$p_i,p_j$ 是一对共轭的向量。

可见，共轭是正交的推广化，因为向量正交的定义为：$p_i^T\cdot p_j = 0$

共轭比正交中间只多了个矩阵A，而矩阵的几何意义正是对一个向量进行线性变换（可见Gilber Strang的线代公开课）。因此共轭向量的意思就是一个向量经过线性变换（缩放剪切和旋转）之后与另一个向量正交。
<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/2b29249d0e29462dae65e18e1e2b25b7.png" alt="在这里插入图片描述" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240528092452183.png" alt="image-20240528092452183" style="zoom:50%;" />

## 步长选择

设计思想：沿搜索方向的目标函数值最小

$\lambda_{k}=\arg \min \limits_{\lambda} f\left(\boldsymbol{x}^{(k)}+\lambda \boldsymbol{p}^{(k)}\right)$



### 分数法

![image-20240528081701243](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240528081701243.png)





### 斐波那契法

![image-20240528081631391](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240528081631391.png)

### 0.618法

![image-20240528081607566](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240528081607566.png)


### Armijo准则

- backtracking line search

- goldstein准则 找一个步长点上下限

- diminishing rule
一定能保证收敛，只不过可能慢一点，用于测试模型的性能



## 迭代终止准则 Terminate

- 绝对误差准则

$$
\left\|\boldsymbol{x}^{(k+1)}-\boldsymbol{x}^{(k)}\right\| \leq \varepsilon_{1} \quad\left|f\left(\boldsymbol{x}^{(k+1)}\right)-f\left(\boldsymbol{x}^{(k)}\right)\right| \leq \varepsilon_{2}
$$

- 相对误差准则

$$
\frac{\left\|\boldsymbol{x}^{(k+1)}-\boldsymbol{x}^{(k)}\right\|}{\left\|\boldsymbol{x}^{(k)}\right\|} \leq \varepsilon_{3} \quad \frac{\left|f\left(\boldsymbol{x}^{(k+1)}\right)-f\left(\boldsymbol{x}^{(k)}\right)\right|}{\left|f\left(\boldsymbol{x}^{(k)}\right)\right|} \leq \varepsilon_{4}
$$

梯度模准则（first-order optimality measure）

$$
\begin{align}
\left\|\nabla f\left(\boldsymbol{x}^{(k)}\right)\right\| \leq \varepsilon_{5} \quad\left\|\nabla f\left(\boldsymbol{x}^{(0)}\right)\right\|
\end{align}
$$


