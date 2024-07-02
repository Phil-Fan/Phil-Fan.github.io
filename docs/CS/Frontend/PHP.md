# PHP 备忘录
[PHP学习路线](https://www.runoob.com/w3cnote/php-learning-recommend.html)

!!! tip "学习路线"
    1. 熟悉HTML/CSS/JS等网页基本元素，完成阶段可自行制作简单的网页，对元素属性相对熟悉。
    2. 理解动态语言的概念和运做机制，熟悉基本的PHP语法。
    3. 学习如何将PHP与HTML结合起来，完成简单的动态页面。
    4. 接触学习MySQL，开始设计数据库。
    5. 不断巩固PHP语法，熟悉大部分的PHP常用函数，理解面向对象编程，MySQL优化，以及一些模板和框架。
    6. 最终完成一个功能齐全的动态站点。



## 基础语法
!!! note "优化之前写过的评论网页"


- PHP是一种开源的通用脚本语言，尤其适用于Web开发。
- PHP（全称：PHP：Hypertext Preprocessor，即"PHP：超文本预处理器"）是一种通用开源脚本语言。
- 有对应的解析器
- 弱类型语言，~~感觉和python有点像，但是学的不太透彻讲不出来~~

### 常量&变量&数组
```php
<?php
// 这是 PHP 单行注释

/*
这是
PHP 多行
注释
*/

$y=10; // 变量声明
global $x,$y;//在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字

// 常量声明
bool define ( string $name , mixed $value [, bool $case_insensitive = false ] )

const CONSTANT_NAME = "value";

// 区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com");
echo GREETING;    // 输出 "欢迎访问 Runoob.com"
echo greeting;   // 输出 "greeting"，但是有警告信息，表示该常量未定义
?>
```
PHP 文件的默认文件扩展名是 `.php`。

常量对大小写敏感，全局的。


### 输入输出

**echo** - 可以输出一个或多个字符串
**print** - 只允许输出一个字符串，返回值总为 1
提示：echo 输出的速度比 print 快， echo 没有返回值，print有返回值1。


```php
<?php
echo "<h2>PHP 很有趣!</h2>";
echo "Hello world!<br>";
echo "我要学 PHP!<br>";
echo "这是一个", "字符串，", "使用了", "多个", "参数。";
?>

<?php
$txt1="学习 PHP";
$txt2="RUNOOB.COM";
$cars=array("Volvo","BMW","Toyota");
 
print $txt1;
print "<br>";
print "在 $txt2 学习 PHP ";
print "<br>";
print "我车的品牌是 {$cars[0]}";
?>
```

定界符 EOF

**超级全局变量** 在PHP 4.1.0之后被启用, 是PHP系统中自带的变量，在一个脚本的全部作用域中都可用。

**魔术常量：** 有八个魔术常量它们的值随着它们在代码中的位置改变而改变。


- 数值数组：带有数字 ID 键的数组
- 关联数组：带有指定的键的数组，每个键关联一个值
- 多维数组：包含一个或多个数组的数组

```php
<?php
$cars=array("Volvo","BMW","Toyota");//数值数组
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");//关联数组
//遍历关联数组
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach($age as $x=>$x_value)
{
    echo "Key=" . $x . ", Value=" . $x_value;
    echo "<br>";
}
?>
```

`count() `函数用于返回数组的长度（元素的数量）：

### 运算

- 松散比较：使用两个等号 `==` 比较，只比较值，不比较类型。
- 严格比较：用三个等号 `===` 比较，除了比较值，也比较类型。
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240702171832.png)


```php
<?php
~ // 二进制取反
a.b //并置 "Hi"."Ha"	→ HiHa
x == y	//等于
x === y	//绝对等于(类型 & 值)
x <> y	//不等于
?>
```

### 结构
写法和c一样

```php
<?php
if (条件)
{
    if 条件成立时执行的代码;
}
elseif (条件)
{
    elseif 条件成立时执行的代码;
}
else
{
    条件不成立时执行的代码;
}
?>
```

函数

变量函数是指在 PHP 中，将一个变量作为函数名来调用的函数。
变量函数可以让我们在运行时动态地决定调用哪个函数。
```php
<?php
function functionName()
{
    // 要执行的代码
}

$func = 'foo';
$func();        // 调用 foo()

$func = 'bar';
$func('test');  // 调用 bar()
?>
```

## 高级特性
### PHP 表单

### PHP + MySQL



## 实战案例
