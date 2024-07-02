# 密码技术

??? note "来源"
    - USTC《计算机网络》<br>
    - 《图解密码技术》<br>
    - 《信息物理系统安全》<br>

!!! bug "如果看不到图像或是公式，多刷新几次"

做PPT时候整理的图像

![image-20240605143933543](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240605143933543.png)

![image-20240605144047495](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240605144047495.png)





## 数论前置知识

### 同余 (Congruence)

同余是表示两个整数除以同一个正整数后余数相等的关系。如果整数 $a$ 除以正整数 $n$ 的余数与整数$b$除以$n$的余数相同，我们说$a$和$b$对模$n$同余，表示为：

$$
a \equiv b \mod n
$$

### 互质 (Coprime)

$$
gcd(a, b) = 1
$$

### 欧拉函数 (Euler's Totient Function)

欧拉函数$\phi(n)$是小于或等于$n$的正整数中与$n$互质的数的数量。

对于质数$p$，$\phi(p) = p - 1$。如果$n$是两个不同质数$p$和$q$的乘积，即$n = pq$，那么$\phi(n) = (p-1)(q-1)$。

$$
\phi(n) = n \prod_{p|n} \left(1 - \frac{1}{p}\right)
$$

### 欧拉定理

欧拉定理指出，对于两个互质的正整数 \(a\) 和 \(n\)（即 \(gcd(a, n) = 1\)），\(a\) 的欧拉函数 \(\phi(n)\) 次幂对 \(n\) 的模等于 1。用数学表达式表示为：

$$
a^{\phi(n)} \equiv 1 \mod n
$$

其中，\(\phi(n)\) 是欧拉函数，表示小于或等于 \(n\) 的正整数中与 \(n\) 互质的数的数量。

### 模逆 (Modular Inverse)

如果存在整数$b$使得$ab \equiv 1 \mod n$，则称$b$是$a$模$n$的逆元

$$
a^{-1} \equiv b \mod n
$$

表示找到一个数$b$，使得$a$和$b$相乘对模$n$同余1。

![image-20240529115856874](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529115856874.png)

### 裴蜀定理（Bézout's Theorem）

**定义**：
裴蜀定理指出，对于任意的整数 \(a\) 和 \(b\)，存在整数 \(x\) 和 \(y\)，使得 \(ax + by = \gcd(a, b)\)，其中 \(\gcd(a, b)\) 是 \(a\) 和 \(b\) 的最大公约数。

**例子**：
考虑 \(a = 56\) 和 \(b = 15\)，计算它们的最大公约数：
\[ \gcd(56, 15) = 1 \]

我们可以找到 \(x\) 和 \(y\) 使得：
\[ 56x + 15y = 1 \]

一个解是 \(x = -2\) 和 \(y = 15\)：
\[ 56(-2) + 15(15) = -112 + 225 = 113 \]

```python
from sympy import gcd, mod_inverse

a = 56
b = 15
g = gcd(a, b)  # 计算最大公约数

# 使用扩展欧几里得算法找到x和y
def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = extended_gcd(b, a % b)
        return (y, x - (a // b) * y)

x, y = extended_gcd(a, b)
print(f"The coefficients x and y are: {x}, {y}")
```

### 中国剩余定理（Chinese Remainder Theorem, CRT）

参考视频：[中国剩余定理，考试包会](https://www.bilibili.com/video/BV1Y84y1E7ts)

**定义**：
中国剩余定理解决同余方程组。若\(m_1, m_2, ..., m_k\) 互素，则对于任意整数 \(a_1, a_2, ..., a_k\)，存在唯一的整数 \(x\)，满足：
\[ x \equiv a_i \mod m_i \]

**例子**：
求解以下方程组：
\[ x \equiv 2 \mod 3 \]
\[ x \equiv 3 \mod 5 \]
\[ x \equiv 2 \mod 7 \]

根据CRT，可以找到唯一解 \(x\)（在模 \(105 = 3 \times 5 \times 7\) 范围内）：
解为 \(x = 23\)，因为：
\[ 23 \mod 3 = 2 \]
\[ 23 \mod 5 = 3 \]
\[ 23 \mod 7 = 2 \]

```python
from sympy.ntheory.modular import crt

# 模数
moduli = [3, 5, 7]
# 余数
remainders = [2, 3, 2]

x = crt(moduli, remainders)[0]
print(f"The solution x is: {x}")
```

### 扩展欧几里得定理（Extended Euclidean Algorithm）

**定义**：
扩展欧几里得算法不仅计算两个整数的最大公约数，还可以找到裴蜀定理中的系数 \(x\) 和 \(y\)，使得：
\[ ax + by = \gcd(a, b) \]

**例子**：
计算 \(a = 30\) 和 \(b = 20\) 的最大公约数，并找到对应的 \(x\) 和 \(y\)：
\[ \gcd(30, 20) = 10 \]

使用扩展欧几里得算法找到 \(x\) 和 \(y\)：
\[ 30x + 20y = 10 \]

一个解是 \(x = 1\) 和 \(y = -1\)，因为：
\[ 30(1) + 20(-1) = 10 \]

```python
from sympy import gcd

a = 30
b = 20
g = gcd(a, b)  # 计算最大公约数

# 使用扩展欧几里得算法找到x和y
def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = extended_gcd(b, a % b)
        return (y, x - (a // b) * y)

x, y = extended_gcd(a, b)
print(f"The coefficients x and y are: {x}, {y}")
```



> 参考网址：[求逆元方法 简单又好记_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11Y4y1U7Gh/?spm_id_from=333.788&vd_source=8b7a5460b512357b2cf80ce1cefc69f5)
> [详解扩展欧几里得算法（扩展GCD） - Seaway-Fu - 博客园 (cnblogs.com)](https://www.cnblogs.com/fusiwei/p/11775503.html)

1、求解不定方程

2、求解模的逆元

3、求解线性同余方程



```cpp
int exgcd(int a,int b,int &x,int &y)
{
    if(b==0)
    {
        x=1,y=0;
        return a;
    }
    int d=exgcd(b,a%b,x,y);
    int k=x;
    x=y;
    y=k-a/b*y;
    return d;
}
```



在RSA算法中求私钥中的整数d时，需要使得$ (e \times d ) \% m = 1$，该方程等价于 $e \times d = 1 + y \times m$ （y为整数），也等价于 $e \times d - y \times m = 1$。

因此求解d的过程就是求解该二元一次方程组（e和m已知，求解d），即求e模m的逆元。



实现的时候采用递归做法

先递归进入下一层，等到到达最后一层即 b=0 时就返回x=1 , y=0

再根据 x1=y2 , y1=x2-a/b*y2 ( x2 与 y2 为下一层的 x 与 y ) 得到当层的解

不断算出当层的解并返回，最终返回至第一层，得到原解

## 加密——机密性

![image-20240215231126309](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240215231126309.png)



!!! note "密钥才是加密的核心"
    加密算法和密钥是分开的，每个人可以拥有相同品牌的锁，但是每一个人有不同的钥匙<br>锁的设计是公开的，但是钥匙是秘密的。



- Trudy: 窃听、插入、伪装、劫持、拒绝服务

只有发送方和预订的接收方能否理解传输的报文内容
发送方加密报文；接收方解密报文

明文密文并不是看是否由人读取



|               Transaction                | Fill In This Column |       Choose From The Following        |
| :--------------------------------------: | :-----------------: | :------------------------------------: |
|   Alice wants to sign an email to Bob    |          b          |         a. Alice's public key          |
|  Alice wants to encrypt an email to Bob  |          c          |         b. Alice's private key         |
|    Bob wants to verify Alice's email     |          a          |          c. Bob's public key           |
|    Bob wants to decrypt Alice's email    |          d          |          d. Bob's private key          |
|  Alice public key certificate signed by  |          f          | e. Certification Authority public key  |
| Bob public key certificate verifies with |          e          | f. Certification Authority private key |

答案和解析:

- Alice想要给Bob签名一封电子邮件：因为Alice使用她的私钥生成数字签名，而Bob需要使用Alice的公钥来验证这个签名。
- Alice想要加密一封发送给Bob的电子邮件：应该是使用Bob的公钥来加密
- Bob想要验证Alice的电子邮件：因为Bob使用Alice的公钥验证了数字签名，所以他知道这封电子邮件确实来自Alice。
- Bob想要解密Alice的电子邮件：d（Bob的私钥）
- Alice的公钥证书由以下机构签名：因为公钥证书是由认证机构使用其私钥签名的，所以其他人可以使用认证机构的公钥来验证这个签名。
- Bob的公钥证书验证如下：使用认证机构的公钥来验证Bob的公钥证书



### 历史上的密码

#### 凯撒密码——平移

![image-20240522173659727](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240522173659727.png)

密钥：平移的字母数量

可以使用暴力破解——平移1-n位

#### 替换密码

密钥：替换表，使用密码本

字母替换，通过分析字频和词频可以破解

> 英文文章出现最高的字母是e

!!! note "Challenge 1"
    ![crypto_challenge1](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/crypto_challenge1.png)

    - 要求：破解纸条上的信息，给出最后的破解结果，对于本问题，可以不用写破解的过程，毕竟福尔摩斯曾经说过，“将中间的推理步骤统统去掉，能够达到惊人的效果”，不过还是很希望能够看到同学们是如何逐步破解问题，得到最后的结果的，这也是密码学题目，或者说 CTF 题目的真正乐趣所在。
    
    - 不妨读一下**福尔摩斯探案集《跳舞的小人》**，说不定对你有帮助呢？
    
    解密结果
    > tonight Ethan will arrive here please lure him to the abandoned warehouse near the police station where the professional assassin reese hired will eliminate him
    >
    > tomorrow she will go to the warehouse and become the first person to discover his corpse with a strong alibi these police officers absolutely cannot arrest her

方法：

> **参考文档和网站**：
>
> [quipqiup - cryptoquip and cryptogram solver](http://quipqiup.com/)<br>
> [古典密码学之词频分析 | Cata1yst's blog (cata1ysts.github.io)](https://cata1ysts.github.io/2022/08/14/古典密码学之词频分析/)<br>
> [单表代换加密 - CTF Wiki (ctf-wiki.org)](https://ctf-wiki.org/crypto/classical/monoalphabetic/#_11)<br>

先使用`opencv`库将图片进行切割和计数，然后猜测带圈和不带圈是同一个字母的大小写关系。

手动匹配大小写关系后，使用程序将密码图片转换成密文字符串

> ABCDEFaHAFIcKDLlINNDOhFHNhQLHIRhLSNhFDgAbAFhIVICWBCHwKINHFBSRhCHInAFhQBLDMhRAIADBcKFHNhAFhQNBPHRRDBCIlIRRIRRDcNHHRhFDNHwKDLlHLDGDCIAhFDgABGBNNBkRFhKDLlEbAbAFhKINHFBSRhICwVHMBGhAFhPDNRaQHNRBcAbWDRMBOHnFDrMBNQRhKDAfiRANBCeILDVdAFHRhQBLDMhBPPDMHNrIVRBLSAHLxMIcCBaINNHRaFHn

将转换后的密文送入解密工具。稍微调整一下格式即可。

![image-20240605182302624](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240605182302624.png)









!!! note "—次性密码本与压缩"
    > 虽然一次性密码本的密钥需要与明文等长，但是我手上有数据压缩程序，只要用这个程序 对一次性密码本的密钥进行压缩，不就可以把密钥变短了吗？ 请问Alice的想法正确吗？<br>
    不正确。因为一次性密码本的密钥无论使用任何压缩软件都无法进行压缩。<br>压缩软件的压缩原理，是找出输入数据中出现的冗余的重复序列，并将它们替换成较短的数据。然而一次性密码本所使用的密钥是随机的，其中不包含任何冗余的重复序列。<br>反过来说， 如果一个比特序列能够被压缩，就说明它不是一个随机的比特序列。



**Enigma加密**

![image-20240522174420066](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240522174420066.png)

!!! bug "这一部分没有看"

### 对称加密

加密解密密钥一样

$K_{A-B}$:对称密钥

密钥的分发：密码本



密码选择

- 首先，DES不应再用于任何新的用途，因为随着计算机技术的进步，**现在用暴力破解法已经能够在现实的时间内完成对DES的破译**。但是，在某些情况下也需要保持与旧版本软件的兼容性。

- 其次，我们也没有理由将三重DES用于任何新的用途，尽管在一些重视兼容性的环境中还会继续使用，但它会逐渐被AES所取代。

- 现在大家应该使用的算法是AES(`Rijndael`),因为它安全、快速，而且能够在各种平台上工作。此外，由于全世界的密码学家都在对AES进行不断的验证，因此即便万一发现它有什么缺陷，也会立刻告知全世界并修复这些缺陷。





#### 一次性密码本——无法被破译

因为无法判断是否为正确的明文，在破译过程中会出现所有的排列组合

又称为维纳密码（`Vernam cipher`）

香农证明其为无条件安全、理论上无法破译

#### DES |  `Data Encryption Standard`

- 56-bit 对称密钥, **64-bit明文输入**（每隔7bit会插入1bit错误检查的bit）
- 分组密码的一种，以64bit为分组
- 16 round Feistel网络
- 已经被破解了

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240526113303219.png" alt="image-20240526113303219" style="zoom:50%;" />

中间的 “子密钥” 指的是本轮加密所使用的密钥。在Feistel 网络中，每一轮都需要使用一个不同的子密钥。由于子密钥只在一轮中使用，它只是一个局部密钥，因此才称为子密钥 (`subkey`)。



1) 将输入的数据等分为左右两部分
2) 将输人的右侧直接发送到输出的右侧
3) 将输入的右侧发送到轮函数
4) 轮函数根据右侧数据和子密钥，计算出一串看上去是随机的比特序列
5) 将上一步得到的比特序列与左侧数据进行XOR运算，并将结果作为加密后的左侧



但是，这样一来 “右侧” 根本就没有被加密，因此我们需要用不同的子密钥对一轮的处理 重复若干次，并在每两轮处理之间将左侧和右侧的数据对调。



**解密**

#### 3DES  | `Triple DES`：

- 3DES 是对 DES 的加强，通过三次应用 DES 算法来增加安全性。
- 使用两到三个 56 位密钥。
- 三重DES并不是进行三次DES加密（加密 —加密 —加密），而是加密—解密——加密的过程。IBM公司设计，能够让3-DES兼容不同DES。

**三个密钥都相同**

当三重DES中所有的密钥都相同时，三重DES也就等同于普通的DES了。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529100522514.png" alt="image-20240529100522514" style="zoom:50%;" />



<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240506083826564.png" alt="image-20240506083826564" style="zoom:50%;" />

**一三密钥相同**

如果密钥1 和密钥3使用相同的密钥，而密钥2使用不同的密钥（也就是只使用两个DES，这种三重DES就称为DES-EDE2(图3 ( Decryption )—加密（Encryption )这个流程。





**三个不同密钥**

- 使用3个key，3重DES 运算；
- 密文分组成串技术：当前明文和前面密文64bit 做异或处理

![image-20240529095943964](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529095943964.png)

尽管三重DES目前还被银行等机构使用，但其处理速度不高，除了特别重视向下兼容性的 情况以外，很少被用于新的用途。





#### AES | `Advanced Encryption Standard`

- 新的对称密钥NIST标准(NIST(National Institute of Standards and Technology, 国家标准技术研究所) 用于替换DES
- 数据128bit成组加密：128, 192, or 256 bit keys
- 穷尽法解密如果使用1秒钟破解DES, 需要花149万亿年破解AES
- 像这样通过竞争来实现标准化（`standardization by competition`)的方式，正是密码算法选拔的正确方式
- 彻底杜绝了隐蔽式安全性（`security by obscurity`)

2000 年 10月2日，`Rijndael`力压群雄，被NIST选定为AES标准。



`Rijndael `的分组长度和密钥长度可以分别以32比特为单位在128比特到256比特的范围内 进行选择。不过在AES的规格中，分组长度固定为128比特，密钥长度只有128、192和256 比特三种。



其中每一轮分为`SubBytes`、`ShiftRows`、 `MixColumns` 和 `AddRoundKey` 共4 个步骤。

- `SubBytes`

![image-20240529101532403](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529101532403.png)

- `shiftrows`:每一行平移字节数也是不同的

![image-20240529101600609](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529101600609.png)

- mixcolumn

![image-20240529101833891](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529101833891.png)



最后，需要将`MixColumns` 的输出与轮密钥进行`XOR`, 即进行`AddRoundKey`处理。

解密过程` AddRoundKey — InvMixColumns — InvShiftRows —InvSubBytes`



!!! bug "如果密钥长度为 56比特，那么用暴力破解找到正确密钥需要平均尝试约$2^{28}$次。 "
    平均尝试次数是密钥总数的大约一半。当密钥长度为56比特时，密钥总数为$2^{56}$个，它的一半是$2^{56}$ ( 注意，不是指数56变成 一半得28,而是减1得55)。 因此，当密钥长度为56比特时，平均尝试次数为$2^{55}$次，大约相当于$3.6\times10^{16}$次。





### 分组密码

分组密码（`block cipher`)是每次只能处理特定长度的一块数据的一类密码算法，这里的 " —块” 就称为分组（`block`)。此外，一个分组的比特数就称为分组长度`blocklength`



- ECB模式：`Electronic Code Book mode`(电子密码本模式
- CBC模式：`Cipher Block Chaining mode`(密码分组链接模式） 
- CFB模式：`Cipher Feed Back mode` (密文反馈模式） 
- OFB模式：`Output Feed Back mode` ( 输出反馈模式） 
- CTR模式：`CounTeR mode`(计数器模式）

#### ECB

ECB模式中，明文分组与密文分组是一一对应的关 系，因此，如果明文中存在多个相同的明文分组，则这些明文分组最终都将被转换为相同的密 文分组。这样一来，只要观察一下密文，就可以知道明文中存在怎样的重复组合，并可以以此 为线索来破译密码，因此ECB模式是存在一定风险的。



在ECB模式中，只要对任意密文分组进行替换，相应的明文分组也会被替换。此外，Mallory 所能做的还不仅限于替换，例如.如果将密文分组删除，则相应的明文分组 也会被删除，如果对密文分组进行复制，则相应的明文分组也会被复制。

> A向B转账1亿元，只要吧密文交换位置，就变成了B向A转一亿元

#### CBC | `Cipher Block Chaining`

**密码块**：如果输入块重复，将会得到相同的密文块

**密码块链**：

异或第`i`轮输入`m(i)`, 与前一轮的密文, `c(i-1)`  

`c(0)` 明文传输到接收端



$mac=MAC(K_{mac},message)$

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240506084559460.png" alt="image-20240506084559460" style="zoom:50%;" />

是一种用于分组密码的加密模式。在CBC模式中，每个明文分组在加密之前会先与前一个密文分组进行XOR运算，然后再进行加密。这种方式使得密文分组之间相互连接，像链条一样

当加密第一个明文分组时，由于不存在前一个密文分组，因此需要使用一个初始化向量（Initialization Vector，IV）来代替。初始化向量是一个随机生成的比特序列，其长度与分组长度相同。每次加密时，都会使用不同的初始化向量，以增加加密的安全性。

CBC模式的特点包括：

- 明文分组在加密之前一定会与前一个密文分组进行XOR运算，因此相同的明文分组在不同的上下文中会产生不同的密文分组。
- 在加密过程中，无法单独对一个中间的明文分组进行加密，因为每个密文分组都依赖于前一个密文分组。

**密文分组损坏**，则最多只有两个分组会受到影响。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529114556558.png)

**bit缺失**

导致密文分组的长度发生变化，此后的分组发生错 位，这样一来，缺失比特的位置之后的密文分组也就全部无法解密了



![image-20240529114626002](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529114626002.png)

确保互联网安全的通信协议之一`SSL/TLS`, 就是使用CBC模式来确保通信的机密性的，如使 用CBC模式三重DES的3DES_EDE _CBC以及CBC模式256比特AES的AES _256 _CBC等。





!!! note "初始化向量"
	在CBC模式中，我们假设永远使用相同的初始化向量。于是，当用同一密钥对同一明文进行加密时，所得到的密文一定是相同的。 <br>例如，密码破译者间隔一周收到了两份相同的密文。于是，密码破译者无需破译密码，就可以判断出：这份密文和上周的密文一样，因此两份密文解密所得到的明文也是一样的。如果在每次加密时都改变初始化向量的值，那么即便是用同一密钥对同一明文进行加密，也可以确保每次所得到的密文都不相同。

#### CFB



#### OFB



#### CTR



### 非对称加密

**公钥只能用做数据加密。公钥加密的数据，只能用对应的私钥才能解密。这是非对称加密的核心概念**。

对称密码通过将明文转换为复杂的形式来保证其机密性，相对地，公钥密码则是基于数学上闲难的问题来保证机密性的。例如RSA就利用了大整数的质因数分解问题的闲难度。**因此，对称密码和公钥密码源于两种根本不同的思路。**

!!! note "为机密性的高低是根据密钥长度而变化的。"
	这个问题无法冋答，因为机密性的高低是根据密钥长度而变化的。

!!! note "密钥长度为256比特的对称密码AES, 与密钥长度为1024比特的公钥密码RSA相比，RSA的安全性更高吗？"
    公钥密码的密钥长度不能直接与对称密码的密钥长度进行比较，而且对不同密码算法的强度进行比较本来就不是一件容易的事。<br>
    尽管如此，在将对称密钥和公钥密码结合起来使用的场景中.我们还是希望使两者的强度保持一定的平衡。很多密码系统中都会给出一些密码算法的理想组合方式，并打包成密码套件( `cipher suite` )<br>
    ![image-20240529122411971](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529122411971.png)

> 首先，将物品放人寄物柜中。然后，投入硬币并拔出钥匙，就可以将寄物柜关闭了。关闭 后的寄物柜，没有钥匙是无法打开的。 <br>只要有硬币，任何人都可以关闭寄物柜，但寄物柜一旦被关闭，再怎么投币也无法打开。 打开寄物柜需要使用钥匙，而不是硬币。 <br>因此我们可以说，硬币是关闭寄物柜的密钥，而钥匙则是打开寄物柜的密钥。



加密

> 我给你一把锁，钥匙只有我自己拿着，你把东西用我的锁锁起来
>

数字签名

> 使用私钥进行盖章，就知道这个锁是来源是谁了

!!! note "案例——小明小红去约会"
    1、小明确定了自己的私钥 mPrivateKey，公钥 mPublicKey。自己保留私钥，将公钥mPublicKey发给了小红<br>
    2、小红确定了自己的私钥 hPrivateKey，公钥 hPublicKey。自己保留私钥，将公钥 hPublicKey 发给了小明<br>
    3、小明发送信息 “周六早10点soho T1楼下见”，并且用小红的公钥 hPublicKey 进行加密。<br>
    4、小红收到信息后用自己的私钥 hPrivateKey 进行解密。然后回复 “收到，不要迟到” 并用小明的公钥mPublicKey加密。<br>
    5、小明收到信息后用自己的私钥 mPrivateKey 进行解密。读取信息后心里暗想：还提醒我不迟到？每次迟到的都是你吧？<br>
    以上过程是一次完整的request和response。通过这个例子我们梳理出一次信息传输的非对称加、解密过程：<br>
    1、消息**接收方**准备好公钥和私钥<br>
    2、私钥**接收方**自己留存、公钥发布给消息**发送方**<br>
    3、消息**发送方**使用接收方公钥对消息进行加密<br>
    4、消息**接收方**用自己的私钥对消息解密<br>



#### RSA | `Rivest, Shamir, Adelson algorithm`

![image-20240529115538998](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529115538998.png)

1978 年，`Ron Rivest`、`Adi Shamir`和`Reonard Adleman`共同发表了一种公钥密码算法 RSA





在中间步骤求mod,可以避免计算大整数的乘积。这种在计算过程中求mod来计算乘方的 方法，也是RSA的加密和解密算法中所使用的方法。



两个密钥不一样

- 公钥公开：证书方式

- 私钥：自己保留





RSA算法过程

**将两个大质数相乘是容易的，但是要将其乘积分解回原来的两个质数却极其困难。**
2004 年 Alexander May 证明了**求 RSA的私钥和对N进行质因数分解**是等价的。

1. 选择两个大质数 $p$ 和 $q$。
2. 计算它们的乘积 $n = pq$，$n$ 的长度就是密钥长度。
3. 计算 $n$ 的欧拉函数 $\phi(n) = (p-1)(q-1)$
4. 选择一个整数 $e$，使得 $e$ 与 $\phi(n)$ 互质，且 $1 < e < \phi(n)$。通常，$e$ 被选为65537。
5. 计算 $e$ 相对于 $\phi(n)$ 的模逆 $d$，即满足 $ed \equiv 1 \mod \phi(n)$ 的 $d$。

加密: 

$$
C = M^e \mod n
$$

解密: 

$$
M = C^d \mod n
$$

- $e$(encryption)和$n$(number)的组合$\{E,N\}$就是公钥。

- $d$(decryption)和$n$(number)的组合$\{D,N\}$就是私钥。(由于W是公钥的一部分，是公开的，因此单独将D称为私钥也是可以的)



证明目标: 显示解密操作确实恢复了原始消息 $M$。 

证明过程: 

1. 根据欧拉定理，如果 $gcd(M, n) = 1$，则 $M^{\phi(n)} \equiv 1 \mod n$。 
2. $ed = 1 + k\phi(n)$ 表示 $e$ 和 $d$ 是模 $\phi(n)$ 的乘法逆元
3. 因此，$M^{ed} = M^{1+k\phi(n)} = M \cdot (M^{\phi(n)})^k$。 由于 $M^{\phi(n)} \equiv 1 \mod n$，我们得到 $M^{ed} \mod n = M \mod n$，这证明了解密后我们可以得到原始消息 $M$。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240216123200169.png" alt="image-20240216123200169" style="zoom:50%;" />

#### 机密性分析

> [[CTF密码学\]RSA相关题目解题方法与python脚本总结](https://blog.csdn.net/qq_46145027/article/details/125047313)

中间人攻击——消息认证和证书



密码破译者知道的信息

- 密文：可以通过窃听来获取
- 数E和N：公钥是公开的信息。因此密码破译者知道E和N

密码破译者不知道的信息

- 明文：需要破译的内容
- 数D：私钥中至少D是不知道的信息
- 其他：密码破译者不知道生成密钥对时所使用的p、q和L



**通过密文来求得明文**

RSA加密过程如下。

密文 = 明文^E mod N (RSA加密)

由于密码破译者知道密文、E和N，那么有没有一种方法能够用E次方mod N之后的密文求出原来的明文呢？如果没有mod N的话，即：

密文 = 明文

通过密文求明文的难度不大，因为这可以被看作是一个求对数的问题。

但是，加上mod N之后，求明文就变成了求离散对数的问题，这是非常困难的，因为人类还没有发现求离散对数的高效算法。



**通过暴力破解来找出D**

现在，RSA中所使用的p和q的长度都是1024比特以上，N的长度为2048比特以上。由 于E和D的长度可以和N差不多，因此要找出D,就需要进行2048比特以上的暴力破解。要 在这样的长度下用暴力破解找出D是极其困难的。

**通过E和N求出D**

那就是质数p和q不能被密码破译者知道。把p和q交给密码破译者与把私钥交给密码破译者是等价的。

##### **对N进行质因数分解攻击**

**一旦发现了对大整数进行质因数分解的高效算法，RSA就能够被破译**

适用情况：n已知且可因式分解

既然n = p*q，那么最常规的想法就是把n因式分解得到p,q，上面说n很难分解，但对于一些不太大的n，我们可以借助工具去分解它。下面介绍两种常规因式分解方法：

第一种：在线因式分解网站，例如[factordb.com](http://www.factordb.com/)，我们可以利用在线网站快速分解出p,q

第二种：yafu大数分解工具，windows下载地址：yafu download | SourceForge.net使用相关命令分解n

```python
import gmpy2
from Crypto.Util.number import long_to_bytes
 
 
q = 189239861511125143212536989589123569301
p = 386123125371923651191219869811293586459
 
e = 65537
c = 28767758880940662779934612526152562406674613203406706867456395986985664083182
#n = 73069886771625642807435783661014062604264768481735145873508846925735521695159
n = q*p

d = gmpy2.invert(e, (p - 1) * (q - 1))
print("d=",d)
m = pow(c, d, n)

print(m)
print(long_to_bytes(m))
```



##### 通过推测p和q进行攻击

即便不进行质因数分解，密码破译者还是有可能知道p和q。 由于p和q是通过伪随机数生成器产生的，如果伪随机数生成器的算法很差，密码破译者 就有可能推测出来q和p因此使用能够被推测出来的随机数是非常危险的。

```python
# 签到题，已知p,q
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

p = 0x848cc7edca3d2feef44961881e358cbe924df5bc0f1e7178089ad6dc23fa1eec7b0f1a8c6932b870dd53faf35b22f35c8a7a0d130f69e53a91d0330c0af2c5ab
q = 0xa0ac7bcd3b1e826fdbd1ee907e592c163dea4a1a94eb03fd4d3ce58c2362100ec20d96ad858f1a21e8c38e1978d27cd3ab833ee344d8618065c003d8ffd0b1cb
e = 0x10001
c = 0x39f68bd43d1433e4fcbbe8fc0063661c97639324d63e67dedb6f4ed4501268571f128858b2f97ee7ce0407f24320a922787adf4d0233514934bbd7e81e4b4d07b423949c85ae3cc172ea5bcded917b5f67f18c2c6cd1b2dd98d7db941697ececdfc90507893579081f7e3d5ddeb9145a715abc20c4a938d32131013966bea539

# 因为给了p,q 相当于就给到了私钥了
n = p * q
phi_n = (p - 1) * (q - 1)

d = mod_inverse(e, phi_n) # 求模逆

m = pow(c, d, n) # 解密方法，求明文

print(m)
print(long_to_bytes(m))
# flag = AAA{Ace_Attorney_is_very_fun_Phoenix_Wright&Miles_Edgeworth}
```



##### 直接开根——N很大，e指数很小

```python
# 例题 ZJUAAA SimpleRSA
import gmpy2
from Crypto.Util.number import *

c=431396049519259356426983102577521801906916650819409770125821662319298730692378063287943809162107163618549043548748362517694341497565980142708852098826686158246523270988062866178454564393347346790109724455155942667492571325721344535616869

n=0x6270470b5e45bb464233683c38eeb03d17d54e0127038c9d286b00ac54946cfa1aa05c33610ec439c449b31f705c9e470ab6443cd090f9d88fab68f016c41bc00b9a1def40e77d836252ff03db2a525742e49b824d375216370d1cd810a60e2eac1824f306205c144b54c5f010ae17c8c88e76d1b41f13313cbd7e1b37822a0d

e=3

def de(c, e, n):
    k = 0
    while True:
        m = c + n * k
        result, flag = gmpy2.iroot(m, e)
        if True == flag:
            return result
        k += 1

m = de(c, e, n)
print(m)
print(long_to_bytes(m))
```


#### ECC 椭圆曲线密码学
- 基于椭圆曲线上的离散对数问题（ECDLP），类似Diffie-Hellman 密钥交换
- $g$是椭圆曲线上的一个公开点, $\alpha$ 是秘密值，计算 $\alpha \cdot g$ 是容易的
但给定 $g$ 和$\alpha \cdot g$，要找到 $\alpha$ 是困难的
- 相比 RSA，ECC 能够在更短的密钥长度下提供相同的安全性


### 混合密码

> 油电混动

对称密码提高速度，用公钥密码保护会话密钥

- 用对称密码加密消息 

- 通过伪随机数生成器生成对称密码加密中使用的会话密钥 

- 用公钥密码加密会话密钥 

- 从混合密码系统外部赋予公钥密码加密时使用的密钥





加密与解密过程

![image-20240529135817229](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529135817229.png)

![image-20240529135843902](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529135843902.png)

密钥长度的平衡 

混合密码系统中运用了对称密码和公钥密码两种密码方式，无论其中任何一方的密钥过短，都可能遭到集中攻击，因此对称密码和公钥密码的密钥长度必须具备同等的强度。 然而考虑到长期运用的情况，公钥密码的强度应该要高于对称密码，因为对称密码的会话密钥被破译只会影响本次通信的内容，而公钥密码一旦被破译，从过去到未来的（用相同公 钥加密的）所有通信内容就都能够被破译了



### 伪随机数生成器

- 生成密钥 用于对称密码和消息认证码。

- 生成密钥对 用于公钥密码和数字签名。

- 生成初始化向量（IV) ：用于分组密码的CBC、CFB和OFB模式。 
- 生成nonce ：用于防御重放攻击以及分组密码的CTR模式等。 
- 生成盐 ：于基于口令的密码（PBE)等。

随机性

不可预测性：避免被攻击者看穿的不可预测性

是指攻击者在知道过去生成的伪随机数列的前提下，依然无法预测出下—个生成出来的伪随机数的性质。

![image-20240529153557497](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529153557497.png)

#### 线性同余法

![image-20240529153657516](C:/Users/Philfan/AppData/Roaming/Typora/typora-user-images/image-20240529153657516.png)



## 认证

### 散列函数——完整性

散列值，Hash，消息摘要，密码校验和，指纹

发送方、接受方需要确认报文在传输的过程中或者事后没有被改变

> 顺便说一句，单向散列函数中的 “散列” 的英文 “hash” 一词，原意是古法语中的 “斧子”，后来被引申为 “剁碎的肉末”，也许是用斧子一通乱剁再搅在一起的那种感觉吧。单向散列函数的作用，实际上就是将很长的消息剁碎，然后再混合成固定长度的散列值。

生成速度快、抗碰撞性、单向性；不能检测伪装，只能检测篡改



报文m 报文摘要H(m)

计算报文摘要的签名$K^-_B(H(m))$
单向散列函数所输出的散列值的长度是固定的

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529140951509.png" alt="image-20240529140951509" style="zoom: 50%;" />

报文摘要：互异、反向计算特别难

> 一车水果打成果汁，取1mL果汁进行签名，足以代表一车水果

![image-20240506091633237](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240506091633237.png)

- 首先，MD5是不安全的，因此不应该使用。 

- SHA-1 除了用于对过去生成的散列值进行校验之外，不应该被用于新的用途
- SHA-2 有效应对了针对SHA-1的攻击方法，因此是安全的，可以使用。
- SHA-3 是安全的，可以使用。  

 和对称密码算法一样，**我们不应该使用任何自制算法**。



> **弱抗碰撞性**：要找出和某条消息具备相同散列值的另一条消息是非常困难的
>
> **强抗碰撞性**：找出具有相同散列值但互不相同的两条消息是非常困难的



#### MD5散列函数 

四个步骤计算出128bit摘要

Calculating a checksum using mathematical algorithms

- It is impossible to guess the original data from the message digest
- Regardless of the size of the original data, the resulting message digest can be a fixed size

> This is the reason why it is used for digital signing and tamper-proofing

- A change of a single bit in the original data will result in a different message digest

  > Possibility of generating the same message digest is practically non-existent


MD4已经被攻破了,MD5强抗碰撞性被攻破

#### SHA-1 - 160bit报文摘要（git使用）

SHA-1是由NIST ( National Institute of Standards and Technology, 美国国家标准技术研究所）设计的一种能够产生160比特的散列值的单向散列函数。

SHA-1已经被列入 “可谨慎运用的密码清单”，即除了用于保持兼容性的目的以外，其他情况下都不推荐使用。

**SHA-1 的强抗碰撞性已于2005年被攻破**

#### SHA-256

SHA-256、SHA-384 和SHA512都是由NIST设计的单向散列函数，它们的散列值长度分别为256比特、384比特和512比特。这些单向散列函数合起来统称SHA-2,它们的消息长度也存在上限（SHA-256的上限接近于264比特，SHA-384和SHA-512的上限接近于2128比特）。

####  RIPEMD-160

160比特的散列值的单向散列函数



强抗碰撞性被攻破，但RIPEMD-160还没有被攻破



#### SHA-3——Keccak

Secure Hash Algorithm-3 新标准，公开竞争的方式进行标准化

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529144434563.png" alt="image-20240529144434563" style="zoom:50%;" />



#### 攻击方法

**针对弱抗碰撞性的攻击**

任何文件中都或多或少地具有一定的冗余性。利用文件的冗余性生成具有相 同散列值的另一个文件，这就是一种针对单向散列函数的攻击。

**生日攻击**

在这里，Mallory所进行的攻击不是寻找生成特定散列值的消息，而是要找到散列值相同的 两条消息，而散列值则可以是任意值。这样的攻击，一般称为生日攻击（`birthday attack`)或者 冲突攻击（`collision attack` )，这是一种试图破解单向散列函数的 “强抗碰撞性” 的攻击。

> 只要有23个人，有两个人生日一样的概率就大于了50%



### 消息认证——完整性、认证

消息认证码（`Message Authentication Code`)是一种确认完整性并进行认证的技术，取三个单词的首字母，简称为MAC。



消息认证码是一种与密钥相关联的单向散列函数，无法保证机密性也无法防止抵赖

![image-20240529145807418](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529145807418.png)



#### 实现方法

**使用单向散列函数实现**：HMAC

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529150336347.png" alt="image-20240529150336347" style="zoom:50%;" />



**使用分组密码实现**

分组密码的密钥作为消息认证码的共享密钥来使用，并用CBC模式（第4章）将消息全 部加密。此时，初始化向量（IV)是固定的。由于消息认证码中不需要解密，因此将除最后一 个分组以外的密文部分全部丢弃，而将最后一个分组用作MAC值。由于CBC模式的最后一个 分组会受到整个消息以及密钥的双重影响，因此可以将它用作消息认证码。例如，AES-CMAC ( RFC4493 )就是一种基于AES来实现的消息认证码。

#### 攻击方法与防御

发送方和接收方需要确认对方的身份。认证目的：避免重放攻击

Nonce: 一生只用一次的整数(R)



ap4.0: 对称密钥加密

为了证明Alice的活跃性, Bob发送给Alice一个nonce,R. 、

Alice 必须返回加密之后的R，使用双方约定好的key

问题：如何分发对称式加密的密钥



ap5.0：非对称密钥加密

Bob发送challenge R，Alice发送私钥加密的报文和公钥，

bob解密

漏洞：Trudy中间截获所有，`middle attack`

原因：不能可靠地拿到Alice的公钥

### 数字签名——认证、不可抵赖性

数字签名类比于手写签名

- 可验证性（对接收方）

- 不可伪造性（对发送方）

- 不可抵赖性（对第三方）

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529150956820.png" alt="image-20240529150956820" style="zoom:50%;" />

**用私钥进行这一行为只能由持有私钥的人完成**：数字签名是利用了 “没有私钥的人事实上无法生成使用该私钥所生成的密文” 这一性质来 实现的。这里所生成的密文并非被用于保证机密性，而是被用于代表一种只有持有该密钥的人 才能够生成的信息。

![image-20240529151054694](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529151054694.png)

也可以对消息的散列值签名

!!! note "签名会不会被重复使用"
    签名提取出来这一行为，就好像是现实世界中把纸质合同上的签名拓下来一样。然而在 数字签名中，签名和消息之间是具有对应关系的，消息不同签名内容也会不同，因此事实上是 无法做到将签名提取出来重复使用的。 <br>总之，将一份签名附加在别的消息后面，验证签名会失败。



### 密钥分发与证书

可信赖中介

> 证书其实和驾照差不多

!!! note "认证机构所做的工作并不是加密，而是对公钥加上数字签名"

#### 对称式解决 | KDC **Key Distribution Center**

为“密钥分发中心”。它是网络安全和加密通信中使用的一个中央服务器，负责分发网络中各方之间通信所需的密钥。

KDC是Kerberos认证协议中的核心组件，主要用于认证服务和分配对称密钥，以确保网络中的数据传输安全。



- 与KDC先建立起可信赖的对话关系
- KDC生成对称密钥

1. **认证请求**：用户客户端向KDC的认证服务请求认证，通常包括用户的ID和所请求服务的ID。 
2. **TGT发放**：KDC验证用户的凭证（如密码）。如果验证成功，KDC会发放一个票据授权票据（Ticket Granting Ticket, TGT），加密包含用户的权限信息，使用KDC的密钥加密。 
3. **服务票据请求**：当用户需要访问服务时，客户端使用TGT向KDC请求针对特定服务的服务票据（Service Ticket）。 
4. **服务票据发放**：KDC验证TGT，并且如果用户有权限访问请求的服务，KDC会发放一个服务票据，该票据使用服务的密钥加密，包含用户的身份信息。 
5. **服务访问**：用户客户端使用服务票据向服务进行认证。服务解密服务票据，验证用户的权限，然后允许访问。 
6. **通信加密**：客户端和服务之间的通信可以使用从KDC获得的会话密钥加密，确保数据传输的安全性。 

![image-20240216132053873](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240216132053873.png)





#### 非对称解决 | CA Certification Authorities

出厂自带CA的公钥

用CA的私钥签署了$$CA^-(Bob,K_B^+)$$​

![image-20240529152153523](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529152153523.png)

![image-20240217100652773](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217100652773.png)

- 串号(证书发行者唯一)
- 证书拥有者信息，包括算法和密钥值本身(不显示出来
- 证书发行者信息
- 有效日期
- 颁发者签名



根证书：根证书是未被签名的公钥证书或自签名的证书
- 拿到一些CA的公钥
- 渠道：安装OS自带的数字证书；从网上下载，你信任的数字证书



信任树：

- 信任了根
- 由根CA签署的给一些机构的数字证书，根信任机构
- 由于你信任了根，从而能够可靠地拿到根CA签发的证书，可靠地拿到这些机构的公钥



#### Diffie-Hellman

Diffie-Hellman 密钥交换( Diffie-Hellman key exchange )是 1976 年由 Whitfield Diffie 和 Martin Heilman 共同发明的一种算法。使用这种算法，通信双方仅通过交换一些可以公开的信息 就能够生成出共享的秘密数字，而这一秘密数字就可以被用作对称密码的密钥。IPsec中就使用 了经过改良的Diffie-Hellman 密钥交换。 

虽然这种方法的名字叫 “密钥交换”，但实际上双方并没有真正交换密钥，而是通过计算生 成出了一个相同的共享秘钥。因此，这种方法也称为Diffie-Hellman密钥协商（`Diffie-Hellman key agreement` )

![image-20240529152845886](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529152845886.png)

双方交换的数字（即能够被窃听者Eve知道的数字）一共有4个：P、 G,$ G^A \mod P$和$G^B \mod P $。根据这4个数字计算出Alice和Bob的共享密钥（$G^{AxB}\mod P$)是 非常困难的。

这个问题称为有限域（`finite field`)的离散对数问题。 

而有限域的离散对数问题的复杂度正是支撑Diffie-Hellman密钥交换算法的基础。

