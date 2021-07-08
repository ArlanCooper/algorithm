# 930. 和相同的二元子数组
地址: https://leetcode-cn.com/problems/binary-subarrays-with-sum/


# 题目描述
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。

示例1:
```
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1]
[1,0,1,0]
    [1,0,1]
  [0,1,0,1]

```

示例2:
```
输入：nums = [0,0,0,0,0], goal = 0
输出：15
```

# 我的解法（参看）
## 思路
滑动窗口
注意到对于方法一中每一个 jj，满足 ${sum}[j]-{sum}[i]={goal}$ 的 i总是落在一个连续的区间中，i 值取区间中每一个数都满足条件。并且随着 j右移，其对应的区间的左右端点也将右移，这样我们即可使用滑动窗口解决本题。
具体地，我们令滑动窗口右边界为right，使用两个左边界 ${left}_1$和 ${left}_2$表示左区间 [${left}_1,{left}_2$]，此时有 ${left}_2-{left}_1$个区间满足条件。
在实际代码中，我们需要注意 ${left}_1 \leq {left}_2 \leq {right} + 1$，因此需要在代码中限制 ${left}_1$和 ${left}_2$不超出范围。

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        lens = len(nums)
        left1,left2,right = 0,0,0
        sum1,sum2 = 0,0
        res = 0
        while right < lens:
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            res += left2 - left1
            right += 1

        return res


```
## 复杂度分析
- 时间复杂度：O(n)，其中 n 为给定数组的长度。我们至多只需要遍历一次该数组。
- 空间复杂度：O(1)。我们只需要常数的空间保存若干变量。


# 最优解法
```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        one = [-1]
        for i, x in enumerate(nums): #记录1所在位置的索引
            if x == 1:
                one.append(i)
        one.append(len(nums)) # 整个序列的总长度
        n = len(one) # 1的个数 + 1 + 1
        ans = 0
        if goal == 0: # 如果目标和为0
            for i in range(1, n):
                diff = one[i] - one[i-1] - 1 # 两个相邻1之间的0的个数
                ans += diff*(diff+1) //2 #计算组合的可能性求和
        else:
            for i in range(goal, n-1): 
                # 从目标值开始计数，因为低于目标值不可能成立，然后普遍历所有的可能性进行求和
                l = one[i-(goal-1)]-one[i-goal] # 左侧两个1之间0的个数
                r = one[i+1] - one[i] # 右侧两个1之间0的个数
                ans += l * r
        return ans 

```