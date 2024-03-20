# 环境配置

## 虚拟环境的配置

```shell
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



## pytorch

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



conda

```shell
# 切换盘符
cd /d d:


```

## Pycharm

### 申请学生权限



语言设置为中文

setting-plugin-chinese





### 远程服务器连接与配置

```shell
ssh -p 15821 root@connect.westb.seetacloud.com
```

[pycharm 打开远程项目_手把手教你Pycharm远程连接服务器端项目进行本地开发调试！...-CSDN博客](https://blog.csdn.net/weixin_34345947/article/details/114909727)

