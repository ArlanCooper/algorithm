# 326. 3的幂
地址:https://leetcode-cn.com/problems/power-of-three/


# 题目描述
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 $n == 3^x$

示例1
```
输入：n = 27
输出：true

```


示例2
```
输入：n = 0
输出：false

```


示例3
```
输入：n = 9
输出：true

```


示例4
```
输入：n = 45
输出：false

```


# 我的解法
```python

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        tmp = round(math.log(n,3))
        if 3**tmp == n:
            return True
        else:
            return False

```


# 参考解法
```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1 and n != 0:
            a = n % 3
            n = n / 3
            if a != 0:
                return False

        return True


```
