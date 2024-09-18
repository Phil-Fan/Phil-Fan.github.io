# 规划
轨迹规划：考虑速度
运动规划：
路径规划



### 前端—路径搜索

#### 采样

##### PRM

基于概率采样的路径

- 均匀生成采样点
- 将与障碍物接触的点给删除
- 领域点计算：在距离为r的园内均为领域点，将其连接
- 碰撞检测：连线是否与障碍物相交

优点：产生的roadmap可以被复用

缺点：对于给定的起点和终点，非最短路径，效率低

![image-20240427143014709](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240427143014709.png)

[基于采样的运动规划算法-RRT(Rapidly-exploring Random Trees) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/133224593)

##### RRT

- 概率采样，投影
- 与最近点相连接，生成树

优点：容易添加对目标点的引导，效率增加

缺点：无法删除已生成树，但不一定是最短



##### RRT*

相比于RRT增加了Rewrie函数

即在采样之后与最短路径连接后，考虑在某一个定长的圆的范围内，其内的点是否可以连接到新采样的点（用到初始点的距离进行判断）

![image-20240427143031710](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240427143031710.png)



[【算法】路径规划中的Dijkstra(狄克斯特拉)与A星算法_dijkstra和a星算法的差异-CSDN博客](https://blog.csdn.net/QLeelq/article/details/113862917)

#### 搜索

##### Dijkstra’s   

加了权重的广度优先算法

##### A*

在Dijkstra's算法的基础上，加了对于距离目标点的预测方向，因而有了更强的目的性

##### JPS

在图上搜素



三者都是最优解

### 后端—轨迹优化

#### Basic Minimum-snap  



#### 硬约束与软约束轨迹优化  

Hard constrained Minimum-snap  

Soft Constrained Trajectory Optimization


