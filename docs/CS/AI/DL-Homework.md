# 人工智能与机器学习 作业


## 简介
人工智能与机器学习是控院臭名昭著的课程。在Mo实验平台上有4个个人作业，和一个小组作业。
小组作业有些班级是需要在Mo平台完成后，再在班级上进行小组ppt展示

2021级应该是选黑白棋的人最多，22级选黑白棋的人稍微少一点，但是也挺多的。

做完这几个实验的感觉就是完全没有必要浪费时间在上面，因为Mo平台的体验完全不如隔壁Kaggle，又因为是HUAWEI开发的，有些题目还要用HUAWEI的mindspore架构。

最主要的是，mo的评分方式是在线运行后评测的，所以每次评测都需要重新跑一遍，非常浪费时间。

个人作业网上可以找到的资料还挺多的


## Mo平台指北

### 如何删除文件

Mo平台应该使用的是一个Jupyter Notebook，因为用户名是jovyan

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241227103802.png)

但是平台应该在前端限制了一些操作，比如说删除`main.ipynb`和`results`文件夹就是被限制的。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241227104321.png)

所以就需要使用命令行来删除文件。

```bash title="删除文件,注意备份！！！谨慎使用"
rm -rf main.ipynb
rm -rf results/
```


### 如何下载到本地

```bash title="压缩所有文件"
zip -r main.zip ./*
```

```bash title="解压文件"
unzip main.zip
```


```bash title="下载文件"
scp main.zip <username>@<ip>:<path>
```
这里也可以右键直接下载压缩包

```bash title="上传文件"
scp <username>@<ip>:<path> <path> 
```

这里需要有一些使用ssh的经验

### 如何使用GPU进行训练

我用它这个GPU训练比较少，一般都是在自己的GPU下进行训练，参考

点击上方的按钮可以进入到这个界面
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241227110225.png)
选择使用GPU进行训练，选择相关的文件就可以开始训练了

### 如何测试
点击测试，会让你选择用到的文件，一般无脑全选就行，有些时候需要取消选择没有用到的架构（比如`torch_py`）

如果需要提交的话，需要主目录下有`程序报告.pdf`文件，只有一次提交机会

由于不知道后台的评分机制，所以不清楚直接`touch 程序报告.pdf`是否会影响最后的分数


### 卡住了怎么办

我在使用的过程中遇到了完全卡在页面上，点不了任何文件的问题(edge浏览器)

换成了chorme浏览器，问题解决



## 手写数字识别和垃圾分类
!!! note "题目"
    LeNet5 + MNIST 被誉为深度学习领域的 “Hello world”。本实验主要介绍使用 MindSpore 在 MNIST 手写数字数据集上开发和训练一个 LeNet5 模型，并验证模型精度。

    通过以上学习，使用MindSpore 深度学习框架实现26种垃圾进行分类。

    MindSpore 是最佳匹配 Ascend（昇腾）芯片的开源 AI 计算框架，同时也支持 CPU、GPU 平台。访问MindSpore 官网了解更多：https://www.mindspore.cn/

    深度学习计算中，从头开始训练一个实用的模型通常非常耗时，需要大量计算能力。常用的数据如 OpenImage、ImageNet、VOC、COCO 等公开大型数据集，规模达到几十万甚至超过上百万张。网络和开源社区上通常会提供这些数据集上预训练好的模型。大部分细分领域任务在训练网络模型时，如果不使用预训练模型而从头开始训练网络，不仅耗时，且模型容易陷入局部极小值和过拟合。因此大部分任务都会选择预训练模型，在其上做微调（也称为 Fine-Tune）。

    本实验以 MobileNetV2+ 垃圾分类数据集为例，主要介绍如在使用 MindSpore 在 CPU/GPU 平台上进行 Fine-Tune。

这个题目使用的是MobileNetV2，然后使用MindSpore框架

不太喜欢这个框架，所以使用了自己的结构

因为另一门课程有作业也是分类任务，所以这里使用了pytorch的架构

进行了一些训练，最后使用的是timm库中`seresnext50_32x4d.racm_in1k`这个模型进行微调的。

使用了4：1的训练集和测试集，训练出了两个模型，做bagging集成学习

达到了92%的准确率
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/2024-12-22-14-00-25.png)

经过同学提醒，predict中输入的图像颜色通道是反的，所以需要将BGR变成RGB


```python title="换通道"
image = Image.fromarray(np.array(image)[:, :, ::-1])
```

切换以后，模型在测试上达到了100%的准确率

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/2024-12-22-13-59-45.png)

```python title="main.py"
import torch
from PIL import Image
import torchvision.transforms as transforms
import torch.nn as nn
import os
import numpy as np
os.system(f'pip install timm') # 注意这里需要安装timm
os.system(f'pip install ttach')
import timm
import ttach as tta
inverted = {
    0: 'Plastic Bottle', 1: 'Hats', 2: 'Newspaper', 3: 'Cans', 4: 'Glassware', 5: 'Glass Bottle',
    6: 'Cardboard', 7: 'Basketball', 8: 'Paper', 9: 'Metalware', 10: 'Disposable Chopsticks',
    11: 'Lighter', 12: 'Broom', 13: 'Old Mirror', 14: 'Toothbrush', 15: 'Dirty Cloth', 16: 'Seashell',
    17: 'Ceramic Bowl', 18: 'Paint bucket', 19: 'Battery', 20: 'Fluorescent lamp', 21: 'Tablet capsules',
    22: 'Orange Peel', 23: 'Vegetable Leaf', 24: 'Eggshell', 25: 'Banana Peel'
}

# 全局，加载模型，避免每一次都加载浪费时间
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model_1 = timm.create_model('seresnext50_32x4d.racm_in1k', pretrained=False)
model_1.fc = nn.Linear(model_1.num_features, 26)
model_1.load_state_dict(torch.load('model_sere.pth', map_location=device)['state_dict'])
model_1 = model_1.to(device)


model_2 = timm.create_model('seresnext50_32x4d.racm_in1k', pretrained=False)
model_2.fc = nn.Linear(model_2.num_features, 26)
model_2.load_state_dict(torch.load('model2.pth', map_location=device)['state_dict'])
model_2 = model_2.to(device)

def predict(image):
    # 如果输入是numpy数组,转换为PIL Image
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    # 确保图像是RGB模式
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = Image.fromarray(np.array(image)[:, :, ::-1])
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]) # 这个是imagenet的均值和方差
    ])
    imgs = transform(image).unsqueeze(0).to(device)
    
    model_1.eval()
    model_2.eval()

    tta_model_1 = tta.ClassificationTTAWrapper(model_1, tta.aliases.flip_transform(), merge_mode='mean')
    tta_model_2 = tta.ClassificationTTAWrapper(model_2, tta.aliases.flip_transform(), merge_mode='mean')

    with torch.no_grad():
        logits_1 = tta_model_1(imgs.to(device))  #预测
        logits_2 = tta_model_2(imgs.to(device))
        logits = logits_1 + logits_2 # 做bagging集成学习
        return inverted[logits.argmax(dim=-1).cpu().numpy().item()]
```

```python title="train.py"
# 之后整理一下再放
```


### 感想
训练比较耗时间，测试也很耗时间
大概搞了3天左右（包括树叶分类的作业）


## 口罩检测
[Search | Kaggle](https://www.kaggle.com/search?q=Masked+face+recognition+in%3Adatasets)

[X-zhangyang/Real-World-Masked-Face-Dataset: Real-World Masked Face Dataset，口罩人脸数据集](https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset/tree/master?tab=readme-ov-file)

[[2003.09093] Masked Face Recognition Dataset and Application](https://arxiv.org/abs/2003.09093)

[NKU-share/人工智能导论 at b60b98043f55257e1e74fc1aa1b7fc5ccbead370 · Starlight0798/NKU-share](https://github.com/Starlight0798/NKU-share/tree/b60b98043f55257e1e74fc1aa1b7fc5ccbead370/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%AF%BC%E8%AE%BA)

[一个基于resnet的口罩检测图片分类（自定义数据集）\_口罩分割数据集-CSDN博客](https://blog.csdn.net/liningxi123/article/details/136702365)



## 作家风格识别
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





