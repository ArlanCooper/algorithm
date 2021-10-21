# 66. 加一
地址:https://leetcode-cn.com/problems/plus-one/


# 题目描述
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。


示例1
```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

```


示例2
```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

```


示例3
```
输入：digits = [0]
输出：[1]

```


# 我的解法
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        flag = 0
        for i,j in enumerate(digits[::-1]):
            if i == 0:
                digits[n -1] = j + 1
            else:
                digits[n -1 - i] = j + flag
            if digits[n -1 - i] == 10:
                if i < n-1:
                    digits[n -1 - i] = 0
                    flag = 1
                else:
                    digits = [1,0]+digits[1:]
                    print(digits)
            else:
                break
        return digits

```

# 参考解法

## 思路
对数组 digits 进行一次逆序遍历，找出第一个不为 9 的元素，将其加一并将后续所有元素置零即可。
如果 digits 中所有的元素均为 9，我们需要返回一个新的数组。


```python

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n

```
