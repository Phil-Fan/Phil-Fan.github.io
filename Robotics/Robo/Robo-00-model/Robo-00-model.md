# 机器人建模

!!! note "课程信息"
    - 名称：机器人建模与控制
    - 授课教师：zrh
    - 本篇笔记来源：zhihu，老师课件，b站视频等

## 基础概念


[机器人学入门（二）：基础知识 - 知乎](https://zhuanlan.zhihu.com/p/368988354)<br>
[机器人学入门（三）：空间描述和变换 - 知乎](https://zhuanlan.zhihu.com/p/369083000)<br>
[机器人学入门（五）：操作臂运动学 - 知乎](https://zhuanlan.zhihu.com/p/495983666)<br>

关节和连杆

这里可以举一个小小的例子，比如下面的图片，黑色箭头地方是关节，将关节连起来的是连杆

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301191114339.png)


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250217105608273.png)



## 空间描述与变换

位置和姿态总是成对出现的，我们将此组合称为坐标系。一个坐标系可以等价的用一个位置向量和一个旋转矩阵来描述。

- **位置**：用向量进行表示，左上标来描述具体的坐标系，例如$^A\!P$ 表明列向量$P$在坐标系$A$下定义的。
- **姿态**：物体上固定坐标系相对于参考坐标系的方位


| 表示方法 | 核心思想 | 公式 | 缺点 |
| --- | --- | --- | --- |
| **旋转矩阵** | 使用3x3矩阵表示三维旋转 | $\mathbf{R} = \begin{pmatrix} r_{11} & r_{12} & r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33} \end{pmatrix}$ | 1. 参数多（9个），冗余<br> 2. 难以直观理解旋转过程<br> 3. 插值复杂 |
| **欧拉角** | 将旋转分解为绕三个正交轴的旋转 | $(\alpha, \beta, \gamma)$，常用ZYX顺序：$\mathbf{R} = R_z(\alpha) R_y(\beta) R_x(\gamma)$ | 易于理解和可视化<br> 但是<br> 1. 万向锁问题（奇异性）<br> 2. 不同顺序定义不唯一<br> 3. 插值不平滑 |
| **等效轴角** | 用一个单位轴和一个旋转角表示旋转 | $(\mathbf{k}, \theta)$，其中$\mathbf{k} = (k_x, k_y, k_z)$为单位向量，$\theta$为旋转角。旋转矩阵为：<br>$\mathbf{R} = \mathbf{I} + \sin\theta \mathbf{K} + (1 - \cos\theta) \mathbf{K}^2$，<br>其中$\mathbf{K} = \begin{pmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{pmatrix}$ | 1. 无法直接表示0°旋转（需特殊处理）<br>2. 插值时需注意旋转角的周期性 |
| **四元数** | 使用四维超复数表示旋转 | $q = \eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3$，其中$\eta^2 + \varepsilon_1^2 + \varepsilon_2^2 + \varepsilon_3^2 = 1$。 | 参数最少（4个）避免了奇异性问题<br>1. 较难直观理解<br>2. 计算稍复杂（但比旋转矩阵简单） |

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



我们知道空间中的变换可以表示为旋转和平移的组合，那么如何表示旋转和平移呢？

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

!!! note "证明$\det(^A_B\!R) = 1$"
    由正交性即可得出 $R^T \cdot R = I$,所以可以得出行列式是正负一之中




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
- **旋转前后，2范数不变**:$\|y\|^2 = y^T y = (Rx)^T Rx = x^T R^T R x = x^T x = \|x\|^2$



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


    同理，zyz俯仰角也可以确定$\beta$的范围在 $[-\pi,\pi]$之间

    1. **定义集合与映射函数** :令集合 $\mathbb{Q} = (-\pi, 0)$，表示β的原始范围中需要调整的部分,定义函数 $f: \mathbb{Q} \to (0, \pi)$，将负β映射为正$f(\beta) = -\beta.$,定义函数 $g: (-\pi, \pi] \to (-\pi, \pi]$，调整前后的z轴旋转角度：  

    $$
    g(\theta) = 
    \begin{cases} 
    \theta + \pi, & \text{当 } \theta \in (-\pi, 0], \\
    \theta - \pi, & \text{当 } \theta \in (0, \pi].
    \end{cases}
    $$

    2. **旋转矩阵的等价性**         对于任意 $\beta \in \mathbb{Q}$（即$\beta \in (-\pi, 0)$），通过以下步骤调整参数：令 $\beta' = f(\beta) = -\beta \in (0, \pi)$,令 $\alpha' = g(\alpha)$，$\gamma' = g(\gamma)$,此时，原旋转矩阵可等价表示为： 

    $$ 
    R_z(\alpha') R_y(\beta') R_z(\gamma') = R_z(g(\alpha)) R_y(-\beta) R_z(g(\gamma)). 
    $$

    根据旋转矩阵的恒等式（$R_z(\pi) R_y(-\beta) R_z(\pi) = R_y(\beta)$），可得：  
    $R_z(g(\alpha)) R_y(-\beta) R_z(g(\gamma)) = R_z(\alpha) R_y(\beta) R_z(\gamma).$ 







### 等效轴角 - 绕给定轴旋转一次

**欧拉旋转定理**：若刚体从初姿态作任意定点转动后呈终姿态，则必可找到一个过该点的轴$K$及角度$\theta$，刚体从初姿态绕$K$作定轴转动$\theta$后呈终姿态

**罗德里格斯公式——求解旋转后向量**

$$
r_{OQ}' = r_{OQ} \cos \theta + (r_{OQ} \cdot r_{OK}) r_{OK} (1 - \cos \theta) + (r_{OK} \times r_{OQ}) \sin \theta
$$

> 其中$r_{OQ}$是初始点，$r_{OQ}'$是旋转后的点，$r_{OK}$是旋转轴上的单位向量，$\theta$是旋转角度


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

**旋转矩阵求解**

$$
R= \begin{pmatrix}k_x^2 \nu \theta + c \theta & k_x k_y \nu \theta - k_z s \theta & k_x k_z \nu \theta + k_y s \theta \\    k_x k_y \nu \theta + k_z s \theta & k_y^2 \nu \theta + c \theta & k_y k_z \nu \theta - k_x s \theta \\    k_x k_z \nu \theta - k_y s \theta & k_y k_z \nu \theta + k_x s \theta & k_z^2 \nu \theta + c \theta\end{pmatrix}
$$

其中$\nu \theta = 1-\cos \theta$
    
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



!!! note "证明两个无穷小旋转次序可以交换"
    使用了 $\sin\theta \approx \theta$，$\cos\theta \approx 1$，以及 $\theta^2 \approx 0$ 的近似条件

    $$
    \begin{align*}
    \mathbf{R}_K(\theta) = \begin{pmatrix}
    k_x^2 \upsilon \theta + c \theta & k_x k_y \upsilon \theta - k_z s \theta & k_x k_z \upsilon \theta + k_y s \theta \\
    k_x k_y \upsilon \theta + k_z s \theta & k_y^2 \upsilon \theta + c \theta & k_y k_z \upsilon \theta - k_x s \theta \\
    k_x k_z \upsilon \theta - k_y s \theta & k_y k_z \upsilon \theta + k_x s \theta & k_z^2 \upsilon \theta + c \theta
    \end{pmatrix}
    \end{align*}
    $$


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

#### 四元数基础

!!! info "哈密顿与四元数"
    哈密顿在1843年提出四元数，并将其用于描述三维空间中的旋转。

四元数是一种扩展了复数的数学对象，由一个实部和三个虚部组成

引入三个虚数单位 $i, j, k$，并规定 $i^2 = j^2 = k^2 = ijk = -1$。

由此规定，可推导得：

$$
ij = k, ji = -k, jk = i, kj = -i, ki = j, ik = -j
$$

> $ij = k$推导过程： ijk = -1等式左右同时右乘k 
> $ji = -k$推导过程： ijk = -1等式左右同时右乘kj, 得 $i = -jk$,得证

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

#### 单位四元数

- **定义**：单位四元数是模长等于1的四元数。
- **关系**：单位四元数与欧拉参数一一对应。

- **单位四元数的乘积仍然是单位四元数**
> 证明：使用Grassmann积，$\mathbb{U}$中任意两个向量的Grassmann积仍是$\mathbb{U}$中的向量

- **单位四元数的逆是其共轭**，即$(\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)(\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)^* = (\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3)^*(\eta + i\varepsilon_1 + j\varepsilon_2 + k\varepsilon_3) = 1$
> 证明思路：按照乘法的公式进行分解，就可以发现i,j,k的系数都消掉了，而常数项因为共轭，所以和为1




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



- 基于Grassmann积，欧拉参数可在 $\mathbb{U}$ 中直接描述3维姿态和3维坐标系旋转。
- 两个欧拉参数做grassman积等效于两个旋转矩阵相乘，$\mathbb{U}$ 中的Grassmann积相当于 $SO(3)$ 中的乘法。（与之前表示方法兼容）

!!! note "$\mathbb{U}$中任意两个向量的Grassmann积仍是$\mathbb{U}$中的向量"
    如果有 $\begin{bmatrix}\eta \\ \varepsilon\end{bmatrix} \in \mathbb{U}$，则 $A^TA = I$

    如果还有 $\begin{bmatrix}\xi \\ \delta\end{bmatrix} \in \mathbb{U}$，则 $[\xi \quad \delta^T]A^TA\begin{bmatrix}\xi \\ \delta\end{bmatrix} = 1$ 即 $\begin{bmatrix}\eta\xi - \varepsilon^T\delta \\ \xi\varepsilon + \eta\delta + \varepsilon \times \delta\end{bmatrix} \in \mathbb{U}$



#### 可视化与参考资料

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=33385105&bvid=BV1SW411y7W1&cid=58437850&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="600px"></iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=35804287&bvid=BV1Lt411U7og&cid=62823973&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="600px"></iframe>

<iframe src="https://eater.net/quaternions/video/intro" width="100%" height="auto"></iframe>

<iframe src="https://eater.net/quaternions/video/doublecover" width="100%" height="auto"></iframe>

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

!!! tip "总结各种变换中的符号与字母"
    - $^A_B\!R$ 表示从A坐标系到B坐标系的旋转矩阵
    - $^A_B\!T$ 表示从A坐标系到B坐标系的齐次变换矩阵
    - SO(3)：全体旋转矩阵的集合
    - SE(3)：全体齐次变换矩阵的集合
    - $\mathbb{U}$ 为由全体欧拉参数构成的集合

#### 旋转矩阵与欧拉角

**欧拉角 to 旋转矩阵**:直接使用矩阵乘法即可

**旋转矩阵 to 欧拉角**：使用反三角函数推导

从旋转矩阵提取欧拉角的公式跟欧拉角顺规的选取有关，因为旋转矩阵的元素会略有不同，但是思路都是一样的，就是根据旋转矩阵的解析表达式+反三角函数凑出来

这里需要特别注意，gimbal lock所带来的特殊情况的讨论



!!! note "已知 $R \in \text{SO}(3)$，求$(\alpha, \beta, \gamma) \in (-\pi, \pi] \times [-\pi/2, \pi/2] \times (-\pi, \pi]$使得$R = R_{z'y'x'}(\alpha, \beta, \gamma)$"
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


#### 旋转矩阵与四元数

**四元数 to 旋转矩阵**

可以直接带入公式，对于四元数$p = \eta + \varepsilon_1 i + \varepsilon_2 j + \varepsilon_3 k$,其旋转矩阵为

$$
A_B^B R = R_\varepsilon(\eta) = \begin{bmatrix}
2(\eta^2 + \varepsilon_1^2) - 1 & 2(\varepsilon_1 \varepsilon_2 - \eta \varepsilon_3) & 2(\varepsilon_1 \varepsilon_3 + \eta \varepsilon_2) \\
2(\varepsilon_1 \varepsilon_2 + \eta \varepsilon_3) & 2(\eta^2 + \varepsilon_2^2) - 1 & 2(\varepsilon_2 \varepsilon_3 - \eta \varepsilon_1) \\
2(\varepsilon_1 \varepsilon_3 - \eta \varepsilon_2) & 2(\varepsilon_2 \varepsilon_3 + \eta \varepsilon_1) & 2(\eta^2 + \varepsilon_3^2) - 1
\end{bmatrix}
$$

假设被旋转的变量为$V$,那么

$$
V' = p V p^{-1}
$$

**旋转矩阵 to 四元数**

- 首先判断旋转矩阵的合法性，判断其是否正交，即$R \cdot R^T = I$
- 然后可以从对应的旋转矩阵的表达式中，使用拼凑法，凑出所需要的四个参数的值。这里需要注意的是，每一个旋转矩阵会对应两个反号的四元数


!!! note "欧拉参数解算"

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
        说明 $\eta > 0$

        $$
        \sqrt{r_{11} + r_{22} + r_{33} + 1} = 2|\eta|
        \sqrt{r_{11} - r_{22} - r_{33} + 1} = 2|\varepsilon_1|, \text{sgn}(r_{32} - r_{23}) = \text{sgn}(2\eta\varepsilon_1)
        $$

        这个时候因为$\eta > 0$,就可以由$\eta\varepsilon_1$的符号推断$\varepsilon_1$的符号了


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

        这个时候 $\eta$是等于0 的
    
        又可知 $r_{11}$、$r_{22}$ 和 $r_{33}$ 不会同时等于 $-1$（同时等于零意味着$\varepsilon$就是0，显然不符合意思）

        以 $r_{11} \neq -1$ ($\varepsilon_1 \neq 0$)为例，可得两组反号的欧拉参数：

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

        这里要注意一下，求出来$\varepsilon_1<0$的时候，在求$\varepsilon_2$的时候，使用到了$sgn(r_{12})$，其实最后$\varepsilon_2$的符号应该是和$\sgn(r_{12})$是反号的，所以加了负号


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

        这里就可以说明欧拉参数以及四元数解决了等效轴角的问题





#### 欧拉角与四元数

**欧拉角 to 四元数**

- 首先欧拉角可以视为绕着给定轴旋转一个角度
- 我们又知道四元数是可以相乘的
- 所以把欧拉角的旋转描述成四元数，再进行相乘即可

**四元数 to 欧拉角** 比较复杂，建议使用四元数转换为旋转矩阵，再转换为欧拉角

#### 等效轴角

**等效轴角 to 四元数**

等效轴角就是绕着某条单位轴旋转一定角度，这个角度和四元数非常类似，所以这两个转换比较容易

四元数可以表示为

$$
p = \eta + \varepsilon_1 i + \varepsilon_2 j + \varepsilon_3 k
$$

$$
\eta = \cos \frac{\theta}{2}, \quad \varepsilon = \begin{bmatrix} \varepsilon_1 \\ \varepsilon_2 \\ \varepsilon_3 \end{bmatrix} = \begin{bmatrix} k_x \sin \frac{\theta}{2} \\ k_y \sin \frac{\theta}{2} \\ k_z \sin \frac{\theta}{2} \end{bmatrix}
$$

**等效轴角 to 旋转矩阵** 罗德里格斯旋转公式|Rodrigues' rotation formula

$$
R = I + \sin(\theta)K + (1 - \cos(\theta))K^2
$$

其中$K$是单位轴的反对称矩阵（叉积矩阵）

$$
K = \begin{bmatrix}
0 & -k_z & k_y \\
k_z & 0 & -k_x \\
-k_y & k_x & 0
\end{bmatrix}
$$

也可以记忆公式

$$
R= \begin{pmatrix}k_x^2 \nu \theta + c \theta & k_x k_y \nu \theta - k_z s \theta & k_x k_z \nu \theta + k_y s \theta \\    k_x k_y \nu \theta + k_z s \theta & k_y^2 \nu \theta + c \theta & k_y k_z \nu \theta - k_x s \theta \\    k_x k_z \nu \theta - k_y s \theta & k_y k_z \nu \theta + k_x s \theta & k_z^2 \nu \theta + c \theta\end{pmatrix}
$$



**旋转矩阵 to 等效轴角**

正方向旋转，等效于负方向逆时针旋转

!!! note "求解"

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


## 正运动学 - 已知角度求末端位姿



**关节空间 (Joint Space)**:关节空间是通过机器人的关节参数来描述机器人配置的空间。在关节空间中，机器人的每个关节都有一个关联的参数，如角度或距离，这些参数描述了机器人的当前配置。
在关节空间中，机器人的运动是通过改变关节参数来实现的，例如，改变关节角或关节位置。
关节空间分析是机器人运动学和控制的基础，它为控制算法和路径规划提供了一个直观的框架。

**笛卡尔空间 (Cartesian Space)**:笛卡尔空间是通过笛卡尔坐标系统来描述机器人末端执行器（例如机器人手或工具）的位置和方向的空间。在笛卡尔空间中，机器人的运动是通过改变末端执行器的位置和方向来实现的，通常使用x, y, z坐标和欧拉角或四元数来描述末端执行器的位置和方向。笛卡尔空间分析为机器人的任务规划和执行提供了一个直观和可视化的框架，它使得能够直接描述和控制机器人在物理世界中的运动。

本章的**正运动学**问题，就是**将关节空间转化到笛卡尔空间**当中去。

我们的目的就是获取机械臂末端相对于机械臂基座的位姿，首先要建立起连杆之间的变换关系，这里比较重要的搞明白连杆坐标系的**建立**以及**变换**（先建立，再变换）


### 连体坐标系建立
我觉得下面这一篇博文图片和解释比较清楚，这里要着重区别一下连杆转角和关节角

[机械臂运动学基础\_关节角和连杆转角的区别-CSDN博客](https://blog.csdn.net/qq_38962956/article/details/124851477)




**坐标系建立规则**(非标准D-HDenavit-Hartenberg方法)

（轴i的方向由设计者给定）
- 固定在关节轴i上的坐标系命名为坐标系$\{i\}$
- 坐标系$\{i\}$的Z轴与关节轴i的轴线重合
- 建立关节轴i和关节轴i+1的公共垂线ai
- 坐标系$\{i\}$的原点为公共垂线ai与关节轴i轴线的交点
- 坐标系$\{i\}$的X轴与公共垂线ai重合
- 根据右手定则确定坐标系$\{i\}$的Y轴

!!! info "机械臂基座和末端坐标系定义"
    固定在基座和末端的坐标系**可以任意设定方向**，但是要**以问题简化为主**
    
    - 例如固定在基座的参考坐标系$\{0\}$的Z0轴与关节轴1方向一致
    - 例如关节n的坐标系$\{n\}$与坐标系$\{n-1\}$的X轴一致

    这样的$T$中的$R$部分就是一个单位阵，加上一个平移向量即可


!!! tip "标准DH和非标准DH的区别"
    （1）**固连坐标系不同** <br>
    Stantard DH方法关节i上固连的是i-1坐标系，即坐标系建在连杆的输出端；MDH关节i上固连的是i坐标系，即坐标系建在连杆的输入端。<br>
    （2）**坐标系变换顺序不同** <br>
    Stantard DH方法是ZX类变换：先绕着i-1坐标系的的$Z_{i-1}$轴旋转和平移，再绕着坐标系i的$X_i$轴进行旋转和平移；（个人记忆方法：ZYX表示最常用，所以standtard使用这种）<br>
    Modified DH方法是XZ类变换：先绕着i坐标系的的$X_i$轴旋转和平移，再绕着坐标系i的$Z_i$轴进行旋转和平移；




#### 运动学参量

- 连杆扭转角$\alpha_{i-1}$：绕$X_{i-1}$轴，从$Z_{i-1}$轴旋转到Zi轴的角度
- 连杆长度$a_{i-1}$：沿$X_{i-1}$轴，从$Z_{i-1}$轴移动到Zi轴的距离（公垂线段为0的时候，当 $a_{i-1} = 0$ 时，我们并不将零长度的 $r_{O_{i-1}P_i}$ 视为传统的零向量，而是在与轴 $i-1$ 和轴 $i$ 同时垂直的方向中选一个作为 $r_{O_{i-1}P_i}$ 的正方向）
- 关节角$\theta_i$：沿$Z_{i-1}$轴，从$X_{i-1}$轴旋转到$X_i$轴的角度
- 连杆轴距$d_i$：沿$Z_{i-1}$轴，从$X_{i-1}$轴移动到$X_i$轴的距离

### 连体坐标系变换

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301174641450.png)

1. 坐标系 $\{i-1\}$ 绕 $X_{i-1}$ 轴旋转连杆扭转角 $\alpha_{i-1}$ 到达坐标系 $\{R\}$
2. 坐标系 $\{R\}$ 沿着 $X_R$ 轴移动连杆长度 $a_{i-1}$ 到达坐标系 $\{Q\}$
3. 坐标系 $\{Q\}$ 绕 $Z_Q$ 轴旋转关节角 $\theta_i$ 到达坐标系 $\{P\}$（因为坐标系的方向是根据公垂线段定义的，所以由于下一个关节的方向不一致，所以原来的坐标系转过来的时候，需要向公垂线段的方向旋转一下）
4. 坐标系 $\{P\}$ 沿着 $Z_P$ 轴移动连杆轴距 $d_i$ 到达坐标系 $\{i\}$


$$
^{i-1}T = \begin{pmatrix}
1 & 0 & 0 & a_{i-1} \\
0 & \cos \alpha_{i-1} & -\sin \alpha_{i-1} & 0 \\
0 & \sin \alpha_{i-1} & \cos \alpha_{i-1} & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
\cos \theta_i & -\sin \theta_i & 0 & 0 \\
\sin \theta_i & \cos \theta_i & 0 & 0 \\
0 & 0 & 1 & d_i \\
0 & 0 & 0 & 1
\end{pmatrix}= \begin{pmatrix}
\cos \theta_i & -\sin \theta_i & 0 & a_{i-1} \\
\sin \theta_i \cos \alpha_{i-1} & \cos \theta_i \cos \alpha_{i-1} & -\sin \alpha_{i-1} & -\sin \alpha_{i-1} d_i \\
\sin \theta_i \sin \alpha_{i-1} & \cos \theta_i \sin \alpha_{i-1} & \cos \alpha_{i-1} & \cos \alpha_{i-1} d_i \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

$$
^0_N\mathrm{T}=_1^0  \mathrm{T}\cdot_2^1  \mathrm{T}\cdot_3^2  \mathrm{T}......_\mathrm{N}^{\mathrm{N}-1}\mathrm{T}
$$


!!! example "例题"
    === "例1"
        下图所示为一个3关节串联机械臂，该臂的末端装有吸盘作为操作工具。试在此机构上建立几何连杆、写出各连杆参数的值并列出各关节变量
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301175836744.png)

        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301180836339.png)

    === "例2"
        采用非标准D-H方法建立如图机器人的连杆联体坐标系
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301180453199.png)

        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301180849138.png)


    === "正运动学问题"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301181505203.png)
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301181610985.png)

        如果两个轴是平行的，在化简的时候可以使用和角公式进行化简（相当与把两个旋转变成一个等效的角度）

        $$
        ^1T_2 = \begin{pmatrix}
        c\theta_2 & -s\theta_2 & 0 & 0 \\
        0 & 0 & 1 & 0 \\
        -s\theta_2 & -c\theta_2 & 0 & 0 \\
        0 & 0 & 0 & 1
        \end{pmatrix}
        $$

        $$
        ^2T_3 = \begin{pmatrix}
        c\theta_3 & -s\theta_3 & 0 & a_2 \\
        s\theta_3 & c\theta_3 & 0 & 0 \\
        0 & 0 & 1 & d_3 \\
        0 & 0 & 0 & 1
        \end{pmatrix}
        $$

        由于关节2和关节3是平行的，所以 $^1T_2$ 和 $^2T_3$ 的乘积可以用简化的表达式表示：

        $$
        ^1T_3 = ^1T_2 \cdot ^2T_3 = \begin{pmatrix}
        c_{23} & -s_{23} & 0 & a_2 c_2 \\
        0 & 0 & 1 & d_3 \\
        -s_{23} & -c_{23} & 0 & -a_2 s_2 \\
        0 & 0 & 0 & 1
        \end{pmatrix}
        $$

        其中，$c_{23} = \cos(\theta_2 + \theta_3)$，$s_{23} = \sin(\theta_2 + \theta_3)$。
        这种简化在机器人运动学中非常有用，尤其是在处理具有平行关节的机械臂时。


### 变量与不变量
- $a_{i-1}$和$\alpha_{i-1}$是固定不变的参数，不会随着 **关节i** 的运动而变化（这里这里说的是关节i和关节$i-1$的关系）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301190411843.png)
> 这样画可能可以理解关节i的行为不会影响之前的关节参数。
> 而且要注意：**关节的旋转是指绕轴进行转动，而不是轴本身进行转动，第一次看的时候在这里有误区**


- 若关节i是转动关节，则$d_i$是固定不变的参数，$\theta_i$是会随着关节i的运动而变化的关节变量，即：3个连杆参数 $a_{i-1}, \alpha_{i-1}, d_i$；1个关节变量 $\theta_i$
- 若关节i是滑动关节，则$\theta_i$是固定不变的参数，$d_i$是会随着关节i的运动而变化的关节变量，即：3个连杆参数 $a_{i-1}, \alpha_{i-1}, \theta_i$；1个关节变量 $d_i$

- 一个有$N$个关节的串联机构，有$4N$个运动学参量，其中$3N$个是连杆参数、$N$个是关节变量，它们包含了串联机构的全部空间几何信息



## 逆运动学 - 已知位姿求解角度

给定工具坐标系的位置和姿态，解算出个各关节变量

??? info "自由度 - 刚体本身具有可独立运动方向的数目"
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