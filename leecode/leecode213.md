# 213. 打家劫舍 II
地址: https://leetcode-cn.com/problems/house-robber-ii/


# 题目描述
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

示例 2：
```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

示例 3：
```
输入：nums = [0]
输出：0
```

# 我的解法
```python
'''
解题思路：
1.动态规划求取最大值，并记录每个最大值的路径；
2. 根据题意，不能将第一个数和最后一个数同时放到序列里面，所以，需要最后判断是否第一个数和最后一个数同时放到结果里面
3. 因为可以放第一个数，也可以只放最后一个数，所以需要对序列进行翻转之后，再求取最大值。

问题：
占用内存过大

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            ans = [0] * (len(nums)+1)
            if len(nums) == 1:
                return nums[0]
            ans[1] = nums[0]
            paths = []
            paths.append({0})
            for i in range(1,len(nums)):
                if nums[i] + ans[i-1] >= ans[i]:
                    ans[i+1] = nums[i] + ans[i-1]
                    if i == 1:
                        paths.append({i})
                    else:
                        paths.append(paths[i-2]|{i})
                else:
                    ans[i+1] = ans[i]
                    paths.append(paths[i-1])
            if 0 in paths[-1] and len(nums)-1 in paths[-1]:
                return ans[-2]
            else:

                return ans[-1]
        f1 = get_max(nums)
        f2 = get_max(nums[::-1])
        return max(f1,f2)

```

优化内存使用之后的算法:
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            lens = len(nums)
            ans = [0] * (lens+1)
            if lens == 1:
                return nums[0]
            ans[1] = nums[0]
            for i in range(1,lens):
                ans[i+1] = max(nums[i] + ans[i-1],ans[i])
            index = lens
            # 生成最大序列的路径
            path = []
            while index>= 1:
                if ans[index] > ans[index-1]:
                    path.append(index-1)
                    tmp = ans[index] - nums[index-1]
                    index -= 1
                    while ans[index] > tmp:
                        index -= 1
                else:
                    index -= 1
            if 0 in path and lens-1 in path:
                return ans[-2]
            else:
                return ans[-1]
        f1 = get_max(nums)
        f2 = get_max(nums[::-1])
        return max(f1,f2)

```

# 参考解法
```python
'''
在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1;
在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是 p2
综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2)

'''

class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]

```
