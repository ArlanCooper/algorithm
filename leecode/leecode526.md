# 526. 优美的排列
地址:https://leetcode-cn.com/problems/beautiful-arrangement/


# 题目描述
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

- 第 i 位的数字能被 i 整除
- i 能被第 i 位上的数字整除

现在给定一个整数 N，请问可以构造多少个优美的排列？


示例1
```
输入: 2
输出: 2
解释: 

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
```

# 我的解法
没写出来

# 参考解法
## 思路
和回溯差不多，每次填入一个合理的可选的数，直到最终填出优美的排列，才累加1。
采用记忆化递归，这样遇到相同位置剩余可选的数相同的情况时，不需要再计算。(注意可以不记录到达第几个数，因为从available的长度即可推)

更新了最佳状态压缩，按可填入个数递归。


```python

class Solution:
    def countArrangement(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1,n+1):
            for j in range(1, n+1):
                # 每个位置可以填入哪些数
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j-1)
        # 根据可填入数字的个数排序，优先填入个数少的
        order = sorted(canFill.keys(), key=lambda x:len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # 全部填入
            if state == end:
                return 1
            cnts = ans = 0
            # 当前该填第几个位置
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # 当前位置可以填哪些数
            for i in canFill[order[cnts]]:
                # 哪些数还没被填
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans
        
        return dfs(0)

```