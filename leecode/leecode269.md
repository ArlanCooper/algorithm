# 260. 只出现一次的数字 III
地址:https://leetcode-cn.com/problems/single-number-iii/

# 题目描述
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

示例1
```
输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
```

示例2
```
输入：nums = [-1,0]
输出：[-1,0]
```

示例1
```
输入：nums = [0,1]
输出：[1,0]
```


# 我的解法
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dics = {}
        res = []
        for i in nums:
            if i in dics:
                dics[i] += 1
            else:
                dics[i] = 1
        for k in dics:
            if dics[k] == 1:
                res.append(k)
        return res

```

# 参考解法

## 思路
在理解如何使用位运算解决本题前，读者需要首先掌握「136. 只出现一次的数字」中的位运算做法。

假设数组nums 中只出现一次的元素分别是x1和x2。如果把 \textit{nums}nums 中的所有元素全部异或起来，得到结果 x，那么一定有：
x=x1⊕x2
其中⊕表示异或运算。这是因为 \textit{nums}nums 中出现两次的元素都会因为异或运算的性质 a⊕b⊕b=a 抵消掉，那么最终的结果就只剩下x1和x2的异或和。

```python

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for num in nums:
            xorsum ^= num
        
        lsb = xorsum & (-xorsum)
        type1 = type2 = 0
        for num in nums:
            if num & lsb:
                type1 ^= num
            else:
                type2 ^= num
        
        return [type1, type2]

```


# 最优解法
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)

```