# dRehmFlight
[nickrehm/dRehmFlight: Teensy/Arduino flight controller and stabilization for small-scale VTOL vehicles](https://github.com/nickrehm/dRehmFlight)


[航模遥控器 | Crazepony开源四轴飞行器](http://www.crazepony.com/book/wiki/remote-controller-2-4.html)

!!! note "项目简介"
    ![](https://github.com/nickrehm/dRehmFlight/raw/master/dRehmFlight%20Logo.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241126113138.png)
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241126113215.png)
    dRehmFlight是由Nicholas Rehm开发的一款专为业余爱好者和非编程者设计的飞行控制器。它提供了直观易懂的代码结构，让你无需深入复杂的类库就能快速理解并进行定制化开发。此外，项目还包含了详细的VTOL飞行稳定概念介绍，无论是新手还是经验丰富的老手都能从中受益。

    dRehmFlight基于Arduino兼容的Teensy 4.0微控制器和MPU6050 6轴惯性测量单元，这使得它具备了出色的硬件扩展性和灵活性。Beta 1.3版本新增了Spektrum DSM卫星接收器支持、一次性IMU校准以及ESC校准功能，进一步提升了用户体验。

## Hardware

### 焊接

!!! tip "需要的材料"
    - Teensy 4.0 板子
    - MPU6050
    - 13pin 3针弯脚
    - 

焊接这里需要注意不要把

### 无线电连接


- 板子上自带的灯应该每秒快速闪烁一次
- 如果连接正常，应该是下面的情形

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250303111327780.png)

- 如果值没有变化，那么

## Software

### 在Arduino中配置Teensy环境
- 第一步是下载 [Teensy Loader app for Windows XP](https://www.pjrc.com/teensy/loader_xp.html)
- 第二步是下载[Teensyduino: Teensy support for Arduino IDE](https://www.pjrc.com/teensy/td_download.html)。在Arduino IDE中选择“文件”-“首选项”，在“其他开发板管理器地址”上加入
```title="每行一个即可"
https://www.pjrc.com/teensy/package_teensy_index.json
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250303094840219.png)

- 在开发板管理器中下载teensy
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250303094757685.png)



### 视频连接
[World's Fastest FLYING RC Drift Car - YouTube](https://www.youtube.com/watch?v=dcu0jODIlWU)

倒立摆
[Flying Inverted Pendulum - YouTube](https://www.youtube.com/watch?v=XmYRQi48s-8)

跟随算法

[Ground Effect Vehicle Autonomous Vision-Based Tracking - YouTube](https://www.youtube.com/watch?v=uaY2G5Kbj_g)

悬停
[abritten/dRehmFlight-StantonModel-VTOL: This is a replica of the Stanton RC VTOL model using the DrehmFlight FC. Replicated and modified by abritten (Drew Britten).](https://github.com/abritten/dRehmFlight-StantonModel-VTOL?tab=readme-ov-file)