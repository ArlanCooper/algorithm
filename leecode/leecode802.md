# 802. 找到最终的安全状态
地址: https://leetcode-cn.com/problems/find-eventual-safe-states/

# 题目描述
在有向图中，以某个节点为起始节点，从该点出发，每一步沿着图中的一条有向边行走。如果到达的节点是终点（即它没有连出的有向边），则停止。

对于一个起始节点，如果从该节点出发，无论每一步选择沿哪条有向边行走，最后必然在有限步内到达终点，则将该起始节点称作是 安全 的。

返回一个由图中所有安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。

该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j 节点的一个列表，满足 (i, j) 是图的一条有向边。

示例1:
![img](../pic/802_1.png)
```
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
解释：示意图如上。

```

示例2:
```
输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
输出：[4]

```


# 我的解法
思路： 通过深度优先遍历，获取每个节点是否为安全节点，但是时间复杂度过高，思路不清晰
导致复杂度过高，没有通过测试

```python

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        lens = len(graph)
        bad = set()
        def dfs(nodes,times,lens,result):
            if len(nodes) == 0 and times < lens:
                result.add(1)
                return result
            if times >= lens:
                result.add(0)
                return result
            for node in nodes:
                if len(dic[node]) == 0 and times+1 < lens:
                    result.add(1)
                if times+1 >= lens:
                    result.add(0)
                dfs(dic[node],times+1,lens,result)
            return result
        dic = {i:a for i,a in enumerate(graph)}
        for i,node in enumerate(graph):
            if len(node) == 0:
                res.append(i)
            elif len(node) == 1 and len(dic[node[0]]) == 0:
                res.append(i)
            else:
                for j,no in enumerate(node):
                    if no in bad or (len(bad)>0 and len(set(dic[no])&bad)>0):
                        j = -1
                        break
                    result = dfs(node,1,lens,set())
                    if 0 in result:
                        j = -1
                        break
                if j != -1:
                    res.append(i)
                else:
                    bad.add(i)


        return res

```

# 参考解法，最优解法
## 思路
深度优先搜索 + 三色标记法

根据题意，若起始节点位于一个环内，或者能到达一个环，则该节点不是安全的。否则，该节点是安全的。

我们可以使用深度优先搜索来找环，并在深度优先搜索时，用三种颜色对节点进行标记，标记的规则如下：

- 白色（用 00 表示）：该节点尚未被访问；
- 灰色（用 11 表示）：该节点位于递归栈中，或者在某个环上；
- 黑色（用 22 表示）：该节点搜索完毕，是一个安全节点。

当我们首次访问一个节点时，将其标记为灰色，并继续搜索与其相连的节点。
如果在搜索过程中遇到了一个灰色节点，则说明找到了一个环，此时退出搜索，栈中的节点仍保持为灰色，这一做法可以将「找到了环」这一信息传递到栈中的所有节点上。

如果搜索过程中没有遇到灰色节点，则说明没有遇到环，那么递归返回前，我们将其标记由灰色改为黑色，即表示它是一个安全的节点。

## 复杂度分析

- 时间复杂度：O(n+m)，其中 n 是图中的点数，m 是图中的边数。

- 空间复杂度：O(n)O(n)。存储节点颜色以及递归栈的开销均为O(n)。



```python
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        lens = len(graph) # 图节点数
        color = [0 for i in range(lens)] # 初始状态为0，即未遍历
        def safe(x): # 定义是否为安全节点函数，深度优先遍历
            if color[x] > 0:
                return color[x] == 2
            color[x] = 1
            for node in graph[x]:
                if not safe(node): # 如果存在一个不是安全节点则返回False
                    return False
            color[x] = 2 #说明为安全节点
            return True
        return [i for i in range(lens) if safe(i)] # 返回所有的安全节点







```