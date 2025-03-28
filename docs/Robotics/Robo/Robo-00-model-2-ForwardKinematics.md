# 02 | 正运动学 - 已知角度求末端位姿

本章的**正运动学**问题，就是**将关节空间转化到笛卡尔空间**当中去。

我们的目的就是获取机械臂末端相对于机械臂基座的位姿，首先要建立起连杆之间的变换关系，这里比较重要的搞明白连杆坐标系的**建立**以及**变换**（先建立，再变换）

=== "关节空间 (Joint Space)"
    关节空间是通过机器人的关节参数来描述机器人配置的空间。在关节空间中，机器人的每个关节都有一个关联的参数，如角度或距离，这些参数描述了机器人的当前配置。<br>
    在关节空间中，机器人的运动是通过改变关节参数来实现的，例如，改变关节角或关节位置。
    关节空间分析是机器人运动学和控制的基础，它为控制算法和路径规划提供了一个直观的框架。
=== "笛卡尔空间 (Cartesian Space)"
    笛卡尔空间是通过笛卡尔坐标系统来描述机器人末端执行器（例如机器人手或工具）的位置和方向的空间。<br>
    在笛卡尔空间中，机器人的运动是通过改变末端执行器的位置和方向来实现的，通常使用x, y, z坐标和欧拉角或四元数来描述末端执行器的位置和方向。笛卡尔空间分析为机器人的任务规划和执行提供了一个直观和可视化的框架，它使得能够直接描述和控制机器人在物理世界中的运动。


## 连体坐标系建立
我觉得下面这一篇博文图片和解释比较清楚，这里要着重区别一下连杆转角和关节角

>[机械臂运动学基础\_关节角和连杆转角的区别](https://blog.csdn.net/qq_38962956/article/details/124851477)
>[机器人学：DH参数总结（传统DH方法和改进DH方法）](https://blog.csdn.net/subtitle_/article/details/130982929)



**坐标系建立规则**(非标准D-HDenavit-Hartenberg方法)


- 根据题目信息确定式R(revolute joint)还是P(prismatic joint)固定在关节轴i上的坐标系命名为坐标系$\{i\}$（轴i的方向由设计者给定）
- **先确定$Z$轴**，坐标系$\{i\}$的Z轴与关节轴i的轴线重合
- **再确定原点**，坐标系$\{i\}$的原点为公共垂线ai与关节轴i轴线的交点
- **再确定$X$轴**，$\{i\}$的X轴与公共垂线ai重合
- **最后确立$Y$轴**，根据右手定则确定坐标系 $\{i\}$ 的Y轴(大拇指指向 $Z$,右手螺旋确定)

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
    Modified DH方法是XZ类变换：先绕着i坐标系的的$X_i$轴旋转和平移，再绕着坐标系i的$Z_i$轴进行旋转和平移；(题目中使用这种方法)


!!! question "这里各种DH的方法没有太搞清楚"
    之前看到知乎上


### 运动学参量

- 连杆扭转角$\alpha_{i-1}$：绕$X_{i-1}$轴，从$Z_{i-1}$轴旋转到Zi轴的角度
- 连杆长度$a_{i-1}$：沿$X_{i-1}$轴，从$Z_{i-1}$轴移动到Zi轴的距离（公垂线段为0的时候，当 $a_{i-1} = 0$ 时，我们并不将零长度的 $r_{O_{i-1}P_i}$ 视为传统的零向量，而是在与轴 $i-1$ 和轴 $i$ 同时垂直的方向中选一个作为 $r_{O_{i-1}P_i}$ 的正方向）
- 关节角$\theta_i$：沿$Z_{i-1}$轴，从$X_{i-1}$轴旋转到$X_i$轴的角度
- 连杆轴距$d_i$：沿$Z_{i-1}$轴，从$X_{i-1}$轴移动到$X_i$轴的距离


## 连体坐标系变换

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301174641450.png)



$^{i-1}_i \!T$ 表示坐标系 $\{i-1\}$ 到坐标系 $\{i\}$ 的变换矩阵，i从1开始

$$
^{i-1}_i \!T = \begin{pmatrix}
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

1. **调整$Z$轴，绕$X$旋转**——坐标系 $\{i-1\}$ 绕 $X_{i-1}$ 轴旋转连杆扭转角 $\alpha_{i-1}$ 到达坐标系 $\{R\}$
2. **沿着$X$轴平移**——坐标系 $\{R\}$ 沿着 $X_R$ 轴移动连杆长度 $a_{i-1}$ 到达坐标系 $\{Q\}$
3. **调整$X$轴,绕$Z$旋转**——坐标系 $\{Q\}$ 绕 $Z_Q$ 轴旋转关节角 $\theta_i$ 到达坐标系 $\{P\}$（因为坐标系的方向是根据公垂线段定义的，所以由于下一个关节的方向不一致，所以原来的坐标系转过来的时候，需要向公垂线段的方向旋转一下）
4. **沿着$Z$轴平移**——坐标系 $\{P\}$ 沿着 $Z_P$ 轴移动连杆轴距 $d_i$ 到达坐标系 $\{i\}$

!!! tip "理解变换中的变量和不变量"
      - $a_{i-1}$和$\alpha_{i-1}$是固定不变的参数，不会随着 **关节i** 的运动而变化（这里这里说的是关节i和关节$i-1$的关系）

      ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250301190411843.png)
      > 这样画可能可以理解关节i的行为不会影响之前的关节参数。
      > 而且要注意：**关节的旋转是指绕轴进行转动，而不是轴本身进行转动，第一次看的时候在这里有误区**


      - 若关节i是转动关节，则$d_i$是固定不变的参数，$\theta_i$是会随着关节i的运动而变化的关节变量，即：3个连杆参数 $a_{i-1}, \alpha_{i-1}, d_i$；1个关节变量 $\theta_i$
      - 若关节i是滑动关节，则$\theta_i$是固定不变的参数，$d_i$是会随着关节i的运动而变化的关节变量，即：3个连杆参数 $a_{i-1}, \alpha_{i-1}, \theta_i$；1个关节变量 $d_i$

      - 一个有$N$个关节的串联机构，有$4N$个运动学参量，其中$3N$个是连杆参数、$N$个是关节变量，它们包含了串联机构的全部空间几何信息

## 题型



### 列写运动学参量表

注意坐标系轴要建立正确

$a_i$的求解：相当于求异面直线之间的距离，可以采用

$$
a = \frac{|\vec{M_1M_2} \cdot (\vec{i_1} \times \vec{i_2})|}{|\vec{i_1} \times \vec{i_2}|}
$$



!!! example "运动学参量表的计算"
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

### 列写齐次变换矩阵

写齐次变换矩阵的时候，可以从**基向量表出**的角度进行。使用原坐标系表示现在坐标系的基

这样在 $\alpha_{i-1}$ 为0或$\pm\frac{\pi}{2}$的时候，可以简化计算。


### 求末端位置与姿态


**方法1**: 几何法转换为三角函数问题（仅适用于平面问题,即$\alpha_i$为0的时候，比较方便）


**方法2**: 矩阵法（适用于任意维度）

$$
^0_N\mathrm{T}=_1^0  \mathrm{T}\cdot_2^1  \mathrm{T}\cdot_3^2  \mathrm{T}......_\mathrm{N}^{\mathrm{N}-1}\mathrm{T}= \begin{bmatrix} R & ^0\!P_N \\ 0 & 1 \end{bmatrix} \in \mathbb{R}^{4 \times 4}
$$

其中，向量 $\vec{P}$ 代表了机器人末端相对于机器人基座的位置，矩阵 $R$ 代表了机器人末端相对于机器人基座的姿态（如果要求解角度的话，相当于旋转矩阵转换为欧拉角）

!!! tip "Casio fx-991 CNX 计算器的矩阵计算方法需要掌握（参考`/环境配置/计算器`页面）"

### 使用Matlab求解

给定DH参数表，计算$^0_N\mathrm{T}$

在化简的过程当中，常常苦恼化简太慢的问题。而且casio等计算器并不能处理带符号的化简。

在室友的介绍下，学了一下Matlab的符号计算方法，还是比较好用的。


```matlab title="解算步骤" hl_lines="6"
function T_final = compute_DH(DH_params)
    n = size(DH_params, 1);  % Number of joints
    T_final = eye(4);
    
    for i = 1:n
        % Extract DH parameters for joint i, attention the order!
        theta_i = DH_params(i, 4);
        d_i = DH_params(i, 3);
        a_i_minus_1 = DH_params(i, 2);
        alpha_i_minus_1 = DH_params(i, 1);
        
        T_i = [
            cos(theta_i), -sin(theta_i), 0, a_i_minus_1;
            sin(theta_i) * cos(alpha_i_minus_1), cos(theta_i) * cos(alpha_i_minus_1), -sin(alpha_i_minus_1), -sin(alpha_i_minus_1) * d_i;
            sin(theta_i) * sin(alpha_i_minus_1), cos(theta_i) * sin(alpha_i_minus_1), cos(alpha_i_minus_1), cos(alpha_i_minus_1) * d_i;
            0, 0, 0, 1
        ];
        fprintf('T_%d = \n', i);
        disp(T_i);
        T_final = T_final * T_i;
    end
    fprintf('Final Transformation Matrix T = \n');
    disp(T_final);
end
```



```matlab title="使用示例"
syms theta_1 theta_2 theta_3 L_1 L_2 L_3;

# order: alpha,a,d,theta
DH_params = [
    0,0,0, theta_1;
    pi/2, L_1, 0, theta_2;
    0,L_2,0,theta_3;
    0,L_3,0,0;
];

T_final = compute_DH(DH_params);
```

效果

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250310162148977.png)