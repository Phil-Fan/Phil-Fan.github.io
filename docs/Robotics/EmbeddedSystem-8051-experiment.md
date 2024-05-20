# 8051 实验

## 实验

### 01 点亮一只发光二极管LED

按照这个图的接法，当1 脚是高电平时，LED 不亮，只有1 脚是低电平时，LED 才发亮。

因此要1 脚我们要能够控制，也就是说，我们要能够让1 管脚按要求变为高或低电平。即然
我们要控制1 脚，就得给它起个名字，总不

能就叫它一脚吧？叫它什么名字呢？设计51 芯片的INTEL 公司已经起好了，就叫它P1.0，这是规定，不能由我们来更改。

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240327113053124.png" alt="image-20240327113053124" style="zoom:50%;" />

## C51编程

<img src="https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240508102042152.png" alt="image-20240508102042152" style="zoom:40%;" />

以main函数为主体

C51片内空间有限，运算能力有限



特殊功能寄存器都定义好了

| 数据类型             | 长度(位)           | 取值范围     |                                |
| -------------------- | ------------------ | ---------------- | ------------------------------ |
| 字符型           | `signed char`  | 8            | -128~127                   |
|         | `unsigned char` | 8       | 0~255 |
| 整   型          | `signed int` | 16           | -32768~32767               |
|          | `unsigned int`  | 16       | 0~65535 |
| 长整型           | `signed long`  | 32           | -21474883648~21474883647   |
|          | `unsigned long` | 32       | 0~4294967295 |
| 浮点型           | `float`        | 32           | ±1.75494E-38~±3.402823E+38 |
| 位   型          | `bit`          | 1            | 0，1               |
|          | `sbit`          | 1        | 0，1 |
| 访问SFR        | `sfr`          | 8            | 0~255                      |
|          | `sfr16`         | 16       | 0~65535 |

存储器分类

| 存储器类型 | 长度（位） | 对应单片机存储器                                         |
| -------------- | -------------- | ------------------------------------------------------------ |
| `bdata`    | 1          | 片内RAM，位寻址区，共128位。（亦能字节访问） |
| `data`     | 8          | 片内RAM，直接寻址，共128字节。           |
| `idata`    | 8          | 片内RAM，间接寻址，共256字节。           |
| `pdata`    | 8          | 片外RAM，分页间址，共256字节。（`MOVX ＠Ri`） |
| `xdata`    | 16         | 片外RAM，间接寻址，共64k字节。（`MOVX ＠DPTR`） |
| `code`     | 16         | ROM区域，间接寻址，共64k字节。（`MOVC ＠DPTR`） |

​    访问片内RAM比访问片外RAM的速度要快得多，所以对于经常使用的变量应该置于片内RAM中，即用`bdata`、`data`、`idata`来定义；对于不经常使用的变量或规模较大的变量应该置于片外RAM中，即用`pdata`、`xdata`来定义。

```c
bit bdata flags；  /* 位变量flags定位在片内RAM的位寻址区 */
char data var；   /* 字符变量var定位在片内RAM区 */
float idata x,y,z； /* 实型变量x，y，z定位在片内间址RAM区 */
sfr  P1=0x90；      /* 定义P1口地址为90H */
```

默认 data 低128位上



特殊功能寄存器的定义

​       80C51单片机内部有21个特殊功能寄存器

`sfr 特殊功能寄存器名 = 地址常数;  `

`sbit 位变量名 = 特殊功能寄存器名^位的位置（0~7）`

```c
sfr SCON = 0x90；/*定义串行口控制寄存器，地址为0x90 */
sfr P0 = 0x80;  /*定义P0口，地址为0x80 */
sfr16 T2 = 0xCC;/*定义80C52的T2L地址为0xCC，T2H地址为0xCD*/   


sfr PSW=0xD0;/* 定义PSW寄存器地址为0xD0 */
sbit OV=PSW^2; /* 定义OV位为PSW.2，地址为0xD2 */
sbit CY=PSW^7; /* 定义CY位为PSW.7，地址为0xD7 */
```



### 运算与控制

与c语言一致

- 加减乘除mod
- 自增自减
- 关系运算
- 逻辑运算 `&&` `!` `||`
- 位运算符：单符号对位进行操作，双符号对字节进行操作
- 类型转换：`bit→char→int→long→float,signed→unsigned`

### 指针

一般指针占用3个字节：

- 第一个字节存放该指针的存储器类型编码（由编译模式的默认值确定）
- 第二和第三个字节分别存放该指针的高位和低位地址偏移量。

| 存储器类型 | `bdata/ data / idata  ` | `xdata` | `pdata` | `code  ` |
| ---------- | ----------------------- | ------- | ------- | -------- |
| 编码       | 0x00                    | 0x01    | 0xfe    | 0xff     |

> 例如：`xdata` 类型，地址为`0x1234`的指针表示为：第一字节为`0x01`，第二字节为`0x12`，第三字节为`0x34`。



一般指针可用于存取任何变量而不必考虑变量在80C51单片机存储空间的位置，许多C51库函数采用了一般指针。例如：

```c
char *xdata strptr； /* 位于xdata 空间的一般指针 */
int *data number；/* 位于data 空间的一般指针 */
```

### 函数

参数表有改造

函数的一般定义形式为：

```
返回值类型 函数名（形式参数列表）[编译模式][reentrant][interrupt n][using n]
{
 函数体
}
```

**`interrupt`区分中断函数和普通函数；**

`reentrant`用于定义可重入函数。

`interrupt n `用于定义中断函数，n为中断号，可以为0~31，通过中断号可以决定中断服务程序的入口地址。

`using n `用于确定中断服务函数所使用的工作寄存器组，n为工作寄存器组号，取值为0~3。 

| 中断源 | 外中断0 | 定时器0 | 外中断1 | 定时器1 | 串行口 |
| :----: | :-----: | :-----: | :-----: | :-----: | :----: |
|中断号|0|1|2|3|4|

**参数传递**

C语言和汇编语言的相互调用

| 传递的参数 | char、1字节指针 | int、2字节指针 | long、float | 一般指针   |
| ---------- | --------------- | -------------- | ----------- | ---------- |
| 参数1      | R7              | R6、R7         | R4~R7       | R1、R2、R3 |
| 参数2      | R5              | R4、R5         | R4~R7       | R1、R2、R3 |
| 参数3      | R3              | R2、R3         |             | R1、R2、R3 |



**库函数**

`reg51.h`

`reg52.h`



!!! note "实例"
    在一80C51单片机应用系统中，**外中断0**引脚接一个开关，**并行端口线P1.0**接一个发光二级管。<br>要求系统的功能是，开关闭合一次，发光二极管的状态改变一次。相应的程序为：<br>

    ```c
    #include “reg51.h”
    #include “intrins.h”
    sbit P10 = P1^0
    Sbit INT0= P3^2
    void delay(void) //延时操作
    {
        int a = 5000;
        while(a--)
            _nop_( );
    }
    void int_srv (void) interrupt 0 
    {
        delay( );
        if(INT0 == 0){
            P10 = ! P10;
            while(INT0 == 0);//按下后等待，而不会一直切换
        }
    }
    void main()
    {
        P10 = 0;
        EA = 1;//中断使能
        EX0 = 1;
        while(1);
    } 
    ```



!!! note "定时计数器编程示例"
    例  利用定时/计数器`T0`的方式1，产生10ms的定时，并使`P1.0`引脚上输出周期为20ms的方波，采用中断方式，设系统时钟频率为`12 MHz`。<br><br>
    1、计算计数初值X：<br>
    由于晶振为`12 MHz`，所以机器周期$T_{cy}$​为$1\mu s$​。因此：
    $N＝\frac{t}{T_{cy}} =10\times10-3/1\times10-6=10000$​<br>
    因计数器是向上计数，计数到10000时溢出，所以计数器初值为-10000。应将` -(10000/256)`送入`TH0`中，`-(10000%256)`送入`TL0`中。<br>
    2、求`T0`的方式控制字`TMOD`：<br>
    M1M0=01，GATE=0，C/    =0，可取方式控制字为`01H`；<br>
    ```c
    #include “reg51.h”
    sbit P10 = P1^0;
    void timer0(void) interrupt 1
    {
        P10 = ! P10;
        TH0 = -(10000/256);//重新初始化
        TL0 = -(10000%256);
    }
    void main(void)
    {
        TMOD = 0x01;			//定时器初始化
        P10 = 0;
        TH0 = -(10000/256);
        TL0 = -(10000%256);		//初始值
        EA = 1;					//中断使能
        ET0 = 1;
        TR0 = 1;				//启动计时器
        while(1);
    } 
    ```



!!! note "A/D转换接口编程示例"
    ADC0809与单片机的接口电路如图所示。采用查询方式采集数据的应用程序为：<br>![image-20240508112233118](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/image-20240508112233118.png)<br>
    ```c
    # include “reg51.h”
    # include “absacc.h”
    # define uchar unsigned char
    # define IN0 XBYTE[0x7ff8]
    sbit ad_busy = P3^3;
    void main(void)
    {
        uchar data ad[10];
        while(1)
        {
            ad0809(ad);
        }
    } 
    void ad0809(uchar idata *x)
    {
        uchar i;
        uchar xdata * ad_adr;
        ad_adr = & IN0;
        for(i = 0；i < 8；i ++)
        {
            * ad_adr = 0; 			/*启动转换*/
            i = i;              	/*延时等待*/
            i = i;
            while(ad_busy == 0);
            x[i] = * ad_adr;  		/*存转换结果*/
            ad_adr ++;            	/*下一通道*/
        }
    }
    ```




### 文件



•.c文件：函数、变量的定义

•.h文件：可被外部调用的函数、变量的声明

- 任何自定义的变量、函数在调用前必须有定义或声明（同一个.c）

- 使用到的自定义函数的.c文件必须添加到工程参与编译

- 使用到的.h文件必须要放在编译器可寻找到的地方（工程文件夹根目录、安装目录、自定义）

## 数码管

共阴极接法



对应表

```c
u8 code smgduan[50]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,
                    0x77,0x7c,0x39,0x5e,0x79,0x71,0x3d,
                    0x76,0x0f,0x0e,0x75,0x38,0x37,0x54,
                    0x5c,0x73,0x67,
                    0x31,0x49,0x78,
                    0x3e,0x1c,0x7e,0x64,0x6e,0x59};
```



交通灯实验代码，改了部分端口

整理了一下才发现还是需要读懂代码到底干了什么



下面的代码大概有三个功能

1. 端口的定义和映射，要和连线一一对应
2. 数码管的赋值和显示
3. 中断函数与定时器的设置

```c
#include "reg52.h" 
typedef unsigned int u16;
typedef unsigned char u8;

sbit LSA=P2^5;//这里端口随便改都行，和实际接口一致就可以
sbit LSB=P2^6;
sbit LSC=P2^7;

//定义灯的映射关系
#define GPIO_DIG   P0
#define GPIO_TRAFFIC P1
sbit RED10   = P1^0;
sbit GREEN10 = P1^1;
sbit RED11   = P1^2;
sbit YELLOW11= P1^3;
sbit GREEN11 = P1^4;
sbit RED00   = P3^0;
sbit GREEN00 = P3^1;
sbit RED01   = P1^5;
sbit YELLOW01= P1^6;
sbit GREEN01 = P1^7;

u8 code smgduan[50]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,
                    0x77,0x7c,0x39,0x5e,0x79,0x71,0x3d,
                    0x76,0x0f,0x0e,0x75,0x38,0x37,0x54,
                    0x5c,0x73,0x67,
                    0x31,0x49,0x78,
                    0x3e,0x1c,0x7e,0x64,0x6e,0x59};

u8 DisplayData[8];
u8 Second;

void delay(u16 i)
{
	while(i--);	
}

void DigDisplay()
{
	u8 i;
	for(i=0;i<8;i++)
    //这个循环的意思是：对于8位数码管的每一位，先通过译码器选择对应位，再赋对应的数值
	{
		switch(i)
		{
			case(0):
				LSA=0;LSB=0;LSC=0; break;
			case(1):
				LSA=1;LSB=0;LSC=0; break;
			case(2):
				LSA=0;LSB=1;LSC=0; break;
			case(3):
				LSA=1;LSB=1;LSC=0; break;
			case(4):
				LSA=0;LSB=0;LSC=1; break;
			case(5):
				LSA=1;LSB=0;LSC=1; break;
			case(6):
				LSA=0;LSB=1;LSC=1; break;
			case(7):
				LSA=1;LSB=1;LSC=1; break;
		}
		GPIO_DIG=DisplayData[i];
		delay(100);
		GPIO_DIG=0x00;
	}
}

void Timer0Init()	//定时器的初始化和开关
{
	TMOD|=0X01;
	TH0 = 0XFC;
	TL0 = 0X18;	//计算中断条件
	ET0 = 1;//打开定时器0中断开关
	EA = 1;//打开中断总开关
	TR0 = 1;//打开定时器0
}


void main()
{	
	Second = 1;
	Timer0Init();	//这里打开定时器

	while(1)
	{
        DisplayData[4] = 0x71;//F
		DisplayData[5] = 0x3e;//U
		DisplayData[6] = 0x39;//C
		DisplayData[7] = 0x75;//K
        //可以删掉上边四行
		if(Second == 30)
		{
			Second = 1;
		}

		if(Second < 11)
		{
			DisplayData[0] = 0x00;
			DisplayData[1] = 0x00;
			DisplayData[2] = smgduan[(10 - Second) % 100 / 10];
			DisplayData[3] = smgduan[(10 - Second) %10];

			DigDisplay();
			GPIO_TRAFFIC = 0xFF;
			RED00 = 1;
			GREEN00 = 1;
			GREEN11 = 0;			
			GREEN10	= 0;
			RED01 = 0; 
			RED00 = 0;
		}

		else if(Second < 16) 
		{
			DisplayData[0] = 0x00;
			DisplayData[1] = 0x00;
			DisplayData[2] = smgduan[(15 - Second) % 100 / 10];
			DisplayData[3] = smgduan[(15 - Second) %10];
			DigDisplay();
            
			GPIO_TRAFFIC = 0xFF;
			RED00 = 1;
			GREEN00 = 1;
			YELLOW11 = 0;			
			RED10	= 0;
			YELLOW01 = 0;
			RED00 = 0;
		}
		else if(Second < 26) 
		{
			DisplayData[0] = 0x00;
			DisplayData[1] = 0x00;
			DisplayData[2] = smgduan[(25 - Second) % 100 / 10];
			DisplayData[3] = smgduan[(25 - Second) %10];
			DigDisplay();
            
			GPIO_TRAFFIC = 0xFF;
			RED00 = 1;
			GREEN00 = 1;
			RED11 = 0;	
			RED10 = 0;
			GREEN01 = 0;
			GREEN00 = 0;
		}

		else 
		{
			DisplayData[0] = 0x00;
			DisplayData[1] = 0x00;
			DisplayData[2] = smgduan[(30 - Second) % 100 / 10];
			DisplayData[3] = smgduan[(30 - Second) %10];
			DigDisplay();
			GPIO_TRAFFIC = 0xFF;
			RED00 = 1;
			GREEN00 = 1;

			YELLOW11 = 0;		
			RED10	= 0;

			YELLOW01 = 0;
			RED00 = 0;      
		}
	}					
}

void Timer0() interrupt 1
{
	static u16 i;
	TH0=0XFC;	
	TL0=0X18;
	i++;
	if(i==1000)
	{
		i=0;
		Second ++;	
	}	
}
```



## LED

LED 采用共阳接法

所以高电平是熄灭

拉电流——电流更大

灌电流——电流小，不足以驱动