# 机器人建模

!!! note "课程信息"
    - 名称：机器人建模与控制
    - 授课教师：zrh

要是讲解机械臂相关的知识，包括空间描述与变换（旋转矩阵、齐次变换矩阵、欧拉角、等效轴角、四元数）、正运动学（关节参数、改进DH参数）、逆运动学（解析法、数值法）、静力学、雅可比、动力学（拉格朗日方程、牛顿欧拉方程）、轨迹规划、控制（位置控制、力控制）等等




**正运动学**：已知角度求末端执行器位姿

**逆运动学**：已知位姿求解角度

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250217105608273.png)

**关节空间**

> 关节坐标是指描述机械臂中各个关节角度的坐标系。在关节坐标系中，每个关节的角度都被独立地表示出来，通过这些角度的变化，可以实现机械臂的运动。

**笛卡尔空间**

> 笛卡尔坐标系是一种常用的直角坐标系，它由三条相互垂直的坐标轴组成，分别为X轴、Y轴和Z轴。在笛卡尔坐标系中，任何点的位置都可以由这三个轴上的坐标值唯一确定。



**自由度**

手臂：7自由度；腿：6自由度

定义：刚体本身具有可独立运动方向的数目。

$$
F = 6(l - n - 1) + \sum_{i = 1}^{n}f_{i} \\
l为连杆数（包括基座），n为关节总数，f_i为第i个关节的自由度数
$$



6自由度DOF 8个解

7个自由度DOF 无穷多个解

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/017a2277142fe6ab01f933ad81c3e281_1440w.webp" alt="img" style="zoom:50%;" />

> 一个6自由度的机械手，即使某两组构型对应的末端机构的三维位置相同，机械手在从一个构型移动到另一个构型的时候无法保持末端机构始终不动。
>
> 如果有人在电视里看过工业机器人焊东西的话，就会发现它在同一个位置焊接的时候，一会儿整个扭到这边，一会儿整个扭到那边，看起来非常酷炫的样子。事实上这么做只是因为，虽然焊接只是想改变末端机构的朝向，而不改变末端机构的位置，但是由于定理的限制，它必须要往后退一些，然后各种扭，才能保证在移动末端机构的朝向的过程中不会撞到东西，因为移动的时候末端机构的三维位置一定会乱动。如果它能够随便转一点点就可以达到目的，还费那个力气酷炫地整体都转起来干啥……
>
> 而多了一个自由度以后就不一样了。
>
> 想想开门时拧钥匙的动作，这个情况下是人胳膊的末端机构（手）的三维位置没有变（始终在钥匙孔前），但是末端机构（手）的三维旋转变了（转动了钥匙）。人能够实现这个简单的动作，就是因为我们的胳膊有7个自由度。

## 坐标系与表示

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

**性质**
- 旋转矩阵是正交矩阵，即$^A_B\!R^T = ^A_B\!R^{-1} = ^B_A\!R$
- 旋转矩阵的行列式为1，即$\det(^A_B\!R) = 1$


SO3：Special Orthogonal Group 三维特殊正交群

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


### 旋转平移 - 齐次变换矩阵

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

### 右乘连体左乘基

1. 对于两个变换的叠加：$M_2M_1$表示先进行$M_1$变换，再进行$M_2$变换，这里$M_1$、$M_2$都是自然基坐标系下。
2. 如果$M_2$变换是在$M_1$坐标系基础上进行的，那么根据相似矩阵把$M_2$转换成自然基坐标系下：$M_1M_2M_1^{-1}$
3. 那么两个变换叠加就是：$(M_1M_2M_1^{-1})M_1 = M_1M_2$

这是一个很有意思的现象，如果每个变换都是在上个变换基础上进行的，那么只要把矩阵顺序反过来即可：

- 所有变换都在自然基下：$M_4M_3M_2M_1$
- 每个变换在前一个变换后的坐标系下：$M_1M_2M_3M_4$


> 可以参考3b1b基坐标变换的视频

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=44855426&bvid=BV1ib411t7YR&cid=80579031&p=13&t=620&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=600px></iframe>



!!! example "例子"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250224160846651.png)

### 欧拉角 - 三个轴次序转动

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

    ![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-9e1b5ce7917863ea39d34e84f3884faa_1440w.webp)






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



#### 是否一一对应呢？




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


- 各种欧拉角，中间的旋转角在$\left[ -\frac{\pi}{2}, \frac{\pi}{2}\right]$的时候，可以求出唯一对应
- 如果不在$\left[ -\frac{\pi}{2}, \frac{\pi}{2}\right]$，则有无穷解


#### 万向节死锁（Gimbal Lock）

同一姿态可以用无穷组欧拉角（固定角）表示


!!! note "简单例子"
    [无伤理解欧拉角中的“万向死锁”现象](https://www.bilibili.com/video/BV1Nr4y1j7kn)
    站起来，y轴朝天，x轴两臂，z轴朝前；
    顺序：YXZ：沿Y轴转，就是转下身；沿X轴转，就是抬头；沿Z轴转，就是保持脸的朝向不变，把头扭一下，就像歪头一样
    
    那么接下来按照以下顺序转：转身转过随便一个角度，然后抬头90度直朝天，然后再随便歪头歪一个角度（注意歪头时脸的朝向是不变的）那么你就会发现，歪头的效果跟开始转身的效果是一样的如果歪头的角度和转身的角度相等但是方向相反，那么就可以相互抵消

对欧拉角的变换是有序的 。欧拉角只记录结果，不记录过程

欧拉角描述相对于初始状态的变换，只和最终状态有关，与过程无关。（外边的轴转动会带动里面的轴转动）


### 四元数

四维空间中的双旋转


[四元数的可视化-3b1b](https://www.bilibili.com/video/BV1SW411y7W1/)

[四元数和三维转动2-3b1b](https://www.bilibili.com/video/BV1Lt411U7og/)

[Visualizing quaternions, an explorable video series](https://eater.net/quaternions)

[三维旋转：欧拉角、四元数、旋转矩阵、轴角之间的转换 - 知乎](https://zhuanlan.zhihu.com/p/45404840)

[欧拉角（易理解）](https://blog.csdn.net/ODDYOU/article/details/119976130)

[评论区pdf](https://krasjet.github.io/quaternion/)


```python
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建一个 3D 绘图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义一个向量
vec = np.array([1, 0, 0])

# 绘制原始向量
ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='b', label='Original Vector')

# 定义一个四元数 (90度绕z轴旋转)
r = R.from_quat([0, 0, np.sin(np.pi/4), np.cos(np.pi/4)])

# 旋转向量
rotated_vec = r.apply(vec)

# 绘制旋转后的向量
ax.quiver(0, 0, 0, rotated_vec[0], rotated_vec[1], rotated_vec[2], color='r', label='Rotated Vector')

# 设置坐标轴限制
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# 添加标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 显示图例
ax.legend()

# 显示绘图
plt.show()
```


## 正运动学
各个关节变量的函数，描述了工具坐标系相对于基坐标系的位置和姿态



## 逆运动学

给定工具坐标系的位置和姿态，解算出个各关节变量

## 速度与静力



讲关节空间速度映射到笛卡尔空间速度，通过雅可比矩阵描述