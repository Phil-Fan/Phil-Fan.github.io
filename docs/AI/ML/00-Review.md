# 复习
!!! note "简介"
    一、选择题：20*2 **单多混选** 真nt啊！！！<br>
    二、填空题：每空1分，共10分<br>
    三、大题/简答题 共50分<br>

## 重点掌握

- 人工智能导论部分的概念背诵<br>
- 盲目搜索几种算法的原理、优缺点<br>
- 启发式搜索几种算法的原理、优缺点；A*的步骤；<br>
- 逻辑：谓词逻辑；归结原理<br>

**机器学习：**
- 概念学习：定义；Find-S；候选消除算法<br>
- 性能度量：recall precision f1-score<br>
- 决策树:信息增益的计算；<br>
- 神经网络：过拟合；正则化；<br>
- 贝叶斯：极大似然估计；naive-bayes：iid假设<br>
- 强化学习：免模型、有模型学习<br>
  

## 统计学习资料


### 资料
[ZJU\_Stat\_Courses/统计学习 at main · Frankgu3528/ZJU\_Stat\_Courses](https://github.com/Frankgu3528/ZJU_Stat_Courses/tree/main/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0)


### 课本
[An Introduction to Statistical Learning](https://www.statlearning.com/)

[ESL CN](https://esl.hohoweiya.xyz/index.html)



https://www.bilibili.com/video/BV1QW411o7fk?from=search&seid=17747537286715723310&spm_id_from=333.337.0.0



### 统计学习 2023-2024春夏
[2023-2024春夏回忆卷 - CC98论坛](https://www.cc98.org/topic/5918627)
[2019-2020春夏回忆卷 - CC98论坛](https://www.cc98.org/topic/4959501)
#### 选择
2. Confusion Matrix
   - 一个平衡样本做二分类问题
   - 给定accuracy以及FN，求TNR

3. Bias-Variance Tradeoff，三道选择题
   - 正则化项会导致bias和variance如何变化
   - irreducible bias来源
   - 如何才能降低irreducible bias

增加正则化项会（增⼤、减⼩）偏差，（增⼤、减⼩）⽅差？
b. Irreducible Error是由什么引起的？
c. 以下那种⽅法可以减少Irreducible Error？




#### 简答
2. 分类：数据集正例负例⼀样多，准确率为80%，把正例错判为负例10%，求把负例判断正确的概率（⼤概是这个数据）

4. 简述Ridge，Lasso Regression，还有Elatic net

4. 决策树，不剪枝，四道判断+论述
   - 如果有X1在DGP中与Y独立，则不会进入决策树
   - 决策树的最大深度是log2（n）+1
   - 如果做bootstrap抽样训练B棵树然后取平均，是随机森林
   - 随机森林只能做预测，不能做分类


5. 判断题（树和随机森林），判断并给出理由，树不进行剪枝
a. 树：有 $X_1, X_2, \ldots, X_p$ $X_1$ 与 $Y$ 独立，$X_1$ 不会出现在树的结构中
b. 树的最大深度小于 $\log_{(2n)} + 1$ （试卷上是这么打的）
c. 随机森林是树的求平均
d. 树可以用于预测和分类，随机森林只能用于预测，不能用于分类

5. 聚类
   - 给样本点和初始的C，手算一个K-means（k=3）任务

6. 因果推断
   - 简述G-formula
   - 简述IPTW

7. 工具变量
   - 简述IV
   - 描述always taker，never taker，defier，compiler是什么
   - 给定A和L，判断是哪一类
   - 什么是CAET，如何识别

### 统计学习19-20 春夏

一、不定项选择（5题）：

1. 模型选择与正则化相关概念

2. 引起随机森林过拟合的可能原因

3. 对 $n$ 个数据进行硬间隔线性SVM分类，有2个支持向量，增加一个数据，最大的支持向量数

4. 来自多个不同概率分布的总体的数据构成一个数据集，对该数据集使用k-means聚类分析，影响聚类效果的因素

5. LASSO与PCA比较

二、判断题（5题）：

1. 3-NN模型比1-NN模型 bias小

2. 深度为3的树比深度为1的树 variance大

3. （不记得了）

4. 假设空间越大，过拟合的可能性越大

5. Boosting采用指数损失函数

三、简答题（4题）：

1. 给出了一张表，包括参与拟合SVM的数据和拟合结果中的系数，判断哪些数据是支持向量

2. 给出了Ridge Regression的损失函数，解释其中参数 $\lambda$ 的作用，当 $\lambda$ 很大或很小时会有什么结果

3. 给出一组数据，判断下列分类方法是否可以对这组数据进行正确分类：
   - Logistic Regression
   - SVM（Linear Kernel）
   - SVM（RBF Kernel）
   - Decision Tree
   - 3-NN

4. 给出 $L_2$ 正则化的线性回归的模型和具体算法

四、
题干大意是用3-order的polynomial regression生成了一组数据

（1）用不同order的polynomial regression对上述数据进行拟合，判断bias和variance大小：
$d=1$, $d=3$, $d=10$

（2）在下列情况下使用flexible的模型是否比inflexible的模型更好，并说明理由：
① predictor与feature有显著的非线性关系
② 随机误差 $\epsilon$ 的方差很大

五、k-means：

给了一组数据并给出了预先设定的centroid，做出第一步迭代后的聚类图，并判断再进行一步迭代后，聚类是否发生变化

六、

题干大意是给了一组数据，拟合了一个模型，进行了变量选择，并求了不同变量数时的LOOCV，给出了train error和LOOCV随变量数 $d$ 的图象

（1）解释上述图象为什么是这样的

（2）$d$ 为多少时开始过拟合

（3）你觉得 $d$ =多少更合适

七、二次SVM：

核函数为quaratic kernel（给了损失函数）
给出一组数据，绘制出 $C$ 很大/小时的决策边界，并判断哪个更好

八、R代码题：（不是写代码，是给了一段R代码让你分析）

导入了一个数据集，用gam拟合了3个模型：

$\text{out1} = \text{gam}(y \sim x)$

$\text{out2} = \text{gam}(y \sim \te xt{as.factor}(x))$

$\text{out3} = \text{gam}(y \sim s(x))$

1.这三个模型中，第一个模型最光滑，第二个模型最曲折，第三个居中，试解释原因

2.给出了上面三个模型的summary，根据对这三个模型做一些评估（问的比我这里更具体一些，比如从拟合训练数据角度哪个更好、从AIC角度哪个更好等等）



h(n) 从 节点n代表的状态 到 目标状态 的 路径耗散 的 最小估计值

=== "可以评价分类的指标"
   - 准确率
   - 精确率
   - 召回率
   - F1-score
   - ROC曲线
   - AUC曲线
   - cross-entropy


=== "可以评价回归的指标"
   - MSE:Mean Squared Error (均方误差)，又称L2 loss
   - RMSE:Root Mean Squared Error (均方根误差)
   - MAE:Mean Absolute Error (平均绝对误差),又称L1 loss
   - l1-smooth:L1正则化 ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108143036.png)
   - MBE:Mean Bias Error (平均偏差误差) 没有取绝对值
   - R2
   - R2_adjusted

## 小测题目

### 搜索
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108125536.png)
1. 广度优先搜索(BFS)<br>
    - 基本原理：从根节点开始，先访问当前层的所有节点，再访问下一层节点。使用队列存储待访问节点（先进先出）<br>
    - 对于图中搜索树的BFS扩展顺序：1-2-3-4-5-6-7-8-9-10-11-12-13<br>

2. 深度优先搜索(DFS)<br>
    - 基本原理：从根节点开始，沿着一条路径一直搜索到底，直到不能再深入才回溯到上一个节点继续搜索。使用栈存储待访问节点（后进先出）<br>
    - 对于图中搜索树的DFS扩展顺序：1-2-5-6-10-11-3-7-12-13-4-8-9<br>

3. 有限深度搜索<br>
    - 基本原理：是DFS的改进版本，设定一个最大搜索深度，超过该深度就回溯。<br>
    - 特点：避免了DFS可能出现的无限递归问题，但可能错过解。<br>

4. 迭代加深搜索<br>
    - 基本原理：将有限深度搜索从小到大反复进行，每次增加最大深度限制。<br>
    - 特点：结合了BFS找到最短路径的优点和DFS空间效率高的优点。<br>

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108125558.png)

$$
f(x) = g(x) + h(x)
$$

g(x)为已经走过的步数，h(x)为初始状态各数字与目标状态各数字的曼哈顿距离之和

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108130126.png)

### 谓词逻辑
**有如下事实：**<br>

- 所有伟大的厨师都是意大利人<br>
- 所有意大利人都喜欢享用美食<br>
- 迈克尔（Michael）或路易斯（Louis）是一位伟大的厨师<br>
- 迈克尔不是一位伟大的厨师<br>

**因此，路易斯喜欢享用美食**<br>

**请：**<br>

!!! question "1. 定义合适的谓词（1.5分）"
    定义如下谓词:<br>
    $GC(x)$: x 是一位伟大的厨师<br>
    $I(x)$:  x 是意大利人<br>
    $EF(x)$: x 享用美食<br>

!!! question "2. 使用定义的谓词表述上述语句（2.0分）"
    谓词逻辑表达：<br>
    1) $(\forall x)(GC(x) \Rightarrow I(x))$<br>
    2) $(\forall x)(I(x) \Rightarrow EF(x))$<br>
    3) $GC(\text{Michael}) \lor GC(\text{Louis})$<br>
    4) $\neg GC(\text{Michael})$<br>
    因此: 5) $EF(\text{Louis})$<br>

!!! question "3. 将谓词语句转换为标准子句（2.5分）"
    转换为子句（量词实例化和蕴含消除）:<br>
    1) $\neg GC(x) \lor I(x)$<br>
    2) $\neg I(y) \lor EF(y)$<br>
    3) $GC(\text{Michael}) \lor GC(\text{Louis})$<br>
    4) $\neg GC(\text{Michael})$<br>

!!! question "4. 应用归结方法证明结论⑤，画出归结过程并标注出合适的合一（4分）"
    否定结论:<br>
    5) ~EF(Louis)<br>
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108130259.png)

### 机器学习

!!! question "1. 神经网络中的权重调整是通过以下哪种算法实现的?"
    A. 梯度下降  B. 牛顿法  C. 拟牛顿法  D. 共轭梯度法<br>
    答案：A。神经网络训练过程中主要使用梯度下降及其变体来优化权重。<br>

!!! question "2. 在神经网络中，反向传播算法主要用于以下哪种目的?"
    A. 优化权重  B. 计算损失函数  C. 更新输入层  D. 确定输出层<br>
    答案：A。
    
    反向传播算法的主要目的是计算梯度并优化网络权重。<br>

!!! question "3. 在多层感知器中，激活函数的作用是?"
    A. 引入非线性  B. 确定神经元的输出  C. 计算损失函数  D. 控制神经元的输入<br>
    答案：A。<br>
    激活函数引入非线性变换，使网络能够学习复杂的非线性映射关系。<br>

!!! question "4. 在卷积神经网络中，卷积层的作用是?"
    A. 对输入数据进行局部感知  B. 实现数据的高维表示<br>
    C. 对数据进行全局感知  D. 实现数据的降维表示<br>
    答案：A。<br>
    卷积层通过局部感受野对输入特征进行局部特征提取。<br>

!!! question "5. 在深度神经网络中，当数据维度很高时，通常采用哪种策略来处理?"
    A. 数据降维  B. 数据增强  C. 数据归一化  D. 数据标准化<br>
    答案：A。<br>
    高维数据通常需要通过降维来减少计算复杂度并避免维度灾难。<br>

!!! question "请简述在神经网络学习模型训练过程中，过拟合和欠拟合的概念及其产生原因。"

    过拟合(Overfitting)：<br>
    - 概念：模型在训练集上表现很好，但在测试集上表现差<br>
    - 原因：<br>
      1. 模型过于复杂，参数过多<br>
      2. 训练数据量不足<br>
      3. 训练时间过长<br>

    欠拟合(Underfitting)：<br>
    - 概念：模型在训练集和测试集上都表现不好<br>
    - 原因：<br>
      1. 模型过于简单，无法捕捉数据特征<br>
      2. 特征选择不当<br>
      3. 训练不充分<br>

!!! question "11. 下列属于无监督学习的是（）"
    A. k-means<br> 
    B. SVM<br> 
    C. 最大熵<br> 
    D. CRF (条件随机场,一种判别式概率无向图模型,常用于序列标注任务)<br>
    答案：A。k-means是一种典型的无监督聚类算法。<br>

!!! question "12. "过拟合"只在监督学习中出现，在非监督学习中，没有"过拟合"，这是（）"
    A. 对的<br>                          
    B. 错的<br>
    答案：B。过拟合现象在无监督学习中同样存在。<br>

!!! question "13. 在下面哪种情况下，一阶梯度下降不一定正确工作（可能会卡住）？"
    A. ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108131252.png)<br>    
    B. ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108131301.png)<br>
    C. ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108131305.png)<br>
    D. 以上都不正确<br>
    答案：B。在局部最小值点处，梯度为0，一阶梯度下降可能会停止。<br>

!!! question "14. 下列哪个函数不可以做激活函数？"
    A. y = tanh(x)<br>        
    B. y = sin(x)<br>        
    C. y = max(x,0)<br>        
    D. y = 2x<br>
    答案：D。线性函数不能作为激活函数，因为无法引入非线性变换。<br>

!!! question "15. 我们想在大数据集上训练决策树，为了使用较少时间，我们可以（）"
    A. 增加树的深度<br> 
    B. 增加学习率 (learning rate)<br> 
    C. 减少树的深度<br> 
    D. 减少树的数量<br>
    答案：C。减少树的深度可以降低计算复杂度。<br>

    增加树的深度, 会导致所有节点不断分裂, 直到叶子节点是纯的为止. 所以, 增加深度, 会延长训练时间.<br>
    决策树没有学习率参数可以调. (不像集成学习和其它有步长的学习方法)<br>
    决策树只有一棵树, 不是随机森林。<br>

!!! question "16. 一监狱人脸识别准入系统用来识别待进入人员的身份，此系统一共包括识别4种不同的人员：狱警，小偷，送餐员，其他。下面哪种学习方法最适合此种应用需求："
    A. 二分类问题<br> 
    B. 多分类问题<br> 
    C. 层次聚类问题<br> 
    D. k-中心点聚类问题<br>
    E. 回归问题<br>
    F. 结构分析问题<br>
    答案：B。这是一个典型的多分类问题。<br>

!!! question "17. Naive Bayes是一种特殊的Bayes分类器，特征变量是X，类别标签是C，它的一个假定是（）"
    A. 各类别的先验概率P(C)是相等的<br>
    B. 以0为均值，sqr(2)/2为标准差的正态分布<br>
    C. 特征变量X的各个维度是类别条件独立随机变量<br>
    D. P(X|C)是高斯分布<br>
    答案：C。朴素贝叶斯的核心假设是特征条件独立性即iid假设<br>

!!! question "18. 对于k折交叉验证，以下对k的说法正确的是（）"
    A. k越大, 不一定越好, 选择大的k会加大评估时间<br> 
    B. 选择更大的k, 就会有更小的bias (因为训练集更加接近总数据集)<br> 
    C. 在选择k时, 要最小化数据集之间的方差<br> 
    D. 以上所有<br>
    答案：D。这些都是关于k折交叉验证的正确描述。<br>
    k越大，就要训练k个模型，计算量越大，所以时间更多；k越大，每次选取的训练集越接近总数据集，所以bias越小；

!!! question "19. 训练决策树模型，属性节点的分裂，具有最大信息增益的图是哪一个（）"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108131317.png)<br>
    A. Outlook<br> 
    B. Humidity<br> 
    C. Windy<br> 
    D. Temperature<br>
    答案：A。根据图中信息增益的计算，Outlook具有最大的信息增益。<br>

!!! question "20. 假定某同学使用Naive Bayesian（NB）分类模型时，不小心将训练数据的两个维度搞重复了，那么关于NB的说法中正确的是（）"
    A. 这个被重复的特征在模型中的决定作用会被加强<br> 
    B. 模型效果相比无重复特征的情况下精确度会降低<br> 
    C. 如果所有特征都被重复一遍，得到的模型预测结果相对于不重复的情况下的模型预测结果一样<br> 
    D. 当两列特征高度相关时，无法用两列特征相同时所得到的结论来分析问题<br> 
    E. NB可以用来做最小二乘回归<br> 
    F. 以上说法都不正确<br>

    答案：BD [假定某同学使用Naive Bayesian（NB）分类模型时\_\_牛客网](https://www.nowcoder.com/questionTerminal/f25c433b9b0d42659d2cf3b39a8367ae)<br>
    A. 看D就知道，如果两个维度比较相似，那么这两个维度可能高度相关，那么就需要转到D。<br>
    B. 当维度重复时，习得的联合概率分布有误，所以精确度会降低。<br>
    C. 多出一个维度的特征，其训练出的模型就会有所不同。这与把两个维度的值重复的情况是不同的。<br>
    D.两列特征高度相关时（也就是有可能是因为重复了），那就无法用这种疑似重复的特征来分析问题了。<br>
    E.最小二乘回归是用在判别式的机器学习方法中，比如SVM,logtic等。它是寻找几何误差最小的预测模型。而贝叶斯是生成式模型。<br>
 



!!! question "1. 混淆矩阵的召回率（Recall）公式为？"
    A. TP/(TP+FN)<br>
    B. FN/(TP+FN)<br>
    C. TN/(TN+FP)<br>
    D. FP/(FP+TN)<br>
    答案：A<br>
    我记忆的方式是：Precision是以P开头的，所以公式中都有P；Recall是对应的

!!! question "2. 在构建决策树时，需要计算每个用来划分数据特征的得分，选择分数最高的特征，以下可以作为得分的是？"
    A. 信息熵<br>
    B. 基尼系数（Gini）<br>
    C. 训练误差<br>
    D. 以上都是<br>
    答案：D<br>

!!! question "3. 下列描述无监督学习错误的是？"
    A. 无标签<br>
    B. 多用于聚类<br>
    C. 多用于分类<br>
    D. 多用于降维<br>
    答案：C<br>

!!! question "4. 强化学习算法可以分为有模型学习（model-based）算法和免模型（model-free）学习算法，以下属于有模型学习算法的是？"
    A. Policy Gradient<br>
    B. Deep Deterministic Policy Gradient (DDPG)<br>
    C. Deep Q Network (DQN)<br>
    D. AlphaZero<br>
    答案：D<br>

!!! question "5. 感知器可以解决一下那些问题？"
    A. 逻辑"与"<br>
    B. 逻辑"或"<br>
    C. 逻辑"与非"<br>
    D. 逻辑"或非"<br>
    答案：ABCD<br>
    都是线性可分的
    与非（NAND）真值表：
    | $A$ | $B$ | $\overline{A \cdot B}$ |
    |-----|-----|----------------------|
    | 0   | 0   | 1                    |
    | 0   | 1   | 1                    |
    | 1   | 0   | 1                    |
    | 1   | 1   | 0                    |

    或非（NOR）真值表：
    | $A$ | $B$ | $\overline{A + B}$ |
    |-----|-----|-------------------|
    | 0   | 0   | 1                 |
    | 0   | 1   | 0                 |
    | 1   | 0   | 0                 |
    | 1   | 1   | 0                 |

!!! question "6. 如果一个"线性回归"模型完美地拟合了训练样本，也就是训练样本误差为零，则下面哪个说法是正确的？"
    A. 测试样本误差始终为零<br>
    B. 测试样本误差不可能为零<br>
    C. 以上答案都不对<br>
    答案：C<br>

!!! question "7. 在一个线性回归问题中，我们使用 R 平方（R-Squared）来判断拟合度。此时，如果增加一个特征，模型不变，则下面说法正确的是？"
    A. 如果 R-Squared 增加，则这个特征有意义<br>
    B. 如果R-Squared 减小，则这个特征没有意义<br>
    C. 仅看 R-Squared 单一变量，无法确定这个特征是否有意义<br>
    D. 以上说法都不对<br>
    答案：C<br>

!!! question "8. 下列哪些假设是我们推导线性回归参数时遵循的？"
    A. X 与 Y 有线性关系（多项式关系）<br>
    B. 模型误差在统计学上是独立的<br>
    C. 误差一般服从 0 均值和固定标准差的正态分布<br>
    D. X 是非随机且测量没有误差的<br>
    答案：ABCD<br>

!!! question "9. 一般来说，下列哪种方法常用来预测连续输出变量？"
    A. 线性回归<br>
    B. 逻辑回顾<br>
    C. 线性回归和逻辑回归都行<br>
    D. 以上说法都不对<br>
    答案：A<br>

!!! question "10. 下面三张图展示了对同一训练样本，使用不同的模型拟合的效果（蓝色曲线）。那么，我们可以得出哪些结论？"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250108135205.png)
    A. 第 1 个模型的训练误差大于第 2 个、第 3 个模型<br>
    B. 最好的模型是第 3 个，因为它的训练误差最小<br>
    C. 第 2 个模型最为"健壮"，因为它对未知样本的拟合效果最好<br>
    D. 第 3 个模型发生了过拟合<br>
    E. 所有模型的表现都一样，因为我们并没有看到测试数据<br>
    答案：ACD<br>

!!! question "11. 两个变量相关，它们的相关系数 r 可能为 0。这句话是否正确？"
    A. 正确<br>
    B. 错误<br>
    答案：A<br>
    一般来说，相关系数 r=0 是两变量相互独立的必要不充分条件。也就是说，如果两个变量相互独立，那么相关系数 r 一定为 0，如果相关系数 r=0，则不一定相互独立。相关系数 r=0 只能说明两个变量之间不存在线性关系，仍然可能存在非线性关系。

!!! question "12. 逻辑回归将输出概率限定在 [0,1] 之间。下列哪个函数起到这样的作用？"
    A. Sigmoid 函数<br>
    B. tanh 函数<br>
    C. ReLU 函数<br>
    D. Leaky ReLU 函数<br>
    答案：A<br>

!!! question "13. 关于 k 折交叉验证，下列说法正确的是？"
    A. k 值并不是越大越好，k 值过大，会降低运算速度<br>
    B. 选择更大的 k 值，会让偏差更小，因为 k 值越大，训练集越接近整个训练样本<br>
    C. 选择合适的 k 值，能减小验方差<br>
    D. 以上说法都正确<br>
    答案：D<br>

!!! question "14. 我们知道二元分类的输出是概率值。一般设定输出概率大于或等于 0.5，则预测为正类；若输出概率小于 0.5，则预测为负类。那么，如果将阈值 0.5 提高，例如 0.6，大于或等于 0.6 的才预测为正类。则准确率（Precision）和召回率（Recall）会发生什么变化？"
    A. 准确率（Precision）增加或者不变<br>
    B. 准确率（Precision）减小<br>
    C. 召回率（Recall）减小或者不变<br>
    D. 召回率（Recall）增大<br>
    答案：AC<br>

    提高阈值意味着只有更高的概率值（大于或等于 0.6）的样本才会被预测为正类。这会带来以下影响：

    1. 样本预测变化：
        - 减少被预测为正类的样本数量
        - 原本预测为正类（概率在 0.5-0.6 之间）的样本会被改为负类

    2. 对准确率（Precision）的影响：
        - 随着阈值提高，一些误判为正类的样本（FP）被排除
        - TP + FP 减少，且 FP 减少比例可能大于 TP 减少比例
        - 因此准确率会增加或保持不变（A）

    3. 对召回率（Recall）的影响：
        - 随着阈值提高，一些实际为正类的样本（TP）被预测为负类
        - TP 减少，而 TP + FN 保持不变
        - 因此召回率会减小或保持不变（C）

!!! question "15. 关于神经网络，下列说法正确的是？"
    A. 增加网络层数，可能会增加测试集分类错误率<br>
    B. 增加网络层数，一定会增加训练集分类错误率<br>
    C. 减少网络层数，可能会减少测试集分类错误率<br>
    D. 减少网络层数，一定会减少训练集分类错误率<br>
    答案：AC<br>

!!! question "16. 下面哪句话是正确的？"
    A. 机器学习模型的精准度越高，则模型的性能越好<br>
    B. 增加模型的复杂度，总能减小测试样本误差<br>
    C. 增加模型的复杂度，总能减小训练样本误差<br>
    D. 以上说法都不对<br>
    答案：C<br>

!!! question "17. 如果一个经过训练的机器学习模型在测试集上达到 100% 的准确率，这是否意味着该模型将在另外一个新的测试集上也能得到 100% 的准确率呢？"
    A. 是的，因为这个模型泛化能力已经很好了，可以应用于任何数据<br>
    B. 不行，因为还有一些模型不确定的东西，例如噪声<br>
    答案：B<br>

!!! question "18. 下面有关分类算法的准确率，召回率，F1 值的描述，错误的是？"
    A. 准确率是检索出相关文档数与检索出的文档总数的比率，衡量的是检索系统的查准率<br>
    B. 召回率是指检索出的相关文档数和文档库中所有的相关文档数的比率，衡量的是检索系统的查全率<br>
    C. 正确率、召回率和 F 值取值都在 0 和 1 之间，数值越接近 0，查准率或查全率就越高<br>
    D. 为了解决准确率和召回率冲突问题，引入了F1分数<br>
    答案：C<br>

    仅依赖 Precision 或 Recall 可能导致模型无法全面评估，尤其在类别不平衡的情况下。调和平均 比算术平均更倾向于较小的值，因此能够捕捉 Precision 和 Recall 之间的平衡。

!!! question "19. "增加卷积核的尺寸，一定能提高卷积神经网络的性能。" 这句话是否正确？"
    A. 正确<br>
    B. 错误<br>
    答案：B<br>

!!! question "20. 假如现在有个神经网络，激活函数是 ReLU，若使用线性激活函数代替 ReLU，那么该神经网络还能表征异或（XNOR）函数吗？"
    A. 可以<br>
    B. 不可以<br>
    答案：B<br>

!!! question "21. 下列哪种方法可以用来减小过拟合？"
    A. 更多的训练数据<br>
    B. L1 正则化<br>
    C. L2 正则化<br>
    D. 减小模型的复杂度<br>
    答案：ABCD<br>

!!! question "22. 下列说法错误的是？"
    A. 当目标函数是凸函数时，梯度下降算法的解一般就是全局最优解<br>
    B. 进行 PCA 降维时，需要计算协方差矩阵<br>
    C. 沿负梯度的方向一定是最优的方向<br>
    D. 利用拉格朗日函数能解带约束的优化问题<br>
    答案：C<br>

!!! question "23. 关于 L1、L2 正则化下列说法正确的是？"
    A. L2 正则化能防止过拟合，提升模型的泛化能力，但 L1 做不到这点<br>
    B. L2 正则化技术又称为 Lasso Regularization<br>
    C. L1 正则化得到的解更加稀疏<br>
    D. L2 正则化得到的解更加稀疏<br>
    答案：C<br>L2叫岭回归，L1叫Lasso回归；L2倾向于参数平滑都很小，L1倾向于参数稀疏。

!!! question "24. 假定你在神经网络中的隐藏层中使用激活函数 X。在特定神经元给定任意输入，你会得到输出 -0.01。X 可能是以下哪一个激活函数？"
    A. ReLU<br>
    B. tanh<br>
    C. Sigmoid<br>
    D. 以上都有可能<br>
    答案：B<br>

!!! question "25. 以下哪些方法不可以直接来对文本分类？"
    A. K-Means<br>
    B. 决策树<br>
    C. 支持向量机<br>
    D. kNN<br>
    答案：A<br>

!!! note "什么是机器学习模型的过拟合和欠拟合？导致模型过拟合的原因有哪些？请结合决策树和神经网络模型进一步阐述解决模型过拟合的方法。"

    参考答案：<br>

    - 过拟合：模型在训练集上错误率很低，但是在未知数据上错误率很高。<br>

    - 欠拟合：模型不能很好地拟合训练数据，在训练集和测试集上的错误率都比较高。<br>

    - 过拟合的原因：过拟合问题往往是由于训练数据少和噪声以及模型复杂度过高等原因造成的。<br>

    - 解决过拟合的方法：<br>
        1. 数据层面：增加训练数据、清除数据噪声<br>
        2. 模型层面：在经验风险最小化的基础上引入参数的正则化、模型训练提前迭代终止远侧、模型剪枝原则等。<br>
        例如，决策树模型可以通过先剪枝操作来控制决策树的生长或通过后剪枝操作对决策树进行修剪。神经网络模型可以通过加入L1正则化或者L2正则化、Dropout、early stopping等<br>

!!! question "关于机器学习算法评估，分别阐述适用于回归算法和分类算法的评估指标有哪些？并阐述各种评估指标的优缺点。"

    参考答案：<br>
    回归算法评估指标：<br>
    a) 平均绝对误差（Mean Absolute Error）<br>
    b) 均方误差（Mean Squared Error）<br>
    c) 均方根误差（Root Mean Squared Error）<br>
    d) 决定系数（Coefficient of determination）<br>

    分类算法评估指标：<br>
    a) 精度 Accuracy<br>
    b) 混淆矩阵 Confusion Matrix<br>
    c) 准确率（查准率）Precision<br>
    d) 召回率（查全率）Recall<br>
    e) Fβ Score<br>
    f) AUC Area Under Curve<br>
    g) KS Kolmogorov-Smirnov<br>

    回归算法评估指标的优缺点举例：<br>
    a) MAE虽能较好衡量回归模型的好坏，但是绝对值的存在导致函数不光滑，在某些点上不能求导，可以考虑将绝对值改为残差的平方；<br>
    b) MSE与目标变量的量纲不一致；<br>
    c) RMSE可以保证量纲一致性；<br>
    d) 以上基于误差的均值对进行评估的指标，均值对异常点（outliers）较敏感，如果样本中有一些异常值出现，会对以上指标的值有较大影响。<br>

    分类算法评估指标的优缺点举例：<br>
    a) 对于有倾向性的问题，往往不能用精度指标来衡量。<br>
    b) 对于样本类别数量严重不均衡的情况，也不能用精度指标来衡量。<br>
    c) AUC是一种模型分类指标，且仅仅是二分类模型的评价指标。<br>
    d) AUC对样本类别是否均衡并不敏感；<br>




 
### 机器学习，找到的网上题目

可以在tb上买一天的csdn会员<br>

!!! question "21. 模型的高bias是什么意思, 我们如何降低它？"
    A. 在特征空间中减少特征<br>
    B. 在特征空间中增加特征<br>
    C. 增加数据点<br>
    D. B和C<br>
    E. 以上所有<br>
    答案：B。bias太高说明模型太简单了, 数据维数不够, 无法准确预测数据, 所以, 升维吧!<br>

!!! question "22. 对于信息增益, 决策树分裂节点, 下面说法正确的是（）"
    1. 纯度高的节点需要更多的信息去区分<br>
    2. 信息增益可以用"1比特-熵"获得<br>
    3. 如果选择一个属性具有许多归类值, 那么这个信息增益是有偏差的<br>

    A. 1<br>
    B. 2<br>
    C. 2和3<br>
    D. 所有以上<br>
    正确答案是：C<br>

!!! question "23. 以下哪些算法可以用神经网络去构造？"
    A. KNN和线性回归<br>
    B. 线性回归和对数几率回归<br>
    C. KNN、线性回归和对数几率回归<br>
    D. 以上都不是<br>

    答案：B<br>
    解析：<br>
    - KNN算法不需要训练参数，而所有神经网络都需要训练参数，因此神经网络帮不上忙<br>
    - 最简单的神经网络感知器，其实就是线性回归的训练<br>
    - 我们可以用一层的神经网络构造对数几率回归<br>

!!! question "24. 位势函数法的积累势函数K(x)的作用相当于Bayes判决中的（）"
    A. 后验概率<br>
    B. 先验概率<br>
    C. 类概率密度<br>
    D. 类概率密度与先验概率的乘积<br>

    答案：A、D<br>

!!! question "25. 下列关于决策树的说法正确的是（）"
    A. ID3决策树是根据信息增益来划分属性<br>
    B. C4.5决策树是根据增益率来划分属性<br>
    C. CART决策树是根据基尼指数来划分属性<br>
    D. 基尼指数反映了从样本集D中随机抽取两个样本，其类别标记不一致的概率，因此越小越好<br>

    答案：A、B、C、D<br>

!!! question "26. 以下可以有效解决过拟合的方法是（）"
    A. 增加样本数量<br>
    B. 通过特征选择减少特征数量<br>
    C. 训练更多的迭代次数<br>
    D. 采用正则化方法<br>

    答案：A、B、D，增加训练迭代次数不会防止过拟合<br>



!!! question "27. 在机器学习中需要划分数据集，常用的划分测试集和训练集的划分方法有哪些（ ）"
    A. 留出法(leave one out)<br>
    B. 交叉验证法<br>
    C. 自助法<br>
    D. 评分法<br>

    正确答案: A B C<br>

!!! question "28. 现在假设负样本量:正样本量=100:1，下列哪些方法可以处理这种极不平衡的情况？（）"
    A. 直接训练模型，预测的时候调节阈值<br>
    B. 复制正样本，以增加正样本数量<br>
    C. 随机降采样负样本<br>
    D. 训练过程中，增加负样本的权重<br>

    正确答案: B C<br>

    解析：解决类别不平衡书中提出三种方法：<br>
    1. 下采样<br>
    2. 过采样<br>
    3. 阈值偏移<br>


!!! question "深度学习调参一般有哪些参数"
    1. 学习率：常用策略<br>
        - 学习率衰减<br>
        - 使用自适应学习率优化器，如Adam和Adagrad<br>

    2. mini batch：<br>
        - 小的mini batch size可能因为收敛的抖动比较厉害反而不容易卡在局部最低点<br>
        - 但是mini batch也不能太大，反而准确率下降<br>

    3. epoch：<br>
        - 用早停法选择合适的Epoch<br>
        - 观察validation error上升时就early stop<br>
        - 但是别一看到上升就停，再观察一下，因为有可能只是暂时的现象，这时候停止反而训练会不充分<br>

    4. 损失函数：<br>
        - 分类一般是softmax<br>
        - 回归一般是L2 loss<br>

    5. 激活函数：对于梯度消失现象<br>
        - Sigmoid会发生梯度消失的情况，所以激活函数一般不用，收敛不了<br>
        - Tanh(x)没解决梯度消失的问题<br>
        - ReLu(Max(0,x))比较好，代表Max门单元，解决了梯度消失的问题，而且起到了降维<br>

    6. 梯度问题：<br>
        - 梯度消失：当数值接近于正向∞，求导之后就更小，约等于0，偏导为0<br>
        - 梯度爆炸：数值无限大<br>

    7. 层数：<br>
        - 层数越多越灵敏收敛越好，但是容易过拟合<br>
        - 可以用Drop-out删除一些无效的节点<br>

    8. 过拟合解决方案：<br>
        - drop-out<br>
        - BN (batch normalization，归一化)<br>

    9. 其他模型参数：<br>
        - 隐藏层单元数(units)<br>
        - 时间序列模型的步长<br>
        - RNN的CELL类型(LSTM/GRU)<br>


## 23/24秋冬回忆卷

### 选择题

!!! problem "1. 哪个不属于人工智能的运用"
    选项：编译原理、人工生命等<br>

!!! problem "2. 通过图灵测试，则可以认为"		
    B. 具有人的智能<br>
    C. 从表现上来说，能够实现与人相似的智能<br>

    具有人的智能<br>

!!! problem "3. 下列哪个算法是按照某种规则遍历搜索空间的算法"
    A. DFS<br>
    B. BFS<br> 
    C. A*<br>
    D. 优先级搜索(例如贪心搜索、Dijkstra)<br>

!!! problem "4. 机器学习是"
    A. 人工智能的一种分支<br>
    B. 数据分析的一种技术<br>

!!! problem "5. 下面哪种算法不是盲目搜索"
    选项：宽度优先搜索、深度优先搜索等<br>

!!! problem "6. 判断谓词语句是否成立"
    应该是逻辑部分用归结原理假言定理等推理矛盾<br>

!!! problem "7. 关于欠拟合定义"
    选项：在训练集表现良好，测试集上表现很差等<br>

!!! problem "8. 下面哪些是常用的算法评价指标"
    A. 准确率召回率<br>
    B. MSE<br>
    C. MAE<br>
    D. AUC-ROC曲线和PR曲线<br>

    准确率、召回率、MSE、MAE、AUC-ROC曲线和PR曲线都是常用的算法评价指标。<br>
    其中准确率、召回率、AUC-ROC曲线和PR曲线主要用于分类问题，<br>
    MSE(均方误差)和MAE(平均绝对误差)主要用于回归问题。<br>
    
    $$
    MAE = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|
    $$

    其中 $y_i$ 是真实值，$\hat{y}_i$ 是预测值，n是样本数量。

!!! problem "9. 下面哪些指标可以评价回归"
    A. MAE<br>
    B. MSE<br>
    C. binary cross-entropy<br>
    D. L1-smooth<br>
    
    

!!! problem "10. 贝叶斯计算"
    概统简单题<br>

!!! problem "11. 下面哪种算法属于强化学习"

!!! problem "12. 人类智能特性"
    选项两短两长，有一选项为感知、学习、适应、创新<br>

!!! problem "13. 如果假设空间很大，应该用哪种方法搜索"
    选项忘了<br>

!!! problem "14. 关于人脸识别的流程顺序正确的是"
    人脸识别的基本流程顺序为：
    人脸检测 、关键点检测、人脸对齐 （通过关键点信息使人脸摆正）、特征提取 、人脸比对

!!! problem "15. 如果存在最优解，哪个算法一定能找到"
    A. BFS<br>
    B. 启发式<br>   
    C. DFS<br>
    D. 有限深度<br>

!!! problem "16. 概念学习定义"
    概念学习定义：<br>
    从有关某个布尔函数的输入输出训练样例中推断出该布尔函数



### 填空题

!!! problem "1. f(n)=g(n)+h(n)中g(n)和h(n)的含义"
    g(n)表示从初始状态到当前状态的实际代价，h(n)表示从当前状态到目标状态的估计代价

!!! problem "2. 人工智能的三个学派分别为"
    人工智能的三个学派分别为 **符号主义、连接主义、行为主义**

!!! problem "3. 人工智能的短期目标和长期目标分别是"
    人工智能的短期目标和长期目标分别是 **制造智能机器、实现机器智能**

!!! problem "4. BFS存储待搜索节点的数据结构_____，DFS存储已搜索节点的数据结构___"
    队列，栈

!!! problem "5. 根据Agent是否理解其所处的环境，将强化学习分为___和___"
    基于模型和免模型

!!! problem "6. Find-S用_____序的方法，在___结构上实现，每一步得到的假设都是在那一点上与训练样例一致的_____假设"
    more general than偏序、偏序链、最特殊的

### 简答题

!!! problem "1. alpha-beta剪枝"
    根据极大极小算法，简述alpha-beta剪枝的原理然后完成剪枝
    
    （1）对抗搜索节点回推值 
    （2）alpha-beta剪枝原理 
    （3）alpha-beta剪枝结果

!!! problem "2. 逻辑推理"
    已知"凡是干净的东西就有人喜欢""没人喜欢苍蝇" 
    
    （1）定义谓词 （2）写出逻辑表达式 （3）转换为标准子句 （4）利用归结原理证明"苍蝇不干净"

!!! problem "3. 过控流程设计"
    过控流程中有数据收集与分析、系统建模、控制系统设计、离线验证与测试、实地部署。请你设计流程，用至少三种本门课学习的方法解决可能遇到的问题，并说明可行性

!!! problem "4. 决策树"
    描述决策树的原理和优缺点

!!! problem "5. 朴素贝叶斯"
    描述朴素贝叶斯分类器的原理和应用场景

!!! problem "6. 梯度消失"
    描述梯度消失的概念和影响，谈谈自己的理解

!!! problem "7. Q-Learning"
    介绍Q-Learning并说明在强化学习中的作用

## 22/23秋冬 A卷
### 一、选择题（2分一道，20道，单选、多选混合）

1.人工智能定义
2.k折交叉验证
3.朴素贝叶斯分类器的假设前提
4. 一个人用Naive beyesian算某个特征得时候算了两遍，影响是：该特征决定能力增大；预测能力变弱、如果每个特征都重复算一遍则不影响；两个相似的特征不能用同一特征来表示；以上都错
5.有监督和无监督学习
6.激活函数
7.深度优先算法的实现
8.信息增益的计算
9.命题逻辑


假设最优解存在，以下哪个搜索算法能够能找到最优解：
A。广度优先（肯定不对，完备性：分叉b为无穷就找不到啦，最优性：前提是越浅的越优，不存在又深又更好的解）
B。深度优先（肯定不对，完备性就不一定）
C。有限深度优先（肯定不对，没有最优性）
D。启发式（肯定不对，取决于h(n)的设计，比如贪婪最好就没有）

### 二、简答题（5分一道，4道）


!!! problem "1. 智能的四种能力"
    - 感知能力<br>
    - 学习和自适应能力<br>
    - 记忆和思维能力<br>
    - 行为能力（人们对感知到的外界信息作出动作反应的能力）<br>

!!! problem "2. 人工智能的短期和终极目标"
    短期目标：制造智能机器<br>
    终极目标：实现机器智能<br>

!!! problem "3. P为原子谓词公式，则P和~P为_____"
    互补
    

!!! problem "4. Find-S算法"
    

!!! problem "5. 若P,R为F，Q为T，则(P∨R)→Q为___"
    T
    

!!! problem "6. Teacher(father(Zhan))的个体是"
    zhan，father(zhan)


    

### 三、大题

!!! problem "1. α-β剪枝"
    1. 倒推出下图各节点的权值
    2. 简述α-β剪枝的原理
    3. 用α-β剪枝，写出哪些分支可以剪掉

    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250107230206.png)

!!! problem "2. 评估函数"
    评估函数是什么，g(x),h(x)分别有什么作用

!!! problem "3. 归结推理"
    赵钱孙李四个人有人偷了张的东西。👮‍出动了5个侦探，A说赵和钱必有一个偷东西，B说钱和孙必有一个偷了，C说孙和李必有一个偷了，D说赵和钱必有一个没偷，E说孙和李必有一个没偷。要用归结的方式证明是谁偷了东西。

    0101,1010,0110都可以，顺序是：赵，钱，孙，李

!!! problem "3. 算法评估指标"
    算法评估中回归算法和分类算法有哪些指标？他们的优缺点分别是什么。

!!! problem "4. 过拟合与欠拟合"
    过拟合和欠拟合是什么？产生的原因又是什么？以决策树和神经网络为例，概述防止过拟合的方法



## 22/23秋冬 B卷

### 一、选择题
!!! problem "1. 如果问题存在最优解，则下面几种搜索算法中，哪种可以认为是'智能程度相对比较高'的算法"
    A. 深度优先搜索
    B. 宽度优先搜索
    C. 有界深度优先搜索
    D. 启发式搜索

    答案：D

!!! problem "2. 非(P 且 Q)=(非 P)或(非 Q)是什么律"
    答案：德摩根律

!!! problem "3. 人类智能具有的4项特性为"
    答案：自主性、反应性、适应性、社会性

!!! problem "4. 不属于知识的特征有哪些"
    选项有"复杂性与明确性""进化性相对性"

    答案：相对正确性、不确定性、可表示性

!!! problem "5. 贝叶斯公式考察"
    答案：

!!! problem "6. 强化学习中属于有模型算法的为"
    答案：AlphaZero

!!! problem "7. 关于搜索算法，下列说法错误的有"
    A. 宽度优先搜索可以看作一致代价搜索的特殊情况
    B. 一致代价搜索可看作A*搜索的特殊情况
    C. 贪婪最佳优先搜索是完备的
    D. 爬山法可以到达起点附近的最佳点

    答案：C

!!! problem "8. 给定谓词公式转换为子句式的结果是"
    答案：

!!! problem "9. 属于回归算法评估指标的有"
    选项有MAE, MSE, binary cross entropy等

    答案：MAE, MSE，l1-loss l1-smooth

!!! problem "10. 智能包含的四类能力"
    答案：感知能力、学习和自适应能力、记忆和思维能力、行为能力

!!! problem "11. 不属于人工智能三大学派的有"
    选项有符号主义学派，连接主义学派，控制论学派，信息论学派

    答案：控制论学派，信息论学派；三大学派：符号主义学派，连接主义学派，行为主义学派

!!! problem "12. 无监督学习不可以用来做什么"
    选项有"分类""数据降维"，"聚类"

    答案：分类

### 二、填空题
!!! problem "1. 谓词与函数的区别"
    答案：谓词返回真假值，函数返回具体的值

!!! problem "2. 若要用反证法证明P→Q，即需要证（）"
    答案：P且非Q为假

!!! problem "3. 给了永真的概念表述，问永真"
    答案：在任何解释下都为真的公式

!!! problem "4. 评价函数中h(n) g(n)的含义，其中（）又可叫效用函数"
    答案：h(n)是启发函数，g(n)是实际代价，h(n)又可叫效用函数

!!! problem "5. 个体常量、变元、函数统称为（）"
    答案：个体

!!! problem "6. 图灵测试的目的为（）"
    答案：判断机器是否具有与人类相似的智能

### 三、大题/简答题
!!! problem "1. 列举至少三种盲目搜索算法并简述其思想（4'）"

!!! problem "2. 决策树算法中以什么为依据来划分节点？请说明如果以序号作为划分属性，为什么不能用基于信息增益的划分方式。"

!!! problem "3. 多变量决策树的优点与缺点（5'）"
    答案：

    多变量决策树的优点：
    1. 可以处理非轴平行的决策边界，提高分类准确性
    2. 可以减少树的深度，提高模型的可解释性
    3. 对数据的利用更充分，可以发现属性间的相关性

    缺点：
    1. 计算复杂度高，训练时间长
    2. 容易过拟合
    3. 模型解释性相对较差，不如单变量决策树直观
    4. 对噪声数据更敏感


!!! problem "4. 神经网络过拟合问题的解决方式（5'）"

!!! problem "5. 神经网络中梯度消失与梯度爆炸的产生原因，以及如何避免"
    答案：

    神经网络中梯度消失和梯度爆炸的原因：

    1. 梯度消失
    - 使用 sigmoid、tanh 等饱和激活函数,导数值域在(0,1)之间
    - 多层网络中,每层的梯度会连乘,导致梯度越来越小
    - 网络层数过深时尤其明显

    2. 梯度爆炸 
    - 权重初始化不当,值过大
    - 学习率设置过大
    - 网络层数过深时梯度累积

    解决方法：

    1. 梯度消失
    - 使用 ReLU 等非饱和激活函数
    - 使用残差连接(ResNet)
    - 使用 Batch Normalization
    - 合理初始化权重

    2. 梯度爆炸
    - 梯度裁剪(Gradient Clipping)
    - 使用 L1/L2 正则化
    - 使用 Batch Normalization
    - 调小学习率
    - 合理初始化权重

!!! problem "6. 考归结原理，比较简单"

!!! problem "7. 候补消除算法，是作业题，下图中打勾的那问"
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250107224014.png)

!!! problem "8. 八数码问题（背景要求同小测题 见下图，不过问题问法不同）"
    （1）请你设计评价函数f(x)
    （2）给出了各步搜索的图示，问各步的评价函数f(x)的值（会算就行，不用画图）
    （3）请填写每一步搜索的open-closed表
    ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20250107224030.png)

## 其他题目

### 简答题

!!! problem "1. 效用函数"
    $f$ 是启发式搜索的效用函数，是当前路径的评价指标；$g$ 是得分函数，代表当前点到目标点的得分，$h$ 是耗散函数，代表当前点到起始点的距离。

!!! problem "2. 对抗搜索与αβ剪枝"
    这题给了一个对抗搜索树，在最末端给出了他们的值，要求把每一个节点的值都表示出来；然后进行αβ剪枝。

!!! problem "3. 学习率对神经网络的影响"
    太大不收敛，太小学不动。

!!! problem "4. 信息增益的公式以及何时它达到最大"
    信息增益的公式为：

    $$
    Gain(D,a) = Ent(D) - \sum_{v=1}^V \frac{|D^v|}{|D|} Ent(D^v)
    $$

    信息增益在以下情况下达到最大：
    1. 当属性$a$将数据集$D$完全划分为纯净的子集时，即每个子集$D^v$中的样本都属于同一类别
    2. 当属性$a$的划分使得子集的熵之和最小时
    3. 当属性$a$的划分使得类别的分布最均匀时

    需要注意的是，信息增益倾向于选择取值较多的属性，这可能导致过拟合。为解决这个问题，可以使用信息增益率等改进指标。

    


### 大题

!!! problem "1. 深度优先搜索和广度优先搜索"
    给了一个课上类似但简化了的地图，要求用两种方法搜索A至E的最佳路径；然后对两种方法进行对比。



!!! problem "3. 极大似然假设"
    D中含有$x_i$和$y_i$，$y_i=h(x_i)+e_i$，$e_i$服从偏差为零的正态分布，求证极大似然假设等价于$y_i$和$h(x_i)$的平方和误差最小。
    
    $$
    h = \arg\max P(h|D) = \arg\max \frac{P(D|h)P(h)}{P(D)} = \arg\max P(D|h) = \arg\max P((x_i, y_i)|h)
    $$

    
    要使其最大，就要使$y_i$和$h(x_i)+e_i$尽可能接近，即:
    
    $$
    h = \arg\min E((y_i-h(x_i)-e_i)^2) = \arg\min [E((y_i-h(x_i))^2)-2E((y_i-h(x_i))e_i)+E(e_i^2)] = \arg\min E((y_i-h(x_i))^2)
    $$

!!! problem "4. 决策树"
    根据气温、天气、温度、适度的情况判断是否打网球，给出了十四条数据，根据信息增益算决策树的节点先后顺序。

    这个题比较常规，看一下西瓜书上的例题。
    但是非常耗时间，如果没有计算器是不可能完成的。




## 复习
整理了一下朋友们和各位前辈的分享，感谢大家

（自动化资料也是多起来了hhh）
### 复习资料
- [复习资料 RrQqSsYy](https://www.cc98.org/topic/5533160)<br>
- [复习资料 云高天遥](https://www.cc98.org/topic/5518130)<br>
- [复习资料 zhyyyyyyyy](https://www.cc98.org/topic/5509967)<br>
- [复习资料 handsome-boy](https://handsome-boy.notion.site/174c1b264eda8067b2a2caa01145d00e?pvs=4)<br>
- [复习ppt+平时作业分享 - the_Piao](https://www.cc98.org/topic/6088456)<br>
- [人机复习笔记 - MyAmigo](https://www.cc98.org/topic/6088275)<br>
- [复习笔记 & 题目整理 - PhilFan](https://www.philfan.cn/CS/AI/ML-CSE/)<br>
- [人机笔记 - 小胖一族](https://skillful-vest-b8d.notion.site/b80fddf304ea4e9bbca7e978f8d1e600)<br>
- [笔记与回忆卷整理 - Twinkle](https://awslasasd.github.io/Class/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/)<br>

### 回忆卷
- [24-25年 秋冬 回忆卷 FLOG司马](https://www.cc98.org/topic/6089499)<br>
- [22-24年 考题整理- FLOG司马](https://www.cc98.org/topic/6089023)<br>
- [2022-2023秋冬 回忆卷 Valkyrie](https://www.cc98.org/topic/5508899)<br>
- [2022-2023秋冬 回忆卷 桂物](https://www.cc98.org/topic/5508902)<br>
- [2022-2023 秋冬 回忆卷 枕流](https://www.cc98.org/topic/5234359)<br>
- [2022-2023 秋冬B 回忆卷 XD233](https://www.cc98.org/topic/5532570)<br>
- [23-24 秋冬 复习资料+回忆卷 rickyman](https://www.cc98.org/topic/5797154)<br>
- [23-24秋冬 回忆卷 KrAulegend](https://www.cc98.org/topic/5796633)<br>
- [2023-2024 秋冬《人工智能与机器学习》回忆卷 - CC98论坛](https://www.cc98.org/topic/5796623)<br>
- [23-24春 机器人班](https://www.cc98.org/topic/5875928)<br>
- [23-24春 机器人班级](https://www.cc98.org/topic/5875948)<br>

### 网上其他资料
- [BAT机器学习1000题目](https://www.cnblogs.com/ciao/articles/10894568.html)<br>
- [神秘模拟卷](https://www.doc88.com/p-99037881885423.html)<br>
- [机器学习笔试面试题——day4](https://blog.csdn.net/selinaqqqq/article/details/95084129)<br>
- [机器学习常见问题与解答-CSDN博客](https://blog.csdn.net/will130/article/details/50704205)<br>
- [BAT机器学习面试1000题系列（第1\~305题](https://blog.csdn.net/v_july_v/article/details/78121924)<br>
[机器学习笔试题精选（二](https://blog.csdn.net/red_stone1/article/details/81023976)<br>
- [机器学习常见问题与解答-CSDN博客](https://blog.csdn.net/will130/article/details/50704205)<br>
- [机器学习常见问题与解答-CSDN博客](https://blog.csdn.net/qq_44528283/article/details/114399093)<br>
