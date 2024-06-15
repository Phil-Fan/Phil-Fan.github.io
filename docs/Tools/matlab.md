# MATLAB使用记录

MATLAB 是“matrix laboratory”的缩写形式。MATLAB® 主要用于处理整个的矩阵和数组，而其他编程语言大多逐个处理数值。矩阵是指通常用来进行线性代数运算的二维数组。

## 软件配置





## 基础



`Ctrl + I`自动整理缩进

多行注释：选中多行 → `Ctrl+R`；

取消多行注释：选中多行 → `Ctrl+T`。

```matlab
format long
```

### 复数

复数包含实部和虚部，虚数单位是 `-1` 的平方根。

```
sqrt(-1)
ans = 0.0000 + 1.0000i
```

要表示复数的虚部，请使用 `i` 或 `j`。

```
c = [3+4i, 4+3j; -i, 10j]
```

### 字符串数组中的文本

当您处理文本时，将字符序列括在双引号中。可以将文本赋给变量。

```matlab
t = "Hello, world";
```



如果文本包含双引号，请在定义中使用两个双引号。

```matlab
q = "Something ""quoted"" and something else."
```

有时，字符表示的数据并不对应到文本，例如 DNA 序列。您可以将此类数据存储在数据类型为 `char` 的字符数组中。字符数组使用单引号。

```matlab
seq = 'GCTAGAATCC';
whos seq
seq2 = [seq 'ATTAGAAACC']
```

```shell
seq2 =
    'GCTAGAATCCATTAGAAACC'
```

### 变量

使用 `whos` 可以查看工作区的内容。

```matlab
whos
```

![The pane has a row for each variable. The columns are Name, Value, Min, and Max. Value includes size and class.](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/workspace.png)

退出 MATLAB 后，工作区变量不会保留。使用 `save` 命令保存数据以供将来使用，

```matlab
save myfile.mat
```

通过保存，系统会使用 `.mat` 扩展名将工作区保存在当前工作文件夹中一个名为 MAT 文件的压缩文件中。

要清除工作区中的所有变量，请使用 `clear` 命令。

使用 `load` 将 MAT 文件中的数据还原到工作区。

```matlab
load myfile.mat
```





### 函数

```matlab
max()
union()
[minA,maxA] = bounds(A) % 如果存在多个输出参数，请将其括在方括号中
```

用引号将任何文本输入括起来：

```matlab
disp("hello world")
```



## 矩阵

### 创建

请使用逗号 (`,`) 或空格分隔各元素,使用分号分隔各行。

创建矩阵的另一种方法是使用 `ones`、`zeros` 或 `rand` 等函数。

```matlab
a = [1 3 5; 2 4 6; 7 8 10]
z = zeros(5,1)
```

### 取值

```matlab
A(4,2)
A(8) % 单一下标按顺序向下遍历每一列

A(1:3,2) % 列出 A 前三行及第二列中的元素,与python元组语法类似
A(3,:)

B = 0:10:100 % 冒号表达式
```







### 运算

MATLAB 允许您使用单一的算术运算符或函数来处理矩阵中的所有值

```matlab
a + 10
sin(a)
a' % 转置
inv(a) % 逆矩阵
```

您可以使用 `*` 运算符执行标准矩阵乘法

```
p = a*inv(a)
```

元素级别乘法

```matlab
p = a.*a
a.^3
```

### 串联

*串联*是连接数组以便形成更大数组的过程。实际上，第一个数组是通过将其各个元素串联起来而构成的。成对的方括号 `[]` 即为串联运算符。

```matlab
A = [a,a]
A = [a; a] % 垂直
```



## 信号处理

```matlab
conv() % 卷积
laplace(x) % 拉普拉斯变换
```



### 连续系统时域分析

```matlab
sys = tf(num,den)
# 单位冲激响应
[y,t] = impulse(sys)
[y,t] = impulse(sys,T_final) 

# 单位阶跃响应
[y,t] = step(sys)
[y,t] = step(sys,Tfinal)

# 任意激励 lsim
[y,t,x] = lsim(sys,u,t) 
[y,t,x] = lism(sys,u,t,x_0) %x_0系统状态变量
```

### 离散系统时域分析

```matlab
# 单位脉冲响应
[h,t] = impz(num,den) 
impz(b,a,-3:10)

# 单位阶跃响应
[h,t] = stepz(num,den)

# 零状态响应
y = filter(num,den,x,zi) 

% x是包含输入序列非零样值点，zi表示系统输入延时
[y,x] = dlism(num,den,u,x0)
```

### 频域分析

时域卷积对应频域相乘

连续系统：$Y(\omega) = X(\omega)H(\omega)$

离散系统：$Y(\Omega) = X(\Omega)H(\Omega)$

```matlab
# 连续系统频率特性
[h,w] = freqs(sys,n) % n为输出频率点个数
abs() % 幅频
angle() % 相频

# 
heaviside(t) 单位冲激响应h(t)
fourier(x) % 傅里叶变换
ifourier(Y) % 傅里叶反变换
```

```matlab
# 离散系统频率特性
[h,w] = freqz(sys, n, Fs) %频率等分点向量w的采样频率Fs，省略时候,w为0-pi的n个频率等分点

[h,w] = freqz(sys,n,'whole') % H(Ω) 0-2pi n个频率等分点
```



### 复频域分析

#### 连续系统

```matlab
# 传递函数表达方式转换
[z,p,k] = tf2zp(num,den)
[num,den] = tf2tf(z,p,k)
[N,D] = numden(A) % 多项式分解成分子多项式N，分母多项式D

a = sym2pol(P) % 返回多项式系数向量
```

```matlab
# 求根
r = roots(N)
N = poly(r) % 将根转换为多项式系数向量
den = conv() % 将因子相乘形式转换为多项式形式
```

```matlab
# 部分分式展开
[r,p,k] = residue(num,den)
```

$$
\frac{num(s)}{den(s)} = k(s) + \frac{r_1}{s-p_1}+\frac{r_2}{s-p_2} +\dots+\frac{r_n}{s-p_n}
$$



```matlab
# 绘制零极点分布
pzmap(sys)
```



#### 离散系统

```
zrans(x)
```



```matlab
[r,p,k] = residuez(num,den)

# 绘制图像
zplane(num,den)
```



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



## 图像绘制



## 程序设计



## 参考文献

[matlab入门图文教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/77669451)

[MATLAB 入门之旅 | 自定进度在线课程 - MATLAB & Simulink (mathworks.com)](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted?s_eid=PEP_ILMEDUPage_learning)

