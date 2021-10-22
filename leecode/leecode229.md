# 229. 求众数 II
地址:https://leetcode-cn.com/problems/majority-element-ii/


# 题目描述
给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

示例1
```
输入：[3,2,3]
输出：[3]

```


示例2
```
输入：nums = [1]
输出：[1]

```


示例3
```
输入：[1,1,1,3,3,2,2,2]
输出：[1,2]

```

# 我的解法
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dics = defaultdict(int)
        for i in nums:
            dics[i] += 1
        th = len(nums)//3
        res = [i for i,j in dics.items() if j > th]
        return res



```

# 参考解法
## 思路
摩尔投票

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:
            # 如果该元素为第一个元素，则计数加1
            if vote1 > 0 and num == element1:
                vote1 += 1
            # 如果该元素为第二个元素，则计数加1
            elif vote2 > 0 and num == element2:
                vote2 += 1
            # 选择第一个元素
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            # 选择第二个元素
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # 如果三个元素均不相同，则相互抵消1次
            else:
                vote1 -= 1
                vote2 -= 1

        cnt1, cnt2 = 0, 0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1 += 1
            if vote2 > 0 and num == element2:
                cnt2 += 1        
        # 检测元素出现的次数是否满足要求
        if vote1 > 0 and cnt1 > len(nums) / 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            ans.append(element2)

        return ans

```

# 最优解法
```python

from collections import Counter
class Solution:
    def majorityElement(self, nums):
        l = len(nums)
        cnter = Counter(nums)
        ans = [ i for i in cnter if cnter[i]>l/3 ]
        return ans

```
