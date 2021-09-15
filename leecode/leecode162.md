# 162. 寻找峰值
地址：https://leetcode-cn.com/problems/find-peak-element/

# 题目讲解
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

示例1
```
输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。

```


示例1
```
输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

```


# 我的解法
## 最差情况下需要O(n)的时间复杂度
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        if n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[n-1] > nums[n-2]:
            return n-1
        return 0



```


# 参考解法

## 思路
爬坡法 + 二分查找法

这道题，最最最重要的是条件，条件，条件，两边都是负无穷，数组当中可能有很多波峰，也可能只有一个，如果尝试画图，就跟股票信息一样，没有规律，如果根据中点値判断我们的二分方向该往何处取， 这道题还有只是返回一个波峰。你这样想，中点所在地方，可能是某座山的山峰，山的下坡处，山的上坡处，如果是山峰，最后会二分终止也会找到，关键是我们的二分方向，并不知道山峰在我们左边还是右边，送你两个字你就明白了，爬山（没错，就是带你去爬山），如果你往下坡方向走，也许可能遇到新的山峰，但是也许是一个一直下降的坡，最后到边界。但是如果你往上坡方向走，就算最后一直上的边界，由于最边界是负无穷，所以就一定能找到山峰，总的一句话，往递增的方向上，二分，一定能找到，往递减的方向只是可能找到，也许没有。


```python

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
        return ans


```
