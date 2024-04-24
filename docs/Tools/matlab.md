# MATLAB使用记录

MATLAB 是“matrix laboratory”的缩写形式。MATLAB® 主要用于处理整个的矩阵和数组，而其他编程语言大多逐个处理数值。矩阵是指通常用来进行线性代数运算的二维数组。

## 软件配置





## 基础

### 变量

### 函数

### 向量

### 函数

## 矩阵计算



## 信号处理

## Simulink

- **系统仿真**：Simulink是MATLAB中用于动态系统建模、仿真和分析的工具箱，可以用于自动控制原理课程中的系统仿真。
- **控制系统设计**：通过Simulink，可以设计和分析各种类型的控制系统，包括反馈控制系统、前馈控制系统等。

## Control System Toolbox

### 构建系统模型

#### 传递函数 `tf()`

$$
G(s) = \frac{Y(s)}{U(s)}
$$

传递函数法可以通过`tf`函数来实现，其基本语法为：

```matlab
sys = tf(num, den)
```

其中，`num`和`den`分别是传递函数的分子和分母多项式系数向量。

#### 状态空间 `ss()`

$$
\begin{aligned}
\dot{x}(t) &= Ax(t) + Bu(t) \\
y(t) &= Cx(t) + Du(t)
\end{aligned}
$$

其中，$x(t)$是系统的状态向量，$u(t)$是系统的输入，$y(t)$是系统的输出，$A$、$B$、$C$、$D$​是系统矩阵。

状态空间法可以通过`ss`函数来实现，其基本语法为：

```matlab
sys = ss(A, B, C, D)
```

其中，`A`、`B`、`C`、`D`分别是状态空间模型的状态矩阵、输入矩阵、输出矩阵和直接传输矩阵。

示例代码：

```matlab
A = [0, 1; -1, -2];
B = [0; 1];
C = [1, 0];
D = 0;
sys = ss(A, B, C, D);
```

这将创建一个状态空间模型`sys`，其状态空间表示为：

$$
\begin{aligned}
\dot{x}(t) &= \begin{bmatrix} 0 & 1 \\ -1 & -2 \end{bmatrix} x(t) + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u(t) \\
y(t) &= \begin{bmatrix} 1 & 0 \end{bmatrix} x(t) + 0u(t)
\end{aligned}
$$



#### 频率响应法 `freqs()`

频率响应法是一种基于频率特性的分析方法，通过建立系统的频率响应函数来描述系统的输入输出关系。

$$
G(j\omega) = \frac{Y(j\omega)}{U(j\omega)}
$$

其中，$G(j\omega)$是系统的频率响应函数，$Y(j\omega)$是系统的输出，$U(j\omega)$是系统的输入，$j$是虚数单位，$\omega$​是角频率。



频率响应法可以通过`freqs`函数来计算系统的频率响应，其基本语法为：

```matlab
[H, w] = freqs(num, den)
```

其中，`H`是系统的频率响应，`w`是对应的频率向量。

示例代码：

```matlab
num = [1, 2];
den = [1, 3, 2];
[H, w] = freqs(num, den);
```

这将计算传递函数`G(s) = (1 + 2s)/(1 + 3s + 2s^2)`的频率响应`H`和对应的频率向量`w`。

#### 零极点法 `zpk(z,p,k)`

零极点法是一种基于零极点的分析方法，通过确定系统的零点和极点来描述系统的频率特性。零极点模型可以表示为：

$$
G(s) = \frac{b_0 + b_1s + \cdots + b_ns^n}{a_0 + a_1s + \cdots + a_ms^m}
$$

其中，$b_0, b_1, \cdots, b_n$是系统的零点，$a_0, a_1, \cdots, a_m$​是系统的极点。

零极点法可以通过`zpk`函数来实现，其基本语法为：

```matlab
sys = zpk(z, p, k)
```

其中，`z`、`p`、`k`分别是系统的零点、极点和增益。

示例代码：

```matlab
z = [-1];
p = [-2, -3];
k = 2;
sys = zpk(z, p, k);
```

这将创建一个零极点模型`sys`，其传递函数为：

$$
G(s) = 2\frac{s + 1}{(s + 2)(s + 3)}
$$



### Time Domain

#### 求解方程

```matlab
p = pole(sys) % 求极点
z = zeros(sys) % 求零点
r = roots([1,2,3]) % 中间是多项式的参数
```



**阶跃响应绘制**

在MATLAB中，可以使用`step`函数来绘制系统的阶跃响应曲线。`step`函数的基本语法如下：

```matlab
step(sys)
```

此外，还可以使用以下语法来获取阶跃响应的输出值和时间向量：

```matlab
[y, t] = step(sys)
```

其中，`y`是阶跃响应的输出值向量，`t`是对应的时间向量。



### S domain

#### 图像绘制

```matlab
pzmap(sys) % 绘制极点、零点图像
```



#### 绘制根轨迹

**法一 —— `rlocus`**

```matlab
rlocus(sys)
```

使用以下代码绘制一个二阶系统的根轨迹：

```matlab
num = [1];
den = [1, 2, 1];
rlocus(num, den);
```

这个案例将绘制一个二阶系统的根轨迹，系统传递函数为`G(s) = 1/(s^2 + 2s + 1)`。

**法二 —— 使用SISOTOOL进行根轨迹设计**
除了使用`rlocus`函数外，你还可以使用MATLAB的SISOTOOL（单输入单输出工具）进行根轨迹设计。SISOTOOL提供了一个交互式的界面，使你可以方便地绘制和分析根轨迹，以及设计控制器。要使用SISOTOOL，只需在MATLAB命令窗口中输入`sisotool`即可。

![image-20240424103521521](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240424103521521.png)

#### 分析根轨迹

- 添加零点、极点、积分器
- 去除零点、极点、积分器
- 移动零极点
- 添加`requirement`<br><img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240424103552781.png" alt="image-20240424103552781" style="zoom:50%;" />





## 程序设计



## 参考文献

[matlab入门图文教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/77669451)

[MATLAB 入门之旅 | 自定进度在线课程 - MATLAB & Simulink (mathworks.com)](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted?s_eid=PEP_ILMEDUPage_learning)

