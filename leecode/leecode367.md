# 367. 有效的完全平方数
地址:https://leetcode-cn.com/problems/valid-perfect-square/


# 题目描述
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。


示例1
```
输入：num = 16
输出：true

```


示例2
```
输入：num = 14
输出：false


```


# 我的解法
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        top = num // 2
        if num < 4:
            if num != 1:
                return False
            else:
                return True
        l,r = 1,top
        while l <= r:
            mid = (l+r)>>1
            if mid*mid == num:
                return True
            if mid*mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False


```



# 参考解法
## 思路
牛顿迭代法
```python

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num

```
