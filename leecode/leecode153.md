# 153. 寻找旋转排序数组中的最小值
地址:https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/

# 题目描述
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
- 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
- 若旋转 4 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。


示例 1：
```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

示例 2：
```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```

示例 3：
```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```

提示：

- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- nums 中的所有整数 互不相同
- nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转


# 我的解法
```python
'''
我的思路：
二分法:
根据题意，可以理解到一下几点：
1. 没有相同数字
2. 旋转之后，还是局部有序的，也就是在某部分都是从小到大的，不存在无序状态

算法逻辑：
1. 先设置起点位置low和终点位置high，数列的长度。
2. 进行判断：
   1. 如果起始位置的值nums[low]小于等于nums[high]，说明是全局有序，第一个数就是最小的，直接返回.
   2. 如果其实位置nums[low]大与nums[high], 则求一下mid数值，表示low和high的中点位置；
     如果nums[mid] >= nums[low],说明右边的数字较小，所以low = mid + 1;
     如果nums[mid] < nums[low], 说明小的数字在low和mid之间，所以，high = mid, low = low + 1.


'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        low, high = 0, len(nums) - 1
        while(low<= high):
            if nums[low] <= nums[high]:
                return nums[low]
            else:
                mid = (low + high) >> 1
                if nums[mid] >= nums[low]:
                    low = mid + 1
                else:
                    high = mid
                    low = low + 1



```


# 参考解法
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]


```


```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        
        l=0
        r=n-1
        while(l<r):
            m=(l+r)//2
            if(nums[m]>nums[r]):
                l=m+1
            elif (nums[m]<nums[r]):
                r=m 
            else:
                r-=1
        return nums[l]

## 这个效率高一点

```
