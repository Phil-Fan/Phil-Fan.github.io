# 05 | 有约束 数值解法





## 可行方向 —— Zoutendijk可行方向法



$$
\begin{array}{l}
\nabla f\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p}<0 \\
-\nabla g_{j}\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p}<0, \quad j \in J\left(\boldsymbol{x}^{(k)}\right)
\end{array}
$$


$$
\begin{align} 
\min \eta \\
s.t.
\left\{
	\begin{array}{lr}  
    \nabla f\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p} \leq \eta \\
    -\nabla g_{j}\left(\boldsymbol{x}^{(k)}\right)^{T} \boldsymbol{p} \leq \eta, \quad j \in J\left(\boldsymbol{x}^{(k)}\right)\\
    -1 \le p \le 1
	\end{array}
\right.
\end{align}
$$

- $\eta<0$：可行下降方向
- $\eta=0$：迭代结束！
- $\eta>0$：不会出现



## 制约函数

### 外点法——罚函数，罚外点

**思想：构造罚函数，惩罚可行域外的迭代点**

$$
\begin{align}
\min P(x,M)=f(x)+M\sum_{i=1}^{m}h_{i}^{2}(x)+M\sum_{j=1}^{l}[\min (0,g_{j}(x))]^{2}
\end{align}
$$

Courant罚函数

$M>0$ 为罚因子，当$M$趋向无穷时，$x^{*}$为原问题约束极值解。



$[\min (0,g_{j}(x))]^{2}$是罚函数，因为在可行域内$g(x)\ge 0$，可行域外$g(x)\le 0$ ，所以相当于用一个二次函数来拟合。



例子

最小化函数 $f(x) = -\frac{1}{3}(x_1+1)^3 + x_2$，满足以下条件：

$$
\begin{aligned}
x_1 - 1 &\geq 0 \\
x_2 &\geq 0
\end{aligned}
$$

其中，$\nabla f(x) = \left[-\frac{(x_1+1)^2}{3}, 1\right]$​。

构造罚函数:

$$
P(x, M)=\frac{1}{3}(x_{1}+1)^{3}+x_{2}+M[\min (0, x_{1}-1)]^{2}+M[\min (0, x_{2})]^{2}
$$

根据一阶驻点条件, 有

$$
\begin{aligned}
\frac{\partial P}{\partial x_{1}} & =(x_{1}+1)^{2}+2 M[\min (0, x_{1}-1)]=0 \\
\frac{\partial P}{\partial x_{2}} & =1+2 M[\min (0, x_{2})]=0
\end{aligned}
$$

如果$x_{1} \geq 1 \Rightarrow x_{1}=1$ ，矛盾

如果$x_{2} \geq 0 \Rightarrow 1=0$ ，不成立

所以考虑$x_{1}<1, x_{2}<0$区域的驻点。(可行域外的点)

$$
\begin{align}
\frac{\partial P}{\partial x_{1}}  =(x_{1}+1)^{2}+2 M(x_{1}-1)=0 \\
\frac{\partial P}{\partial x_{2}}  =1+2 M x_{2}=0
\end{align}
$$

可得:

$$
\begin{align}
& x_{1}^{*}=-1-M \pm \sqrt{M^{2}+4 M}\\
& x_{2}^{*}=-\frac{1}{2 M} \\
 &\quad M \rightarrow+\infty \\
& \nabla^{2} P(x)=\left[\begin{array}{cc}
2\left(x_{1}+1\right)+2 M & 0 \\
0 & 2 M
\end{array}\right]>0 \\
& 故为极小值
\end{align}
$$

![image-20240612002931360](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240612002931360.png)



### 内点法——障碍函数，阻止内点

**构造障碍函数，阻止迭代点离开可行域。**

$$
\begin{array}{l}
\min \limits_{x \in R_{0}} \bar{P}(x, r)=f(x)+r \sum_{j=1}^{l} \frac{1}{g_{j}(x)} \\
或  \\
\min \limits_{x \in R_{0}} \bar{P}(x, r)=f(x)-\sum_{j=1}^{l} \log g_{j}(x)
\end{array}
$$



其中 $R_{0}=\left\{x \mid g_{j}(x) > 0, j=1,2, \cdots, l\right\}$ 严格内点

$r>0$ 为障碍因子，其在迭代中的取值会不断减小，趋向于 0 ，使$x$​可趋向于边界。

**例子**

最小化函数 $f(x) = x_1 + x_2$，满足以下条件：

$$
\begin{aligned}
-x_1^2 + x_2 &\geq 0 \\
x_1 &\geq 0
\end{aligned}
$$



构造障碍函数:

$$
\begin{align}
\bar{P}(x, r)=x_{1}+x_{2}-r \cdot\left[\log \left(-x_{1}^{2}+x_{2}\right)+\log \left(x_{1}\right)\right]
\end{align}
$$

根据驻点一阶条件, 有

$$
\begin{array}{l}
\frac{\partial \bar{P}}{\partial x_{1}}=1-r \cdot \frac{-2 x_{1}}{-x_{1}^{2}+x_{2}} \cdot r \cdot \frac{1}{x_{1}}=0 \\
\frac{\partial \bar{P}}{\partial x_{2}}=1-r \cdot \frac{1}{-x_{1}^{2}+x_{2}}=0
\end{array}
\text { 求解得到: }
$$

$$
\begin{array}{l}
x_{1}=\frac{\sqrt{1+8 r}-1}{4} \\
x_{2}=\frac{3}{2} r-\frac{\sqrt{1+8 r}-1}{8}
\end{array}
$$

$r \rightarrow 0$ 时, 有

$$
\left\{\begin{array}{l}
x_{1}^{*}=0 \\
x_{2}^{*}=0
\end{array}\right.
$$

**内点法收敛性分析**

障碍函数

$$
\bar{P}(x, r)=f(x)-r_k \sum_{j=1}^{l} \log g_{j}(x)
$$

第k步障碍函数局部极小值满足

$$
\begin{align}
\nabla \bar{P}\left(x^{(k)}, r_k\right)  =\nabla f\left(x^{(k)}\right)-r_k \sum_{j=1}^{l} \frac{1}{g_{j}\left(x^{(k)}\right)} \nabla g_{j}\left(x^{(k)}\right)=0 \\
\nabla P\left(x^{(k)}, r_k\right)  =\nabla f\left(x^{(k)}\right)-\sum_{j=1}^{l} \mu_{j}\left(k\right) \nabla g_{j}\left(x^{(k)}\right)=0 \\
\mu_{j}(k)=\frac{r}{g_{j}\left(x^{(k)}\right)} \geq 0
\end{align}
$$

$x_{k}^{*}$迭代收敛时

$$
\begin{align}
 \nabla P\left(x^{*}, r\right)=\nabla f\left(x^{*}\right)-\sum_{j=1}^{l} \mu_{j}^{*} \nabla g_{j}\left(x^{*}\right)=0 \\
 \mu_{j}^{*}=\frac{r}{g_{j}\left(x^{*}\right)} \geq 0 \\
 \mu_{j}^{*} g_{j}\left(x^{*}\right)=r \rightarrow 0
\end{align}
$$

**KKT条件!**

**如果$x(k)$是$\min \bar{P}(x ; r)$的全局极小值，则内点法收敛到全局最优解！**

### 混合法

- 内点法不能处理等式约束问题
- 外点法不能处理目标函数在可行域外不存在的问题
- 对等式约束和当前不被满足的不等式约束，使用罚函数法，对满足的不等式约束，使用障碍函数法。

