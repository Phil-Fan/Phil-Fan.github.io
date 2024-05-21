# 规划论 | 凸优化

## 概念

半平面的交点一定是凸集，



![image-20240521163820391](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521163820391.png)

![image-20240521164034690](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521164034690.png)

凸优化：函数是凸函数，可行域是凸集；凹函数求最大值其实是一样的，加一个负号就可以了

## 数学模型

$$
\min f(x) \\
\text { s.t. }\left\{

\begin{array}{c}
  \quad h_{i}(x)=0 \quad i=1,2, \ldots, m \\
g_{j}(x) \geq 0 \quad j=1,2, \ldots, l \\
x \in R^{n}
\end{array}
\right.
$$



以求最小值为标准问题

![image-20240521100601777](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521100601777.png)

## 解析解法：

### 无约束：

严格局部极小点：

- 必要条件：
- 充分条件：$\nabla f(X^*)=0$ 且$\mathbf{H(f)}$正定



#### **驻点**：

$\nabla f\left(x^{*}\right)=\left[\frac{\partial f(x)}{\partial x}\right]_{x=x^{*}}^{T}=0$



!!! note "方向导数是一个数，梯度是一个向量"

#### **方向导数**

方向导数是函数在某一特定方向上的变化率。它表示函数在定义域内某一点沿着给定方向的变化趋势。具体来说，对于一个具有定义域的函数 $f(x, y)$，在点 $(x_0, y_0)$ 处沿着方向向量 $\vec{u} = (u_1, u_2)$ 的方向导数被定义为：

$$
D_{\vec{u}}f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + hu_1, y_0 + hu_2) - f(x_0, y_0)}{h}
$$

其中，$h$ 是一个很小的正数，$u_1$ 和 $u_2$ 是方向向量 $\vec{u}$ 的分量。





#### **梯度**：

具有连续偏导→可微→**有切平面**→切线都在切平面上→有一个斜率最大的

$$
\nabla f(x)=\left[\begin{array}{c}
\frac{\partial f(x)}{\partial x_{1}} \\
\frac{\partial f(x)}{\partial x_{2}} \\
\vdots \\
\frac{\partial f(x)}{\partial x_{n}}
\end{array}\right]
$$



梯度的几何性质

- $\nabla f(x)$ 为目标函数 $f(x)$ 等值面在 $x$ 的法向量。
- $\nabla f(x)$ 是目标函数值 $f(x)$ 在 $x$ 点增长最快的方向。



#### **雅可比矩阵（Jacobian matrix）**

它的重要性在于它体现了一个可微方程与给出点的最优线性逼近，因此，雅可比矩阵类似于多元函数的导数
$$
J(\mathbf{f}) = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$





#### **黑塞矩阵 Hessian Matrix 二阶导数矩阵**

$$
\mathbf{H(f)} = \nabla^{2} f(x)=\left[\begin{array}{cccc}
\frac{\partial^{2} f(x)}{\partial x_{1}^{2}} & \frac{\partial^{2} f(x)}{\partial x_{1} \partial x_{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{1} \partial x_{n}} \\
\frac{\partial^{2} f(x)}{\partial x_{2} \partial x_{1}} & \frac{\partial^{2} f(x)}{\partial x_{2}^{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{2} \partial x_{n}} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^{2} f(x)}{\partial x_{n} \partial x_{1}} & \frac{\partial^{2} f(x)}{\partial x_{n} \partial x_{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{n}^{2}}
\end{array}\right]
$$



二次型理论

- $\mathbf{H(f)}$负定，有极大值： 奇数阶主子式为负数，偶数阶为正数
- $\mathbf{H(f)}$正定，有极小值：顺序主子式都为正数
- $\mathbf{H(f)}$不定，鞍点：特征值有正有负
- $\mathbf{H(f)}$不可逆，无法判断：特征值有0

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/b05544056c037bc56f9070e45533f02.jpg" alt="b05544056c037bc56f9070e45533f02" style="zoom: 33%;" />



无约束极小值问题的最优性条件

一阶必要条件：（局部极小值/局部极大值）：$\nabla f(x^*)=0$

二阶必要条件：（局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)\geq 0$

二阶充分条件：（严格局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)>0$



### 有约束

等式约束
$$
\begin{array}{ll} 
\min & f(x) \\ 
\text{s.t.} & h_i(x) = 0, \quad i = 1, 2, ..., m \\ 
& x \in \mathbb{R}^n 
\end{array}
$$

等式约束的向量形式
$$
\begin{array}{ll} 
\min & f(x) \\ 
\text{s.t.} & h(x) = 0 \\ 
& x \in \mathbb{R}^n 
\end{array}
$$

其中，$h(x) = \begin{bmatrix} h_1(x) \\ h_2(x) \\ \vdots \\ h_m(x) \end{bmatrix}$。



#### 拉格朗日函数

$$
L(x, \lambda) = f(x) + \lambda^T h(x) = f(x) + \sum_{i=1}^m \lambda_i h_i(x)
$$

其中，$\lambda = [\lambda_1, \lambda_2, ..., \lambda_m]^T$。



对$L(x, \lambda)$求偏导数，令偏导数为0：

$$
\frac{\partial L(x, \lambda)}{\partial x} \Big|_{x^*} = 0 \quad \Rightarrow \quad \nabla f(x^*) + \sum_{i=1}^m \lambda_i \nabla h_i(x^*) = 0
$$

$$
\frac{\partial L(x, \lambda)}{\partial \lambda} \Big|_{x^*} = 0 \quad \Rightarrow \quad h_i(x^*) = 0, \quad i = 1, 2, ..., m
$$



<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521160859915.png" alt="image-20240521160859915" style="zoom:50%;" />

只有在相切的时候，可行域的切线和梯度才能在同一方向，相加才可能为0











不等式约束
$$
\begin{array}{ll} 
\min & f(x) \\ 
\text{s.t.} & g_i(x) \geq 0, \quad i = 1, 2, ..., m \\ 
& x \in \mathbb{R}^n 
\end{array}
$$



目标函数减小的充分条件

约束$g(x) = 0$强约束





#### **可行方向判别条件（充分条件）**

对于点$x^{(0)}$，若满足以下条件，则$p$是$x^{(0)}$的可行方向：

$$
\nabla g_j(x^{(0)})^T p \geq 0, \quad \forall j \in J(x^{(0)})
$$

其中，$J(x^{(0)}) = \{j \mid g_j(x^{(0)}) = 0, j = 1, 2, ..., l\}$为起作用约束集合。

证明：根据Taylor公式，有

$$
g_j(x^{(0)} + \lambda p) = g_j(x^{(0)}) + \lambda \nabla g_j(x^{(0)})^T p + O(\lambda)
$$

当$\lambda$足够小时，如果$j \in J(x^{(0)})$，假设$g_j(x)$连续，有

$$
g_j(x^{(0)} + \lambda p) \geq 0
$$

如果$j \in J(x^{(0)})$，当$\nabla g_j(x^{(0)})^T p > 0$时，也有

$$
g_j(x^{(0)} + \lambda p) \geq 0
$$

几何含义：与所有起作用约束梯度的夹角小于$90^\circ$的方向。

**局部极小值存在的直观条件**

在点$x^*$处，不存在同时满足下面两类不等式的方向：

$$
\nabla f(x^*)^T p < 0
$$

$$
\nabla g_j(x^*)^T p > 0, \quad j \in J(x^*)
$$

其中，$J(x^*)$为起作用约束集合。

几何含义：不存在与$\nabla f(x^*)$和所有的$\nabla g_{j \in J(x^*)}$均成锐角的方向。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521153533251.png" alt="有行下降方向" style="zoom:50%;" />

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521153609542.png" alt="无可行下降方向" style="zoom:50%;" />



#### **Gordan引理**

设$B \in R^{m\times n}$，则下列两个系统有且仅有一个有解：<br>
(I) $Bx < 0$<br>
(II) $B^T y = 0, y \ge 0, y \ne 0$<br>

> 参考网址：[运筹说 第99期 | 非线性规划—最优性条件 ](https://zhuanlan.zhihu.com/p/677937880)<br>[凸集分离定理中的 Gordan 定理有什么几何意义，或者怎么用数形结合方法解释？](https://www.zhihu.com/question/374628766)<br>[“拉格朗日对偶问题”如何直观理解？“KKT条件” “Slater条件” “凸优化”打包理解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1HP4y1Y79e/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

翻译一下：<br>
$B^T$是$R^n$中一组基，由$m$个$n$维列向量组成，只存在两种情况：<br>

1. 存在一个方向，与$B^T$中所有向量都呈钝角<br>
2. $B^T$这组基的非负、非零线性组合可以得到原点<br>
    换句话说，**如果一组基的非负组合是一个凸锥，则等价为这组基的正组合表示不了原点，除非系数都是0。即$b_j$不可能分布在任何超平面的同一侧**<br>

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-995890416cc10e852566f5ff1a292f68_1440w.webp" alt="img" style="zoom:50%;" />

正线性相关（positive linear dependence）

几何含义：$a_j$不可能分布在任何超平面的同一侧

正线性相关$\Rightarrow$线性相关



#### **Fritz John定理**

设$X^*$是非线性规划的局部最优点，函数$f(x)$和$g_j(x)(j=1,2,...,l)$在点$X^*$有连续一阶偏导，则必然存在不全为零的数$\mu_0, \mu_1, \mu_2, ..., \mu_l$，使

$$
\begin{align}
\mu_0 \nabla f(X^*) - \sum_{j=1}^l \mu_j \nabla g_j(X^*) = 0 \quad &Lagrange函数驻点条件\\
\mu_j g_j(X^*) = 0 \quad (j=1,2,...,l) \quad &互补松弛条件\\
\mu_0 \ge 0, \mu_j \ge 0 \quad (j=1,2,...,l) \quad &强非负条件
\end{align}
$$

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521161306273.png" alt="image-20240521161306273" style="zoom:50%;" />

> 红线上的梯度，在$\lambda_i > 0$的情况下是不可能和目标函数相抵消的，所以只能是$\lambda_i =0$（松弛的约束条件），然后让$x^*$处的约束条件（紧致的约束条件）线性组合为负梯度

* Fritz John条件是由Gordan引理矩阵展开得到。Gordan引理只对起作用约束做了说明，Fritz John定理采用互补松弛条件将起作用约束引入，取对应参数为0改良得到。
* 判断一个点是不是Fritz John点的步骤就是找到对应的函数梯度，带入公式看是否能找到不全为零的数使得方程成立。
* 如果$\mu_j=0$，$pf_j(x)$就从Fritz John条件中消去，说明在所讨论的点$X^*$处，起作用约束的梯度线性相关，即该点Fritz John条件失效，因此需要对讨论点处起作用约束的梯度附加上线性无关的约束条件，保证$\mu_j>0$，这样就引出了库恩-塔克条件。



**原问题**
$$
\begin{aligned}
\min_x \ & f_0(x), x \in \mathbb{R}^n \\
\text{s.t.} \quad & f_i(x) \le 0, \text{其中} i=1,2,3...m \\
& h_i(x) = 0, \text{其中} i=1,2,3...q
\end{aligned}
$$

**等价问题**
$$
\begin{aligned}


\min_x \ \max_{\lambda, \nu} \ & L(x, \lambda, \nu)
= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^q \nu_i h_i(x) \\

\text{s.t.} \quad & \lambda_i \ge 0 \\
\end{aligned}
$$


等价性的证明
$$
x \text{在可行域内} \\
\left\{
\begin{array}{**lr**}
 \lambda_i f_i(x) = 0 \quad \text{或} \lambda_i = 0 \quad\text{或} f_i(x) = 0 \\
\nu_i h_i(x) = 0 \quad\text{或} \nu_i = 0 \quad\text{或} h_i(x) = 0
\end{array}
\right.
$$

* 当$x$在可行域内时，$\max_{\lambda, \nu} L(x, \lambda, \nu) = f_0(x) + 0 + 0 = f_0(x)$
* 当$x$不在可行域内时，$\max_{\lambda, \nu} L(x, \lambda, \nu) = f_0(x) + \infty + \infty = \infty$

因此，$\min \limits_x \max \limits_{\lambda, \nu} L(x, \lambda, \nu) = \min \limits_x f_0(x)$



**对偶问题**
$$
\begin{aligned}
&\max \limits_{\lambda,v} g(\mathbf{\lambda},\mathbf{v}) =  \max \limits_{\lambda,v} \ \min \limits_x \ L(x,\mathbf{\lambda},\mathbf{v})\\
&\text{s.t.} 
\left\{
    \begin{array}{**lr**}
    
        \nabla_x \ L(x,\mathbf{\lambda},\mathbf{v}) = 0\\
        \lambda \geq0
    \end{array}
\right.
\end{aligned}
$$
![image-20240521165037244](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240521165037244.png)

!!! note "无论原问题是什么问题，对偶问题都是凸问题"











## 数值解法

包括基于梯度的数值解法，如最速下降法、牛顿法、拟牛顿法等，以及有约束极值问题的数值解法，如可行方向法、制约函数法等。