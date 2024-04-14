# 嵌入式小玩具

## 平衡车

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



改进

平衡轮腿式步兵车

[RoboMaster平衡步兵机器人](https://zhuanlan.zhihu.com/p/563048952)

[腾讯轮腿式机器人Ollie](https://www.zhihu.com/question/462906299)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-e729a367adb27910f79f9b112b4b6bfd_1440w.webp)