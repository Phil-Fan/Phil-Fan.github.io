# 数据结构与算法



## 第二章 主定理

### **时间复杂度定义**

![image-20230101145242893](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145242893.png)

定义2.5：若存在c>0和n0，当N>n0时，T(N)>cq(N)，则记为T(N) = w(q(N))

![image-20230101145822408](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145822408.png)

![image-20230101145831844](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145831844.png)

$O(1)$ 是指$f(n)$ 有上界



### **法则1,2,3**

$$
rule1 \\
IF T_1(N) = O(f(N)) and T_2(N) O(g(N))\\
\begin{align}
	T_1(N) + T_2(N) &= O(f(N) + g(N))\\
	T_1(N) * T_2(N) &= O(f(N) * g(N))\\
\end{align}
$$

![image-20230101145916672](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145916672.png)

主要考虑 最坏可能性 与 平均可能性



### **主定理**

<img src="https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101154020619.png" alt="image-20230101154020619" style="zoom:50%;" />

<img src="https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101154044049.png" alt="image-20230101154044049" style="zoom:50%;" />

[时空复杂度分析及master定理 - Chanis 的博客 - 洛谷博客 (luogu.com.cn)](https://www.luogu.com.cn/blog/Chanis/master)

[重谈主定理（master定理）及其证明 - 这人太菜了 - 洛谷博客 (luogu.com.cn)](https://www.luogu.com.cn/blog/GJY-JURUO/master-theorem)

![数据范围](https://gitee.com/philfan/my-images/raw/master/26845.png)

![例题](https://img-blog.csdnimg.cn/4afab6cb811245649465647d62c45a31.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzU2MDkxMw==,size_16,color_FFFFFF,t_70#pic_center)



## 第三章 表、堆、队列

### **表的数组实现**

查找的时间复杂度 `O(1)`

插入和删除的时间复杂度 `O(N)`

### **单链表**

每一个节点都含有一个表元素和链，该链指向包含该元素后继元的另一个节点，最后一个单元的`next link`指向`nullptr`。

插入和删除操作时间复杂度是 `O(1)`

查询时间复杂度是 `O(N)`

```c++
template <typename DT>
void SingleLinkedList<DT>::insert(DT _val)
{
    if (head == nullptr)
    {
        Node *p = new(Node);
        p->data = _val;
        p->next = nullptr;
        head = p;
        size++;
        currentPosition = head;
    }
    else
    {
        Node *p = new(Node);
        p->data = _val;
        p->next = currentPosition->next;
        currentPosition->next = p;
        size++;
    }
}
```

```c++
template <typename DT>
void SingleLinkedList<DT>::remove()
{
    if (currentPosition == nullptr)
        return;
    if (currentPosition->next == nullptr)
    {
        std::cerr << "Out of Range!" << std::endl;
        std::exit(-1);
    } 
    Node* p = currentPosition->next;
    currentPosition->next = p->next;
    delete p;
    size--;
}
```

### **双链表**

双向链表解决了单向链表 知道删除某一节点但不能获取上一节点的缺点

#### **插入操作**

![image-20230101164802876](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101164802876.png)

![image-20230101164821049](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101164821049.png)

#### **删除操作**

![image-20230101164855945](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101164855945.png)

### 堆栈

#### **特点：**

先进后出 后进先出 `LIFO : last in first out`

push()向栈输入 pop()从栈输出

#### **实现形式：**

①：单链表 

push() 表的前端插入元素 pop()删除表的前端元素

②：数组

push() push_back()   pop() pop_back()函数

#### **应用**：

计算后缀表达式

[中缀转后缀](https://zhuanlan.zhihu.com/p/135433833)



### 队列

**特点：**

先进先出 `FIFO : first in first out`

`enquene()`入队 `dequene()`出队

**队列的数组实现：**

保留一个数组`theArray`以及位置`front`和`back`，代表队列的两端，以及队列中的元素个数currentSize

`enquene()`：currentSize和back都+1;theArray[back] = x；

`dequene()`：currentSize和front都-1



#### 用数组模拟链表

```
data[] = {5.5,6.7,7.2,9.3,-1,255,3.1,114,514}

next[] = {-1,0,4,0,0,0,2,0,0}

head = 6

3.1->7.2->-1->5.5
```



## 第四章 树型结构

### 术语解释

树是N个节点和N-1条边的集合

节点$n_i$的**深度**为从根到ni的唯一路径的长

节点$n_i$的**高度**为从ni到一片树叶的最长路径的长

树的高度等于根的高度



### 性质

- 节点数 = 所有节点的度数+1
- 度为m的树，第i层至多有$m^{i-1}$个节点
- 最多节点：（等比数列求和）$\frac{m^h - 1}{m-1}$
- n个结点的m叉树最小高度 代入上一行

1、先序遍历：先遍历根节点，再遍历左节点，最后遍历右节点；
2、中序遍历：先遍历左节点，再遍历根节点，最后遍历右节点；
3、后序遍历：先遍历左节点，再遍历右节点，最后遍历根节点；

### 二叉树

**特点：**

每个节点都不能有多于两个的儿子

 **实现：**

![image-20230101184951393](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101184951393.png)



### 二叉查找树`BST binary search tree`

#### **特点：**

对于树中的每一个节点X，它的左子树中所有项的值都小于X中的项，它的右子树中所有项的值都大于X中的项。

**contains**

思路：遇到比X小的节点就递归右子树；遇到比X大的节点就递归左子树

![image-20230101190630001](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101190630001.png)

#### **findMin和findMax**

思路：一直往左走或者一直往右走

![image-20230101190756266](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101190756266.png)

#### **insert**

思路：像contains一样沿着树查找，如果找到X则什么也不做，否则将X插入到所遍历路径的最后一点上。

<img src="https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101191356007.png" alt="image-20230101191356007"  />

#### **remove**

思路：

如果节点是树叶，直接删除

如果节点有一个儿子，则该节点的父节点调整它的链以绕过该节点后删除

如果节点有两个儿子，用其右子树的最小数据代替该节点的数据并且递归删除那个节点

![image-20230101192614904](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101192614904.png)





### **AVL树**

结点数目一定，保持树的左右两端保持平衡，树的查找效率最高。

用插入的成本弥补查询的效率

但当插入操作多于查询操作时候不方便。

#### **特点：**

带有平衡条件的二叉搜索树，它保证树的深度是O(log(N))，平衡条件为其每个节点的**左子树和右子树的高度最多相差1**的二叉查找树。每个节点都保留高度信息。



#### 方法：

问题结构：左右深度差值>1

从第一个有问题的节点开始，向叶子节点伸展三个节点，把中间数字第二大的节点提升，其他两个节点分列两侧——左边放左边，右边放右边。

![image-20231113142105049](https://gitee.com/philfan/my-images/raw/master/image-20231113142105049.png)

![image-20231113142031094](https://gitee.com/philfan/my-images/raw/master/image-20231113142031094.png)



![image-20230101195437730](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101195437730.png)

1和4 使用单旋转 2和3 使用双旋转

##### **单旋转**

![image-20230101200041908](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101200041908.png)

思路：将X上移一层，Z下移一层，抓住k1轻轻抖动

##### **双旋转**

旋转前条件：

深度高的是左子树，那么左子树平衡必须偏左，如果偏右，则需要加一次旋转使得平衡偏左，最后再右转；

深度高的是右子树，那么右子树平衡必须偏右，如果偏左，则需要加一次旋转使得平衡偏右，最后再左转；

![image-20230101202411868](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202411868.png)

![image-20230101202422717](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202422717.png)

##### **balance**

![image-20230101202654097](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202654097.png)

![image-20230101202711279](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202711279.png)



### 红黑树

#### 特点

最长子树不超过最短子树的2倍

不需要很多旋转

#### 方法

1. 根节点是黑色的
2. 插入节点是红色的
3. 看叔叔脸色（叔叔红脸，三世取反；叔叔黑脸，AVL调整）

#### 缺点

树的深度变多，查找次数增加，io变慢



红黑树不严格要求平衡，且再插入、排序、查询操作时候更为稳定。

在连续插入操作时，效率较高。

[红黑树的插入实现](https://www.bilibili.com/video/BV1fw41117zt)

[什么是红黑树动画理解](https://www.bilibili.com/video/BV1zU4y1H77f)



### 伸展树

应用：输入法候选框，cache



一个节点在一次被访问后，这个节点很可能不久再次被访问。那么伸展树的做法就是在每次一个节点被访问后，我们就把它推到树根的位置。





### B-tree

key-value 文件系统的索引

线性表和哈希表不合适

[b树的引用](https://www.bilibili.com/video/BV1rB4y1Q7e6)



有序的多路平衡查找树

绝对平衡 每一个节点高度都相同，平衡因子均等于0

![image-20231113153948020](https://gitee.com/philfan/my-images/raw/master/image-20231113153948020.png)

![image-20231113154712384](https://gitee.com/philfan/my-images/raw/master/image-20231113154712384.png)



### B+tree

非叶子节点只存储记录，叶子节点存储数据。

把空间让渡给索引

 

## 第五章 散列表与hash

address = H [key] 



找不同 找相同 经典的hash应用



### 散列表

一种以常数平均时间执行插入删除查找的技术

根据关键码值(Key value)而直接进行访问的数据结构。也就是说，它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数，存放记录的数组叫做散列表。

### **冲突**：

当一个元素被插入时与一个已经插入的元素散列到相同的值

#### 分离链接法

将散列到同一个值的所有元素保存到一个链表中

![image-20230101211655326](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101211655326.png)

**装填因子：**散列表中的元素个数/该表的大小  等于链表的平均长度

填装因子越低，发生冲突的可能性越小，散列表的性能越高。一旦填装因子大于1，就应该调整散列表的长度。

#### 线性探测法

遇到冲突后，就按照某种规则，寻找下一个位置，直到找到空位置为止；

线性探测就是在发生冲突后，在原来的地址上往下一个地址找，一个一个的往下探测，直到找到空位置为止。

容易出现一次聚集 适用于装填因子小于0.5

#### 平方探测法

平方探测就是在发生冲突后，在原来的地址上往下（$1^2, 2^2$...）地址找，一个一个的往下探测，直到找到空位置为止。

解决一次聚集问题 快速

#### 双散列



hash1 = x mod m

小于n的质数 z

hash2 =  z - (x mod z)

冲突函数： f(i) = i * hash2(x)

耗时间 预期探测次数几乎和随机冲突解决方法的情形相同

### 再散列

对于使用平方探测的开放定址散列法，如果散列表填的太满，那么操作的运行时间将开始消耗过长，且插入操作可能失败。一种解决方法是建立另外一个大约两倍大的表，扫描整个原始散列列表，计算每个（未删除的）元素的新增散列值将其出入新表中，这个操作就是再散列。

散列表何时扩展，大多数实现是设置一个装载因子α（设m和n分别表示表长和填入的点数，则将α = n/m定义为散列表的装填因子，α越大，表越满，冲突越大。），对于大多数容器α设置为0.75较为合理，0.75是时间和空间上的一种折中。

### 删除方法

- 永不删除
- 标记法
- 

#### 伪随机数

独立

均匀 同余方法保证

简单均匀哈希 simple uniform hashing

$P(h(k) = i) = \frac{1}{m}$

$E[T] = (1+\Theta(\frac{n}{m})),\alpha := \frac{n}{m}$ 为装载率

#### 乘同余方法

![image-20231120140954994](https://gitee.com/philfan/my-images/raw/master/image-20231120140954994.png)

### MT19937



**全域散列解决的是确定性散列算法无法应对特殊输入的问题**。我们有 m（为方便讨论，不妨设 m 远大于 2）个格子时，单个好的散列函数的冲突概率是 1/m（已经均匀散列了，但还会恰好两个掉到同一个格子里）。但是，我们可以为这个“好的”散列函数精心构造输入数据：把正好都掉到一个格子里的数拿出来作为输入，这样冲突概率就 100% 了。**我们要解决的问题是，对于精心构造的输入，冲突率仍然可以达到 1/m。**

**灵感是随机地选散列函数。**如果散列函数是随机选择的，那么精心构造的数据就不一定起作用了。但是，

1. 多少个备选函数才够呢？比如，两个是不够的。比如我们有两个散列函数 h1 和 h2 来随机选择，各 50% 概率被选到。那么构造一个 h1 的特殊输入（让 h1 100% 冲突），这个输入里任意两个元素仍然会有 50% 的情况一定冲突（就是 h1 被选中的概率），没有达到理想的 1/m。
2. 备选函数够多就可以吗？比如，这些函数都会在两个特殊的点上面冲突，即存在 x != y，使得任取 h 都有 h(x) == h(y)，那么用这两个点作为输入，冲突概率就是 100%。也就是说，这些函数冲突的地方还不能太重合。

**全域散列指出可以选择 |H| 个散列函数，且它们最大重合 ≤ |H|/m**。其中重合是指，对任意 x != y，散列函数集合 H 中 h(x) == h(y) 的散列函数个数。随机选择散列函数后，对于精心构造的 x, y（我知道 x, y 会在某个或某些函数上冲突），能够被这个 x, y 命中的散列函数个数就会 ≤ |H|/m，即命中概率 ≤ |H|/m / |H| = 1/m。也就是说，对于精心构造的输入，冲突率重新达到了 1/m。



### hash的应用

#### 开发应用一：安全加密

说到哈希算法的应用，最先想到的应该就是安全加密。最常用于加密的哈希算法是 MD5（MD5 Message-Digest Algorithm，MD5 消息摘要算法）和SHA（Secure Hash Algorithm，安全散列算法）

#### 开发应用二：唯一标识

哈希算法可以对大数据做信息摘要，通过一个较短的二进制编码来 表示很大的数据



## 第六章 优先队列和二叉堆

### 优先队列

特点：

插入以及删除最小者 可以找出、返回并删除优先队列中最小元素

### 二叉堆

二叉堆是一种特殊的堆，二叉堆是完全二叉树或者是近似完全二叉树。

二叉堆有两种：最大堆和最小堆。最大堆：父结点的键值总是大于或等于任何一个子节点的键值；最小堆：父结点的键值总是小于或等于任何一个子节点的键值 最小堆最小值在根节点处

可以使用数组表示 对于数组任意位置i的元素，左儿子在2i上，右儿子在2i+1上，父亲在[i/2]上

#### **insert**

在下一个可用位置创建一个空穴，将X放入空穴中，若满足则结束；否则将该空穴不断与父节点之间交换，直到X可以插入

![image-20230101220607799](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101220607799.png)

#### **delete**

删除根后留下一个空穴，将空穴进行下滤，直到最后一个元素可以放入空穴中

![image-20230101221136073](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101221136073.png)

## 第七章 sort

![image-20230101230057146](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101230057146.png)





### 桶排序

桶排序（Bucket sort）是将数据分到有限数量的桶子里，然后每个桶再分别排序

先创建n个桶，桶的区间跨度=(最大值-最小值)/桶的数量

遍历原始序列，将序列放入桶中

每个桶内部的元素分别排序

遍历所有桶，将桶中元素依次输出

O（M+N）

### 插入排序

在第p趟，将位置p上的元素向左移动直至找到它在前p+1个元素中的正确位置

时间复杂度O(N^2)

N个互异的元素的数组的平均逆序数是N(N-1)/4

通过交换相邻元素进行排序的任何算法时间复杂度Ω(N^2)

### 堆排序

建立N个元素的二叉堆 O(N)

执行N次deleteMin 每次O(logN)

总运行时间 O（NlogN）

### 归并排序

将数组分而治之，最后再加上线性的O(N)合并的代价

![image-20230101225240004](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225240004.png)

![image-20230101225257854](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225257854.png)

![image-20230101225310487](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225310487.png)

### 快速排序

(1)如果S的元素个数为0或1返回

(2)取S中的一个元素v为枢纽元

(3)将S-v划分成两个不相交的集合

(4)返回{qiucksort(S1),v,qiucksort(S2)}

可以三个元素去中间值来确定枢纽元以及小数组直接快速排序

快速排序最慢O(N^2) 平均sita（NlogN）最坏O（NlogN）





### 计数排序

稳定性：保持顺序不变

### 基数排序

基数排序（Radix Sort）是将待排序序列的每个元素统一为同样位数长度的元素，位数较短的通过补0达到长度一致，然后从最低位或从最高位开始，依次进行稳定的计数排序，最终形成有序的序列



对于每一位进行计数排序，从而达到

穿孔制表机

[查尔斯·巴贝奇](https://zhuanlan.zhihu.com/p/107462919)





## 第八章 

### 等价关系

![image-20230101231048256](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101231048256.png)

find:返回包含给定元素的集合

union:把含有两个等价类合并成一个新的等价类

采用森林 每个节点都只有父节点信息代表类 合并操作只要修改父节点信息即可

合并时采用高度或者大小合并 不要太偏向于一边

## 第九章 DP与图论

 

### DP

#### LCS(longest common subsequence)最长公共子序列

max(dp(i-1,j-1)+1,dp(i,j-1),dp(i-1,j))



#### LIS(Longest Increasing Subsequence) 最长上升子序列





![image-20240116141856812](https://gitee.com/philfan/my-images/raw/master/image-20240116141856812.png)

### 图

#### 邻接表和邻接矩阵

[11. MIT线性代数---矩阵空间、秩1矩阵和小世界图 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/44500497)

[【3.7】线性代数应用：图和矩阵 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/186266784)

[邻接表（Adjacency List） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/618361957)





图的邻接表存储

图的邻接矩阵存储



#### 拓扑排序

对一个有向无环图 ( Directed Acyclic Graph 简称 DAG ) G 进行拓扑排序，是将 G中所有顶点排成一个线性序列，使得图中任意一对顶点 u 和 v ，若边 < u , v > ∈ E ( G )，则 u 在线性序列中出现在 v之前。通常，这样的线性序列称为满足拓扑次序 ( Topological Order )

##### **算法**

对每个顶点计算入度，将所有入度为0的点放入队列，当队列不为空时，删除一个顶点v，并将临接到v的所有顶点的入度-1。只要入度为0就将其放入队列中，那么出队顺序记为拓扑排序。

#### 最短路径算法

##### Floyd算法

常数小，复杂度高

[图-最短路径-Floyd(弗洛伊德)算法](https://www.bilibili.com/video/BV19k4y1Q7Gj)



##### Dji



单源最短路径一般算法：Dijkstra算法

![image-20230102084925781](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230102084925781.png)

##### bellmand ford算法

Bellman-Ford算法大致可以分成三部分：

1.初始化所有d[s],源点d[s]=0,其他d[s]=INF

2.进行n-1次循环，在循环体中遍历所有的边，进行松弛计算（if(d[v]>d[u]+w[u][v]) d[v]=d[u]+w[u][v]）

3.遍历图中所有的边，检验是否出现这种情况：d[v]>d[u]+w[u][v],若出现则返回false,没有最短路



##### SPFA

[【洛谷日报#16】SPFA算法教学 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/58727559)

[最短路算法（Dijkstra + SPFA + Floyd） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/357580063)



#### 最小生成树

[最小生成树详解(模板 + 例题)_最小生成树算法-CSDN博客](https://blog.csdn.net/qq_43619271/article/details/109091314)

##### prim算法

基本思想：对图G(V,E)设置集合S来存放已被访问的顶点，然后执行n次下面的两个步骤(n为顶点个数)

每次从集合V-S中选择与集合S最近的一个顶点(记为u)，访问u并将其加入集合S，同时把这条离集合S最近的边加入最小生成树。
令顶点u作为集合S与集合V-S连接的接口，优化从u能到达的未访问顶点v与集合S的最短距离

##### Kruskal 算法

1 初始化。将所有边都按权值从小到大排序，将每个节点集合号都初始化为自身编号。

2 按排序后的顺序选择权值最小的边（u,v）。

3 如果节点 u 和 v 属于两个不同的连通分支，则将边(u,v)加入边集 TE 中，并将两个连通分支合并。（使用并查集算法）

4 如果选取的边数小于 n-1,则转向步骤2，否则算法结束。







# STL

## `vector`

```c++
# initialization
vector<int> a;
vector<int> v(n); //length = n
vector<int> v(n); //length = n, all element is equavalent to 1

v.front();
v.back();
v.popback();
v.pushback();
v.size();
v.clear();
v.begin();
v.end();
v.empty();

# sort
sort(a.begin()+1,a.end())

```



```c++
# iterate
vector<int> v;
vector<int>::iterator it = v.begin();

vector<int>::iterator it;
for(it = vi.begin(); it != vi.end();it ++)
	cout << *it << " ";
//vi.end()指向尾元素地址的下一个地址

// 或者
auto it = vi.begin();
while (it != vi.end()) {
    cout << *it << "\n";
    it++;
}
vector<int> a(n);
for (auto &x: a) {
    cin >> x; // 可以进行输入，注意加引用
}
```

