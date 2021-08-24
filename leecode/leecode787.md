# 787. K 站中转内最便宜的航班
地址:https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/

# 题目描述
有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 toi 抵达 pricei。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。

示例1
```
输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200

```

示例2
```
输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500

```
- 提示
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
航班没有重复，且不存在自环
0 <= src, dst, k < n
src != dst

# 我的解法
没有想法，未解出来

# 参考解法
## 思路，动态规划
我们用 f[t][i]表示通过恰好 tt 次航班，从出发城市 src 到达城市 i 需要的最小花费。在进行状态转移时，我们可以枚举最后一次航班的起点 j，即：

$f[t][i]= \underset{(j,i)∈flights }{min}$​​​​​{f\[t−1\]\[j\]+cost(j,i)}

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
         dics = {}
         for edge in edges:
            if edge[0] not in dics:
                 dics[edge[0]] = [(edge[1],edge[2])]
            else:
                dics[edge[0]].append((edge[1],edge[2]))
        def search(dics,src,dst,l,result=[]):
            for edge in dics[src]:
                if dst == edge[0] and l+1 == k:
                    result 


```

# 最优解法
```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = collections.defaultdict(list)
        for x, y, p in flights:
            g[x].append([y, p])
        
        q = collections.deque([(src, 0, 0)]) # (place, k, price)
        minm = float('inf')
        seen = dict()

        while q:
            cur, trans, price = q.popleft()
            if trans > k + 1 or price > minm:
                continue
            if cur == dst:
                minm = min(minm, price)
                continue
            if cur not in seen:
                seen[cur] = price
            elif cur in seen and seen[cur] < price:
                continue
            elif cur in seen and seen[cur] > price:
                seen[cur] = price
            for y, p in g[cur]:
                q.append((y, trans + 1, price + p))
        
        return minm if minm != float('inf') else -1

```

