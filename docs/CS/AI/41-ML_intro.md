# 机器学习导论

!!! note "课程信息"
    === "机器学习"
        - 课程时间：2024年秋冬
        - 课程教师：赵洲
        - 考核内容：2次书面作业+2次编程作业[Kaggle](https://www.kaggle.com/)（45%）+15次随机签到（15%）+1次期末摸底考试+1次期末考试；（40%）
        - 课本：西瓜书
    === "实用的机器学习"


[人工智能基础 - 鹤翔万里的笔记本 (tonycrane.cc)](https://note.tonycrane.cc/cs/ai/basic/)

[02：贝叶斯定理 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/ML/统计机器学习02：贝叶斯定理/)

[命题逻辑 - Jerry's Blog (wxxcl.tech)](https://blog.wxxcl.tech/course/aid/知识表达与推理/命题逻辑/)

[笔记](https://github.com/mura1n/Machine-Learning-in-Practice-Crash-Course-Notes)

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

解决问题的方案：采用精确率或者召回率

!!! tip "查准率和查全率"
    - 查准率：即你认为是True的样本中，到底有多少个样本是真为True。
    - 查全率：即在预测样本中属于True的样本，你真的判断为True的有几个。

- 真阳性率（True Positive Rate，TPR）通常也被称为敏感性（Sensitivity）或召回率（Recall）。它是指分类器正确识别正例的能力。真阳性率可以理解为所有阳性群体中被检测出来的比率(1-漏诊率)，因此TPR越接近1越好。它的计算公式如下：$precision=\frac{T P}{TP+FP}$


- 召回率（查全率）：实际为正类的样本中，被预测正确的正类的比例。$recall=\frac{T P}{T P+F N}$



- 假阳性率 (False Positive Rate, FPR)
假阳性率（False Positive Rate，FPR）是指在所有实际为负例的样本中，模型错误地预测为正例的样本比例。假阳性率可以理解为所有阴性群体中被检测出来阳性的比率(误诊率)，因此FPR越接近0越好。它的计算公式如下 FP = \frac{FP}{FP+TN}

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240909154344.png)


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


### 极大似然法 maximum likehood


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
  - laplace smoothing: $P(x_i| y_k) = \frac{|x_{ik}|+1}{N_{y_k}+K}$,K是label的数量

!!! note "改成取$\ln$的原因"
    最重要的不是值本身，而是相对大小
    为了避免向上溢出，和向下溢出（浮点数问题），take a log

!!! example "例题"
    首先需要将文本表示成词向量，再从词向量中计算得到条件概率 $P(X|C)$和先验概率 $P(C)$
    然后利用条件概率 $P(X|C)$与先验概率 $P(C)$计算后验概率 $P(C_0|X)$、 $P (C_1|X)$
    最终比较 $P(C_0|X)$、 $P (C_1|X)$大小得到 $X$ 属于 $C_0$ 类还是 $C_1$ 类





## linear Regression
y 是一个连续的值；
区别于classification，y是一个离散的值

### Polynomial Curve Fitting

$f(x,\omega) = \omega_0 + \omega_1x + \omega_2x^2 + \omega_3x^3 + \dots + \omega_Mx^M = \sum_{j=0}^{M}\omega_jx^j$

loss function: MSE: 


$MSE(\omega) = \frac{1}{N}\sum_{i=1}^{N}(y_i - f(x_i,\omega))^2$

模型是已知的，$\omega$未知，通过最小化MSE来求解$\omega$

- 最小二乘法

只能用于线性回归

!!! note "过程"
    using matrix notation for convenience: $X = [1,x,x^2,x^3,...,x^n], y = [y_1,y_2,...,y_n]^T$

    $Loss(\omega) = (y - X^T\omega)^T(y - X^T\omega)$

    梯度： $\nabla_{\omega}Loss(\omega) = -2X(y - X^T\omega)$

    令梯度为0，求解$\omega$，得到$\omega = (X^TX)^{-1}X^Ty$

!!! tips "几何理解"

    

- Gradient Descent | 梯度下降法
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240806020009.png)
步长的大小：学习率
Time complexity: $O(ndt)$,t是迭代次数,d是特征的数量,n是样本的数量


stochastic gradient descent | 随机梯度下降法
- randomly select b(batch size) samples from the training set
- Time complexity: $O(bdt)$


- Quasi Newton Method | 拟牛顿法



### overfitting | 过拟合
在测试集上效果好的模型就是好的模型

在测试集上效果差的模型就是差模型

把training data中的noise也学习到了

- Ridge Regression | 岭回归

Loss(\omega*)

regularization: 一些先验的假设，比如$\omega$是稀疏的，或者$\omega$是平滑的；避免学习到

超参数：
- $\lambda$：控制正则化的强度: $\lambda$越大，正则化的强度越大，模型越简单，training error 越大；如下图，左侧叫做过拟合，右侧叫做欠拟合![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240806021738.png)
- $\alpha$：控制学习率





### Logistic Regression
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240807233452.png)

线性回归有一个很强的假设，就是y是连续的；并且有更像邻近数的趋势(MSE 对于线性回归不是一个好的function)

- one vs. Rest

logistic function:

- sigmoid function: $f(x) = \frac{1}{1+e^{-x}}$
CDF(累积分布函数)ofthe standard logistic distribution   
使用sigmoid函数将线性回归的输出转换为概率

!!! note "logistic Regreesion是一个线性模型"
    主要考虑的是decision boundary
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240807234021.png)


为什么loss function要取log
- 为了方便求导
- 取log使得连乘变成连加，不会丢失信息

Assumptions behind logistic regression
- l(a) = -\sum_{i\in I} \log(1+e^{-y_i a^T x_i})


pros:
- binomial distribution is a  good assumption for classification
- provide a probability
- low computation, easy to optimize
- support online learning:梯度下降的模型都支持在线学习

cons:
- too simple:high bias & low variance


### Support Vector Machine
计算每个点到决策边界的距离$\gamma$

- Maximum Margin Classifier:数据集最小的margin
目的就是要找到一个决策边界，使得margin最大

为什么使用这种方法
- 裕度更高，容错性更好
- 如果margin越大，对于噪声的容忍度越高

### loss function


task



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

