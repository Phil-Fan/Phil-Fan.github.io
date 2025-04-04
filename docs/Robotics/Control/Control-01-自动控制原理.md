# 自动控制原理

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241025103426.png)

???+note "课程信息"
    === "回忆卷"
      [自动控制原理（甲）2023-2024 春夏回忆卷 自控](https://www.cc98.org/topic/5926127)<br>
      [自动控制理论（甲）2023-2024春夏学期回忆卷 自控 自控原理](https://www.cc98.org/topic/5926477)<br>
      [2023-2024 海洋学院 自动控制原理期末回忆卷（海院 自控）](https://www.cc98.org/topic/5801048)<br>
      [23-24学年秋冬航院自动控制原理 回忆](https://www.cc98.org/topic/5797599)<br>
      [23-自控-海洋-期中-回忆卷(自动控制原理&海院）](https://www.cc98.org/topic/5750932)<br>
      [控院自动控制原理（甲）/自控回忆卷 2022-2023春夏](https://www.cc98.org/topic/5644437/1#1)<br>
      [2020-2021自动控制原理（甲）回忆卷）（控院+电院）](https://www.cc98.org/topic/5116198/1#1)<br>
       
    === "资源"
      [自动化专业课A4分享——自动控制原理](https://www.cc98.org/topic/5639945)<br>
      [梁毅浩学长资源整理](https://www.cc98.org/topic/5116220)<br>
      [Healor学长整理](https://www.cc98.org/topic/5805674)<br>
      [the_Piao A4分享](https://www.cc98.org/topic/5926182)
    
    === "考核方式"
      随机掉落小测,期末7道大题


考后码点字攒攒rp

## 课程简介与体验

课堂体验：★★★☆☆

作业量：★★★☆☆

硬核程度：★★★★☆

自控是自动化专业的专业核心课程，也是大二春夏比较重要的一门课。

### 自控讲了什么
!!! note "以下内容均为笔者个人理解，如有错误，先滑跪"
      可以结合思维导图进行框架建立和理解
      纯为了搭一个大致的框架，肯定会有很多表述不太严谨的地方

自动控制原理从自动控制系统的基本概念和组成讲起。


**第一部分讲了控制系统的数学建模方法**（微分方程、传递函数、状态空间模型），以及几种方法的转换关系和常见图像（方块图、状态变量图、信号流图、仿真图）。课堂上在建模部分也会讲到建模的示例，比如电路、机械系统、传热系统等等。

**第二部分是对控制系统的性能进行分析**

首先定义了一些分析的指标：主要讲解的是一阶二阶系统的动态性能指标（可以形象理解为如何确定一些参数去描述一个响应的图像），例如多久会到达稳定值，多久会到达第一个峰值，两个峰值之间的比例，峰值高度有多“高”等等。

然后从稳准快（稳定性——能不能收敛；准确性——能不能达到给定要求；快速性：这个貌似没有太讲）三个方面对建立的数学模型进行分析。

使用的数学工具是微分方程求解（暂态稳态）、Laplace变换（对应传递函数）、状态方程（对应状态空间模型）

这部分会先后接触到几种分析稳定性的工具：劳斯判据（时域）、根轨迹（复频域）、Bode图（频域）、Nyquist图（频域）。由于$1+GH = 0$闭环极点有时候比较难求，所以这几种方法多是研究开环函数与稳定性的关系。

**第三部分是对建立的系统进行修正和更改，使之更符合设计的要求。**

这部分主要讲的内容有补偿器的设计和PID的相关内容。补偿器期末其实没有考察到，课堂学习也散落在几个章节当中。

这个部分个人感觉[Compensator - YouTube](https://www.youtube.com/watch?v=NMpmb0ihoFo&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk&index=34)中的讲述顺序比较合理：补偿器分为超前和滞后补偿器，而两种补偿器都可以使用极点图（复频域）和波特图（频域）两种方法进行设计。

PID部分也可以参照[PID - Youtube](https://www.youtube.com/watch?v=UR0hOmjaHp0&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk&index=28)

### 课程体验
~~一直不是很清楚为什么用中文讲英文课件，不是很懂为了英特纳施奈尔而英特纳施奈尔、、、~~

比较推荐的学习资源是

* 赵豫红老师的[智云](https://classroom.zju.edu.cn/livingpage?course_id=51670&sub_id=886268&tenant_code=112)和PPT（已附在课程资料里）
* 油管上大神的Control System Lectures:以10min左右一集的时长讲明白自控的大部分内容（不包括做题，在某些知识点上讲的没有学校深入）<br>[Why Learn Control Theory - YouTube](https://www.youtube.com/watch?v=oBc_BHxw78s&list=PLUMWjy5jgHK1NC52DXXrriwihVrYZKqjk&index=1)<br>B站搬运版本[Control System Lectures控制系统理论](https://www.bilibili.com/video/BV1jt411Z77J)
* 其他有意思的讲解，如：<br>[通过开车展示系统闭环极点在s域的左半平面、虚轴上以及右半平面](https://www.bilibili.com/video/BV1R8411P7YF/?spm_id_from=333.337.search-card.all.click)
* 在[这个帖子](https://www.cc98.org/topic/5835370)当中有8u还推荐了b站卢京潮老师的[【最新，考研专用速成版】自动控制原理 卢京潮 西北工业大学](https://www.bilibili.com/video/BV1vo4y147QZ)，但是我没有听过，不知道具体效果

### 复习顺序
留给我的复习时间其实不多了，考完勾实嵌入式之后只有一天多一点点的时间了。但好在之前没有落课，所以我的主要任务就是将忘记的内容回忆起来+建立一个整体的知识框架。

- 搭建知识框架（可能笔者比较倾向于先建立一个整体的框架再逐渐深入）。用到的是《自控课程纲要梳理》和之前自己总结的思维导图
- 抄写A4：这个部分可以直接使用98前辈总结的A4纸，自己查漏补缺一下；因为笔者之前一直在使用ipad做笔记，所以就自己整理了一版A4，~~这部分也耗了一天中的大部分时间~~。
- 复习作业题目：没有时间精细复习，就只能看一下
- 瞄一眼回忆卷都考哪些内容，心里有个底

### 考试感受
[自动控制理论（甲）2023-2024春夏学期回忆卷 自控 自控原理](https://www.cc98.org/topic/5926477)
老哥的回忆卷牛的

- 今年没有出波特图，很奇怪；劳斯判据倒是有好几问，可以重点掌握一下。
- 补偿器不考
- 题型应该和22-23类似，考前有一些没有掌握，比如根轨迹绘制m>n等；还是复习的时间有点短了，大家如果有空的话还是提前开始吧。
- 希望老师捞一下

### 资料分享
链接：https://pan.baidu.com/s/1W6qcDByeKaxhjGYZ1WughA?pwd=CC98 
提取码：CC98

资料大纲如下，包含了zyh老师的ppt，作业答案（~~请合理借鉴~~）,98上找到的历年题目，98上找到的整理资料（A4，课件整理）和我自己的A4

参考来源详见最开始
```
│  思维导图.xmind
│
├─01-赵豫红PPT
│      C1-第一章 概述及基本概念.pdf
│      C10-时域分析-2023.pdf
│      C11-高阶系统-2023.pdf
│      C12-状态方程解-2023.pdf
│      C13-稳定性与稳态误差-2023.pdf
│      C2-方块图与电路数学模型_2023.pdf
│      C3-方块图简化_2023.pdf
│      C5-信号流图-上课_2023.pdf
│      C6-模型间的转换-2023.pdf
│      C7-其他系统模型-2023.pdf
│      C8-非线性系统线性化与特殊环节建模-2023.pdf
│      C9-时域响应-2023.pdf
│      夏C1-根轨迹概述.pdf
│      夏C10-第六章稳定性判据-2023.pdf
│      夏C11-第六章稳定裕度-2023.pdf
│      夏C12-第六章补偿器设计-2023.pdf
│      夏C2-根轨迹绘制法则-2023.pdf
│      夏C3-广义根轨迹-2023.pdf
│      夏C4-根轨迹性能分析-2023.pdf
│      夏C5-补偿器设计-2023.pdf
│      夏C6-第六章概述.pdf
│      夏C7-第六章BODE图20230525.pdf
│      夏C8-第六章BODE图-2-20230530.pdf
│      夏C9-第六章极坐标图-2023.pdf
│
├─02-作业
│      夏学期第1周作业参考答案.pdf
│      夏学期第2周作业参考答案.pdf
│      夏学期第3周作业参考答案.pdf
│      夏学期第4周作业参考答案.pdf
│      夏学期第5周作业答案.pdf
│      夏学期第6周作业参考答案.pdf
│      夏学期第7周作业参考答案.pdf
│      春学期第1周作业参考答案.pdf
│      春学期第3周作业参考答案.pdf
│      春学期第4周作业参考答案.pdf
│      春学期第5周作业参考答案.pdf
│      春学期第6周作业参考答案.pdf
│      春学期第7周作业参考答案 .pdf
│      春学期第8周作业参考答案.pdf
│      自动控制原理学习辅导  知识精粹  习题详解  考研真题_14304221.pdf
│
├─03-历年卷
│      20-21春夏 控院.pdf
│      22-23春夏 控院.pdf
│      22-23期中 海洋.pdf
│      23-24春夏 控院.pdf
│      23-24春夏 海洋.pdf
│      23-24秋冬 航院.pdf
│
└─04-整理
        梁毅浩-cheating sheet列表.md
        梁毅浩-自控课程纲要梳理.pdf
        梁毅浩-课件摘要.pdf
        自控A4-Healor.pdf
        自控A4-PhilFan.pdf
        自控A4-the_Piao.pdf
        自控A4-林林home.pdf
        自控A4-梁毅浩.pdf
        自控A4-沐长风.pdf
```


## 控制系统建模

![连续系统](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E8%BF%9E%E7%BB%AD%E7%B3%BB%E7%BB%9F.svg)

### 实例


### 非线性系统

## 控制系统性能

![时域分析](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E6%97%B6%E5%9F%9F%E5%88%86%E6%9E%90.svg)
### 微分方程

### 传递函数
### Laplace变换

### 时域性能指标

二阶系统的特征多项式通常表示为：

$$
s^2 + 2\zeta\omega_ns + \omega_n^2
$$

其中：
- $s$ 是复数频率变量。
- $\zeta$ 是阻尼比。
- $\omega_n$ 是无阻尼系统的自然频率
  

**动态指标性能**

1. **上升时间（Rise Time）**: $T_r = \frac{\pi - \beta}{\omega_n \sqrt{1 - \zeta^2}}$
2. **峰值时间（Peak Time）**: $T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$  ，峰值时间的等高线是一条射线，且等峰值线是虚轴相同。
3. **超调量（Overshoot）**: $\sigma = e^{-\frac{\zeta \pi}{\sqrt{1 - \zeta^2}}}$  ，超调量只由阻尼比 $\zeta$ 决定。
4. **调节时间（Settling Time）**:  
  - 5%误差: $T_s \approx \frac{3}{\zeta \omega_n}$  
  - 2%误差: $T_s \approx \frac{4}{\zeta \omega_n}$
5. **衰减比（Damping Ratio）**: $n = \frac{\sigma}{B'} = e^{-\frac{2\zeta \pi}{\sqrt{1 - \zeta^2}}}$

![控制系统性能](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F%E6%80%A7%E8%83%BD.svg)

## 控制系统校正与设计
  f
