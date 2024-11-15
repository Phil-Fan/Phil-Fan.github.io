---
comments: true
---

# 智能控制技术


!!! note "控制学科三大任务：建模、控制、优化"


!!! note "课程介绍"

    === "简介"

        - 一般不依据数学模型 进行处理。
        - 根据积累的经验和知识进行在线推理，确定控制策略。
        - 在 **精度和不确定性** 之间 折中

    === "知识框架"

        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241107134330.png)
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241107135609.png)

|               | 第一阶段         | 第二阶段         | 第三阶段         |
|---------------|------------------|------------------|------------------|
| 形成时间      | 40—50年代       | 60—70年代       | 80年代以来       |
| 理论基础      | 经典控制理论    | 现代控制理论    | 智能控制理论    |
| 研究对象      | 单入单出系统    | 多入多出系统    | 多级多变量系统   |
| 分析方法      | 传递函数频域法  | 状态方程时域法  | 多学科交叉      |
| 研究重点      | 反馈控制        | 最优、随机、自适应控制 | 不确定、大系统智能控制 |
| 控制装置      | 自动调节器      | 数字计算机       | 智能机器        |
| 应用          | 单机自动化      | 机组自动化       | 综合自动化       |


- 规则驱动： 专家系统
- 数据驱动： 神经网络








## 递阶控制 | Hierarchical Control

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115112217.png)

<iframe src="https://wuhua.cug.edu.cn/__local/B/A1/9D/1850F4F1F9922A6F917E10E40B6_BDCC55BC_10D898.pdf" width="100%" height="600px" style="border: none;">
This browser does not support PDFs
</iframe>



分级递阶的控制结构成为智能控制的一种典型结构。

三级递阶智能控制系统由**组织级、协调级和执行级**组成。

在实际应用中，往往采用不同的基于知识的表示和搜索推理技术的组合，这些技术包括状态空间、与或图、谓词逻辑、语义网络、模糊集合、Petri网、规则、过程、黑板和神经网络等。

各级按**“精度递增伴随智能递减”**的原则进行设计。

递阶智能控制是基于**信息论**的智能控制系统。

### 原理与结构


**第一级： 组织级**

代表系统的主导思想，人工智能起控制作用。

组织级为决策控制级，其接受控制期望目标和协调级反馈信息，制定最优决策，对协调级下达决策指令。

推理，规划，决策，记忆，数据存取

**第二级： 协调级**


上（第一级）下（第三级）级间的接口，由人工智能和运筹学起控制作用。

其接受组织级的决策指令，协调和优化执行级各控制器的设定值，并向组织级传送执行结果信息；

**第三级： 执行级**

智能控制系统的最低层级，要求具有很高的精度，并由控制理论进行控制。


执行级为直接控制级，其各个控制器分别控制被控对象的一部分；





**多级多目标结构**

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115115601.png)

1. **系统组成**：系统由若干个可分的、相互关联的子系统组成。
2. **决策单元排列**：所有决策单元按一定支配关系递阶排列。
3. **上下级关系**：
   - 同一级各单元要受上一级的干预。
   - 同时又对下一级决策单元施加影响。
4. **信息交换**：
   - 同级之间不交换信息。
   - 上下级间交换信息。
5. **目标协调**：
   - 同一级决策单元如有相互冲突的决策目标，由上一级决策单元加以协调。
6. **总目标**：协调的总目标是使全局达到优化或近似优化。
7. **结构形式**：多级多目标决策单元在不同级间递阶排列，形成了金字塔式结构。




### 信息论
对系统的各级均采用熵（信息熵，Shannon熵）作为描述和度量系统控制作用的测度。

**熵（Entropy, H）**

在信息论中指的是信息源中所包含的平均信息量

$$ 
H = -k \sum_{i=1}^{n} P_i \ln P_i 
$$

其中，$P_i$为信息源中各事件发生的概率。

**机器知识K可表示**为

$$ 
K = -\alpha - \ln p(K) 
$$

**知识流量R**是智能机器的主要变量，在一有限时间间隔T上为

$$ 
R = K/T 
$$

机器智能MI、事件数据库DB与知识流量R之间满足关系

$$ 
(MI):(DB) \rightarrow (R) 
$$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115112758.png)
- 若知识流量不变，增大数据库DB的熵将减少机器智能MI的熵。
- 知识流R在信息理论意义上代表系统的工作能力。
- 建立和执行任务期间，知识流量一般不变。


**IPDI原理：**

精度递增伴随智能递减 (Increasing precision with decreasing intelligence)

原理适用于递阶系统的单个层级和多个层级。




### 分层递阶

!!! note "递阶智能控制的实质"
    在结构上遵循精度随智能降低而提高（ IPDI ）的原理，寻求系统的正确决策与控制序列，能够使系统的总熵为最小。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113315.png)


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113452.png)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113459.png)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113510.png)

!!! example "智能机器人控制系统"

    **学习级（组织级）**
    基于专家系统、识别、规划

    **技能级（协调级）**
    神经模糊网络、为学习级形成的控制策略生成合适的控制参考信号。

    **适应级（执行级）**
    神经网络、作为机器人的控制器以适应
    技能级生成的控制参考信号。

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113721.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115113755.png)

    协调级：Petri网翻译器；语言决策树
    组织级：Boltzmann机；语言决策树；自动机


### 集散控制系统

集散控制系统的特点：
- 分级递阶控制
- 分散控制
- 自治性与协调性
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115114228.png)


### HW01-递阶控制
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115114628.png)

如图所示的多机器人协作系统由三个机器人组成，分别为两个悬挂移动式多关节机器人（SMR1和SMR2）和一个地面移动式多关节机器人（GMR）。

SMR1和SMR2的主体是两个七关节式机器人，悬挂在一个固定在顶部的方形托架上，它们的移动支架都能够沿着悬挂导轨在方形托架的允许范围内移动。GMR的主体是六关节式机器人HP3，安装在一个轮式移动基座PowerBot上，能够在地面上随意移动。

系统配置三级视觉系统，第一级为全局的外部三维点云相机，第二级为装在机械臂腕部的深度相机，第三级为装在机械臂手抓中心的摄像头。各机械臂均配备力矩传感器。

SMR1、SMR2和GMR都有自己独立的控制计算机，系统中另有一台独立的计算机TAC，各计算机之间通过无线通讯连接，实现数据交互。

系统的目标任务是：从无序堆放的工件中拾取目标螺杆，并将螺杆的两端装上合适的螺帽，然后放置在期望目标位置。

请根据以上各部分的具体任务和功能，采用递阶控制的思想将多机器人协作系统进行分解，并画出该递阶控制系统的分级系统结构图。



## 专家控制 | Expert Control

### 概念
应用专家系统概念和技术，模拟人类专家的控制知识与经验而建造的控制系统，称为专家控制系统。

专家系统的基本功能取决于它所含有的知识，因此，专家系统称为基于知识的系统（ knowledge based system ）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115215810.png)
### 结构、类型与设计

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241107135241.png)



1. **知识库**：
   - 存储专家系统的专门知识，包括事实、可行操作和规则等。

2. **推理机**：
   - **解释程序**：能够根据知识进行推理和导出结论，而不是简单地搜索现成的答案。
   - **调度程序**：用于记忆所采用的规则和控制策略的程序，使整个专家系统能够以逻辑方式协调地工作。

3. **综合数据库**：
   - 又称全局数据库或总数据库，用于存储领域或问题的初始数据和推理过程中得到的中间数据（信息），即被处理对象的一些当前事实。

4. **解释接口**：
   - 能够使系统与用户进行对话的接口，使用户能够输入数据和提出问题并获得答案，了解推理过程。

专家系统将知识组织成三级：数据、知识库、控制



### 专家PID控制

### 应用


### HW02-专家控制
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241115215028.png)

如图所示为车载倒立摆系统，一辆小车在水平轨道上移动，小车上有一个可绕固定点转动的倒立摆。控制小车在水平方向的移动可使摆杆维持直立不倒，这和手掌移动可使直立木棒不倒的现象类似。

忽略车轮与地面的摩擦力等阻力，可推导出车载倒立摆的动力学方程如下：

$$
\begin{cases}
(M + m) \ddot{x} + m l (\ddot{\theta} \cos \theta + ml \dot{\theta}^2 \sin \theta) = F \\
ml^2 \ddot{\theta} + ml \ddot{x} \cos \theta - mgl \sin \theta = 0
\end{cases}
$$

其中的参数如表所示：

| 参数 | 大小 |
| --- | --- |
| 摆杆质量 $m$ | 0.5kg |
| 小车质量 $M$ | 1kg |
| 摆杆转动轴心到摆杆质心的长度 $l$ | 0.5m |
| 摆杆与垂直向上方向的夹角 $\theta$ | $[0, \pi]$ rad |
| 重力加速度 $g$ | 9.8m/s² |
| 施加在小车上的水平外力 $F$ | $[-F_m, F_m]$ N |
| 小车在水平方向的位移 $x$ | 不限制 |

增量型离散PID控制算法如下：

$$
F(k) = F(k-1) + K \left[ K_p \Delta \theta (k) + \frac{T}{T_i} \theta (k) + \frac{T}{T_d} (\Delta \theta (k) - \Delta \theta (k-1)) \right]
$$

其中 $T$ 为采样时间，$\Delta \theta (k) = \theta (k) - \theta (k-1)$

若 $F_m = 25$，取 $T = 0.0001s$，$K_p = 20$，$K_i = 3$，$K_d = 1$，设计 $0 < \theta_1 < \theta_2 < \theta_m$，$0 < K_s < 1 < K_b$


在离散PID控制基础上，采用专家PID控制方案，规则如下：

1. 若 $|\theta (k)| \geq \theta_m$ 时，则 $F(k) = \text{sgn}(\theta) F_m$
2. 若 $\theta_2 \leq |\theta (k)| < \theta_m$ 时，
    1. 若 $\theta (k) \Delta \theta (k) > 0$ 时，则 $K = K_b$
    2. 若 $\theta (k) \Delta \theta (k) < 0$ 时，
        a. 若 $\Delta \theta (k) \Delta \theta (k-1) > 0$ 时，则 $K = 1$
        b. 若 $\Delta \theta (k) \Delta \theta (k-1) < 0$ 时，则 $K = K_b$
3. 若 $\theta_1 \leq |\theta (k)| < \theta_2$ 时，
    1. 若 $\theta (k) \Delta \theta (k) > 0$ 时，则 $K = 1$
    2. 若 $\theta (k) \Delta \theta (k) < 0$ 时，
        a. 若 $\Delta \theta (k) \Delta \theta (k-1) > 0$ 时，则 $K = K_s$
        b. 若 $\Delta \theta (k) \Delta \theta (k-1) < 0$ 时，则 $K = 1$
4. 若 $|\theta (k)| < \theta_1$ 时，则 $K = 1$



若小车和摆杆静止，摆杆与垂直向上方向的初始夹角 $\theta(0) = \frac{\pi}{4} \text{ rad}$，请：

1. 给出上述专家PID控制方案的合适参数 $\theta_1, \theta_2, \theta_m$ 和 $K_s, K_b$，通过调节 $F$ 使倒立摆的摆杆夹角 $\theta$ 恢复并维持在期望值（$\theta_d = 0$），在 matlab 中进行仿真，给出位移 $x$、夹角 $\theta$ 和水平力 $F$ 的变化曲线，并比较专家PID控制与常规PID控制的结果（可尝试参数 $\theta_1 = 0.5, \theta_2 = 0.3, \theta_m = 0.1$ 和 $K_s = 0.85, K_b = 1.4$）。

2. 针对不同的初始夹角 $\theta(0)$，给出专家PID控制的结果。（可能需要调整相关参数 $\theta_1, \theta_2, \theta_m$ 和 $K_s, K_b$）

## 模糊控制 | Fuzzy Control

### 数学基础

### 原理与结构
在被控制对象的模糊模型的基础上 运用模糊控制器近似推理手段实现系统控制 。

模糊模型是用模糊语言和规则描述的一个系统的动态特性及性能指标 。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241107135344.png)

### 设计方法


### 模糊专家系统

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241107135524.png)


## 神经网络控制 | Neural Network Control
### 控制方案

### 控制设计

