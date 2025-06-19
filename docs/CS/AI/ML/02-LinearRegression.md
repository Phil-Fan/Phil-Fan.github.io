# 02 | Linear Regression

## OLS

考虑经典的线性回归模型：

$$
y = X \beta + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma^2 I_n)
$$

其中：

* $y \in \mathbb{R}^n$：响应变量
* $X \in \mathbb{R}^{n \times p}$：满秩设计矩阵（列满秩）
* $\beta \in \mathbb{R}^p$：未知回归系数
* $\varepsilon$：独立同分布噪声，均值 0，方差 $\sigma^2$


残差平方和（Residual Sum of Squares, RSS）定义为：

$$
RSS = \sum_{i=1}^n \left( y_i - x_{i1}\beta_1 - \cdots - x_{ip}\beta_p \right)^2
$$

也可以写成向量形式：

$$
RSS = \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\mathsf{T}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})
$$

最小二乘估计（Ordinary Least Squares, OLS）就是选择使 RSS 最小的 $\boldsymbol{\beta}$：

$$
\widehat{\beta} = \underset{\boldsymbol{\beta}}{\operatorname*{arg\,min}} \; (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\mathsf{T}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})
$$


- To estimate $\beta$, we set the derivative equal to 0
$$\frac{\partial \text{RSS}}{\partial \beta} = -2 \mathbf{X}^\top (\mathbf{y} - \mathbf{X} \beta) = 0$$

$$
\widehat{\beta} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}
$$

- $\mathbf{X}$ full rank $\iff \mathbf{X}^\top \mathbf{X}$ invertible

### 性质

$$
\hat{\beta} = (X^T X)^{-1} X^T y
$$




**无偏**




我们计算 $\mathbb{E}[\hat{\beta}]$：

$$
\begin{aligned}
\mathbb{E}[\hat{\beta}] &= \mathbb{E}[(X^T X)^{-1} X^T y] \\
&= (X^T X)^{-1} X^T \mathbb{E}[y] \\
&= (X^T X)^{-1} X^T (X\beta) \\
&= (X^T X)^{-1} X^T X \beta \\
&= \beta
\end{aligned}
$$

---

**方差**

将 $\mathbf{y} = \mathbf{X} \boldsymbol{\beta} + \boldsymbol{\varepsilon}$ 代入：

$$
\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top (\mathbf{X} \boldsymbol{\beta} + \boldsymbol{\varepsilon}) \\
= \boldsymbol{\beta} + (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \boldsymbol{\varepsilon}
$$

有

$$
\begin{aligned}
\operatorname{Var}(\hat{\boldsymbol{\beta}})
&= \operatorname{Var} \left( (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \boldsymbol{\varepsilon} \right) \\
&= (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \operatorname{Var}(\boldsymbol{\varepsilon}) \mathbf{X} (\mathbf{X}^\top \mathbf{X})^{-1} \\
&= \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{X} (\mathbf{X}^\top \mathbf{X})^{-1} \\
&=\boxed{ \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1} }\\
&= \widehat{\sigma}^2 (\mathbf{X}^\top \mathbf{X})^{-1} \quad \text{（可用残差平方和估计）} \\
&= \frac{RSS}{n - p} (\mathbf{X}^\top \mathbf{X})^{-1} \\
&= \frac{1}{n - p} \sum_{i=1}^n \hat{\varepsilon}_i^2 (\mathbf{X}^\top \mathbf{X})^{-1}
\end{aligned}
$$


---

**UMVUE**

Lehmann–Scheffé 定理告诉我们：

> 若某无偏估计量是充分统计量的函数，则它是 UMVUE。

我们来验证：

1️⃣ $\hat{\beta}$ 是 $\beta$ 的无偏估计量 → ✅

已证

2️⃣ $X^T y$ 是充分统计量 → ✅

由**因子分解定理**：

* $y \sim \mathcal{N}(X\beta, \sigma^2 I)$
* 联合密度函数可以写成关于 $X^T y$ 的函数和不含 $\beta$ 的函数之积
* 所以 $X^T y$ 是 $\beta$ 的充分统计量

而 $\hat{\beta}$ 是 $X^T y$ 的函数 ⇒ 它是**充分统计量的函数**

✅ 满足 Lehmann–Scheffé 定理条件 ⇒ 是 UMVUE！

---

或者你也可以使用 Gauss-Markov 定理（非正态条件下）

> 在线性模型中，在所有线性无偏估计量中，OLS 是方差最小的。

但要注意：

* **Gauss-Markov 定理 → 最优线性无偏估计（BLUE）**
* **Lehmann–Scheffé 定理（+ 正态性）→ 最小方差无偏估计（UMVUE）**



### Training Error & Test Error

$$
\begin{aligned}
\mathbb{E}[\mathrm{TestErr}] &= \mathbb{E}\|\mathbf{y}^*-\mathbf{X}\widehat{\beta}\|^2 \\
&= \mathbb{E}\|(\mathbf{y}^*-\mathbf{X}\beta)+(\mathbf{X}\beta-\mathbf{X}\widehat{\beta})\|^2 \\
&= \mathbb{E}\|\mathbf{y}^*-\mu\|^2 + \mathbb{E}\|\mathbf{X}(\widehat{\beta}-\beta)\|^2 \\
&= \mathbb{E}\|\mathbf{e}^*\|^2 + \mathrm{Trace}(\mathbf{X}^\mathsf{T}\mathbf{X}\,\mathrm{Cov}(\widehat{\beta})) \\
&= n\sigma^2 + p\sigma^2
\end{aligned}
$$

$$
\begin{aligned}
\mathbb{E}[\mathrm{TrainErr}] &= \mathbb{E}\|\mathbf{y}-\mathbf{\widehat{y}}\|^2 = \mathbb{E}\|(\mathbf{I}-\mathbf{H})\mathbf{y}\|^2 \\
&= \mathbb{E}\|(\mathbf{I}-\mathbf{H})\mathbf{e}\|^2 \\
&= \mathrm{Trace}\left((\mathbf{I}-\mathbf{H})^\mathsf{T}(\mathbf{I}-\mathbf{H})\,\mathrm{Cov}(\mathbf{e})\right) \\
&= (n-p)\sigma^2
\end{aligned}
$$

## 广义线性回归

### logistic

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240807233452.png)

线性回归有一个很强的假设，就是y是连续的；并且有更像邻近数的趋势(MSE 对于线性回归不是一个好的function)

- one vs. Rest

logistic function:

- sigmoid function: $f(x) = \frac{1}{1+e^{-x}}$
CDF(累积分布函数)ofthe standard logistic distribution   
使用sigmoid函数将线性回归的输出转换为概率

!!! note "logistic Regreesion是一个线性模型"
    主要考虑的是decision boundary
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240807234021.png)


为什么loss function要取log
- 为了方便求导
- 取log使得连乘变成连加，不会丢失信息

Assumptions behind logistic regression
- l(a) = -\sum_{i\in I} \log(1+e^{-y_i a^T x_i})


pros:
- binomial distribution is a  good assumption for classification
- provide a probability
- low computation, easy to optimize
- support online learning:梯度下降的模型都支持在线学习

cons:
- too simple:high bias & low variance


对于分类问题，只关心分类正确的类的值

## 统计视角

!!! note "因此，在高斯噪声的假设下，最小化均方误差等价于对线性模型的极大似然估计。"


## Penalty

A unified framework is to minimize the objective function

$$
\arg\min_{\beta} \frac{1}{2n}\|\mathbf{y}-\mathbf{X}\boldsymbol{\beta}\|^2 + \sum_{j=1}^p P_{\lambda}(\beta_j)
$$

where $P_{\lambda}(\cdot)$ is a penalty function applied on the value of each parameter, and $\lambda$ is a tuning parameter.

- Lasso: $P_{\lambda}(\beta) = \lambda|\beta|$
- Ridge: $P_{\lambda}(\beta) = \lambda\beta^2$
- Best subset: $P_{\lambda}(\beta) = \lambda\mathbf{1}\{\beta \neq 0\}$
- Elastic net: $P_{\lambda}(\beta) = \lambda_1|\beta| + \lambda_2\beta^2$


### Lasso - l1

| 核心内容            | 解释                                          |
| --------------- | ------------------------------------------- |
| Oracle Property | 同时实现变量选择一致性 + 最优估计精度                        |
| Lasso 的问题       | 有偏差，不能同时实现两者                                |
| 理论上条件           | 为了选变量，$\lambda$ 要够大；但为估计精度，$\lambda$ 又要趋于 0 |
| 解决方法            | 改用无偏惩罚函数（如 SCAD），或者接受一定折中                   |


求解下面的优化问题

$$
\begin{aligned}
& \text{minimize } \sum_{i=1}^{n} \left(y_i - \sum_{j=1}^{p} \beta_j x_{ij}\right)^2 \\
& \text{subject to } \sum_{j=1}^{p} |\beta_j| \leq s
\end{aligned}
$$

- Each value of $\lambda$ corresponds to an unique value of $s$.


#### Lasso 回归在正交设计下的推导与原理


**假设：**

* 设计矩阵满足 $\mathbf{X}^\top \mathbf{X} = \mathbf{I}_p$（即列向量正交，单位范数）
* 目标是求解 Lasso 回归问题：

$$
\widehat{\boldsymbol{\beta}}^{\text{lasso}} = \arg\min_{\boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_1
$$

步骤 1：插入 OLS 解

因为 OLS 解为：

$$
\widehat{\boldsymbol{\beta}}^{\text{ols}} = \mathbf{X}^\top \mathbf{y}
$$

我们将其插入目标函数：

$$
\begin{align*}
\|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|^2 &= \|\mathbf{y} - \mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}} + \mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}} - \mathbf{X} \boldsymbol{\beta}\|^2\\
&= \|\mathbf{y} - \mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}}\|^2 + \|\mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}} - \mathbf{X} \boldsymbol{\beta}\|^2 + 2 \underbrace{(\mathbf{y} - \mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}})^\top (\mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}} - \mathbf{X} \boldsymbol{\beta})}_{=0}
\end{align*}
$$

其中最后一项为 0 是因为：

* 残差 $\mathbf{r} = \mathbf{y} - \mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}}$ 垂直于 $\operatorname{Col}(\mathbf{X})$
* 而 $\mathbf{X}(\widehat{\boldsymbol{\beta}}^{\text{ols}} - \boldsymbol{\beta}) \in \operatorname{Col}(\mathbf{X})$

---

步骤 2：目标函数化简

因为第一项与 $\boldsymbol{\beta}$ 无关，我们只需最小化第二项 + 正则项：

$$
\min_{\boldsymbol{\beta}} \|\mathbf{X} \widehat{\boldsymbol{\beta}}^{\text{ols}} - \mathbf{X} \boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_1\\
\leftrightarrow \min_{\boldsymbol{\beta}} \|\widehat{\boldsymbol{\beta}}^{\text{ols}} - \boldsymbol{\beta}\|^2 + \lambda \|\boldsymbol{\beta}\|_1 \quad (\because\mathbf{X}^\top \mathbf{X} = \mathbf{I})
$$

**变量独立求解**

目标函数可分解为每个参数的独立优化：

$$
\widehat{\beta}_j^{\text{lasso}} = \arg\min_{x} (x - a)^2 + \lambda |x|, \quad a = \widehat{\beta}_j^{\text{ols}}
$$

这就是经典的 **Soft Thresholding 问题**，解为：

$$
\boxed{
\widehat{\beta}_j^{\text{lasso}} = \operatorname{sign}(a) \cdot \max(|a| - \lambda/2, 0)
}
$$

即：

* 如果 $|a| \leq \lambda/2$，解为 0
* 否则，在方向上缩减 $\lambda/2$

Soft Thresholding = 变量选择机制

* Ridge 回归使用 $\ell_2$ 惩罚：系数永远不会变为 0，只是变小
* Lasso 使用 $\ell_1$ 惩罚：会直接把小的系数压成 0
* 所以 Lasso 能实现 **变量选择（sparsity）**


| 项目             | 解释   |
| ---------------- | ------------------------ |
| 正交设计         | $\mathbf{X}^\top \mathbf{X} = \mathbf{I}$ 简化问题            |
| 拆分误差项        | 残差项垂直于列空间，交叉项为 0                               |
| 可分解目标        | 可对每个 $\beta_j$ 独立求解                                  |
| Soft Threshold 解 | |
| 稀疏性来源        | 系数可能直接为 0，实现选择                                   |
| $\lambda$ 越大   | 越多的参数会被压成 0                                         |



### Ridge - l2

| 视角    | 解释                                                                                                   |
| ----- | ---------------------------------------------------------------------------------------------------- |
| 最优化视角 | Ridge 解是最小化 $\|\mathbf{y} - \mathbf{X}\boldsymbol{\beta} \|^2 + \lambda \|\boldsymbol{\beta}\|^2$ 的解 |
| 贝叶斯视角 | Ridge 解是 $\boldsymbol{\beta} \sim \mathcal{N}(0, \frac{\sigma^2}{\lambda} \mathbf{I})$ 下的后验均值        |
|PCA视角||

#### 优化视角
最优化视角，即求解下面的最优化问题

$$
(y - X\beta)^{\top}(y - X\beta) + \lambda\beta^{\top}\beta
$$

Take derivative with respect to $\beta$ and set to zero

$$
\begin{aligned}
\widehat{\beta}^{\mathrm{~ridge}}&= \boxed{(X^{\top}X + \lambda I)^{-1}X^{\top}y}\\&=(\mathbf{X}^\mathsf{T}\mathbf{X}+\lambda\mathbf{I})^{-1}(\mathbf{X}^\mathsf{T}\mathbf{X})(\mathbf{X}^\mathsf{T}\mathbf{X})^{-1}\mathbf{X}^\mathsf{T}\mathbf{y}\\&=(\mathbf{X}^\mathsf{T}\mathbf{X}+\lambda\mathbf{I})^{-1}(\mathbf{X}^\mathsf{T}\mathbf{X})\widehat{\boldsymbol{\beta}}^\mathsf{ols}\\&=\mathbf{Z}\widehat{\boldsymbol{\beta}}^{\mathrm{ols}}
\end{aligned}
$$


#### PCA视角

!!! note "SVD 分解"

    $$
    \mathbf{X} = U D V^\top
    $$

    * $U$：正交列向量，表示在数据空间中的方向（主成分）
    * $D$：奇异值（与协方差矩阵特征值相关）
    * $V$：输入空间的正交基（回归系数方向）


将协方差矩阵写成 PCA 形式：

$$
\frac{1}{n} \mathbf{X}^\top \mathbf{X} = V D^2 V^\top
$$

* 说明协方差的主方向（特征向量）就是 $V$，对应特征值 $d_j^2$
* 第 $j$ 个主成分为 $X v_j = d_j u_j$
* 大的奇异值方向：数据方差大，保留信息多
* 小的奇异值方向：容易过拟合，要强烈惩罚

Ridge 回归对响应变量的估计：

$$
\mathbf{X} \hat{\boldsymbol{\beta}}^{\text{ridge}} = \sum_{j=1}^p u_j \cdot \frac{d_j^2}{d_j^2 + \lambda} \cdot u_j^\top \mathbf{y}
$$


1. 把 $\mathbf{y}$ 投影到每个主成分方向 $u_j$
2. 投影结果 $u_j^\top y$ 被 **缩小** 了一个因子 $\frac{d_j^2}{d_j^2 + \lambda}$
3. $d_j^2$ 小的方向（低方差）被惩罚得更严重，防止对噪声过拟合


| 主题     | 内容                                    |
| ------ | ------------------------------------- |
| 有偏性    | Ridge 有偏，但可控制偏差                       |
| 方差降低   | Ridge 显著减少估计方差                        |
| MSE 更优 | 合适的 $\lambda$ 可让 MSE 优于 OLS           |
| 几何理解   | Ridge 在 PCA 空间中对不同方向施加不同强度的 shrinkage |
| 实用价值   | 尤其在高维/共线性严重时表现更好                      |




#### 贝叶斯视角

📌 先验假设

我们将回归系数 $\boldsymbol{\beta}$ 视为一个随机变量，赋予如下先验分布：

$$
\boldsymbol{\beta} \sim \mathcal{N}\left(0, \frac{\sigma^2}{\lambda} \mathbf{I} \right)
$$

这是一个零均值、高斯先验，对每个参数都做了 $\ell_2$ 范数的惩罚。

🎯 似然函数（来自线性模型）

$$
\mathbf{y} \mid \boldsymbol{\beta} \sim \mathcal{N}(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I})
$$

🧠 后验分布

利用贝叶斯定理（高斯 + 高斯 ⇒ 高斯），得到后验分布为：

$$
\boldsymbol{\beta} \mid \mathbf{y} \sim \mathcal{N}\left( \underbrace{(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{y}}_{\text{ridge 解}}, \; \text{协方差矩阵} \right)
$$

其中后验 **均值** 正是 Ridge 回归的解析解：

$$
\boxed{
\mathbb{E}[\boldsymbol{\beta} \mid \mathbf{y}] = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{y}
}
$$






#### bias


**Ridge 回归是有偏估计**

$$
\mathbb{E}[\hat{\boldsymbol{\beta}}^{\text{ridge}}] = Z \boldsymbol{\beta}, \quad Z = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{X}
$$

* 因为 $Z \neq I$，所以 ridge 估计是 **有偏的**
* 随着正则化参数 $\lambda$ 增大，**bias² 增加**
* 这是偏差-方差权衡的一部分



#### variance

$$
\begin{align*}
\operatorname{Var}\left(\widehat{\boldsymbol{\beta}}^{\text{ ridge}}\right) &= \operatorname{Var}\left(\mathbf{Z}\widehat{\boldsymbol{\beta}}^{\mathrm{ols}}\right) \\
 &= {\color{red}Z}\operatorname{Var}\left(\widehat{\boldsymbol{\beta}}^{\mathrm{ols}}\right) {\color{red}Z^T}\\
&= {\color{red}(\mathbf{X}^\mathsf{T}\mathbf{X}+\lambda\mathbf{I})^{-1}(\mathbf{X}^\mathsf{T}\mathbf{X})}\sigma^2(X^TX)^{-1}{\color{red}(\mathbf{X}^\mathsf{T}\mathbf{X})(\mathbf{X}^\mathsf{T}\mathbf{X}+\lambda\mathbf{I})^{-1}}\\
&=\sigma^{2}\left(\mathbf{X}^{\top} \mathbf{X}+\lambda \mathbf{I}\right)^{-1} \mathbf{X}^{\top} \mathbf{X}\left(\mathbf{X}^{\top} \mathbf{X}+\lambda \mathbf{I}\right)^{-1}
\end{align*}
$$

!!! note "总体方差是一个关于正则化强度 $\lambda$ 的**单调递减函数**"

    $$
    \text{Total Variance} = \operatorname{Tr}\left( \operatorname{Var}\left(\hat{\boldsymbol{\beta}}^{\text{ridge}} \right) \right)
    = \sigma^2 \cdot \operatorname{Tr} \left[ \left( X^T X + \lambda I \right)^{-1} X^T X \left( X^T X + \lambda I \right)^{-1} \right]
    $$

    记 $\mathbf{S} = X^T X$，它是对称正定的

    我们可以对它做**特征值分解**（因为它对称）：

    $$
    \mathbf{S} = Q \Lambda Q^\top, \quad \text{其中 } \Lambda = \text{diag}(\lambda_1, \ldots, \lambda_p), \lambda_i > 0
    $$

    于是整个方差矩阵可以化简为：

    $$
    \operatorname{Var}(\hat{\boldsymbol{\beta}}^{\text{ridge}})
    = \sigma^2 Q \cdot \text{diag} \left( \frac{\lambda_i}{(\lambda_i + \lambda)^2} \right) \cdot Q^\top
    $$

    所以其 trace 为：

    $$
    \text{Total Variance} = \sigma^2 \sum_{i=1}^p \frac{\lambda_i}{(\lambda_i + \lambda)^2}
    $$

    * 总体方差是一个关于正则化强度 $\lambda$ 的**单调递减函数**
    * 换句话说，**正则化越强 ⇒ 系数波动越小**


#### 自由度


* Ridge 回归虽然估计 $\widehat{\boldsymbol{\beta}}^{\text{ridge}} \in \mathbb{R}^p$，但由于 **Shrinkage**，不等价于使用所有 $p$ 个变量的全部自由度。
* 自由度随着 $\lambda$ 的变化而变化：

  * $\lambda \to 0$: Ridge 退化为 OLS，$\text{df} = p$
  * $\lambda \to \infty$: 所有参数被压缩到 0，$\text{df} \to 0$
  * 所以：

    $$
    0 \leq \text{df}(\lambda) \leq p
    $$

!!! note "dof"
    $$
    \text{df}(\hat{f}) = \frac{1}{\sigma^2} \sum_{i=1}^n \operatorname{Cov}(\hat{y}_i, y_i) = \frac{1}{\sigma^2} \operatorname{Trace} \left( \operatorname{Cov}(\hat{\mathbf{y}}, \mathbf{y}) \right)
    $$

$$
\widehat{\mathbf{y}} = \mathbf{S} \mathbf{y}, \quad \text{其中} \quad \mathbf{S} = \mathbf{X}(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top
$$

$$
\text{df}(\lambda) = \operatorname{Trace}(\mathbf{S}) = \operatorname{Trace} \left( \mathbf{X}(\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \right)
$$

* 若对 $\mathbf{X}$ 做奇异值分解（SVD）：

  $$
  \mathbf{X} = UDV^\top, \quad \text{其中} \ D = \operatorname{diag}(d_1, \dots, d_p)
  $$

* 则自由度可写为：

$$
\boxed{
\text{df}(\lambda) = \sum_{j=1}^{p} \frac{d_j^2}{d_j^2 + \lambda}
}
$$

* 每个主成分方向 $j$ 的自由度贡献是一个 shrinkage 因子：

  $$
  \frac{d_j^2}{d_j^2 + \lambda}
  $$
* 方差小的方向（$d_j$ 小）会被严重 shrink，自由度贡献也少
* 这是 Ridge 比 OLS 更稳健但有偏的原因





### elastic
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202506200340914.png)

lasso与ridge对比
- Ridge is $\ell_{2}$ penalty
- Lasso is $\ell_{1}$ penalty
- Best subset is $\ell_{0}$ penalty
- Bridge penalty is $\ell_{q}$ normal

$q = 4$  
$q = 2$  
$q = 1$  
$q = 0.5$  
$q = 0.1$

$\sum_{j}|\beta_{j}|^{q}$ for given values of $q$.

Elastic-net is a hybrid of $\ell_{1}$ and $\ell_{2}$:

$\lambda_{1}\|\beta\|_{1} + \lambda_{2}\|\beta\|_{2}^{2}$


## LDA

[理解主成分分析（1）——最大方差投影与数据重建 - Fenrier Lab](https://seanwangjs.github.io/2017/12/21/principal-components-analysis.html)

[简单理解线性判别分析 - 知乎](https://zhuanlan.zhihu.com/p/66088884)

[LDA线性判别分析——投影的疑问解答\_lda投影-CSDN博客](https://blog.csdn.net/qq_41398808/article/details/100065314)

最小化类内方差

$$
\begin{align*} &\quad \min\limits_w \left[\sum\limits_{x\in X_0}(w^Tx-w^T\mu_0)^2+\sum\limits_{x\in X_1}(w^Tx-w^T\mu_1)^2\right]\\ &=\min\limits_w w^T \left[\sum\limits_{x\in X_0}(x-\mu_0)(x-\mu_0)^T+\sum\limits_{x\in X_1}(x-\mu_1)(x-\mu_1)^T\right]w \\ &=\min\limits_w w^TS_ww \\ \end{align*}
$$

最大化类间方差


$$
\begin{align*} &\quad \max\limits_w \left[(w^T\mu_0-\frac{w^T\mu_0+w^T\mu_1}{2})^2+(w^T\mu_1-\frac{w^T\mu_0+w^T\mu_1}{2})^2\right]\\ &=\max\limits_w \frac{1}{2}w^T(\mu_0-\mu_1)(\mu_0-\mu_1)^Tw\\ &=\max\limits_w \frac{1}{2}w^TS_bw \\ \end{align*}
$$

因为自变量只有$w$，不一定二者都能同时达到最优，所以整合到一起取下式的最大值：

$$
J = \displaystyle \frac{w^TS_bw}{w^TS_ww}
$$

[LDA——线性判别分析基本推导与实验-CSDN博客](https://blog.csdn.net/qq_37189298/article/details/108656649)

[二分类线性判别分析，看懂这篇就够了 - 知乎](https://zhuanlan.zhihu.com/p/488134514)