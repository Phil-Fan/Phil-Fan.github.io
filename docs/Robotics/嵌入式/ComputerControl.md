# 计算机控制系统


!!! note "课程信息"
    - 授课教师：
    - 上课时间：2025春夏
    - 学分：3.5pt
    - 成绩组成:<br>平时成绩占20%——出勤、课堂测试/互动/交流、作业<br>
        实践成绩占35%——综合实践大作业，小组情况、个人完成情况各占50%计算<br>
        期末考试占45%——半开卷，1张A4纸，手写，复印无效<br>
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250220082031246.png)
    

<iframe src="http://www.cse.zju.edu.cn/aec/2012/0308/c73095a2676372/page.htm" width="100%" height="600px" frameborder="0"></iframe>

## A4

[云高天遥 - A4原型](https://www.cc98.org/topic/5645283)

[Healor - A4](https://www.cc98.org/topic/5925911)

[Rainbow0 - A4](https://www.cc98.org/topic/5658322)

## 历年卷
[计算机控制系统设计与实践 2023-2024春夏 回忆卷 - CC98论坛](https://www.cc98.org/topic/5925877)

[计算机控制系统设计与实践（计控）22-23春夏回忆卷 - CC98论坛](https://www.cc98.org/topic/5644108)

[计算机控制系统设计与实践（计控）21-22春夏回忆卷 - CC98论坛](https://www.cc98.org/topic/5353159)



## 实验课

硬件、软件、编程、综合实践


## 第一章

!!! note "常见英文术语对照"
    - DDZ 电动单元组合元件
    - PLC
    - D/A，A/D
    - IO
    - DDC 直接数字量控制
    - DCS 集散控制
    - FCS 现场总线控制系统
    - CSMA/CD

### 自动控制（反馈控制）的基本逻辑

1. **控制的基本形式**：开环、闭环；  
   **基本要求**：稳、准、快、优

2. **四个（类）基本环节**：  
   - 被控对象、检测仪表、控制器、执行器
   - **对象**：工业过程、运动对象、社会科学问题  
   - **目标**：过程性＋结果性

3. **反馈的两种形式**：正反馈和负反馈

### 计算机控制系统组成

1. **计算机控制系统的工作过程**：  
   周期性，采样 + 分析决策 + 输出执行

2. **计算机控制系统的基本组成**：  
   软件（系统软件、支持软件、应用软件） + 硬件（可靠性、IO）

### 计算机控制的简要发展过程

1. **模拟调节器**：模拟电路调节

2. **计算机控制系统的几个典型发展阶段**：  
   DDC — 集中型 — DCS — FCS


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250227084020236.png)

### 网络通信技术简介

1. **若干基本概念**:模拟/数字；并行/串行；单工/半双工/全双工；

2. **串行总线**：RS-232、-422、-485

3. **现场总线**

4. **工业以太网**


##

DDZ-II型：分立元件电源220VAC信号0～10mA 
DDZ-III型：集成电路电源24VDC信号4～20mA、1～5VDC

二线制(DDZ-III)比四线制(DDZ-II)更安全防爆
四线制可以抵消引线电阻

需要注意电阻信号的接线方式和变送器信号制的区别