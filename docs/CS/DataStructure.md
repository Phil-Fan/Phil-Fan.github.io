# 数据结构与算法



## 第二章 主定理

### **时间复杂度定义**


**定义 2.1:** 如果存在正常数 \(c\) 和 \(m_{0}\) 使得当 \(N \geqslant m_{0}\) 时 \(T(N) \leqslant c f(N)\), 则记为 \(T(N)=O f(N)\) 。


**定义 2.2:** 如果存在正常数 \(c\) 和 \(m_{0}\) 使得当 \(N \geqslant m_{0}\) 时 \(T(N) \geqslant c g(N)\), 则记为 \(T(N)=\Omega(g(N))\) 。


**定义 2.3: ** \(T(N)=\Theta(h(N))\) 当且仅当 \(T(N)=O(h(N))\) 且 \(T(N)=\Omega(h(N))\) 。


**定义 2.4:** 如果对每一正常数 \(c\) 存在常数 \(m_{0}\) 使得当 \(N \geqslant m_{0}\) 时 \(T(N) \leqslant c p(N)\), 则 \(T(N)=\)
 \(o(p(N))\) 。也可简述为, 如果 \(T(N)=O(p(N))\) 且 \(T(N) \neq \Theta(p(N))\), 则 \(T(N)=o(p(N))\) 。

**定义2.5：** 若存在c>0和n0，当N>n0时，T(N)>cq(N)，则记为T(N) = w(q(N))

![image-20230101145822408](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145822408.png)

![image-20230101145831844](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145831844.png)

$O(1)$ 是指$f(n)$ 有上界



### **法则1,2,3**

$$
rule1 \\
IF \quad T_1(N) = O(f(N)) \ and \ T_2(N) O(g(N))\\
\begin{align}
	T_1(N) + T_2(N) &= O(f(N) + g(N))\\
	T_1(N) * T_2(N) &= O(f(N) * g(N))\\
\end{align}
$$

![image-20230101145916672](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101145916672.png)

主要考虑 最坏可能性 与 平均可能性



### **主定理**

$$
T(n) = aT(\frac{n}{b}) + f(n)
$$

<!-- <img src="https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101154044049.png" alt="image-20230101154044049" style="zoom:50%;" /> -->

- (1) 若 \(f(n)<n^{\log _b^a}\) , 且是多项式的小于。即\(\exists \varepsilon>0\), 有 \(f(n)=O\left(n^{\log_b^a-\varepsilon}\right)\), 则 \(T(n)=\Theta\left(n^{\log_{b}^a}\right)\)
- (2) 若 \(f(n)=n^{\log _{b}^a}\), 则 \(T(n)=\Theta\left(n^{\log _{b}^ a} \log n\right)\)
- (3) 若 \(f(n)>n^{\log_b^a}\), 且是多项式的大于。即\(\exists \varepsilon>0\), 有 \(f(n)=\Omega\left(n^{\log_{b}^a+\varepsilon}\right)\), 且对 \(\forall c<1\) 与所有足够大的 \(n\), 有 \(a f\left(\frac{n}{b}\right) \leqslant c f(n)\), 则 \(T(n)=\Theta(f(n))\)

[时空复杂度分析及master定理 - Chanis 的博客 - 洛谷博客 (luogu.com.cn)](https://www.luogu.com.cn/blog/Chanis/master)

[重谈主定理（master定理）及其证明 - 这人太菜了 - 洛谷博客 (luogu.com.cn)](https://www.luogu.com.cn/blog/GJY-JURUO/master-theorem)

![数据范围](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/26845.png)

![例题](https://img-blog.csdnimg.cn/4afab6cb811245649465647d62c45a31.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzU2MDkxMw==,size_16,color_FFFFFF,t_70#pic_center)

### P,NP,NP Hard

- **P 问题**：P 问题是可以在多项式时间内得到最优解的问题。
- **NP 问题**：NP 问题是可以在不确定的多项式时间内验证一个解是否可行的问题。
- **NP-hard 问题**：NP-hard 问题是所有 NP 问题的求解都可在多项式时间复杂度内归约成的问题，也是更难求解的问题。
- **NP-complete 问题**：NP-complete 问题是 NP-hard 问题中为 NP 的问题。

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



## 第八章 等价关系



### 等价关系

![image-20230101231048256](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101231048256.png)

find:返回包含给定元素的集合

union:把含有两个等价类合并成一个新的等价类

采用森林 每个节点都只有父节点信息代表类 合并操作只要修改父节点信息即可

合并时采用高度或者大小合并 不要太偏向于一边









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

