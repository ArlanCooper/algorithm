# 797. 所有可能的路径
地址:https://leetcode-cn.com/problems/all-paths-from-source-to-target/


# 题目描述
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。

译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。


示例 1：
![img](../pic/797_1.jpg)
```
输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3

```

示例2
![img](../pic/797_2.jpg)
```
输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

```

示例3
```
输入：graph = [[1],[]]
输出：[[0,1]]

```


示例4
```
输入：graph = [[1,2,3],[2],[3],[]]
输出：[[0,1,2,3],[0,2,3],[0,3]]

```


示例5
```
输入：graph = [[1,3],[2],[3],[]]
输出：[[0,1,2,3],[0,3]]

```

# 我的解法
没解出来


# 参考解法
```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = list()
        stk = list()

        def dfs(x: int):
            if x == len(graph) - 1:
                ans.append(stk[:])
                return
            
            for y in graph[x]:
                stk.append(y)
                dfs(y)
                stk.pop()
        
        stk.append(0)
        dfs(0)
        return ans


```