# 581. 最短无序连续子数组
地址: https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/

# 题目描述
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。


示例1
```
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

```

示例1
```
输入：nums = [1,2,3,4]
输出：0

```


示例1
```
输入：nums = [1]
输出：0

```


# 我的解法
思路:
将整个序列排序后的索引列表抽取出来，使用双指针的方法，只要左右两边的数值与对应的索引不一致，就返回相应的值，然后求差，即可得出最小的长度。


``` python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_nums = [(j,i) for i,j in enumerate(nums)] 
        new_nums.sort() #进行排序
        inds = [j for i,j in new_nums]
        lens = len(nums)
        l,r = 0, lens-1
        while l < lens and l == inds[l]:
            l += 1
        while r > l and r == inds[r]:
            r -= 1
        return r - l + 1
```


# 最优解法
思路：

我们需要正序、倒序遍历两次数组
正序遍历时，不断更新right指针，获取小于当前最大值的那个下标
倒序遍历时，不断更新left指针，获取大于当前最小值的那个下标即可。

```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums) # 数组长度
        if n == 1: #长度为1，直接返回
            return 0
        left = n-1 #取最后数字的索引，先假定左边都是大于最后一个元素的数字
        min_nums = nums[-1] #先假定最小的数字为最后一个数字
        for j in range(n-1, -1, -1): #倒序查找最小的数字，并找到最左边的，比右边大的数字
            if nums[j] <= min_nums:
                min_nums = nums[j]
            else: #
                left = j
        right = 0
        max_nums = nums[0]
        for i in range(n): # 同理，找到最右边比左边大的数字的索引地址
            if nums[i] >= max_nums:
                max_nums = nums[i]
            else:
                right = i 
        return max(right - left + 1, 0)
```

```python
class Solution:
    def findUnsortedSubarray(self, nums):
        left, right, min_num, max_num = 0, 0, float("inf"), float("-inf")

        for i, j in enumerate(nums):
            if j < max_num:
                right = i
            max_num = max(max_num, j)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > min_num:
                left = i
            min_num = min(min_num, nums[i])
        return 0 if left == right else right - left + 1

```