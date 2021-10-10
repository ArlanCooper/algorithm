# 441. 排列硬币
地址: https://leetcode-cn.com/problems/arranging-coins/

# 题目描述
你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

示例1
![img](../pic/441_1.jpg)
```
输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2 。

```


示例2
![img](../pic/441_2.jpg)
```
输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3 。

```


# 我的解法
## 思路

根据公式，计算2S开根号之后，如果2S大于等于开根号之后的整数，则返回该整数即可，否则，返回该整数减一即为最后的答案。

```python

class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = int((2*n)**(1/2))
        if 2*n >= res*(res+1):
            return res
        else:
            return res-1
        


```

# 参考解法
```python
## 二分法计算
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left

```


```python

## 直接求根，下取整即可。
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)



```