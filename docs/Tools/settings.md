# 环境配置

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

