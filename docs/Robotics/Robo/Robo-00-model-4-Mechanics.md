# 04 | 速度与静力
[机器人学导论---第五章 速度和静力（一）5.1-5.11（好难） - 知乎](https://zhuanlan.zhihu.com/p/155829972)



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
{}^A({}^B\mathbf{V}_Q) = {}^A_B\mathbf{R} {}^B\mathbf{V}_Q = \frac{d}{dt} {}^A_B\mathbf{Q} = \lim_{\Delta t \to 0} {}^A_B\mathbf{R}(t) \left( \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t} \right)
$$

坐标系原点相对于世界坐标系{U}的速度:$\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}$


!!! note "需要注意，\( {}^A({}^B\mathbf{V}_Q) \) 不同于 \( {}^A\mathbf{V}_Q \)"

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

**向外迭代法**

知道了这样的变换方法，就可以从连杆0，变换到连杆N，一个个地计算速度和角速度



## 雅可比

复杂变换在某个局部点可以看作线性变换

【（干货）《雅可比矩阵是什么东西》3Blue1Brown，搬自可汗学院。 【自制中文字幕】】 【精准空降到 03:53】 https://www.bilibili.com/video/

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=79626296&bvid=BV1NJ411r7ja/?share_source=copy_web&vd_source=1ce3320d605852426ce5ccfc9b31eb50&t=233&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=450px height=600px></iframe>



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

$$
v = J(\Phi) \dot{\Phi}
$$



### 几何雅可比





- 向外迭代法是计算机器人几何雅可比矩阵的方法之一



### 求逆


### 奇异性

### 分析雅可比


## 静力学

### 操作臂的静力

### 力域中的雅可比