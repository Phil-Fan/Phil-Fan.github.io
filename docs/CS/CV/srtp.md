# 一种隐私保护的姿态识别系统



## 硬件部分

### 流程






查看ip：`ipconfig`

ssh usslab@192.168.1.70
ssh pi@192.168.1.23

1. laptop 运行 setup.sh
2. pi 运行 setup.sh
3. pi 运行 video.py
4. laptop 运行 server.py
5. 电脑连接 laptop 共享文件夹，将数据集放入 source 文件夹
6. pi 运行 main.py
7. laptop 运行 TempestSDR 并调整窗口位置（运行 ./capture.sh）
8. 选择要采集的数据集，开始采集

### 可以优化的
1.播放数据集的第一张图片重复
1. 安装USRP X310
3.把combine和crop集成到tcp中
4.TempestSDR软件按照路径保存
5.自动寻找
6.鼠标自动寻找按钮



## 软件部分


## `mmpose 0.28`复现遇到问题

### 安装流程

[依赖环境 — MMPose 0.29.0 文档](https://mmpose.readthedocs.io/zh-cn/0.x/install.html#id2)

[mmdet代码复现：安装指定版本的mmcv和mmdet以及版本匹配问题。-CSDN博客](https://blog.csdn.net/shysea2019/article/details/129818430)






#### 安装`pytorch`

> MMPose 适用于 Linux、Windows 和 macOS。它需要 Python 3.6+、CUDA 9.2+ 和 PyTorch 1.5+


```shell
conda create --name openmmlab python=3.8 -y
conda activate mmpose.28
```


#### 下载`mmpose 0.28`代码

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