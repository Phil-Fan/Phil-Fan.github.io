# RespbeeryPi
[树莓派中文文档](https://hackpi.fun/docs/)


## 系统烧录

[树莓派4B安装Ubuntu20.04桌面（详细教程）\_树莓派4b ubuntu-CSDN博客](https://blog.csdn.net/m0_70372760/article/details/140354298)

sd卡格式化[SD Memory Card Formatter for Windows Download | SD Association](https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091401.png)



利用烧录工具Raspberry Pi Imager[下载](https://www.raspberrypi.com/software/)烧录Ubuntu 20.04镜像系统，步骤如下：
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091552.png)
点击选择操作系统，下拉到最下面，选择自己下载的系统镜像

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240914091604.png)

[树莓派4B安装Ubuntu20.04桌面（详细教程）\_树莓派4b ubuntu-CSDN博客](https://blog.csdn.net/m0_70372760/article/details/140354298)

## 遇到问题

### SD卡故障排除
1. 确保不要使用劣质的SD
2. 检查电源供电是否满足要求。全速运行时，如果电压低于4.75V会导致系统不稳定
3. 检查供电USB线，不要使用劣质线，也不要使用太长的供电线，以免由于线路损失导致供电不足
断电前确保运行 `sudo halt` 关闭系统
4. 超频也可以导致一些问题
### 无法进入图形界面

[树莓派开机黑屏只有光标无法进入图形界面桌面\_树莓派开机后一直进不去系统-CSDN博客](https://blog.csdn.net/df1445/article/details/124310115)