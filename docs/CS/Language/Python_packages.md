# Python 常用库
## csv库

- CSV（Comma-Separated Values）是以纯文本形式存储的表格化数据
- CSV文件由任意数目的记录组成，记录间以某种换行符分隔；每条记录由字段组成，字段间的分隔符是其它字符或字符串，最常见的是逗号或制表符
- Excel和Numbers都可以产生和读入CSV格式的文件
- 很多仪器产生CSV格式的实验结果数据
  - GPS模块给出的定位数据NEMA-0183就是一种CSV格式



- 读

```py
import csv

with open('13-1.csv','rt') as f: 
    reader = csv.reader(f)
    header = next(reader)
    print(header)
```



- 写

```py
with open('1.csv','wt') as f2:
   cw = csv.writer(f2)
   for item in l:
      cw.writerow(item)
   #或采用writerows()方法
   #cw.writerows(l) #将嵌套列表内容写入csv文件，每个外层元素为一行，每个内层元素为一个数据
```



- 改





## re 正则表达式

```py
import re

. 　　　　表示任何单个字符
[ ] 　　　字符集,对单个字符给出取值范围 　　　　　[abc]表示a、b、c,[a‐z]表示a到z单个字符
[^ ] 　　非字符集,对单个字符给出排除范围 　　　　[^abc]表示非a或b或c的单个字符
* 　　　　前一个字符0次或无限次扩展 　　　　　　　abc* 表示 ab、abc、abcc、abccc等
+ 　　　　前一个字符1次或无限次扩展 　　　　　　　abc+ 表示 abc、abcc、abccc等
? 　　　　前一个字符0次或1次扩展 　　　　　　　　abc? 表示 ab、abc
| 　　　　左右表达式任意一个 　　　　　　　　　　　abc|def 表示 abc、def
{m} 　　　扩展前一个字符m次 　　　　　　　　　　　ab{2}c表示abbc
{m,n} 　　扩展前一个字符m至n次(含n) 　　　　　　ab{1,2}c表示abc、abbc
^ 　　　　匹配字符串开头 　　　　　　　　　　　　^abc表示abc且在一个字符串的开头
$　　　　 匹配字符串结尾 　　　　　　　　　　　　　abc$表示abc且在一个字符串的结尾
( ) 　　　分组标记,内部只能使用 | 操作符 　　　　(abc)表示abc,(abc|def)表示abc、def
\d 　　　数字,等价于[0‐9] 
\w 　　　单词字符,等价于[A‐Za‐z0‐9_]
[\u4e00-\u9fa5] 中文字符
\s       空格

```



正整数: `^\d+$`
负整数: `^-\d+$`
电话号码: `^+?[\d\s]{3,}$`
电话代码: `^+?[\d\s]+(?[\d\s]{10,}$`
整数: `^-?\d+$`
用户名: `^[\w\d_.]{4,16}$`
字母数字字符: `^[a-zA-Z0-9]*$`
带空格的字母数字字符: `^[a-zA-Z0-9 ]*$`
密码: `^(?=^.{6,}$)((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.*$`
电子邮件: `^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})*$`
IPv4 地址: `^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))*$`
小写字母: `^([a-z])*`$`
大写字母: `^([A-Z])*$`
网址: ^(((http|https|ftp):\/\/)?([[a-zA-Z0-9]\-\.])+(\.)([[a-zA-Z0-9]]){2,4}([[a-zA-Z0-9]\/+=%&_\.~?\-]*))*$`
VISA 信用卡号码: `^(4[0-9]{12}(?:[0-9]{3})?)*$`
日期 (MM/DD/YYYY): `^(0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])[- /.](19|20)?[0-9]{2}$`
日期 (YYYY/MM/DD): `^(19|20)?[0-9]{2}[- /.](0?[1-9]|1[012])[- /.](0?[1-9]|[12][0-9]|3[01])$`
万事达信用卡号码: ^(5[1-5][0-9]{14})*$`

```py
     1)如果^是第一个字符，表示'非'：
       a='5f1a5FT,sf15f;/4sFyol46l'
       b=re.findall(r"[^a-z^0-4]",a) # 找出a中除小写字母和0-4之外的所有字符
       >>> ['5', '5', 'F', 'T', ',', '5', ';', '/', 'F', '6']
       
     2)'+'
       y=re.findall(r"\d+",a)
       >>> ['5', '1', '5', '15', '4', '46'] # ‘+’用于将前面的模式匹配1次或多次（贪婪模式）
       
       y=re.findall(r"\d",a)
       >>> ['5', '1', '5', '1', '5', '4', '4', '6'] # 没有加号，表示找到数字就结束，接着继续找下一个数字
       
     3)match
       # match 表示从头开始匹配，如果头没有匹配上的就是None，
       re.match(r'g','guanyonglai').group()  #返回g
       re.match(r'y','guanyonglai')  #返回None
       re.search(r'y','guanyonglai').group() #返回y
       
     4)'|'表示'或'：  2019-4-23 13:37:42 # 它在 []之中不再表示或，而表示他本身的字符。
       z=re.findall(r'[a-zA-Z]+|[0-9]+', r'alal ,b6al \56 fPython   \t Ac\n') # 找出数字或字母(数字和字母分开)
       >>> ['alal', 'b', '6', 'al', '56', 'fPython', 't', 'Ac', 'n', 'al']
       
       z=re.findall(r'[a-zA-Z0-9]+', r'alal ,b6al \56 fPython   \t Ac\n') # 找出数字和字母(数字和字母可以连一块)
       >>> ['alal', 'b6al', '56', 'fPython', 't', 'Ac', 'n']
       
     5)无捕获组 '(?: )' ：   2019-4-23 13:56:12
       z=re.findall(r'tho(n|p)', r'alal ,b6al \56 fPython   \t Ac\n')  # tho(n|p) 这样写达不到我们的要求，应当用误捕获组
       >>> ['n']
       z=re.findall(r'tho(?:n|p)', r'alal ,b6al \56 fPython   \t Ac\n')
       >>> ['thon']
       
     6)匹配行首行尾,头尾
       #匹配行首的字母，支持跨行    2019-4-23 14:15:33
       z=re.findall(r'^[a-z]+', 'alal ,b6al \56 \nfPython   \t Ac\n',re.M)
       >>> ['alal', 'f']
       
       z=re.findall(r'\d+$', 'alal ,b6al 56\nfPython\t4Ac\65',re.M) # 匹配行尾的数字(\6可能是个bug吧，匹配不到)
       >>> ['56', '5']
       
       # \A  只匹配整个字符串的开头，即使在 ’M’ 模式下，它也不会匹配其它行的行首。 2019-4-23 14:29:06
       z=re.findall(r'\A[a-z]+', 'alal ,b6al \56 \nfPython   \t Ac\n',re.M)
       >>> ['alal']
       
     7)单词的边界\b：   2019-4-23 14:48:25
       z=re.findall(r'\bth\b', 'alal ,b6 th al 56\nfPython\t4Ac\65') # 找到单独的'th'，，，\B相反：不能匹配以'th'为边界的字符串
       >>> ['th']
       
       z=re.findall(r'(?:\w+|\s+)th(?:\w+|\s+)', 'alal ,b6 th al 56\nfPython\t4Ac\65') # 找到所有含'th'的单词(\w包括数字和大小写字母)
       >>>[' th ', 'fPython']
       
     8)如何在正则表达式中包含变量： 2019-4-23 15:24:10
       aa='th'
       ss=re.compile(r'\b%s\b'%aa)
       z=re.findall(ss, 'alal ,b6 th al 56\nfPython\t4Ac\65')
       >>> ['th']
       
     9)汉字代码：[\u4e00-\u9fa5]          2019-4-23 16:16:39
       
     10)注释：(?#)  ’(?#’ 与‘)’ 之间的内容将被忽略。如 (?#abcdefg)
       
     11)重复匹配，*表示匹配前面的规则0或多次，+表示匹配前面的规则1或多次，，2019-4-23 17:08:41
       s='aaa bbb111 cc22cc 33dd '
       zz=re.findall( r'\b[a-z]+\d*\b' , s ) # 必须至少 1 个字母开头，以连续数字结尾或没有数字，，(为何不能把*放前面？因为*表示匹配前面的规则)
       >>> ['aaa', 'bbb111'] 
       
     12)'''注意！注意！注意！注意！注意！：'''  2019-4-23 17:52:13
       s='123 10e3 20e4e4 30ee5'
       zz=re.findall( r'\d+\w+\b' , s ) # 以多个数字或字母结尾，且前面是数字
       >>> ['123', '10e3', '20e4e4', '30ee5']
       ||
       zz=re.findall( r'\d+\w\b' , s ) # 以一个数字或字母结尾，且倒数第二个是数字，所以只有123
       >>> ['123']
       
       s='1 22 333 ert4444 55555 666666'     2019-4-24 08:57:07
       zz=re.findall( r'\b\w\b' , s )  #为啥只有1？他的意思是不是以一个\w开头，并以该\w结尾，所以只能是一个？？
       >>> ['1']
       s='&555撒地方55$ 666666'
       zz=re.findall( r'\b\W+.*?\W+\b' , s )
       >>> ['$ ']  # 这里输出的为啥不是&555撒地方55$？问得好！因为这里要找的是\W，开头和结尾不再以空格来判断，而是以字母数字汉字，这里的字母数字汉字就相当于\w里的空格！！！
       ||
       #下面我们把&555撒地方55$头尾都加数字，现在的输出就是我们期盼的了，
       s='2&555撒地方55$2 666666'
       zz=re.findall( r'\b\W+.*?\W+\b' , s )
       >>> ['&555撒地方55$']
       ????? # 前面的DBPNE也属于字母为啥没检测到？？ 2019-4-24 09:54:29
       s='K71U8DBPNE-eyJsaWNlbnNlSWQiOiJLNzFVOERCUE5FIiwibGljZW5zZWVOYW1lIjoibGFu'
       zz=re.findall( r'\b[A-Za-z-_]{10,}' , s )
       >>> ['-eyJsaWNlbnNlSWQiOiJLNzFVOERCUE']  
       # 因为我们需要查找10个以上字母开头的串，既然是开头，那么就需要找到空格等空字符，而'-'也可以作为空字符(虽然我们查找的内容包含了'-'，但它作为空字符标识这个身份并没有改变)
 
       data='2.35 6  56adf6.f336.65ff '
       oneday=re.findall(r"\d+\.?\d*",data)  # \.? 表示有一个点，或者没有(常用语找小数点2019-4-24 14:42:20)
       >>> ['2.35', '6', '56', '6.', '336.65']
       '''注意！注意！注意！注意！注意！'''
       
       
       
       
     13)精确匹配  2019-4-23 18:02:21
       # {m,n}表示匹配最少 m 次，最多 n 次(n>m)，{m}表示只匹配m次，{m,}表示最少匹配m次，{,n}表示最多匹配n次，
       s='1 22 333 4444 55555 666666'
       zz=re.findall( r'\b\d{3,}\b' , s ) # 匹配出三位及以上的数字
       >>> ['333', '4444', '55555', '666666']
       
     14)最小匹配   ‘*?’ ‘+?’ ‘??’   2019-4-23 18:21:14
       s='/* part 1 */ code /* part 2 */'   # 这是C语言的注释，/**/里面的内容表示注释的内容，
       zz=re.findall( r'/\*.*\*/' , s ) # 匹配以/*开头以*/结尾的字符串，默认是尽可能多地匹配字符，所以结果是把两部分的注释连在一起了(在正则表达式里*有别的含义，这里用\*转义一下表示*本身)
       >>> ['/* part 1 */ code /* part 2 */']
       
       zz=re.findall( r'/\*.*?\*/' , s ) # *?表示尽可能少地匹配，
       >>> ['/* part 1 */', '/* part 2 */'] # 尽可能少地匹配，使得两部分注释分开了，
       
     15)前向界定与后向界定   2019-4-23 19:31:29
       '(?<=...)' 前向界定: ...代表你希望匹配的字符串前面应该出现的字符串。 #前向界定括号中必须是常值，不能是正则表达式
       '(?=...)'  后向界定：同理
       s='/* part 1 */ code /* part 2 */'    
       zz=re.findall( r'(?<=/\*).*?(?=\*/)' , s )
       >>> [' part 1 ', ' part 2 ']   # 相比于14)，我们只匹配注释部分的内容而不要注释符号，
       
     16)前向非界定yu后向非界定，和15)相反，2019-4-23 19:54:11
       '(?<!...)' 前向非界定：...代表你希望匹配的字符串前面不要出现的字符串。
       '(?!...)'后向非界定：同理
 
     17)组的基本知识:  2019-4-24 10:05:47
       s='aaa111aaa , bbb222 , 333ccc'
       zz=re.findall( r'[a-z]+(\d+)[a-z]+' , s )
       >>> ['111']   # 返回的是111而不是aaa111aaa，因为我们把\d括起来了，(\d+)就是一个组，
       
       ?P<name> 给一个组命名
       ?P=name 调用已匹配的命名过的组
       s='aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
       zz=re.findall( r'([a-z]+)\d+([a-z]+)' , s )    
       >>> [('aaa', 'aaa'), ('fff', 'ggg')]  # 找到包夹数字的字母，
       
       zz=re.findall( r'(?P<g1>[a-z]+)\d+(?P=g1)' , s )  # 前面给字母串命名g1,后面查找名为g1的字母串，2019-4-24 10:22:59
       >>> ['aaa']   找出被中间夹有数字的前后同样的字母('''注意是前后同样的字母''')
       
       zz=re.findall( r'([a-z]+)\d+\1' , s )   # 意义同上，只不过这里用\1表示前面的命名组(每个命名组都有一个序号)
       >>> ['aaa']
       
       s='111aaa222aaa111 , 333bbb444bb33'
       zz=re.findall( r'(\d+)([a-z]+)(\d+)(\2)(\1)' , s ) # 找出完全对称的 数字－字母－数字－字母－数字 中的数字和字母
       >>> [('111', 'aaa', '222', 'aaa', '111')]
       
       ||
       ‘(?( id/name )yes-pattern|no-pattern)’ 判断指定组是否已匹配，执行相应的规则 # 条件匹配没太弄明白 2019-4-24 10:51:59
       ||
       
     18)compile()规则预编译     2019-4-24 11:04:04  # 作用：可以加速
       s='111,222,aaa,bbb,ccc333,444ddd'
       rule=r’/b/d+/b’
       compiled_rule=re.compile(rule)
       compiled_rule.findall(s)
       >>> ['111', '222']
       预编译作用：#直接使用 findall ( rule , target ) 的方式来匹配字符串，一次两次没什么，如果是多次使用的话，
       #由于正则引擎每次都要把规则解释一遍，而规则的解释又是相当费时间的，所以这样的效率就很低了。如果要多次使
       #用同一规则来进行匹配的话，可以使用 re.compile 函数来将规则预编译，使用编译过返回的 Regular Expression Object 或叫做 Pattern 对象来进行查找。
       
     19)match 与 search   2019-4-24 11:43:00  两者区别：match 从字符串的开头开始匹配，如果开头位置没有匹配成功，就算失败；search 会继续向后寻找是否有匹配的字符串
       s= 'Tom:9527 , Sharry:0003'
       m=re.match( r'(?P<name>\w+):(?P<num>\d+)' , s ) # 注意有(?P<name>\w+)和(?P<num>\d+)两个组，(?P<name>\w+)是组1，(?P<num>\d+)是组2，组0是整体
       print(m.group())
       >>> Tom:9527
       
       print(m.groups())
       >>> ('Tom', '9527')
       
       print(m.group(0))
       >>> Tom:9527
       
       print(m.group(1))
       >>> Tom
       
       print(m.group(2))
       >>> 9527
       
       print(m.group('name'))
       >>> Tom
       
       print(m.groupdict())
       >>>{'name': 'Tom','num': '9527'}
       
     20)finditer( rule , target [,flag] )  返回一个迭代器，参数同 findall    
       s='111 222 333 444'
       for i in re.finditer(r'\d+' , s ):
           print (i.group(),i.span()) 
       >>> 111 (0, 3)
           222 (4, 7)
           333 (8, 11)
           444 (12, 15)
```







## request库 - 爬虫、网络相关



```python title='发送 GET 请求'
import requests

response = requests.get('https://api.example.com/data')
print(response.status_code)
print(response.json())
```

```python title='发送 POST 请求'
import requests

data = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=data)
print(response.status_code)
print(response.json())
```

```python
# 添加请求头
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)

# 处理查询参数
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://api.example.com/data', params=params)
```

