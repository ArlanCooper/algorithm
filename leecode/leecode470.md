# 470. 用 Rand7() 实现 Rand10()
地址:https://leetcode-cn.com/problems/implement-rand10-using-rand7/

# 题目描述
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

示例 1:
```
输入: 1
输出: [7]

```

示例 2:
```
输入: 2
输出: [8,4]

```

示例 3:
```
输入: 3
输出: [8,1,10]

```


# 我的解法
## 思路
建立多重映射
```python
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        f = rand7()
        while True:
            if f not in [6,7]:
                break
            f = rand7()
        if f == 1:
            while True:
                tmp = rand7()
                if tmp in [1,2,3]:
                    return 1
                elif tmp in [4,5,6]:
                    return 2
                else:
                    tmp = rand7()
        if f == 2:
            while True:
                tmp = rand7()
                if tmp in [1,2,3]:
                    return 3
                elif tmp in [4,5,6]:
                    return 4
                else:
                    tmp = rand7()
        if f == 3:
            while True:
                tmp = rand7()
                if tmp in [1,2,3]:
                    return 5
                elif tmp in [4,5,6]:
                    return 6
                else:
                    tmp = rand7()
        if f == 4:
            while True:
                tmp = rand7()
                if tmp in [1,2,3]:
                    return 7
                elif tmp in [4,5,6]:
                    return 8
                else:
                    tmp = rand7()
        if f == 5:
            while True:
                tmp = rand7()
                if tmp in [1,2,3]:
                    return 9
                elif tmp in [4,5,6]:
                    return 10
                else:
                    tmp = rand7()


```


# 参考解法1

取巧的方法
```python

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return random.randint(1, 10)




```

# 参考解法2

## 思路
通过两个rand7()相乘，得到49个数，每个数的生成概率是1/49；则取前40个数，分别代表1-10，则可以得到均匀分布。


```python
class Solution:
    def rand10(self) -> int:
        while True:
            row = rand7()
            col = rand7()
            idx = (row - 1) * 7 + col
            if idx <= 40:
                return 1 + (idx - 1) % 10


```