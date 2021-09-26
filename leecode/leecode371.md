# 371. 两整数之和
地址:https://leetcode-cn.com/problems/sum-of-two-integers/


# 题目描述
给你两个整数 a 和 b ，不使用 运算符 + 和 - ​​​​​​​，计算并返回两整数之和。

示例1
```
输入：a = 1, b = 2
输出：3

```



示例2
```
输入：a = 2, b = 3
输出：5

```


# 我的解法
```python

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return a+b


```



# 参考解法

```python

MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a



```
