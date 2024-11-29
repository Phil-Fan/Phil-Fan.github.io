# MATLAB使用记录

MATLAB 是“matrix laboratory”的缩写形式。MATLAB® 主要用于处理整个的矩阵和数组，而其他编程语言大多逐个处理数值。矩阵是指通常用来进行线性代数运算的二维数组。

## 软件配置

### Matlab in VSCode

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241128002347.png)

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241128002415.png)

下载插件

在python环境中，最好3.9

```python title="检查32or64位系统"
import sys
print(sys.maxsize > 2**32)
```


找到安装matlab 的root路径

`\extern\engines\python`进入放置`setup.py`的位置；
```shell title="安装"
python setup.py install
```
安装 MATLAB Engine API 的 Python 设置脚本。


```shell title="测试"
ipython
```

```python title="测试代码"
import matlab.engine
eng = matlab.engine.start_matlab()
eng.sqrt(4.0)
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241128002703.png)

注意这里如果使用conda环境，需要配置对应的conda中的python路径


配好了以后右上角就会有执行代码的按钮了


#### 小bug
1. 需要vscode打开`.m`文件的文件夹，否则会报错

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

### 输出
#### `disp()`
```matlab
A = [1 0];
disp(A)

S = 'Hello World.';
disp(S)
```
#### `fprintf()`
```matlab
fprintf('X is %4.2f\n',A)
```
#### `print()`
```matlab
bar(1:10)
print
```


## 矩阵

### 创建

请使用逗号 (`,`) 或空格分隔各元素,使用分号分隔各行。

创建矩阵的另一种方法是使用 `ones`、`zeros` 或 `rand` 等函数。

```matlab
a = [1 3 5; 2 4 6; 7 8 10]
z = zeros(5,1)
```

```matlab
eye(size(A)) %产生与A矩阵同阶的单位矩阵
zeros()
ones() % 产生0和1的矩阵
rand() % 产生随机元素的矩阵
diag() % 产生对角矩阵
triu() % 产生上三角矩阵
tril() % 产生下三角矩阵
size() %显示一个包含两个元素的向量：矩阵的行与列的个数。函数length()返回向量的长度或矩阵行数和列数的最大值
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

乘方
```
A^P
```
表示A的P次

### 矩阵值

方阵的行列式：`det`
矩阵的迹： `trace`
矩阵的秩： `rank`
矩阵和向量的范数
- `norm` 欧几里德范数
- `norm(x,inf)` 无穷范数
矩阵函数
expm logm sqrtm


eig(A)以列向量形式返回特征值，`[X,D]=eig(A)`返回
特征值和特征向量，D为特征值对角阵，特征向量X。
### 串联

*串联*是连接数组以便形成更大数组的过程。实际上，第一个数组是通过将其各个元素串联起来而构成的。成对的方括号 `[]` 即为串联运算符。

```matlab
A = [a,a]
A = [a; a] % 垂直
```

### 分解
#### LU
矩阵的三角分解：将一个方阵表示为一个上三角阵（U）和一个下
三角阵（L）的乘积（LU分解） 
```
[L,U]=lu(X)
```
#### QR
矩阵的正交变换：分解为正交矩阵（Q）和上三角矩阵（R）的乘积
（QR分解） 
```
[Q,R]=qr(A)
```
#### SVD

奇异值分解
```
[U,S,V]=svd(A) 
```
A=U*S*V’

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

使用方法：在matlab中输入simulink，打开simulink模型编辑器。


### 快捷键

- `Ctrl + R`：顺时针旋转
- `Ctrl + Shift + R` 逆时针旋转
- 按住`Ctrl`键并连接线，可以从一条线中分支

[MATLAB的Simulink的信号线 - 知乎](https://zhuanlan.zhihu.com/p/615160855)
### 常用元件

mux：多路复用器，可以实现多个输入信号的选择

scope：示波器，用于显示信号波形；设置里可以更改输入端口的个数

transfer function：传递函数，用于建立系统的传递函数模型

step：阶跃信号，用于产生阶跃信号

add：加法器，用于实现信号的加法运算；设置里可以更改输入端口的个数

!!! note "例子"
    === "搭建二阶系统"
        ![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241020131407.png)
        [MATLAB——Simulink二阶系统 - 哔哩哔哩](https://www.bilibili.com/read/cv9223784/)


### S function

!!! note "S function就是自定义的模型，用于补充simulink中没有的功能"


[S-function入门及案例详解（1）——S-function基础介绍及基本案例-CSDN博客](https://blog.csdn.net/didi_ya/article/details/118186847)

[S-function入门及案例详解（2）——S-function基本案例介绍\_s-function怎么用-CSDN博客](https://blog.csdn.net/didi_ya/article/details/118251832)

[S-function入门及案例详解（3）——S-function进阶案例\_s函数 英文学习指导-CSDN博客](https://blog.csdn.net/didi_ya/article/details/118190541)

[S-function入门及案例详解（4）——S-function进阶案例之连续/离散状态空间表达式的S-function实现\_s-function实例-CSDN博客](https://blog.csdn.net/didi_ya/article/details/118195184)



S-function模块，位于Simulink/User-Defined Functions模块库中，是使S-function图形化的模板工具，用于为S-function创建一个定值的对话框和图标。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241117101401.png)


- `S-function name`：填入S-function的函数名称，这样就建立了S-function模块与M文件形式的S-function之间的对应关系；

- `S-function parameters`：填入S-function需要输入的外部参数的名称，如果有对各变量，则变量中间用逗号隔开，如a，b，c；

- `S-function modules`：仅当S-function是用C语言编写并用MEX工具编译的C-MEX文件时，才需要填写该参数；


**直接馈通**

如果输出函数（mdlOutputs或flag==3）是输入u的函数，即，如果输入u在mdlOutputs中被访问，则存在直接馈通。ex：$y= k\cdot u$

**采样时间与偏移量**

采样时间是按照固定格式成对指定的：`[采样时间 偏移时间]`。

|采样时间表示	|意义|
|---|---|
|[0 0]	|连续采样时间|
|[-1 0]	|继承S-function输入信号或父层模型的采样时间|
|[0.5 0.1]	|离散采样时间，从0.1s开始每0.5s采样一次|

#### 函数分析
S-function包括主函数和6个功能子函数，包括mdlInitializeSizes（初始化）、mdlDerivatives（连续状态微分）、mdlUpdate（离散状态更新）、mdlOutputs（模块输出）、mdlGetTimeOfNextVarHit（计算下次采样时刻）和mdlTerminate（仿真结束）。

在S-function仿真过程中，利用switch-case语句，根据不同阶段对应的flag值（仿真流程标志向量）来调用S-function的不同子函数，以完成对S-function模块仿真流程的控制。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241117102637.png)




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

#### 状态空间 `ss()` | state space


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


#### 连续系统离散化
```
SYSD = c2d(SYSC,Ts,METHOD)
```
将连续模型转换为离散模型，`METHOD`缺省为采用零阶保持器的方法，`Ts`为采样周期。

Method: 
- `zoh`——采用零阶保持器
- `foh`——采用一阶保持器
- `tustin`——采用双线形（tustin）逼近方法
- `prewarp`——采用改进的tustin方法
- `matched`——采用SISO系统的零极点匹配法。

!!! note "例子"
    ```matlab
    A = [0 1; -.5 -.5]
    B = [1;0]
    C = [1 0]
    sys = ss(A,B,C)
    sys_d = c2d(sys,0,1)
    ```


#### 离散系统连续化
```matlab
sysc=d2c(sysd,method)
```

Method: 
- `zoh`——采用零阶保持器
- `tustin`——采用双线形（tustin）逼近方法
- `prewarp`——采用改进的tustin方法
- `matched`——采用SISO系统的零极点匹配法。具有接近1的极点
的情况。
!!! note "注意"
    zoh法不适合系统具有z=0的极点的情况，对于具有负实数极点的系统，该方法将增加系统的阶。
    Tustin法不适合系统具有z=1

### 系统组合
```
SYS = APPEND(SYS1,SYS2, ...)
```



#### 串联
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240929115631.png)

```
sys=series(sys1,sys2)
```
返回两个系统sys1和sys2的串联系统。
两个子系统必须连续时间系统或者具有相同采样周期的离散时间系
统。
```
sys=series(sys1,sys2,outputs1,inputs2)
```
outputs1和inputs2用于指定sys1的部分输出与sys2的部分输入进行连接。


#### 并联
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240929115722.png)


```
sys=parallel(sys1,sys2)
```
返回两个系统并联连接系统，两个子系统必须连续时间系统或者具有相同采样周期的离散时间系统。

```
sys=parallel(sys1,sys2,inp1,inp2,out1,out2)
```
inp1和inp2分别表示两个系统连接在一起的输入端，out1和out2中分别指定要做相加的输出端编号。
#### 反馈

```
sys=feedback(sys1,sys2)
```

返回sys1和sys2的反馈连接系统sys，反馈为负反馈。两个子系统必须连续时间系统或者具有相同采样周期的离散时间系统。

```
sys=feedback(sys1,sys2,sign)
```
定义反馈形式sign，sign=+1表示正反馈，sign=-1表示负反馈。

```
sys=feedback(sys1,sys2,feedin,feedout,sign)
```
将sys1的指定输出`feedout`连接到sys2的输入，sys2的输出连接到sys1的指定输入`feedin`，以此构成闭环
系统

#### 框图连接

sysc=connect(sys,Q,inputs,outputs)——框图建模，sys为由append生成的无连接对角方块系统，Q矩阵用于指定系统sys的内部连接关系，其中矩阵的每一行对应一个输入，其第一个元素为输入编号，其后为连接该输入的输出编号，如采用负连接，则以负值表示。inputs和outputs用于指定无连接系统中的某些输入/输出保留作为外部的输入输出
### Time Domain

#### 求解方程

```matlab
p = pole(sys) % 求极点
z = zeros(sys) % 求零点
r = roots([1,2,3]) % 中间是多项式的参数
```



#### 阶跃响应绘制

在MATLAB中，可以使用`step`函数来绘制系统的阶跃响应曲线。`step`函数的基本语法如下：

```matlab
step(sys)
```

此外，还可以使用以下语法来获取阶跃响应的输出值和时间向量：

```matlab 
[y, t] = step(sys)
```

其中，`y`是阶跃响应的输出值向量，`t`是对应的时间向量。

```matlab title="求解时域指标" linenums="1" hl_lines="7 8 14 20"
[y,t]=step(sys);

[Y,k] = max(y);
timetopeak = t(k); % 峰值时间
C = dcgain(sys); % 系统的终值
overshoot = 100*(Y-C)/C; % 超调
n=1;
while y(n)<C
    n = n+1;
end
risetime = t(n) % 上升时间

i=length(t);
while (y(i)>0.98*C) & (y(i)<1.02*C)
    i = i-1;
end
setllingtime = t(i) % 稳态时间

fprintf("峰值时间:%.4f,超调:%.4f,上升时间%.4f,稳态时间%.4f",timetopeak,overshoot,risetime,setllingtime)
```

### S domain

#### 图像绘制

```matlab
pzmap(sys) % 绘制极点、零点图像
```
```
[P, Z] = pzmap(SYS)
```
返回系统零极点列向量，不画图


#### 绘制根轨迹 `rlocus`

```matlab
rlocus(sys)
```
**rlocus 求系统的根轨迹**
```
rlocus(SYS)
```

计算并绘制系统的根轨迹图。根轨迹图用来分析
负反馈系统，并显示当反馈增益从0变化到$\infty$时，闭环极点的轨迹。

```
[R, K] = RLOCUS(SYS)，R＝rlocus(SYS,K) 
```
K为用户定义的增益。




```matlab title="有阻尼比线的根轨迹图"
num = [1];
den = [1, 2, 1];
rlocus(num, den);
zeta = ;
sgrid(zeta,[]) % 绘制根轨迹图上的阻尼比线
```

```matlab title="找到根轨迹图像上最小阻尼比"
min_zeta = inf;       % 初始化最小阻尼比
min_zeta_pole = [];   % 保存最小阻尼比对应的极点
min_zeta_K = [];      % 保存最小阻尼比对应的增益

% 遍历每个增益的闭环极点，计算阻尼比
for i = 1:size(r,2)
    poles = r(:,i);    % 第 i 列对应的是增益 K(i) 下的闭环极点
    for j = 1:length(poles)
        zeta = -real(poles(j)) / abs(poles(j));  % 计算每个极点的阻尼比
        if zeta < min_zeta
            min_zeta = zeta;           % 更新最小阻尼比
            min_zeta_pole = poles(j);   % 保存对应的极点
            min_zeta_K = k(i);          % 保存对应的增益 K
        end
    end
end

% 显示最小阻尼比、对应极点和增益 K
disp(['最小阻尼比: ', num2str(min_zeta)])
disp(['对应极点: ', num2str(min_zeta_pole)])
disp(['对应增益 K: ', num2str(min_zeta_K)])
```

#### 根轨迹分析

**rlocfind 计算给定一组根的根轨迹增益**


```
[K, POLES] = rlocfind(SYS)
```
可在图形窗口根轨迹图中显示出十字光标，当用户选择其中一点时，其相应的增益由k记录，与增益相关的所有极点记录在poles中

```
[K, POLES] = rlocfind(SYS,P)
```
指定要得到增益的根矢量P。


**sgrid 在连续系统根轨迹图和零极点图中绘出阻尼系数和自然频率栅格**

`sgrid`——在连续系统的根轨迹或零极点图上绘制出栅格线，栅格线由等阻尼系数和等自然频率线构成，阻尼系数以步长0.1从ξ＝0到ξ＝1绘出

`sgrid(‘new’)`——先清除图形屏幕，然后绘制出栅格线，并设置成`hold on`，使后续绘图命令能绘制在栅格上。

`sgrid(z, wn)`——可制定阻尼系数z和自然频率$\omega_n$

`sgrid(‘new’, z, wn)`——可制定阻尼系数z和自然频率$\omega_n$，并且在绘制栅格线之前清除图形窗口。



#### SISOTOOL
除了使用`rlocus`函数外，你还可以使用MATLAB的SISOTOOL（单输入单输出工具）进行根轨迹设计。SISOTOOL提供了一个交互式的界面，使你可以方便地绘制和分析根轨迹，以及设计控制器。要使用SISOTOOL，只需在MATLAB命令窗口中输入`sisotool`即可。

![image-20240424103521521](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240424103521521.png)

#### 分析根轨迹

- 添加零点、极点、积分器
- 去除零点、极点、积分器
- 移动零极点
- 添加`requirement`<br>
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009145358.png) 
<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240424103552781.png" alt="image-20240424103552781" style="zoom:50%;" />
- 查看阶跃图像特征点
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20241009145809.png)


### 现代控制

#### 能控性
```matlab
Co = ctrb(A,B) # return the controllability matrix
```


## 图像绘制
> 绘制相平面图像[MathWorks-Teaching-Resources/Phase-Plane-and-Slope-Field: Apps for qualitative ODE analysis.](https://github.com/MathWorks-Teaching-Resources/Phase-Plane-and-Slope-Field)


## 程序设计



## 参考文献

[matlab入门图文教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/77669451)

[MATLAB 入门之旅 | 自定进度在线课程 - MATLAB & Simulink (mathworks.com)](https://matlabacademy.mathworks.com/cn/details/matlab-onramp/gettingstarted?s_eid=PEP_ILMEDUPage_learning)

