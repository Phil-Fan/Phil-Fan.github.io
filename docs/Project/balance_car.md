# 平衡车

!!! note "项目简介"
    - 项目名称：
    - 一句话简介：
    - 目的：
    - 项目进程：
      - [ ] 
      - [ ] 
      - [ ] 
    - 相关知识记录
    - 项目技术栈
    - 项目难点
    - 项目成果



## 数学建模


[平衡小车的控制算法（PID,LQR,MPC)及arduino程序导航贴\_平衡车mpc-CSDN博客](https://blog.csdn.net/qqliuzhitong/article/details/124355565)

[平衡小车动力学建模\_两轮平衡小车建模-CSDN博客](https://blog.csdn.net/qq_23096319/article/details/129704288)


[迷你掌上平衡车miniBot - 立创开源硬件平台](https://oshwhub.com/leannn/minibot)



[B站全套教程](https://www.bilibili.com/video/BV1Va411Z7G4)<br>

[嘉立创PCB](https://www.jlc.com/)<br>


## 算法

- PID

- 前馈PID
- 模糊PID

- LQR


## 组装

### 焊接

sbus

![image-20240410224052064](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410224052064.png)

### 连线

![image-20240410224422169](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410224422169.png)

电机驱动不要装反

![image-20240410112212309](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410112212309.png)

编码器电源的两根线不要连反，连反会烧掉

![image-20240410111731510](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410111731510.png)

MOS输出不可以接入感性负载：如电机、电磁铁

### 框架

底板使用M3螺丝

## 代码

`freetros`框架

![image-20240410112718916](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410112718916.png)

![image-20240410113354807](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410113354807.png)

`control.c`进行PID调参



Set_PWM

![image-20240410113703874](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240410113703874.png)



电机死区












