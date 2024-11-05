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

