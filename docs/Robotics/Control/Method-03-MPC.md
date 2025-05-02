# MPC控制

指的是通过模型预测系统在某一未来时间段的表现，进而优化控制量

多用于数位控制，离散时间系统

别名：
- 开环最优反馈
- 反应式规划
- Receding Horizon Control | 滚动优化控制

=== "优势"

    - 考虑未来时域
    - 考虑误差
    - 减少问题规模

=== "缺点"

    - 计算量大
    - 需要在线求解

## Acknowledgement
- DR_CAN [【MPC模型预测控制器】](https://www.bilibili.com/video/BV1SQ4y1Y7FG)系列课程
- 笔记部分参考了[colaforced/ControlTheoryNote](https://github.com/colaforced/ControlTheoryNote/tree/main/MPC)


## 是什么


在$k$时刻

- 估计/测量得到当前状态值（无法测量的话，设计观测器）
- 基于$u(k), u(k+1), \cdots, u(k+N-1)$ 进行优化
  - Cost Function：$J = \sum_{i=k}^{k+N-1} (E_i^T Q E_i + U_i^T R U_i) + E_N^T F E_N$
    - $F$ 是终端惩罚,Terminal cost
  - 预测区间：$\left[y(k+1), y(k+2), \cdots, y(k+N-1)\right]$
  - 控制区间：$\left[u(k), u(k+1), \cdots, u(k+N-1)\right]$
  - N 是预测时域 prediction horizon
  
- 在输出的时候，只执行$u(k)$这一个控制量
- 将预测区间和控制区间后移一个时刻，重复上述过程

约束项:包括等式约束或者不等式约束，比如避障约束

$$
h(x(k), u(k)) = 0\\
g(x(k), u(k)) \leq 0
$$


fix horizon，N 是固定的
预测时间和计算量是一个balance



!!! note "重点"
    - 解十个指令，只执行1个指令
    - 每个状态都可以有当前状态$x(k)$,进行前向积分求得

    

!!! note "terminal cost"

    不想指定最后terminal cost而不加的话，有可能不动

    所以加一个正则项，让他动起来




线性有约束或者非线性有约束需要一些人为的约束


!!! example "无约束MPC = 线性反馈控制"
    一个线性无约束的MPC解析最优解是一个关于初值的最优反馈



## 如何建模

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=720052375&bvid=BV1SQ4y1Y7FG&cid=394181293&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=975621520&bvid=BV1Y44y1b7ke&cid=410625595&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>


我们的任务是最小化代价函数。

$$
\min \; J = \sum_{k}^{N-1}{(X_{(K+i|k)}^T Q X_{(K+i|k)} + U_{(k+i|k)}^T R U_{(K+i|k)})} + X_{(k+N)}^T F X_{(k+N)}
$$

> 其中
> - $X_{(k+i|k)}$ 表示在$k$时刻预测的$k+i$时刻的状态
> - $U_{(k+i|k)}$ 表示在$k$时刻预测的$k+i$时刻的控制量
> - $Q$ 是状态的权重矩阵
> - $R$ 是控制量的权重矩阵
> - $F$ 是终端惩罚

这个方程当中，有$X_{(k+i|k)}$ 和 $U_{(k+i|k)}$ 两个变量，我们又知道对于二次型函数的优化

$$
\min \;\frac{1}{2} x^T P x + q^T x
$$

已经有成熟的方法，所以，我们的目的就是把原有的代价函数，变化到只包含当前状态量$x(k)$（常数）和控制量$u(k)$的函数，只有一个变量之后，就可以套用二次规划的方法求解了。



---


先做一些声明：

状态量：

$$
\hat{X}_k = [X_{(k|k)}, X_{(k+1|k)}, ..., X_{(k+N|k)}]^T
$$

控制量：

$$
\hat{U}_k = [U_{(k|k)}, U_{(k+1|k)}, ..., U_{(k+N-1|k)}]^T
$$

> - $X_{(k|k)} = X_k$ 表示初始状态
> - $X_{(k+1|k)}$ 则是根据模型和 $U_{(k|k)}, X_k$ 计算出来的
> - $X_{(k+1|k)}, ..., X_{(k+N|k)}$ 是进一步迭代计算得到的



研究的是离散形式的状态空间表达式

$$
x(k+1)_{\textcolor{blue}{N \times 1}} = A_{\textcolor{blue}{N \times N}} x(k)_{\textcolor{blue}{N \times 1}} + B_{\textcolor{blue}{N \times P}} u(k)_{\textcolor{blue}{P \times 1}}
$$

把状态空间表达式展开，写成方程组的形式

$$
\left\{
\begin{align*}
    X_{(k|k)} &= X_{k}, \\
    X_{(k+1|k)} &= \textcolor{red}{A}X_{k} + \textcolor{green}{B}U_{k|K}, \\
    X_{(k+2|k)} &= \textcolor{red}{A^2}X_{k} + \textcolor{green}{AB}U_{k|k} + \textcolor{green}{B}U_{k+1|K}, \\
    &\vdots \\
    X_{(k+N|k)} &= \textcolor{red}{A^N}X_{k} + \textcolor{green}{A^{N-1}B}U_{k|K} + \dots +  \textcolor{green}{B}U_{k+N-1|K}
\end{align*}
\right.
$$

可以化简成矩阵的形式（对应元素使用相同颜色进行标注）

$$
\begin{align*}
\hat{X}_k  &= \begin{bmatrix}
    \textcolor{red}{I}  \\
    \textcolor{red}{A}  \\
    \textcolor{red}{A^2}  \\
    \vdots \\
    \textcolor{red}{A^N}
\end{bmatrix}X_k + \begin{bmatrix}
    0 & 0 & \dots & 0  \\
    \textcolor{green}{B} & 0 & \dots & 0 \\
    \textcolor{green}{AB} & \textcolor{green}{B} & \dots & 0 \\
    \vdots & \vdots & \vdots & \textcolor{green}{B} \\
    \textcolor{green}{A^{N-1}B} & \textcolor{green}{A^{N-2}B} & ... &...
\end{bmatrix}\hat{U}_k\\
&= MX_k + C\hat{U}_k
\end{align*}
$$


回顾公式 $J$，我们也可以使用矩阵对于求和项进行化简

$$
\begin{align*}
J &= \sum_{k}^{N-1}{(X_{(K+i|k)}^T \textcolor{green}{Q} X_{(K+i|k)} + U_{(k+i|k)}^T \textcolor{red}{R} U_{(K+i|k)})} + X_{(k+N)}^T \textcolor{green}{F} X_{(k+N)}\\
&= \hat{X}_k^T \begin{bmatrix}
    \textcolor{green}{Q} & 0 & 0 &\dots & 0  \\
    0 & \textcolor{green}{Q} & 0 &\dots & 0 \\
    0 & 0 & \textcolor{green}{Q} & 0& 0 \\
    \vdots & \vdots & 0 &\vdots & 0 \\
    0 & 0 & 0 &0 &\textcolor{green}{F}
\end{bmatrix}\hat{X}_k + \hat{U}_k^T\begin{bmatrix}
    \textcolor{red}{R} & 0 & 0 &\dots & 0  \\
    0 & \textcolor{red}{R} & 0 &\dots & 0 \\
    0 & 0 & \textcolor{red}{R} & 0& 0 \\
    \vdots & \vdots & 0 &\vdots & 0 \\
    0 & 0 & 0 &0 &\textcolor{red}{R}
\end{bmatrix}\hat{U}_k\\
&= \hat{X}_k^T \bar{Q} \hat{X}_k + \hat{U}_k^T \bar{R} \hat{U}_k
\end{align*}
$$

带入刚才求得的 $\hat{X}_k = M\hat{X}_k + C\hat{U}_k$

可以得到

$$
\begin{align*}
J =& \hat{X}_k^T M^T \bar{Q} M \hat{X}_K + \hat{X}_k^T M^T \bar{Q} C \hat{U}_k+ \hat{U}_k^T C^T \bar{Q} M^T \hat{X}_k+ \hat{U}_k^T C^T \bar{Q} C \hat{U}_k + \hat{U}_k^T \bar{R} \hat{U}_k\\
=& \hat{X}_k^T \textcolor{green}{M^T \bar{Q} M} \hat{X}_K + 2\hat{X}_k^T \textcolor{blue}{M^T \bar{Q} C} \hat{U}_k+  \hat{U}_k^T \textcolor{red}{(C^T \bar{Q} C + \bar{R} )} \hat{U}_k \quad \rightarrow \quad \textcolor{gray}{\hat{X}_k^T M^T \bar{Q} C \hat{U}_k = (\hat{U}_k^T C^T \bar{Q} M^T \hat{X}_k)^T \quad \text{constant}}\\
=& \hat{X}_k^T \textcolor{green}{G} \hat{X}_K + 2\hat{X}_k^T \textcolor{blue}{E} \hat{U}_k+ \hat{U}_k^T \textcolor{red}{H} \hat{U}_k\\
\end{align*}
$$


所以最后推导出的代价函数形式：

$$
J ={\hat{X}_k^T G \hat{X}_k} + 2\hat{X}_k^T E \hat{U}_k+ \hat{U}_k^T H \hat{U}_k
$$

此时我们的目标是通过最小化$J$，来求解$\hat{U}_k$，而$\hat{X}_k$是已知的，与优化过程无关

$$
\begin{align*}
\min \; J =&  \hat{X}_k^T G \hat{X}_k + 2\hat{X}_k^T E \hat{U}_k+ \hat{U}_k^T H \hat{U}_k\\
\leftrightarrow
\min \; J =& 2\hat{X}_k^T E \hat{U}_k+ \hat{U}_k^T H \hat{U}_k\\
\leftrightarrow
\min \; J =& \hat{X}_k^T E \hat{U}_k+ \frac{1}{2}\hat{U}_k^T H \hat{U}_k
\end{align*}
$$

观察可得，$2\hat{X}_k^T E \hat{U}_k$ 是一个关于$\hat{U}_k$的线性项，$\hat{U}_k^T H \hat{U}_k$ 是一个关于$\hat{U}_k$的二次型，可以套用二次规划的方法求解

这里也可以直接对$J$ 求梯度

$$
\nabla_{\hat{U}_k}J(\hat{U}_k,\hat{X}_k)=\hat{X}_k^T E + H \hat{U}_k = 0\\ \rightarrow \hat{U}_k^{*}=-  H^{-1}E^T \hat{X}_k
$$

所以最优的控制量是一个关于初值$X_k$的线性反馈

所以无约束MPC其实等价于线性反馈控制（linear feedback control）








### 整理

最后，我们来整理一下整个求解过程当中遇到的矩阵以及它们的维度


$$
x(k+1)_{\textcolor{blue}{N \times 1}} = A_{\textcolor{blue}{N \times N}} x(k)_{\textcolor{blue}{N \times 1}} + B_{\textcolor{blue}{N \times P}} u(k)_{\textcolor{blue}{P \times 1}}
$$



$$
状态量：
\hat{X}_k = \begin{bmatrix}
    X_{(k|k)} \\
    X_{(k+1|k)} \\
    \vdots \\
    X_{(k+N|k)}
\end{bmatrix}_{\textcolor{blue}{(N+1)n \times 1}} 控制量：\hat{U}_k = \begin{bmatrix}
    U_{(k|k)} \\
    U_{(k+1|k)} \\
    \vdots \\
    U_{(k+N-1|k)}
\end{bmatrix}_{\textcolor{blue}{NP \times 1}}
$$


$$
M = \begin{bmatrix}
    I  \\
    A  \\
    A^2  \\
    \vdots \\
    A^N
\end{bmatrix}_{\textcolor{blue}{(N+1)n \times n}} \quad 
C=\begin{bmatrix}0&0&...&0\\\vdots&\vdots&...&\vdots\\0&0&&0\\B_{\textcolor{blue}{n\times P}}&0&...&0\\AB_{\textcolor{blue}{n\times P}}&B&...&0\\\vdots&\vdots&\ddots&0\\A^{N-1}B&A^{N-2}B&...&B\end{bmatrix}_{\textcolor{blue}{(1+N)n\times NP}}
$$

B是$n \times p$的矩阵，AB也是$n \times p$的矩阵


$$
\hat{X}(k)_{\textcolor{blue}{(N+1)n \times 1}}=M_{\textcolor{blue}{(N+1)n \times n}}x(k)_{\textcolor{blue}{n \times 1}}+C_{\textcolor{blue}{(N+1)n \times NP}}\hat{U}(k)_{\textcolor{blue}{NP \times 1}}
$$








## 代码实现

核心公式

$$
\hat{X}(k) = Mx(k) + C\hat{U}(k)
$$


$$
\min \; J = 2\hat{X}_k^T E \hat{U}_k+ \hat{U}_k^T H \hat{U}_k
$$

- $E = C^T \bar{Q} M,\quad H = C^T \bar{Q} C + \bar{R}$

所以，计算$E$和$H$需要$A,B,Q,R,F,N$
> - $C$:$A,B$
> - $M$:$A$
> - $\bar{Q}$:$Q,F$
> - $\bar{R}$:$R$



```matlab title="MPC_Test.m"
clear ; 
close all; 
clc;

%% 第一步，定义状态空间矩阵
A = [1 0.1; -1 2]; %% 定义状态矩阵 A, n x n 矩阵
n= size (A,1);

B = [ 0.2 1; 0.5 2]; %% 定义输入矩阵 B, n x p 矩阵
p = size(B,2);

Q=[100 0;0 1]; %% 定义Q矩阵，n x n 矩阵
F=[100 0;0 1]; %% 定义F矩阵，n x n 矩阵
R=[1 0 ;0 .1]; %% 定义R矩阵，p x p 矩阵

k_steps=100; %% 定义step数量k
X_K = zeros(n,k_steps); %% 定义矩阵 X_K， n x k 矩 阵
X_K(:,1) =[20;-20]; %% 初始状态变量值， n x 1 向量
U_K=zeros(p,k_steps); %% 定义输入矩阵 U_K， p x k 矩阵

N=5; %% 定义预测区间K
[E,H]=MPC_Matrices(A,B,Q,R,F,N);  %% Call MPC_Matrices 函数 求得 E,H矩阵

%% 计算每一步的状态变量的值
for k = 1 : k_steps 

    %% 求得U_K(:,k)
    U_K(:,k) = Prediction(X_K(:,k),E,H,N,p);

    %% 计算第k+1步时状态变量的值
    X_K(:,k+1)=(A*X_K(:,k)+B*U_K(:,k));

end

%% 绘制状态变量和输入的变化
subplot  (2, 1, 1);
hold;
for i =1 :size (X_K,1)
    plot (X_K(i,:));
end
legend("x1","x2")
hold off;

subplot (2, 1, 2);
hold;
for i =1 : size (U_K,1)
    plot (U_K(i,:));
end
legend("u1","u2")
```

```matlab title="MPC_Matrices.m"
function  [E,H]=MPC_Matrices(A,B,Q,R,F,N)

    n = size(A,1);   % A 是 n x n 矩阵, 得到 n
    p = size(B,2);   % B 是 n x p 矩阵, 得到 p

    %% 定义M和C 
    M = [eye(n);zeros(N*n,n)];                    % 初始化 M 矩阵. M 矩阵是 (N+1)n x n的， 它上面是 n x n 个 "I", 这一步先把下半部分写成 0
    C = zeros((N+1)*n,N*p);                       % 初始化 C 矩阵, 这一步令它有 (N+1)n x NP 个 0
    tmp = eye(n);                                 %定义一个n x n 的 I 矩阵

    %%　更新M和C
    for i=1:N % 循环，i 从 1到 N
        rows = i*n+(1:n);                         %定义当前行数，从i x n开始，共n行 
        C(rows,:) = [tmp*B,C(rows-n, 1:end-p)];   %将c矩阵填满
        tmp = A*tmp;                              %每一次将tmp左乘一次A
        M(rows,:) = tmp;                          %将M矩阵写满
    end 

    %% 定义Q_bar和R_bar
    Q_bar = kron(eye(N),Q);
    Q_bar = blkdiag(Q_bar,F);
    R_bar = kron(eye(N),R); 

    %% 计算G, E, H
    G = M'*Q_bar*M;                               % G: n x n
    E = C'*Q_bar*M;                               % E: NP x n
    H = C'*Q_bar*C+R_bar;                         % NP x NP 

end
```

```matlab title="Prediction.m"
function u_k= Prediction(x_k,E,H,N,p)
    
    U_k = zeros(N*p,1);             % NP x 1
    U_k = quadprog(H,E*x_k);
    u_k = U_k(1:p,1);               % 取第一个结果

end
```

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=597117364&bvid=BV11B4y1X78N&cid=735160025&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>


## Papers & Applications
### MPCC - Model Predictive Contouring Control


但在无人驾驶方程式大赛中，走赛道中心线显然不是最优路线，在不依靠路径优化的情况下，如何走出最短的路线，这就是MPCC希望解决的。

他的核心思想就是车辆的行驶路程（Frenet坐标系的s）也放到MPC的状态量。例如，当前s=1m，在预测域中，s = 1.1，s = 1.2，s = 1.3，s = 1.4，s = 1.5，在计算跟踪误差时，就可以根据s插值得到在每个步长下的期望参考点


[[MPCC in FSAC | Casadi]基于MPCC的无人系统控制设计思路-CSDN博客](https://blog.csdn.net/vonct/article/details/134781569)



MPC and MHE implementation in Matlab using Casadi - Workshop
<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=95675332&bvid=BV1LE411j75o&cid=163328476&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"></iframe>

- 作者的代码在[MPC-and-MHE-implementation-in-MATLAB-using-Casadi](https://github.com/MMehrez/MPC-and-MHE-implementation-in-MATLAB-using-Casadi)
- [网友优化版本](https://github.com/lzlbadguy/Lane-change-MPC-for-dynamic-bicycle-model-using-CasADi-with-Matlab)

> [CasADi](https://web.casadi.org/) is an open-source tool for nonlinear optimization and algorithmic differentiation.

### 自动驾驶 & RC小车轨迹控制

有障碍物的轨迹控制
[alexliniger/MPCC: Model Predictive Contouring Controller (MPCC) for Autonomous Racing](https://github.com/alexliniger/MPCC)


![](https://github.com/alexliniger/MPCC/raw/master/Images/MPC_sim.gif)




[Optimization‐based autonomous racing of 1:43 scale RC cars - Liniger - 2015](https://onlinelibrary.wiley.com/doi/full/10.1002/oca.2123)
提出了两种不同的控制方案。

- 第一个控制器采用两级结构，由路径规划器和用于跟踪的非线性模型预测控制器（NMPC）组成。
- 第二个控制器将这两个任务结合在一个非线性优化问题（NLP）中，遵循轮廓控制的思想。通过线性化获得的线性时变模型用于在每个采样时间构建控制NLP的局部近似，形成凸二次规划（QP）。生成的QP具有典型的MPC结构，障碍物规避通过基于动态规划的高级走廊规划器实现，该规划器根据对手的当前位置和赛道布局为控制器生成凸约束。
- 实验平台：控制性能通过使用1:43比例的RC赛车进行实验研究，这些赛车以超过3 m/s的速度行驶，并在后轮胎力饱和（漂移）的操作区域内运行。算法在嵌入式计算平台上以50 Hz的采样率运行，展示了基于优化的方法在自动驾驶中的实时可行性和高性能。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250502203924.png)

<iframe width="560" height="315" src="https://www.youtube.com/embed/ioKTyc9bG4c?si=qGy-q34mUUqRq74R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



> **Related links**
> - 论文中用到的RC小车是[ミニッツRWD MR-04 レディセット シボレー コルベット C8.R ガンメタル / レッド 32356GMR - KYOSHO RC](https://rc.kyosho.com/en/rccar/miniz/mini-zrwd/32356gmr.html)
> - RCFans论坛上有搭建轨道的教程[RCFans论坛 【自建赛道】 完成 【制作全过程分享】 - Powered by Discuz!](https://www.rcfans.com/thread-807710-1-1.html)
> - [开源！手把手教你搭建阿克曼自动驾驶小车（上） - 知乎](https://zhuanlan.zhihu.com/p/499251426)



### 机器人当中应用

- 非线性MPC用于容错控制


- Whole-body MPC用于轮腿机器人






### 飞机轨迹控制

[ZJU-FAST-Lab/CMPCC: CMPCC: Corridor-based Model PredictiveContouring Control for Aggressive Drone Flight](https://github.com/ZJU-FAST-Lab/CMPCC)

![](https://github.com/ZJU-FAST-Lab/CMPCC/blob/master/figs/1.gif)

### 桨叶失效控制

Fault-Tolerant MPC 问题构建:

$$
\min_{u_{k:k+N-1}} y_{N}^{T} Q_{N} y_{N} + \sum_{i=k}^{k+N-1} y_{i}^{T} Q y_{i} + u_{i}^{T} R u_{i}
$$

$$
\begin{aligned}
s.t.\quad & x_{i+1} = f(x_{i}, u_{i}) \quad i = k, k+1, \ldots, k+N-1 \\
& \underline{u} \leq u \leq \bar{u}.
\end{aligned}
$$

$$
y_{i} = \left[\begin{array}{c}
p - p_{\text{ref}} \\
q_{xy,x}^{2} + q_{xy,y}^{2} \\
q_{z,z} \\
v - v_{\text{ref}} \\
\omega - \omega_{\text{ref}} \\
t - t_{\text{ref}} \\
u - u_{\text{ref}}
\end{array}\right]
$$

- 正常飞行:$\bar{u} = T_{\max} 1_{4 \times 1}$
- 单桨失效:$\bar{u}_{i} = \underline{u}_{i} = 0$

$$
\begin{aligned}
q_{e} &= q_{z} \circ q_{xy}\\
q_{z} &= \left[\begin{array}{llll}
q_{z,w} & 0 & 0 & q_{z,z}
\end{array}\right]^{T}\\
q_{xy} &= \left[\begin{array}{cccc}
q_{xy,w} & q_{xy,x} & q_{xy,y} &0
\end{array}\right]^{T}
\end{aligned}
$$


### 飞行吊载控制

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250502210334.png)