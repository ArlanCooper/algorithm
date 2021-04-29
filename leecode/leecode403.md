# 403. 青蛙过河
地址:https://leetcode-cn.com/problems/frog-jump/


# 题目讲解
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

示例1：
```
输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。

```

示例2:
```
输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

```

提示:
- 2 <= stones.length <= 2000
- 0 <= stones[i] <= $2^31$ - 1
- stones[0] == 0


# 参考解法
```python
'''
动态规划

'''

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones=set(stones) # 设置石头所在位置的集合
        dp = defaultdict(set) #设置字典
        dp[0]={0} # dp[0] 表示一个元素的话，就返回第一个元素
        for s in stones: # 遍历所有的石头
            for step in dp[s]: # 针对某个stone,遍历这个跳法中的所有石头，setp表示需要跳的步长
                for d in [-1,0,1]: # 每次的步长只能-1,0,1
                    if step+d>0 and s+step+d in set_stones: #如果跳的步长大于0，而且跳过之后所在的石头在集合里面，则在该石头所在的位置添加这个跳法
                        dp[s+step+d].add(step+d)
        return len(dp[stones[-1]])>0 #返回最后一个位置是否有跳法



```

```python
'''
深度优先遍历

dfs(pos,step)表示 如果青蛙经过步数为step的跳跃到达位置在pos的石头 它能否跳跃到终点。

结束: pos==stones[-1] 已经在终点 所以返回true
递归: 因为是step跳跃到达的pos，所以再往下可以跳跃step, step+1, step-1, 但是需要注意只能向前跳(即step+d>0)，并且必须跳到石头上(即pos+step+d in stones).
关键：会对同一状态多次求值，所以用记忆化递归，dfs前面加上@lru_cache(None)当参数相同时直接返回值不需要重复计算。
细节：因为第一次跳跃步数只能是1，所以初始step=0

'''



def canCross(stones: List[int]) -> bool:
    @lru_cache(None)
    def dfs(pos,step):
        if pos==stones[-1]: return True
        for d in [-1,0,1]:
            if step+d>0 and pos+step+d in set(stones):
                if dfs(pos+step+d, step+d):
                    return True
        return False
    pos, step = 0, 0
    return dfs(pos, step)

```




