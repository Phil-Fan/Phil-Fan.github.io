# 机器学习导论

[人工智能基础 - 鹤翔万里的笔记本 (tonycrane.cc)](https://note.tonycrane.cc/cs/ai/basic/)

[02：贝叶斯定理 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/ML/统计机器学习02：贝叶斯定理/)

[命题逻辑 - Jerry's Blog (wxxcl.tech)](https://blog.wxxcl.tech/course/aid/知识表达与推理/命题逻辑/)

[笔记](https://github.com/mura1n/Machine-Learning-in-Practice-Crash-Course-Notes)

## 导论

!!! note "什么是机器学习"
    自动从数据中学习提高系统能力

- supervised learning ：分类任务（离散），回归任务（连续）；学习一个映射函数$x\rightarrow \mathbf{y}$
- unsupervised learning ：找到标签或者模式，聚类、降维
- reinforcement learning：强化学习（相当于是监督学习）
  ![image-20240611173113321](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240611173113321.png)

??? note "Fundamental Concepts in Machine Learning"

    === "**Sample, Instance, Example**"
        - Sample, instance, and example refer to the same concept, which is a single data point used for training or testing a machine learning model.

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
    
    === "**Training Error and Test Error**"
    
        - Training error is the error calculated on the training data.
        - Test error is the error calculated on the test data.
    
        use test error to evaluate the quality of model

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614191634130.png" alt="image-20240614191634130" style="zoom: 50%;" />

overfitting 过拟合

更复杂的模型：更小的training error





### 什么时候使用机器学习

**there should be some patterns in the data**

- we know the patterns,but don't know how to use
- ML can discover the pattern themselves



### pipeline

pipeline，中文意为管线，意义等同于流水线。<br>
一个生动的形容<br>
Pipeline，你 土味一点 你把它 翻译成 **一条龙服务**<br>
专业一点，叫 它 **综合解决方案**，就行。<br>

![image-20240614191015217](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614191015217.png)

- **定义问题**:是有监督还是无监督？是分类还是回归？
- 收集数据：
- 数据预处理 transform data & get features：找到x和y
- 创建模型（具体到模型也有相应的Pipeline,比如模型的具体构成部分：比如GCN+Attention+MLP的混合模型）
- 评估模型结果
- 模型调参

是一个**迭代**的过程



## metric

### 分类

先介绍一下混淆矩阵（T/F: 预测是否正确，P/N：预测是正类还是负类）
- TP：预测为正类，实际为正类，预测正确。
- FP：预测为正类，实际为负类，预测错误。
- FN：预测为负类，实际为正类，预测错误。
- TN：预测为负类，实际为负类，预测正确。



**准确率 | Accuracy**

正类和负类中预测正确的数量占总数量的占比。$Accuracy=\frac{T P+T N}{T P+F P+F N+T N}$

=== "存在问题1"
	准确率不可导，无法作为cost function去做训练，只能用作评估。
=== "存在问题2"
	正类和负类预测正确的重要性不一样，比如对于癌症检测来说，可能负类(没有患癌症) 预测正确的数量非常大，就导致Accuracy的分子非常大，得到的Accuracy就非常大，但是可能正类(患癌症) 预测正确的数量非常小，就导致虽然模型的准确率很高，但根本检测不出癌症。

解决问题的方案：采用精确率或者召回率
- 精确率：预测为正类的样本中预测正确的比例。$precision=\frac{T P}{T P+F P}$

- 召回率：实际为正类的样本中，被预测正确的正类的比例。$recall=\frac{T P}{T P+F N}$



### 回归

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



![image-20240614200543795](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614200543795.png)

more closed to the realistic world



## 贝叶斯决策

### 问题与定义

$x$ sample

$y$ state of the nature

$P(y|x)$ given $x$​​,what is the probability of the state of the nature





条件概率：
$$
P(A|B) = \frac{P(A,B)}{P(B)}
$$




**先验概率 | `prior`**: $P(A)$​the probability A being True. this is the knowledge

反映了我们关注的标签在自然界中(无人为干预的情况下)的数量分布情况（在某个特征下也可以）。例如：我们可以看在 lightness 特征条件下See bass和salmon这两个标签的数量情况。更简单的来讲，先验就是在我们不知情的情况下猜测的标签种类。（我们倾向于猜测炸弹不会爆炸，因为其先验概率很小）

- 如果没有先验概率的情况下，我们可能会认为salmon和sea bass的捕捉概率是相等的。这种假设并不适用于任何情况。$P(y_{1} )=P(y_{2} )$

- 如果是二分类问题$P(y_{1} )+P(y_{2} )=1$
- 如果只根据先验信息进行决策
    - 即如果y1的概率大于y2则认为是y1，否则就是y2.
    - 先验概率不一定准确，没有用到事物本身的feature，纯在猜测。

**似然性 | `likelihood`**: $P(B|A)$​the probability of B being true,given A is true

!!! note "概率和似然"
	**概率：** 在一件事的结果未知的情况下，通过事件自身的性质估计事件各个结果的可能性的大小，就是事件各个结果发生的概率。（抛硬币：硬币有两面，所以两面分别朝上的概率都是百分之五十，概率只有在事件发生前是有意义的，因为当硬币抛出后，结果就已经确定了。）<br>
	**似然：** 基于事件已经确定的结果来推测产生这个结果的可能环境（环境中的某些参数）。（抛硬币：直接抛硬币10000次，其中8000次正面朝上，2000次反面朝上，我们会认为硬币的构造比较特殊，进而推测该硬币的具体参数）



**后验概率 | `posterior`**: $P(A|B)$​

贝叶斯定理
$$
P(A|B) = P(A)\frac{P(B|A)}{P(B)}
$$

$$
[后验概率] = [先验概率]\times[后验概率]
$$

[【官方双语】贝叶斯定理，使概率论直觉化_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1R7411a76r)

> rationality is not about knowing facts, it's about recognizing which facts are relevant
>
> 新证据不能直接决定看法，而是应该更新你的观点








最大似然概率决策 MLE

$$
P(y_i|x) = \frac{P(x|y_i) P(y_i)}{P(x)}
$$


**Bayes Decision Rule**

Decide $y_1$, if $P(y_1|x)> P(y_2|x)$,otherwise $y_2$

> 因为$P(x)$与类别$y_i$无关，所以可以省略

**最小化错误概率**

最小错误其实和最大后验概率是等价的，因为最小错误就是最大化后验概率。（使用二分类来理解）

[例子](https://blog.csdn.net/Harry_Jack/article/details/111242672)



### Bayesian Risk | 贝叶斯风险

> 并不是所有的错误代价都是相同的

如果将两个类别互相识别错误的风险相当的前提下，类别只需要比较两者的后验概率即可，就与之前绘制直方图类似。如果两者不相等，则需要依据风险函数比较大小进行类别判定。

$$
\begin{align*}
E_{ij} = E(\hat{y_i}|y_j)\\
R(\hat{y_1}|x) = E_{11} P(y_1|x)+E_{12}P(y_2|x) = E_{12}P(y_2|x)\\
R(\hat{y_2}|x) = E_{21} P(y_1|x)+E_{22}P(y_2|x) = E_{21}P(y_1|x)\\
\end{align*}
$$

决策方法：选风险最小的，decide $y_1$ if $R(\hat{y_1}|x) < R(\hat{y_2}|x)$

- 二分类中：当 likelihood ratio 超过某个与x无关的阈值时候，就做决策

$$
\begin{align*}
E_{21}P(x|y_1)P(y_1) > E_{12}P(x|y_2)P(y_2)\\
\frac{P(x|y_1)}{P(x|y_2)} > \frac{E_{12}P(y_2)}{E_{21}P(y_1)}\\
\end{align*}
$$

> 如果$E_{12} = E_{21}$​，最小化风险函数Risk就是最大化后验概率P(yi|x)
>
> 你会觉得要让等式左边的R越小，等式右边的P不是也该越小吗？为什么要最大化呢？仔细看下表你就会发现R中的$\hat{y}$的下标和P中的$y$的下标是不一样的，你要$\hat{y_1}$的Risk值越小，$\hat{y_2}$对应的P值就越小，$y_1$对应的P值就应该越大，所以确实是given x条件下$y_1$的后验概率越大

- 多分类的情况：seek a decision rule that minimizes the probability of error or maximizes the accuracy;

$$
\begin{align*}
    E(\hat{y_i}|y_j) = \begin{cases}
    0 & if\ i=j\\
    1 & if\ i\ne j
    \end{cases}
\end{align*}
$$



### 回顾

贝叶斯的框架
- 知道先验概率P(yi)，知道似然P(x|yi)，我们就可以得到一个最优的分类器。
- 现实生活中，很难获取到准确的似然的信息（特征维度太高或者特征并不充分）。
- 常用的做法：利用训练数据去估计出先验概率和似然，再去做贝叶斯决策。

classifier assigns a feature when:

$$
g_i(x) > g_j(x), \forall j \neq i
$$



![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240630201905.png)
中间的节点是一个分类器

- 判别函数是先验
- 判别函数是后验：贝叶斯决策
- 似然函数：极大似然估计
- 期望风险最小化：贝叶斯风险





**Decision Regions and surfaces**

- learning 的过程其实就是将feature space 分成不同的 decision regions
- 现实生活中，由于只能从有限的样本中学习，所以只能得到likelihood和先验的估计值

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240630210634705.png" alt="image-20240630210634705" style="zoom:33%;" />

**离散形式极大似然估计**

- 先验概率：将频率估计为概率$P\left(y_{k}\right)=\frac{N_{y_{k}}}{N}$

- 似然：在类别为$y_k$的样本中特征为$x_i$样本的占比。$P\left(x_{i} \mid y_{k}\right)=\frac{\left|x_{i k}\right|}{N_{y_{k}}}$
  

**连续形式极大似然估计**

- discretize: the range into bins，对于体重来说，可以50-100kg，100-150kg，150-200kg。再将数据段离散成不同的类别即可。
- two-way split: 暴力分为两个段，设置一个中间值，小于中间值的设为一类，大于中间值的设为另一类。
- Probability Density estimation: assume attribute follows a normal distribution or some other distribution



### 朴素贝叶斯

curse of dimensionality: feature space becomes sparse 

假设特征之间是独立的

$$
\begin{align*}
    P(y|x_1,\dots,x_p) \propto  P(x_1,\dots,x_p | y) P(y)= P(y)P(x_1|y)P(x_2|y)\dots P(x_p|y)\\
\end{align*}
$$

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240630201709.png)

好处：
- robust to isolated noise points
- can handle missing values
- robust to irrelevant features
- 可解释性非常好
- 计算量非常小
- 在实践中表现好的原因：数据中的特征之间的关系很弱；或者就算等式两侧不相等，其大小的相对关系仍然是一致的

问题：
- 上述假设在实际中可能并不成立
- float point underflow
- 0 probability
  - smoothing: $P(x_i| y_k) = \frac{|x_{ik}|+1}{N_{y_k}+K}$,K是label的数量

!!! note "改成取$\ln$的原因"
    最重要的不是值本身，而是相对大小
    为了避免向上溢出，和向下溢出（浮点数问题），take a log





## generalization 泛化





## 学习资源

[Machine Learning in Practice Crash Course | Jinming Hu (conanhujinming.github.io)](https://conanhujinming.github.io/post/ml_in_practice_crash_course/)

[实用的机器学习 第一课 机器学习导论 2024summer_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Gw4m1i7ys/?spm_id_from=333.788.recommend_more_video.0&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)

[机器学习2023-10-19第6-8节 (zju.edu.cn)](https://classroom.zju.edu.cn/livingpage?course_id=53449&sub_id=915451&tenant_code=112)

赵洲老师







[有监督的机器学习：回归与分类 | Coursera](https://www.coursera.org/learn/machine-learning?action=enroll)

[CS229吴恩达机器学习](https://www.bilibili.com/video/BV16J411t71N)

[CS229: Machine Learning (stanford.edu)](https://cs229.stanford.edu/)



深度学习

[CS231n Convolutional Neural Networks for Visual Recognition](https://cs231n.github.io/)：deep learning for CV

[图灵班《机器学习》课程总结 - CC98论坛](https://www.cc98.org/topic/5599897)

我在心灵学ML系列doge

[再次入门deep learning以及一些回忆（更新第二部分） - CC98论坛](https://www.cc98.org/topic/5207160)

[再次入门deep learning，这次直接上重点（完结篇） - CC98论坛](https://www.cc98.org/topic/5208795)



孔院🐕🦁课

[人工智能与机器学习复习资料 - CC98论坛](https://www.cc98.org/topic/5518130)

[2022-2023秋冬人工智能与机器学习线上考试回忆卷（和大佬们发重了） - CC98论坛](https://www.cc98.org/topic/5508899)

[人工智能与机器学习回忆卷 - CC98论坛](https://www.cc98.org/topic/5234359)





本人农学博士，科研接触的机器学习，之前有计算机的导师领入门了。个人目前遇到最好的教程是吴恩达的视频课程，因为他充分考虑到了学生的水平，把需要的数学知识也讲了，先看了吴恩达早期的机器学习（反向传播的那节讲的不是很好），然后近两年的深度学习，在看了b站北大的tensorflow笔记课程，觉得至少知道该怎么做机器学习（包括深度学习）了。 不过作为一个非计算机专业的学生，个人觉得所有的教程都忽视了一个最基础但是也是最重要的东西——**特征工程**，指的不是特征选择（无监督学习的降维），而是特征表征（feature represent），深度学习里面叫embedding（自己看了功能后理解的），就是我们应该怎样去表征问题，将问题的信息表示为数据给计算机进行学习。之前看了什么有监督学习啊，无监督学习啊，对特征就是告诉你样本或向量空间，完全不知道机器学习去做什么。只到有个老师让我在做了特征提取，然后降维，然后分类或预测的时候我才明白机器学习是一个什么样的过程。



我是入门看的咱们学校的机器学习课程，对机器学习大概有个了解，没太关心数学。 说实话这些算法（ml里不包含dl的那些）我科研上用到的比较少，后来随着科研的深入会去思考这些算法后面的数学原理，就去参考李航的机器学习，西瓜书。更加高屋建瓴一点的教材就是PRML了。 我比较推荐UCB的CS188，从整个人工智能的角度讲问题，机器学习是其中的一个部分。编程项目有趣连贯。用的教材也是经典，一些思想现在也不过时。



pipeline

完成实用机器学习的所有作业

完成赵洲老师的所有作业+大作业

