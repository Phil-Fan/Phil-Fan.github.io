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





## `mmpose 0.28`复现遇到问题

### 安装流程

[依赖环境 — MMPose 0.29.0 文档](https://mmpose.readthedocs.io/zh-cn/0.x/install.html#id2)

[mmdet代码复现：安装指定版本的mmcv和mmdet以及版本匹配问题。-CSDN博客](https://blog.csdn.net/shysea2019/article/details/129818430)

1. 安装`pytorch`
2. 下载`mmpose 0.28`代码

```shell
pip install -U openmim
mim install mmcv-full==1.3.8

cd mmpose # 切换到源码目录
pip install -r requirements.txt
pip install -v -e .
```

### `错误 Microsoft Visual C++ 14.0 or greater is required.`

这个原因就是因为由于缺少Microsoft Visual C++ Build Tools导致的

根据报错里面提供的网址：[Microsoft C++ Build Tools - Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/)把工具下好，如果你不知道你的项目部署的具体情况，就把c++的选项全点上。

![img](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/e4f5ed6621e244de97c7a152277297b5.png)

### `ModuleNotFoundError: No module named 'version'`

错误原因：在`./mmpose/__init__.py`头有

```python
from version import __version__, short_version
```

相对引用有问题，需要改成

```python
from .version import __version__, short_version
```



### `AssertionError: Torch not compiled with CUDA enabled`

问题：CUDA配置有问题，但是我的电脑没有显卡，所以需要使用CPU进行运算，所以在CPU上运行。

```python
# 法1
# 原来的 torch.cuda.set_device(0)
# 即把有device=xxx的语句统统写成cpu
device = ('cuda' if torch.cuda.is_available() else 'cpu')



# 法2
# 原来的 checkpoint = torch.load("/home/model/model_J18.pth.tar")
checkpoint = torch.load("C:/Users/user/Desktop/CoRRN/CoRRN/model/model_J18.pth.tar",map_location = 'cpu') 

# 法3
# 原来的 model = model.cuda() 
model = model.to(device)
```

即将`.cuda()` 的地方都换成`.to(device)`

