# 机器学习导论

[人工智能基础 - 鹤翔万里的笔记本 (tonycrane.cc)](https://note.tonycrane.cc/cs/ai/basic/)

[02：贝叶斯定理 - 小角龙的学习记录 (zhang-each.github.io)](https://zhang-each.github.io/My-CS-Notebook/ML/统计机器学习02：贝叶斯定理/)

[命题逻辑 - Jerry's Blog (wxxcl.tech)](https://blog.wxxcl.tech/course/aid/知识表达与推理/命题逻辑/)



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





the performance of the classifier on test data



accuracy

- 不是所有人都会得癌症

- 不是所有错误都是同样重要的

- spam/ham email detection 



精度$presicision = \frac{TP}{TP+FP}$

召回率$Recall = \frac{TP}{TP+FN}$

mean squared error | MSE: 均方误差

$MSE(f,\theta) = \frac{1}{n} \Sigma^n_{i=1}(y_i-f(x_i,\theta))^2$

- 极值影响很大

Mean Absolute Error | MAE:

$MAE(f,\theta) = \frac{1}{n}|y_i - f(x_i,\theta)|$



speed

FPS



memory consumption

platform required for running 

CPU vs GPU

server,workstation



![image-20240614200543795](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240614200543795.png)

more closed to the realistic world



## generalization 泛化





## typical ML problems

### 贝叶斯决策

$x$ sample

$y$ state of the nature

$P(y|x)$ given $x$​,what is the probability of the state of the nature

条件概率：
$$
P(A|B) = \frac{P(A,B)}{P(B)}
$$
独立的含义



贝叶斯
$$
P(A|B) = P(A)\frac{P(B|A)}{P(B)}
$$

$$
[后验概率] = [先验概率]\times[后验概率]
$$

先验概率 | `prior`: $P(A)$the probability A being True. this is the knowledge

似然性 | `likelihood`: $P(B|A)$the probability of B being true,given A is true

最大似然概率决策

后验概率 | `posterior`: $P(A|B)$





## basic ML method

linear boundary





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

