# 502. IPO
地址:https://leetcode-cn.com/problems/ipo/

# 题目描述
假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。

给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。

最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内。

示例1
```
输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。

```



示例2
```
输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
输出：6

```
# 我的解法
```python
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        res = 0
        n = len(capital)
        inds = set()
        ind = 0
        for _ in range(k):
            tmp_c = 0
            for i in range(n):
                if capital[i] <= w and i not in inds:
                    if profits[i] > tmp_c:
                        tmp_c = profits[i]
                        ind = i
            res += tmp_c
            inds.add(ind)
            w = w - capital[ind] + profits[ind]
        return res


```
不知为什么，我的解法答案提示不对，但是我觉得没问题，不知道为什么了

# 参考解法
## 思路

我们首先思考，如果不限制次数下我们可以获取的最大利润，我们应该如何处理？我们只需将所有的项目按照资本的大小进行排序，依次购入项目 i，同时手中持有的资本增加 profits[i]，直到手中的持有的资本无法启动当前的项目为止。

如果初始资本w≥max(capital)，我们直接返回利润中的 k个最大元素的和即可。

当前的题目中限定了可以选择的次数最多为 k 次，这就意味着我们应该贪心地保证选择每次投资的项目获取的利润最大，这样就能保持选择 k 次后获取的利润最大。

我们首先将项目按照所需资本的从小到大进行排序，每次进行选择时，假设当前手中持有的资本为 w，我们应该从所有投入资本小于等于 w 的项目中选择利润最大的项目 j，然后此时我们更新手中持有的资本为 w+profits[j]，同时再从所有花费资本小于等于 w+profits[j] 的项目中选择，我们按照上述规则不断选择 k 次即可。

我们利用大根堆的特性，我们将所有能够投资的项目的利润全部压入到堆中，每次从堆中取出最大值，然后更新手中持有的资本，同时将待选的项目利润进入堆，不断重复上述操作。

如果当前的堆为空，则此时我们应当直接返回。

```python
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))

        n = len(profits)
        curr = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key = lambda x : x[0])
        
        pq = []
        for _ in range(k):
        # 将所有需要的本金小于等于当前资本的项目加入最大堆
            while curr < n and arr[curr][0] <= w:
                heappush(pq, -arr[curr][1])
                curr += 1
            # 如果有项目在当前的大顶堆中，我们做利益最大的那一个。
            if pq:
                w -= heappop(pq)
            else:
                break
        
        return w

```
