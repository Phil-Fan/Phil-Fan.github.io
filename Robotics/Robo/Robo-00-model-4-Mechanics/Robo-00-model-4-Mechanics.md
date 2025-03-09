# 04 | 速度与静力
[机器人学导论---第五章 速度和静力（一）5.1-5.11（好难） - 知乎](https://zhuanlan.zhihu.com/p/155829972)


讲关节空间速度映射到笛卡尔空间速度，通过雅可比矩阵描述

## 时变位姿

[三维空间角速度、线速度表示及推导（旋转矩阵求导）（李群李代数引入） - 知乎](https://zhuanlan.zhihu.com/p/680478526)



同维矢量的微分表示

矢量 \( {}^B\mathbf{Q} \) 的微分表示为如下同维矢量：

$$
{}^B\mathbf{V}_Q = \frac{d}{dt} {}^B\mathbf{Q} = \lim_{\Delta t \to 0} \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t}
$$

描述点的位置矢量与速度矢量

若 \( {}^B\mathbf{Q} \) 是描述某个点的位置矢量，该点关于{B}的速度是 \( {}^B\mathbf{V}_Q \)。

像其他矢量一样，速度矢量 \( {}^B\mathbf{V}_Q \) 可在任意坐标系中描述(相当于在B的原点建立一个和B固连的，与A姿态相同的坐标系)

$$
{}^A({}^B\mathbf{V}_Q) = {}^A_B\mathbf{R} {}^B\mathbf{V}_Q = \frac{d}{dt} {}^A_B\mathbf{Q} = \lim_{\Delta t \to 0} {}^A_B\mathbf{R}(t) \left( \frac{{}^B\mathbf{Q}(t + \Delta t) - {}^B\mathbf{Q}(t)}{\Delta t} \right)
$$

!!! note "需要注意，\( {}^A({}^B\mathbf{V}_Q) \) 不同于 \( {}^A\mathbf{V}_Q \)"

    $$
    \begin{align*}
    {}^A\mathbf{V}_Q &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{Q}(t + \Delta t) - {}^A\mathbf{Q}(t)}{\Delta t}\\
    &= \lim_{\Delta t \to 0} \frac{{}^A\mathbf{P}_{BORG}(t + \Delta t) + {}^A_B\mathbf{R}(t + \Delta t) {}^B\mathbf{Q}(t + \Delta t) - {}^A\mathbf{P}_{BORG}(t) - {}^A_B\mathbf{R}(t) {}^B\mathbf{Q}(t)}{\Delta t}
    \end{align*}
    $$

经常讨论的是一个坐标系原点相对于世界坐标系{U}的速度，对于这种情况，定义一个缩写符号：

$$
\mathbf{v}_C = {}^U\mathbf{V}_{\text{CORG}}
$$

式中的点为坐标系{C}的原点。

特别注意符号的意义${}^A\mathbf{v}_C = {}^A_U\mathbf{R} \mathbf{v}_C = {}^A_U\mathbf{R} {}^U\mathbf{V}_{\text{CORG}} \neq {}^A\mathbf{V}_{\text{CORG}}$


### 坐标系线速度&角速度


### 刚体线速度&角速度

### 连杆间速度传递



## 雅可比

复杂变换在某个局部点可以看作线性变换

【（干货）《雅可比矩阵是什么东西》3Blue1Brown，搬自可汗学院。 【自制中文字幕】】 【精准空降到 03:53】 https://www.bilibili.com/video/

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=79626296&bvid=BV1NJ411r7ja/?share_source=copy_web&vd_source=1ce3320d605852426ce5ccfc9b31eb50&t=233&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=450px height=600px></iframe>

### 集合雅可比

### 求逆


### 奇异性

### 分析雅可比


## 静力学

### 操作臂的静力

### 力域中的雅可比