# SQL
SQL (Structured Query Language:结构化查询语言) 是用于管理关系数据库管理系统（RDBMS）

!!! note "What is RDBMS"
    即关系数据库管理系统(Relational Database Management System)的特点：
    1. 数据以表格的形式出现
    2. 每行为各种记录名称
    3. 每列为记录名称所对应的数据域
    4. 许多的行和列组成一张表单
    5. 若干的表单组成database
## 语法
[菜鸟教程](https://www.runoob.com/sql/sql-tutorial.html)
### 增

**INSERT**

id字段自动更新，不需要插入
```sql
INSERT INTO table_name
VALUES (value1,value2,value3,...);

INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

INSERT INTO Websites (name, url, country)
VALUES ('stackoverflow', 'http://stackoverflow.com/', 'IND');
```
### 删

同样要注意 WHERE 子句，否则会删除所有记录

```sql
DELETE FROM table_name
WHERE condition;
```

### 改

!!! note "请注意 SQL UPDATE 语句中的 WHERE 子句！"
    WHERE 子句规定哪条记录或者哪些记录需要更新。如果您省略了 WHERE 子句，所有的记录都将被更新！


```sql
UPDATE Websites 
SET alexa='5000', country='USA' 
WHERE name='菜鸟教程';
```
 
### 查
SELECT 语句用于从数据库中选取数据。

结果被存储在一个结果表中，称为结果集。
if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)
if(ascii(substr((select(flag)from(flag)),1,1))=ascii('f'),1,2)

```sql
SELECT column1, column2, ... FROM table_name;
```
**column1, column2, ...** ：要选择的字段名称，可以为多个字段。如果不指定字段名称，则会选择所有字段。
**table_name** ：要查询的表名称。

**SELECT DISITINCT 选出不同的值**
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

**WHERE 子句 | 条件查询**

|运算符|描述|
|---|---|
|`=`|	等于|
|`<>`|	不等于。注释：在 SQL 的一些版本中，该操作符可被写成 `!=`|
|`>`|	大于|
|`<`|	小于|
|`>=`|	大于等于|
|`<=`|小于等于|
|`BETWEEN`|	在某个范围内|
|`LIKE`|	搜索某种模式|
|`IN`|	指定针对某个列的多个可能值|

**AND OR 条件**

```sql
SELECT * FROM Websites WHERE country='USA' OR country='CN';

SELECT * FROM Websites WHERE country='CN' AND alexa > 50;
```


**ORDER BY**

```sql
SELECT * FROM Websites ORDER BY alexa;

SELECT * FROM Websites
ORDER BY alexa DESC; //降序排序

SELECT * FROM Websites
ORDER BY country,alexa;//多列
```
## MySQL

> MySQL 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最好的 RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。


MySQL 为关系型数据库(Relational Database Management System), 这种所谓的"关系型"可以理解为"表格"的概念, 一个关系型数据库由一个或数个表格组成
![](https://philfan-pic.oss-cn-beijing.aliyuncs.com/img/20240702184602.png)
- 表头(header): 每一列的名称;
- 列(col): 具有相同数据类型的数据的集合;
- 行(row): 每一行用来描述某条记录的具体信息;
- 值(value): 行的具体信息, 每个值必须与该列的数据类型相同;
- **键(key): 键的值在当前列中具有唯一性。**
if(ascii(substr((select(flag)from(flag)),{position},5))=ascii('{'),1,2)

flag{af266f5e-79e1-41ee-96bd-784b3417a30d}