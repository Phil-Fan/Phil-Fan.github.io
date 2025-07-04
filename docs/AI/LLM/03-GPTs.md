# GPT


!!! note "主要介绍一下decoder技术路线的模型，以GPT系列为主"

## Acknowledgement

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=296939123&bvid=BV1AF411b7xQ&cid=541096351&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width=100% height=450px></iframe>

写笔记的时候也参考了“产品黄叔”、“小清舍”等用户的笔记

[通向AGI之路：大型语言模型（LLM）技术精要 - 知乎](https://zhuanlan.zhihu.com/p/597586623)



## 发展历程与chitchat

ImageNe有标号的图片和文字对应关系的数据集，100万的量



换算到文本，1张图片的信息对等于10个句子，意味着自然语言处理需要1000万的标好的数据集才能够进行训练。



之前都是计算机视觉在引领潮流，现在来到了自然语言处理届，然后很多创新反馈回CV。



CLIP打通了文本和图像。



16:46半监督学习（自监督学习）



![img](https://i2.hdslb.com/bfs/note/f1d4be3d8e495ce8be0cb94c5511e762b7b22f20.jpg@690w_!web-note)

GPT2，搜集了更大的数据集，训练了一个更大的模型。



GPT3比GPT2数据和模型都大了一百倍，暴力出奇迹。



OPenAI想解决更大的问题。



GPT-3模型更复杂，要求更高，很难复现，因此引用较少，想往强人工智能走，解决更大问题

transformer解决机器翻译，一个序列到另外一个序列

Bert想把计算机视觉成熟的先训练一个预训练的模型然后再做微调出子任务的结果，然后搬到NLP上做好，提升技术的效果

在同样模型大小，比如是一个亿级别模型大小时候

Bert的性能要好于GPT

所以未来文章更愿意用bert文章，因为更容易找到足够的机器把模型跑起来



## GPT

Improving Language Understanding by Generative Pre-Training

https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

unlabeled data 如何进行训练

- 困难1：优化目标函数较难寻找
- 困难2：NLP子任务差别较大，所以没有一个统一的简单范式，把学到的文本表示传递到下游的子任务上面；

### 核心卖点：Pretrained + 微调

我有一些标好的数据，但我还有大量的相似的没有标好的数据，我怎么样把这些没有标好的数据用过来，这就是半监督学习想学习的东西。



半监督学习现在被统称为自监督学习（Self supervised Learning）







摘要

NLP领域没有像ImageNet那样那么多标好的数据，因此没有足够多的数据去训练一个比较大的模型，就不能使用CV当中先训练好预训练模型再做微调的范式

但使用的是没有标号的文本，因此走了一大步，然后在GPT系列后面的文章做Zero Shot

提出半监督方法（后面称之为自监督学习）



基于transformer模型架构，发表在transformer出来一年之后，和RNN模型相比transformer在迁移学习的时候学习到的特征更加稳健一些，可能是因为其里面有更加结构化的记忆使得能够处理更长的文本信息从而能够抽取出更好的句子层面和段落层面的语义信息

GPT在做迁移的是后用的是一个任务相关的输入的一个表示

相关工作

- GPT在没有标注的数据上如何进行训练
- 在训练好之后，如何在有标注的数据集上面进行微调
- 子任务如何表示输入



### 优化目标函数

$$
L_{1}(\mathcal{U})=\sum_{i}\log P(u_{i}|u_{i-k},\ldots,u_{i-1};\Theta)
$$

这里的优化函数的含义是指在给定前面$k$个词汇以及模型$\Theta$，预测出下一个词的似然

这里$k$指的是窗口的大小，是一个超参数









GPT是预训练模型，是Transformer的解码器。

!!! note "与BERT的区别"

主要的区别是优化目标函数的选取：GPT是要更难的，天花板更高

> GPT类似于已知过去的股票价格，去预测未来一天的股票价格
>
> 而BERT是已知今天以前之前的股票价格，预测昨天的。

BERT相当于完形填空，可以看到前后的句子，所以可以使用Transformer的编码器。而GPT看不到后面的词汇，所以用的是Transfomer的解码器

这是作者为何一直不断的把模型做大，一直不断努力最后才能做出GPT3。选择了更难的技术路线，但很可能天花板就更高。







Transformer的解码器，只看当前词和词之前的信息，不看后面的词。

选用transformer解码器（有掩码机制）

微调标号



$$
P(y|x^1, \ldots, x^m) = \text{softmax}(h_l^m W_y)
$$



$$
L_2(C) = \sum_{(x,y)} \log P(y|x^1, \ldots, x^m)
$$



给你一个序列预测这个序列的下一个词

给你完整的序列预测序列对应的标号两个一起训练效果是最佳的

$$
L_3(\mathcal{C})=L_2(\mathcal{C})+\lambda*L_1(\mathcal{C})
$$

### 输入表示

加入了开始符、分隔符、结束符

这在之前的模型中是没有的

![img](https://i2.hdslb.com/bfs/note/a8f41f109cc5a897c575dce166e262dba3a66e5a.png@624w_!web-note)

- 第一行是分类

- 第二行是蕴含，下一句的假设是否被上一句的事实所支持。比如上一句是A送B玫瑰，下一句是A喜欢B。

- 第三行是相似

- 第四行，多选题，选答案。算置信度，选最大的那个。

都可以构造成序列，预训练好Transformer的模型，不变。





### 参数

12层 768维度

用的12层解码器，每一层768个维度。

### 数据集

BooksCorpus数据集：有7000篇没有发表的书



## GPT-2

Language Models are Unsupervised Multitask Learners





### 核心卖点：**Zero-Shot**——不在下游任务微调

现在的模型，泛化性不好，一个数据集在一个应用上面不错，但不好应用在另一个应用。举例，我拿来写情书OK，但写PRD不OK。



Multitask Learning，多任务学习，训练一个模型的时候，同时看多个数据集。但在NLP上用的不多。



现在流行的还是，预训练，然后再对每一个任务做有监督的学习的微调。**这样的问题就是对于每一个任务都需要重新微调，以及要导入有标号的数据。**



zero-shot要做的就是在下游任务的时候，不需要下游任务的信息，也可以进行

下游任务不能出现没有见过的符号，不然模型会非常困惑

- prompt



!!! note "新意度"

沐神关于做研究的启发： 做研究不要一条路走到黑，做过程你可以一条路走到黑，但是在做研究的时候，你要灵活一些，不要一条路走到黑。你需要尝试从一个新的角度来看问题。  gpt2还是做语言模型，但是在做到下游任务的时候，会用一个叫做zero-shot的设定，zero-shot是说，在做到下游任务的时候，不需要下游任务的任何标注信息，那么也不需要去重新训练已经预训练好的模型。这样子的好处是我只要训练好一个模型，在任何地方都可以用。 如果作者就是在gpt1的基础上用一个更大的数据集训练一个更大的模型，说我的结果比Bert好一些，可能也就好那么一点点，不是好那么多的情况下，大家会觉得gpt2这篇文章就没什么意思了，工程味特别重。那么我换一个角度，选择一个更难的问题，我说做zero-shot。虽然结果可能没那么厉害了，没那么有优势，但是新意度一下就来了。





### 数据集

Common Crawl，这是有一群人写的一个网络爬虫，不断的去网上抓取网页。TB级的数量级，但数据需要清洗，很麻烦。



后面用Reddit，大家可以自主的放网页上去，大家可以投票，Karma是用户对帖子的评价，选取有3个Karma的帖子，拿到4500万的链接，一共有800万个文档，40GB的文字



### 参数



GPT-2 15亿参数，百万网页的数据集：WebText。



### 实验

与别的zero-shot进行比较

![img](https://i2.hdslb.com/bfs/note/6f580e9c03f8fd2e43ce97ed4c8cf9868abfe2dd.jpg@690w_!web-note)

GPT2在很多任务上得分并不高，更多地看起来还是在讲Zero-Shot的问题。







## GPT-3

language models are few-shot learners



### 核心卖点：不训练、不梯度更新、上下文学习

微调问题：

1. 对于每一次都需要一些标号的数据；
2. 微调效果好，不一定模型的泛化性能好：不允许微调，那么拼的就是预训练模型的泛化性能
3. 人类不需要很大的数据集来学会绝大部分的语言任务

GPT3不去更新梯度，不做微调

- meta learning： 训练一个很大的模型，泛化性能不错

- “In-Context learning”：即使给了一些样本，GPT3因为模型太大了，更新不了，所以不会去更新所谓的权重。

### 参数：1750亿

自回归模型，1750亿个可学习的参数，





W_E GPT3 50267个token，每个token具有12288维度，共6亿左右参数，随机初始化



### 数据集

多个数据集，不同采样率

- 过滤：common crawl作为负例，GPT2数据集作为正例，做一个logistic regression而分类
- 去重：lsh算法（局部敏感哈希），去掉相似的文章



### 训练方法

DGX-1集群，带宽非常高



### 评估



评估GPT3：

1. few-shot：每个子任务提供10-100个训练样本；
2. one-shot：1个样本
3. zero-shot：0个样本



- 分类：true/false
- 补全：beam search

### 训练结果

power law：不需要过度训练



使用validation loss是因为与子任务精度有关系

数据量指数翻倍的时候，验证精度是线性下降的





GPT3模型偏扁

使用相对比较大的批量大小，计算性能更好，每台机器的并行度更高，通讯量变低，降低批量里的噪音分布式比较好

小的模型批量大小更容易过拟合一些

模型越来越大的时候过拟合没有那么的严重，搜索范围更广，可能存在一个比较简单的模型架构，SDG可以帮助找到那个模型，使泛化精度更好一些

模型批量大小增大学习率下降

### 局限性

- 长文本比较弱，写小说就不行。

- 结构和算法上的局限性，只能往前看。（原因：使用的是transformer的解码器的原因）

- 对于词的预测是平均的，不知道什么词才是重点。虚词。

- 视频、真实世界的物理交互是无法理解的

- 样本有效性不够

- 训练起来非常的贵

- **无法解释，不知道为何得出的输出**



负面：

1. 可能会被用来做坏事
2. 散布一些不实的消息
3. 论文造假
4. 公平性、偏见
5. 性别





## GPT-4





## Interpretability

词汇存在高维向量当中，向量的方向可以编码不同的含义

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202507040930043.png)

transformer大部分的参数在MLP层当中（约占用2/3的参数，GPT3 - 12亿）

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202507040940946.png)

第一个线性层可以使用行视角，视作嵌入空间中的方向

ReLU 类似于与门，只有最终结果为正数时，才会输出

第二个线性层，可以使用列视角，如果某个列向量学习到了“篮球”的概念，同时对应的向量又被激活


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/202507040938039.png)


在$N$维空间当中，如果使用正交基表示一个概念，那么最多只能表示$N$个概念

johnson-lindenstrauss lemma 告诉我们，如果使用非正交基，那么可以表示更多的概念，尤其是在高维空间当中。能表示的概念数量与维数$n$成指数分布

这也说明，某个概念并不是单纯由一个单元激活，而是由多个单元激活（superposition）

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113215035936825&bvid=BV1aTxMehEjK&cid=26046694390&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height=450px></iframe>

### 拓展阅读
芝加哥大学victor veitch 的论文

Anthropic Transformer circuit

[Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)

[Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html)

- RLHF
- scaling law







