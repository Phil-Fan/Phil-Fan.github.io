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

![image-20240228122022442](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122022442.png)

### 异或

不进位的加法
$$
Y = A \oplus B 
$$
![异或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122336850.png)

### 同或

$$
Y = A \odot B
$$

![同或关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122444834.png)

### 与非

![与非关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122126931.png)

### 或非

![或非关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122142374.png)

### 与或非

![与或非关系](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240228122203636.png)



## 门电路





## 组合逻辑电路





## 触发器



## 时序逻辑电路







