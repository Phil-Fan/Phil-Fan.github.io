# 有趣的项目
## dRehmFlight
[nickrehm/dRehmFlight: Teensy/Arduino flight controller and stabilization for small-scale VTOL vehicles](https://github.com/nickrehm/dRehmFlight)

如果你是一位无人机爱好者，对飞行控制代码有浓厚的兴趣，或者正在寻找一个易于理解和修改的飞行控制器，那么dRehmFlight是你的理想选择。这个项目不仅是一个强大的VTOL（垂直起降）飞行控制器，更是一本生动的飞行控制教程，让你在实践中学习和创新。

项目简介
dRehmFlight是由Nicholas Rehm开发的一款专为业余爱好者和非编程者设计的飞行控制器。它提供了直观易懂的代码结构，让你无需深入复杂的类库就能快速理解并进行定制化开发。此外，项目还包含了详细的VTOL飞行稳定概念介绍，无论是新手还是经验丰富的老手都能从中受益。

技术分析
dRehmFlight基于Arduino兼容的Teensy 4.0微控制器和MPU6050 6轴惯性测量单元，这使得它具备了出色的硬件扩展性和灵活性。Beta 1.3版本新增了Spektrum DSM卫星接收器支持、一次性IMU校准以及ESC校准功能，进一步提升了用户体验。


![](https://github.com/nickrehm/dRehmFlight/raw/master/dRehmFlight%20Logo.png)


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241126113138.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241126113215.png)

### Hardware
This flight controller is based off of the Teensy 4.0 microcontroller and MPU6050 6DOF IMU. The following components (available on Amazon) are required to complete the flight controller assembly:

Teensy 4.0: https://amzn.to/3oFG3QN

Alternative Links: Sparkfun, Adafruit, Electromaker

Due to supply chain issues, the Teensy 4.0 has been frequently out of stock throughout 2022. The Teensy 4.1 is generally in stock more often and is immediately compatible with the dRehmFlight pin mappings (plus you get extra bonus pins!): https://amzn.to/3c1OSSw

GY-521 MPU6050 IMU: https://amzn.to/3edF1Vn

These (and all Amazon links contained within the supporting documentation) are Amazon Affiliate links; by purchasing from these, I receive a small portion of the revenue at no cost to you. I appreciate any and all support!

x
### 视频连接
[World's Fastest FLYING RC Drift Car - YouTube](https://www.youtube.com/watch?v=dcu0jODIlWU)

倒立摆
[Flying Inverted Pendulum - YouTube](https://www.youtube.com/watch?v=XmYRQi48s-8)

跟随算法

[Ground Effect Vehicle Autonomous Vision-Based Tracking - YouTube](https://www.youtube.com/watch?v=uaY2G5Kbj_g)

悬停
[abritten/dRehmFlight-StantonModel-VTOL: This is a replica of the Stanton RC VTOL model using the DrehmFlight FC. Replicated and modified by abritten (Drew Britten).](https://github.com/abritten/dRehmFlight-StantonModel-VTOL?tab=readme-ov-file)