# 人工智能与机器学习作业
## Mo平台指北

## 口罩检测
[Search | Kaggle](https://www.kaggle.com/search?q=Masked+face+recognition+in%3Adatasets)

[X-zhangyang/Real-World-Masked-Face-Dataset: Real-World Masked Face Dataset，口罩人脸数据集](https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset/tree/master?tab=readme-ov-file)

[[2003.09093] Masked Face Recognition Dataset and Application](https://arxiv.org/abs/2003.09093)

[NKU-share/人工智能导论 at b60b98043f55257e1e74fc1aa1b7fc5ccbead370 · Starlight0798/NKU-share](https://github.com/Starlight0798/NKU-share/tree/b60b98043f55257e1e74fc1aa1b7fc5ccbead370/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%AF%BC%E8%AE%BA)

[一个基于resnet的口罩检测图片分类（自定义数据集）\_口罩分割数据集-CSDN博客](https://blog.csdn.net/liningxi123/article/details/136702365)

## trick

### 数据增强

### 模型保存


### 集成学习

投票制度


### 正则化


### 学习率下降 scheduler

### 


## NLP
[bert-base-chinese模型离线使用案例-CSDN博客](https://blog.csdn.net/w13716207404/article/details/140223895)

[解决BERT模型bert-base-chinese报错（无法自动联网下载）\_国内下载bert-base-chinese-CSDN博客](https://blog.csdn.net/m0_70574207/article/details/138312224)

[google-bert/bert-base-chinese at main](https://huggingface.co/google-bert/bert-base-chinese/tree/main)

```python title="bert-base-chinese模型离线使用"
import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

# 通过torch.hub(pytorch中专注于迁移学的工具)获得已经训练好的bert-base-chinese模型
# model =  torch.hub.load('huggingface/pytorch-transformers', 'model', 'bert-base-chinese')
model = BertModel.from_pretrained('D:\\MyPython\\data\\bert-base-chinese')

# 获得对应的字符映射器, 它将把中文的每个字映射成一个数字
# tokenizer = torch.hub.load('huggingface/pytorch-transformers', 'tokenizer', 'bert-base-chinese')
tokenizer = BertTokenizer.from_pretrained('D:\\MyPython\\data\\bert-base-chinese')
```






!!! bug "nll_loss_forward_reduce_cuda_kernel_2d: Assertion `t ＞= 0 && t ＜ n__classes` failed."
    [nll\_loss2d: t >= 0 && t < n\_classes assertion is not checked when using GPU tensors and reduction='none' · Issue #49882 · pytorch/pytorch](https://github.com/pytorch/pytorch/issues/49882)

    [深度学习模型训练时报错“nll\_loss\_forward\_reduce\_cuda\_kernel\_2d\_index“ not implemented for ‘Float‘问题解决 - 欣杰科技 - 博客园](https://www.cnblogs.com/xjkj/p/17688698.html)

    ```shell
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [26,0,0] Assertion `t >= 0 && t < n_classes` failed.
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [27,0,0] Assertion `t >= 0 && t < n_classes` failed.
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [28,0,0] Assertion `t >= 0 && t < n_classes` failed.
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [29,0,0] Assertion `t >= 0 && t < n_classes` failed.
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [30,0,0] Assertion `t >= 0 && t < n_classes` failed.
    ../aten/src/ATen/native/cuda/Loss.cu:271: nll_loss_forward_reduce_cuda_kernel_2d: block: [0,0,0], thread: [31,0,0] Assertion `t >= 0 && t < n_classes` failed.

    Test Iter:  140/ 143. Data: 0.313s. Batch: 0.342s. Loss: 3.9630. top1: 6.09. top5: 22.77. :  98%|█████████▊| 140/143 [00:56<00:01,  2.48it/s]
    Traceback (most recent call last):
    File "./train.py", line 533, in <module>
        main()
    File "./train.py", line 314, in main
        train(args, labeled_trainloader, unlabeled_trainloader, test_loader,
    File "./train.py", line 450, in train
        test_loss, test_acc = test(args, test_loader, test_model, epoch)
    File "./train.py", line 508, in test
        losses.update(loss.item(), inputs.shape[0])
    RuntimeError: CUDA error: device-side assert triggered
    CUDA kernel errors might be asynchronously reported at some other API call,so the stacktrace below might be incorrect.
    ```
