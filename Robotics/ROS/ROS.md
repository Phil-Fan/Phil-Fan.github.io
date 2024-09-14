# ROS 操作
## 系统烧录

[balenaEtcher已经烧录的u盘恢复](https://blog.csdn.net/A___LEi/article/details/117700660#:~:text=1、打开命令行cmd（win%2Br打开运行，在其中输入cmd就可以打开）； 2、在cmd下输入diskpart命令； 3、在diskpart里面，输入list disk命令查看当前系统挂载的磁盘（包括SATA、U盘、SD卡等）； balenaEtcher烧录U盘%2FSD卡恢复方法,4、找到要恢复的磁盘，比如我要恢复的是磁盘1，输入命令select disk 1； 5、输入命令clean就可以将4中所选的磁盘数据清空了，再次输入list disk可以看到磁盘的可用已经和大小一样了。)

```shell
wget http://fishros.com/install -O fishros && . fishros
```
[小鱼的一键安装系列 | 鱼香ROS](https://fishros.org.cn)

!!! note "no directory"
    切换到`bash`使用 可以把 `. fishros` 替换成 `bash fishros`


[如何在树莓派 4 上安装 Ubuntu 桌面系统 | Linux 中国 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/413743940)

注意安装desktop版本而不是sever版本

测试代码
```shell
roscore
rosrun turtlesim turtlesim_node
rosrun turtlesmi turtle_teleop_key
```



## 硬件安装

### 风扇
风扇安装与控制

```
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
sudo vi /etc/rc.local
sudo chmod 755 /etc/rc.local
```

```
#!/bin/bash
sleep 10
sudo /usr/bin/jetson_clocks
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```



nano板子和stm32板子使用usb-b -》usb-c 链接

[英伟达 Jetson Nano 新手必备：连接蓝牙音频_jetson nano 链接音响_许野平的博客-CSDN博客](https://blog.csdn.net/quicmous/article/details/115174779)

## 



## `ROS`操作

````shell
#查看ip地址
ifconfig


#底盘
roslaunch clbrobot bringup.launch

#键盘操控
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
小写 & 大写字母

#imu校正
roslaunch clbrobot bringup.launch
rosrun imu_calib do_calib
按照提示调整小车，并按照指示按下enter

#线速度修正
roslaunch clbrobot bringup.launch
rosrun clbrobot_nav calibrate_linear.py
rosrun rqt_reconfigure rqt_reconfigure
设定1m，最后一栏记录实际值，多次实验平均
roscd clbrobot/launch
gedit bringup.launch

#角速度修正
roslaunch clbrobot bringup.launch
rosrun clbrobot_nav calibrate_angular.py
rosrun rqt_reconfigure rqt_reconfigure

-30
-25
-26
-30

 #雷达启动


 #相机启动
roslaunch clbrobot camera.launch
roslaunch clbrobot clbrobot_web.launch
IP:8080

 #相机建图
 roslaunch clbrobot bringup.launch
 
 roslaunch clbrobot astra_xtion_gmapping.launch
 rviz
 打开 home/catkin_ws/src/clbrobot_project/clbrobot/rviz/slam.rviz
 rosrun teleop_twist_keyboard teleop_twist_keyboard.py
 roscd clbrobot/maps
 ./map.sh
 
 #相机导航
 roslaunch clbrobot bringup.launch
 roslaunch clbrobot astra_navigate.launch
 rviz
 nav goal
 
 #避障
 roslaunch clbrobot bringup.launch
 roslaunch clbrobot_follower follower.launch
 
 #手机
 roslaunch clbrobot bringup.launch
 roslaunch clbrobot camera.launch
 roslaunch clbrobot lidar_slam.launch
 roscd clbrobot/maps
 ./map.sh
 
 #巡线
 roslaunch clbrobot bringup.launch
 roslaunch clbrobot camera.launch
 roslaunch clbrobot_line_follower clbrobot_line.launch
 
 
 #二维码识别
 roslaunch clbrobot bringup.launch
 roslaunch clbrobot camera.launch
 
 roslaunch clbrobot_ar_track clbrobot_ar_camera.launch
 roslaunch clbrobot_ar_track clbrobot_ar_large_markers.launch
 roslaunch clbrobot_ar_track clbrobot_ar_tags_cog.launch
 roslaunch clbrobot_ar_track clbrobot_ar_follower.launch
 
#多点导航
roslaunch clbrobot bringup.launch
roslaunch clbrobot navigate.launch
rviz
open "navigate.rviz"

use "2D Pose Estimate"
use "Publish Point" to choose dots to be passed

  
 
 
 
  roslaunch clbrobot_hand_pose clbrobot_hand_pose.launch
  
  roslaunch clbrobot_object_detect clbrobot_face_object.launch
  
  
````



### 激光雷达建立地图

```shell
#gmapping slam
roslaunch clbrobot bringup.launch
roslaunch clbrobot lidar_slam.launch

#hector slam
roslaunch clbrobot bringup.launch
roslaunch clbrobot hector_slam.launch
rviz
open "slam.rviz"
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
roscd clbrobot/maps/
./map.sh

#Karto SLAM
roslaunch clbrobot bringup.launch
roslaunch clbrobot karto_slam.launch
rviz
open "slam.rviz"
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

#Cartographer SLAM算法构建地图
roslaunch clbrobot bringup.launch
roslaunch clbrobot rplidar.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
roslaunch clbrobot cartographer_slam.launch
rviz
open config "cartographer.rviz"
```

python 依赖包

```
roslaunch target_object_detector target_object_detector.launch
```

```

```

- rviz 操作： 平移，2d，视角转换，家



```shell
catkin_make -DCATKIN_WHITELIST_PACKAGES="darknet_ros"

 roslaunch clbrobot bringup.launch
 roslaunch clbrobot camera.launch
 roslaunch darknet_ros darknet_ros.launch
 roscd darknet_ros/script
 python ObjectLocation.py
 
 roslaunch clbrobot astra_navigate.launch
```

[jetson nano之(6):配置蓝牙音响 – 走着的博客 (openpilot.cc)](https://blog.openpilot.cc/archives/2307)

```
#查看摄像头
rqt_image_view

#蓝牙连接
```

[ROS实战( 三 )利用科大讯飞tts实现ROS下语音合成播报_无驰复逸的博客-CSDN博客](https://blog.csdn.net/weixin_40522162/article/details/80525758)



[darknet-yolov3训练自己的数据集，并测试训练结果_dota数据集在yolov3 训练结果_pd很不专业的博客-CSDN博客](https://blog.csdn.net/qq_42145185/article/details/105816128)

[Jetson Nano之ROS入门 -- YOLO目标检测与定位_ros目标检测_szu_ljm的博客-CSDN博客](https://blog.csdn.net/m0_55202222/article/details/132016297)





# 
