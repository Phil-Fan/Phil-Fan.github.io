# 06 | 动力学

主要讲解牛顿-欧拉迭代动力学方程和拉格朗日动力学方程。

## 前置知识

### 叉乘运算

**叉乘** $\mathbf{a} \times \mathbf{b}$是向量运算，结果为一个向量，遵循以下规则：  

1. **基本法则**：  
   - **反交换律**：$\mathbf{a} \times \mathbf{b} = -\mathbf{b} \times \mathbf{a}$
   - **分配律**：$\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$ 
   - **标量兼容性**：$\lambda (\mathbf{a} \times \mathbf{b}) = (\lambda \mathbf{a}) \times \mathbf{b} = \mathbf{a} \times (\lambda \mathbf{b})$  

2. **几何意义**：  
   - **模长**：$|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta$,$\theta$ 为两向量夹角，对应以 $\mathbf{a}, \mathbf{b}$ 为邻边的平行四边形面积。  
   - **方向**：垂直于 $\mathbf{a}$ 和 $\mathbf{b}$ 所在平面，遵循**右手定则**（四指从 $\mathbf{a}$ 转向 $\mathbf{b}$，拇指方向为结果方向）。  

3. **混合运算**：  
   - **混合积**：$(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c}$ 表示平行六面体体积，满足轮换对称性：$(\mathbf{a} \times \mathbf{b}) \cdot \mathbf{c} = (\mathbf{b} \times \mathbf{c}) \cdot \mathbf{a} = (\mathbf{c} \times \mathbf{a}) \cdot \mathbf{b}$
   - **拉格朗日公式**：$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = \mathbf{b}(\mathbf{a} \cdot \mathbf{c}) - \mathbf{c}(\mathbf{a} \cdot \mathbf{b})$

力矩：$\tau = r \times F$

### 分析力学基础
- 拉格朗日力学
  - 达朗贝尔原理
  - 拉格朗日方程；拉格朗日关系
- 哈密顿力学
  - 哈密顿原理

[从零学分析力学（拉格朗日力学篇） - 知乎](https://zhuanlan.zhihu.com/p/156760739)


牛顿力学又称为矢量力学，基于相对性原理和伽利略变换。
但是在描述复杂系统（如单摆）的时候，比较复杂。所以使用广义坐标来描述系统的状态。

广义坐标：不是特定坐标，描述力学系统状态即可；

力学系统所受理想约束力所做的虚功为0


<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=210135201&bvid=BV1za41167an&cid=471387902&p=1&autoplay=0 " scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width= 80% height = 600px></iframe>

### 达朗贝尔原理：拉格朗日力学中的第二个基本原理

$$
\sum_{i=1}^{n} (\vec{F}_i - m_i \ddot{\vec{r}}_i) \cdot \delta \vec{r}_i = 0
$$

没有约束的情况下，$\delta \vec{r}_i$相互独立，所以前面系数为0，即牛顿第二定律

### 拉格朗日方程：描述物体运动的方程

> 地位如同牛顿第二定律

- $\delta$ 与 $d$ 运算规则基本相同
- 消去的一个思路：利用广义坐标相互独立，所以系数为0
- 另一个思路：矢量的化简比较复杂，标量化简较为简单

拉格朗日函数：$L = T-U$ 只在保守系下成立，$T$为动能，$U$为势能

$$
Q_a = \frac{d}{dt} \left( \frac{\partial T}{\partial \dot{q}_a} \right) - \frac{\partial T}{\partial q_a} = 0
$$

T: 动能,$q_a$广义坐标，$\dot{q}_a$广义速度，$Q_a$广义力,广义动量$P_{\alpha} = \frac{\partial T}{\partial \dot{q_\alpha}}$


$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}_a} \right) - \frac{\partial L}{\partial q_a} = 0
$$

保守体系下，完整系统的拉格朗日方程



### 泛函求极值；欧拉方程

欧拉-拉格朗日方程

$$
\frac{d}{dx}\left( \frac{\partial F}{\partial \dot{y}} \right) - \frac{\partial F}{\partial y} = 0
$$

欧拉方程是泛函求极值的一个条件，形式和保守体系下的拉格朗日方程类似。

所以隐含着：物体的运动对应着某个量取极值


### 哈密顿原理

系统的运动是使作用量$S$取得极值的运动，也就是说物理系统倾向于选择更省力、更节能的方式来运动

$$
Energy = K + U = \sum_{i=1}^{n} \frac{1}{2} m_i \dot{r}_i^2 + \sum_{i=1}^{n} m_i g h_i
$$

Hamiltonian：哈密顿量，系统的总能量

$H = K+U$

$$
H = \frac{P^2}{2ml^2} - mgl \cos(\theta)
$$

满足两个一阶微分方程

$$
\dot{q} = \frac{\partial H}{\partial P}, \dot{P} = -\frac{\partial H}{\partial q}
$$

把运动化到了face space上面；知道了任意一点的位置和动量，就可以知道它的运动轨迹；


<iframe src="https://static1.squarespace.com/static/611b0e99ffc7aa45df0df283/t/664509416beeaf1f4526e773/1715800385413/Problem+Sheet.pdf" width="100%" height="600px" style="border: none;" title="Problem Sheet PDF">
This browser does not support PDFs.
</iframe>

[Solutions to the Problem Sheet: Lagrangian and Hamiltonian Mechanics in Under 20 Minutes — Physics with Elliot](https://www.physicswithelliot.com/store/p/lagrangian-hamiltonian-mini-solution)



## 惯性张量
> 参考资料：
> [转动惯量、惯性张量、转动动能的推导 - 知乎](https://zhuanlan.zhihu.com/p/672567095)
> [机器人动力学建模之理解惯性张量-CSDN博客](https://blog.csdn.net/handsome_for_kill/article/details/104615496)


### 转动惯量

引入力矩后，将一个物体看做由无数个质点组成，该物体在绕着某个轴转动时，除了轴处的质点，其余质点以到轴的距离为半径做圆周运动。为了更方便地研究转动，还需要定义出一些描述转动的物理量，如角位移，角速度，角加速度，可以理解为转动的位移，转动的快慢和转动状态变化的快慢，与描述平动的物理量对应。

从牛顿定律出发，可以推导出一个结论，物体转动的加速度——角加速度，与该物体受到的合力矩成正比（听起来很像牛顿第二定律对吧），比例系数是个与物体本身的质量，和物体质量相对于转轴分布情况有关的量。这就是转动惯量。转动惯量与质量对应，描述物体转动时的惯性。受到相同的力矩，转动惯量越大的物体，角加速度越小。

### 惯性张量

转动惯量是绕着某个轴的，而惯性张量是绕着某个点的。

绕着x、y、z三个轴转动惯量恰好就是惯性张量的三个对角元素$I_{xx}, I_{yy}, I_{zz}$(称为惯性矩)

非对角元素称为惯性积


### 平移

### 旋转


### 与其他物理量的联系





## 迭代动力学方程

### 外推法

| **物理量**       | **公式**|
|------------------|-----------------------|
| **角速度**       | $^{i+1}\omega_{i+1} = {}^{i+1}_i R \cdot {}^i \omega_i$|
| **角加速度**     | $^{i+1}\dot{\omega}_{i+1} = {}^{i+1}_i R \cdot {}^i \dot{\omega}_i$|
| **加速度**       | $^{i+1}\dot{v}_{i+1} = {}^{i+1}_i R \left[ {}^i \dot{\omega}_i \times O_{i+1} + {}^i \omega_i \times \left( {}^i \omega_i \times ^iO_{i+1} \right) + {}^i \dot{v_i} \right] + 2 \cdot {}^{i+1} \omega_{i+1} \times \dot{d}_{i+1} ^{i+1} \hat{Z}_{i+1}  \ + \ \ddot{d}_{i+1}\cdot {}^{i+1} \hat{Z}_{i+1}$ |
| **质心加速度**   | $^{i+1}\dot{v}_{C_{i+1}} = {}^{i+1}_i \dot{\omega}_{i+1} \times {}^{i+1} P_{C_{i+1}} + {}^{i+1} \omega_{i+1} \times \left( {}^{i+1} \omega_{i+1} \times {}^{i+1} P_{C_{i+1}} \right) + {}^{i+1} \dot{v}_{i+1}$ |
| **力**           | $^{i+1} F_{i+1} = m_{i+1} \cdot {}^{i+1}_i \dot{v}_{C_{i+1}}$ |
| **力矩**         | $^{i+1}N_{i+1} = {}^{C_{i+1}} I_{i+1} \cdot {}^{i+1}\dot{\omega}_{i+1} + {}^{i+1} \omega_{i+1} \times{}^{C_{i+1}} I_{i+1} \cdot {}^{i+1} \omega_{i+1}$ |


转动

| **物理量**       | **公式** |
|------------------|-------------------|
| **角速度**       | $^{i+1}\omega_{i+1} ={}^{i+1}_i R \cdot {}^i \omega_i + \dot{\theta}_{i+1} \cdot {}^{i+1} \hat{Z}_{i+1}$ |
| **角加速度**     | $^{i+1}\dot{\omega}_{i+1} ={}^{i+1}_i R \cdot {}^i \dot{\omega}_i + {}^{i+1}_i R \cdot {}^i \omega_i \times  \dot{\theta}_{i+1} \cdot {}^{i+1} \hat{Z}_{i+1} + \ddot{\theta}_{i+1} \cdot {}^{i+1} \hat{Z}_{i+1}$ |
| **加速度**       | $^{i+1}\dot{v}_{i+1} ={}^{i+1}_i R \left[ {}^i \dot{\omega}_i \times O_{i+1} + {}^i \omega_i \times \left( {}^i \omega_i \times {}^iO_{i+1} \right) + {}^i \dot{v_i} \right]$   |
| **质心加速度**   | $^{i+1}\dot{v}_{C_{i+1}} ={}^{i+1}_i \dot{\omega}_{i+1} \times {}^{i+1} P_{C_{i+1}} + {}^{i+1} \omega_{i+1} \times \left( {}^{i+1} \omega_{i+1} \times {}^{i+1} P_{C_{i+1}} \right) + {}^{i+1} \dot{v}_{i+1}$ |
| **力**           | $^{i+1} F_{i+1} =m_{i+1} \cdot {}^{i+1}_i \dot{v}_{C_{i+1}}$ |
| **力矩**         | $^{i+1}N_{i+1} ={}^{C_{i+1}} I_{i+1} \cdot {}^{i+1}\dot{\omega}_{i+1} + {}^{i+1} \omega_{i+1} \times{}^{C_{i+1}} I_{i+1} \cdot {}^{i+1} \omega_{i+1}$ |

注意事项


- **角速度初始值**：  ${}^0 \omega_0 = (0,0,0)^T$
- **角加速度初始值**：  ${}^0 \dot{\omega}_0 = (0,0,0)^T$
- **加速度初始值（含重力）**：  ${}^0 v_0 = (0, g, 0)^T$

### 内推法

连杆力 ${}^i f_i = {}_{i+1}^i R {}^{i+1} f_{i+1} + {}^i F_i$

连杆力矩 ${}^i n_i = {}^i N_i + {}_{i+1}^i R {}^{i+1} n_{i+1} + {}^i P_{C_i} \times {}^i F_i + {}^i O_{i+1} \times {}_{i+1}^i R {}^{i+1} f_{i+1}$

关节力/力矩 

- 转动：$\tau_i = {}^i n_i^T \cdot{}^i \hat{Z}_i$
- 平动：$\tau_i= {}^i f_i^T \cdot {}^i \hat{Z}_i$


## 拉格朗日动力学方程

### 计算方法：

- 首先计算雅可比矩阵、旋转矩阵、惯性张量
- 计算$\boldsymbol{M}(\boldsymbol{\Phi})$, $\boldsymbol{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})$ 和 $\boldsymbol{G}(\boldsymbol{\Phi})$
- 带入公式，求解动力学方程

$$
\boldsymbol{M}(\boldsymbol{\Phi})\ddot{\boldsymbol{\Phi}}+\boldsymbol{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})\dot{\boldsymbol{\Phi}}+\boldsymbol{B}\dot{\boldsymbol{\Phi}}+\boldsymbol{G}(\boldsymbol{\Phi})=\boldsymbol{\tau}
$$

每一项的计算方法如下：

- $\boldsymbol{M}(\boldsymbol{\Phi})=\sum_{i=1}^{N}(m_{i}(\boldsymbol{J}_{P}^{(i)})^{\mathrm{T}}\boldsymbol{J}_{P}^{(i)}+(\boldsymbol{J}_{0}^{(i)})^{\mathrm{T}0}\boldsymbol{R}^{C_{i}}\boldsymbol{I}_{ii}^{0}\boldsymbol{R}^{\mathrm{T}}\boldsymbol{J}_{0}^{(i)})$
- $\boldsymbol{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})= \left.\left(\begin{array}{ccccccc}\sum_{k}c_{k11}\dot{\phi}_{k}&\sum_{k}c_{k21}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kj1}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kN1}\dot{\phi}_{k}\\\sum_{k}c_{k12}\dot{\phi}_{k}&\sum_{k}c_{k22}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kj2}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kN2}\dot{\phi}_{k}\\\vdots&\vdots&&\vdots&&\vdots\\\sum_{k}c_{k11}\dot{\phi}_{k}&\sum_{k}c_{k21}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kj1}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kNi}\dot{\phi}_{k}\\\vdots&\vdots&&\vdots&&\vdots\\\sum_{k}c_{k1N}\dot{\phi}_{k}&\sum_{k}c_{k2N}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kjN}\dot{\phi}_{k}&\cdots&\sum_{k}c_{kNN}\dot{\phi}_{k}\end{array}\right.\right)$
- $c_{jki}=\frac{1}{2}\left(\frac{\partial m_{ik}}{\partial\phi_{j}}+\frac{\partial m_{ij}}{\partial\phi_{k}}-\frac{\partial m_{kj}}{\partial\phi_{i}}\right)=c_{kji}$
- $G(\boldsymbol{\Phi})=\binom{g_1(\boldsymbol{\Phi})}{g_N(\boldsymbol{\Phi})}$, 其中$g_i(\boldsymbol{\Phi})=\frac{\partial u}{\partial\phi_i}=-\sum_{j=1}^Nm_j^0g^\mathrm{T} \frac{\partial^0\boldsymbol{P}_{C_j}}{\partial\phi_i}$
- $B=\mathrm{diag}(\begin{array}{ccc}b_1&\cdots&b_N\end{array})$,$b_i$ 为折算到关节 $i$的粘性摩擦参数(Viscous Friction Coefficient)

### 性质

$\dot{\boldsymbol{M}}(\boldsymbol{\Phi})-2\boldsymbol{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})$ 是反对称的