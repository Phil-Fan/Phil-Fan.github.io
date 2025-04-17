# 07 | 运动控制

- 被控变量：末端执行器位姿
- 控制输入：关节力/力矩
- 反馈：

通过传感器检测运动状态，末端和环境没有接触的情况下，**设计出关节执行器输入的闭环控制律**（也称闭环控制器），使得各关节较好地**跟踪期望轨迹**。

[机械臂操作控制基础(一) - 知乎](https://zhuanlan.zhihu.com/p/264809240)
[机械臂操作控制基础(二) - 知乎](https://zhuanlan.zhihu.com/p/264811391)
先进控制方法（没用） [机械臂先进控制方法综述 - 知乎](https://zhuanlan.zhihu.com/p/1892973878374033325)

[零基础机械臂操作控制(一) - 知乎](https://zhuanlan.zhihu.com/p/28035516596)
[零基础机械臂操作控制(二) - 知乎](https://zhuanlan.zhihu.com/p/28284740164)

[(9 封私信 / 80 条消息) 机械臂的动力学模型是如何解耦和线性化的？常用的线性化解耦方法有哪些？ - 知乎](https://www.zhihu.com/question/52607272)
[现代控制理论和机械臂控制（二） - 知乎](https://zhuanlan.zhihu.com/p/474813957)

[机器人-课时2-3-控制-PD控制器 - 知乎](https://zhuanlan.zhihu.com/p/297464197)
[机器人学-4-1-控制方法 - 知乎](https://zhuanlan.zhihu.com/p/335306452)
[机器人-课时2-附件2 - 知乎](https://zhuanlan.zhihu.com/p/297504556)
两种设计思路

- 将带执行器的机器人作为多输入多输出的受控对象，设计出利用全部关节期望轨迹及反馈信息计算全部关节执行器输入的控制器，即**集中控制**；
- 另一种是分别将每个关节作为单输入单输出的受控对象，设计出利用本关节期望轨迹及反馈信息计算本关节执行器输入的单变量控制器，即**独立关节控制**。


!!! todo "todo"
    - [ ] 独立关节控制
    - [ ] 关节建模方法与记忆
    - [ ] 转矩前馈控制
    - [x] 重力补偿PD控制
    - [ ] 逆运动学控制
    - [x] 鲁棒控制
    - [ ] 自适应控制
    - [ ] 各个方法优缺点，应用范围
    - [ ] 
[现代机器人学：力学，规划，控制（chapter11Ⅰ）自动控制原理回顾 - 知乎](https://zhuanlan.zhihu.com/p/377810484)

[现代机器人学：力学，规划，控制（chapter11 Ⅱ）机器人控制之运动控制 - 知乎](https://zhuanlan.zhihu.com/p/378218165)


[【现代机器人学】学习笔记十：机器人控制\_机器人控制算法csdn-CSDN博客](https://blog.csdn.net/zkk9527/article/details/128709448)
## 前置知识

1. 方块图的化简、梅森增益公式、信号流图
2. 二阶系统的时域响应的参数
3. 准确性：
   - 劳斯判据
   - 稳态误差计算；终值定理
4. PID系统的设计；调参方法
5. Lyapunov稳定性定理
6. 奇异值分解


## 传感器：旋转编码器——测关节转角转速

原理：**光栅圆盘**——在不透光的圆盘上等宽等间隔的透光狭缝，把转角/转速转换成光传感器接收到的脉冲的数量


方法

- **高速**：频率法（M法）——计算单位时间内的脉冲数。
- **低速**：周期法（T法）——计算相邻脉冲间的时间间隔。
- **综合**：M/T法——结合频率法和周期法，适用于全速段，分辨率高，广泛应用。


## 独立关节控制

!!! note "这里有很多字母，联系英文进行记忆"

### 电机建模



| 符号       | 描述                                   | 英文翻译                          |
|------------|----------------------------------------|-----------------------------------|
| $T_{ei}$   | 电机转矩                               | Motor torque                     |
| $C_{Ti}$   | 转矩系数                               | Torque coefficient               |
| $I_{mi}$   | 电机的电流                             | Motor current                    |
| $E_{mi}$   | 电机的电动势                           | Motor voltage                    |
| $\omega_{mi}$ | 电机的转速                           | Motor speed                      |
| $k_{ei}$   | 电机的反电动势常数                     | Back EMF constant                |
| $R_{mi}$   | 电机的电阻                             | Motor resistance                 |
| $U_{mi}$   | 电机的电压                             | Motor voltage                    |
| $k_{ui}$   | 关节 $i$ 电机驱动器的增益；节省能量，用小功率的器件控制大功率的电机 | Joint $i$ motor driver gain      |

带驱动器的直流有刷电机模型：转矩&转速

$$
T_{ei} = C_{ti} \cdot I_{mi}
$$

$$
\omega_{mi} = (\frac{k_{ui}}{k_{ei}})U_{ci} - (\frac{R_{mi}}{k_{ei}})I_{mi}
$$

### 关节建模与传递函数
$\theta_{mi}$ 电机转角
$\theta_{i}$ 关节i转角
$T_{ei}$    电机的输出力矩
$T_{ai}$ 输入齿轮对关节的作用力矩
$T_{li}$  反作用力的力矩，后续方程可以约掉
$T_{ci}$ 干扰力矩
$b_{mi},b_{ai}$ 轴承的粘性摩擦系数
$J$ 转动惯量


减速器：其实是扭矩放大器，代价是转速的下降 

编码器：对转速进行观测

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250401120430.png)

电机动力学：$J_{mi}\dot{\omega}_{mi}=T_{ei}-T_{li}-b_{mi}\omega_{mi}$
关节侧动力学： $J_{ai}\dot{\omega}_{i}=T_{ai}-T_{ci}-b_{ai}\omega_{i}$
转速关系：$\omega_i = \frac{\omega_{mi}}{\eta_i}$，转速下降，扭矩上升

使用$\eta * eq1 + eq2$可以得到关节模型

$J_{ci}\ddot{\theta}_{i}+B_{ci}\dot{\theta}_{i}=J_{ci}\dot{\omega}_{i}+B_{ci}\omega_{i}=K_{ci}U_{ci}-T_{ci}$

- 输入量：$U_{ci}$
- 干扰输入$T_{ci}$
- 输出 $\theta_i$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250401121056.png)

Laplace变换

$$
J_{ci}s^2\theta_i(s)+B_{ci}s\theta_i(s)=K_{ci}U_{ci}(s)-T_{ci}(s)
$$

得到系统的传递函数

$$
\theta_i(s)=\frac{K_{ci}}{s(J_{ci}s+B_{ci})}U_{ci}(s)-\frac{1}{s(J_{ci}s+B_{ci})}T_{ci}(s)
$$

### PD控制器


反馈信号是：被控对象的输出$\theta_i$ 和其微分

控制算法：

$$
\begin{align*}
U_{ci}(s) = k_{P_i}\widetilde{\theta}_i(s) - k_{D_i}\omega_i(s)\\
\widetilde{\theta}_i(s) = \theta_{di}(s) - \theta_i(s)    
\end{align*}
$$


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202504011210339.png)

$$
\theta_{i}(s)=\frac{k_{Pi}K_{ci}}{J_{ci}s^{2}+(B_{ci}+k_{Di}K_{ci})s+k_{Pi}K_{ci}}\theta_{di}(s)-\frac{1}{J_{ci}s^{2}+(B_{ci}+k_{Di}K_{ci})s+k_{Pi}K_{ci}}T_{ci}(s)
$$

#### 稳定性分析
!!! note "这里需要用到二阶动态性能的一些公式以及稳定性分析中的劳斯判据知识"

误差传递函数

$$
\tilde{\theta}_i\left(s\right)= \theta_{di}\left(s\right) - \theta_i\left(s\right)
$$

无扰动的情况下无静差

这里化简的时候使用梅森增益公式求解比较简单

### PID控制器 ｜ 消除静差

带一个积分环节

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202504011209180.png)


### 前馈PID ｜ 消除参考输入影响


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202504011208914.png)


### 转矩前馈控制

对关节干扰进行推算，增加补偿量主动消减干扰的影响


### $\alpha$-$\beta$ 方法


这一块可以看[机器人学-4-3-线性控制 - 知乎](https://zhuanlan.zhihu.com/p/340272432)这个博主的笔记，讲的很好


!!! note "什么是伺服"
    （1）伺服系统：是使物体的位置、方位、状态等输出，能够跟随输入量（或给定值）的任意变化而变化的自动控制系统。

    （2）在自动控制系统中，能够以一定的准确度响应控制信号的系统称为随动系统，亦称伺服系统。

    伺服的主要任务是按控制命令的要求，对功率进行放大、变换与调控等处理，使驱动装置输出的力矩、速度和位置控制得非常灵活方便。



## 集中控制

!!! note "可以看出教材是一步步逐渐递进的，各个方法需要准确获取的参数越来越少，鲁棒性越来越强"

$$
\eta_iT_{ei}=\eta_iC_{Ti}V_{ci}-\eta_i^2\frac{C_{Ti}k_{ei}}{k_{ui}\pi_{pi}+R_{mi}}\dot{\theta}_i
$$

$\eta_i T_{e i}$ 是第 $i$ 个关节电机（含减速器）对机器人的驱动转矩。记

$\tau = \begin{pmatrix} \eta_1 T_{e 1} \\ \vdots \\ \eta_N T_{e N} \end{pmatrix}, \tau_d = \begin{pmatrix} \eta_1 C_{T 1} V_{c 1} \\ \vdots \\ \eta_N C_{T N} V_{c N} \end{pmatrix}, B_e = \begin{pmatrix} \eta_1^2 \frac{C_{T 1} k_{e 1}}{k_{u 1} \pi_{p 1} + R_{m 1}} & \cdots & \eta_N^2 \frac{C_{T N} k_{e N}}{k_{u N} \pi_{p N} + R_{m N}} \end{pmatrix}, \dot{\Phi} = \begin{pmatrix} \dot{\theta}_1 \\ \vdots \\ \dot{\theta}_N \end{pmatrix}$

则对于全部关节电机，有

$\tau = \tau_d - B_e \dot{\Phi}$

与机器人动力学方程式合并，得到集中控制的被控对象模型

$$
M(\Phi) \ddot{\Phi} + C(\Phi, \dot{\Phi}) \dot{\Phi} + L \dot{\Phi} + G(\Phi) = \tau_d
$$

式中，$L = B + B_e$为正定对角矩阵。


**集中控制的任务在于设计计算 $\tau_d$ （相当于计算各关节电机期望电流）的算法，使得 $\Phi$ 跟踪 $\Phi_d$。**
### 重力补偿PD控制

重力力矩在控制中往往被视为一种非线性扰动，但是重力矩的数学模型可获取，因此，可作为一种已知的非线性扰动。直接补偿掉，在推导控制算法时就不需要考虑重力项了。

在实验中，重力补偿的明显作用有两点：1.在位置控制时，能够增加机器人的动态性能，动态跟踪误差相比无重力补偿时更小。在无积分的位置控制器中，如PD控制器，重力补偿能够减少稳态误差。


**控制律为**

$$
\boldsymbol{\tau}_d=\boldsymbol{\Lambda}_P(\boldsymbol{\Phi}_d-\boldsymbol{\Phi})-\boldsymbol{\Lambda}_D\dot{\boldsymbol{\Phi}}+\boldsymbol{G}(\boldsymbol{\Phi})
$$


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250401112408.png)

!!! note "Lyapunov 方法证明收敛"

    $$
    M\ddot{\Phi}=\Lambda_P\widetilde{\Phi}-(C+L+\Lambda_D)\dot{\Phi}
    $$

    取$(\widetilde{\Phi}^T,\dot{\Phi}^T)^T$为该闭环系统的状态，则其状态方程为

    $$
    \begin{pmatrix}\dot{\Phi}\\\ddot{\Phi}\end{pmatrix}=\begin{pmatrix}0&-I\\M^{-1}\Lambda_P&-M^{-1}(C+L+\Lambda_D)\end{pmatrix}\begin{pmatrix}\widetilde{\Phi}\\\dot{\Phi}\end{pmatrix}
    $$

    表明这是一个自治系统且原点是系统的平衡状态。构造正定李亚普诺夫函数

    $$
    V_L(\widetilde{\Phi},\dot{\Phi})=\frac{1}{2}\dot{\Phi}^TM\dot{\Phi}+\frac{1}{2}\widetilde{\Phi}^T\Lambda_P\widetilde{\Phi}
    $$

    那么

    $$
    \begin{align*}
    \dot{V}_L(\widetilde{\Phi},\dot{\Phi})&=\dot{\Phi}^TM\ddot{\Phi}+\frac{1}{2}\dot{\Phi}^TM\dot{\Phi}+\dot{\widetilde{\Phi}}^T\Lambda_P\widetilde{\Phi}\\
    &=\dot{\Phi}^T(\Lambda_P\widetilde{\Phi}-(C+L+\Lambda_D)\dot{\Phi})+\frac{1}{2}\dot{\Phi}^TM\dot{\Phi}-\dot{\Phi}^T\Lambda_P\widetilde{\Phi}\\
    &=\frac{1}{2}\dot{\Phi}^T(M-2C)\dot{\Phi}-\dot{\Phi}^T(L+\Lambda_D)\dot{\Phi}
    \end{align*}
    $$

    注意到$\dot{M}-2C$的反对称性使得$\dot{\Phi}^T(\dot{M}-2C)\dot{\Phi}=0$，于是

    $$
    \dot{V}_L(\widetilde{\Phi},\dot{\Phi})=-\dot{\Phi}^T(L+\Lambda_D)\dot{\Phi}
    $$

    这意味着$\dot{V}_L(\widetilde{\Phi},\dot{\Phi})$半负定（$\dot{V}_L(\widetilde{\Phi},\dot{\Phi})=0$时，$\widetilde{\Phi}$可以非零）。接下来，需要证明$\dot{V}_L(\widetilde{\Phi},\dot{\Phi})$

    !!! info "自治系统与非自治系统"
        >  来源：[什么是自治系统、非自治系统、时不变系统、时变系统？ - 知乎](https://zhuanlan.zhihu.com/p/441100050)
        
        考虑如下系统：

        $$
        \dot{x} = f(t, x)
        $$

        其中 $x = [x_1, x_2, \ldots, x_n]^T \in \mathbb{R}^n$ 是系统状态，$t > 0$ 是时间。

        $f(t, x)$ 中显含时间 $t$ 的系统就是**非自治系统**（nonautonomous system），也称**时变系统**（time varying system）。

        如果不显含时间 $t$，即

        $$
        \dot{x} = f(x)
        $$

        称为**自治系统**（autonomous system），也称为**时不变系统**（time invariant system）。

        注1：决定自治和非自治的是是否“显含时间 $t$”。注意这里的描述是“显含”而不是“不含”。事实上，$x$ 本身就是时间的函数，即 $x = x(t)$，也就是说系统 (1) 的完整描述是 $\dot{x}(t) = f(t, x(t))$，系统 (2) 的完整描述是 $\dot{x}(t) = f(x(t))$。$x(\cdot)$ 中包含的时间 $t$ 对于系统来说不是显含的，而是隐含的，所以 $x(\cdot)$ 中所包含的时间 $t$ 与判断系统是否自治无关。

        注2：如果 $f$ 是线性的，那么系统 (1) 就是**线性非自治系统**（线性时变系统），系统 (2) 就是**线性自治系统**（线性时不变系统）。


    !!! note "反对称矩阵二次型为0"
        **标量的转置是本身**

        如果 $A$ 是反对称矩阵，即 $A^T = -A$，则对于任意向量 $x$，有 $x^T A x = 0$。这显然成立，因为：

        $$
        x^T A x = x^T (-A^T) x = -x^T A^T x = -(x^T A x)^T = -x^T A x
        $$

        所以 $2x^T A x = 0$，即 $x^T A x = 0$。

    不恒为零：从任意非零初态（$\widetilde{\Phi}^{T}(0)$ $\dot{\Phi}^{T}(0)$）$^{T}$ 出发的解（$\widetilde{\Phi}^{T}(t)$ $\dot{\Phi}^{T}(t)$）$^{T}$ 不会有 $\dot{V}_{L}(\widetilde{\Phi}(t), \dot{\Phi}(t)) \equiv 0$。
    
    采用反证法，假设从某非零初态（$\widetilde{\Phi}^{T}(0)$ $\dot{\Phi}^{T}(0)$）$^{T}$ 出发的解（$\widetilde{\Phi}^{T}(t)$ $\dot{\Phi}^{T}(t)$）$^{T}$ 有 $\dot{V}_{L}(\widetilde{\Phi}(t), \dot{\Phi}(t)) \equiv 0$，即 $-\dot{\Phi}^{T}(t)(L + \Lambda_{D})\dot{\Phi}(t) \equiv 0$。显然 $\dot{\Phi}(t) \equiv 0$，其导函数 $\ddot{\Phi}(t) \equiv 0$，进而由式（8-83）知 $\ddot{\Phi}(t) \equiv 0$。于是（$\widetilde{\Phi}^{T}(t)$ $\dot{\Phi}^{T}(t)$）$^{T} \equiv 0$，则初态（$\widetilde{\Phi}^{T}(0)$ $\dot{\Phi}^{T}(0)$）$^{T} = 0$，这与非零初态假设矛盾，“不恒为零”得证。最后，当 $\|[\widetilde{\Phi}^{T} \quad \dot{\Phi}^{T}]^{T}\| \rightarrow \infty$ 时，有 $V_{L}(\widetilde{\Phi}, \dot{\Phi}) \rightarrow \infty$。
    
    综上，系统式的原点平衡状态是大范围渐近稳定的。因此，对任意初态（$\widetilde{\Phi}^{T}(0)$ $\dot{\Phi}^{T}(0)$）$^{T}$，有

    $$
    \lim_{{t \to +\infty}} (\widetilde{\Phi}^{T}(t) \quad \dot{\Phi}^{T}(t))^{T} = 0
    $$

    重力补偿PD控制可以使$\Phi$收敛于定常的$\Phi_d$，适用于一种静止位形运动到另一种静止位形

### 逆运动学控制

在反馈中利用补偿将复杂非线性模型 化成N个无耦合的单变量的线性模型

采用补偿：

$$
\boldsymbol{\tau}_d=\boldsymbol{M}(\boldsymbol{\Phi})\boldsymbol{\alpha}_\phi+\boldsymbol{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})\dot{\boldsymbol{\Phi}}+\boldsymbol{L}\dot{\boldsymbol{\Phi}}+\boldsymbol{G}(\boldsymbol{\Phi})
$$

得到：

$$
\ddot{\Phi} = \alpha_\Phi
$$


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250401092616.png)

所以控制律为

$$
\alpha_{\phi}=\ddot{\boldsymbol{\Phi}}_{d}+K_{D}\dot{\widetilde{\boldsymbol{\Phi}}}+K_{P}\widetilde{\boldsymbol{\Phi}}
$$

其中，$\ddot{\boldsymbol{\Phi}}_{d}+K_{D}\dot{\widetilde{\boldsymbol{\Phi}}}$ 是前馈的部分,即框图左上角的部分

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202504010926579.png)

## 非线性控制

### feedback linearization


### 鲁棒控制 ｜ 估计参数

$M(\boldsymbol{\Phi})\ddot{\boldsymbol{\Phi}}+C(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})\dot{\boldsymbol{\Phi}}+L\dot{\boldsymbol{\Phi}}+G(\boldsymbol{\Phi})=\boldsymbol{\tau}_d$ 的参数值无法准确获取，使用估计值进行控制


控制律

$$
\boldsymbol{\alpha}_{\phi}=\ddot{\boldsymbol{\Phi}}_{d}+\boldsymbol{K}_{D}\dot{\widetilde{\boldsymbol{\Phi}}}+\boldsymbol{K}_{P}\widetilde{\boldsymbol{\Phi}}+\boldsymbol{\Xi}
$$

其中，$\boldsymbol{\Xi}$是不确定性项

$$
\boldsymbol{\Xi}=\boldsymbol{B}_r(\boldsymbol{\varphi})=\begin{cases}(\rho_1+\rho_2\|\boldsymbol{\varphi}\|)\frac{\overline{B}^\mathrm{T}\boldsymbol{P}_L\boldsymbol{\varphi}}{\|\overline{B}^\mathrm{T}\boldsymbol{P}_L\boldsymbol{\varphi}\|},&\text{当}\|\overline{\boldsymbol{B}}^\mathrm{T}\boldsymbol{P}_L\boldsymbol{\varphi}\|\neq0\text{时}\\\\0,&\text{当}\|\overline{\boldsymbol{B}}^\mathrm{T}\boldsymbol{P}_L\boldsymbol{\varphi}\|=0\text{时}&\end{cases}
$$

一些参数的定义如下

$$
\begin{align*}
&\rho_{1}>\frac{1}{1-\gamma_{3}}(\gamma_{3}\gamma_{2}+\overline{m}\gamma_{1})\\
&\rho_{2}>\frac{\gamma_{3}\left\|(K_{P}\quad K_{D})\right\|}{1-\gamma_{3}}\\
\text{正数}\quad&\gamma_1>\|\widetilde{\boldsymbol{\Gamma}}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})\| = \|\tilde{C}(\boldsymbol{\Phi},\dot{\boldsymbol{\Phi}})\dot{\boldsymbol{\Phi}}+\widetilde{\boldsymbol{L}}\dot{\boldsymbol{\Phi}}+\widetilde{\boldsymbol{G}}(\boldsymbol{\Phi})\|\\
\text{正数}\quad &\gamma_2>\|\ddot{\boldsymbol{\Phi}}_d\|\\
\text{非负数}\quad1>&\gamma_3\ge\|\boldsymbol I-\boldsymbol M^{-1}(\boldsymbol{\Phi})\hat{M}(\boldsymbol{\Phi})\|
\end{align*}
$$

- 矩阵范数采用矩阵最大的奇异值
- $K_P$,$K_D$采用逆运动学控制设计，保证大范围渐进稳定
- 正数$\overline{m}$ 大于$M^{-1}(\boldsymbol{\Phi})$的最大奇异值和正数 $\underline{m}$ 小于$M^{-1}(\boldsymbol{\Phi})$的最小奇异值，再取$\hat{M}(\boldsymbol{\Phi})=\frac2{\underline{m}+\overline{m}}\boldsymbol{I}$，可以保证$\left\|\boldsymbol{I}-\boldsymbol{M}^{-1}(\boldsymbol{\Phi})\hat{\boldsymbol{M}}(\boldsymbol{\Phi})\right\|\leqslant\frac{\overline{m}-\underline{m}}{\underline{m}+\overline{m}}=\gamma_{3}<1$


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250401101152.png)


又根据Lyapunov稳定性定理，可以证明，保证在不确定性$\Delta$ 下 $\boldsymbol{\Phi}$对 $\boldsymbol{\Phi}_d$的渐近跟踪。

### 自适应控制 ｜ 动态估计参数

在鲁棒控制中，参数的估计是不变的。

自适应控制的思想就是使用在控制过程中观测到的数据，动态更新估计不确定性参数的值。

