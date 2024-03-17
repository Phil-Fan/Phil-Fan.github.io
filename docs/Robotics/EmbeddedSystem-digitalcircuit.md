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

杂合子
$$
Y = A \oplus B = \bar{A}B + A\bar{B}
$$

![异或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122336850.png)

### 同或

**不同则为0，相同则为1;**

纯合子
$$
Y = A \odot B
$$

![同或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122444834.png)

### 基本公式

证明方法：推演，真值表

![image-20240301142946084](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301142946084.png)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144447212.png" alt="公式17的证明" style="zoom: 50%;" />

![image-20240301144528140](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301144528140.png)

### 逻辑函数

[逻辑函数(表示方法、形式转换、化简、最小项、最大项)](https://blog.csdn.net/qq_44431690/article/details/104587163)



由真值表写逻辑表达式

第一步：从真值表内找输出端为“1”的各行,把每行的输入变量写成乘积形式;遇到“0”的输入变量上加非号。

第二步：把各乘积项相加,即得逻辑函数的表达式。

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



[数字电路-逻辑式化简公式](https://zhuanlan.zhihu.com/p/392457877)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-8dc1606574d995edbc843fb019b38fad_1440w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-61355c6b4a7dba5e2e887c17d8e480a8_1440w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-55a64baa868c2fd6676c3369c66ea3ff_r.jpg)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-939bf95fd46b11c990a59657ff7bc67f_r.jpg)

反演律（**De Morgan's laws**）

并项法
$$
AB + A\bar{B} = A
$$
吸收法（**短项吸收长项**）
$$
A + AB = A(1+B)= A\\
AB + \bar{A}C + BC = AB + \bar{A}C
$$
消因子（**短项能够消去 长项中 的 相反项**）
$$
A+\bar{A}B = A+B\\
A\cdot (1+B) = A+AB+A’B = A+B
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

功能上：**输出仅与该时刻的输入有关**，与控制电路没有关系

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
    |  R   |  A   |  G   |  Z   |<br>
    | :--: | :--: | :--: | :--: |<br>
    |  0   |  0   |  0   |  1   |<br>
    |  0   |  0   |  1   |  0   |<br>
    |  0   |  1   |  0   |  0   |<br>
    |  0   |  1   |  1   |  1   |<br>
    |  1   |  0   |  0   |  0   |<br>
    |  1   |  0   |  1   |  1   |<br>
    |  1   |  1   |  0   |  1   |<br>
    |  1   |  1   |  1   |  1   |<br>
    逻辑表达式<br>
$$
    \begin{align}
    Z &= R'A'G'+R'AG + RA'G + RAG'+RAG\\
    &=R'A'G'+RA+RG+AG
    \end{align}
$$
​    <br>
​    ![image-20240301151540684](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301151540684.png)<br>

### 分析方法

- 从输入级开始，**逐级写出**门的**逻辑表达式**
- 对表达式进行化简
- 列真值表
- 描述电路的逻辑功能

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200404082218222.png)

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/2020022812360080.png)

![八种逻辑门电路符号,8个基本门电路符号图,同或门图形符号_大山谷图库](https://ts1.cn.mm.bing.net/th/id/R-C.17f7966df61b03e0e9ad1338517516bc?rik=TC423C2D%2fk%2bYEA&riu=http%3a%2f%2ffile.elecfans.com%2fweb1%2fM00%2f46%2f1D%2fo4YBAFqTpBGAEefFAADd-9wfZXM945.jpg&ehk=byn9hbynzFmeTQwlsVmRqX14tvd9t3pNdbrpwFnc0V8%3d&risl=&pid=ImgRaw&r=0)



### 加法器

#### 半加器

不考虑来自低位的进位，将两个1位的二进制数相加

![image-20240313103532819](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313103532819.png)

#### 全加器

将两个1位二进制数及来自低位的进位相加

![image-20240313103643704](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313103643704.png)

#### 多位加法器

1.串行进位加法器

优点：简单；缺点：慢

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313103958992.png" alt="image-20240313103958992" style="zoom:50%;" />

2.超前进位加法器

**预测进位信息**

[超前进位加法器（较为详细讲解）-CSDN博客](https://blog.csdn.net/qq_26707507/article/details/106146619)

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200517172901988.png)

基本原理：加到第$i$位的进位输入信号是两个加数第$i$位以前各位$0 \ to\ i-1$​的函数，可在相加前由A,B两数确定。

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200517172150217.png)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200517172524948.png)

可以使用4个4位超前进位加法器组成一个16位的超前进位加法器

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200517173457592.png)

![image-20240313104336683](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313104336683.png)



### 比较器

[专题2-7：数值比较器 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/567962452)

从高到低比较

#### 一位比较

![image-20240313105836046](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313105836046.png)

![image-20240313105805295](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313105805295.png)

> 推导：最上面一条支路函数使用德摩根定律进行化简：
>
> $A\cdot \bar{AB} = A \cdot (\bar{A} + \bar{B}) = A\cdot\bar{B}$​

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-d8395a6b49feb6f83a45ebe81201c8be_1440w.webp)

先实现一位比较，写出逻辑表达式，再给出逻辑图。

注意或非门的画法



#### 两位比较

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-bdaebb6580d3bbdd7a4cc252a0d25e6c_r.jpg)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-e417ce3acbe7a1f6ed053c1efe8dac80_r.jpg)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-1a5b5e5de9e966642139cc2ca11b7027_r.jpg)

#### CC14585  

  实现4位二进制数的比较

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200415151753424.png" alt="在这里插入图片描述" style="zoom:50%;" />

??? bug "这是为什么 为什么采用这种方式"

![image-20240313105942397](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313105942397.png)

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20200415152514518.png)

- 多位比较

级联方式：串联 and 并联

串联需要将后4位的比较结果作为输入，最低一级要将$I_{A=B} = 1,I_{A>B}= I_{A<B} = 0$

> 相当于串一个第零级比较器，且第零级比较结果是相同，所以要比高位

$I_{A=B},I_{A>B},I_{A<B}$称为扩展输入端，为了传递低位的比较结果，便于级联

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-162580e457a1fcb6c7d5b398fbcb9adb_r.jpg)





并联用于位数比较多，且对速度有要求的时候。

由图可以看出这里采用**两级比较方法**，将16 位按高低位次序分成四组，每组4位，**各组的比较是并行进行的**。将每组的比较结果再经4位比较器进行比较后得出结果。

显然，从数据输入到稳定输出只需2倍的4 位比较器延迟时间，若用串联方式，则16位的数值比较器从输入到稳定输出需要约四倍的4位比较器的延迟时间。







### 编码器

写的非常清楚的一篇笔记[自上而下理解优先编码器](https://zhuanlan.zhihu.com/p/569801290)

- **编码**：是将信息从一种形式或格式转换为另一种形式的过程。在数字电路中，用预先规定的方法，将一些逻辑信号转换成二进制数代码，这个过程就称为编码。

- **编码器**：实现编码这一过程的集成组合逻辑电路器件。

#### 普通编码器

任何时刻只允许输入一个编码信号

![image-20240301153440191](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301153440191.png)

![image-20240301153448177](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240301153448177.png)



#### 优先编码器

允许同时输入两个以上的编码信号，但只对其中优先权最高的一个进行编码。





### 译码器

译码：将每个输入的二进制代码译成对应的输出高、低电平信号

•常用的有：二进制译码器，二-十进制译码器，显示译码器等



![3线-8线译码器](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240313111134365.png)

把连续的地址空间变成连续的八片



## 触发器



## 时序逻辑电路







