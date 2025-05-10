# 02 | 无约束 解析解法



## 单变量问题定义

严格局部极小点：

- 必要条件：
- 充分条件：$\nabla f(X^*)=0$ 且$\mathbf{H(f)}$正定


## 向量变元问题定义


## 矩阵变元问题定义



 

## 平稳点

### local minimum

### local maximum

### saddle point


#### **驻点**：

$\nabla f\left(x^{*}\right)=\left[\frac{\partial f(x)}{\partial x}\right]_{x=x^{*}}^{T}=0$



!!! note "方向导数是一个数，梯度是一个向量"

#### **方向导数**

方向导数是函数在某一特定方向上的变化率。它表示函数在定义域内某一点沿着给定方向的变化趋势。具体来说，对于一个具有定义域的函数 $f(x, y)$，在点 $(x_0, y_0)$ 处沿着方向向量 

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

对于一个二元函数 $f(x, y)$，它的黑塞矩阵是一个 2x2 的矩阵，由函数的二阶偏导数组成。黑塞矩阵的一般形式为：

$$
H = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix}
$$

由于二阶偏导数具有对称性，即 $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$，所以黑塞矩阵是一个对称矩阵。因此，我们可以将黑塞矩阵简化为：

$$
H = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial x \partial y} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix}
$$



## 最优性条件
### 实数域

一阶必要条件：（局部极小值/局部极大值）：$\nabla f(x^*)=0$

二阶必要条件：（局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)\geq 0$

二阶充分条件：（严格局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)>0$

### 复数域





## 案例 - 最小二乘

!!! note "观测出模型的假设非常关键，给人判定模型好坏的一个直观的方法"

最小二乘和最大似然在高斯噪声的假设下是等价的。

conditional pdf 对b

likelihood function 对z


建模假设：模型的预测能力是比较好的，没有outlier（超出$3\sigma$的离群值），比如上课一次不来，作业一次不交，考试考100分。
