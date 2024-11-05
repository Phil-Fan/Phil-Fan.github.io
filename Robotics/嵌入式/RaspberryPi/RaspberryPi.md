# Raspberry Pi
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

### 风扇

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241031231019.png)

### 显示屏

如果显示屏黑屏的话，考虑电压是不是太低了，电压过低会驱动不了显示屏


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

重启电脑`reboot`


```shell title="查看设备列表"
sudo apt install v4l-utils

v4l2-ctl --list-devices
```

```shell title="设置"
sudo vim /boot/config
```
找到以`config`开头的文件，再最后一行加入与相机对应的代码
```
dtoverlay=ov5647
```

| Camera Module | In /boot/config.txt |
|----------------|----------------------|
| V1 camera (OV5647) | `dtoverlay=ov5647` |
| V2 camera (IMX219) | `dtoverlay=imx219` |
| HQ camera (IMX477) | `dtoverlay=imx477` |
| IMX290 and IMX327 | `dtoverlay=imx290,clock-frequency=74250000` or `dtoverlay=imx290,clock-frequency=37125000` (both modules share the imx290 kernel driver, please refer to instructions from the module vendor for the correct frequency) |
| IMX378 | `dtoverlay=imx378` |
| OV9281 | `dtoverlay=ov9281` |




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

```shell title="motion.conf设置"
daemon on  #off改成on
width 640  
height 480 #根据摄像头像素自行更改
framerate 50 #帧率
stream_maxrate 200
stream_localhost off    #设为off
```

```shell title="关闭motion服务"
sudo killall -TERM motion
```

```shell title="打开motion"
sudo motion
```

接着就可以在`http://<本机ip>:8081`看到你的视频流了

#### opencv


```python title="测试能用的相机接口"
import cv2

def test_open_cam():
    connected_cam = []
    for port in range(0, 20):
        try:
            cam = cv2.VideoCapture(port)
            if cam.isOpened():
                connected_cam.append(port)
            cam.release()
            cv2.destroyAllWindows()
        except:
            cam.release()
            cv2.destroyAllWindows()
    print(f'=> list of found cameras: {connected_cam}')
    return(connected_cam)

test_open_cam()
```

```shell title="结果"
[ WARN:0] VIDEOIO(V4L2:/dev/video16): can't open camera by index
[ WARN:0] VIDEOIO(V4L2:/dev/video17): can't open camera by index
[ WARN:0] VIDEOIO(V4L2:/dev/video18): can't open camera by index
[ WARN:0] VIDEOIO(V4L2:/dev/video19): can't open camera by index
=> list of found cameras: [0, 14, 15]
```


```python title="openCV拍单帧照片例程"
import cv2
cap = cv2.VideoCapture(0) # 打开摄像头
if not cap.isOpened(): # 检查摄像头是否成功打开
    print("无法打开摄像头")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 设置摄像头分辨率
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
ret, frame = cap.read() # 读取一帧图像

if not ret:
    print("无法读取图像") # 检查是否成功读取图像
    exit()

cv2.imwrite("photo.jpg", frame) # 保存图像
cap.release() # 释放摄像头
```

```python title="RGB & 灰度图例程"
import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
  
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
     
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
 
cap.release()
cv2.destroyAllWindows()
```


[用树莓派实现实时的人脸检测 | 树莓派实验室](https://shumeipai.nxez.com/2018/03/09/real-time-face-recognition-an-end-to-end-project-with-raspberry-pi.html)


## 操作
### 共享文件夹
```shell
apt-get install -y cifs-utils
```

[在windows上共享文件夹](https://zhuanlan.zhihu.com/p/402820328)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026225133.png)
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241026225143.png)


**挂载文件系统**

将 `//<ip>/test` 挂载到 `/mnt/` 目录上，如果不需要认证，则无需指定用户名和密码。

```shell
sudo mount -t cifs //<ip>/test /mnt/test_shared -o dir_mode=0777,file_mode=0777
```

[linux mount挂载文件夹设置权限 - 秋声梧叶 - 博客园](https://www.cnblogs.com/sctrkb/articles/15407736.html)


开机自动挂载（修改 `/etc/fstab` 文件）：

将`//192.168.xx.xx/sharedir`挂载到`/mnt/cifs`上，并指定了用户名和密码;如果不需要认证，可以不指定用户名和密码。
```shell
//192.168.3.4/sharedir /mnt/cifs cifs username=demo,password=demo 0 0
```

然后可以把`/mnt/folder`直接当作linux中的文件夹进行文件的操作

> pywin32库没有安装好 [Python 如何通过Python访问Windows网络上的共享文件夹|极客教程](https://geek-docs.com/python/python-ask-answer/311_python_using_python_how_can_i_access_a_shared_folder_on_windows_network.html)


## 遇到问题

### SD卡故障排除
1. 确保不要使用劣质的SD
2. 检查电源供电是否满足要求。全速运行时，如果电压低于4.75V会导致系统不稳定
3. 检查供电USB线，不要使用劣质线，也不要使用太长的供电线，以免由于线路损失导致供电不足
断电前确保运行 `sudo halt` 关闭系统
4. 超频也可以导致一些问题
### 无法进入图形界面

[树莓派开机黑屏只有光标无法进入图形界面桌面\_树莓派开机后一直进不去系统-CSDN博客](https://blog.csdn.net/df1445/article/details/124310115)


### `Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.`

```shell
sudo vim /etc/gdm3/custom.conf
```
按下`/` ，寻找 `#WaylandEnable=false`

将`#`删除，重启系统

