
# 01 | 机器学习导论

!!! note "课程信息"
    === "机器学习"
        - 课程时间：2024年秋冬
        - 课程教师：赵洲
        - 考核内容：2次书面作业+2次编程作业[Kaggle](https://www.kaggle.com/)（45%）+15次随机签到（15%）+1次期末摸底考试+1次期末考试；（40%）
        - 课本：西瓜书
    === "实用的机器学习"

    === "人工智能与安全"
        - 课程时间：2024年秋冬
        - 课程教师：陈艳姣
        - workload：


Artificial Intelligence is a scientific field concerned with the development of algorithms that allow computers to learn without being explicitly programmed

• Machine Learning is a branch of Artificial Intelligence, which focuses on
methods that learn from data and make predictions on unseen data

[人工智能基础 - 鹤翔万里的笔记本 (tonycrane.cc)](https://note.tonycrane.cc/cs/ai/basic/)

[02：贝叶斯定理 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/ML/统计机器学习02：贝叶斯定理/)

[命题逻辑 - Jerry's Blog (wxxcl.tech)](https://blog.wxxcl.tech/course/aid/知识表达与推理/命题逻辑/)

[笔记](https://github.com/mura1n/Machine-Learning-in-Practice-Crash-Course-Notes)


1. 机器学习：B站/youtube 李宏毅/吴恩达课程二选一，mo平台(https://mo.zju.edu.cn/)上似乎有课程笔记自己搜索一下，如果时间不多可以先跳过，后面再补;  如果时间特别特别充裕的话，西瓜书也可以看。
2. 深度学习：https://zh-v2.d2l.ai/ notebook和课程质量较高，使用的框架的话, pytorch文献用的比较多,tensorflow和硬件兼容性好，根据需求选择框架学习, 如果觉得难以接受可以多刷几遍
3. 强化学习：https://hrl.boyuai.com/   https://datawhalechina.github.io/easy-rl/#/ 应该比较好，但是lz不是做这个方向的，还没看过(x
之后要做什么根据自己的需求来
https://github.com/AccumulateMore 这个笔记似乎也做的比较好
B站https://space.bilibili.com/1567748478/的论文带读也挺不错



## 导论

!!! note "什么是机器学习"
    以数据作为经验的载体，利用经验数据不断提高性能的计算机系统/程序/算法

    最理想的机器学习技术是学习到 **概念** （⼈类学习，可理解的）

- supervised learning ：分类任务（离散），回归任务（连续）；学习一个映射函数$x\rightarrow \mathbf{y}$
- unsupervised learning ：找到标签或者模式，聚类、降维
- reinforcement learning：强化学习（相当于是监督学习）
  ![image-20240611173113321](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240611173113321.png)



PAC 模型

$$
P(|f(x)-y \le \epsilon|) \ge 1-\delta
$$

预测误差很小的概率大于1-δ

iid 保证了统计意义上可以使用机器学习

而$\epsilon$ 表示了泛化能力

概率近似正确：以很高的概率得到一个很接近真实值的结果

??? note "Fundamental Concepts in Machine Learning"

    === "**Sample, Instance, Example**"
        - Sample, instance, and example refer to the same concept, which is a single data point used for training or testing a machine learning model.
        - instance don't contain the label
        - example: instace + label

    === "**Feature, Representation, Predictor**"
        - A feature is an attribute or aspect of the data used to describe a data point.
        - Representation refers to the process of converting data into a form that a computer can process, such as a vector or a matrix.
        - A predictor is a model or function used to predict the target variable.
    
    === "**Label, Target, Class, Pattern Class**"
    
        - A label is the true category or value of the data, used in supervised learning.
        - A target is the variable that the model is intended to predict.
        - A pattern class is a category or grouping of data.
        - A class is a group of data points that belong to the same pattern.
    
    === "**Training Data**"
    
        - Training data is the dataset used to train the model.
        - $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ represent individual data points in the training data, where $x_i$ is the feature and $y_i$ is the label.
    
    === "**Model, Classifier, Regressor**"
    
        - A model is a mathematical structure used to describe data or predict the target.
        - A classifier is a model used for categorizing data, with a discrete output representing the category.
        - A regressor is a model used for regression analysis, with a continuous output representing the numerical value.
    
    === "**Test Data**"
    
        - Test data is the dataset used to evaluate the performance of the model.
        - $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ represent individual data points in the test data, where $x_i$ is the feature and $y_i$ is the label.
    
    === "验证集"
        训练集上用来调参数的集合

|机器学习术语|疾病诊断例子|
|---|---|
|数据集，特征，标记|某疾病患者⼈群|
|假设空间|所有可能的药|
|版本空间（跟训练集一致的“假设集合”）|能治好的药|
|归纳偏执|偏执：中药西药，副作用大小，费用高低|
|没有免费午餐|没有特效药，万能药|


**inductive bias** | 归纳偏好: 机器学习算法对于某些假设的倾向性，存在多条曲线符合数据时候，算法的倾向性叫做inductive bias

**Occam's Razor** | 奥卡姆剃刀原理：在所有可能的解释中，最简单的解释最有可能是正确的（大道至简）

!!! tip "算法的优越性来自于算法的assumption和数据的匹配程度"

**No Free Lunch Theorem**:
一个算法A在某个问题上表现比B好，比存在另一个问题，B比A好
脱离具体问题，空泛谈论“什么学习算法更好”毫无意义

脱离数据分布和输出去谈学习算法，是没有意义的

[NFL定理推导-CSDN博客](https://blog.csdn.net/qq_43246110/article/details/104617780)
### 什么时候使用机器学习

**there should be some patterns in the data**

- we know the patterns,but don't know how to use
- ML can discover the pattern themselves

机器学习是大胆假设和小心求证的折衷




### pipeline

pipeline，中文意为管线，意义等同于流水线。土味一点 你把它 翻译成 **一条龙服务**；专业一点，叫它 **综合解决方案**<br>

![image-20240614191015217](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614191015217.png)

- **定义问题**:是有监督还是无监督？是分类还是回归？
- 收集数据：
- 数据预处理 transform data & get features：找到x和y
- 创建模型（具体到模型也有相应的Pipeline,比如模型的具体构成部分：比如GCN+Attention+MLP的混合模型）
- 评估模型结果
- 模型调参

是一个**迭代**的过程

### generalization 泛化
机器学习最重要的能力就是generalization，最重要的就是要学习到一些概念

## 概率和似然

这两个概念我经常有点糊涂

所谓概率就是已知参数$\theta$的情况下，求$X$的分布



而似然是指在给定X的情况下，去预估参数$\theta$，

根据已有的数据(相当于$\textbf{X}$)学到相应的分布(即$\theta$),此概念对应training阶段, 即在训练阶段, 是根据已有的$X$来估计其真实的数据分布服从什么样的分布$\theta$
> 一个质量不均的骰子，投了很多次，求一个分布

## 性能
$经验性能E \approx 泛化性能E^*$

iid假设：训练集和测试集是独立同分布的 `identical and independently distributed`

### 定义
"**Training Error and Test Error**"
- Training error is the error alculated on the training data.
- Test error is the error calculated on the test data.

use test error to evaluate the quality of model
<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614191634130.png" alt="image-20240614191634130" style="zoom: 50%;" />

!!! tip "不同的算法就是在用不同的方式去达到平衡点"


overfitting 过拟合

更复杂的模型：更小的training error

- 优化目标，加入正则化项，使得模型更简单
- early stopping

Ridge Regression: 

$$
\min_{\omega} \sum_{i=1}^n (y_i - \omega^T x_i)^2 + \lambda \|\omega\|^2
$$
简介：岭回归



欠拟合：对训练样本的一般性质没有学好
- 决策树：拓展分支
- 神经网络：增加训练轮数
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240912105851.png)


### 评估方法
理解方法：题库出小测题目


#### **hold-out**：
- 直接将数据集划分为两个互斥集合——训练集和测试集。在划分训练集和测试集时，要尽可能保持数据分布的一致性。
- 使用分层采样（stratified sampling）方法，以保持类别比例一致。
- 一般进行若干次随机划分，重复实验并取平均值。
- 训练集和测试集的样本比例通常为2:1或4:1，效果还不错。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240912151812.png)
#### **交叉验证法**

1. 分层采样划分数据集：将数据集分层采样划分为K个大小相似的互斥子集。
2. 训练和测试：每次使用K-1个子集的并集作为训练集，剩下的一个子集作为测试集。
3. 重复实验：重复上述过程K次，每次都使用不同的子集作为测试集。
4. 计算平均值：最终返回K个测试结果的平均值
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240912152056.png)

LOO leave-one-out：留一法，最接近于理想情况，开销太大，NFL

!!! tip "猜测进教室性别问题"
    男生多猜男生，女生多猜女生

#### 自助法 bootstrap

包外估计，有36.8%不出现
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240912152608.png)

- 改变了数据的分布

#### **调参数**

- 模型参数：算法计算
- 超参数：用户提供,轮数，


### 性能度量
作为设计自己度量的一种启发

#### 回归

- MSE:
  
$$
MSE(f, \boldsymbol{\theta})=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-f\left(x_{i}, \boldsymbol{\theta}\right)\right)^{2}
$$

- MAE:

$$
MAE(f, \boldsymbol{\theta})=\frac{1}{n}\left|y_{i}-f\left(x_{i}, \boldsymbol{\theta}\right)\right|
$$







memory consumption

platform required for running 

CPU vs GPU

server,workstation

#### 混淆矩阵

先介绍一下混淆矩阵（T/F: 预测是否正确，P/N：预测是正类还是负类）
- TP：预测为正类，实际为正类，预测正确。
- FP：预测为正类，实际为负类，预测错误。
- FN：预测为负类，实际为正类，预测错误。
- TN：预测为负类，实际为负类，预测正确。



**准确率 | Accuracy**

正类和负类中预测正确的数量占总数量的占比。

$Accuracy=\frac{T P+T N}{T P+F P+F N+T N}$




=== "存在问题1"
	准确率不可导，无法作为cost function去做训练，只能用作评估。
=== "存在问题2"
	正类和负类预测正确的重要性不一样，比如对于癌症检测来说，可能负类(没有患癌症) 预测正确的数量非常大，就导致Accuracy的分子非常大，得到的Accuracy就非常大，但是可能正类(患癌症) 预测正确的数量非常小，就导致虽然模型的准确率很高，但根本检测不出癌症。
=== "存在问题3"
    如果正类样本非常多，即使不做任何学习，也可以得到很高的准确率


解决问题的方案：采用精确率或者召回率

!!! tip "查准率和查全率"
    - 查准率Precision：即你认为是True的样本中，到底有多少个样本是真为True。
    - 查全率Recall：即在预测样本中属于True的样本，你真的判断为True的有几个。

- 真阳性率（True Positive Rate，TPR）通常也被称为敏感性（Sensitivity）或召回率（Recall）。它是指分类器正确识别正例的能力。真阳性率可以理解为所有阳性群体中被检测出来的比率(1-漏诊率)，因此TPR越接近1越好。它的计算公式如下：$precision=\frac{T P}{TP+FP}$



- 假阳性率 (False Positive Rate, FPR)
假阳性率（False Positive Rate，FPR）是指在所有实际为负例的样本中，模型错误地预测为正例的样本比例。假阳性率可以理解为所有阴性群体中被检测出来阳性的比率(误诊率)，因此FPR越接近0越好。它的计算公式如下 FP = \frac{FP}{FP+TN}

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240909154344.png)

[P-R曲线绘制原理及代码实现\_求p-r曲线的代码-CSDN博客](https://blog.csdn.net/weixin_43298886/article/details/110696655)


F1 度量：

$F 1=\frac{2 \times \text { precision } \times \text { recall }}{\text { precision }+\text { recall }} = 、\frac{2\times TP}{总数 + TP -TN}$

!!! tip "F1是P和R的调和平均"

对查准率、查全率有不同的偏好
$F_\beta = \frac{(1+\beta^2)\times P\times R}{(\beta^2 \times P) + R}$
$\beta = 1$:标准F1

$\beta > 1$:偏重查全率（逃犯信息检索）

$\beta < 1$:偏重查准率，商品推荐系统

#### ROC & AUC
绘制方法：给定$m^+$个正样本和$m^-$个负样本，对于每个样本，计算其预测概率，然后按照概率从大到小排序，然后逐个样本计算TP rate和FP rate，然后绘制ROC曲线。

预测准确，增加y值；预测错误，增加x值；

---

**AUC**

AUC（ROC曲线下面积）是ROC曲线下的面积，用于衡量分类器性能。AUC值越接近1，表示分类器性能越好；反之，AUC值越接近0，表示分类器性能越差。在实际应用中，我们常常通过计算AUC值来评估分类器的性能。

理论上，完美的分类器的AUC值为1，而随机分类器的AUC值为0.5。这是因为完美的分类器将所有的正例和负例完全正确地分类，而随机分类器将正例和负例的分类结果随机分布在ROC曲线上。

综上，ROC曲线和AUC值是用于评估二分类模型性能的两个重要指标。通过ROC曲线，我们可以直观地了解分类器在不同阈值下的性能；而通过AUC值，我们可以对分类器的整体性能进行量化评估。

### 性能评价

- 测试性能不等于泛化性能
- 测试性能随着测试集的变化而变化

假设检验：
有多少把握在统计意义上说这个模型是好的




### bias and variance decomposition
偏差 & 方差

- bias: 最好的模型和ground truth之间的差距;模型的上限; training error
- variance: 最优的模型和最差的模型之间的差距；模型的下限; the difference between training error and test error

prediction error = bias + variance + noise

- high bias, low variance: underfitting
- low bias, high variance: overfitting
- low bias, low variance: good model


改进策略

underfitting:
- add more features
- use more complex model
- descrease regularization

overfitting:
- decrease model complexity
- decrease number of features
- add more regularization
- add more data
!!! note "train val test"
    60% 20% 20%
    - training set: train the model
    - validation set: tune the hyperparameters
    - test set: evaluate the model



## 学习资源

[Machine Learning in Practice Crash Course | Jinming Hu (conanhujinming.github.io)](https://conanhujinming.github.io/post/ml_in_practice_crash_course/)

[实用的机器学习 第一课 机器学习导论 2024summer_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Gw4m1i7ys/?spm_id_from=333.788.recommend_more_video.0&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[机器学习2023-10-19第6-8节 (zju.edu.cn)](https://classroom.zju.edu.cn/livingpage?course_id=53449&sub_id=915451&tenant_code=112)








[有监督的机器学习：回归与分类 | Coursera](https://www.coursera.org/learn/machine-learning?action=enroll)

[CS229吴恩达机器学习](https://www.bilibili.com/video/BV16J411t71N)

[CS229: Machine Learning (stanford.edu)](https://cs229.stanford.edu/)



深度学习

[CS231n Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/)：deep learning for CV

[图灵班《机器学习》课程总结 - CC98论坛](https://www.cc98.org/topic/5599897)

我在心灵学ML系列doge

[再次入门deep learning以及一些回忆（更新第二部分） - CC98论坛](https://www.cc98.org/topic/5207160)

[再次入门deep learning，这次直接上重点（完结篇） - CC98论坛](https://www.cc98.org/topic/5208795)






### 会议论文
- ICML (International Conference on Machine
Learning)
- NeurIPS (Neural Information Processing Systems)
- KDD (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)
- AAAI (AAAI conference on Artificial Intelligence)

本人农学博士，科研接触的机器学习，之前有计算机的导师领入门了。个人目前遇到最好的教程是吴恩达的视频课程，因为他充分考虑到了学生的水平，把需要的数学知识也讲了，先看了吴恩达早期的机器学习（反向传播的那节讲的不是很好），然后近两年的深度学习，在看了b站北大的tensorflow笔记课程，觉得至少知道该怎么做机器学习（包括深度学习）了。 不过作为一个非计算机专业的学生，个人觉得所有的教程都忽视了一个最基础但是也是最重要的东西——**特征工程**，指的不是特征选择（无监督学习的降维），而是特征表征（feature represent），深度学习里面叫embedding（自己看了功能后理解的），就是我们应该怎样去表征问题，将问题的信息表示为数据给计算机进行学习。之前看了什么有监督学习啊，无监督学习啊，对特征就是告诉你样本或向量空间，完全不知道机器学习去做什么。只到有个老师让我在做了特征提取，然后降维，然后分类或预测的时候我才明白机器学习是一个什么样的过程。



我是入门看的咱们学校的机器学习课程，对机器学习大概有个了解，没太关心数学。 说实话这些算法（ml里不包含dl的那些）我科研上用到的比较少，后来随着科研的深入会去思考这些算法后面的数学原理，就去参考李航的机器学习，西瓜书。更加高屋建瓴一点的教材就是PRML了。 我比较推荐UCB的CS188，从整个人工智能的角度讲问题，机器学习是其中的一个部分。编程项目有趣连贯。用的教材也是经典，一些思想现在也不过时。



pipeline

完成实用机器学习的所有作业

完成赵洲老师的所有作业+大作业

