# 规划
轨迹规划：考虑速度
运动规划：
路径规划(我如何去)


## 基于搜索的路径规划

### Dijkstra’s   

加了权重的广度优先算法


!!! note "将完备搜索具有一些方向性"
### A*

在Dijkstra's算法的基础上，加了对于距离目标点的预测方向，因而有了更强的目的性
[【算法】路径规划中的Dijkstra(狄克斯特拉)与A星算法_dijkstra和a星算法的差异-CSDN博客](https://blog.csdn.net/QLeelq/article/details/113862917)


### JPS

在图上搜素



三者都是最优解


## 基于采样的路径搜索

### PRM
Probabilistic Road Map 基于概率采样的路径

**构建阶段**
- 均匀生成采样点，删除碰撞点
- 连接近邻的节点，删除和环境碰撞的路径段

**搜索阶段**

在构建出的路标连接图中搜索一条起点到终点的路径（使用Dijkstra或者A*算法）

优点：产生的roadmap可以被复用

缺点：对于给定的起点和终点，非最短路径，效率低

![image-20240427143014709](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240427143014709.png)

[基于采样的运动规划算法-RRT(Rapidly-exploring Random Trees) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/133224593)

### RRT | rapidly-exploring random tree

- 在整个地图上随机采样
- 采样点选择最近点
- 走一个步长的距离，看有没有碰撞，加入树中
- 终止判断：是否在最近点的范围内；路径回溯得到最终路径

不需要对地图进行预处理，栅格地图或是

#### 技巧

采样的方法非常重要

!!! note "有一点贪心但不太贪心"

- kd-tree
- 双向RRT
#### 分析

过小缝问题：没有栅格地图，很难采样到合适的点；采样到合适点后连接也不一定合适

优点：容易添加对目标点的引导，效率增加

缺点：无法删除已生成树，但不一定是最短



### RRT*


采样变多对于结果的优化并不多
RRT没有遗忘机制，对已知路径没有更新，对错误连接没有修正


- 选择最近点，以新采样点为中心，定义一个Redius，找到在这个范围内的点
- choose parent：选择一个父节点，使得从起始点到采样点的距离最小
- rewire：即在采样之后与最短路径连接后，考虑在某一个定长的圆的范围内，其内的点是否可以连接到新采样的点（用到初始点的距离进行判断）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183058.png)

!!! note "核心：半径R的选择"


![image-20240427143031710](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240427143031710.png)



#### informed RRT*
产生采样的启发式规则:采用一个椭圆采样方式来代替全局均匀采样
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183144.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183158.png)

以起点 $x_{start}$ 和终点 $x_{goal}$ 作为椭圆的焦点，令 $a$ 等于初始路径长度的一半，即 $a = \frac{c_{best}}{2}$，则 $c = \frac{c_{min}}{2}$，$b = \frac{\sqrt{c_{best}^2 - c_{min}^2}}{2}$。这样就可以得到椭圆方程的所有参数。

在之后的迭代中，没找到一次更短的路径，就用这条更短路径的长度作为新的 $c_{best}$，更新采样椭圆。

然后**在椭圆采样区域中进行采样**。



[路径规划 | 随机采样算法：Informed-RRT\* - 知乎](https://zhuanlan.zhihu.com/p/372315811)

## Kinodynamic
运动动力学

- **控制空间采样**：选择一个输入$u$，固定一个持续时间$T$，前向模拟系统（数值积分）；一般都是幂0矩阵
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183841.png)
- **状态空间采样**：算则一个$s_f$ 找到两个状态$s_0$与$s_f$之间的连接
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183859.png)

### 小车模型

- simple car model
- Dubins car model
- Reeds-Shepp car model

### State-state Boundary Value Optimal Control Problem

### State Lattice Search
lattice: 广义的栅格

构成状态和状态之间的搜索图




9-discretization & 25-discretization 

a_x = [-a_m,0,a_m]
a_y = [-a_m,0,a_m]
排列：3x3=9种


构建图的方法：可以剪枝，根据模型的性质有很强的对称性；控制图的层数



### 后向采样问题的求解器
BVP | Boundary Value Problem 边值问题


1. 构建哈密顿函数
2. 构建正则方程组
3. 最小值原理
4. 相轨迹分析
5. 确定最优量



![](https://i-blog.csdnimg.cn/blog_migrate/b08c1999103b530af6670e6e43d34ffe.png)
### 优化
- 工程上一般采用轨迹库：trajectory library，只维护一层图
- 启发式函数；不考虑动力学；不考虑障碍物

[Boundary Value Problem (BVP) 两点边界最优控制问题-CSDN博客](https://blog.csdn.net/weixin_44673253/article/details/125114116)

### Kinodynamic RRT*


### Hybrid A*

运用A*对lattice graph进行剪枝

   传统的A * 算法是在栅格地图中进行搜索，可行路径中的点，都是栅格地图的中心点，如下面的第一幅图所示，lattice planner算法是先构建一个用于搜索的lattice图，如下面的第二幅图所示，Hybrid A* 算法结合了A * 算法和lattice planner算法的思想，将栅格地图的路径搜索与lattice图结合起来，在搜索过程中选取不同的控制量预演一段轨迹，且保持在每个栅格中仅保留一个可行的状态，如下面的第三幅图所示
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023190050.png)


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241023183547.png)
[动力学约束下的运动规划算法——Hybrid A\*算法（附程序实现及详细解释）\_pythonrobotics hybrida\*-CSDN博客](https://blog.csdn.net/qq_44339029/article/details/132466521)