# 网络安全

??? note "来源"

- USTC《计算机网络》

- 《图解密码技术》

- 《信息物理系统安全》

![image-20240522172938101](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240522172938101.png)

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



#### RSA: `Rivest, Shamir, Adelson algorithm`

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

**对N进行质因数分解攻击**

**一旦发现了对大整数进行质因数分解的高效算法，RSA就能够被破译**



**通过推测p和q进行攻击** 

即便不进行质因数分解，密码破译者还是有可能知道p和q。 由于p和q是通过伪随机数生成器产生的，如果伪随机数生成器的算法很差，密码破译者 就有可能推测出来q和p因此使用能够被推测出来的随机数是非常危险的。



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



#### 随机数





## 认证

### 散列函数——完整性

散列值，Hash，消息摘要，密码校验和，指纹

发送方、接受方需要确认报文在传输的过程中或者事后没有被改变



报文m 报文摘要H(m)

计算报文摘要的签名$K^-_B(H(m))$

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240529140951509.png" alt="image-20240529140951509" style="zoom: 50%;" />

报文摘要：互异、反向计算特别难

> 一车水果打成果汁，取1mL果汁进行签名，足以代表一车水果

![image-20240506091633237](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240506091633237.png)

#### MD5散列函数 

四个步骤计算出128bit摘要

Calculating a checksum using mathematical algorithms

- It is impossible to guess the original data from the message digest
- Regardless of the size of the original data, the resulting message digest can be a fixed size

> This is the reason why it is used for digital signing and tamper-proofing

- A change of a single bit in the original data will result in a different message digest

  > Possibility of generating the same message digest is practically non-existent

- SHA-1 - 160bit报文摘要（git使用）

- SHA-256





公钥机制也有它的缺点，那就是**效率非常低**

所以使用公私钥算法结合的方法

用非对称算法对 对称密钥进行加密，明文使用对称密钥进行加密

- 私钥用来进行解密和签名，是给自己用的。
- 公钥由本人公开，用于加密和验证签名，是给别人用的。
- 当该用户发送文件时，用私钥签名，别人用他给的公钥解密，可以保证该信息是由他发送的。即数字签名。

### 消息认证——完整性、认证

发送方和接收方需要确认对方的身份

认证目的：避免重放攻击

Nonce: 一生只用一次的整数(R)



ap4.0: 对称密钥加密

为了证明Alice的活跃性, Bob发送给Alice一个nonce,

R. Alice 必须返回加密之后的R，使用双方约定好的key

问题：如何分发对称式加密的密钥



ap5.0：非对称密钥加密

Bob发送challenge R，Alice发送私钥加密的报文和公钥，bob解密

漏洞：Trudy中间截获所有，`middle attack`

原因：不能可靠地拿到Alice的公钥

### 数字签名——认证、不可抵赖性

数字签名类比于手写签名

- 可验证性（对接收方）

- 不可伪造性（对发送方）

- 不可抵赖性（对第三方）



### 密钥分发与证书

可信赖中介

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

用CA的私钥签署了$$CA^-(Bob,K_B^+)$$

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



## 安全场景







### 安全

!!! note "What is Security? "
	Confidentiality, Integrity, Availability (CIA triad)

"CIA三元组"，它由保密性（Confidentiality）、完整性（Integrity）和可用性（Availability）三个要素组成，用于描述一个安全系统所需的基本属性。

保密性是指保护系统和数据不被未授权的访问或泄露；

完整性是指确保数据的准确性和一致性，防止未经授权的修改或破坏；

可用性是指确保系统和数据在需要时可被授权用户访问和使用。



!!! note "What Security Do We Need? "
	Integrity, Confidentiality, Authenticity, Non-repudiation (I-CAN)

"I-CAN"，它由完整性（Integrity）、保密性（Confidentiality）、认证性（Authenticity）和不可否认性（Non-repudiation）四个要素组成，用于描述一个安全系统所需的具体要求。

Integrity | 完整性 : implementation using **message signature**

Confidentiality | 保密性 : implementation using data encryption

Authenticity | 认证性 : implementation using **challenge - response**,登录

> 两个特工：天王盖地虎-宝塔镇河妖

Non-repudiation | 不可否认性 : implementation using **message signature**。用私钥加密，公钥解密





### HTTP 认证

#### 基本认证

当一个客户端向 HTTP 服务器进行数据请求时，如果客户端未被认证，则 HTTP 服务器将通过基本认证过程对客户端的用户名及密码进行验证，以决定用户是否合法。

客户端在接收到 HTTP 服务器的身份认证要求后，会提示用户输入用户名及密码，然后将用户名及密码以`BASE64`加密，加密后的密文将附加于请求信息中。

> 如当用户名为`anjuta`，密码为：`123456`时，客户端将用户名和密码用“：”合并，并将合并后的字符串用`BASE64`加密为密文，并于每次请求数据时，将密文附加于请求头（Request Header）中

HTTP 服务器在每次收到请求包后，根据协议取得客户端附加的用户信息（`BASE64`加密的用户名和密码），解开请求包，对用户名及密码进行验证

BASIC 认证的步骤：

1. 客户端访问一个受 HTTP 基本认证保护的资源；

2. 服务器返回 `401` 状态，要求客户端提供用户名和密码进行认证。（验证失败的时候，响应头会加上`WWW-Authenticate: Basic realm="请求域"`），如下所示：

   ```
   401 Unauthorized
   WWW-Authenticate： Basic realm="WallyWorld"
   ```

3. 客户端将输入的用户名密码用`Base64`进行编码后，采用非加密的明文方式传送给服务器；

   ```
   Authorization: Basic xxxxxxxxxx.
   ```

4. 服务器将 `Authorization` 头中的用户名密码解码并取出，进行验证，如果认证成功，则返回相应的资源；如果认证失败，则仍返回 `401` 状态，要求重新进行认证。



#### 摘要认证 digest authentication

该认证是 HTTP1.1 提出的基本认证的替代方法，不包含密码的明文传递。 摘要认证使用`随机数 + MD5 加密哈希函数`来对用户名、密码进行加密，在上述第二步时，服务器返回随机字符串 `nonnce` 之后，客户端发送摘要`MD5（HA1:nonce:HA2）`。 其中`HA1=MD5(username:realm:password),HA2=MD5(method:digestURI)`。

#### 开放认证 OAuth Authentication

开放认证允许用户提供一个令牌，而不是用户名和密码来访问它们存放在特定服务器的数据，每一个令牌授权一个特定的第三方系统。

#### 令牌认证 Token Authentication

令牌认证是指当用户第一次登陆时，服务器生成一个 token 并返回给客户端，之后的每次访问客户端都会带上该 token，无需再次带上用户名和密码。

#### 基本认证中的认证相关字段

（1）服务器响应状态码与状态描述：当服务器响应状态码为 401 时，表明服务器资源需要认证。 其状态描述为`Unauthorized`，表明未通过认证，当响应`200 OK`时，表明通过认证，正常响应； 

（2）当用户提供用户名和密码后，重新提出请求时：  ` Authorization: Basic xxxxxxxxxx. ` `Authorization` 字段表明在请求中，提供了需要的认证方式和认证信息（已经经过加密）。



### 安全电子邮件

私密性：对称式+非对称式

可认证性和报文完整性：传报文和数字签名（用对称式密钥加密），密钥用对方公钥加密；

​	如果接收方bob算出的报文摘要和传过来的报文摘要是相同的

PGP 电子邮件加密方案

应用层

![image-20240217101521016](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217101521016.png)

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217101539896.png" alt="image-20240217101539896" style="zoom: 67%;" />

### SSL (secure sockets layer)

为使用SSL服务的、基于TCP的应用提供传输层次的安全性

步骤

- 握手
- 密钥导出
- 数据传输

传输层



### IPsec

网络层

双方要建立通信关系

Authentication Header (AH) 协议

提供源端的可认证性，数据完整性，但是不提供机密性



ESP 协议

提供机密性，主机的可认证性，数据的完整性



### 802.11 security

链路层的安全





## 运行中的安全性

### 手段

#### 病毒 virus

计算机病毒是一种计算机程序，它在执行时将自己附于其他程序或文件并编写其自己的代码，从而能够从一个程序传播到另一个程序，并在传播过程中感染计算机。

几乎所有的计算机病毒都附于一个可执行文件，**不点击不感染**！

#### 蠕虫 worm

**自我复制！独立运行！**

蠕虫在设计上类似于计算机病毒，但它是病毒或特洛伊木马程序的一个子类别。

然而与病毒不同的是，它能够在不附于主机程序的情况下传播，并且可以独立运行。

蠕虫利用了系统中的文件或信息传输功能，使其能在无帮助的情况下传播。其结果是蠕虫消耗了太多的系统内存（或网络带宽），从而导致Web服务器、网络服务器和个人的计算机停止响应。

> 一个例子是蠕虫向您的电子邮件地址簿列出的每个人发送其副本。然后，蠕虫继续自我复制并将自己发送给每个收件人的地址簿列出的每个人，并继续重复此过程.

#### 木马

特洛伊木马程序是指让用户误解其意图的各类恶意软件，例如看似是正版应用程序或软件程序但实际是破坏性程序。

特洛伊木马程序是根据古希腊神话中特洛伊木马的故事所命名的，特洛伊木马具有欺骗性，它摧毁了特洛伊城。与病毒不同，特洛伊木马程序不会自我复制，但它们同样具有破坏性。特洛伊木马还能打开计算机的后门，向恶意分子发出命令，或能让恶意用户/程序访问您的系统。这会导致机密信息和个人信息被盗。

### 攻击

- 加密算法已知，求密钥
- 加密算法和密钥均不知道
- 唯密文攻击
- 已知明文攻击
- 已经知道部分密文和明文的对应关系
- 选择明文攻击
- 攻击者能够选择一段明文，并得到密文

### 防火墙

将组织内部网络和互联网络隔离开来，按照规则进行分组过滤

防火墙在网络层



1.阻止拒绝服务攻击(DOS deny of service,DDOS distributive)：

SYN flooding: 攻击者建立很多伪造TCP链接，对于真正用户而言已经没有资源留下了

阻止非法的修改/对非授权内容的访问

2.只允许认证的用户能否访问内部网络资源(经过认证的用户/主机集合)

- 2种类型的防火墙:
  - 网络级别：分组过滤器
  - 应用级别：应用程序网关



规则

- 源IP地址,目标IP地址
- TCP/UDP源和目标端口
- ICMP报文类别
- TCP SYN 和ACK bits



#### 无状态规则

防火墙不维持通讯状态

| 策略                                                         | 设置                                                      |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| 所有的进出UDP流以及telnet 连接的数据报都被阻塞掉             | 只要拥有IP协议字段= 17，<br/>而且源/目标端口号= 23.       |
| 阻止外部客户端和内部网络的主机建立TCP连接<br/>但允许内部网络的客户端和外部服务器建立TCP连接 | 阻塞进入内网的TCP段：它的ACK=0.                           |
| 不允许外部的web进行访问                                      | 阻塞掉所有外出具有目标端口80的IP分组                      |
| 不允许来自外面的TCP连接，除非是机构公共WEB服务器的连接       | 阻塞掉所有进来的TCP SYN分组，除非130.207.244.203, port 80 |
| 阻止Web无线电占用可用带宽.                                   | 阻塞所有进来的UDP分组 除非DNS 和路由器广播                |
| 阻止你的网络被`smurf DoS`所利用                              | 阻塞掉所有具有广播地址的ICMP分组(eg130.207.255.255).      |
| 阻止内部网络被`tracerout`，从而得到你的网络拓扑              | 阻塞掉所有外出的ICMP TTL过期的流量                        |



#### 有状态规则

无状态分组过滤根据每个分组独立地检查和行动
有状态的分组过滤联合分组状态表检查和行动



知道连接后，才不被block掉；防火墙知道是否已经进行连接

防火墙变成了状态维护的设备



#### ACL `access control list`

最后一条规则，默认规则匹配所有



根据应用数据的内容来过滤进出的数据报，就像根据IP/TCP/UDP字段来过滤一样

- 检查的级别：应用层数据

对应用进行深度剖析

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217110805828.png" alt="image-20240217110805828" style="zoom:50%;" />

`IP spoofing`: 路由器不知道数据报是否真的来自于声称的源地址

更改IP的头部字段

对UDP要么全过，要么全不过



**折中: 与外部通信的自由度，安全的级别**



### 入侵检测系统 IDS intrusion detection system

multiple IDSs: 在不同的地点进行不同类型的检查

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240217111255212.png" alt="image-20240217111255212" style="zoom:50%;" />

在所有流量上放置sensor

- 深入分组检查: 检查分组的内容(e.g., 检查分组中的特征串已知攻击数据库的病毒和攻击串

- 检查分组间的相关性，判断是否是有害的分组

  • 端口扫描
  • 网络映射
  • DoS 攻击



映射:
- 在攻击之前： “踩点” – 发现在网络上实现了哪些服务
- 使用ping来判断哪些主机在网络上有地址
- 端口扫描：试图顺序地在每一个端口上建立TCP连接(看看发生了什么)



分组嗅探: 对策
- 机构中的所有主机都运行能够监测软件，周期性地检查是否有网卡运行于**混杂模式**
- 每一个主机一个独立的网段(交换式以太网而不是使用集线器)



IP Spoofing欺骗:
- 可以有应用进程直接产生“raw” IP分组, 而且可以在IP源地址部分直接放置任何地址
- 接收端无法判断源地址是不是具有欺骗性的
- e.g. C 伪装成B

设置入口过滤，出去的分组源IP应该和这个网段一致



Denial of service (DOS): 对策
- 在到达主机之前过滤掉这些泛洪的分组(e.g., SYN): throw out good with bad
- 回溯到源主机(most likely an innocent,compromised machine)



### 
