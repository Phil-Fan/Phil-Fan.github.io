# 无人机实验

!!! note "基础信息"
    时间：
    分组：
    实验内容：
    实验要求：4000字以上报告
    tips：每组一位助教，珍惜助教hhh

## 硬件平台
### 硬件搭建
**qgroundcontrol**

[Download and Install | QGC Guide (master)](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/getting_started/download_and_install.html#windows)

### 树莓派安装


### 动捕测试
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920205747.png)


## 软件搭建

### mavros
```shell
sudo apt-get install ros-noetic-mavros ros-noetic-mavros-extras ros-noetic-control-toolbox

cd /opt/ros/noetic/lib/mavros
sudo ./install_geographiclib_datasets.sh
sudo chmod 777 /dev/ttyACM0
```

```shell
cd real_ws
sudo cp src/mavros_launch_files/px4_pluginlists.yaml /opt/ros/noetic/share/mavros/launch
sudo cp src/mavros_launch_files/px4.launch /opt/ros/noetic/share/mavros/launch
```
启动mavros，检查是否正常通信：

```shell
roslaunch mavros px4.launch
```

另一个终端
```shell
rostopic hz /mavros/imu/data
```

应该能得到如图所⽰的50hz imu数据

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920203808.png)
### nomachine

[NoMachine - NoMachine for Arm](https://downloads.nomachine.com/linux/?distro=Arm&id=30)

查看芯片架构

```bash
uname -m
```

```bash
sudo dpkg -i nomachine_7.6.2_4_armhf.deb
```
### PlotJuggler
PlotJuggler，一个基于Qt的应用程序，允许用户加载、搜索和打印数据。许多ROS用户会为此使用MATLAB或rqt_plot，但是当要分析的数据相当大时，使用这些解决方案可能会不尽人意。

PlotJuggler是rqtplot和rqtbag更好的替代品，它提供了更友好的用户界面。

- Multiplot(多曲线)：将多条曲线添加到绘图中。在行、列、选项卡和/或单独的窗口中排列绘图。
- Zoom(缩放)：轻松缩放绘图。可以锁定所有绘图的X轴。
- Save/Load layouts(保存/加载布局)：组织布局后，可以将其保存到文件中以供以后重用。
- Complete Undo/Redo(完全撤消/重做)：CTRL-Z按您的预期操作。
- DataLoad plugins(数据加载插件)：轻松加载CSV或rosbags。
- DataStreaming plugins(数据流插件)：订阅一个或多个ros主题并实时绘制它们的数据。
- RosPublisher plugin(RosPublisher 插件)：使用交互式跟踪器重新发布原始ROS消息。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920205340.png)
[【ROS学习】- PlotJuggler绘图工具的安装使用-CSDN博客](https://blog.csdn.net/qq_39779233/article/details/106478608)


```shell
sudo apt-get install ros-noetic-plotjuggler
```

```shell
roscore
rosrun plotjuggler plotjuggler  
```

可以看到如下界面
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920205309.png)

### vrpn

```shell
cd ~/catkin_ws/src
git clone https://github.com/clearpathrobotics/vrpn_client_ros.git

sudo apt-get install ros-noetic-vrpn

cd ~/catkin_ws

catkin_make
```


查看电脑ip地址

```shell title="启动"
roslaunch vrpn_client_ros sample.launch server:=192.168.43.195:3883
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920210352.png)

```shell title="查看"
rostopic echo /vrpn_client_node/<刚体名称>
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920210343.png)

## 启动
已经将所有要启动的程序写在⼀个脚本`run.sh`中，只需要⼀键即可启动，但需要先检查各个ros节点的topic是否正确：

⾸先根据在动捕中创建的刚体名称，修改`src/ekf_pose/launch/PX4_vicon.launch`中接收的位姿topic

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920203843.png)

改节点利⽤EKF扩展卡尔曼滤波，对imu和动捕的数据进⾏融合估计，我们以此结果作为⽆⼈机的里程计信息给到控制器。

随后修改run.sh中启动vrpn的ip为动捕主机的ip

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920204616.png)


```shell title="编译"
catkin_make
source devel/setup.bash
./run.sh
```

可通过rqt_graph 来检查各模块间的通讯是否正常。

## 代码
要编写的控制器部分代码位于`real_ws/src/px4ctrl/src/linear_control.cpp`

其中`computeDesiredCollectiveThrustSignal`函数⽤来根据加速度计算油门百分⽐，在实际过程中通过在线估计参数，这部分不需要同学们实现，只需要给定加速度即可。

另外需要计算的是⽆⼈机的姿态`u.q`。
程序提供了debug的接⼝，通过`rostopic`向外发送，可通过`run.sh`中最后一行注释记录`rosbag`，通过`plotjuggler`进行后续分析（详⻅ros仿真中的说明）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240920204728.png)

参数⽂件位于`real_ws/src/px4ctrl/config/ctrl_param_fpv.yaml`，可调节增益参数。

## attention
1. 注意实验安全！！！
2. 四元数、旋转矩阵、欧拉⻆之间的转换
3. 世界系、机体系的坐标变换
4. 建议在实物控制器测试前确保其它模块功能正常
## 调试

移动飞机，查看获得的位姿是否连续光滑

检查动捕球、动捕相机、刚体识别是否都正常

注意小组间区分


### 
- 录rosbag，记录里程计数据
```shell
rosbag record /sim/odom
```
- plotjuggler数据分析软件

https://github.com/facontidavide/PlotJuggler

