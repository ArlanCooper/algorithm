# 1588. 所有奇数长度子数组的和
地址:https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/

# 题目描述
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。

示例1
```
输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

```

示例2
```
输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。

```

示例3
```
输入：arr = [10,11,12]
输出：66

```


# 我的解法
```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            res += arr[i]
            for j in range(i):
                if (i-j) % 2 == 0:
                    res += sum(arr[j:i+1])
        return res


```

# 参考解法
## 思路，数学思路
对于一个数字，它所在的数组，可以在它前面再选择 0, 1, 2, ... 个数字，一共有 left = i + 1 个选择；

可以在它后面再选择 0, 1, 2, ... 个数字，一共有 right = n - i 个选择。

如果在前面选择了偶数个数字，那么在后面，也必须选择偶数个数字，这样加上它自身，才构成奇数长度的数组；

如果在前面选择了奇数个数字，那么在后面，也必须选择奇数个数字，这样加上它自身，才构成奇数长度的数组；

数字前面共有 left 个选择，其中偶数个数字的选择方案有 left_even = (left + 1) / 2 个，奇数个数字的选择方案有 left_odd = left / 2 个；

数字后面共有 right 个选择，其中偶数个数字的选择方案有 right_even = (right + 1) / 2 个，奇数个数字的选择方案有 right_odd = right / 2 个；

所以，每个数字一共在 left_even * right_even + left_odd * right_odd 个奇数长度的数组中出现过。
```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=0
        length = len(arr)
        for i in range(length):
            result += (i//2+1)*((length-i-1)//2+1)*arr[i]
            result += ((i+1)//2)*((length-i)//2)*arr[i]
        return result


```