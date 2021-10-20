# 453. 最小操作次数使数组元素相等
地址:https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/

# 题目描述
给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

示例1
```
输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

```


示例2
```
输入：nums = [1,1,1]
输出：0

```


# 我的解法
简单的数学问题
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = min(nums)
        return sum(nums) - mi * len(nums)


```

# 参考解法
解法一致
```python
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums) if len(nums)!=0 else 0


```
