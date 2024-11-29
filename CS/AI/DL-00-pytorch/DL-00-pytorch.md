# Pytorch

| 模式 | 前向传播 | 反向传播 | 参数更新 | Dropout 层行为 | BatchNorm 层行为 |
| --- | --- | --- | --- | --- | --- |
| 训练模式（Training Mode） | 是 | 是 | 是 | 随机将一部分神经元关闭，以防止过拟合 | 使用每一批数据的均值和方差进行归一化处理 |
| 评估模式（Evaluation Mode） | 是 | 否 | 否 | 关闭所有神经元，不再进行随机舍弃 | 使用在训练阶段计算得到的全局统计数据进行归一化处理 |



[【小白学PyTorch】5 torchvision预训练模型与数据集全览 - 知乎](https://zhuanlan.zhihu.com/p/209276308)

[Models and pre-trained weights — Torchvision 0.20 documentation](https://pytorch.org/vision/stable/models.html)