# 第四章 Tree

## 术语解释

树是N个节点和N-1条边的集合

节点$n_i$的**深度**为从根到ni的唯一路径的长

节点$n_i$的**高度**为从ni到一片树叶的最长路径的长

树的高度等于根的高度



## 性质

- 无环
- 加上一条边就有环，去掉一条边就不连通
- 节点数 = 所有节点的度数+1
- 度为m的树，第i层至多有$m^{i-1}$个节点
- 最多节点：（等比数列求和）$\frac{m^h - 1}{m-1}$
- n个结点的m叉树最小高度 代入上一行

1、先序遍历：先遍历根节点，再遍历左节点，最后遍历右节点；
2、中序遍历：先遍历左节点，再遍历根节点，最后遍历右节点；
3、后序遍历：先遍历左节点，再遍历右节点，最后遍历根节点；

## 二叉树

**特点：**

每个节点都不能有多于两个的儿子

 **实现：**

![image-20230101184951393](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101184951393.png)



## 二叉查找树`BST binary search tree`

### **特点：**

对于树中的每一个节点X，它的左子树中所有项的值都小于X中的项，它的右子树中所有项的值都大于X中的项。

**contains**

思路：遇到比X小的节点就递归右子树；遇到比X大的节点就递归左子树

![image-20230101190630001](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101190630001.png)

### **findMin和findMax**

思路：一直往左走或者一直往右走

![image-20230101190756266](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101190756266.png)

### **insert**

思路：像contains一样沿着树查找，如果找到X则什么也不做，否则将X插入到所遍历路径的最后一点上。

<img src="https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101191356007.png" alt="image-20230101191356007"  />

### **remove**

思路：

如果节点是树叶，直接删除

如果节点有一个儿子，则该节点的父节点调整它的链以绕过该节点后删除

如果节点有两个儿子，用其右子树的最小数据代替该节点的数据并且递归删除那个节点

![image-20230101192614904](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101192614904.png)





## **AVL树**

结点数目一定，保持树的左右两端保持平衡，树的查找效率最高。

用插入的成本弥补查询的效率

但当插入操作多于查询操作时候不方便。

### **特点：**

带有平衡条件的二叉搜索树，它保证树的深度是O(log(N))，平衡条件为其每个节点的**左子树和右子树的高度最多相差1**的二叉查找树。每个节点都保留高度信息。



### 方法：

问题结构：左右深度差值>1

从第一个有问题的节点开始，向叶子节点伸展三个节点，把中间数字第二大的节点提升，其他两个节点分列两侧——左边放左边，右边放右边。

![image-20231113142105049](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20231113142105049.png)

![image-20231113142031094](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20231113142031094.png)



![image-20230101195437730](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101195437730.png)

1和4 使用单旋转 2和3 使用双旋转

#### **单旋转**

![image-20230101200041908](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101200041908.png)

思路：将X上移一层，Z下移一层，抓住k1轻轻抖动

#### **双旋转**

旋转前条件：

深度高的是左子树，那么左子树平衡必须偏左，如果偏右，则需要加一次旋转使得平衡偏左，最后再右转；

深度高的是右子树，那么右子树平衡必须偏右，如果偏左，则需要加一次旋转使得平衡偏右，最后再左转；

![image-20230101202411868](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202411868.png)

![image-20230101202422717](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202422717.png)

#### **balance**

![image-20230101202654097](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202654097.png)

![image-20230101202711279](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101202711279.png)



## 红黑树

### 特点

最长子树不超过最短子树的2倍

不需要很多旋转

### 方法

1. 根节点是黑色的
2. 插入节点是红色的
3. 看叔叔脸色（叔叔红脸，三世取反；叔叔黑脸，AVL调整）

### 缺点

树的深度变多，查找次数增加，io变慢



红黑树不严格要求平衡，且再插入、排序、查询操作时候更为稳定。

在连续插入操作时，效率较高。

[红黑树的插入实现](https://www.bilibili.com/video/BV1fw41117zt)

[什么是红黑树动画理解](https://www.bilibili.com/video/BV1zU4y1H77f)



## 伸展树

应用：输入法候选框，cache



一个节点在一次被访问后，这个节点很可能不久再次被访问。那么伸展树的做法就是在每次一个节点被访问后，我们就把它推到树根的位置。





## B-tree

key-value 文件系统的索引

线性表和哈希表不合适

[b树的引用](https://www.bilibili.com/video/BV1rB4y1Q7e6)



有序的多路平衡查找树

绝对平衡 每一个节点高度都相同，平衡因子均等于0

![image-20231113153948020](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20231113153948020.png)

![image-20231113154712384](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20231113154712384.png)



## B+tree

非叶子节点只存储记录，叶子节点存储数据。

把空间让渡给索引

 