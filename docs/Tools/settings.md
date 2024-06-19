# 环境配置

## 如何复制Phil Fan的工作环境

### 效率软件

- 日程 - 滴答清单
- Markdown - Typora
- 图片： HoneyView，PicGo（图床）
- 视频：QQ影音
- 思维导图: Xmind
- 计时：ManicTime
- 绘图：Draw.io, Geogebra
- PDF阅读：Adobe Acrobat
- 云同步：百度网盘、阿里网盘
- 即时通讯：TIM，WeChat，飞书，腾讯会议，钉钉
- 压缩：Bandzip
- 浏览器：Edge
- 翻译：欧陆词典

### 专业软件

- Coding: VSC, PyCharm, WebStorm
- 环境：python，R，VMware，anaconda，git
- 数据：Tableau，excel，origin
- 文献：Zotero
- word，小恐龙公文助手
- latex：overleaf

### 设计软件

- Adobe: AI,PS,PR,剪映
- powerpoint，okplus，Canva

## windows

电脑

[AirPods Pro2蓝牙耳机连接win10电脑有杂音、不稳定问题 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/641213713)

### 显示器相关

#### 如何修复Type-C接口

当我的type-c接口插了一段时间以后，接口就会出现松动的情况

用针头将两侧的钩子撑开，就可以解决一定问题



> 以下图片来自[USB TYPE C                             拆解以及USB3.1规范详解 (lulian.cn)](https://www.lulian.cn/news/88-cn.html)

![USB Type C接头拆解图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1540889232305758.jpg)

![USB Type C接头拆解图](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/1540889232965453.jpg)

**盒盖不息屏**

设置里搜“关闭盖子”

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-debea2bfb9bc1c5d7449c2a6c7080dfd_720w.webp)

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/v2-79a54efe642a46bd24107b2a97f160d1_720w.webp)



**Windows +A**进入消息中心

![image-20240429090307137](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090307137.png)

![image-20240429090336993](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090336993.png)

打开显示设置，调节分辨率

![image-20240429090404258](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240429090404258.png)



### 环境变量

#### 使用命令行调用不同版本的python

在系统路径path（高级系统系统设置——环境变量）中加入python.exe所在目录（打开文件所在位置——属性——打开文件所在位置）（因为是快捷方式，所以需要先找到快捷方式所在目录，再找到原exe文件所在位置）

**注：应考虑到优先级的问题，将想要通过命令行直接进入的python版本所对应的路径放在上面**





#### 如何用命令行直接打开软件

省流：建立一个文件夹保存快捷方式，将文件夹路径添加到PATH环境变量

首先你要创建一个文件夹，存储程序的快捷方式



- 右键点击计算机图标，选择属性，选择高级系统设置，高级->选择环境变量

- 编辑用户变量下的PATH复制存储快捷方式文件夹的路径

备注：快捷方式可以自定义名称，在CMD中输入名称就行了

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201221085949893.png)

高级系统设置 - 环境变量

![image-20240422084315579](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240422084315579.png)

## `Vimium`配置

[使用 Vimium 获得更舒适的网页阅读体验 - 少数派 (sspai.com)](https://sspai.com/post/57091#!)

## `pytorch`

```shell
import torch # 如果pytorch安装成功即可导入
print(torch.cuda.is_available()) # 查看CUDA是否可用
print(torch.cuda.device_count()) # 查看可用的CUDA数量
print(torch.version.cuda) # 查看CUDA的版本号

# 查看CUDA的版本
nvcc -V
nvcc --version

# 查看CUDA版本
nvidia-smi
```



## `conda`

```shell
# 切换盘符
cd /d d:

conda --version
conda -V #获取版本号

conda env list # 列出所有的环境

# 创建环境
conda create -n your_env_name(虚拟环境名称) python==xx(想要创建的虚拟环境的python版本号)

conda activate name
conda deactivate
conda env remove -n flowers

# 检查安装
conda list

```

## `Pycharm`

### 申请学生权限



语言设置为中文

setting-plugin-chinese





### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你Pycharm远程连接服务器端项目进行本地开发调试！...-CSDN博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)





## 搜狗输入法

搜狗输入法老是出现快捷键冲突或是占用热键的情况

所以进入设置界面 - 按键 - ban掉系统功能快捷键

![在这里插入图片描述](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20201218111624799.png)

![image-20240619085926633](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240619085926633.png)

## vscode

markdown 插件 —— Markdown Preview Enhanced

设置一个`picgo`的快捷键，我这里设置的是`ctrl + alt + P`

截图之后直接按就可以将图片上传到图床，并将连接复制到剪贴板
