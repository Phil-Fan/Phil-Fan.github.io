# 02 | 无约束 解析解法



## 单变量问题定义
### 邻域
开邻域：

$$
B_o(c;r)=\{x\mid x\in\mathcal{D}, |x-c|<r\}
$$

闭邻域：

$$
B_o(c;r)=\{x\mid x\in\mathcal{D}, |x-c|\leq r\}
$$


### 极值点

**全局极小点**：对于定义域内的所有点，都满足：

$$
f(x^*) \leq f(x), \forall x\in D, x\neq x^*
$$

**严格全局极小点**：对于定义域内的所有点，都满足：

$$
f(x^*) < f(x), \forall x\in D
$$



**局部极小点**：点 $c$ 称为函数 $f(x)$ 的一个局部极小(或极大)点，若对于满足 $0<|\Delta x|\leq r$ 的所有 $\Delta x$，均有：

$$
f(c) \leqslant f(c+\Delta x) \text{ 或 } f(c) \geqslant f(c+\Delta x)
$$

## 向量变元问题定义

### 闭合邻域

$$
B(\bar{x}; r) = \{x \mid \|x - \bar{x}\|_2 \leqslant r\}
$$

$$
B(c; r) = \{x \mid x \in \mathbb{R}^n, \|x - c\|_2 < r\}
$$

**内点**

给定一集合$S$,点$\bar{x}$称为集合$S$的内点(interior point),若$\bar{x}\in S$,并且存在$\bar{x}$的一邻域，该邻域完全包含在集合$S$内. 集合$S$的内集 (interior) 记作 $int(S)$,它是$S$的所有内点的合集

**边界点**

给定一集合$S$,点$x$是$S$的边界点 (boundary point),若$x$的每一个邻域至少有一个点在$S$ 内，并且至少有一个点不在$S$内. 集合$S$的边界记作 $bnd(S)$,是$S$的所有边界点的合集一个闭集包含其所有边界点.


## 矩阵变元问题定义



 

## 平稳点

$$
\nabla f\left(x^{*}\right)=\left[\frac{\partial f(x)}{\partial x}\right]_{x=x^{*}}^{T}=0
$$

### local minimum

### local maximum

### saddle point










#### **黑塞矩阵 Hessian Matrix 二阶导数矩阵**

$$
\mathbf{H(f)} = \nabla^{2} f(x)=\left[\begin{array}{cccc}
\frac{\partial^{2} f(x)}{\partial x_{1}^{2}} & \frac{\partial^{2} f(x)}{\partial x_{1} \partial x_{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{1} \partial x_{n}} \\
\frac{\partial^{2} f(x)}{\partial x_{2} \partial x_{1}} & \frac{\partial^{2} f(x)}{\partial x_{2}^{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{2} \partial x_{n}} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^{2} f(x)}{\partial x_{n} \partial x_{1}} & \frac{\partial^{2} f(x)}{\partial x_{n} \partial x_{2}} & \ldots & \frac{\partial^{2} f(x)}{\partial x_{n}^{2}}
\end{array}\right]
$$





## 最优性条件
### 实数域

一阶必要条件：（局部极小值/局部极大值）：$\nabla f(x^*)=0$

二阶必要条件：（局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)\geq 0$

二阶充分条件：（严格局部极小值）$\nabla f(x^*)=0 \text{且} \nabla^2 f(x^*)>0$

### 复数域






