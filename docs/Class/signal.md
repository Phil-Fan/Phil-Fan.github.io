# 信号分析与处理

???+note "课程信息"
    === "回忆卷"
        [2022-2023 春夏《信号分析与处理》回忆卷](https://www.cc98.org/topic/5638145)<br>
        [2023电气学院信号分析与处理回忆卷](https://www.cc98.org/topic/5637543)<br>
        [信号分析与处理（控院电院）2022春夏回忆卷](https://www.cc98.org/topic/5352194)<br>
        [2022春夏 信号分析与处理 部分回忆卷及复习建议](https://www.cc98.org/topic/5352226)<br>
        [《信号分析与处理》2020-2021春夏期末回忆卷及复习整理](https://www.cc98.org/topic/5111712)<br>


    === "资源"
        [《信号分析与处理》课件例题整理](https://www.cc98.org/topic/5642928)<br>
        [梁毅浩学长资料](https://www.cc98.org/topic/5111712)<br>
        [张建老师ppt](https://www.cc98.org/topic/5621768/postid/822283147)<br>
        [赵光宙习题答案](https://wenku.baidu.com/view/c80a2f629b6648d7c1c746e5.html?_wkts_=1706713380659)<br>
        [赵光宙第二版答案](https://www.cc98.org/topic/4838843)<br>
        [信号分析与处理 郑军老师 实验指导书](https://www.cc98.org/topic/3930519)<br>
    

## 信号分类 + 连续信号分析

![连续信号](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%25E8%25BF%259E%25E7%25BB%25AD%25E4%25BF%25A1%25E5%258F%25B7.svg)

模拟信号和数字信号的定义

模拟：时间幅度均连续

离散：时间幅度均离散

**幅度信号和功率信号**

幅度有限的周期信号必定是功率信号 **正确**



**信号的变换**

- 要注意所有变换都是针对自变量而言的。要注意正负号的问题



**采用正交分解的视角观察**
补充知识：正交基下的坐标求解，复向量的内积求法。

推荐几篇写的很好的博客[CFS](https://zhuanlan.zhihu.com/p/418211643),[CTFT](https://zhuanlan.zhihu.com/p/418220682),[DFS](https://zhuanlan.zhihu.com/p/418221087)

!!! bug
    写出非周期连续信号傅里叶变换和周期连续信号傅里叶变换的公式，并简述他们的特点。

### **傅里叶变换的各种性质**

比较重要，需要反复记忆背诵

!!! bug 
    $\mathscr{F}(Sa(\frac{t}{2})) = ?\quad \int_{-\infty}^{\infty}Sa(\frac{t}{2})dt = ?$
    解答：<br>第一问使用CFT的尺度变换性质<br>第二问先把t替换成$\omega$,使用ICFT看作求解x(0)的问题即可.所以任务变成了求解$Sa(\frac{\omega}{2})$​的原函数，就不难了



微分性质，需要注意直流分量的处理；注意突变的信号求导时候要写$\delta(t-t_0)$

最保险的方法是把原函数的解析表达式写出来然后一步一步求微分


各种常见信号傅里叶变换需要记住

- $cos(\omega_0 t)$频谱搬移
- 门函数的表达 $u(t) - u(t-t_0)$



**帕斯瓦尔定理**

从时域和频域分别表述信号的能量

n维空间的勾股定理
[可以看这篇回答](https://www.zhihu.com/question/326625744/answer/3074587071)

### **周期信号的傅里叶变换（!!非常重要）**

周期信号可以表示为

$$
\begin{align}
x(t) &= \mathop{\Sigma}\limits_{n=-\infty}^{\infty}X(n\omega_0)e^{jn\omega_0t}\\
X(\omega) &= \mathscr{F}(\mathop{\Sigma}\limits_{n=-\infty}^{\infty}X(n\omega_0)e^{jn\omega_0t})\\
&= X(n\omega_0)\mathscr{F}(e^{jn\omega_0t})\\
&=X(n\omega_0)\mathop{\Sigma}\limits_{n=-\infty}^{\infty} 2\pi \delta(\omega - n \omega_0)
\end{align}
$$

!!! note "例子:求周期为$T_0$的周期性冲激串$\delta_T(t)$的傅里叶变换。"

    $$
    \begin{align*}
    \delta_T(t)&= \mathop{\sum}\limits_{n=-\infty}^{\infty}\delta(t-nT_0)\\
    \delta_T(t)&= \mathop{\sum}\limits_{n=-\infty}^{\infty}X(n\omega_0)e^{jn\omega_0t}
    \end{align*}
    $$

    又因为在一个周期内
    $X(n\omega_0) = \frac{1}{T_0} \int^\frac{T_0}{2}_{-\frac{T_0}{2}} \delta_T(t)e^{-jn\omega_0 t} = \frac{1}{T_0}$
    **所以可以求得**
    
    $$
    \begin{align*}
    X(\omega) = \mathop{\sum}\limits_{n=-\infty}^{\infty} 2\pi \frac{1}{T_0} \delta(\omega-n \omega_0) = \omega_0 \mathop{\sum}\limits_{n=-\infty}^{\infty}{\delta(\omega-n \omega_0) }
    \end{align*}
    $$
    
    **该式子在推导时域、频域采样定理时候反复出现**



## 离散信号的分析

![离散信号](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E7%A6%BB%E6%95%A3%E4%BF%A1%E5%8F%B7.svg)

**常见离散信号、信号的时域计算**
关于信号卷积、相关性和反卷积，可以看[这一篇](https://zhuanlan.zhihu.com/p/196786958)

相关可以看作是向量内积的推广（内积为两向量点乘，其物理意义为将一个向量投影到另一个向量）：

$$
<\vec{a},\vec{b}> = \vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cos \theta
$$

内积越大，投影越大，两个向量间夹角越小，方向越一致，相似度越高。特别地，当内积为0时，两个向量是垂直的；只有当两个向量夹角为0时，内积最大（相关系数也最大）。因此，相关可反映两个向量空间的夹角。

### 时频域采样定理(!!!很重要)





### **卷积的计算方法**

对位相乘求和

### **归一化角频率**(!!!!!核心中的核心)

$\Omega$的单位是弧度，表示的是一个采样周期内转过的角度，自然而然可以得出计算公式

$$
\Omega = \omega_0 T_s = \frac{2\pi}{T_0}T_s = \frac{2\pi}{N T_s}T_s = \frac{2\pi}{N}
$$

其中，$\Omega$是数字角频率，$T_s,w_s$是采样，$\omega_0$是模拟角频率，$N$采样点数

- 采样时长$T = N\cdot T_s$
- 模拟角频率$\omega_0 = \frac{2\pi}{T_0} = 2\pi f_0$

- 实际频率$f = \frac{f_s}{N} \cdot K$

原因：我们拿到一串数字信号，不可能还附带着把采样间隔也告诉你。或者说，信号就是信号，在这组关于时间的一维信号上是没有采样率这样的信息的。有一个大聪明发现，反正经过采样后的数字信号在频域上是周期性的，这个周期只与采样率有关，那我**想办法忽略采样率，让周期都变成$2\pi$**，岂不是更好，那样很多算法就通用了。所以搞出来一个归一化角频率。

**DFS的推导**
课本：利用冲激函数串进行采样，计算傅里叶变换（参考对周期函数进行傅里叶变换的例题）

[这篇文章](https://zhuanlan.zhihu.com/p/418221087)给出了从正交分解的视角看待DFS。


!!! bug "正交基必须与原向量等维度"

!!! bug "内插公式如何理解"

**DFS性质**

共轭对称性
若$x(n) \stackrel{DFS}{\longrightarrow} X(k\Omega_0)$，则有

$$
x^*(-n)\stackrel{DFS}{\rightleftharpoons} X^*(k\Omega_0)
$$

证明：

!!! bug "各种对称性如何理解：共轭对称"

### **FFT算法**

[张健智云01-四种变换总结+FFT开头](https://vod.cmc.zju.edu.cn/default/2024/04/25/31e3e7edf9545c28bd0b4662d92b7bb3_1920_1080.mp4?auth_key=1718711773-0-0-770f3dc5eb4dc4974c8488d614155b80&t=636426-1718697487-4cbc4d619c41b4ee4b763e161565061a)

[张健智云02-FFT计算](https://vod.cmc.zju.edu.cn/default/2024/05/09/b83939657f5025d61f36c484fa1c8b2e_1920_1080.mp4?auth_key=1718712318-0-0-b617cdf8ed64cf6f52632bb39f87c02d&t=636426-1718697921-5e4148b13c439b8655a2e0a039f4a074)

[张健智云03-FFT谱分析误差](https://vod.cmc.zju.edu.cn/default/2024/05/11/2d522960da558ee3491a97e579c5b7e9_1920_1080.mp4?auth_key=1718713123-0-0-30f5c00809c6639de3343e4880648339&t=636426-1718698726-5a32d3c63d6fcdbcc20bf9879fa659d2)

!!! note "基本思想"
	将原始的N点序列，一次分解成一系列短序列，并充分利用$W_N^{nk}$的对称性质和周期性质，求出短序列的DFT，适当组合后再求出长序列的DFT，减少乘法运算。

[可视化理解](https://www.bilibili.com/video/BV1za411F76U),前半部分有点冗余

[简单理解](https://www.bilibili.com/video/BV1Rb4y1Z72j)

复杂度计算，因为FFT相当于把规模为N的问题，每次拆分成两个规模为$\frac{N}{2}$的问题，然后用$o(1)$的时间进行处理。

由主定理可得（主定理部分内容详见数据结构）

$$
T(n) = aT(\frac{n}{b}) + f(n)
$$

$a = 2, b = 2 \therefore T(n) = n\log n$

**FFT 逆变换**

两种方法进行求解：
* 全系数取反，结果最后乘$\frac{1}{N}$,直接求出来的就是序列
* 因为实数序列共轭是本身，所以先取共轭序列列，再使用蝶形运算，求出来的是序列的共轭，这个时候要再注意一次取反。

$$
\begin{align*}
 x^*(n) = [ \frac{1}{N} \sum \limits_{n=0}^{N-1}X(k)W_N^{-kn}]^* = \frac{1}{N}DFT[X^*(k)] 
\end{align*}
$$

**蝶形运算**

N点序列FFT运算

- 运算次数：复数乘法总数$\frac{N}{2}\log_2{N}$,复数加法$N\log_2 N $ 对应实数乘法$2N\log_2{N}$,实数加法$3N\log_2{N}$
- 存储空间：$N + \frac{N}{2}$
- 全系数：因为想要节省内存空间，所以将中间的系数根据可约性进行统一，统一成$W_N^{kn}$的形式，下标都为$N$
- 倒位序：输入自然序，输出倒位序；输入倒位序，输出自然序

**计算线性卷积**

圆周卷积是线性卷积周期延拓取主值
（DFT是DTFT取主值）

先补零，再反转，再卷积。



**谱分析**

- 时限连续信号：频域无限长，必定会有混叠；采用抗混叠滤波器去除次要的高频信号，再进行采样；或者选择合适的$T_s$，减少混叠的影响。
- 带限连续信号：时宽无限，会出现频谱泄漏；加大时宽$\tau$或者选择形状合适的窗函数；
- 连续周期信号：时域正周期截断，

### **z变换**

[张健智云](https://vod.cmc.zju.edu.cn/default/2024/05/16/018231e133b1fe4dd793dd3ac9182714_1920_1080.mp4?auth_key=1718713170-0-0-523036fad9a613322d4ff4d85ff0cd55&t=636426-1718698772-3fd1aea60633bbede2412ad2a2ec047d)
这部分其实直接看书就行了，有联系的是微积分2数列收敛性分析、复变函数洛朗级数、


z变换的直观意义

!!! bug "z变换和复变中的保角映射的联系"

**单边z变换的特殊性质**
单边z变换就是加上了因果序列$u(n)$

- 时移定理

$$
\begin{align*}
    move \ left :\mathscr{Z}[x(n+m)u(n)] = z^m \left[X(z) - \sum^{m-1}_{k=0}x(k)z^{-k}\right]\\
    move \ right :\mathscr{Z}[x(n-m)u(n)] = z^{-m} \left[X(z) - \sum^{-1}_{k=-m}x(k)z^{-k}\right]
\end{align*}
$$

- 初值定理 $x(0) = \lim\limits_{z\rightarrow \infty}X(z)$

- 终值定理 $\lim\limits_{n\rightarrow\infty}x(n) = \lim\limits_{z-\rightarrow 1}[(z-1)X(z)]$



****



### 各种变换之间的关系

**DFT，DFS，DTFT**

DFS→DFT：DFT是DFS的主值序列，是一种通过DFS得出的变换，将有限非周期离散信号的频谱离散化

DTFT→DFT：DFT是在主周期$[-\pi,\pi]$上按$\Omega_0 = \frac{2\pi}{N}$为采样间隔进行采样.

频域采样后时域发生周期延拓，周期为N



**z变换和其他变换的关系**

- 与傅里叶变换：z变换是蜡像抽样信号拉普拉斯变换进行$z = e^{sT_s}$映射的结果；有$X(z) = X_s(s)|_{s = \frac{\ln{z}}{T_s}}$

- 与DTFT：DTFT就是在z平面单位圆上的z变换。可以先求出z变换，再用$e^{j\Omega}$替换$z$
- 与DFT：DFT视为序列的z变换在单位圆上取样间隔$\Omega_0 = \frac{2\pi}{N}$的均匀取样

## 信号处理

### 系统类型

**时变非时变**

注意所有操作都是对$t$进行，不要想当然；

证明顺序 $y_1(t)$,$x_2(t) = x_1(t-t_0)$,求$y_2(t)$

!!! note "只对t进行操作，不是对括号内所有的进行变换"

比如下面的信号

$$
y(t) = x(-t)
$$

$$
证：
y_1(t) = x_1(-t) \\
y_1(t-t_0) = x_1(-t+t_0)\\
x_2 = x_1(t-t_0)\\
y_2(t) = x_2(-t) = x_1(-t-t_0)只对t进行操作
$$





### **系统部分**



**零状态响应**：系统没有内部条件

**零输入响应**：输入为0时候的响应

$$
y(t) = y_{zs}(t)+y_{zi}(t)\\
y(n) = y_{zs}(n) + y_{zi}(n)
$$

时域

$$
\sum_{k=0}^{n}a_k y^{(k)}(t) = \sum^{m}_{k=0}b_kx^{(k)}(t)
$$


单位冲激响应：

- n>m （物理可实现）$h(t) = \sum^{n}_{i=1} A_i e^{\lambda_i t}u(t)$
- n=m: $h(t) = c\delta(t) + \sum^{n}_{i=1} A_i e^{\lambda_i t}u(t)$
- n<m: $h(t) = \sum_{j=0}^{m-n}c_j \delta^{(j)}(t) + \sum^{n}_{i=1} A_i e^{\lambda_i t}u(t)$


$$
\sum_{k=0}^{N}a_k y(n-k) = \sum^{M}_{k=0}b_kx(n-k)
$$


单位脉冲响应：

- $N>M$:$\sum_{i=1}^{N}A_i\lambda_i^n u(n)$
- $N\le M$: $h(n) = \sum^{N-M}_{j=0} C_j \delta(n-j)  + \sum^{N}_{i=1}A_i\lambda_i^Nu(n)$



### **时域分析**

知道单位冲激响应之后，就可以计算零状态响应了


$$
y(t) = x(t) * h(t)
$$

- $t<0$时候，$x(t) = 0$，所以积分下限取0
- $\tau> t$时候，$t-\tau <0$ ，$h(t-\tau)=0$ 积分上限取t

!!! note "$\int_{-\infty}^{t}\delta(\tau)d\tau = u(t)$​"







### **无失真传输**

通过传输系统，波形不变，幅度可以放缩，允许时延

$$
y(t) = kx(t-t_0)
$$

$$
h(t) = k \delta(t-t_0)\\
|H(\omega) |= K\\
\phi_n(\omega) = -\omega t_0
$$

### **判断稳定性**

单位圆内没有极点

当$H(z)$的极点全部位于z平面单位圆内部的时候，系统稳定

### **稳态响应**

先求频率特性函数

离散系统的频率特性函数$H(\Omega)$可以由$H(z)$求取

$$
H(\Omega) = H(z)|_{z = e^{j\Omega}}
$$

再带入对应的$\Omega $





## 滤波器

![模拟滤波器](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E6%A8%A1%E6%8B%9F%E6%BB%A4%E6%B3%A2%E5%99%A8.png)



![数字滤波器](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/%E6%95%B0%E5%AD%97%E6%BB%A4%E6%B3%A2%E5%99%A8.png)




**FIR滤波器**

!!! bug "窗函数设计FIR"
    主瓣、旁瓣、过冲值分别代指哪个部分