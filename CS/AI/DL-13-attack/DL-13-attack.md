# 13 | DL攻防
## Adversarial ML
[Adversarial Machine Learning (AML, 对抗机器学习）技术调研 - 知乎](https://zhuanlan.zhihu.com/p/135374750)
make the model more robust


l1 norm: absolute value of the difference between the two vectors

l2 norm: square root of the sum of the squares of the differences between the two vectors



linear classifier: a function that maps an input to a class label

important factors:
- the choice of the loss function
- the quality of the features

decision boundary: the line that separates the classes





CV tasks:
- classification
- classification+localization
- object detection
- instance segmentation

active security threats
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240919152147.png)

passive security threats
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240919152207.png)

Evasion/adversarial example attacks: adversary crafts
adversarial examples that evade detection (spam email marked as ham)

Poisoning/backdoor attacks: adversary inserts emails that contain spam but removes them from the spam folder back to inbox

Membership inference: adversary inspects model to test whether an email was used to train it (privacy violation)

Model extraction: adversary observes predictions and
reconstructs model locally


## solutions

### Adversarial Training
Learning the model parameters using adversarial samples is referred to as adversarial training
### Random Resizing and Padding
Model training with randomly resizing the image and applying random padding on all four sides have shown to improve the robustness to adversarial attacks

隐藏梯度(gradient masking)：由于大多数攻击算法都是基于分类器的梯度信息，因此掩蔽或混淆梯度会混淆攻击机制。
鲁棒性优化(robust optimization): 这类研究展示了如何训练一个鲁棒的分类器，可以正确地分类对抗样本。
对抗检测(adversary detection): 这类方法试图在将样本输入深度学习模型之前，检查一个样本是良性的还是对抗的。