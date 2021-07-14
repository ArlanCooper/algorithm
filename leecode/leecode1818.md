# 1818. 绝对差值和
地址: https://leetcode-cn.com/problems/minimum-absolute-sum-difference/


# 题目描述
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 $10^9 + 7$ 取余 后返回。


示例 1：
```
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3

```

示例 2：
```
输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0


```

示例3
```
输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

```


# 我的解法
```
def minAbsoluteSumDiff(nums1, nums2):
    lens = len(nums1)
    mod = 10**9 + 7
    ans = 0
    ind = []
    for i in range(lens):
        tmp = abs(nums1[i]-nums2[i])
        ans += tmp
        last = 0
        tmps = (tmp - abs(nums2[i]-nums1[j]) for j in range(lens))
        ind.append(max(tmps))
    ans -= max(ind)
    return ans % mod

```
时间复杂度过高，超出时间

# 参看解法
```python

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n, total, sl, ans = len(nums1), 0, sorted(nums1), inf
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            # bisect是python内置模块，用于有序序列的插入和查找。
            idx = bisect.bisect_left(sl, nums2[i])
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total

```

# 参看解法2
```python
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7

        size = len(nums1)
        res = 0
        max_value = 0

        sortedlist = sorted(nums1)

        for i in range(size):
            d = abs(nums1[i]-nums2[i])
            
            res = (res + d) % mod
            if d > max_value:
                max_value = max(max_value, d - self.fun(sortedlist, nums2[i]))

        return (res-max_value+mod) % mod

    def fun(self, sortedlist, target):
        '''
        二分法查找与target最相近的数字
        '''
        l = 0
        r = len(sortedlist)

        while l < r - 1:
            m = (l+r) >> 1
            if sortedlist[m] == target:
                return 0
            elif sortedlist[m] < target:
                l = m
            else:
                r = m

        if l + 1 == len(sortedlist):
            return abs(target - sortedlist[-1])
        
        return min(abs(target-sortedlist[l]), abs(sortedlist[l+1]-target))

```