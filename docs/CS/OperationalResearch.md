# 规划论 | Mathematical Programming

???+note "课程信息"
    === "回忆卷"
        [hy运筹学23夏回忆](https://www.cc98.org/topic/5630278)<br>
		[23梁军回忆卷](https://www.cc98.org/topic/5630287)<br>
		[2022年夏 控院运筹学 lj老师回忆卷](https://www.cc98.org/topic/5345089)<br>
		[2022夏学期 控院运筹学 hy老师回忆卷](https://www.cc98.org/topic/5344993)<br>
		[2022夏学期 控院运筹学 wzg老师回忆卷](https://www.cc98.org/topic/5344941)<br>
		[18-19春夏 运筹学 试题回忆](https://www.cc98.org/topic/4855659)<br>
		[17-18电气学院运筹学回忆](https://www.cc98.org/topic/4778040)<br>

    === "资料"
    	[pcgg分享](https://www.cc98.org/topic/5671695)<br>
        [运筹学控院hy老师班笔记整理](https://www.cc98.org/topic/5630999)<br>
        [2021-2022春夏 管理学院-应用运筹学I（英文班） 学习分享](https://www.cc98.org/topic/5360245) <br>



> 知识是学不完的，最重要的是学习思想
>
> 
>
> 为什么学习运筹学？
>
> - 运筹学有丰富的优化思想与技术
> - 提供科学管理和决策的方法



## 线性规划

### 数学表述与标准形式

线性规划问题的一般数学模型可以表示为：

目标函数：maximize (或 minimize) $Z = c_1x_1 + c_2x_2 + \cdots + c_nx_n$

约束条件：

1. $a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n \leq b_1$<br>
2. $a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n \leq b_2$<br>
3. $\cdots$<br>
4. $a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n \leq b_m$<br>
5. $x_1, x_2, \cdots, x_n \geq 0$<br>

$C_n$为价值向量，$x_n$是约束变量，$A$是工艺矩阵，B为约束向量



**矩阵**方式表示为：

$Z = \begin{bmatrix} c_1 & c_2 & \cdots & c_n \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \mathbf{c}^T \mathbf{x}$

约束条件：

$\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} \leq \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}$

即 $\mathbf{A}\mathbf{x} \leq \mathbf{b}$，以及非负约束：$\mathbf{x} \geq \mathbf{0}$



**向量形式**
$$
\begin{align*}
max(min)\quad &z = CX\\
s.t. \quad&\Sigma P_j x_j \le b\\
&X \ge 0,unr
\end{align*}
$$



**线性规划问题的标准形式**


$$
\begin{align*}
max \quad &z = \mathbf{C}X\\
s.t. &\left\{
	\begin{array}{**lr**}  
		\mathbf{A}x = \vec{b}\\
		x\ge 0 
	\end{array}
	\right.
\end{align*}
$$

> 可参照[【线性规划2】线性规划的标准型 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/31729190)中的例题

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-60940d3d6f2b4378f3cb88c0217f25ed_1440w.webp" alt="img" style="zoom: 33%;" /><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-c67044816117c7099e3d4c264edff055_1440w.webp" alt="img" style="zoom:33%;" /><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-66da5ba9c5f0c5ddfb02c4ab77d26479_1440w.webp" alt="img" style="zoom:33%;" />



### 图解法

找到可行域

移动平行直线



从图解法我们可以发现有以下规律

1. 解的情况:唯一最优解、无穷最优解、无界解（少了约束）无可行解（约束矛盾，鱼与熊掌不可得兼）<br>
2. 可行域很可能是一个凸集<br>
3. 最优解若存在，很可能就是可行域的顶点<br>



### 数学技巧：

**变量条件转化为标准约束**

$$
\begin{align*}
x_j \ge 0 \quad &不变\\
x_j \le 0 \quad &取x_j' = -x_j\\
x_j \ 无约束 \quad &取x_j'\ge 0,x_j''\ge 0,x_j = x_j'-x_j''
\end{align*}
$$

**约束条件的转化**

把不等式条件转化为等式条件
$$
\begin{align*}
\sum^n_{j=1} a_{ij}{x_j} \le b_i \quad\rightarrow\quad \sum^n_{j=1} a_{ij}x_{j} + x_{si}= b_i\\
x_{sj} \quad 松弛变量
\end{align*}
$$

**目标函数的转化**
$$
\begin{align*}
max \ z = \Sigma C_j x_j \quad &不变\\
 min \ z = \Sigma C_j x_j \quad &取 z' = -z\\
 \end{align*}
$$





!!! bug "拉格朗日方程不可以用"
	$x\ge 0$这个条件不可以用求极值的方法

??? note "定义"
    === "可行域"
    在线性规划问题中，可行域是指满足所有约束条件的区域。换句话说，可行域包含了所有可行的解，即满足所有约束条件的解。

    数学表示：对于线性规划问题 $\max Z = \mathbf{c}^T\mathbf{x}$，约束条件为 $\mathbf{A}\mathbf{x} \leq \mathbf{b}$ 且 $\mathbf{x} \geq \mathbf{0}$，其可行域可以表示为：
    
    $$
    \mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n \mid \mathbf{A}\mathbf{x} \leq \mathbf{b}, \mathbf{x} \geq \mathbf{0}\}
    $$
    
    其中，$\mathcal{F}$ 表示可行域，$\mathbb{R}^n$ 表示 $n$ 维实数空间。
    
    === "凸集"
    
    **凸集是指集合中任意两点之间的线段仍然属于该集合的集合。**<br>
    
    换句话说，如果集合中任意两点 $\mathbf{x}$ 和 $\mathbf{y}$，以及任意实数 $\lambda \in [0, 1]$，都有 $\lambda\mathbf{x} + (1-\lambda)\mathbf{y}$​ 属于该集合，那么该集合就是凸集。<br>
    
    数学表示：对于集合 $\mathcal{S} \subseteq \mathbb{R}^n$，如果对于任意 $\mathbf{x}, \mathbf{y} \in \mathcal{S}$ 和任意 $\lambda \in [0, 1]$，都有 $\lambda\mathbf{x} + (1-\lambda)\mathbf{y} \in \mathcal{S}$，那么集合 $\mathcal{S}$ 是一个凸集。
    
    === "顶点"
    不出现在任意两点的连线内<br>
    
    凸集的顶点是指凸集中不能被表示为其他点线性组合的点。换句话说，顶点是凸集中的极值点，无法通过凸集中其他点的线性组合来得到。<br>
    
    数学表示：对于凸集 $\mathcal{S} \subseteq \mathbb{R}^n$，如果存在点 $\mathbf{x} \in \mathcal{S}$，使得对于任意 $\mathbf{y}, \mathbf{z} \in \mathcal{S}$ 和任意 $\lambda \in (0, 1)$，都有 $\lambda\mathbf{y} + (1-\lambda)\mathbf{z} \neq \mathbf{x}$，那么点 $\mathbf{x}$ 是凸集 $\mathcal{S}$ 的一个顶点。<br>
    === "解"
    满足$\left\{
    	\begin{array}{**lr**}  
    		\mathbf{A}x = \vec{b}\\
    		x\ge 0 
    	\end{array}
    	\right.
    \end{align*}$的解$\mathbf{x} = (x_1,\dots,x_n)^T$是可行解。可行解的集合叫可行域。目标函数最值叫最优解


​    
​    === "基"
​    系数矩阵$\mathbf{A}=(a_{ij})_{m\times n}$ $rank(A)=m$，$\mathbf{B_{m \times m}}= (p_1,p_2,\dots,p_m)$ 是A的非奇异子矩阵，B称为基。
​    
    === "基向量"
    
    基$\mathbf{B_{m \times m}}= (p_1,p_2,\dots,p_m)$的向量$p_j$称为基向量，其他称为非基变量
    
    === "基解"
    约束方程变为
    
    $$
    \begin{align*}
    \sum^m_{j=1}p_j x_j = b- \sum^n_{j=m+1}p_j x_j
    \end{align*}
    $$
    
    令$x_j=0,\quad j=\left[ m+1,n\right]$
    基解为解向量$\mathbf{x} = (x_1,\dots,x_m,0,\dots,0)^T$
    
    === "基可行解"
    基解中$\mathbf{x} \ge 0$的解

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240501113721301.png" alt="image-20240501113721301" style="zoom:50%;" />

!!! note "定理1若线性规划问题存在可行解，则问题的可行域是凸集"

!!! note "引理1 若$rank(A)=m$，则可行解$x$为基可行解"
	可行解x的正分量所对应的系数列向量线性独立<br>
	必要性证明：基可行解的定义<br>
	充分性证明：<br>
    可行解x是基解,构造x对应的基<br>
    假设x正分量个数为k，可知$k\le m$<br>

    - 如果$k=m$，可直接视正分量对应的列向量为基；<br>
    - 如果$k<m$，总可补充$m-k$个列向量构成基。

!!! note "定理2 线性规划的可行域顶点与**基可行解**一一对应"
    考察逆否命题：$x$不是可行域顶点$\iff$$x$不是基可行解
    1）**$x$不是基可行解$\Rightarrow$ $x$不是可行域顶点**<br>
    可行解$x$不是基可行解<br>
    $\Rightarrow$ $x$正分量对应的系数列向量线性相关<br>
    构造两个可行点<br>
    $\Rightarrow$ $x$为两可行点的凸组合<br>
    $\Rightarrow$$ x$​​不是顶点<br>

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-7de510c8cb1aedc309628d4f2984d2d6_1440w.webp)![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-3b51222801e565e186e6980183f6ae92_1440w.webp)




!!! note "定理3 若线性规划问题有最优解，一定存在一个**最优解是基可行解**"

|     几何概念     |        代数概念        |
| :--------------: | :--------------------: |
|    约束超平面    |  满足一个等式约束的解  |
|    约束半平面    | 满足一个不等式约束的解 |
| 约束半平面的交集 | 满足一组不等式约束的解 |
| 约束超平面的交点 |          基解          |
|   可行域的顶点   |        基可行解        |
|  目标函数等值面  |   目标函数值相同的解   |

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200507160216458.png)

### 一、基本单纯形法

> 博客
>
> [【运筹学】单纯形法总结 ( 单纯形法原理 | 单纯形法流程 | 单纯形表 | 计算检验数 | 最优解判定 | 入基变量 | 出基变量 | 方程组同解变换 ) ★★★-CSDN博客](https://hanshuliang.blog.csdn.net/article/details/114498881)
>
> 详细步骤解答
>
> [【Wu的课堂】《运筹学》单纯形法中文讲解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1j7411d7Gm/?spm_id_from=333.880.my_history.page.click)
>
> 思想
>
> **解必然存在于顶点处，那么只需要验证顶点就可以了，但是一个一个验证很麻烦，所以采用相邻迭代**



<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240501140607194.png" alt="image-20240501140607194" style="zoom:50%;" />

基本单纯形法是一种求解线性规划问题的方法，包括以下几个步骤：

- **松弛化为标准形式**：通过添加松弛变量将不等号化为等号，并保证所有变量都大于等于0。找到一组单位矩阵

- **找初始基可行解**：通常通过构造某一部分单位矩阵来找到初始基可行解。

- **最优性检验**：计算检验数$\sigma$​，即目标函数系数与对应基变量系数的差值。<br>

  $\sigma_j = c_j - \Sigma^m_{i=1} c_ia_{ij}$<br>

  没有大于0的最优值时候，跳出循环

  <img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240501153721390.png" alt="image-20240501153721390" style="zoom:50%;" />

- **基可行解迭代**：每次都只变更一个基向量<br>

  入基变量：按检验数最大选取<br>

  出基变量：按$\theta_i = \frac{b_i}{a_{lk}}$​最小选取<br>

  初等行变换<br>

- 最优解判别：根据最终的检验数结果判断是否有唯一解、无穷解或无解。<br>
  若最后检验数全等于0，有唯一可行解<br>若有至少一个检验数小于0，则有无数可行解<br>若检验数全小于0（没有一个等于0），则有无界解。

2、单纯形表的各个元素的含义

![image-20240423091540343](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240423091540343.png)



![5c6bd94b01acd096378bcc5de043abb](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/5c6bd94b01acd096378bcc5de043abb.jpg)

相邻基可行解的非基变量仅有一个不同

![image-20240501153555816](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240501153555816.png)



> 退化：基变量出现零的现象
>
> 影响：可能出现循环迭代

#### 例题

**套裁问题**：注意这种先分情况，再列写方案求解的思路



例：某车间接到制作100套钢架的订单，每套钢架要用长为2.9m，2.1m，1.5m的圆钢各一根，已知原料长7.4m，问应如何下料，可使所用原料最省。

| 方案     | 1    | 2    | 3    | 4    | 5    |
| -------- | ---- | ---- | ---- | ---- | ---- |
| 2.9      | 1    | 2    | 0    | 1    | 0    |
| 2.1      | 0    | 0    | 2    | 2    | 1    |
| 1.5      | 3    | 1    | 2    | 0    | 3    |
| **合计** | 7.4  | 7.3  | 7.2  | 7.1  | 6.6  |
| **剩余** | 0    | 0.1  | 0.2  | 0.3  | 0.8  |

设$x_j$为按方案$j$​下料的原料根数

$$
\begin{align*}
    min \quad z&=0\cdot x_1+0.1\cdot x_2 +0.2\cdot x_3 +0.3\cdot x_4 +0.8\cdot x_5\\
    s.t. &\left\{ 
    	\begin{array}{**lr**}  
    		x_1+ 2x_2 + x_4=100\\
    		2x_3+2x_4 + x_5 =100\\
    		3x_1+ x_2 +2x_3 + 3x_5 =100\\
    		x_1, x_2, x_3, x_4,x_5\ge0\\
    	\end{array}
    \right.
\end{align*}
$$

结果: $X^*=\left[30, 10, 0, 50, 0\right]^T ,\quad z^*=16m$



**最优跟踪控制问题**



已知被控对象的输入输出模型为：

$y(k+1) = 0.5\cdot y(k) + u(k)\quad k = 1,2,\dots,10$

控制输入约束

$|u(k| \le M \quad |u(k+1)-u(k)| \le N \quad k = 1,2,\dots,10$

求使下列目标最小的控制序列$u(k)$

$\mathop{min}\limits_{u(k),1\le k\le 10} \ max |y(k)-r(k)|$



### 二、人工变量法

人工变量法是在无法直接找到单位矩阵作为起始时使用的一种方法，主要步骤包括：

- 引入人工变量：人为引入几个人工变量使其构成对角单位矩阵。
- 目标函数引入M：为了防止引入人工变量对线性规划的最大、最小解产生影响，在目标函数中引入一个正无穷的M。
- 计算检验数：与基本单纯形法类似，计算检验数来确定入基和出基变量。
- 中心元变换：在迭代过程中将人工变量替换成其他已有的变量，如果无法将人工变量替走，则无可行解。

[【运筹学】人工变量法总结 ( 人工变量法解的分析 | 标准型变换 | 构造单位阵 | 目标函数引入 M | 计算检验数 | 选择入基变量 | 选择出基变量 | 中心元变换 | ) ★★_什么时候需要加入人工变量-CSDN博客](https://hanshuliang.blog.csdn.net/article/details/114544508)

（如果无法直接找到单位矩阵，用人工变量法构建单位矩阵）
在无法直接产生与系数矩阵同秩的单位矩阵的时候，人为引入几个人工变量使其构成对角单位矩阵，但是为了防止引入人工变量对线性规划的最大、最小解产生影响，在max/min栏处要-Mxi，这里的M为正无穷，寓意只要新引入的人工变量不为0就会产生很大的影响。
人工变量法的关键在于一定要在不断的迭代过程中将人工变量替换成其他已有的变量，只要人工变量为出基变量，非人工变量为入基变量，人工变量栏也可以消去。人工变量可以看成一个“由头”，在后续迭代过程中将“头”舍去，如果在迭代过程中无法将人工变量替走，则无可行解。

![image-20240423091734877](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240423091734877.png)

### 三、对偶理论

对偶理论是研究原问题和对偶问题之间的关系，包括以下内容：

- 对偶问题的理解：通过生产问题和出租设备问题来理解对偶问题。
- 对偶松弛定理：通过计算对偶解的值，并代入对偶问题的不等式来判断原问题的解。
- 对偶的自反性：问题的对偶的对偶是原问题。
- 对偶单纯形法：在选择出基和入基变量以及最优性检验上与基本单纯形法有所不同。
- 灵敏度分析：对问题的参数变化进行分析，研究其对最优解的影响。



1、对偶问题的理解：
• 生产 : 目标函数追求 利润最大化 , 约束方程设备的使用时长受约束 , 小于等于 某个时间值 ;
• 出租设备 : 目标函数追求 租金最小化 , 约束方程设备产生的利润要 大于等于 生产的利润 , 不能亏钱 ;

2、对偶松弛定理：
先将问题的对偶解算出来，得到对偶解的值（条件1），代入对偶问题的不等式可得到对偶问题不等式是否为严格不等式（条件2）

条件1：说明对偶问题的解如果不为0，原问题的对应解为等式（即AX-b=0）

条件2：反之如果将对偶问题解代入可得为严格不等式，则原问题的对应解为0。

3、对偶的自反性：问题的对偶的对偶是原问题

## 非线性规划

非线性规划是研究目标函数或约束条件为非线性的优化问题，包括解析解法和数值解法：

- 解析解法：包括无约束情况和有约束情况的求解方法，如拉格朗日乘数法、库恩塔格条件等。
- 数值解法：包括基于梯度的数值解法，如最速下降法、牛顿法、拟牛顿法等，以及有约束极值问题的数值解法，如可行方向法、制约函数法等。

## 整数规划

整数规划是要求解变量为整数的线性规划问题，求解方法包括：

- 分支定界法：将每个变量分为上下最接近的两个整数，逐步满足整数规划的约束条件。
- 割平面法：利用整数约束条件引入新变量，构造新的松弛问题进行求解。

## 目标规划

目标规划是线性规划的一种变式，用于处理多目标优化问题，特点包括：

- 目标规划的特点：与线性规划相比，目标规划的约束为软约束，目标可以设定优先级。
- 目标规划的方法：包括集中求解和序贯算法等。

## 运输规划

运输规划是研究如何在满足一定约束条件下，将货物从产地运到销地的最优方案，包括以下内容：

- 运输问题的方法：包括最小元素法、差额法等表上作业法，以及闭回路法等检验最优解的方法。
- 运输规划的秩：由行约束（运出地）和列约束（运入地）的数量决定。

## 不确定规划



