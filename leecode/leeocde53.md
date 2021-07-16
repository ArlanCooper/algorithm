# 剑指 Offer 53 - I. 在排序数组中查找数字 I

地址:https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/


# 题目描述
统计一个数字在排序数组中出现的次数。


示例1
```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

```


示例2
```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```


# 我的解法
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)
```


# 参考解法
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                left = right = mid
                while nums[left]==nums[mid] and left>=0:
                    left -= 1
                while right <=n-1 and nums[right] == nums[mid]:
                    right += 1
                return right-left-1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return 0
```
