# 队列

**特点：**

先进先出 `FIFO : first in first out`

`enquene()`入队 `dequene()`出队

**队列的数组实现：**

保留一个数组`theArray`以及位置`front`和`back`，代表队列的两端，以及队列中的元素个数currentSize

`enquene()`：currentSize和back都+1;theArray[back] = x；

`dequene()`：currentSize和front都-1



### 用数组模拟链表

```
data[] = {5.5,6.7,7.2,9.3,-1,255,3.1,114,514}

next[] = {-1,0,4,0,0,0,2,0,0}

head = 6

3.1->7.2->-1->5.5
```



## 优先队列

特点：

插入以及删除最小者 可以找出、返回并删除优先队列中最小元素

## 二叉堆

二叉堆是一种特殊的堆，二叉堆是完全二叉树或者是近似完全二叉树。

二叉堆有两种：最大堆和最小堆。最大堆：父结点的键值总是大于或等于任何一个子节点的键值；最小堆：父结点的键值总是小于或等于任何一个子节点的键值 最小堆最小值在根节点处

可以使用数组表示 对于数组任意位置i的元素，左儿子在2i上，右儿子在2i+1上，父亲在[i/2]上

### **insert**

在下一个可用位置创建一个空穴，将X放入空穴中，若满足则结束；否则将该空穴不断与父节点之间交换，直到X可以插入

![image-20230101220607799](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101220607799.png)

### **delete**

删除根后留下一个空穴，将空穴进行下滤，直到最后一个元素可以放入空穴中

![image-20230101221136073](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101221136073.png)

