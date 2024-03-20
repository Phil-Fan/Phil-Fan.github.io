# HPE领域综述

[【万字长文！人体姿态估计(HPE)入门教程】 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/596043913)

[人体姿态估计的过去，现在，未来 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/85506259)

??? note "基本信息"
    题目 ：**Vision-Based Human Pose Estimation via Deep Learning: A Survey**<br>
    Author ：[Gongjin Lan](https://arxiv.org/search/cs?searchtype=author&query=Lan,+G), [Yu Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Y), [Fei Hu](https://arxiv.org/search/cs?searchtype=author&query=Hu,+F), [Qi Hao](https://arxiv.org/search/cs?searchtype=author&query=Hao,+Q)<br>
    arXiv地址：[Vision-Based Human Pose Estimation via Deep Learning: A Survey (arxiv.org)](https://arxiv.org/abs/2308.13872)<br>

![image-20240318194903268](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318194903268.png)

## 名词解释

regression paradigm

### Deep learning

#### CNN(`Convolutional Neural Networks`)

AlexNet

ResNet

CNN在HPE任务中通常分为两个主要部分：

1. **骨干网络（Backbone Network）**：这是CNN的第一部分，通常采用现成的、经过预训练的通用网络模型来提取图像的特征。例如，ResNet是一个非常常用的骨干网络，它通过深层的卷积层学习图像中的高级特征。这些特征包含了图像中重要的视觉信息，为后续的姿态预测提供基础。

2. **预测头（Prediction Head）**：这是CNN的第二部分，负责使用骨干网络提取出的特征来预测人体的姿态。预测头的设计和实现方式可以有很多种，但它的主要任务是根据输入图像的特征，确定图像中人体各个关节的位置。

   1. 回归范式（直接预测关节坐标）在回归范式中，模型直接从输入图像预测出每个关节的坐标。这种方法通常采用全连接层（fully connected layers）来对具体的关键点坐标进行回归。这意味着模型输出的是一个坐标列表，每个坐标代表一个关节在图像中的位置。

      **举例**：假设我们想要从一张人体图像中预测头部、肩膀、肘部和手腕的位置，使用回归范式的模型将直接输出这些部位的x和y坐标值，例如，头部可能被预测为(100, 50)，肩膀为(120, 80)，等等。

   2. 热图预测范式（生成热图后计算关节坐标）热图预测范式先生成每个关节的热图表示，然后从这些热图中计算出关节坐标。热图是一种概率分布图，表示了关节出现在图像不同位置的可能性。在生成热图之后，通过某种方式（通常是找到热图中的最大值点）来确定关节的最终坐标。为了提高热图的分辨率，常用的操作是上采样（`upsampling`）。

      **举例**：使用热图预测范式来估计同样的头部、肩膀、肘部和手腕的位置时，模型首先为每个关节生成一张热图。例如，头部的热图中最亮的点（最大概率值所在点）位于(102, 48)，这个点就被认为是头部的预测位置。肩膀、肘部和手腕也以同样的方式从它们各自的热图中确定位置。

#### RNN(`Recurrent Neural Networks`)

They are widely used in video-based HPE by considering videos as sequential RGB images.

#### GCN(`Graph Convolutional Networks`) 

GCNs are generally expected to better exploit the relationship among key points and used for the pose refinement, joint association, 2D-to-3D pose lifting

### 方法解释

**自上而下（Top-down）方法：**

1. **流程**：首先通过人体检测器在图像中识别出每个人的位置，即为每个人生成一个边界框（bounding box），然后对每个检测到的人体边界框内的图像进行单人姿态估计。
2. **优点**：通常能提供较高的姿态估计精度，因为每个人体被单独处理，避免了不同人之间的姿态混淆。
3. **缺点**：计算量随着人数的增加而线性增加，因此在人数较多的场景中效率较低。人体检测的准确性直接影响姿态估计的结果。
4. **适用场景**：对精度要求较高的应用，如需要精细分析每个人姿态的场合。

**自下而上（Bottom-up）方法：**

1. **流程**：首先在整个图像范围内直接检测所有的人体关节点，然后使用某种算法（如图匹配、聚类等）将这些检测到的关节点根据归属分配到不同的人体上。
2. **优点**：不需要先进行人体检测，直接在图像上识别关节点，因此计算量不直接随人数增加而增加，适合于处理大规模人群的场景，具有更高的效率。
3. **缺点**：在关节点分配和人体实例的区分上可能面临更大的挑战，尤其是在人体密集或严重遮挡的场景中，可能导致精度略低于自上而下方法。
4. **适用场景**：适用于人群密集的场景，或需要实时处理的应用中。

### 主流数据集和技巧

![image-20240318203018496](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240318203018496.png)

## 2D HPE

### 单人图像





### 多人图像





### 2D视频





### 鲁棒性分析





## 3D HPE



## 应用领域

