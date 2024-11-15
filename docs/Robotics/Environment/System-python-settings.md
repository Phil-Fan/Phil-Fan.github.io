# Python 相关配置

## conda



[conda换地址](https://blog.csdn.net/chengjinpei/article/details/119835339)


清华镜像地址：`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/`

按照你系统的架构选择合适的下载
```shell
uname -m
```

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```
下载后执行得到的文件
```shell
bash Miniconda3-py39_24.7.1-0-Linux-aarch64.sh
```

一路点enter和yes，最后重启终端，得到带有`(base)`的提示符，说明安装成功




[conda 使用指南](https://blog.csdn.net/miracleoa/article/details/106115730)

!!! note " conda 和 pip 的区别"
    [Anaconda | Understanding Conda and Pip](https://www.anaconda.com/blog/understanding-conda-and-pip)

    ||conda|pip|
    |---|---|---|
    |manages|binaries|	wheel or source|
    |can require compilers|	no|	yes|
    |package types|	any	|Python-only|
    |create environment|yes, built-in|no, requires virtualenv or venv|
    |dependency checks|	yes|no|
    |package sources|Anaconda repo and cloud|PyPI|


### conda的环境变量配置
在安装目录下的`\Scripts`文件夹下

### pip

查看某个包所有的版本
```shell
pip index versions <package>
```

安装指定版本的包

```shell
pip install <package>==<version>
```

#### 使用命令行调用不同版本的python

在系统路径path（高级系统系统设置——环境变量）中加入python.exe所在目录（打开文件所在位置——属性——打开文件所在位置）（因为是快捷方式，所以需要先找到快捷方式所在目录，再找到原exe文件所在位置）

**注：应考虑到优先级的问题，将想要通过命令行直接进入的python版本所对应的路径放在上面**
### pip换源

```shell title="临时换源"
pip install package_name -i https://pypi.tuna.tsinghua.edu.cn/simple 
```

```shell title="清华源 永久换源"
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 使用

激活
```shell
source ~/anaconda3/bin/activate
```




```shell
# 切换盘符
cd /d d:

conda --version
conda -V #获取版本号

# 1. 创建虚拟环境
conda create -n your_env_name(虚拟环境名称) python==xx(想要创建的虚拟环境的python版本号)
 
# 在指定的位置创建虚拟环境
conda create -p /PATH/TO/path
conda env list # 查看所有的conda虚拟环境  
conda list # 检查安装
 
# 2. 激活虚拟环境
conda activate name
conda deactivate
conda env remove -n flowers
 
# 5. 安装包
conda install package_name(包名)
conda install scrapy==1.3 # 安装指定版本的包
conda install -n 环境名 包名 # 在conda指定的某个环境中安装包
 
# 6. 跳过安装失败的包，继续安装
# conda方式
while read requirement; do conda install --yes $requirement; done < requirements.txt
 
# pip方式
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt

# 7. 卸载包
conda remove -n <package_name> --all
```


### `conda`环境导出与导入
导出
```bash
conda list -e > requirements.txt
```

导入安装
```bash
conda install --yes --file requirements.txt
```

导出 yml 文件方式
```bash
conda env export > freeze.yml
```

安装
```bash
conda env create -f freeze.yml
```

### pip 导出环境

1. 导出结果含有路径
导出结果会存在路径，生成的requirements.txt文件在当前目录下。
```shell
pip freezen > requirements.txt
```

2. 导出不带路径的
生成的requirements.txt文件在当前目录下。
```shell
pip list --format=freeze > requirement.txt
```
生成requirements.txt，pip freeze会将当前PC环境下所有的安装包都进行生成,再进行安装的时候会全部安装很多没有的包.此方法要注意。

安装requirements文件的pip源的包
```shell
pip install -r requirements.txt
```


## Pytorch

### CUDA
!!! note "什么是CUDA"
    通俗地说，CUDA是一种协助“CPU任务分发+GPU并行处理”的编程模型/平台，用于加速GPU和CPU之间的计算。
    
    也就是说CUDA通过CPU任务分发和GPU并行处理的方式，把计算任务通过CPU分发给GPU进行并行计算加速。而GPU并行计算的能力需要CUDA借助其自带的编程接口和工具，比如C/C++语言来编写并行计算程序，并通过CUDA编译器将程序转化为可以在英NVIDIA GPU上执行的机器码快速运行。
                        
查看cuda支持版本，`win+R`输入`cmd`输入`nvidia-smi.exe`

下载地址[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829195225.png)

点击符合的版本选择下载，直接安装。注意安装路径要装在自己记得住的地方下，要预留好空间，最好不要装在C盘。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829195549.png)

**安装验证方法：**

1. cmd中输入`nvcc -V`，有信息说明成功
2. 安装路径下`\extras\demo_suite\deviceQuery.exe`，运行这个文件，有`PASS`说明成功（查询一下本机的gpu设备
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829200019.png)
3. 安装路径下`\extras\demo_suite\bandwidthTest.exe`，运行这个文件，有`PASS`说明成功
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240829200006.png)

[Installation Guide Windows :: CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/archive/11.6.0/cuda-installation-guide-microsoft-windows/index.html#system-requirements)

### cuDNN安装
cuDNN是NVIDIA CUDA®深度神经网络库，用于GPU加速的深度神经网络。它提供了高度优化的实现，包括前向和反向卷积、池化层、归一化和激活层等标准例程

安装网站[cuDNN Archive | NVIDIA Developer](https://developer.nvidia.com/rdp/cudnn-archive)

找到符合自己上面CUDA安装版本的cuDNN版本，下载解压，将解压后的文件夹中的`bin`、`include`、`lib\x64`文件夹中的文件复制到CUDA的安装目录中对应的文件夹中。

注意这一步需要注册一下NVIDIA的账号


### Pytorch 安装


```shell title="查看CUDA版本"
nvidia-smi
```

```shell title="查看CUDA的版本"
nvcc -V
nvcc --version
```

装了python3.9，我的CUDA版本是10.2，在[Previous PyTorch Versions | PyTorch](https://pytorch.org/get-started/previous-versions/)这个网站上可以找到各个版本对应的下载链接

```shell title="CUDA=10.2"
pip install torch==1.10.1+cu102 torchvision==0.11.2+cu102 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu102/torch_stable.html
```

!!! failure "numpy报错"
    安装好torch之后，numpy会报错

    ```
    UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at  ..\torch\csrc\utils\tensor_numpy.cpp:68.)
    _dtype_to_storage = {data_type(0).dtype: data_type for data_type in _storages}
    ```

    **解决方法：** 将numpy版本降低为非>2.0.0的版本，之后就能成功导入了。
    ```shell
    pip uninstall numpy
    pip install numpy==1.26
    ```



```python title="测试是否可用"
import torch # 如果pytorch安装成功即可导入
print(torch.cuda.is_available()) # 查看CUDA是否可用
print(torch.cuda.device_count()) # 查看可用的CUDA数量
print(torch.version.cuda) # 查看CUDA的版本号
```
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240903112501.png)





## Pycharm

### 申请学生权限



语言设置为中文

setting-plugin-chinese





### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你Pycharm远程连接服务器端项目进行本地开发调试！...-CSDN博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)