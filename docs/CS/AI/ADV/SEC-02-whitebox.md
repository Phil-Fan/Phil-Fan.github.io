

## Boundary Attack
[机器学习里的攻击-躲避攻击(Evasion attacks)-CSDN博客](https://blog.csdn.net/weixin_42468475/article/details/111684668)
### 样本生成方式
#### 基于梯度的攻击
基于梯度的攻击是最常见也是最容易成功的一种攻击方法。它的核心思想可以用一句话来概括：以输入图像为起点，在损失函数的梯度方向上修改图像。

执行此类攻击主要有两种方法：

一次攻击(One-shot Attacks)：攻击者在梯度方向上迈出一步，如FGSM、 T-FGSM

迭代攻击(Iterative attacks)：攻击者在梯度方向迈出多步，逐渐调整，如I-FGSM
d
#### FGSD（Fast gradient sign method）
这是一种基于梯度生成对抗样本的算法，其训练目标是最大化损失函数 ​ 以获取对抗样本​，其中 ​ 是分类算法中衡量分类误差的损失函数，通常取交叉熵损失。最大化 ​ 即时添加噪声后的样本不再属于该类，由此则达到了上图所示的目的。在整个优化过程中，需满足 ​ 约束 ​，即原始样本与对抗样本的误差要在一定范围之内。


## gradient-based 
## score-based
## transfer-based attacks


