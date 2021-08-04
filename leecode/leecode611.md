# 611. 有效三角形的个数
地址: https://leetcode-cn.com/problems/valid-triangle-number/


# 题目描述
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例1:
```
输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

```


# 我的解法

超出时间限制

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens <= 2:
            return 0
        res = 0
        for i in range(lens):
            for j in range(i+1,lens):
                for k in range(j+1,lens):
                    if nums[i] == 0 or nums[j] == 0 or nums[k] == 0:
                        continue
                    if nums[i]+nums[j] > nums[k] and abs(nums[i]-nums[j]) < nums[k]:
                        res += 1
        return res


```

# 参考解法

## 思路
暴力法的时间复杂度为 $O(N ^ 3)$， 其中 NN 最大为 1000。一般来说， $O(N ^ 3)$的算法在数据量 <= 500 是可以 AC 的。1000 的数量级则需要考虑 $O(N ^ 2)$或者更好的解法。

**降低时间复杂度的方法主要有： 空间换时间 和 排序换时间（我们一般都是使用基于比较的排序方法）。而排序换时间仅仅在总体复杂度大于 O(NlogN)才适用。**



```python

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens <= 2:
            return 0
        res = 0
        nums.sort()
        for i in range(lens-2):
            if nums[i] == 0:
                continue
            k = i + 2
    # 通过进一步观察，发现 k 没有必要每次都从 j + 1 开始。而是从上次找到的 k 值开始就行。
    #原因很简单， 当 nums[i] + nums[j] > nums[k] 时，我们想要找到下一个满足 nums[i] + nums[j] > nums[k] 的 新的 k 值，
    #由于进行了排序，因此这个 k 肯定比之前的大（单调递增性），因此上一个 k 值之前的数都是无效的，可以跳过。
            for j in range(i+1,lens-1):
                while k < lens and nums[i] + nums[j] > nums[k]:
                    k += 1
                res += k - j - 1
        return res

```


# 最优解法
```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        RE=0
        for k in range(len(nums)): # 外面一层遍历
            i,j=0,k-1 # 里面双指针的办法，一个指头，一个指尾
            while i<j: # 当i 小于j 的时候
                if nums[i]+nums[j]>nums[k]: # 如果i + j > k 则说明，i取到 j-i 之间都满足，此时 j可以变小 
                    RE+=j-i
                    j-=1
                else: # 否则，i + 1
                    i+=1
        return RE

```


