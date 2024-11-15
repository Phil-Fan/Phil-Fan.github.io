# 嵌入式小玩具
[平衡小车的控制算法（PID,LQR,MPC)及arduino程序导航贴\_平衡车mpc-CSDN博客](https://blog.csdn.net/qqliuzhitong/article/details/124355565)

[平衡小车动力学建模\_两轮平衡小车建模-CSDN博客](https://blog.csdn.net/qq_23096319/article/details/129704288)



## 动量轮平衡车


[平衡自行车+独轮车 - 立创开源硬件平台](https://oshwhub.com/hvan/canmotordrive_copy)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241112120107.png)

[STM32动量轮平衡自行车 - 立创开源硬件平台](https://oshwhub.com/bonus/stm32_bike)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241112120157.png)

[做了个独轮的自平衡车，很稳！支持循迹！开源了 - 知乎](https://zhuanlan.zhihu.com/p/685827105)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241112120222.png)

## PID平衡车

[迷你掌上平衡车miniBot - 立创开源硬件平台](https://oshwhub.com/leannn/minibot)



[B站全套教程](https://www.bilibili.com/video/BV1Va411Z7G4)<br>

[嘉立创PCB](https://www.jlc.com/)<br>

### 组装

#### 焊接

sbus

![image-20240410224052064](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410224052064.png)

#### 连线

![image-20240410224422169](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410224422169.png)

电机驱动不要装反

![image-20240410112212309](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410112212309.png)

编码器电源的两根线不要连反，连反会烧掉

![image-20240410111731510](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410111731510.png)

MOS输出不可以接入感性负载：如电机、电磁铁

#### 框架

底板使用M3螺丝

### 代码

`freetros`框架

![image-20240410112718916](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410112718916.png)

![image-20240410113354807](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410113354807.png)

`control.c`进行PID调参



Set_PWM

![image-20240410113703874](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410113703874.png)



电机死区







### 平衡算法

- PID

- 前馈PID
- 模糊PID

- LQR


## RC小车

### 
[Optimization‐based autonomous racing of 1:43 scale RC cars - Liniger - 2015 - Optimal Control Applications and Methods - Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/oca.2123)

[ミニッツRWD MR-04 レディセット シボレー コルベット C8.R ガンメタル / レッド 32356GMR - KYOSHO RC](https://rc.kyosho.com/en/rccar/miniz/mini-zrwd/32356gmr.html)

[MPC and MHE implementation in Matlab using Casadi - Workshop\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1LE411j75o/?spm_id_from=333.337.search-card.all.click&vd_source=e720e65e2dd33b661142321b2d818921)


[[MPCC in FSAC]基于MPCC的无人系统控制设计思路-CSDN博客](https://blog.csdn.net/vonct/article/details/134781569)


https://github.com/MMehrez/MPC-and-MHE-implementation-in-MATLAB-using-Casadi


[硬核 WiFi/4G/5G 网络遥控车制作教程 | 树莓派实验室](https://shumeipai.nxez.com/2021/01/28/wifi-4g-5g-network-remote-control-car-making-tutorial.html)

[RCFans论坛 【自建赛道】 完成 【制作全过程分享】 - Powered by Discuz!](https://www.rcfans.com/thread-807710-1-1.html)

[开源！手把手教你搭建阿克曼自动驾驶小车（上） - 知乎](https://zhuanlan.zhihu.com/p/499251426)





## 四足

[stanfordroboticsclub/StanfordQuadruped](https://github.com/stanfordroboticsclub/StanfordQuadruped/tree/master)



## 赛博魔杖

[赛博魔杖\_STM32卷积神经网络 - 立创开源硬件平台](https://oshwhub.com/lyg0927/cyberwand-stm32-convolutional-ne)

## 桌面机器人
[【全开源】ATom-Bot 桌面机器人 - 立创开源硬件平台](https://oshwhub.com/rbbbb/ATom-Bot)

## 轮腿机器人

[LeTian-robot2（轮腿机器人） - 立创开源硬件平台](https://oshwhub.com/z.sir/letian-robot2)


平衡轮腿式步兵车

[RoboMaster平衡步兵机器人](https://zhuanlan.zhihu.com/p/563048952)

[腾讯轮腿式机器人Ollie](https://www.zhihu.com/question/462906299)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-e729a367adb27910f79f9b112b4b6bfd_1440w.webp)
