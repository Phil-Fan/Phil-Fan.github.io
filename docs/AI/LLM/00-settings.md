# 环境配置与工具使用记录


## huggingface

[Hugging Face Forums - Hugging Face Community Discussion](https://discuss.huggingface.co/)


[OSError: We couldn‘t connect to ‘https://huggingface.co‘ to load this file, couldn‘t find it(亲测有效)\_checkout your internet connection or see how to ru-CSDN博客](https://blog.csdn.net/l8947943/article/details/143099409)



1. 科学上网，访问该网址
通过全局代理的方式，实现模型的下载。

1. 使用镜像网址
国内huggingface镜像地址：https://hf-mirror.com/
往下翻，直接可看到使用教程。主要有四种解决方式。最直接的方式就是一个个下载使用。

1. 在代码中增加设置
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'



## Attention is All You Need 论文复现

选择[hyunwoongko/transformer: Transformer](https://github.com/hyunwoongko/transformer): PyTorch Implementation of "Attention Is All You Need"

### 问题1 conda环境问题

- [miniconda安装](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda)

```shell title="conda换源"
conda config --add channels conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
conda config --set show_channel_urls yes
```

```shell title="创建环境"
conda create -n transformer python=3.10
```

```shell title="激活环境"
conda activate transformer
```

```shell title="安装torchtext"
conda install torchtext==0.13.1
```

```shell title="安装torchdata"
conda install torchdata==0.4.1
```

> [艰辛的torchtext安装旅程 - 知乎](https://zhuanlan.zhihu.com/p/598841083)


### 问题2 mkl降级
[解决lib/python3.7/site-packages/torch/lib/libtorch_cpu.so: undefined symbol: iJIT_NotifyEvent_python_皮卡兔子屋-2048 AI社区](https://2048.csdn.net/682d3789606a8318e85865cc.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTk4OTc1LCJleHAiOjE3NTIyNDk0OTYsImlhdCI6MTc1MTY0NDY5NiwidXNlcm5hbWUiOiJQaGxpRmFuIn0.1FEb7DOwlbsLHbG-UjecQRWeRotMNeiLvlZ3V2dUdW4)

遇到了`/site-packages/torch/lib/libtorch_cpu.so: undefined symbol: iJIT_NotifyEvent`

对mkl进行降级

```shell title="mkl"
conda install mkl=2024.0
```

### 问题3 libfii库出错
```
ImportError: /usr/lib/x86_64-linux-gnu/libp11-kit.so.0: undefined symbol: ffi_type_pointer, version LIBFFI_BASE_7.0
```
[Conda虚拟环境下libp11-kit.so.0: undefined symbol: ffi_type_pointer...问题解决-CSDN博客](https://blog.csdn.net/qq_38606680/article/details/129118491)

```shell title="libffi"
ls -l | grep libffi
mv libffi.so.7 libffi_bak.so.7
sudo ln -s /lib/x86_64-linux-gnu/libffi.so.7.1.0 libffi.so.7
ln -s /lib/x86_64-linux-gnu/libffi.so.7.1.0 libffi.so.7
ldconfig
```

### 问题4 datasets库出错
`ImportError: cannot import name 'load_dataset' from 'datasets' (unknown location)`

```shell title="datasets"
pip install datasets
# 或者在 conda 环境中
conda install -c huggingface datasets
```

### 问题5 torchtext库出错
’No module named ‘torchtext.legacy’

问题出现原因：
1. torchtext is not compatible with new versions of Numpy
2. torchtext current version don't have "from torchtext.legacy.data import Field, BucketIterator"

解决方法：
修改代码，参照[Fixed 'data_loader.py' by Faizanfarhad · Pull Request #35 · hyunwoongko/transformer](https://github.com/hyunwoongko/transformer/pull/35)

### 问题6 spacy库安装


`OSError: [E050] Can't find model 'de_core_news_sm'. It doesn't seem to be a Python package or a valid path to a data directory.`

```shell title="spacy"
pip install spacy
python -m spacy download de_core_news_sm
python -m spacy download en_core_web_sm
```



```shell title="spacy"
pip install -U spacy==3.6.0
python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm
python -m spacy download de_core_news_sm
```

```shell title="如果网络有问题，可以直接下载后本地安装"
wget https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.6.0/de_core_news_sm-3.6.0-py3-none-any.whl
wget https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl
wget https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.6.0/zh_core_web_sm-3.6.0-py3-none-any.whl
pip install zh_core_web_sm-3.6.0-py3-none-any.whl de_core_news_sm-3.6.0-py3-none-any.whl en_core_web_sm-3.6.0-py3-none-any.whl
```

```shell title="numpy降版本"
pip install numpy==1.26.4
```


### 问题7 Multi30k数据集下载
`Could not get the file at http://www.quest.dcs.shef.ac.uk/wmt16_files_mmt/training.tar.gz. [RequestException] None.`

```shell title="wmt16_files_mmt"
wget http://www.quest.dcs.shef.ac.uk/wmt16_files_mmt/training.tar.gz
```

https://github.com/neychev/small_DL_repo/tree/master/datasets/Multi30k

并将三个文件放在`/root/.cache/torch/text/datasets/Multi30k`（本目录根据个人有所变化）

但是这一招对我并不管用。

所以我直接修改了`data_loader.py`，使用本地数据集进行加载

### 训练结果

这里使用的是Multi30K数据集

en2de训练结果

![image-20250706135450331](assets/00-Settings.assets/image-20250706135450331.png)

de2en训练结果

![image-20250706135404376](assets/00-Settings.assets/image-20250706135404376.png)



## llama-factory 使用记录


1. 模型问题，下载模型
- 如果下载出现问题，会报错
```
safetensors_rust.SafetensorError: Error while deserializing header: MetadataIncompleteBuffer
```

2. 模版问题：使用`llama3`模版：可以在   `template.py` 中添加自己的对话模板。
3. lora问题

```
ValueError: Target modules {'c_attn'} not found in the base model. Please check the target modules and try again.
```
改成`q_proj,v_proj`
```
--lora_target q_proj,v_proj
```
