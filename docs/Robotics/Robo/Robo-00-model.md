# 机器人建模

!!! note "课程信息"
    - 名称：机器人建模与控制
    - 授课教师：zrh

要是讲解机械臂相关的知识，包括空间描述与变换（旋转矩阵、齐次变换矩阵、欧拉角、等效轴角、四元数）、正运动学（关节参数、改进DH参数）、逆运动学（解析法、数值法）、静力学、雅可比、动力学（拉格朗日方程、牛顿欧拉方程）、轨迹规划、控制（位置控制、力控制）等等



![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250217105608273.png)



## 空间描述与变换

位置和姿态总是成对出现的，我们将此组合称为坐标系。一个坐标系可以等价的用一个位置向量和一个旋转矩阵来描述。

- **位置**：用向量进行表示，左上标来描述具体的坐标系，例如$^A\!P$ 表明列向量$P$在坐标系$A$下定义的。
- **姿态**：物体上固定坐标系相对于参考坐标系的方位

### 数学基础

=== "向量点乘"
    两个向量 $r_{OP}$ 和 $r_{OQ}$ 的点乘(内积)可按下式计算:

    $$
    r_{OP} \cdot r_{OQ} 
    = ^AP \cdot ^AQ = ^AP^T \cdot ^AQ\\ 
    = (p_x \quad p_y \quad p_z)\begin{pmatrix}q_x\\q_y\\q_z\end{pmatrix} \\ 
    = p_xq_x + p_yq_y + p_zq_z
    $$

=== "向量叉乘"
    两个向量 $\vec{a}$ 和 $\vec{b}$ 的叉乘结果是一个新向量 $\vec{c}$:

    $$
    \vec{c} = \vec{a} \times \vec{b}= |a||b|\sin\theta
    $$

    方向遵循右手定则，垂直于这两个向量所在的平面。

    简单计算方法:

    - 把 $\vec{a}$ 和 $\vec{b}$ 写成下面的矩阵形式

    $$
    \begin{pmatrix}
    a_x & a_y & a_z & a_x & a_y & a_z \\
    b_x & b_y & b_z & b_x & b_y & b_z
    \end{pmatrix}
    $$

    - 去掉第一列和最后一列，剩下的3个2x2的矩阵（每次滑动1格子），计算行列式即可

### 平移变换 - 向量加法

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224145149274.png)

$$
^A\!P = ^B\!P + ^A\!P_{BORG}
$$

点本身没有移动，只是随着观察的参考系不同，其坐标表示也不同

### 旋转变换 - 旋转矩阵

**旋转矩阵**

把新坐标系下的单位向量用旧坐标系下的单位向量表示

> $^A_B\!R$ 表示由A坐标系到B坐标系的旋转矩阵

$$
^A_BR = \begin{bmatrix} ^A\!X_B & ^A\!Y_B & ^A\!Z_B \end{bmatrix} = \begin{bmatrix} r_{11} & r_{12} & r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33} \end{bmatrix}
$$

**性质**<br>
- 旋转矩阵是正交矩阵，即$^A_B\!R^T = ^A_B\!R^{-1} = ^B_A\!R$<br>
- 旋转矩阵的行列式为1，即$\det(^A_B\!R) = 1$<br>


**SO3**：Special Orthogonal Group 三维特殊正交群

$$
SO(3) = \left\{ 
\begin{pmatrix} 
r_{11} & r_{12} & r_{13} \\ 
r_{21} & r_{22} & r_{23} \\ 
r_{31} & r_{32} & r_{33} 
\end{pmatrix} 
\in \mathbb{R}^{3 \times 3} \mid 
\begin{pmatrix} 
r_{11} \\ 
r_{21} \\ 
r_{31} 
\end{pmatrix}^T 
\begin{pmatrix} 
r_{11} \\ 
r_{21} \\ 
r_{31} 
\end{pmatrix} = 1, 
\begin{pmatrix} 
r_{12} \\ 
r_{22} \\ 
r_{32} 
\end{pmatrix}^T 
\begin{pmatrix} 
r_{12} \\ 
r_{22} \\ 
r_{32} 
\end{pmatrix} = 1, 
\begin{pmatrix} 
r_{11} \\ 
r_{21} \\ 
r_{31} 
\end{pmatrix}^T 
\begin{pmatrix} 
r_{12} \\ 
r_{22} \\ 
r_{32} 
\end{pmatrix} = 0, 
\begin{pmatrix} 
r_{11} \\ 
r_{21} \\ 
r_{31} 
\end{pmatrix}^T 
\begin{pmatrix} 
r_{13} \\ 
r_{23} \\ 
r_{33} 
\end{pmatrix} = 0, 
\begin{pmatrix} 
r_{12} \\ 
r_{22} \\ 
r_{32} 
\end{pmatrix}^T 
\begin{pmatrix} 
r_{13} \\ 
r_{23} \\ 
r_{33} 
\end{pmatrix} = 0 
\right\}
$$

??? info "群"
    群 $(G, *)$ 是一个集合 $G$ 与一个二元运算 $*$ 的组合

    1. **封闭性（Closure）**：对于任意 $a, b \in G$，有 $a * b \in G$。
    2. **结合性（Associativity）**：对于任意 $a, b, c \in G$，有 $(a * b) * c = a * (b * c)$。
    3. **单位元（Identity Element）**：存在一个元素 $e \in G$，对于任意 $a \in G$，有 $a * e = e * a = a$。
    4. **逆元（Inverse Element）**：对于任意 $a \in G$，存在一个元素 $b \in G$，使得 $a * b = b * a = e$，其中 $e$ 是单位元。

- SO(3)是全体旋转矩阵的集合,任何一个旋转矩阵（对应于刚体的一个姿态）都属于$SO(3)$
- 旋转前后，2范数不变:$\|y\|^2 = y^T y = (Rx)^T Rx = x^T R^T R x = x^T x = \|x\|^2$



!!! tip "空间中确定一个旋转至少需要3个参数"
    SO(3)群有6个约束：两个单位向量（范数为1），两个单位向量正交，叉乘得到第三个单位向量
    
    所以自由度是3



**表示旋转**：源坐标系下的向量使用基向量以及坐标表示的，如果要转到目标坐标系下，那么就需要把基向量用目标坐标系的基向量表示（旋转矩阵）

$$
\begin{equation}
{}^A\!P = {}^A_B\!R \,{}^B\!P
\end{equation}
$$

> 记忆法则：消消乐，前面的矩阵的下标$A$消去了后面矩阵的上标$A$


### 旋转+平移变换 - 齐次变换矩阵

??? info "齐次坐标"
    > 没有什么问题是增加一个维度解决不了的，如果有，那就加二个
    
    **motivation:** 欧氏空间可以很好描述2D/3D，但是不能处理投影空间(平行线无法相交)

    **齐次坐标:** 增加额外变量$W$，用$n+1$维坐标表示$n$维坐标,把W归一化之后，相当于是一个向量

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224151848494.png)

    任何$N$维度齐次坐标，只要$W$不为0，都可以通过将每一个分量除以$W$来转换到 $W=1$的向量, 然后获得其$N-1$维的欧式空间的点值。(也就是在$W=1$的时候，齐次坐标兼容欧氏空间)

    而当$W=0$时，这个坐标表示无限x长的一个向量，通常表示$N-1$维的矢量。

    **无穷远:** 齐次坐标系统中可以用$W=0$来表示无穷远的点，即任何$(x,y,0)$表示无穷远的点。

将平移变换和旋转变换结合起来，应该怎么表示呢？

先在B点建立一个与A姿态相同的坐标系，再使用向量加法

$$
^A\!P = {}^A_B\!R \,{}^B\!P + {}^A\!P_{B}
$$

写成矩阵的形式

$$
\begin{bmatrix}
^AP \\
1
\end{bmatrix}=
\begin{bmatrix}
\begin{array}{c|c}
^AR & P_{B} \\ \hline
0 & 1
\end{array}
\end{bmatrix}
\begin{bmatrix}
^BP \\
1
\end{bmatrix}
$$

$$
^A\!P = {}^A_B\!T \,{}^B\!P
$$



其中，齐次变换矩阵

$$
^A_B\!T = \begin{bmatrix} ^A_B\!R & ^A\!P_B \\ 0 & 1 \end{bmatrix} \in \mathbb{R}^{4 \times 4}
$$

SE(3):Special Euclidean Group in 3 dimensions

$$
SE(3) = \left\{ 
    \begin{bmatrix} ^A_B\!R & ^A\!P_B \\ 0 & 1 \end{bmatrix} \middle| ^A_B\!R \in SO(3), ^A\!P_B \in \mathbb{R}^3 
\right\}
$$

**刚体的不同位姿与$SE(3)$中的不同齐次变换矩阵是一一对应的**

经旋转和平移后的**齐次变换矩阵**与一个坐标系相对于参考坐标系经旋转和平移后的齐次变换矩阵是相同的。


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224155556956.png)

$$
\begin{align}
^A_B\!T &= 
\begin{bmatrix} 
\begin{array}{c|c}
^A_B\!R & ^A\!O_B \\ \hline
0 &  1 
\end{array}
\end{bmatrix}
\\
^B_A\!T = 
\begin{bmatrix} 
\begin{array}{c|c}
^B_A\!R & ^B\!O_A \\ \hline
0 &  1 
\end{array}
\end{bmatrix} &= 
\begin{bmatrix} 
\begin{array}{c|c}
^B_A\!R & -^B_A\!R \cdot ^A\!O_B \\ \hline
0 & 1  
\end{array}
\end{bmatrix}
\end{align}
$$

$$
^A_B\!T \cdot ^B_A\!T = I
$$

### 欧拉角 - 三个轴次序旋转

通过将三个基本旋转（Roll, Pitch, Yaw）按特定顺序组合来表示任意的旋转。

**正方向**：按照右手螺旋确定

=== "共有12种欧拉角"
    - 非对称型：3个轴的排列组合：$^3_3A = 3! = 6$
    - 对称型：zxz, xyz, yxy, yzy, xzx, xyx
=== "优点"
    - 直观易懂,便于人类理解
    - 只需要3个参数就能表示旋转
    - 在航空航天等领域应用广泛
=== "缺点"
    - 存在万向节死锁(Gimbal Lock)问题
    - 计算复杂度较高
    - 不同旋转顺序会得到不同结果



!!! note "记忆方法" 
    首先旋转轴必有一个1<br>
    $\cos$ 一定在主对角线<br>
    $\sin$ 的符号不同y的负号在左下角，xz的负号在右上角

=== "桶滚 `roll`"
    ![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20190410212347423.gif)

    x轴不变，滚动（Roll)的旋转矩阵：

    $$
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & \cos\phi & -\sin\phi \\
    0 & \sin\phi & \cos\phi
    \end{bmatrix}
    $$

=== "俯仰 `pitch`"
    ![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20190410212338361.gif)

    y轴不变，俯仰（Pitch)的旋转矩阵：

    $$
    \begin{bmatrix}
    \cos\theta & 0 & \sin\theta \\
    0 & 1 & 0 \\
    -\sin\theta & 0 & \cos\theta
    \end{bmatrix}
    $$

=== "偏摆 `yaw`"
    ![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20190410212324456.gif)

    z轴不变，偏摆（Yaw）的旋转矩阵：

    $$
    \begin{bmatrix}
    \cos\psi & -\sin\psi & 0 \\
    \sin\psi & \cos\psi & 0 \\
    0 & 0 & 1
    \end{bmatrix}
    $$

    其中，$\phi$表示滚动角，$\theta$表示俯仰角，$\psi$表示偏摆角。这些矩阵分别表示了绕X轴、Y轴和Z轴的旋转。






z-y-x欧拉角:

$$
\begin{align}
R_{z,y,x}(\alpha,\beta,\gamma) &= \begin{pmatrix}
\cos\alpha & -\sin\alpha & 0 \\
\sin\alpha & \cos\alpha & 0 \\
0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
\cos\beta & 0 & \sin\beta \\
0 & 1 & 0 \\
-\sin\beta & 0 & \cos\beta
\end{pmatrix}
\begin{pmatrix}
1 & 0 & 0 \\
0 & \cos\gamma & -\sin\gamma \\
0 & \sin\gamma & \cos\gamma
\end{pmatrix} \\
&= \begin{pmatrix}
\cos\alpha\cos\beta & \cos\alpha\sin\beta\sin\gamma-\sin\alpha\cos\gamma & \cos\alpha\sin\beta\cos\gamma+\sin\alpha\sin\gamma \\
\sin\alpha\cos\beta & \sin\alpha\sin\beta\sin\gamma+\cos\alpha\cos\gamma & \sin\alpha\sin\beta\cos\gamma-\cos\alpha\sin\gamma \\
-\sin\beta & \cos\beta\sin\gamma & \cos\beta\cos\gamma
\end{pmatrix}
\end{align}
$$


$\forall R \in SO(3)$可用$R_{z,y,x}(\alpha, \beta, \gamma)$表示出来




#### 万向节死锁（Gimbal Lock）

  
非对称型欧拉角：

- 中间的旋转角在$\left[ -\frac{\pi}{2}, \frac{\pi}{2}\right]$的时候，可以求出唯一对应
- 如果不在$\left[ -\frac{\pi}{2}, \frac{\pi}{2}\right]$，则有无穷解
  
对称型欧拉角

- 当 $0 < \beta < \pi$ 时，类比可得取唯一一欧拉角或固定角的公式；
- 若 $\beta = 0$ 或 $\beta = \pi$，有无穷组欧拉角解和固定角解，只能确定 $a + \gamma$ 或者 $\alpha - \gamma$ 的值

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=771397545&bvid=BV1Nr4y1j7kn&cid=788925183&p=1&autoplay=0&t=40" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>


对欧拉角的变换是有序的,欧拉角只记录结果，不记录过程

欧拉角描述相对于初始状态的变换，只和最终状态有关，与过程无关。（外边的轴转动会带动里面的轴转动）

欧拉角描述的**不是转动过程**，而是一个**变换**

!!! example "例子"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224203714801.png)

    比如这个xyz欧拉角，表述的操作顺序是x-y-z,假设y轴的欧拉角参数是90度。

    物体将先绕x旋转（初始的x），再绕y旋转90，最后绕z旋转（这个z和初始的x轴其实已经重合了）。

    所以理解的关键是要明白，欧拉角描述的**是一个变换**，而不是一个连续的转动过程。**后面的变换使用的是前面变换的坐标系。**


!!! note "命题 $R_z(\pm \pi + \alpha) R_y(\pm \pi - \beta) R_x(\pm \pi + \gamma) = R_z(\alpha) R_y(\beta) R_x(\gamma)$"

    **证明**
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224165627208.png)


    **定义集合** 记集合：

    $$
    \mathbb{Q} = \left( -\pi, -\frac{\pi}{2} \right] \cup \left[ \frac{\pi}{2}, \pi \right]
    $$

    **定义函数** 
    
    令函数 $f: \mathbb{Q} \to \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$，定义为：

    $$
    f(\beta) = 
    \begin{cases} 
    -\pi - \beta, & \text{当 } \beta \in \left( -\pi, -\frac{\pi}{2} \right) \\
    \pi - \beta, & \text{当 } \beta \in \left[ \frac{\pi}{2}, \pi \right]
    \end{cases}
    $$

    以及函数 $g: (-\pi, \pi] \to (-\pi, \pi]$，定义为：

    $$
    g(\alpha) = 
    \begin{cases} 
    \pi + \alpha, & \text{当 } \alpha \in (-\pi, 0] \\
    -\pi + \alpha, & \text{当 } \alpha \in (0, \pi]
    \end{cases}
    $$

    **命题**<br> 
    对于任意 $(\alpha, \beta, \gamma) \in (-\pi, \pi] \times \mathbb{Q} \times (-\pi, \pi]$，有：

    $$
    R_z(g(\alpha)) R_y(f(\beta)) R_x(g(\gamma)) = R_z(\alpha) R_y(\beta) R_x(\gamma)
    $$

    且 $(g(\alpha), f(\beta), g(\gamma)) \in (-\pi, \pi] \times \left[ -\frac{\pi}{2}, \frac{\pi}{2} \right] \times (-\pi, \pi]$。

    **一个姿态若能被一组俯仰角绝对值大于90°的z-y-x欧拉角或x-y-z固定角描述，那么也能被另一组俯仰角绝对值不大于90°的z-y-x欧拉角或x-y-z固定角描述**

    所以规定：$(\alpha, \beta, \gamma) \in (-\pi, \pi] \times \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] \times (-\pi, \pi]$







!!! example "已知 $R \in \text{SO}(3)$，求$(\alpha, \beta, \gamma) \in (-\pi, \pi] \times [-\pi/2, \pi/2] \times (-\pi, \pi]$使得$R = R_{z'y'x'}(\alpha, \beta, \gamma)$"
    虽然zyx欧拉角可以表示任意旋转，但是这个命题限制了$\beta$的取值范围

    $$
    R_{z'y'x'}(\alpha, \beta, \gamma) = \begin{pmatrix}
    \cos\alpha \cos\beta & \cos\alpha \sin\beta \sin\gamma - \sin\alpha \cos\gamma & \cos\alpha \sin\beta \cos\gamma + \sin\alpha \sin\gamma \\
    \sin\alpha \cos\beta & \sin\alpha \sin\beta \sin\gamma + \cos\alpha \cos\gamma & \sin\alpha \sin\beta \cos\gamma - \cos\alpha \sin\gamma \\
    -\sin\beta & \cos\beta \sin\gamma & \cos\beta \cos\gamma
    \end{pmatrix}
    $$



    首先，因为$\beta$的定义域是$\left[ -\frac{\pi}{2}, \frac{\pi}{2} \right]$，所以$\cos\beta \ge 0$


    **情况 1** $\cos\beta > 0$

    - $\cos\beta = \sqrt{r_{32}^2 + r_{33}^2}$
    - $\beta = \arctan2\left(-r_{31}, \sqrt{r_{32}^2 + r_{33}^2}\right)$
    - $\alpha = \arctan2(r_{21}, r_{11})$
    - $\gamma = \arctan2(r_{32}, r_{33})$

    **情况 2** $\beta = \frac{\pi}{2}$

    $$
    R_{z'y'x'}(\alpha, \frac{\pi}{2}, \gamma) = \begin{pmatrix}
    0 & \cos\alpha \cos\gamma - \sin\alpha \sin\gamma & \cos\alpha \sin\gamma + \sin\alpha \cos\gamma \\
    0 & \sin\alpha \cos\gamma + \cos\alpha \sin\gamma & \sin\alpha \sin\gamma - \cos\alpha \cos\gamma \\
    -1 & 0 & 0
    \end{pmatrix}=\begin{pmatrix}
    0 & -\sin(\alpha - \gamma) & \cos(\alpha - \gamma) \\
    0 & \cos(\alpha - \gamma) & \sin(\alpha - \gamma) \\
    -1 & 0 & 0
    \end{pmatrix}
    $$

    - 只能得到一个关于 $\alpha$ 与 $\gamma$ 之差的结果：$\alpha - \gamma = \arctan2(r_{23}, r_{22})$
    - 对应这种姿态的 $z'y'x'$ 欧拉角或 $xyz$ 固定角不唯一。

    **情况 3** $\beta = -\frac{\pi}{2}$

    当 $\beta = -\frac{\pi}{2}$ 时，旋转矩阵 $R_{z'y'x'}(\alpha, \beta, \gamma)$ 可以简化为：

    $$
    R_{z'y'x'}(\alpha, -\frac{\pi}{2}, \gamma) = \begin{pmatrix}
    0 & \cos\alpha \cos\gamma + \sin\alpha \sin\gamma & -\cos\alpha \sin\gamma + \sin\alpha \cos\gamma \\
    0 & \sin\alpha \cos\gamma - \cos\alpha \sin\gamma & \sin\alpha \sin\gamma + \cos\alpha \cos\gamma \\
    1 & 0 & 0
    \end{pmatrix}=\begin{pmatrix}
    0 & \sin(\alpha + \gamma) & \cos(\alpha + \gamma) \\
    0 & \cos(\alpha + \gamma) & -\sin(\alpha + \gamma) \\
    1 & 0 & 0
    \end{pmatrix}
    $$

    - $\alpha + \gamma = \arctan2(-r_{23}, r_{22})$

### 等效轴角 - 绕给定轴旋转一次

**欧拉旋转定理**：若刚体从初姿态作任意定点转动后呈终姿态，则必可找到一个过该点的轴$K$及角度$\theta$，刚体从初姿态绕$K$作定轴转动$\theta$后呈终姿态


**罗德里格斯公式**

$$
r_{OQ}' = r_{OQ} \cos \theta + (r_{OQ} \cdot r_{OK}) r_{OK} (1 - \cos \theta) + (r_{OK} \times r_{OQ}) \sin \theta
$$

> 其中$r_{OQ}$是初始点，$r_{OQ}'$是旋转后的点，$r_{OK}$是旋转轴上的单位向量，$\theta$是旋转角度

也可以表示为矩阵的形式

$$
R = I + \sin \theta [\mathbf{k}]_{\times} + (1 - \cos \theta) [\mathbf{k}]_{\times}^2
$$

其中，$I$ 是单位矩阵，$[\mathbf{k}]_{\times}$ 是 $\mathbf{k}$ 的叉积矩阵：

$$
[\mathbf{k}]_{\times} = \begin{pmatrix}
0 & -k_z & k_y \\
k_z & 0 & -k_x \\
-k_y & k_x & 0
\end{pmatrix}
$$


??? note "可行性验证——罗德里格斯公式推导"

    以单位向量$^A\!K=(k_x,k_y,k_z)^\mathrm{T}$表示旋转轴，记旋转角度为$\theta$

    旋转前$\{B\}$与$\{A\}$重合，即$^A_B\!R(0)=\mathbf{I}$，求$\{B\}$绕$^A\!K$旋转$\theta$后的$^A_{B(1)}\!R$

    即分别求$^{A}\mathbf{X}_{B(0)}=\begin{pmatrix}1\\0\\0\end{pmatrix}$，$^{A}\mathbf{Y}_{B(0)}=\begin{pmatrix}0\\1\\0\end{pmatrix}$，$^{A}\mathbf{Z}_{B(0)}=\begin{pmatrix}0\\0\\1\end{pmatrix}$绕$^A\!K$旋转$\theta$后所得到的$^{A}\mathbf{X}_{B(1)}$，$^{A}\mathbf{Y}_{B(1)}$，$^{A}\mathbf{Z}_{B(1)}$

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224214115258.png)

    向量 $\mathbf{r}_{OQ}$ 绕单位向量 $\mathbf{r}_{OK}$ 旋转，这个过程中，$\mathbf{r}_{OQ}$在$\mathbf{r}_{OK}$的投影长度是不变的，所以$\mathbf{r}_{OQ}$ 向 $\mathbf{r}_{Ox}$ 作投影，得投影向量 $\mathbf{r}_{OP} = (\mathbf{r}_{OQ} \cdot \mathbf{r}_{Ox}) \mathbf{r}_{Ox}$ **（点乘获得长度，乘以单位向量获得方向）** ，则 $\mathbf{r}_{PQ} = \mathbf{r}_{OQ} - \mathbf{r}_{OP}$

    将直角三角形 $OPQ$ 绕 $\mathbf{r}_{Ox}$ 旋转 $\theta$，得到直角三角形 $OP'Q'$  那么 $\mathbf{r}_{OQ'}$ 即为旋转后的 $\mathbf{r}_{OQ}$。为了求得 $\mathbf{r}_{OQ'}$，构造向量 $\mathbf{r}_{PW} = \mathbf{r}_{Ox} \times \mathbf{r}_{PQ}$，将 $\mathbf{r}_{PQ}$ 绕 $\mathbf{r}_{Ox}$ 旋转 $90^\circ$，即得到 $\mathbf{r}_{PW}$

    $$
    \mathbf{r}_{PW} \perp \mathbf{r}_{Ox}, \mathbf{r}_{PW} \perp \mathbf{r}_{PQ}, |\mathbf{r}_{PW}| = |\mathbf{r}_{Ox}| |\mathbf{r}_{PQ}| \sin \frac{\pi}{2} = |\mathbf{r}_{PQ}| = |\mathbf{r}_{PW}|
    $$

    显然，点 $P, Q, W, Q'$ 在同一平面，在该平面上，以点 $P$ 为圆心，以 $|\mathbf{r}_{PQ}|$ 为半径画圆，点 $Q, W, Q'$ 都在此圆上，且 $\mathbf{r}_{PQ'} = \mathbf{r}_{PQ} \cos \theta + \mathbf{r}_{PW} \sin \theta$  **（可以理解为正交分解，乘上了对应方向的单位向量）**

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224213858660.png)

    

    于是 $\mathbf{r}_{OQ'} = \mathbf{r}_{OP} + \mathbf{r}_{PQ'} = \mathbf{r}_{OP} + (\mathbf{r}_{OQ} - \mathbf{r}_{OP}) \cos \theta + (\mathbf{r}_{OK} \times \mathbf{r}_{OQ}) \sin \theta - (\mathbf{r}_{OK} \times \mathbf{r}_{OP}) \sin \theta$

    **$\mathbf{r}_{OK}$ 和$\mathbf{r}_{OP}$ 同方向，叉积为0**

!!! note "唯一性求解"

    已知 $R \in \mathrm{SO}(3)$，求单位向量 $(k_x, k_y, k_z)^\mathrm{T}$ 和旋转角 $\theta \in (-\pi, \pi]$ 使得 $R = R_K(\theta)$

    $$
    R = \begin{pmatrix}
    r_{11} & r_{12} & r_{13} \\
    r_{21} & r_{22} & r_{23} \\
    r_{31} & r_{32} & r_{33}
    \end{pmatrix} = \begin{pmatrix}
    k_x^2 \nu \theta + c \theta & k_x k_y \nu \theta - k_z s \theta & k_x k_z \nu \theta + k_y s \theta \\
    k_x k_y \nu \theta + k_z s \theta & k_y^2 \nu \theta + c \theta & k_y k_z \nu \theta - k_x s \theta \\
    k_x k_z \nu \theta - k_y s \theta & k_y k_z \nu \theta + k_x s \theta & k_z^2 \nu \theta + c \theta
    \end{pmatrix} \quad \nu \theta = 1 - c \theta
    $$

    不难理解 $R_K(\theta) = R_{-K}(-\theta)$ （绕正方向旋转一个角度，等同于绕反方向旋转同样的负的角度）

    因此规定 $\theta \in [0, \pi]$

    $$
    \theta = \arccos\left(\frac{r_{11} + r_{22} + r_{33} - 1}{2}\right)
    $$

    === "若 $\theta \in (0, \pi)$,唯一解"

        $$
        \begin{pmatrix}
        k_x \\
        k_y \\
        k_z
        \end{pmatrix} = \frac{1}{2 \sin \theta} \begin{pmatrix}
        r_{32} - r_{23} \\
        r_{13} - r_{31} \\
        r_{21} - r_{12}
        \end{pmatrix} \quad \text{唯一解}
        $$

    === "若 $\theta = \pi$,两组解"

        $$
        \begin{pmatrix}
        r_{11} & r_{12} & r_{13} \\
        r_{21} & r_{22} & r_{23} \\
        r_{31} & r_{32} & r_{33}
        \end{pmatrix} = \begin{pmatrix}
        2k_x^2 - 1 & 2k_x k_y & 2k_x k_z \\
        2k_x k_y & 2k_y^2 - 1 & 2k_y k_z \\
        2k_x k_z & 2k_y k_z & 2k_z^2 - 1
        \end{pmatrix}
        $$

        由 $r_{11} + r_{22} + r_{33} = (2k_x^2 - 1) + (2k_y^2 - 1) + (2k_z^2 - 1) = -1$，知 $r_{11}, r_{22}, r_{33}$ 不会同时等于 $-1$

        以 $r_{11} \neq -1$ 为例，$k_x = \pm \sqrt{(r_{11} + 1)/2}$

        $$
        \begin{pmatrix}
        k_x \\
        k_y \\
        k_z
        \end{pmatrix} = \pm \begin{pmatrix}
        \sqrt{(r_{11} + 1)/2} \\
        r_{12} / \sqrt{2(r_{11} + 1)} \\
        r_{13} / \sqrt{2(r_{11} + 1)}
        \end{pmatrix} \quad \text{两组解}
        $$

    === "若 $\theta = 0$,无穷解"

        $$
        \begin{pmatrix}
        r_{11} & r_{12} & r_{13} \\
        r_{21} & r_{22} & r_{23} \\
        r_{31} & r_{32} & r_{33}
        \end{pmatrix} = \begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
        \end{pmatrix}
        $$


        任何单位向量$\begin{pmatrix}k_x \\k_y \\k_z\end{pmatrix}$ 均可，无穷组解




### 四元数


#### 欧拉参数


在等效轴 $[k_x \, k_y \, k_z]^T$ 和等效轴角 $\theta \in \mathbb{R}$ 的基础上，定义欧拉参数$[\eta \,\ \varepsilon_1 \ \varepsilon_2 \ \varepsilon_3]^T$,一个标量和一个长度不超过1的三维向量

其中

$$
\eta = \cos \frac{\theta}{2}, \quad \varepsilon = \begin{bmatrix} \varepsilon_1 \\ \varepsilon_2 \\ \varepsilon_3 \end{bmatrix} = \begin{bmatrix} k_x \sin \frac{\theta}{2} \\ k_y \sin \frac{\theta}{2} \\ k_z \sin \frac{\theta}{2} \end{bmatrix}
$$


满足约束 $\eta^2 + \varepsilon_1^2 + \varepsilon_2^2 + \varepsilon_3^2 = 1$

记 $\mathbb{U}$ 为由全体欧拉参数构成的集合,显然$\mathbb{U}$ 是 $\mathbb{R}^4$ 中的单位超球面

将之前的等效轴角表示写成欧拉参数的形式

$$
R = \begin{bmatrix}
k_x^2 \nu \theta + c \theta & k_x k_y \nu \theta - k_z s \theta & k_x k_z \nu \theta + k_y s \theta \\
k_x k_y \nu \theta + k_z s \theta & k_y^2 \nu \theta + c \theta & k_y k_z \nu \theta - k_x s \theta \\
k_x k_z \nu \theta - k_y s \theta & k_y k_z \nu \theta + k_x s \theta & k_z^2 \nu \theta + c \theta
\end{bmatrix}\\
= \begin{bmatrix}
2(\eta^2 + \varepsilon_1^2) - 1 & 2(\varepsilon_1 \varepsilon_2 - \eta \varepsilon_3) & 2(\varepsilon_1 \varepsilon_3 + \eta \varepsilon_2) \\
2(\varepsilon_1 \varepsilon_2 + \eta \varepsilon_3) & 2(\eta^2 + \varepsilon_2^2) - 1 & 2(\varepsilon_2 \varepsilon_3 - \eta \varepsilon_1) \\
2(\varepsilon_1 \varepsilon_3 - \eta \varepsilon_2) & 2(\varepsilon_2 \varepsilon_3 + \eta \varepsilon_1) & 2(\eta^2 + \varepsilon_3^2) - 1
\end{bmatrix} = R_\varepsilon(\eta)
$$

其中，$\nu \theta = 1 - c \theta$，$c = \cos \theta$，$s = \sin \theta$。

任给一组欧拉参数，必有一个姿态（或旋转）与之对应。

!!! note "欧拉参数的唯一性"

    已知 $R \in SO(3)$，求欧拉参数使得

    $$
    R = \begin{bmatrix}
    r_{11} & r_{12} & r_{13} \\
    r_{21} & r_{22} & r_{23} \\
    r_{31} & r_{32} & r_{33}
    \end{bmatrix} = \begin{bmatrix}
    2(\eta^2 + \varepsilon_1^2) - 1 & 2(\varepsilon_1 \varepsilon_2 - \eta \varepsilon_3) & 2(\varepsilon_1 \varepsilon_3 + \eta \varepsilon_2) \\
    2(\varepsilon_1 \varepsilon_2 + \eta \varepsilon_3) & 2(\eta^2 + \varepsilon_2^2) - 1 & 2(\varepsilon_2 \varepsilon_3 - \eta \varepsilon_1) \\
    2(\varepsilon_1 \varepsilon_3 - \eta \varepsilon_2) & 2(\varepsilon_2 \varepsilon_3 + \eta \varepsilon_1) & 2(\eta^2 + \varepsilon_3^2) - 1
    \end{bmatrix}
    $$

    === "若 $r_{11} + r_{22} + r_{33} > -1$，两组反号的欧拉参数"

        $$
        \begin{bmatrix}
        \eta \\
        \varepsilon
        \end{bmatrix} = \frac{1}{2} \begin{bmatrix}
        \sqrt{r_{11} + r_{22} + r_{33} + 1} \\
        \text{sgn}(r_{32} - r_{23}) \sqrt{r_{11} - r_{22} - r_{33} + 1} \\
        \text{sgn}(r_{13} - r_{31}) \sqrt{r_{22} - r_{33} - r_{11} + 1} \\
        \text{sgn}(r_{21} - r_{12}) \sqrt{r_{33} - r_{11} - r_{22} + 1}
        \end{bmatrix}
        $$

        或

        $$
        \begin{bmatrix}
        \eta \\
        \varepsilon
        \end{bmatrix} = -\frac{1}{2} \begin{bmatrix}
        \sqrt{r_{11} + r_{22} + r_{33} + 1} \\
        \text{sgn}(r_{32} - r_{23}) \sqrt{r_{11} - r_{22} - r_{33} + 1} \\
        \text{sgn}(r_{13} - r_{31}) \sqrt{r_{22} - r_{33} - r_{11} + 1} \\
        \text{sgn}(r_{21} - r_{12}) \sqrt{r_{33} - r_{11} - r_{22} + 1}
        \end{bmatrix}
        $$
        
        
    === "若 $r_{11} + r_{22} + r_{33} = -1$"
    
        又可知 $r_{11}$、$r_{22}$ 和 $r_{33}$ 不会同时等于 $-1$。

        以 $r_{11} \neq -1$ 为例，可得两组反号的欧拉参数：

        $$
        \begin{bmatrix}
        \eta \\
        \varepsilon
        \end{bmatrix} = \frac{1}{2} \begin{bmatrix}
        0 \\
        \sqrt{r_{11} - r_{22} - r_{33} + 1} \\
        \text{sgn}(r_{12}) \sqrt{r_{22} - r_{33} - r_{11} + 1} \\
        \text{sgn}(r_{13}) \sqrt{r_{33} - r_{11} - r_{22} + 1}
        \end{bmatrix}
        $$

        或

        $$
        \begin{bmatrix}
        \eta \\
        \varepsilon
        \end{bmatrix} = -\frac{1}{2} \begin{bmatrix}
        0 \\
        \sqrt{r_{11} - r_{22} - r_{33} + 1} \\
        \text{sgn}(r_{12}) \sqrt{r_{22} - r_{33} - r_{11} + 1} \\
        \text{sgn}(r_{13}) \sqrt{r_{33} - r_{11} - r_{22} + 1}
        \end{bmatrix}
        $$


    === "$\theta = 2k\pi$ 时"
    
        $$
        \begin{bmatrix}
        \eta \\
        \varepsilon
        \end{bmatrix} = \begin{bmatrix}
        \pm 1 \\
        0 \\
        0 \\
        0
        \end{bmatrix}
        $$

        当 $\theta = 2k\pi$ 时，利用 $\sin \frac{\theta}{2} = 0$ 使得 $\varepsilon$ 为零向量。

        这意味着当旋转角 $\theta$ 为 $2k\pi$（其中 $k$ 为整数）时，欧拉参数中的 $\varepsilon$ 向量为零向量，而 $\eta$ 的值为 $\pm 1$。这对应于旋转矩阵 $R$ 为单位矩阵的情况，即没有发生旋转。










#### Grassmann积

在欧拉参数中定义 $\eta$ 和 $\varepsilon$ 的 Grassmann 积如下:

$$
\begin{bmatrix}
\eta \\
\varepsilon
\end{bmatrix} \oplus \begin{bmatrix}
\xi \\
\delta
\end{bmatrix} = \begin{bmatrix}
\eta\xi - \varepsilon^T\delta \\
\eta\delta +\xi\varepsilon +  \varepsilon \times \delta
\end{bmatrix} = \begin{bmatrix}
\eta & -\varepsilon_1 & -\varepsilon_2 & -\varepsilon_3 \\
\varepsilon_1 & \eta & -\varepsilon_3 & \varepsilon_2 \\
\varepsilon_2 & \varepsilon_3 & \eta & -\varepsilon_1 \\
\varepsilon_3 & -\varepsilon_2 & \varepsilon_1 & \eta
\end{bmatrix} \begin{bmatrix}
\xi \\
\delta_1 \\
\delta_2 \\
\delta_3
\end{bmatrix} = A\begin{bmatrix}
\xi \\
\delta
\end{bmatrix}
$$

如果有 $\begin{bmatrix}\eta \\ \varepsilon\end{bmatrix} \in \mathbb{U}$，则 $A^TA = I$

如果还有 $\begin{bmatrix}\xi \\ \delta\end{bmatrix} \in \mathbb{U}$，则 $[\xi \quad \delta^T]A^TA\begin{bmatrix}\xi \\ \delta\end{bmatrix} = 1$ 即 $\begin{bmatrix}\eta\xi - \varepsilon^T\delta \\ \xi\varepsilon + \eta\delta + \varepsilon \times \delta\end{bmatrix} \in \mathbb{U}$

$\mathbb{U}$中任意两个向量的Grassmann积仍是$\mathbb{U}$中的向量

基于Grassmann积，欧拉参数可在 $\mathbb{U}$ 中直接描述3维姿态和3维坐标系旋转。

两个欧拉参数做grassman积等效于两个旋转矩阵相乘，$\mathbb{U}$ 中的Grassmann积相当于 $SO(3)$ 中的乘法。（与之前表示方法兼容）


!!! info "哈密顿与四元数"
    哈密顿在1843年提出四元数，并将其用于描述三维空间中的旋转。

四元数是一种扩展了复数的数学对象，由一个实部和三个虚部组成

引入三个虚数单位 $i, j, k$，并规定 $i^2 = j^2 = k^2 = ijk = -1$。

由此规定，可推导得：

$$
ij = k, ji = -k, jk = i, kj = -i, ki = j, ik = -j
$$

对任意 $[\eta \,\ \varepsilon_1 \,\ \varepsilon_2 \,\ \varepsilon_3]^T \in \mathbb{R}^4$，其对应的四元数 $q$ 为：

$$
q = \eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3
$$

记 $\mathbb{H}$ 为由全体四元数构成的集合。

=== "加法"
    与复数加法一致

    $$
    (\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3) + (\xi + i\delta_1 + j\delta_2 + k\delta_3) = (\eta + \xi) + i(\varepsilon_1 + \delta_1) + j(\varepsilon_2 + \delta_2) + k(\varepsilon_3 + \delta_3)
    $$


=== "乘法"

    $$
    (\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)(\xi + i\delta_1 + j\delta_2 + k\delta_3) = (\eta\xi - \varepsilon_1\delta_1 - \varepsilon_2\delta_2 - \varepsilon_3\delta_3) + i(\eta\delta_1 + \varepsilon_1\xi + \varepsilon_2\delta_3 - \varepsilon_3\delta_2) + j(\eta\delta_2 - \varepsilon_1\delta_3 + \varepsilon_2\xi + \varepsilon_3\delta_1) + k(\eta\delta_3 + \varepsilon_1\delta_2 - \varepsilon_2\delta_1 + \varepsilon_3\xi)
    $$

    $\mathbb{H}$ 中的乘法相当于 $\mathbb{R}^4$ 中的 Grassmann 积。

=== "共轭"

    $\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3$的共轭$(\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)^* = \eta - i\varepsilon_1 - j\varepsilon_2 - k\varepsilon_3$

=== "模长"

    $\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3$的模长$|\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3| = \sqrt{\eta^2 + \varepsilon_1^2 + \varepsilon_2^2 + \varepsilon_3^2}$

单位四元数

- **定义**：单位四元数是模长等于1的四元数。
- **关系**：单位四元数与欧拉参数一一对应。
- **应用**：基于乘法，单位四元数可直接描述三维姿态和三维坐标系旋转。

原点不变条件下的三维向量的转换公式 $A^B P = A_B^B R^B P$
- 记 $B^P = \begin{bmatrix} x_1 & y_1 & z_1 \end{bmatrix}^T$，$A^P = \begin{bmatrix} x_2 & y_2 & z_2 \end{bmatrix}^T$


!!! note "兼容性"
    旋转矩阵基于欧拉参数表示为：

    $$
    A_B^B R = R_\varepsilon(\eta) = \begin{bmatrix}
    2(\eta^2 + \varepsilon_1^2) - 1 & 2(\varepsilon_1 \varepsilon_2 - \eta \varepsilon_3) & 2(\varepsilon_1 \varepsilon_3 + \eta \varepsilon_2) \\
    2(\varepsilon_1 \varepsilon_2 + \eta \varepsilon_3) & 2(\eta^2 + \varepsilon_2^2) - 1 & 2(\varepsilon_2 \varepsilon_3 - \eta \varepsilon_1) \\
    2(\varepsilon_1 \varepsilon_3 - \eta \varepsilon_2) & 2(\varepsilon_2 \varepsilon_3 + \eta \varepsilon_1) & 2(\eta^2 + \varepsilon_3^2) - 1
    \end{bmatrix}
    $$

    上述三维向量的转换公式可基于单位四元数表示为：

    $$
    ix_2 + jy_2 + kz_2 = (\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)(ix_1 + jy_1 + kz_1)(\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)^*
    $$

#### 可视化与参考资料

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=33385105&bvid=BV1SW411y7W1&cid=58437850&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="600px"></iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=35804287&bvid=BV1Lt411U7og&cid=62823973&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="600px"></iframe>

<iframe src="https://eater.net/quaternions/video/intro" width="100%" "></iframe>

<iframe src="https://eater.net/quaternions/video/doublecover" width="100%" "></iframe>

<iframe src="https://krasjet.github.io/quaternion/quaternion.pdf" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>

### Left or Right —— 右乘连体左乘基

1. 对于两个变换的叠加：$M_2M_1$表示先进行$M_1$变换，再进行$M_2$变换，这里$M_1$、$M_2$都是自然基坐标系下。
2. 如果$M_2$变换是在$M_1$坐标系基础上进行的，那么根据相似矩阵把$M_2$转换成自然基坐标系下：$M_1M_2M_1^{-1}$
3. 那么两个变换叠加就是：$(M_1M_2M_1^{-1})M_1 = M_1M_2$

这是一个很有意思的现象，如果每个变换都是在上个变换基础上进行的，那么只要把矩阵顺序反过来即可：

- 所有变换都在自然基下：$M_4M_3M_2M_1$
- 每个变换在前一个变换后的坐标系下：$M_1M_2M_3M_4$


> 可以参考3b1b基坐标变换的视频

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=44855426&bvid=BV1ib411t7YR&cid=80579031&p=13&t=620&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>

!!! example "例子"
    === "例1"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224160846651.png)

    === "例2"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224215632614.png)

    === "例3"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224215659494.png)

    === "例4"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224215724829.png)

    === "例5"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224215732527.png)

    === "例6"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224215712797.png)


### 各种表示之间的转换

[三维旋转：欧拉角、四元数、旋转矩阵、轴角之间的转换 - 知乎](https://zhuanlan.zhihu.com/p/45404840)


## 正运动学 - 已知角度求末端位姿
各个关节变量的函数，描述了工具坐标系相对于基坐标系的位置和姿态



## 逆运动学 - 已知位姿求解角度

给定工具坐标系的位置和姿态，解算出个各关节变量


??? info "自由度 - 刚体本身具有可独立运动方向的数目"。
    > 手臂：7自由度；无穷多个解
    > 腿：6自由度;8个解

    $$
    F = 6(l - n - 1) + \sum_{i = 1}^{n}f_{i} \\
    l为连杆数（包括基座），n为关节总数，f_i为第i个关节的自由度数
    $$

    <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/017a2277142fe6ab01f933ad81c3e281_1440w.webp" alt="img" style="zoom:50%;" />

    > 一个6自由度的机械手，即使某两组构型对应的末端机构的三维位置相同，机械手在从一个构型移动到另一个构型的时候无法保持末端机构始终不动。
    >
    > 如果有人在电视里看过工业机器人焊东西的话，就会发现它在同一个位置焊接的时候，一会儿整个扭到这边，一会儿整个扭到那边，看起来非常酷炫的样子。事实上这么做只是因为，虽然焊接只是想改变末端机构的朝向，而不改变末端机构的位置，但是由于定理的限制，它必须要往后退一些，然后各种扭，才能保证在移动末端机构的朝向的过程中不会撞到东西，因为移动的时候末端机构的三维位置一定会乱动。如果它能够随便转一点点就可以达到目的，还费那个力气酷炫地整体都转起来干啥……
    >
    > 而多了一个自由度以后就不一样了。
    >
    > 想想开门时拧钥匙的动作，这个情况下是人胳膊的末端机构（手）的三维位置没有变（始终在钥匙孔前），但是末端机构（手）的三维旋转变了（转动了钥匙）。人能够实现这个简单的动作，就是因为我们的胳膊有7个自由度。


## 速度与静力



讲关节空间速度映射到笛卡尔空间速度，通过雅可比矩阵描述