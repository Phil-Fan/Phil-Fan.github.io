# 机器人导论

!!! note "课程简介"
    - 资源
       [2023春《机器人导论》笔记分享](https://www.cc98.org/topic/5601621)<br>
       [2020-2021春学期《机器人导论》整理复习笔记分享](https://www.cc98.org/topic/5070984)<br>
       [设计框图](https://www.cc98.org/topic/5306160)
    - 回忆卷
       [2022-2023春机器人导论回忆卷](https://www.cc98.org/topic/5597275)<br>
       [2021-2022 春 机器人导论 回忆卷](https://www.cc98.org/topic/5306507)<br>
       [2019-2020春夏机器人导论回忆卷](https://www.cc98.org/topic/4961482)<br>
       [2019-2020春夏部分考试回忆（机器人导论](https://www.cc98.org/topic/4960976/1#1)<br>
       [2020-2021春学期机器人导论回忆卷](https://www.cc98.org/topic/5070617)<br>



1、冯诺依曼结构的硬件结构
 2、巡线小车的框图和程序设计（据我观察已经考了三四年了这题……不做评价）
 3、传感器的定义，根据智能家居机器人写四种传感器or分析超声波/激光传感器的原理及其各自的优缺点
 4、五种旋转变直线的机构
 5、写出3绕组2极无刷直流电机（就课上讲的模型）的联结方式和导通状态图

![image-20240416103542259](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416103542259.png)





## 微控制器

总线 bus

GPIO ： general purpose io

二进制减法： 用[补码](https://zhuanlan.zhihu.com/p/99082236)

二进制乘法： 移位相加 倍增

![image-20240416101254260](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416101254260.png)

![image-20240416101303336](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416101303336.png)

![e90541dc83a0c99e8be34aef](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/e90541dc83a0c99e8be34aef.png)

 控制器：每一个箭头 决定开关是否打开

 ALU ： 逻辑计算

![0dd3435c8313464ffc25e96f](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/0dd3435c8313464ffc25e96f.png)
 嵌入式系统： 和硬件完全对应

![image-20230907135656516](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135656516.png)
 根据PID系统 

![image-20230907140310732](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140310732.png)

![image-20230907135740437](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135740437.png)

![image-20230907135728112](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135728112.png)



## 传感器

### 定义

![image-20240416115839492](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416115839492.png)

### 静态特性

- 灵敏度
- 信噪比（S/N）：传感器输出信号中信号分量与噪声分量的平方平均值之比
- 线性：输入输出为线性

精度

- 稳定性：输入量恒定，输出量向一个方向偏移（温漂、零漂）
- 准确度：测量值对真值的偏移程度
- 精密度：测量相同对象，每次得到不同值

### 动态特性

![image-20240416111624968](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111624968.png)

### 选择

**尺寸、重量、价格、功耗敏感**

![image-20240416111656391](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111656391.png)

### 常见传感器

![image-20230907140033593](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140033593.png) 

#### 电位器

![image-20240416111731145](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111731145.png)

类别
旋转式:测量角位移

直线式:测量线位移

#### 编码器

根据测量介质分：光电码盘、磁编码器

根据测量结果分

- 增量式
- 绝对式

![image-20240416112056238](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112056238.png)

绝对式光电码盘

上电时候可以检测到位置、

![image-20240416112342658](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112342658.png)



**检测正反转 - 使用两个错位的码道**

![image-20240416112311474](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112311474.png)

**检测速度**

![image-20240416112459436](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112459436.png)

![image-20240416112618436](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112618436.png)

计量周期法和计量频率法

![image-20230907140242381](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140242381.png)

#### 方向角传感器

指南针：霍尔效应

易受环境影响



**陀螺仪**：

机械（角动量大转轴不动）

光纤：光速不变、光干涉

MEMS（科里奥利力）：体积小、重量轻、成本低；航向角不准



#### 距离传感器

- 红外光接近觉传感器
- 回波式接近觉传感器



??? note "题目"
	分析超声波/激光传感器的原理及其各自的优缺点

**超声波**

**原理：**

![image-20240416113219037](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416113219037.png)

发出声波，检测发出与回波之间的时间差
$$
Length = \frac{v\times T_{total}}{2}
$$

**问题：**

- 声波速度慢，时间比较好测量，但是降低了感知速率
- 声波束按照锥形传播，分辨率较差，无法分辨尺寸偏大or偏小；无法分辨角度、方向
- 光滑反射、吸收

![image-20240416113455608](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416113455608.png)





**激光雷达**

光是不会像声波发散

精确检测方位角，检测物体宽度

 方法：三角法，时飞法，相位偏移测量法

![image-20240416115157833](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416115157833.png)

![image-20240416115210183](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416115210183.png)

#### 力觉传感器

压阻式、压电式、电容式



## 驱动

电机驱动：将电能转换为旋转或直线运动动能，最常见最普遍，控制简单稳定性好，输出精准，但是力矩小，需要配合减速器使用。

液压驱动：以液压油为传动介质，液压缸作为驱动器，单位重量传输功率大，可以产生很大输出力，响应迅速，但是系统复杂、成本高，体积重量大，输出精度较低。

气压驱动：以压缩空气作为动力源，动作迅速，反应快，结构简单，但是受负载影响大，不适宜精密位置和速度的控制，输出力小。
其他驱动：压电陶瓷驱动，形状记忆合金驱动（软体机器人）等

### 电机 motor 

 \- 速度高、力矩小
 减速器
 $P = \frac{v}{i} \times Ti$

#### 分类

- 电机驱动
- 气动
- 液压驱动

![image-20230907140256665](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140256665.png)

直流电机

输出力矩、速度

#### [有刷电机与无刷电机](https://www.bilibili.com/video/BV1ig411S7gX/?spm_id_from=333.337.search-card.all.click&vd_source=c22bb8d123dbc6430c3057dc8d2701b4)

舵机
控制角度

转动惯量的匹配

![image-20240416104119842](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104119842.png)

转动顺序、导通方式

![image-20240416104143466](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104143466.png)

换向的过程



#### 调速

滤波


 [H桥的基本原理-刹车-正反转-调速](https://www.bilibili.com/video/BV1ZG4y1v7LS/?spm_id_from=333.1007.top_right_bar_window_history.content.click) ![image-20230907140632003](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140632003.png)



#### 电机控制

> 一个电机由静止到额定转速是怎么实现的



> 如何控制小车右转
>
> 如何控制小车原地右转
>
> 如何控制小车以半径1m右转

力矩和转速

等效电路

![image-20240416104333256](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104333256.png)

### 舵机

> 控制角度

控制线：电源线、地线、控制线

![image-20230907143850328](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907143850328.png)

电机 + 减速器





直流电机PWM匹配

占空比

![image-20230907135711661](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135711661.png) ![image-20230907140616101](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140616101.png)![image-20230907140621883](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140621883.png)

### 气动

![image-20240416104446817](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104446817.png)

方向控制回路

**几位几通**

基本符号

![image-20240416104540736](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104540736.png)



## 传动

执行结构：完成操作任务

传动机构：伺服系统 如齿轮



### 参数

#### 自由度DOF：

​	手臂：7自由度

减速比（传动比：输入速度与输出速度之比

转动惯量尽可能小，防止谐振

刚度

阻尼





支撑、导向系统：轴承和导轨

### 齿轮传动

#### 定轴传动

![image-20240416104731762](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104731762.png)

#### 周转轮系

![image-20240416104742305](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104742305.png)

渐开线

![image-20230907144343497](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907144343497.png)

![image-20240416104846198](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104846198.png)



### 连杆传动

![image-20240416104926218](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104926218.png)

AB当做输入，CD当做输出，则BC就是一个连杆

#### 曲柄

双曲柄机构

#### 摇杆



推导过程与分类

![image-20240416105135035](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105135035.png)

![image-20240416105220455](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105220455.png)

![image-20240416105229282](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105229282.png)

矢量方程的思路

![image-20240416105246543](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105246543.png)

### 滑轮组

### 带传动

### 链传动

### 涡轮-蜗杆传动

### 凸轮机构

### 轴承

使轴系有确定的位置

## 机器人运动学

正运动学：已知角度求位姿

逆运动学：已知位姿求解角度

滚动 `roll`

俯仰 `pitch`

偏摆 `yaw`



公式



欧拉角

![image-20240416110144598](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416110144598.png)

## 地图与规划

1、导航地图：
栅格地图（稠密有结构、直接索引查询）
八叉树地图（稀疏有结构、直接索引查询）
点云地图（无顺序，因而无法查询）
ESDF图、沃罗若伊图、自由空间路线图

### 路径规划

精确最优

- 深度优先
- 广度优先

近似最优

- 启发式搜索 A* D*
- 模拟退火、进化、蚁群

### 避障规划

### 轨迹规划



## 集群导论 - 高飞

swarm

flocking

formation

chstering

>**群体行为**
>
>有限的局部信息群体中的每个个体只能获得有限的局部信息，对群体中其他个体共后参与构建的结构没有全局性的了解。
>简单的个体规则每个个体仅遵从一些简单的行为规则，这套规则允许群体协调其活动并建立一个全局结构或构型。
>全局结构涌现出有利的功能这些结构使群体能够解决一些个体无法完成的问题，并体现出灵活和鲁棒性。

群体智能的关键机制:通过局部的个体之间相互作用**涌现**出具有全局效果的结构;
指定系统个体之间交互的规则是在局部信息的基础上执行的而不参考全局模式，这是系统的一种涌现属性，而不是外部排序影响强加给系统的属性，

- 聚合(Aggregation)
- 图案形成(Pattern Formation)
- 自组装(Self-assembly)
- 群体搬运(Collective Transport)
- 群体探索(Collective Exploration)



### 基于 `Virtual Structures`的编队控制

核心思想： 集群表示为世界坐标系下的整体 `VRB | virtual rigid body`

- 规划质心的运动：中心点的运动轨迹

- 规划每个虚拟刚体顶点对于`vrb`坐标系的相对运动即可

![image-20240408083548437](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240408083548437.png)

**势场法：构建映射函数**

避障 - 做排斥

导航 - 做吸引

人工势场法（Artificial Potential Field，简称APF）是一种用于路径规划的算法。它的基本思想是在环境中创建一个虚拟的势场，其中目标点产生引力，吸引机器人向目标移动，而障碍物则产生斥力，使机器人远离障碍物。通过计算机器人在势场中的受力情况，可以规划出一条从起始点到目标点的无碰撞路径。

在APF算法中，势场通常由引力场和斥力场组成。引力场由目标点产生，其强度随着机器人与目标点的距离减小而增大，吸引机器人向目标点移动。斥力场由障碍物产生，其强度随着机器人与障碍物的距离减小而增大，使机器人远离障碍物。机器人在势场中的运动方向由引力和斥力的合力决定。



用3个向量的penalty函数人工势场

![image-20240408085149873](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240408085149873.png)

![image-20240408085201361](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240408085201361.png)

调参过程：对于A,B,C等参数进行调参

**缺陷：**

- 短视：只把位置期望映射成下一时刻的速度值（没有考虑未来的一段时间，只看眼前）容易陷入局部极小值（被卡住）
- 把势能映射成速度不合理



### `Velocity Obstacle`多智能体避障算法

分布式的控制率



假设一个虚拟的速度障碍，任何落在蓝色区域以内的速度矢量最后都会让两物体相撞



线性速度障碍之下的，

![image-20240408090619488](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240408090619488.png)

VO的震荡问题

只考虑其他机器人的当前速度，而不考虑其他机器人下一控制周期的速度。



改进 - RVO | reciprocal velocity obstacle

如果B不动的话，A需要承担所有的避障职责

如果B动的话，AB各承担50%的避障职责



### 生物群落模型 flocking



