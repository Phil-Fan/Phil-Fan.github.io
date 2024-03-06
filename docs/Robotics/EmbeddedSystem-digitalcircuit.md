# 数电

逻辑电平

正逻辑：高电平为`1`，低电平为`0`

负逻辑：高电平为`0`，低电平为`1`





## 数制和码制

数字量：离散的

模拟量：连续的

### 进制与进制转换

2，4，16

- x变10：多项式加法
- 10变2：模二取余法
- 2变16：隔4位合并
- 16变2：每位拆成4位二进制
- 其他：通过二进制间接变换

### 运算

- 移位和相加

- 反码
- 补码
  - 最高位符号位：0正1负
  - 正数不变，负数反码+1

> [**为什么要采用反码和补码？？**](https://zhuanlan.zhihu.com/p/99082236)(参考这篇知乎文档)
>
> **采用同余的思想，用加法完成减法的任务**
>
> 在这里，再次强调原码、反码、补码的引入是为了解决做减法的问题。在原码、反码表示法中，我们把减法化为加法的思维是减去一个数等于加上这个数的相反数，结果发现引入符号位，却因为符号位造成了各种意想不到的问题。
>
> 但是从上面的例子中，可以看到其实减去一个数，对于数值有限制、有溢出的运算（模运算）来说，其实也相当于加上这个数的同余数。
>
> 也就是说，不引入负数的概念，就可以把减法当成加法来算。



## 逻辑代数基础

[真值表与逻辑表达式 || 由逻辑表达式列真值表 || 由真值表写逻辑表达式](https://zhuanlan.zhihu.com/p/154529095)

### 与 AND

$$
Y = A\quad AND\quad B = A\&B = A\cdot B = AB
$$

![与关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228121552683.png)

### 或 OR

$$
Y = A \quad OR \quad B = A+B
$$

![或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228121833879.png)

### 非 NOT

$$
Y = A' = NOT \quad A
$$

![非关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122022442.png)

### 异或

不同则为1，相同则为0

**不进位的加法**

$$
Y = A \oplus B
$$

![异或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122336850.png)

### 同或

**不同则为0，相同则为1**
$$
Y = A \odot B
$$

![同或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122444834.png)

### 基本公式

证明方法：推演，真值表

![image-20240301142946084](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301142946084.png)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144447212.png" alt="公式17的证明" style="zoom:35%;" />

![image-20240301144528140](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144528140.png)

### 逻辑函数

[逻辑函数(表示方法、形式转换、化简、最小项、最大项)](https://blog.csdn.net/qq_44431690/article/details/104587163)

- 真值表

- 逻辑式：将输入/输出之间的逻辑关系用与/或/非的运算式表示就得到逻辑式。

- 逻辑图：用逻辑图形符号表示逻辑运算关系，与逻辑电路的实现相对应

  ![逻辑图](https://img-blog.csdnimg.cn/20200301203119397.png)

- 波形图：将输入变量所有取值可能与对应输出按时间顺序排列起来画成时间波形。

  ![波形图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301143107960.png)

- 卡诺图



!!! bug "这里没弄明白"

最简与或：包含的乘积项已经最少，每个乘积项的因子也最少，称为最简的与-或逻辑式

![img](https://pic2.zhimg.com/80/v2-06ac3268bb0d79aea7786e0d763dc2cd_1440w.webp)

并项法
$$
AB + A\bar{B} = A
$$
吸收法
$$
A + AB = A(1+B)= A\\
AB + \bar{A}C + BC = AB + \bar{A}C
$$
消因子
$$
A+\bar{A}B = A+B
$$

配项法
$$
A + \bar{A} = 1\\
A \cdot A = 0
$$
![image-20240306113302112](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240306113302112.png)


## 门电路

门电路中以高/低电平表示逻辑状态的1/0

正逻辑：高电平表示1，低电平表示0负逻辑：高电平表示0，低电平表示1

### 二极管门电路

#### 与门

![与门](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144709854.png)

使用优先导通原理

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144940899.png" alt="判断" style="zoom: 50%;" />

#### 或门

![或门](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144723459.png)

- 二极管构成的门电路的缺点

电平有偏移，带负载能力差

### MOS管门电路



!!! bug "电路具体实现"

![CMOS反相器](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301145253756.png)

![image-20240301145306253](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301145306253.png)

### TTL门电路

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301145508449.png" alt="image-20240301145508449" style="zoom:33%;" /><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301145520310.png" alt="image-20240301145520310" style="zoom:33%;" />

只要参数合理：
$$
\begin{align}
V_I = V_{IL},T截止,V_o = V_{OH}\\
V_I = V_{IH},T导通,V_o = V_{OL}
\end{align}
$$
三极管的基本开关电路就是**非门**

#### 三态输出门（Three state Output Gate ,TS）

![image-20240301150229595](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301150229595.png)

### TTL集成与非门

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301150301018.png" alt="image-20240301150301018" style="zoom:50%;" />

![image-20240301150314521](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301150314521.png)

## 组合逻辑电路

功能上：**输出仅与该时刻的输入有关。**

结构上：由门电路组成，不含记忆（存储）元件。

### 设计方法

一、逻辑抽象

- 分析因果关系，确定输入/输出变量

- 定义逻辑状态的含意（赋值）

- 列出真值表

二、写出函数式

三、选定器件类型

四、根据所选器件：对逻辑式化简（用门）；变换（用MSI）； 或进行相应的描述（PLD）

五、画出逻辑电路图，或下载到PLD

???+note "Example —— 红绿灯故障检测"
    ![image-20240301151233403](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301151233403.png)<br>
    |  R   |  A   |  G   |  Z   |
    | :--: | :--: | :--: | :--: |
    |  0   |  0   |  0   |  1   |
    |  0   |  0   |  1   |  0   |
    |  0   |  1   |  0   |  0   |
    |  0   |  1   |  1   |  1   |
    |  1   |  0   |  0   |  0   |
    |  1   |  0   |  1   |  1   |
    |  1   |  1   |  0   |  1   |
    |  1   |  1   |  1   |  1   |
    逻辑表达式<br>
$$
    \begin{align}
    Z &= R'A'G'+R'AG + RA'G + RAG'+RAG\\
    &=R'A'G'+RA+RG+AG
    \end{align}
$$
​    <br>
​    ![image-20240301151540684](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301151540684.png)<br>

编码器

•编码：将输入的每个高/低电平信号变成一个对应的二进制代码

•普通编码器

任何时刻只允许输入一个编码信号

![image-20240301153440191](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301153440191.png)

![image-20240301153448177](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301153448177.png)



优先编码器

允许同时输入两个以上的编码信号，但只对其中优先权最高的一个进行编码。

译码器

译码：将每个输入的二进制代码译成对应的输出高、低电平信号

•常用的有：二进制译码器，二-十进制译码器，显示译码器等



## 触发器



## 时序逻辑电路







