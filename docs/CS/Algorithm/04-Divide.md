# divide and conquer

- 分治法
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。
- 分治法的核心思想是将一个问题分解为若干个子问题，然后递归地解决这些子问题，最后将这些子问题的解合并起来得到原问题的解。


- 二分算法

注意二分板子的打法，注意+1问题

```c
int l = 0 , r = Count -1 , mid = (l+r) / 2;
while(l < r){ 
    mid = (l+r) / 2;
    if(value <= a[mid])     r = mid;
    else                    l = mid + 1;
}
```


## 经典问题 - 汉诺塔问题

问题描述





## 经典问题 - 树递归

!!! note "问题"



求正整数 n 的分割数，最大部分为 m，即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列。例如，使用 4 作为最大数对 6 进行分割的方式有 9 种：

1. 6 = 2 + 4  
2. 6 = 1 + 1 + 4  
3. 6 = 3 + 3  
4. 6 = 1 + 2 + 3  
5. 6 = 1 + 1 + 1 + 3  
6. 6 = 2 + 2 + 2  
7. 6 = 1 + 1 + 2 + 2  
8. 6 = 1 + 1 + 1 + 1 + 2  
9. 6 = 1 + 1 + 1 + 1 + 1 + 1  

我们将定义一个名为 `count_partitions(n, m)` 的函数

**转化方式**

我们可以递归地将使用最大数为 m 的整数分割 n 的问题转化为两个较简单的问题：  
① 使用最大数为 m 的整数分割更小的数字 n-m，  
② 使用最大数为 m-1 的整数分割 n。

**边界条件**

- 整数 0 只有一种分割方式
- 负整数 n 无法分割，即 0 种方式
- 任何大于 0 的正整数 n 使用 0 或更小的部分进行分割的方式数量为 0

```python
def count_partitions(n, m):
    """
    计算使用最大数 m 的整数分割 n 的方式的数量

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
```


!!! note "练习题目"

    Given a positive integer `total`, a set of dollar bills makes change for `total` if the sum of the values of the dollar bills is `total`. Here we will use standard US dollar bill values: 1, 5, 10, 20, 50, and 100. For example, the following sets make change for 15:

    - 15 1-dollar bills
    - 10 1-dollar, 1 5-dollar bills
    - 5 1-dollar, 2 5-dollar bills
    - 5 1-dollar, 1 10-dollar bills
    - 3 5-dollar bills
    - 1 5-dollar, 1 10-dollar bills

    Thus, there are 6 ways to make change for 15. Write a recursive function `count_dollars` that takes a positive integer `total` and returns the number of ways to make change for `total` using 1, 5, 10, 20, 50, and 100 dollar bills.

    Use `next_smaller_dollar` in your solution: `next_smaller_dollar` will return the next smaller dollar bill value from the input (e.g. `next_smaller_dollar(5)` is 1). The function will return `None` if the next dollar bill value does not exist.

    ```python title="count_dollars"
    def next_smaller_dollar(bill) -> int:
        """Returns the next smaller bill in order."""
        if bill == 100:
            return 50
        if bill == 50:
            return 20
        if bill == 20:
            return 10
        elif bill == 10:
            return 5
        elif bill == 5:
            return 1
        
    def count_with_top(total,top) -> int:
        """ Return the number of partition of charge with a maximum of top
        """
        if total == 0:
            return 1
        elif total < 0:
            return 0
        else:
            return count_with_top(total-top,top) + (count_with_top(total,next_smaller_dollar(top)) if top != 1 else 0)
        

    def count_dollars(total) -> int:
        """Return the number of ways to make change.

        >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
        6
        >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
        4
        >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
        10
        >>> count_dollars(45)  # How many ways to make change for 45 dollars?
        44
        >>> count_dollars(100) # How many ways to make change for 100 dollars?
        344
        >>> count_dollars(200) # How many ways to make change for 200 dollars?
        3274
        >>> from construct_check import check
        >>> # ban iteration
        >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
        True
        """
        return count_with_top(total,100)
    ```