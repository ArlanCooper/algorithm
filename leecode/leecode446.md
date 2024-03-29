# 446. 等差数列划分 II - 子序列
https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/

# 题目描述
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数。

示例 1：
```
输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

```

示例2
```
输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。

```

# 我的解法
没写出来


# 参考解法
## 思路
核心思想：从 413. 等差数列划分 的「状态转移方程」迁移过来：如果一个等差数列的后面再加上一个整数，可以得到一个长度更长的等差数列，那么这个长度更长的等差数列对结果的贡献，就可以从之前的等差数列对结果的贡献中得到。
### 状态定义
关键：状态不够用了，需要「升维」，在原来定义的状态的基础上加上「公差」。

- 「以 nums[i] 结尾」这件事情肯定要定义在状态中；
- 题目不要求连续，因此在求每一个状态的时候，就需要 考虑它之前的所有的元素；
- 能不能接上去，看「公差」，因此记录状态的时候，除了要求以 nums[i] 结尾以外，还要记录「公差」，两个整数的差可以有很多很多，因此需要用哈希表记录下来。
到这里为止，每一个 nums[i] 的状态，其实是一张哈希表（键值对），「键」 是 nums[i] 与它前面的每一个元素的「差」，那「值」是什么呢？「值」是以 nums[i] 结尾组成的、公差为某个值的（元素之间可以不连续的）等差数列的长度 - 1，也可以认为是「nums[i] 之前的元素的个数」。
为什么值是「之前的元素的个数」？
- 计算「差」，至少需要两个元素；
- 等差数列最开始形成的时候，即：只有两个元素的时候，对结果没有贡献，因为题目要求等差数列的长度至少为 3；
- 如果发现公差相等，才能够找到若干个长度大于等于 3 的等差数列。



 ```python
 
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3:
            return 0
        
        dp = [defaultdict(int) for _ in range(size)]
        res = 0
        for i in range(size):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                if diff in dp[j]:
                    res += dp[j][diff]
        return res
 
 ```

