# 704. 二分查找
地址:https://leetcode-cn.com/problems/binary-search/


# 题目描述
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例1
```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

```

示例2
```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

```

# 我的解法
```python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1 
        

```

# 参考解法
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
        while a<=b:
            i=a+(b-a)//2
            if nums[i]==target:
                return i
            if nums[i]<target:
                a=i+1
            if nums[i]>target:
                b=i-1
        return -1


```

