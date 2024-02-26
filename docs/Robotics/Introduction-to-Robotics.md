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



1、冯诺依曼结构的硬件结构
 2、巡线小车的框图和程序设计（据我观察已经考了三四年了这题……不做评价）
 3、传感器的定义，根据智能家居机器人写四种传感器or分析超声波/激光传感器的原理及其各自的优缺点
 4、五种旋转变直线的机构
 5、写出3绕组2极无刷直流电机（就课上讲的模型）的联结方式和导通状态图







## CPU

总线 bus

GPIO ： general purpose io

二进制减法： 用[补码](https://zhuanlan.zhihu.com/p/99082236)

二进制乘法： 移位相加 倍增





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



## 传感器 

### 静态特性

- 灵敏度
- 信噪比（S/N）：传感器输出信号中信号分量与噪声分量的平方平均值之比
- 线性：输入输出为线性
- 稳定性
- 准确度：测量值对真值的偏移程度
- 精密度：测量相同对象，每次得到不同值

![image-20230907140033593](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140033593.png) 



方向角传感器

指南针：霍尔效应

陀螺仪：机械（角动量大转轴不动）、光纤、MEMS（科里奥利力）

距离传感器：光、激光、超声波
力觉传感器



 ![image-20230907140242381](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140242381.png)

 ## 电机 motor 

 \- 速度高、力矩小
 减速器
 $P = \frac{v}{i} \times Ti$

### 分类

- 电机驱动
- 气动
- 液压驱动

![image-20230907140256665](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140256665.png)

直流电机

输出力矩、速度

[有刷电机与无刷电机](https://www.bilibili.com/video/BV1ig411S7gX/?spm_id_from=333.337.search-card.all.click&vd_source=c22bb8d123dbc6430c3057dc8d2701b4)

舵机
控制角度

转动惯量的匹配
直流电机PWM匹配

占空比

![image-20230907135711661](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907135711661.png) ![image-20230907140616101](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140616101.png)![image-20230907140621883](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140621883.png)滤波


 [H桥的基本原理-刹车-正反转-调速](https://www.bilibili.com/video/BV1ZG4y1v7LS/?spm_id_from=333.1007.top_right_bar_window_history.content.click) ![image-20230907140632003](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907140632003.png)

### 舵机

控制线：电源线、地线、控制线

![image-20230907143850328](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907143850328.png)

电机 + 减速器



## 机器人结构

执行结构：完成操作任务

传动机构：伺服系统 如齿轮

​	转动惯量尽可能小，防止谐振

​	刚度

​	阻尼

- 减速比（传动比：输入速度与输出速度之比

自由度DOF：

​	手臂：7自由度



支撑、导向系统：轴承和导轨

齿轮传动

渐开线

![image-20230907144343497](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20230907144343497.png)

连杆传动

曲柄机构

双曲柄机构



## 机器人运动学

正运动学

逆运动学：已知位姿求解角度

滚动 `roll`

俯仰 `pitch`

偏摆 `yaw`
