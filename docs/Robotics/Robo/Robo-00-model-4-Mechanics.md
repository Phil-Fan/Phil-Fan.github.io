# 04 | 速度与静力
[机器人学导论---第五章 速度和静力（一）5.1-5.11（好难） - 知乎](https://zhuanlan.zhihu.com/p/155829972)

## 数学基础
- 向量叉乘
- 矩阵求微分
- 向量求导、矩阵求导
- 矩阵求逆（逆矩阵、伪逆）
- 二次型
- 奇异值分解

## 时变位姿

!!! abstract "本节内容：角速度的表示、线速度的表示、如何在不同连杆之间传递速度"
    由理论力学知：刚体（其联体坐标系为$B$）在参考坐标系{A}中的任何运动都可以分解为点 $^A \!O_B$ 的运动和刚体绕 $^A \!O_B$ 的定点转动

    所以这一节先研究如何表示运动

!!! note "本节的一些符号表示"
    |符号|含义|注意点|
    |---|---|---|
    |${}^B\mathbf{V}_Q$|线速度向量||
    |$\mathbf{v}_C$|相对于世界坐标系|$\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}$|
    |${}^A\Omega_B$|角速度向量|在{A}中描述{B}的定点转动|
    $\mathbf{\omega}_C$|相对于世界坐标系角速度|$\mathbf{\omega}_C = {^U_C}\mathbf{\Omega}_C$|

### 坐标系的平移

同维矢量的微分表示

若 \( {}^B\mathbf{Q} \) 是描述某个点的位置矢量，该点关于{B}的速度是 \( {}^B\mathbf{V}_Q \)。

$$
{}^B\mathbf{V}_Q = \frac{d}{dt} {}^B\mathbf{Q} = \lim_{\Delta t \to 0} \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t}
$$

速度矢量 \( {}^B\mathbf{V}_Q \) 可在任意坐标系中描述(相当于在B的原点建立一个和B固连的，与A姿态相同的坐标系)

$$
{}^A({}^B\mathbf{V}_Q) = {}^A_B\mathbf{R} {}^B\mathbf{V}_Q = ^A(\frac{d}{dt} {}^B\mathbf{Q}) = \lim_{\Delta t \to 0} {}^A_B\mathbf{R}(t) \left( \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t} \right)
$$

坐标系原点相对于世界坐标系{U}的速度:$\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}$


!!! note "需要注意，${}^A({}^B\mathbf{V}_Q)$ 不同于 ${}^A\mathbf{V}_Q$"

    $$
    \begin{align*}
    {}^A\mathbf{V}_Q &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{Q}(t + \Delta t) - {}^A\mathbf{Q}(t)}{\Delta t}\\
    &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{P}_{BORG}(t + \Delta t) + {}^A_B\mathbf{R}(t + \Delta t) {}^B\mathbf{Q}(t + \Delta t) - {}^A\mathbf{P}_{BORG}(t) - {}^A_B\mathbf{R}(t) {}^B\mathbf{Q}(t)}{\Delta t}
    \end{align*}
    $$
    
    特别注意符号的意义
    ${}^A\mathbf{v}_C = {}^A_U\mathbf{R} \mathbf{v}_C = {}^A_U\mathbf{R} {}^U\mathbf{V}_{\text{CORG}} \neq {}^A\mathbf{V}_{\text{CORG}}$






### 坐标系的转动
在 $\{A\}$ 中描述 $\{B\}$ 的定点转动可用角速度向量 $^A\mathbf{\Omega}_B$ 表示
- $^A\mathbf{\Omega}_B$的方向是瞬轴在 $\{A\}$ 中的方向
- $^A\mathbf{\Omega}_B$的大小表示在 $\{A\}$ 中 $\{B\}$ 绕瞬轴的旋转速度。
- 在任意坐标系中描述：$^C(^A\mathbf{\Omega}_B) = {^C_A}\mathbf{R}{^A\mathbf{\Omega}_B}$
- 世界坐标系：$\mathbf{\omega}_C = {^U_C}\mathbf{\Omega}_C$

特别要注意下列符号的意思

$$
\begin{align*}
^A\mathbf{\omega}_C &= {^U_C}\mathbf{R}\mathbf{\omega}_C = {^A_U}\mathbf{R}{^U_C}\mathbf{\Omega}_C \neq {^A\mathbf{\Omega}_C}\\
^C\mathbf{\omega}_C &= {^C_U}\mathbf{R}\mathbf{\omega}_C = {^C_U}\mathbf{R}{^U_C}\mathbf{\Omega}_C
\end{align*}
$$


### 刚体线速度

$$
^A\mathbf{V}_Q = {^A\mathbf{V}_{BORG}} + {^A_B}\mathbf{R}{^B\mathbf{V}_Q} + {^A\mathbf{\Omega}_B} \times {^A_B}\mathbf{R}{^B\mathbf{Q}}
$$

$Q$ 点对 ${A}$ 的线速度为坐标系 ${B}$ 原点的线速度、$Q$ 点在坐标系 ${B}$ 中的线速度和坐标系 ${B}$ 针对坐标系 ${A}$ 旋转形成的 $Q$ 点切向线速度三者的向量合成


### 角速度关系

$$
{^A\mathbf{\Omega}_C} = {^A\mathbf{\Omega}_B} +   {^A_B}\mathbf{R}{^B_C}\mathbf{\Omega}_C
$$

在同一坐标系中，角速度可以相加

### 连杆间速度传递

!!! note "规律"
    - 前一个关节的线速度和角速度都要转换到后一个关节上面
    - 转动型关节会增加角速度的项，平动型关节会增加线速度的项。

**转动型关节**

角速度：连杆 i+1 针对世界坐标系角速度在{i+1}坐标系的表示

$$
^{i+1}\!\omega_{i+1} = ^{i+1}_i\!R {^i\omega_i} + \dot{\theta}_{i+1} {}^{i+1}\!\hat{Z}_{i+1}\\
$$

> 其中，$\hat{Z}_{i+1}$ 是轴 $i+1$在 ${i+1}$ 中的表示；${\theta}_{i+1}$ 是转动型关节 $i+1$ 的关节转速。

线速度：连杆i+1 针对世界坐标系线速度在{i+1}坐标系的表示

$$
{}^{i+1}\!v_{i+1} = {^{i+1}_iR} (^iv_i + ^i\omega_i \times {^iP_{i+1}})
$$

> 连杆的长度隐含在了 $^iP_{i+1}$ 叉乘项当中

**平动型**

角速度：不变

$$
^{i+1}\omega_{i+1} = _i^{i+1}R {^i\omega_i}
$$


线速度：要加一个在轴线上的速度

$$
^{i+1}v_{i+1} = _i^{i+1}R (^iv_i + ^i\omega_i \times ^iP_{i+1}) + \dot{d_{i+1}} \hat{Z}_{i+1}
$$





## 雅可比 - 速度空间的映射

复杂变换在某个局部点可以看作线性变换


<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=79626296&bvid=BV1NJ411r7ja/?share_source=copy_web&vd_source=1ce3320d605852426ce5ccfc9b31eb50&t=233&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=80% height=auto></iframe>



$$
\begin{cases}
\delta y_1 = \frac{\partial f_1}{\partial x_1} \delta x_1 + \frac{\partial f_1}{\partial x_2} \delta x_2 + \cdots + \frac{\partial f_1}{\partial x_6} \delta x_6 \\
\delta y_2 = \frac{\partial f_2}{\partial x_1} \delta x_1 + \frac{\partial f_2}{\partial x_2} \delta x_2 + \cdots + \frac{\partial f_2}{\partial x_6} \delta x_6 \\
\vdots \\
\delta y_6 = \frac{\partial f_6}{\partial x_1} \delta x_1 + \frac{\partial f_6}{\partial x_2} \delta x_2 + \cdots + \frac{\partial f_6}{\partial x_6} \delta x_6
\end{cases}
$$

$$
\delta Y = \frac{\partial F}{\partial X} \delta X = J(X) \delta X
$$

关节速度 $\dot{\Phi}$ 末端速度$v$

- 雅可比矩阵的行数是自由度，列数是关节数量。

- 雅可比矩阵是时变的
- 雅可比矩阵可以看作x的速度空间向y的速度空间做映射

$$
v = J(\Phi) \dot{\Phi}
$$



### 几何雅可比

#### 向外迭代法
知道了这样的变换方法，就可以从连杆0，变换到连杆N，一个个地计算速度和角速度

向外迭代法是计算机器人几何雅可比矩阵的方法之一

#### 向量积构造法

计算每一个关节对于连杆N速度的贡献

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250314234911486.png)

- 若第 $i$ 个关节为平动型关节，则：$v_N^{(i)} = d_i \hat{Z}_i$,$\omega_N^{(i)} = 0$
- 若第 $i$ 个关节为转动型关节，则：$v_N^{(i)} = \dot{\theta}_i \hat{Z}_i \times (O_N - O_i)$,$\omega_N^{(i)} = \dot{\theta}_i \hat{Z}_i$

> 为什么要叉乘：**类似于“力矩”中“矩”的概念**

!!! question "这里问一下"

以机器人每个关节均为转动型关节为例构造几何雅可比矩阵。

定义笛卡尔速度向量 $v_N = \begin{pmatrix} v_N \\ \omega_N \end{pmatrix} \in \mathbb{R}^6$ 和关节空间角速度向量 $\dot{\Phi} = \begin{pmatrix} \dot{\theta}_1 \\ \dot{\theta}_2 \\ \vdots \\ \dot{\theta}_N \end{pmatrix} \in \mathbb{R}^N$，则：

$$
v_N = \begin{pmatrix} \hat{Z}_1 \times (O_N - O_1) & \hat{Z}_2 \times (O_N - O_2) & \cdots & \hat{Z}_{N-1} \times (O_N - O_{N-1}) & 0 \\ \hat{Z}_1 & \hat{Z}_2 & \cdots & \hat{Z}_{N-1} & \hat{Z}_N \end{pmatrix} \dot{\Phi}\\
= \mathbf{J(\Phi)}\dot{\Phi}
$$

此处，$J(\Phi) \in \mathbb{R}^{6 \times N}$ 即为雅可比矩阵。



### 不同frame变换

$$
^i\boldsymbol{J}(\boldsymbol{\Phi})=\begin{pmatrix}{}_0^i\boldsymbol{R}&0\\0&{}_0^i\boldsymbol{R}\end{pmatrix}\boldsymbol{J}(\boldsymbol{\Phi})
$$


### 求逆

逆微分求解：已知

- 满秩矩阵，直接求解雅可比矩阵的逆

- 对于不满秩的矩阵来说，求取伪逆


对于机械臂来说，操作空间维度相当于$m$，关节数目相当于$n$（自变量数目）


=== "左逆"

    仅当 $m \geq n$ 时("Tall matrix")，说明这个时候方程的数目大于未知数的个数，方程是过定(overdetermined)的。矩阵 $A$ 可能有**左逆矩阵** 
    
    $$
    A^\dagger_L = \left(A^HA\right)^{-1}A^H
    $$
    
    左逆列满秩的时候一定存在
    
    **超定方程最小二乘解**



=== "右逆"

    仅当 $m \leq n$ 时("fat matrix")，方程数目小于未知数的个数，方程式欠定的。矩阵 $A$ 可能有**右逆矩阵** 
    
    $$
    A^\dagger_R = A^H\left(AA^H\right)^{-1}
    $$
    
    右逆行满秩的时候一定存在
    
    欠定方程最小范数解



> 关于最小二乘和最小范数解的证明可以看[线性方程组的最小二乘解和最小范数解 - 一以知行](https://zhuanlan.zhihu.com/p/503664717)

 

### 奇异性

奇异位形：无法通过关节变量速度实现要求的末端速度


对于一般机器人，奇异位形为令雅可比矩阵 $J$ 不满秩的 $\Phi$ 值所构成的位形，（$N$是机器人关节数目）时

$$
\text{rank}(J(\Phi) < \min(m, N)
$$


不同情况下的奇异点的判断条件为：

1. **无冗余 ($m = N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不可逆，即 $\det(J(\Phi)) = 0$。
2. **冗余 ($m < N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不行满秩，即 $\text{rank}(J(\Phi)) < m$。（可能有最小范数解）
3. **欠驱动 ($m > N$)**: 在此 $\Phi$ 时 $J(\Phi)$ 不列满秩，即 $\text{rank}(J(\Phi)) < N$。（可能有最小二乘解）



- 奇异位形是机器人的构型决定的，是机器人的固有特征
- 接近奇异位形的时候，存在机器人末端在工作空间中的微小速度导致关节空间产生过大速度



**边界奇异性**: 工作空间边界的奇异位形。出现在机器人完全展开或者收回使得末端执行器处于或非常接近工作空间边界的情况。

**内点奇异性**: 工作空间内部的奇异位形。出现在远离工作空间的边界，通常是由于两个或两个以上的关节轴线共线引起的。





可操作度：


!!! note "二次型与椭圆"

    二次型对应椭球体。 椭球的轴沿着$A$的特征向量，半长轴长度是$A$特征值倒数的开方


    **椭圆的标准方程：** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$。其中，椭圆的长轴长度为 $2a$，短轴长度为 $2b$。

    **矩阵形式：**

    $$
    \begin{bmatrix} x \\ y \end{bmatrix}^T \begin{bmatrix} \frac{1}{a^2} & 0 \\ 0 & \frac{1}{b^2} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = x^T A x = 1
    $$


    **特征值与特征向量：**

    矩阵 $A$ 的特征值为：$\lambda_1 = \frac{1}{a^2}, \quad \lambda_2 = \frac{1}{b^2}$，特征值则表示了半长轴和半短轴长度平方的倒数。 


    对应的归一化特征向量为：$\mu_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad \mu_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$，表示了椭圆的长轴和短轴的方向



假设机器人有 $N$ 个关节，末端速度空间的维数为 $m$，要求 $N \geq m$，则 $m \times N$ 维雅可比矩阵 $J$ 的奇异值分解为：


$$
J = U \Sigma V^T
$$


其中，$\Sigma$ 是 $m \times N$ 维矩阵，其主对角线外的元素均为零，主对角线上的每个元素为 $J$ 的奇异值 $\sigma_i = \sqrt{\lambda_i(JJ^T)} (i = 1, \cdots, m)$，且 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_m \geq 0$；$U$ 和 $V$ 分别为 $m$ 维和 $N$ 维正交矩阵，且 $U$ 由矩阵 $JJ^T$ 的特征向量 $u_i (i = 1, \cdots, m)$ 张成，$V$ 由矩阵 $J^TJ$ 的特征向量 $v_i (i = 1, \cdots, N)$ 张成。由此得到：


$$
v_e^T (J J^T)^{-1} v_e = (U^T v_e)^T \Sigma^{-2} (U^T v_e)
$$


此时，$\Sigma^{-2} = \text{diag}(\sigma_1^{-2}, \sigma_2^{-2}, \cdots, \sigma_m^{-2})$ 为 $m$ 维对角矩阵。记 $\alpha = U^T v_e$

$$
v_e^T (J J^T)^{-1} v_e - \alpha^T \Sigma^{-2} \alpha = \sum_{i=1}^m \frac{\alpha_i^2}{\sigma_i^2} \leq 1
$$


是一个标准的椭球体方程，表明机器人此位形的可操作椭球体的轴由向量 $\sigma_i u_i$ 给出。

机器人关节速度取单位速度时，可操作椭球体轴的长度越大，在该轴方向上，所得到的末端速度可以越大，表明在该方向上运动能力越强；反之，轴的长度越小，在该轴方向上，所得到的末端速度被限制得越小，表明在该方向上运动能力越弱。因此，机器人位形的可操作椭球体描述了机器人改变末端位姿的能力。

定义可操作度，用来衡量机器人位形与奇异位形之间的距离

$$
\kappa(\boldsymbol{\Phi})=\sigma_1\sigma_2\cdots\sigma_m=\sqrt{\det(\boldsymbol{J}(\boldsymbol{\Phi})\boldsymbol{J}^\mathrm{T}(\boldsymbol{\Phi}))}
$$


特别的，当雅可比矩阵可逆的时候 $\kappa(\boldsymbol{\Phi})=\mid\det(\boldsymbol{J}(\boldsymbol{\Phi}))\mid$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250314222953648.png)


### 几何雅可比和分析雅可比
> 参考文献：[机械臂的几何雅可比和分析雅可比有什么区别？ - 知乎](https://www.zhihu.com/question/67687838)


| 符号 | 含义 |
|------|------|
| $q$ | 关节角度向量，表示机器人各个关节的角度值 |
| $\dot{q}$ | 关节速度向量，表示关节变量的时间变化率 |
| $p_e$ | 末端执行器的位置向量 |
| $\dot{p}_e$ | 末端执行器的位置变化率（平移速度） |
| $\phi_e$ | 末端执行器的姿态（通常用欧拉角表示） |
| $\dot{\phi}_e$ | 末端执行器的**姿态变化率（旋转速度）** |
| $\omega$ | 角速度向量，表示**绕各个轴**的旋转速度 |
| $v$ | 线速度向量，表示在笛卡尔空间中的平移速度 |










**Analytical Jacobians**：
- 在笛卡尔坐标系下，它得到的“角速度”是选择的表示末端方向的角度的时间导数。
- 表示的是机器人姿态的变化。这个姿态是自己定义的，它取决于你的坐标系。

$$
\begin{align*}
\dot{x} &= \frac{d}{dt}(x, y, z, \phi, \theta, \psi) = \begin{bmatrix} \frac{dx}{dt} & \frac{dy}{dt} & \frac{dz}{dt} & \frac{d\phi}{dt} & \frac{d\theta}{dt} & \frac{d\psi}{dt} \end{bmatrix}^T\\
&= \begin{bmatrix}
\dot{P} \\
\dot{\phi}
\end{bmatrix}= J_A(q) \dot{q}
\end{align*}
$$


**Geometrical Jacobians**：
- 获得的“角速度”是绕旋转轴的速度。得到的是关节空间速度与末端力矩之间的映射关系。

$$
\begin{align*}
\dot{x} &= \begin{bmatrix} \frac{dx}{dt} & \frac{dy}{dt} & \frac{dz}{dt} & \omega_x & \omega_y & \omega_z \end{bmatrix}^T\\
&= \begin{bmatrix}
\dot{P} \\
\dot{\omega}
\end{bmatrix}= J(q) \dot{q}
\end{align*}
$$

其中，$\omega_x$、$\omega_y$、$\omega_z$ 表示绕 $x$、$y$、$z$ 轴的角速度。


**转化关系**

$$
J(\Phi) \dot{\Phi} = \begin{pmatrix} v \\ \omega \end{pmatrix} = \begin{pmatrix} \dot{P} \\ B_a(\Psi)\dot{\Psi} \end{pmatrix} = \begin{pmatrix} I & 0 \\ 0 & B_a(\Psi) \end{pmatrix} \begin{pmatrix} \dot{P} \\ \dot{\Psi} \end{pmatrix}= \begin{pmatrix} I & 0 \\ 0 & B_a(\Psi) \end{pmatrix} J_a(\Phi) \dot{\Phi}
$$

所以，分析雅可比矩阵 $J_a(\Phi)$ 与几何雅可比矩阵 $J(\Phi)$ 的关系为：

$$
J_a(\Phi) = \begin{pmatrix} I & 0 \\ 0 & B_a^{-1}(\Psi) \end{pmatrix} J(\Phi) = T_a J(\Phi)
$$


刚体角速度$\omega$和欧拉角速率$\dot{\Psi}$之间的关系

$$
\omega = \begin{pmatrix}
0 & -s\alpha & c\alpha s\beta \\
0 & c\alpha & s\alpha s\beta \\
1 & 0 & c\beta
\end{pmatrix} \dot{\Psi} = B_a(\Psi) \dot{\Psi}
$$

??? note "证明"

    若刚体姿态矩阵为 $R = \begin{pmatrix}    r_{11} & r_{12} & r_{13} \\    r_{21} & r_{22} & r_{23} \\    r_{31} & r_{32} & r_{33}\end{pmatrix}$ ,刚体角速度 $\omega$ 为：$\omega = \begin{pmatrix}    \omega_x \\    \omega_y \\    \omega_z    \end{pmatrix}$

    $$
    \dot{R} R^T = S\\
    \begin{pmatrix}
    \dot{r}_{11} & \dot{r}_{12} & \dot{r}_{13} \\
    \dot{r}_{21} & \dot{r}_{22} & \dot{r}_{23} \\
    \dot{r}_{31} & \dot{r}_{32} & \dot{r}_{33}
    \end{pmatrix}
    \begin{pmatrix}
    r_{11} & r_{21} & r_{31} \\
    r_{12} & r_{22} & r_{32} \\
    r_{13} & r_{23} & r_{33}
    \end{pmatrix}=\begin{pmatrix}
    0 & -\omega_z & \omega_y \\
    \omega_z & 0 & -\omega_x \\
    -\omega_y & \omega_x & 0
    \end{pmatrix}
    $$

    对应元素相等可以得到

    $$
    \omega_x = \dot{r}_{31} r_{21} + \dot{r}_{32} r_{22} + \dot{r}_{33} r_{23}\\
    \omega_y = \dot{r}_{11} r_{31} + \dot{r}_{12} r_{32} + \dot{r}_{13} r_{33}\\
    \omega_z = \dot{r}_{21} r_{11} + \dot{r}_{22} r_{12} + \dot{r}_{23} r_{13}
    $$


    以 $z-y-z$ 欧拉角表示刚体在基坐标系中的姿态为例，此时：

    $$
    R = R_{z'y'z'}(\alpha, \beta, \gamma) = R_z(\alpha) R_y(\beta) R_z(\gamma)= \begin{pmatrix}
    c\alpha & -s\alpha & 0 \\
    s\alpha & c\alpha & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
    c\beta & 0 & s\beta \\
    0 & 1 & 0 \\
    -s\beta & 0 & c\beta
    \end{pmatrix}
    \begin{pmatrix}
    c\gamma & -s\gamma & 0 \\
    s\gamma & c\gamma & 0 \\
    0 & 0 & 1
    \end{pmatrix}
    $$



    记 $z-y-z$ 欧拉角表示为 $\Psi = (\alpha, \beta, \gamma)^T$，欧拉角速率为 $\dot{\Psi} = (\dot{\alpha}, \dot{\beta}, \dot{\gamma})^T$，

    $$
    \begin{align*}
    \omega_x &= \dot{r}_{31} r_{21} + \dot{r}_{32} r_{22} + \dot{r}_{33} r_{23}\\
    &= \left( \frac{\partial r_{31}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{31}}{\partial \beta} \dot{\beta} + \frac{\partial r_{31}}{\partial \gamma} \dot{\gamma} \right) r_{21} + \left( \frac{\partial r_{32}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{32}}{\partial \beta} \dot{\beta} + \frac{\partial r_{32}}{\partial \gamma} \dot{\gamma} \right) r_{22} + \left( \frac{\partial r_{33}}{\partial \alpha} \dot{\alpha} + \frac{\partial r_{33}}{\partial \beta} \dot{\beta} + \frac{\partial r_{33}}{\partial \gamma} \dot{\gamma} \right) r_{23}\\
    &= \begin{pmatrix} 0 & -s\alpha & c\alpha s\beta \end{pmatrix} \dot{\Psi}
    \end{align*}
    $$

    同理可得：

    $$
    \begin{align*}
    \omega_y = \dot{r}_{11} r_{31} + \dot{r}_{12} r_{32} + \dot{r}_{13} r_{33} = \begin{pmatrix} 0 & c\alpha & s\alpha s\beta \end{pmatrix} \dot{\Psi}\\
    \omega_z = \dot{r}_{21} r_{11} + \dot{r}_{22} r_{12} + \dot{r}_{23} r_{13} = \begin{pmatrix} 1 & 0 & c\beta \end{pmatrix} \dot{\Psi}
    \end{align*}
    $$



### 数值法解方程

这里主要用到的是**牛顿法**

一句话简述：从一个起始解开始，使用切线逐步逼近交点

$$
x_{n+1} = x_n - J(x_n)^{-1} f(x_n)
$$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250313094528065.png)

!!! note "为什么这么写？"
    写出泰勒展开，忽略二次高阶项. 相当于做了一条切线，再求这个切线和x轴的交点，得到新一轮的x

    $$
    f(x) = f(x_0) + f'(x_0)(x - x_0) = 0
    $$
    
    > **参考资料**
    > [牛顿迭代法 - OI Wiki](https://oi-wiki.org/math/numerical/newton/)
    > [牛顿法原理与应用 - CSDN博客](https://blog.csdn.net/sinat_29244519/article/details/101872198)


## 静力学

|符号|含义|补充|
|---|---|---|
||||


**力的大小：** 衡量力对平动的作用效果

**力矩：** 衡量力对转动的作用效果

**力偶：** 等大反向不共线的力，所有旋转都可以等效看作是力偶的作用。也就是说，力形成力偶，才使得物体发生了旋转。

**力偶矩：** 用来描述物体力偶的作用效果

**物体平衡的条件：** 合力为0，合力矩为0

> 参考资料<br>
> [力矩、力偶矩、弯矩的区别是什么？ - 知乎](https://www.zhihu.com/question/23371844?sort=created)<br>
> [力矩的本质是什么？与力偶有什么关系？ - 知乎](https://www.zhihu.com/question/398334639/answer/1258696609)<br>


**力的平移原理**


- 引理1：作用在刚体上的力沿着其作用线移动后，力对刚体作用效应不变
- 引理2：在刚体上增加一组平衡力系，不改变原力系对刚体的作用效应

所以如果想将力平移，那么可以在B点增加一组平衡力系，使得B点的力和A点的力相同，方向相反。这个时候把$F$和$F_2$视为一组力偶。

可以看作力$F$平移到$F_1$之后，刚体受到$F_1$和力偶矩$M = F \times r_{AB}$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250313095306008.png)
> 图源 [力平移定理与平衡 - CSDN博客](https://blog.csdn.net/weixin_43989965/article/details/120471367)






### 操作臂的静力传递

- 传递方向：从末端向下传递
- 方式：先固定，写出各连杆的平衡关系，再加外力，写出各关节轴需要加多少力
> 忽略重力

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250313114049005.png)

$$
\begin{align*}
^i f_i = ^i f_{i+1}\\
^i n_i = ^i n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i+1}
\end{align*}
$$

加上坐标系变换后

$$
\begin{align*}
^i f_i = ^{i}_{i+1}R ^{i+1} f_{i+1}\\
^i n_i = ^{i}_{i+1}R^{i+1} n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i+1}
\end{align*}
$$


!!! note "转动型关节需要考虑施加多少力矩,平动型关节需要考虑施加多少力.需要对(力，力矩)向量进行正交分解"


**转动型关节$i$**

$f_i$ 不是主动力而是约束力，它阻止连杆 $i$ 作直线运动；$n_i$ 阻止连杆 $i$ 作旋转运动。在 $\{i\}$ 中对 $n_i$ 进行正交分解，可得到 1 个沿 $\hat{z}_i$ 的力矩向量和 1 个垂直于 $\hat{z}_i$ 的力矩向量，垂直于 $\hat{z}_i$ 的力矩向量是约束力矩，沿 $\hat{z}_i$ 的力矩向量是主动力矩，主动力矩需由关节 $i$ 的旋转驱动器提供，主动力矩可表示为 $\tau_i \hat{z}_i$，其中

$$
\tau_i = |n_i| \cos \theta = |n_i| |\hat{z}_i| \cos \theta = n_i^{\mathrm{T}} \hat{z}_i
$$

**平动型关节$i$**

$n_i$ 是约束力矩。在 $\{i\}$ 中对 $f_i$ 进行正交分解，得到 1 个主动力和 1 个约束力，需由关节 $i$ 的直线驱动器提供的主动力表示为 $\tau_i \hat{z}_i$，其中

$$
\tau_i = f_i^{\mathrm{T}} \hat{z}_i
$$


!!! example "例子"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250313112419504.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250313112444810.png)
    > 课本习题


### 力域中的雅可比
笛卡尔力映射到关节上的力矩，不需要求解逆运动学

$$
\tau = J^T F 
$$

!!! note "证明方法 - 虚功原理"
    以机器人在末端笛卡儿空间所做的功与在关节空间所做的功相等，即

    $$ 
    F^T \delta x = \tau^T \delta \Phi 
    $$
    
    > **注：力矩做功是力矩和角位移的积分**
    
    式中，$F$ 是末端作用于外部的 $6 \times 1$ 维笛卡儿力-力矩向量；$\delta x$ 是末端的 $6 \times 1$ 维无穷小笛卡儿位移向量；$\tau$ 是 $6 \times 1$ 维关节力矩向量；$\delta \Phi$ 是 $6 \times 1$ 维无穷小关节位移向量。
    
    由雅可比矩阵的定义有（速度空间的映射）
    
    $$ 
    \delta x = J \delta \Phi 
    $$


    $$ 
    F^T J \delta \Phi = \tau^T \delta \Phi 
    $$


    上式对所有的 $\delta \Phi$ 均成立，因此有
    
    $$ 
    F^T J = \tau^T 
    $$
    
    同取转置
    
    $$ 
    \tau = J^T F 
    $$

## 题型


### 基础公式记忆


**z-y-x 欧拉角** 公式


$$
\begin{align}
R_{z,y,x}(\alpha,\beta,\gamma) = \begin{pmatrix}
c\alpha c\beta & c\alpha s\beta s\gamma-s\alpha c\gamma & c\alpha s\beta c\gamma+s\alpha s\gamma \\
s\alpha c\beta & s\alpha s\beta s\gamma+c\alpha c\gamma & s\alpha s\beta c\gamma-c\alpha s\gamma \\
-s\beta & c\beta s\gamma & c\beta c\gamma
\end{pmatrix}
\end{align}
$$


MDH建模下，坐标系**齐次变换矩阵**


$^{i-1}_i \!T$ 表示坐标系 $\{i-1\}$ 到坐标系 $\{i\}$ 的变换矩阵，i从1开始

$$
^{i-1}_i \!T = \begin{pmatrix}
\cos \theta_i & -\sin \theta_i & 0 & a_{i-1} \\
\sin \theta_i \cos \alpha_{i-1} & \cos \theta_i \cos \alpha_{i-1} & -\sin \alpha_{i-1} & -\sin \alpha_{i-1} d_i \\
\sin \theta_i \sin \alpha_{i-1} & \cos \theta_i \sin \alpha_{i-1} & \cos \alpha_{i-1} & \cos \alpha_{i-1} d_i \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

**几种常见的齐次变换矩阵**



**几种方法对比**

| 方法               | 计算量                           | 需要求解                     | 注意点                                                                 |
|--------------------|----------------------------------|-----------------------------|----------------------------------------------------------------------|
| **运动学方程微分** | 中等                             | 正运动学方程 $^0_nT$         | 确保正确求导，注意矩阵维度一致性                                      |
| **向量积构造法**   | 较低                             | 各关节轴的单位向量 $\hat{Z}_i$ 和原点位置 $O_i$ | $\hat{Z}_i$ 和 $O_i$ 必须在世界坐标系下表示，注意叉乘方向             |
| **速度传递**       | 较高                             | 各连杆的旋转矩阵 $^{i+1}_iR$ 和位置向量 $^iP_{i+1}$ | 确保旋转矩阵和位置向量的正确性，注意旋转矩阵的转置操作                 |
| **力传递**         | 较高                             | 各连杆的旋转矩阵 $^{i+1}_iR$ 和位置向量 $^iP_{i+1}$ | 求解的雅可比需要转置，需要乘R转回全局坐标系下   |

### 求雅可比矩阵 - 运动学方程微分

由正运动学，求解 $^0_nT$

$$
^0_nT = \begin{pmatrix} ^0_nR & ^0_nP \\ 0 & 1 \end{pmatrix}
$$

对上式求导，得到

$$
P' = \frac{d P}{d t} = J(\theta) \dot{\theta}
$$

即可得到雅可比矩阵

### 求雅可比矩阵 - 向量积构造法


$O_i$是坐标系${i}$的原点位置，$\hat{Z}_i$是转轴单位向量，这里要特别注意，$\hat{Z}_i$需要在世界坐标系下表出

- 若第 $i$ 个关节为平动型关节，则：$v_N^{(i)} = d_i \hat{Z}_i \quad \omega_N^{(i)} = 0$
- 若第 $i$ 个关节为转动型关节，则：$v_N^{(i)} = \dot{\theta}_i \hat{Z}_i \times (O_N - O_i) \quad \omega_N^{(i)} = \dot{\theta}_i \hat{Z}_i$



### 求雅可比矩阵 - 速度传递

公式不要记错，这里要注意 $^{i+1}_i\!R$ 需要使用 $^{i}_{i+1}\!R^T$ 进行求解

**转动型关节**

角速度：连杆 i+1 针对世界坐标系角速度在{i+1}坐标系的表示

$$
^{i+1}\!\omega_{i+1} = ^{i+1}_i\!R {^i\omega_i} + \dot{\theta}_{i+1} {}^{i+1}\!\hat{Z}_{i+1}\\
$$

> 其中，$\hat{Z}_{i+1}$ 是轴 $i+1$在 ${i+1}$ 中的表示；${\theta}_{i+1}$ 是转动型关节 $i+1$ 的关节转速。

线速度：连杆i+1 针对世界坐标系线速度在{i+1}坐标系的表示

$$
{}^{i+1}\!v_{i+1} = {^{i+1}_iR} (^iv_i + ^i\omega_i \times {^iP_{i+1}})
$$

> 连杆的长度隐含在了 $^iP_{i+1}$ 叉乘项当中

**平动型**

角速度：不变

$$
^{i+1}\omega_{i+1} = _i^{i+1}R {^i\omega_i}
$$


线速度：要加一个在轴线上的速度

$$
^{i+1}v_{i+1} = _i^{i+1}R (^iv_i + ^i\omega_i \times ^iP_{i+1}) + \dot{d_{i+1}} \hat{Z}_{i+1}
$$




### 求雅可比矩阵 - 力传递


$$
\begin{align*}
^i f_i = ^{i}_{i+1}R ^{i+1} f_{i+1}\\
^i n_i = ^{i}_{i+1}R^{i+1} n_{i+1} + ^{i}P_{i+1} \times ^{i}f_{i}
\end{align*}
$$


转动型关节需要考虑施加多少力矩,平动型关节需要考虑施加多少力.需要对(力，力矩)向量进行正交分解



**转动型关节$i$**

$$
\tau_i = |n_i| \cos \theta = |n_i| |\hat{z}_i| \cos \theta = n_i^{\mathrm{T}} \hat{z}_i
$$

**平动型关节$i$**

$$
\tau_i = f_i^{\mathrm{T}} \hat{z}_i
$$


将式子写成矩阵的形式，即可得到

$$ 
\tau = J^T F 
$$

取转置，得到 $\boldsymbol{^iJ}$，是末端坐标系下的雅可比矩阵

但是要注意到，这里的雅可比矩阵需要转到全局下


$$
\boldsymbol{J}(\boldsymbol{\Phi})= ^0_i\boldsymbol{R} \boldsymbol{^iJ}(\boldsymbol{\Phi})
$$






