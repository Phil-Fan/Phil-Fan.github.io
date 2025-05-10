# 复变函数

## 解析函数

复解析函数

1. 复变函数 $f(z)$ 是全纯函数 (即复解析函数);
2. 复变函数的导数 $f'(z)$ 存在，并且连续;
3. 复变函数 $f(z)$ 满足 Cauchy-Riemann 条件

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{和} \quad \frac{\partial v}{\partial x} = -\frac{\partial u}{\partial y}
$$

4. 复变函数 $f(z)$ 的所有导数存在，并且具有一个收敛的幂级数。

形式偏导定义：

$$
\begin{aligned}
\frac{\partial}{\partial z} &= \frac{1}{2}\left(\frac{\partial}{\partial x}-\mathrm{j}\frac{\partial}{\partial y}\right) \quad z=x+\mathrm{j}y \\
\frac{\partial}{\partial z^{*}} &= \frac{1}{2}\left(\frac{\partial}{\partial x}+\mathrm{j}\frac{\partial}{\partial y}\right)
\end{aligned}
$$

实部与虚部的独立性假设：

$$
\begin{aligned}
\frac{\partial x}{\partial y} &= 0 \quad\text{和}\quad \frac{\partial y}{\partial x} = 0 \\[1em]
\frac{\partial z}{\partial z^*} &= \frac{\partial x}{\partial z^*}+\mathrm{j}\frac{\partial y}{\partial z^*} \\
&= \frac{1}{2}\left(\frac{\partial x}{\partial x}+\mathrm{j}\frac{\partial x}{\partial y}\right)+\mathrm{j}\frac{1}{2}\left(\frac{\partial y}{\partial x}+\mathrm{j}\frac{\partial y}{\partial y}\right) \\
&= \frac{1}{2}(1+0)+\mathrm{j}\frac{1}{2}(0+\mathrm{j}) \\[1em]
\frac{\partial z^*}{\partial z} &= \frac{\partial x}{\partial z}-\mathrm{j}\frac{\partial y}{\partial z} \\
&= \frac{1}{2}\left(\frac{\partial x}{\partial x}-\mathrm{j}\frac{\partial x}{\partial y}\right)-\mathrm{j}\frac{1}{2}\left(\frac{\partial y}{\partial x}-\mathrm{j}\frac{\partial y}{\partial y}\right) \\
&= \frac{1}{2}(1-0)-\mathrm{j}\frac{1}{2}(0-\mathrm{j})
\end{aligned}
$$

因此：

$$
\frac{\partial z}{\partial z^*} = 0 \quad\text{和}\quad \frac{\partial z^*}{\partial z} = 0
$$

即 $z$ 和 $z^*$ 是两个相互独立的变量。


## 复积分

## 级数

### 泰勒展开


### Talor定理


## 留数


## 保角映射


## Laplace变换

[拉普拉斯变换与拉普拉斯逆变换的常用结论与经典公式-CSDN博客](https://blog.csdn.net/wh_STUDY/article/details/126403817)

