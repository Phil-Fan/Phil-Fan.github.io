# 02 | Linear Regression
y 是一个连续的值；
区别于classification，y是一个离散的值

## Polynomial Curve Fitting

$f(x,\omega) = \omega_0 + \omega_1x + \omega_2x^2 + \omega_3x^3 + \dots + \omega_Mx^M = \sum_{j=0}^{M}\omega_jx^j$

loss function: MSE: 


$MSE(\omega) = \frac{1}{N}\sum_{i=1}^{N}(y_i - f(x_i,\omega))^2$

模型是已知的，$\omega$未知，通过最小化MSE来求解$\omega$

- 最小二乘法

只能用于线性回归


using matrix notation for convenience: $X = [1,x,x^2,x^3,...,x^n], y = [y_1,y_2,...,y_n]^T$

$Loss(\omega) = (y - X^T\omega)^T(y - X^T\omega)$

梯度： $\nabla_{\omega}Loss(\omega) = -2X(y - X^T\omega)$

令梯度为0，求解$\omega$，得到$\omega = (X^TX)^{-1}X^Ty$

!!! tip "这里应该需要补充一下矩阵求导的一些知识"
    [矩阵的导数运算](https://www.bilibili.com/video/BV1av4y1b7MM/?spm_id_from=333.788&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)
    
    矩阵求导广泛应用于最优控制、机器学习等领域
    
    [小白都能理解的矩阵与向量求导链式法则\_矩阵求导链式法则-CSDN博客](https://blog.csdn.net/bitcarmanlee/article/details/105668357)


- Gradient Descent | 梯度下降法
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240806020009.png)
步长的大小：学习率
Time complexity: $O(ndt)$,t是迭代次数,d是特征的数量,n是样本的数量


stochastic gradient descent | 随机梯度下降法
- randomly select b(batch size) samples from the training set
- Time complexity: $O(bdt)$


- Quasi Newton Method | 拟牛顿法



## overfitting | 过拟合
在测试集上效果好的模型就是好的模型

在测试集上效果差的模型就是差模型

把training data中的noise也学习到了

- Ridge Regression | 岭回归

Loss(\omega*)

regularization: 一些先验的假设，比如$\omega$是稀疏的，或者$\omega$是平滑的；避免学习到

超参数：
- $\lambda$：控制正则化的强度: $\lambda$越大，正则化的强度越大，模型越简单，training error 越大；如下图，左侧叫做过拟合，右侧叫做欠拟合![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240806021738.png)
- $\alpha$：控制学习率





## Logistic Regression
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