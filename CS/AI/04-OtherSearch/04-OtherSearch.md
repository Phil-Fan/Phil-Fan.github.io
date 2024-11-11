# 博弈
## Minimax 搜索

我方是绿色：越大越好
对方是红色：越小越好

最朴素的方法就是从叶子节点向上回溯


Minimax 算法又叫极小化极大算法，是一种找出失败的最大可能性中的最小值的算法。

在局面确定的双人对弈里，常进行对抗搜索，构建一棵每个节点都为一个确定状态的搜索树。奇数层为己方先手，偶数层为对方先手。搜索树上每个叶子节点都会被赋予一个估值，估值越大代表我方赢面越大。我方追求更大的赢面


来看一个简单的例子。

称我方为 MAX，对方为 MIN，图示如下：

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241106204322.png)

例如，对于如下的局势，假设从左往右搜索，根节点的数值为我方赢面：

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241106204330.png)

我方应选择中间的路线。因为，如果选择左边的路线，最差的赢面是 3；如果选择中间的路线，最差的赢面是 15；如果选择右边的路线，最差的赢面是 1。虽然选择右边的路线可能有 22 的赢面，但对方也可能使我方只有 1 的赢面，假设对方会选择使得我方赢面最小的方向走，那么经过权衡，显然选择中间的路线更为稳妥。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241106204340.png)

实际上，在看右边的路线时，当发现赢面可能为 1 就不必再去看赢面为 12、20、22 的分支了，因为已经可以确定右边的路线不是最好的。


### 分析
性能：

- 完备性：Yes，如果树有限
- 最优性：Yes
- 时间复杂性：$O(b^m)$
- 空间复杂性：$O(bm)$

极大极小算法将**所有子树全部扫描，极其浪费时间和空间**



## alpha-beta剪枝算法
对MinMax算法的优化，产生的结果完全相同，但运行效率不一样

基本思想：根据上一层已经得到的当前最优结果，决定目前的搜索是否要继续下去

两个假设：

- 整个博弈属于零和博弈，即一方的收益必然意味着另一方的损失
- 博弈双方足够聪明，即每一方在决策时总会选择使自己利益最大化的决策

算法流程详见：https://oi-wiki.org/search/alpha-beta/

- 对于Max层，本体值为$\alpha$；对于Min层，本体值为$\beta$
- 初始情况均为$\alpha=-\inf,~\beta=+\inf$
- 按照**先序遍历的顺序**
- **向上传递：更新本体值**
- **向下传递：复制$\alpha$，$\beta$的值到子节点**
- 若在某一节点更新后出现$\alpha>\beta$，则其后面不需要再进行更新，直接剪枝即可

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241106205632.png)


### 分析
- 剪枝不会影响最终结果
- 剪枝效率很大程度上取决于检查后继的顺序
- 理想排序下先检查可能最好的后继，时间复杂度从$O(b^m)$降低到$O(b^{m/2})$

### 实现

???+ note "参考代码"

    ```cpp
    int alpha_beta(int u, int alph, int beta, bool is_max) {
      if (!son_num[u]) return val[u];
      if (is_max) {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          alph = max(alph, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return alph;
      } else {
        for (int i = 0; i < son_num[u]; ++i) {
          int d = son[u][i];
          beta = min(beta, alpha_beta(d, alph, beta, !is_max));
          if (alph >= beta) break;
        }
        return beta;
      }
    }
    ```

<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=405104472&bvid=BV1yG411o7uH&cid=1243642275&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="500" height="300"></iframe>

## 蒙特卡洛树搜索


## 参考资料
[详解Minimax算法与α-β剪枝-CSDN博客](https://blog.csdn.net/wenjianmuran/article/details/90633418)

[y_lz的笔记本](https://skillful-vest-b8d.notion.site/AI-edb0292f25db4b428b34042aff7bef0c#ce0fffc50e57478d802af27eb41d1ff1)