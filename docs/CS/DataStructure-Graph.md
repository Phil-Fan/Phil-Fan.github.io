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

>**Dijkstra和Bellman-Ford的区别**
>
>Dijkstra开头是D，所以是以点为单位进行操作
>
>Bellman-Ford开头是B，所以是以边为单位进行操作

![最短路算法比较](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240116141856812.png)

### Floyd

常数小，复杂度高

[图-最短路径-Floyd(弗洛伊德)算法](https://www.bilibili.com/video/BV19k4y1Q7Gj)



### Dijkstra

假设现在要求出从某一点s到其他所有点的最短距离，对于每个点v均维护一个“当前距离”`（dist[v]）`和“是否访问过”`(visited[v])`。首先将`dist[s]`初始化为0，将其他点的距离初始化为无穷，并将所有点初始化为未访问的。记`u->v`的边权为`weight[u->v]`。然后进行以下步骤：

1. 从所有未访问的点中，找出当前距离最小的，设为u，并将其标记为已访问的。
2. 调整u的所有边（若是有向图则为出边）连接的并且**未被访问过的**点：若`weight[u->v] + dist[u] < dist[v]`, 则将`dist[v]`更新为`dist[u]+weight[u->v]`。
3. 重复1和2步骤，直到所有点都被标记为已访问的，则`dist[i]`即`s`到`i`的最短距离。如果只想求从s到某一点的最短距离，那么当该点被标记为访问过之后可直接退出。
4. 补充：如果除了最短距离之外还想求出具体的路径，只需建立一个`pre`数组，在步骤2后添加操作：`pre[v] = u`（前提是`dist[v]`被更新）。



复杂度分析
$$
正常情况\quad O(n^2)\\
堆优化下 \quad O(n\log n)
$$


```c++
void djikstra(const std::vector<std::vector<int>> &graph, int V,int src){
    std::vector<int> dis(V,INF);
    std::vector<int> visited(V,0);

    dis[src] = 0;

    for(int covered_node = 0 ; covered_node < n-1; covered_node++){//外层是n-1循环
        int min = -1;
        //find the closest node
        for(int i = 0; i < V ; i++){
            if(visited[i] != 1 && (min==-1||dis[i] <= dis[min])){
                min = i;
            }
        }
        visited[min] = 1;
        for(int v = 0; v < V; v ++){
            if(visited[v] == 0 && dis[min] != INF && graph[min][v] && dis[min]+graph[min][v] < dis[v]){
                dis[v] = dis[min] + graph[min][v];
            }
        }   
    }
}
```



### Bellman-Ford

[可视化展示](https://www.bilibili.com/video/BV1j34y1s7d8)

它基于一个很基本的事实：**对于一个不包含负权环的V个点的图，任意两点之间的最短路径至多包含V-1条边。**



Bellman-Ford算法大致可以分成三部分：

1.初始化所有`d[s]`,源点`d[s]=0`,其他`d[s]=INF`

2.进行n-1次循环，在循环体中遍历所有的边，进行松弛计算

```c++
if( d[v] > d[u]+w[u][v] ) 
	d[v] = d[u] + w[u][v]
```

3.遍历图中所有的边，检验是否出现这种情况：`d[v]>d[u]+w[u][v]`,若出现则返回`false`,没有最短路

```c
#define inf 9999999

int s, v, e; // s为源点,v为顶点数,e为边数；
struct Edge{
    int from, to, weight;
};
Edge edges[1000];

int dist[1000], pre[1000];
void bellman(){
    for (int i = 0; i < v; ++i) dist[i] = inf;
    dist[s] = 0;
    for (int i = 1; i <= v - 1; ++i){//只需要n-1条边
        for (int j = 0; j < e; ++j){//循环所有的边进行松弛
            int u = edges[j].from, v = edges[j].to, w = edges[j].weight;
            if (dist[u] + w < dist[v]){
                dist[v] = dist[u] + w;
                pre[v] = u;
            }
        }
    }
}
```



### SPFA`Shortest Path Faster Algorithm`

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