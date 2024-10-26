# RespbeeryPi
[树莓派中文文档](https://hackpi.fun/docs/)


## 系统烧录


sd卡格式化[SD Memory Card Formatter for Windows Download | SD Association](https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091401.png)



利用烧录工具Raspberry Pi Imager[下载](https://www.raspberrypi.com/software/)烧录Ubuntu 20.04镜像系统，步骤如下：
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091552.png)
点击选择操作系统，下拉到最下面，选择自己下载的系统镜像

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091604.png)

[树莓派4B安装Ubuntu20.04桌面（详细教程）\_树莓派4b ubuntu-CSDN博客](https://blog.csdn.net/m0_70372760/article/details/140354298)

20.04只有server版本，没有desktop版本，但是cli界面+校网简直无敌，所以还是选择了mate


烧录的镜像应该是像这样的压缩包一样的，不要烧录iso，
```shell
ubuntu-mate-20.04-beta1-desktop-arm64+raspi.img.xz
```


[Ubuntu MATE Releases - /20.04/](https://releases.ubuntu-mate.org/20.04/)

## 硬件

### 摄像头
[树莓派4B摄像头的详细使用教程（拍照+录像+监控）\_树莓派拍照-CSDN博客](https://blog.csdn.net/weixin_45994747/article/details/109605765)

[【2023新教程】树莓派4B安装摄像头教程-配置CSI摄像头-使用libcamera命令操作-解决树莓派安装摄像头后VNC黑屏并显示Cannot currently show the desktop - 知乎](https://zhuanlan.zhihu.com/p/651059892)

[python - 避免\`can't open camera by index\`，用cv2测试时，所有cam都连接\_Stack Overflow中文网](https://stackoverflow.org.cn/questions/65603793)



摄像头连接方法
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026003911.png)

```shell
sudo apt-get install -y raspi-config
```

```shell
raspi-config
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026005020.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026005032.png)

重启电脑


```shell title="查看设备列表"
sudo apt install v4l-utils

v4l2-ctl --list-devices
```




#### 自带

```shell
raspistill -o a.jpg -t 1000
```

这行命令的作用是在一秒钟的延迟之后，拍下一张名为a.jpg的照片，保存在树莓派的主目录下。-t的延迟选项后的参数是以毫秒为单位，1000便表示1秒。延时选项在输入命令时可以不加，但-o后的名称是一定要有的。


#### motion
```shell
sudo apt-get install motion
```


首先将motion软件的后台进程改为开启，让它能够一直在后台运行。输入以下命令，将文件中 `start_motion_daemon=no` 的no改为yes。
```shell
sudo nano /etc/default/motion
```
之后输入命令打开motion的配置文件：
```shell
sudo nano /etc/motion/motion.conf
```
这个文件中保存了许多motion的基本设置，文件内容很多，感兴趣的话可以慢慢研究。因为选项比较多，下面只写出一些比较重要的选项的值，其他可以用默认值，或者参考motion官网上的documents，那里面写得很详尽，每个参数的解释都有。motion.conf里自带的注释也很完整。

需要更改的参数有以下几行，在nano编辑器环境下可以使用快捷键ctrl+w对关键字进行查找。
```shell
daemon on  #off改成on
width 640  
height 480 #根据摄像头像素自行更改
framerate 50 #帧率
stream_maxrate 200
stream_localhost off    #设为off
```

当然要想获得最佳的效果，文档中的参数需要多次根据自己的设备进行相应的调整。
修改完成后保存并退出。

若你之前打开过motion，那么在每次更改完配置后，需要先关闭motion进程，并再次打开，相当于对motion进行一次重启。关闭motion服务的命令如下：
```shell
sudo killall -TERM motion
```
接着输入命令重新打开motion：
```shell
sudo motion
```

#### opencv

```python
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
while(1):
 # get a frame
 ret, frame = cap.read()
 # show a frame
 cv2.imshow("capture", frame)
 
 if cv2.waitKey(1) & 0xFF == ord('q'):
 #退出并拍照
  cv2.imwrite("takephoto2.jpg", frame)
  print("take Photo Ok")
  break
cap.release()
cv2.destroyAllWindows()
```

## 遇到问题

### SD卡故障排除
1. 确保不要使用劣质的SD
2. 检查电源供电是否满足要求。全速运行时，如果电压低于4.75V会导致系统不稳定
3. 检查供电USB线，不要使用劣质线，也不要使用太长的供电线，以免由于线路损失导致供电不足
断电前确保运行 `sudo halt` 关闭系统
4. 超频也可以导致一些问题
### 无法进入图形界面

[树莓派开机黑屏只有光标无法进入图形界面桌面\_树莓派开机后一直进不去系统-CSDN博客](https://blog.csdn.net/df1445/article/details/124310115)