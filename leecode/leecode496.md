# 496. 下一个更大元素 I
地址: https://leetcode-cn.com/problems/next-greater-element-i/


# 题目描述
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。


示例1
```
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

```

示例2
```
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

```


# 我的解法
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        inds = {j:i for i,j in enumerate(nums2)}
        for i in nums1:
            ind = inds[i]
            for j in nums2[ind+1:]:
                if j > i:
                    res.append(j)
                    break
            else:
                res.append(-1)
        return res


```


# 参考解法
```python

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]

```


# 最优解法
```python

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        i = 0
        mp = {}
        while i<len(nums2):
            x = nums2[i]
            if not stack or x<stack[-1]:
                stack.append(x)
                i += 1
            else:
                mp[stack.pop()] = x
        while stack:
            mp[stack.pop()] = -1
        
        ans = []
        for x in nums1:
            ans.append(mp[x])
        return ans


```
