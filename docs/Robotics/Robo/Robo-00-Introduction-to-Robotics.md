# 机器人导论

!!! note "课程简介"
    - 资源
       [2023春《机器人导论》笔记分享](https://www.cc98.org/topic/5601621)<br>
       [2020-2021春学期《机器人导论》整理复习笔记分享](https://www.cc98.org/topic/5070984)<br>
       [设计框图](https://www.cc98.org/topic/5306160)
    - 回忆卷
       [2022-2023春机器人导论回忆卷](https://www.cc98.org/topic/5597275)<br>
       [2021-2022 春 机器人导论 回忆卷](https://www.cc98.org/topic/5306507)<br>
       [2019-2020春夏机器人导论回忆卷](https://www.cc98.org/topic/4961482)<br>
       [2019-2020春夏部分考试回忆（机器人导论](https://www.cc98.org/topic/4960976/1#1)<br>
       [2020-2021春学期机器人导论回忆卷](https://www.cc98.org/topic/5070617)<br>

![机器人导论](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E6%9C%BA%E5%99%A8%E4%BA%BA%E5%AF%BC%E8%AE%BA.png)

![image-20240416103542259](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416103542259.png)

![image-20240416164110402](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416164110402.png)

## 一、导论



机器人具备的主要特征

- 运动
- 交互
- 感知
- 决策



设计的流程

1. 明确执行机构
2. 确定传动方式
3. 设计导向机构
4. 结构设计
5. 优化分析
6. 组装与测试



执行结构：完成操作任务

传动机构：伺服系统 如齿轮

支撑/导向机构：导向机构作用是**支撑和导向**，使运动能安全、准确地完成特定方向的运动。如：轴承和导轨





## 二、微控制器

总线 bus

GPIO ： general purpose io

二进制减法： 用[补码](https://zhuanlan.zhihu.com/p/99082236)

二进制乘法： 移位相加 倍增

![冯诺依曼.drawio](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E5%86%AF%E8%AF%BA%E4%BE%9D%E6%9B%BC.drawio.svg)

![image-20240416101303336](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416101303336.png)

![e90541dc83a0c99e8be34aef](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/e90541dc83a0c99e8be34aef.png)

 控制器：每一个箭头 决定开关是否打开

 ALU ： 逻辑计算

![0dd3435c8313464ffc25e96f](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/0dd3435c8313464ffc25e96f.png)
 嵌入式系统： 和硬件完全对应

![image-20230907135656516](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135656516.png)
 根据PID系统 

![image-20230907140310732](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140310732.png)

![image-20230907135740437](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135740437.png)

![image-20230907135728112](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135728112.png)

### Arduino

#### 主代码

```c
//所有程序都写在下面两个函数里

/*开机的时候运行一次，各种设定放在setup（）里*/
Void setup（）
{
	Serial.begin（9600）；//设置波特率
}
/*不断循环*/
Void loop()
{
	Serial.println("Hello world!");
	delay(1000);//延迟1s
}


```



#### LED灯闪烁

```c++
#define led 13
Void setup（）
{
	pinMode(led,OUTPUT); //设定led管脚为输出引脚
}
Void loop()
{
	digitalWrite（led,HIGH); //设置led为高电平，点亮led
	delay(1000);//延迟1s
    digitalWrite（led,LOW); //设置led为低电平，熄灭led
	delay(1000);//延迟1s
}
```



### Question

Q1：如何让LED不闪烁，但亮度只有正常的20%?



原理：人眨眼的频率有限，当闪烁频率低时，会认为没有闪烁

```C
#define led 13
Void setup（）
{
	pinMode(led,OUTPUT); //设定led管脚为输出引脚
}
Void loop()
{
	digitalWrite（led,HIGH); //设置led为高电平，点亮led
	delay(2);//延迟1s
    digitalWrite（led,LOW); //设置led为低电平，熄灭led
	delay(8);//延迟1s
}
```

Q2:原理的推广

- 输出电压调节（利用电容滤波）

​		PWM波					

- 电流电机控制
- 信号传输（舵机控制）

#### 相关知识

- delay()/delayMicroseconds()：用于延时，第一个单位为毫秒，第二个为微秒。  

- analogWrite():模拟 I/O 口输出，一般用于 PWM 输出，如：

  analogWrite(13,127)，为在13 号引脚处输出一个占空比为 50%的 PWM 方波，后一参数 0 表示关， 255 表示全开  

```C++
void setup()
{
    pinMode(13,OUTPUT);//设定13号端口为输出
}

void loop()
{
    digitalWrite(13,HIGH);
    delayMicroseconds(100);//大约10%占空比的1KHZ方波
    digitalWrite(13,LOW);
    delayMicroseconds(900);
}
```



## 三、传感器

### 定义

用于**定量**感知环境**特定物质属性**的**电子、机械、化学设备**，并能够把各种物理量和化学量等**精确**地变换为**电信号**，再经由电子电路或计算机进行分析与处理，从而对这些量进行检测  

### 静态特性

指检测系统的输入为**不随时间变化**的恒定信号时，系统的输出与输入之间的关系

- 灵敏度（**越高越好**）
- 信噪比（S/N）：传感器输出信号中信号分量与噪声分量的平方平均值之比
- 线性：输入输出为线性

精度

- 稳定性：输入量恒定，输出量向一个方向偏移（温漂、零漂）
- 精度
  - 准确度：测量值对真值的偏移程度
  - 精密度：测量相同对象，每次得到不同值


### 动态特性

![image-20240416111624968](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111624968.png)

### 选择

**尺寸、重量、价格、功耗敏感**

![image-20240416111656391](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111656391.png)

### 常见传感器

![image-20230907140033593](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140033593.png) 

#### 电位器

![image-20240416111731145](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416111731145.png)

类别

旋转式:测量角位移

直线式:测量线位移



#### 编码器

根据测量介质分：光电码盘、磁编码器

根据测量结果分

- 增量式
- 绝对式

![image-20240416112056238](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112056238.png)

绝对式光电码盘

上电时候可以检测到位置、

![image-20240416112342658](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112342658.png)



**检测正反转 - 使用两个错位的码道**

![image-20240416112311474](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112311474.png)

**检测速度**

![image-20240416112459436](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112459436.png)

![image-20240416112618436](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416112618436.png)

计量周期法和计量频率法

![image-20230907140242381](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140242381.png)

#### 方向角传感器

指南针：霍尔效应

易受环境影响



**陀螺仪**：

机械（角动量大转轴不动）

光纤：光速不变、光干涉

MEMS（科里奥利力）：体积小、重量轻、成本低；航向角不准



#### 距离传感器

- 红外光接近觉传感器
- 回波式接近觉传感器



??? note "题目"
	分析超声波/激光传感器的原理及其各自的优缺点

**超声波**

**原理：**

![image-20240416113219037](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416113219037.png)

发出声波，检测发出与回波之间的时间差
$$
Length = \frac{v\times T_{total}}{2}
$$

**问题：**

- 声波速度慢，时间比较好测量，但是降低了感知速率
- 声波束按照锥形传播，分辨率较差，无法分辨尺寸偏大or偏小；无法分辨角度、方向
- 光滑反射、吸收

![image-20240416113455608](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416113455608.png)





**激光雷达**

光是不会像声波发散

精确检测方位角，检测物体宽度

 方法：三角法，时飞法，相位偏移测量法

![image-20240416115157833](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416115157833.png)

![image-20240416115210183](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416115210183.png)

#### 力觉传感器

压阻式、压电式、电容式



## 四、驱动

电机驱动：将电能转换为旋转或直线运动动能，最常见最普遍，控制简单稳定性好，输出精准，但是力矩小，需要配合减速器使用。

液压驱动：以液压油为传动介质，液压缸作为驱动器，单位重量传输功率大，可以产生很大输出力，响应迅速，但是系统复杂、成本高，体积重量大，输出精度较低。

气压驱动：以压缩空气作为动力源，动作迅速，反应快，结构简单，但是受负载影响大，不适宜精密位置和速度的控制，输出力小。
其他驱动：压电陶瓷驱动，形状记忆合金驱动（软体机器人）等

### 电机 motor 

> 输出力矩和速度，如小车的直线运动和转弯
>
> 需要驱动芯片以及控制方式

- 优点：控制调节简单、稳定性较好
- 缺点：力矩小、刚度低，常常需要配合减速器使用

 $P = \frac{v}{i} \times Ti$​

注意：**力矩 X 转速 = 功率**

#### [有刷电机与无刷电机](https://www.bilibili.com/video/BV1ig411S7gX/?spm_id_from=333.337.search-card.all.click&vd_source=c22bb8d123dbc6430c3057dc8d2701b4)

![image-20240416164453791](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416164453791.png)

![image-20240416164945042](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416164945042.png)

定子不动，改变转子的磁极，就可以完成换向。

中间部分由惯性。

![image-20240416165039391](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416165039391.png)

使用三、五线圈的奇数线圈，就不存在“平衡位置”了。

使用2N1S顺，2S1N逆

![image-20240416165250656](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416165250656.png)

限制：电刷；电刷与换向片接触产生动力损耗。



![image-20240416165453808](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416165453808.png)

永磁铁作为转子，电磁铁作为定子。

如何判断何时改变电流输入：一般在电机的不同位置上装三个霍尔传感器，就可测出转子的位置，使用霍尔原件感应转子的状态和位置。

![image-20240416104119842](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104119842.png)

!!! note "转动顺序、导通方式"
    **AB，AC，BC，BA，CA，CB**<br>
    后三个是前三个反序

![image-20240416104143466](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104143466.png)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-dd52b5ed852d7e746c35aad78f4e3851_r.jpg)

换向的过程

![image-20240416164651385](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416164651385.png)



三相9绕组6极（3对极）

转子的NS极与绕组电流产生的NS极有对其的运动趋势，这个惯性使得其能够旋转

注意：每一相是**串联**的

![image-20240416164727698](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416164727698.png)

采用**9绕组6极**，而不是**6绕组6极**原因：为了防止定子的齿与转子的磁钢相吸而对齐，产生类似步进电机的效果，此情况下转矩会产生很大波动





总体来说且转数提升容易基本只受限于轴承。

缺点是启动功率输出和荷重输出（工作突然加重工作/爬坡能力）类比有刷电机少将近百分之20，控制器贵稳定性成熟度（工业性价比）不如有刷



#### 调速

滤波


 [H桥的基本原理-刹车-正反转-调速](https://www.bilibili.com/video/BV1ZG4y1v7LS/?spm_id_from=333.1007.top_right_bar_window_history.content.click) ![image-20230907140632003](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140632003.png)



#### 电机控制

> 一个电机由静止到额定转速是怎么实现的

等效电路

![image-20240416171746564](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416171746564.png)

电枢电动势Ea，电磁转矩T，电磁功率P

Ke速度常数，Km力矩常数

I 电枢电流，w角速度
$$
\begin{align}
E_a &= K_e \cdot n\\
T &= K_m \cdot I\\
P &= E_a \cdot I = T \cdot \bar{\omega}\\\\

U &= E_a + I \cdot R_a = K_e \cdot n + I \cdot R_a\\
n &= \frac{U-I\cdot R_a}{K_e}
\end{align}
$$

$$
P = T\cdot W
$$


**力矩与电流大小成正比**

**转速与感应电动势大小成正比**
$$
\begin{align}
电压平衡方程：& u_a(t) = R_ai_a(t) + L_a\frac{di_a(t)}{dt} + E_a(t)\\
感应电动势方程：&E_a(t) = K_e \omega\\
电磁转矩方程：&T(t) = K_t i_a(t)\\
转矩平衡方程：&T(t) = J\frac{d\omega(t)}{dt}+ B\omega(t) + T_d(t) 
\end{align}
$$
$J$表示电机的转动惯量，$\omega(t)$表示电机的角速度，$B$表示电机的阻尼系数，$T_d(t)$表示电机所受的负载转矩。





![image-20240416174456906](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416174456906.png)

电机烧掉：**电机铜线外绝缘体破坏，电线与电线之间短路**



检查方法：测量电机绕组的电阻值是否正常进行判断

![image-20240416173535098](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416173535098.png)

白色区域需要注意



> 如何控制小车右转
>
> 如何控制小车原地右转
>
> 如何控制小车以半径1m右转

##### **有刷电机（H桥驱动）**

最常用的驱动方式

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/61EC0040D67F475F87D07883A700D778_735.jpeg)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/99F657663FFE42398711F883963F8542_566.jpeg)

上图为电机的正反转

![image-20240414193034701](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414193034701.png)

为了避免电机的反电动势的危害，仍然需要在三极管两端接二极管，因为电机线圈在电路开闭瞬间产生的反向电动势会高过电源，对晶体管和电路会造成影响，甚至是烧毁元件。

一般用**L298芯片**来控制电机转动，可以驱动两个直流电机



##### 光电隔离电路

![image-20240414193622133](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414193622133.png)

可以实现抗干扰



##### 基本控制方式

###### 开环伺服系统

精度较低， 但稳定性最好。

![image-20240414193757089](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414193757089.png)

###### 闭环伺服系统

精度较高，但系统的结构较复杂、成本高，还有系统稳定性的问题

![image-20240414193902662](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414193902662.png)

###### 半闭环伺服系统

反馈电机信息，控制电机

精度比闭环要差一些，稳定性比闭环好，但比开环要差一些

![image-20240414193936717](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414193936717.png)

#### 转动惯量匹配

负载的转动惯量折合到主动轴上时候，从动轴上的转动惯量和阻尼系数都要除以传动比的平方，负载转矩处于传动比


$$
J_L=J_1+\frac{J_2+J_3}{i_1^2 }+\frac{J_4}{i_1^2 i_2^2 }
$$
对于直流电机而言，高动态的伺服系统，一般要求：
$$
J_M < (2-3)J_L \\
电机的转动惯量 J_M、负载的等效转动惯量J_L
$$



![image-20240416174549458](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416174549458.png)

![image-20240416104333256](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104333256.png)

![image-20240416232800538](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416232800538.png)

设一直接高电平时，转速最大是$V_{max}$，占空比为$D= \frac{t_1}{T}$

电机平均速度为
$$
V_d = V_{max}\cdot D
$$

$V_d$:电机的平均速度

$V_{max}$

$D=\frac{t_1}{T}$:占空比

#### 舵机

> 控制角度，位置伺服，如机械手；
>
> 用PWM波控制

控制线：电源线、地线、控制线

![image-20230907143850328](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907143850328.png)

电机 + 减速器

**标准舵机有三条控制线，分别为**电源线、地线和控制线。控制线连接到控制芯片上

![image-20240422172314384](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422172314384.png)

直流电机PWM匹配

占空比

![image-20230907135711661](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135711661.png) ![image-20230907140616101](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140616101.png)![image-20230907140621883](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140621883.png)

### 气动

- 气压驱动以空气压缩为动力源，也是机器人驱动的一种重要形式。
- 气动式主要有气缸、气阀、管路等元件组成。
- 优点：气源获得方便、成本低、动作快。
- 缺点：输出功率小，体积大。一般而言，其工作噪声较大、控制精度较差。



#### 分类

包括气压发生装置、辅助元件、控制元件和执行元件

![image-20240416104446817](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104446817.png)

- 气压元件：气源装置，其功能是将原动机**输入的机械能转换成流体的压力能**，为系统**提供动力**
- 执行元件：**气缸、气马达**，功能是将流体的压力能转换成机械能，输出力和速度或转矩和转速），以带动负载进行直线运动或旋转运动
- 控制元件：**压力、流量和方向控制阀**，作用是控制和调节系统中流体的压力、流量和流动方向，以保证执行元件达到所要求的输出力（或力矩）、运动速度和运动方向
- 辅助元件：保证系统正常工作所需要的辅助装置， 包括**管道、管接头、储气罐、过滤器和压力计**

#### 气体的特性

- 系统的压力应小于**8**个大气压（即0.8MPa）
- **不可压缩流体**
- **1**大气压=0.1013MPa=15psi(磅/平方英寸)



#### **方向控制回路**

##### 单作用气缸换向回路

**几位几通（考！）**

[电磁阀工作原理_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1x8411c7hh/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[二位五通双电控电磁阀的工作原理](https://www.bilibili.com/video/BV1fz421r7yX/?spm_id_from=333.337.search-card.all.click&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

几位：看有几种回路可以切换（有几个小格子）

几通：看**每一个回路**（小格子）里面有几个连接处

![image-20240414195847393](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414195847393.png)

![image-20240422161542854](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422161542854.png)

![image-20240422161556062](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422161556062.png)

![image-20240422161610644](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422161610644.png)

对于a图

在第二位时，P2P3相通，P3出气，右边气缸由于弹簧被压缩，向下运动

在第一位时，P3堵住，P2P1相通，进气导致向上运动

对于b图

在第三位时（蓝色），向上

在第二位时（粉色），不动

在第一位时（黄色），向下



注：**有几位就有几种状态!**

对于每一种状态，将接线平移到对应的格子上，观察进气口气体的流向，从而判断如何进行换向



##### 双作用气缸换向回路 



![image-20240414200332022](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414200332022.png)

例：

![image-20240414201155714](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240414201155714.png)

不拍按钮时：左移

拍按钮时：右下角的被改变，因此右移





### 液压

- **将液体压力转化为机械能**
- 利用**不可压缩的流体**，将作用于某一点的力传递到另一点，这种流体通常是**工业液压油** 
- 由液压源、伺服阀、传感器、执行机构等构成
  - 优点： 重量轻、尺寸小、动作平稳、快速性好、产生的力 力矩非常大 。
  - 缺点： 易漏油、维护困难；不确定性和非线性因素多，控制和校正不如电气式方便

![image-20240422162943114](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422162943114.png)



## 五、传动

### 参数

#### 传动机构的性能要求

- 质量和转动惯量应尽量小。
- 刚度尽量大：伺服系统动力损失小（变形损失能量小）；
- 频率要高，超出机构的频带宽度，使之不易产生共振；
- 闭环系统更加稳定。
- 阻尼越大，振动的振幅就越小，衰减也越快。但大阻尼会使系统稳态误差增大、精度降低。



#### 强度与刚度  

- 强度：零件在工作中发生**断裂或残余变形**均属于强度不足。
- 刚度：零件在工作中所产生的**弹性变形**不超过允许的限度。包括整体刚度和表面刚度两种。
- 相同的强度，结构不同，刚度不同


#### 减速比

（传动比：输入速度与输出速度之比

减速比，也即传动比。指减速机构输入速度与输出速度之比，用“i”表示。即，*i* =输入速度/输出速度，并使输出力/力矩变为原来的i倍。

$$
i = \frac{输入速度}{输出速度} = \frac{输入力矩}{输出力矩}
$$

例：电机输入减速箱的速度1000n/min，输出速度10n/min，则减速比 i =1000/10=100

如电机输出力矩为Tin=0.1Nm，则输出力矩为Tout=Tin*i=0.1Nm*100=10Nm

传动比是指机械传动系统中，始端主动轮与末端从动轮的角速度或转速的比值。传动比可以描述输入轴和输出轴之间的速度关系，包括齿轮传动、链条传动等多种传动方式。传动比的计算公式为：传动比 = 主动轮转速 / 从动轮转速。

减速比则是传动比的一种特殊形式，专指减速装置的传动比。减速比是指减速机构中瞬时输入速度与输出速度的比值。减速比的目的是降低转速并增加扭矩，通常用于将高速低扭矩的驱动装置（如电动机）的速度降低，并提供高扭矩输出。减速比的计算公式为：减速比 = 输入转速 / 输出转速。



#### 转动惯量

尽可能小，防止谐振

#### 阻尼





支撑、导向系统：轴承和导轨

### 齿轮传动

齿轮传动是指由齿轮副传递运动和动力的装置，它是现代各种设备中应用最广泛的一种机械传动方式。

**优点**：传动比较准确，效率高，结构紧凑，工作可靠，寿命长。

![image-20230907144343497](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907144343497.png)

#### 基本参数的计算公式

$$
p_i = s_i + e_i a_i = e_i\\
模数m = \frac{m_i}{\pi}\\
国标压力角的标准值为20°\\
分度圆直径 d =mz (欲使两齿轮正确啮合，两轮的模数必须相等
)\\
定常传动比i_12 = \frac{\omega_1}{\omega_2} = \frac{O_2P}{O_1P} (P为节点)
$$

齿数要尽量大于17

https://max.book118.com/html/2020/0123/8140121006002074.shtm



#### 定轴传动

定轴轮系：所有转动轴可以是平行的或者交错的；每个轴上可以有多个齿轮。

![image-20240416104731762](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104731762.png)

#### 周转轮系

周转轮系：**至少有一个齿轮的轴线不固定** ，而是绕另一个齿轮的轴线转动的轮系。

![image-20240416104742305](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104742305.png)



![image-20240416104846198](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104846198.png)

![image-20240416215257877](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416215257877.png)

#### 减速比计算（重点）

![image-20240416215432743](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416215432743.png)

$$
i_{首末} = \frac{\omega_{首}}{\omega_{末}} = \frac{Z_末}{Z_首} \quad 包含正负 \\
本题答案 \\
i_{12} = \frac{\omega_1}{\omega_2} = -\frac{Z_2}{Z_1} \\
i_{23} = \frac{\omega_2}{\omega_3} = \frac{Z_3}{Z_2} \\
i_{33'} = \frac{\omega_3}{\omega_3'} = \frac{Z_3'}{Z_3} = 1 \\
i_{3'4} = \frac{\omega_3'}{\omega_4} = -\frac{Z_4}{Z_3'} \\
i_{44'} = \frac{\omega_4}{\omega_4'} = \frac{Z_4'}{Z_4} = 1\\
i_{4'5} = \frac{\omega_4'}{\omega_5} = -\frac{Z_5}{Z_4'} \\
综上：i_{15} = \frac{\omega_1}{\omega_5} = -\frac{Z_3}{Z_1}\frac{Z_4}{Z_3'}\frac{Z_5}{Z_4'} \\
$$


#### 方向关系

![image-20240422185707338](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422185707338.png)

![image-20240422192109099](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422192109099.png)

### 连杆传动

![image-20240416104926218](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416104926218.png)

AB当做输入，CD当做输出，则BC就是一个连杆

#### 优缺点（重点）

优点：

- 连杆机构中的运动副一般均为低副（连杆机构也称低副机构）低副元素之间为面接触，压强较小，承载能力较大；
- 可改变各构件的 长度使得从动件得到不同的运动规律；
- **可以设计出各种曲线轨迹**。

缺点：

- 需要经过中间构件传递运动，传递路线较长，易产生较大的误差，同时，**使得机械效率降低**
- 质心在作变速运动，所产生的惯性力难于用一般平衡方法加以消除，易增加机构的动载荷， **不适宜高速运动（相对于齿轮而言）**

#### 分类

[5分钟搞懂四杆机构运动规律](https://zhuanlan.zhihu.com/p/541849290)

分类方法：看哪一根杆最短

**基本形式一：曲柄摇杆机构**

斜边最短的时候，是曲柄摇杆机构

![动图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-2b39fc71abcddb619afb965cb02acedc_b.webp)



**基本形式二：双曲柄机构**

最短杆为机架时候

![动图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-03d65aeed7c393ce21f4de19533c46f0_b.webp)

**基本形式三：双摇杆机构**

最短杆为连杆

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-2c969a21e62d70333d3c939c9586c189_b.webp)

证明方法：三角形两边之和大于第三边

![image-20240416105135035](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105135035.png)

曲柄滑块

![动图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-961dc510e2e17588e10de4e6fc78b2d8_b.webp)

对心曲柄滑块机构

![动图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-f4160d9cf92145412fd189df02a4dbd7_b.webp)

![image-20240416105229282](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416105229282.png)

曲柄摇杆机构的条件

- 曲柄摇杆机构：两个连架杆中有一个为曲柄，另一个为摇杆：最短杆为连架杆 1 时
- 双曲柄机构：两个连架杆均为曲柄：最短杆为机架 4 时
- 双摇杆机构：两个连架杆均为摇杆：最短杆为连杆 2 时

![image-20240416220706207](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240416220706207.png)

#### 矢量方程法(不重要)

##### 步骤

![image-20240417032040907](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032040907.png)

- 总的来说就是列写矢量方程
- 再按照实部和虚部相等列写两个方程求解
- 速度与加速度对位移方程求导即可

##### 曲柄滑块机构

位移分析

![image-20240417032129498](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032129498.png)

速度分析（位移求导）

![image-20240417032205341](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032205341.png)

加速度分析

![image-20240417032228970](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032228970.png)

##### 曲柄摇杆机构

位置分析

![image-20240417032407332](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032407332.png)

![image-20240417032513797](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032513797.png)

![image-20240417032540629](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032540629.png)

速度分析

![image-20240417032607292](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240417032607292.png)

### 滑轮组

- 固定轮只能用于改变力的方向，而运动轮可以降低输入力量的大小
- 通过动滑轮，可以实现两倍的运动距离，但是需要的力矩需要增加一倍。

### 带传动

结构简单、传动平稳、造价低廉以及缓冲吸振

#### 链传动

是依靠链齿轮齿与链节的啮合来传递运动和动力，但在运转时**不能保证瞬时传动比**

#### 同步带

- 综合了带传动和链传动的优点
- 避免采用润滑油对橡胶材料的皮带进行润滑，易造成橡胶的膨胀，导致其网裂和硬化。

### 涡轮-蜗杆传动

- 传动比大，结构紧凑
- 传动平稳，噪声小。
- 具有自锁性。

![动图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/d081b02f504c3556ffff9d5a7d91d409_b.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/a942d11ag00qeurw800kpd000b4007wp.gif)

### 凸轮机构

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/q3fgrs7uda.gif)

## 六、支撑与导向

### 轴承

作用：用来支撑轴，使轴系有确定的位置

![image-20240422195340577](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422195340577.png)





![image-20240422195359029](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422195359029.png)

![image-20240422195541021](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422195541021.png)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/skzr7cxa9j.gif)

![image-20240422201036218](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422201036218.png)

![image-20240422201142655](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422201142655.png)

![image-20240422201356861](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422201356861.png)

### 联接

![image-20240422201534848](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422201534848.png)