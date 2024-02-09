# 第七章 Sorting

![image-20230101230057146](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101230057146.png)





## 桶排序

桶排序（Bucket sort）是将数据分到有限数量的桶子里，然后每个桶再分别排序

先创建n个桶，桶的区间跨度=(最大值-最小值)/桶的数量

遍历原始序列，将序列放入桶中

每个桶内部的元素分别排序

遍历所有桶，将桶中元素依次输出

O（M+N）

## 插入排序

在第p趟，将位置p上的元素向左移动直至找到它在前p+1个元素中的正确位置

时间复杂度O(N^2)

N个互异的元素的数组的平均逆序数是N(N-1)/4

通过交换相邻元素进行排序的任何算法时间复杂度Ω(N^2)

## 堆排序

建立N个元素的二叉堆 O(N)

执行N次deleteMin 每次O(logN)

总运行时间 O（NlogN）

## 归并排序

将数组分而治之，最后再加上线性的O(N)合并的代价

![image-20230101225240004](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225240004.png)

![image-20230101225257854](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225257854.png)

![image-20230101225310487](https://zjushine-picgo.oss-cn-hangzhou.aliyuncs.com/img/image-20230101225310487.png)

## 快速排序

(1)如果S的元素个数为0或1返回

(2)取S中的一个元素v为枢纽元

(3)将S-v划分成两个不相交的集合

(4)返回{qiucksort(S1),v,qiucksort(S2)}

可以三个元素去中间值来确定枢纽元以及小数组直接快速排序

快速排序最慢O(N^2) 平均sita（NlogN）最坏O（NlogN）





## 计数排序

稳定性：保持顺序不变

## 基数排序

基数排序（Radix Sort）是将待排序序列的每个元素统一为同样位数长度的元素，位数较短的通过补0达到长度一致，然后从最低位或从最高位开始，依次进行稳定的计数排序，最终形成有序的序列



对于每一位进行计数排序，从而达到

穿孔制表机

[查尔斯·巴贝奇](https://zhuanlan.zhihu.com/p/107462919)



