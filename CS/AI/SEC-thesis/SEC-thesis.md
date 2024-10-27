# Zero-Query Adversarial Attack on Black-box Automatic Speech Recognition Systems

[珞珈学子成果被ACM CCS 2024录用-武汉大学新闻网](https://news.whu.edu.cn/info/1015/455257.htm)

[Zero-Query Adversarial Attack on Black-box Automatic Speech Recognition Systems](https://arxiv.org/html/2406.19311v1)

## 论文内容

## 概念辨析
迁移性：假设对抗样本具有迁移性，即当一个对抗样本可以成功攻击一个模型时，它也很有可能成功攻击另一个相似的模型。

替代模型：当我们想对一个平台提供的黑盒模型进行攻击时，一种可行的方法是先训练一个与目标模型具有相似决策边界的本地模型，之后对本地模型进行白盒攻击得到对抗样本，再利用迁移性实现对目标模型的攻击，这个部署在本地的模型即为替代模型。


### Black Box

### ASR | Automatic Speech Recognition Systems


作者研究发现，当前的智能语音识别系统主要基于注意力机制或卷积神经网络两类深度学习模型实现。


### 端到端
端到端模型直接将原始数据作为输出返回输出结果，非端到端模型需要使用经过数据处理后的处理数据作为模型输入


## 现有难点
- 目标模型是个黑盒，我们得不到相关的模型结构、参数或者训练数据；
- 在使用目标模型进行图像分类时，通常只能得到该图像的唯一标签，并且没有准确率；
- 调用API接口的查询次数有限，过多的查询除了带来成本上的负担外，还有可能被平台的异常检测程序制裁。

语音系统需要处理时间维度上的信息变化，这比图像分类系统要复杂得多。其次，音频采样率通常很高（例如16kHz，这意味着每秒采样16,000个点），但是图像总共只有数百/数千个像素（例如，最流行的数据集中图像的大小，即，MNIST和CIFAR-10，分别为28×28和32×32）。因此，与图像相比，制作对抗性音频更加困难，因为向音频添加少量噪声不太可能影响局部特征。

不可察觉性质

## 解决方案
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241027183631.png)

### 多替代模型
既用CNN 又用transformer

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241027183654.png)

### 初始化

在此基础上，作者提出了动态的对抗扰动初始化方法

对所有代理ASR，求解最优的padding

在音量较大的部分，允许的扰动更大，而在音量较小的部分，扰动被严格限制，从而减少了人耳对小扰动的察觉。这种自适应扰动可以减少对原音频的可感知干扰。

### 集成优化

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241027183827.png)


序列化的集成优化算法

考虑每个之间的影响

- 外环：每次对进行交换
- 内环


### loss function
考虑了三重因素，加权求和
- adversial attack
- 不可感知
- 特征提取


## 实验设计