# 05 | Tricks
## 正则化






正则化约束参数的大小

如何验证正则化的大小


### dropout
Randomly drop units (along with their connections) during training
§ Each unit is retained with a fixed dropout rate p, independent of other units
§ The hyper-parameter p needs to be chosen (tuned)
o Often, between 20% and 50% of the units are dropped

### Early-stopping


Batch normalization layers

## 多GPU


## 可视化方法

https://blog.csdn.net/qq_45258632/article/details/145030407

1. 🇺🇸Tensorboard: 老牌工具，尚能饭否

Tensorboard，包括用于 Pytorch 的 TensorboardX，Tensorboard 本身被设计成插件化的方式，好处是轻量、轻耦合，可以按需要很快的自定义一个新的 tab，这种方式的缺点是缺少一个用户整体的视图，用户很难在宏观视角上对整个训练流程有一个比较清楚的认识。

​​

特点:

出的比较早，格式通用，但功能相对单薄，用户体验已跟不上新的工具
虽然是跟 Tensorflow 出的，但并不仅限于 Tensorflow，Pytorch也能用（通过TensorboardX）
实验全流程记录
报表和跟其他系统的兼容性比较好，因为出的早?..
适合单人使用，没有团队功能
开源项目里带的比较多
‍

2. 🇨🇳SwanLab: 国产新星，简洁易用

SwanLab是2024年推出的深度学习可视化工具，来自一支年轻的中国团队，支持云端+离线两种使用方式。SwanLab的UI设计应该是所有这类工具里面最现代的、交互最阳间的（类似Vercel的Next设计风格），Python API的设计基本上对标Wandb做的，综合实力不错。不过因为比较新的关系，一些高级功能还有待完善。

​​

​​

特点:

整体UI交互体验拉满，很好看
有云端版，所以手机上也能看实验
适配框架很多，有接近30个，基本上主流的不主流的都覆盖了；因为是中国团队的关系，也适配了很多国产框架（LLaMA Factory、XTuner、ModelScope Swift等等）
实验全流程记录，超参数记录，日志记录，硬件环境记录，GPU实时监控，Python库记录，一体化表格对比
支持华为昇腾显卡，应该是这类工具里唯一一款能记录昇腾NPU的显存变化的
支持团队使用
推出时间较短，所以一些功能还有待健全，比如超参数搜索、模型数据存储这些都还没有
‍

3. 🇺🇸Wandb: 云端协作，功能强大

wandb 就是 Weights & Biases，出的比较早，团队最早是因为tensorboard不是很好用，所以重新设计了一个实验跟踪可视化系统，Python API设计的很简洁易用。在综合功能上应该是最强的，有不少像超参数搜索、模型存储这样的功能。在UI交互上有些地方设计不是很好，用久了会会有点烦躁；以及因为服务器在海外的关系，访问和上传容易炸。​

特点：

功能很完善，基于cover了上面提到的基本功能，覆盖了机器学习pipeline的各个环节
Reports 功能很有特点，基本上就是把你的实验整理成一个 blog 文档，你做的什么实验、怎么做的、选的那些参数为什么这么选，都可以有个记录，形成文档之后可以把相关的实验附上去，请团队的人或者其他感兴趣的人一起来探讨，隐隐有点社区的意思，赞！
支持团队使用
服务器在海外，国内用起来有点顶，网页经常要加载半天
