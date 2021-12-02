# 506. 相对名次
地址:https://leetcode-cn.com/problems/relative-ranks/


# 题目描述
给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。

运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：

- 名次第 1 的运动员获金牌 "Gold Medal" 。
- 名次第 2 的运动员获银牌 "Silver Medal" 。
- 名次第 3 的运动员获铜牌 "Bronze Medal" 。
- 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
- 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。


示例1
```
输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。

```

示例2
```
输入：score = [10,3,8,9,4]
输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释：名次为 [1st, 5th, 3rd, 2nd, 4th] 。

```


# 我的解法
```python

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sorted_nums = sorted(enumerate(score), key=lambda x: x[1],reverse=True)
        dics = {}
        res = []
        for ind,nums in enumerate(sorted_nums):
            if ind == 0:
                dics[nums[0]] = 'Gold Medal'
            elif ind == 1:
                dics[nums[0]] = 'Silver Medal'
            elif ind == 2:
                dics[nums[0]] = 'Bronze Medal'
            else:
                dics[nums[0]] = str(ind+1)
        ans = [i[1] for i in sorted(dics.items(),key=lambda x:x[0])]
        return ans

```


# 参考解法
```python
class Solution:
    desc = ("Gold Medal", "Silver Medal", "Bronze Medal")

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = self.desc[i] if i < 3 else str(i + 1)
        return ans



```
