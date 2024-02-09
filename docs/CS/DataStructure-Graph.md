# 第九章 图论

## 表示方法

### 邻接表和邻接矩阵

[11. MIT线性代数---矩阵空间、秩1矩阵和小世界图 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/44500497)

[【3.7】线性代数应用：图和矩阵 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/186266784)

[邻接表（Adjacency List） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/618361957)





图的邻接表存储

图的邻接矩阵存储



### 拓扑排序

对一个有向无环图 ( Directed Acyclic Graph 简称 DAG ) G 进行拓扑排序，是将 G中所有顶点排成一个线性序列，使得图中任意一对顶点 u 和 v ，若边 < u , v > ∈ E ( G )，则 u 在线性序列中出现在 v之前。通常，这样的线性序列称为满足拓扑次序 ( Topological Order )

##### **算法**

对每个顶点计算入度，将所有入度为0的点放入队列，当队列不为空时，删除一个顶点v，并将临接到v的所有顶点的入度-1。只要入度为0就将其放入队列中，那么出队顺序记为拓扑排序。





## 最短路径算法

### Floyd算法

常数小，复杂度高

[图-最短路径-Floyd(弗洛伊德)算法](https://www.bilibili.com/video/BV19k4y1Q7Gj)



### Dji



单源最短路径一般算法：Dijkstra算法

![image-20230102084925781](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230102084925781.png)

### bellmand ford算法

Bellman-Ford算法大致可以分成三部分：

1.初始化所有d[s],源点d[s]=0,其他d[s]=INF

2.进行n-1次循环，在循环体中遍历所有的边，进行松弛计算（if(d[v]>d[u]+w[u][v]) d[v]=d[u]+w[u][v]）

3.遍历图中所有的边，检验是否出现这种情况：d[v]>d[u]+w[u][v],若出现则返回false,没有最短路



### SPFA

[【洛谷日报#16】SPFA算法教学 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/58727559)

[最短路算法（Dijkstra + SPFA + Floyd） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/357580063)



## 最小生成树

[最小生成树详解(模板 + 例题)_最小生成树算法-CSDN博客](https://blog.csdn.net/qq_43619271/article/details/109091314)

### prim算法

基本思想：对图G(V,E)设置集合S来存放已被访问的顶点，然后执行n次下面的两个步骤(n为顶点个数)

每次从集合V-S中选择与集合S最近的一个顶点(记为u)，访问u并将其加入集合S，同时把这条离集合S最近的边加入最小生成树。
令顶点u作为集合S与集合V-S连接的接口，优化从u能到达的未访问顶点v与集合S的最短距离

### Kruskal 算法

1 初始化。将所有边都按权值从小到大排序，将每个节点集合号都初始化为自身编号。

2 按排序后的顺序选择权值最小的边（u,v）。

3 如果节点 u 和 v 属于两个不同的连通分支，则将边(u,v)加入边集 TE 中，并将两个连通分支合并。（使用并查集算法）

4 如果选取的边数小于 n-1,则转向步骤2，否则算法结束。