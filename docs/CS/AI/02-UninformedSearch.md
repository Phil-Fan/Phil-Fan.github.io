# Uninformed Search

| 评判标准 | 广度优先 (BFS) | 深度优先 (DFS) | 有限深度 (DLS) | 迭代加深 (IDS) |
|----------|----------------|----------------|----------------|----------------|
| 简单表述 | 从最浅节点开始扩展，探索所有可能性。序列为先进先出 | 一条路径一直向下扩展，没有节点可以扩展就向前回溯，序列为先进后出 | 在DFS基础上限制深度在一个常数$l$，防止过深。 | 逐步增加深度限制$l$ |
| 完备性(是否有解) | Yes           | No             | Yes, if l ≥ d  | Yes            |
| 最优性（是否最优解） | No/Yes        | No             | No             | No/Yes         |
| 时间     | O(bd+1)       | O(bm)          | O(bl)          | O(bd)          |
| 空间     | O(bd+1)       | O(bm)          | O(bl)          | O(bd)          |

*注：DFS不完备是因为可能陷入无穷循环，不满足最优性是因为默认*



## BFS
Breadth-first Search （宽度优先搜索）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/02373e65ff0b858a0e1d46f99f5d1a29.gif)


!!! note "可以实现两类问题"
    - 从节点A出发，有前往节点B的路径吗
    - 从节点A出发，前往节点B的哪条路径最短




Search Strategy （搜索策略）：扩展最浅的未扩展节点。
Implementation（实现方法）：使用FIFO队列，即新的后继节点放在后面。

Breadth-first Search Algoruthm on a Graph （图的宽度优先搜索算法）

![](https://i-blog.csdnimg.cn/blog_migrate/6d343ab09c49d991ad0a67b93506f433.png)

### 性能分析

完备性：
时间复杂性



### Uniform-cost Search （一致代价搜索）

是对广度优先搜索算法的引伸，扩展路径消耗$g(n)$最低的节点。即$f(n) = g(n)$即启发式搜索的效用函数，是当前路径的评价指标。



## DFS | 深度优先搜索

!!! note "类似于“不撞南墙不回头”"
    BFS 常用于找单一的最短路线，它的特点是 "搜到就是最优解"，而 DFS 用于找所有解的问题，它的空间效率高，而且找到的不一定是最优解，必须记录并完成整个搜索，故一般情况下，深搜需要非常高效的剪枝（剪枝的概念请百度）。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/a88bbfac61dbfa8e000f6bd9c5a0040d.gif)




### 剪枝

Depth-limited Search （深度受限搜索）

若状态空间无限，深度优先搜索就会发生失败。
这个问题可以用一个预定的深度限制$l$得到解决，即：深度$l$以外的节点被视为没有后继节点。
缺点：
如果我们选择$l<d$，即最浅的目标在深度限制之外，这种方法就会出现额外的不完备性。
如果我们选择$l>d$，深度受限搜索也将是非最优的。

### DLS | Depth-limited Search （深度受限搜索）

### Iterative Deepening Search （迭代加深搜索）


### 例题

#### 全排列
```cpp
#include <iostream>
int number[10]={0,1,2,3,4,5,6,7,8,9};
int num[10];
bool vis[10]={0};
void dfs(*int num,int n){
    if (n==10){
        for (int i=0;i<10;i++){
            cout<<num[i];
        }
        cout<<endl;
        return;
    }
    for(int i=0;i<10;i++){
        if (!vis[i]){
            vis[i]=1;
            num[n]=number[i];
            dfs(num,n+1);
            vis[i]=0;
        }
    }
}
int main(){ 
    dfs(num,0);
    return 0;
}
```










## Bidirectional Search （双向搜索）


实际上，BS就是将BFS画的半径为d的一个大圆，换成了半径为d/2的两个小圆。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241017102041.png)