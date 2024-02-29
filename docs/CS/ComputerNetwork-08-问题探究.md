# 有趣问题探究

## 排队延时问题

本书作者制作的[排队延时的可视化动画](https://media.pearsoncmg.com/ph/esm/ecs_kurose_compnetwork_8/cw/content/interactiveanimations/queuing-loss-applet/index.html)

![image-20240229213626432](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240229213626432.png)



### $\frac{L \cdot a}{R} > 1$​时

队伍显然越来越长，直到发散

### $\frac{L \cdot a}{R} = 1$时

分为几种情况

- 周期性到达，很规律，来一个发一个，这个时候没有排队延时

  > 类似流水线

- 短时间集中，但是也是规律的；这个时候排队延时是等差数列，平均一下即可

  > 类似车队下高速

- 随机到达，书中只描述了一个趋势：

  即趋于0的时候排队延时也趋于0，流量强度趋于1时候，排队延时趋于正无穷。

  但是也没有说具体数学模型

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240229211257617.png" alt="image-20240229211257617" style="zoom:50%;" />


### 查询资料

网上资料假设了两个前提

1. 到来分组符合**泊松分布** 

   >在给定间隔内期望有$λ$ 个事件的泊松分布下，同一间隔内 $k$ 个事件的概率为
   >
   >$\frac{\lambda^k e^{-\lambda}}{k!}$

2. **分组等长**

证明：在这些假设前提下，流量强度=1时候，排队延迟无限大

Denote 到达率为$l$，处理速率为$u$，也就是该条链路的带宽，流量强度$p=\frac{l}{u}$

考虑到处理单个等长的数据包的时间应该是固定的，根据排队论的知识和Kendall表示法，符合M/D/1模型，进而由公式得到

平均分组数量
$$
Ls=p+\frac{1}{2}\cdot\frac{p^2}{(1-p)}
$$

平均排队延时
$$
Wq=\frac{p}{2u(1-p)}
$$
可以看到p趋向于1时分母为0，排队延时趋于无穷。



### ref

[M/D/1 queue - Wikipedia](https://en.wikipedia.org/wiki/M/D/1_queue)

[为什么流量强度为 1 时排队时延是无穷？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/317549997)

[OM | 浅谈排队论 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/99131787)

