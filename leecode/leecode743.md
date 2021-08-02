# 743. 网络延迟时间
地址：https://leetcode-cn.com/problems/network-delay-time/


# 题目描述
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

示例1
![img](../pic/743_1.png)
```
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

```

示例2
```
输入：times = [[1,2,1]], n = 2, k = 1
输出：1

```


示例3
```
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1

```


# 我的解法(有问题)
```python
def networkDelayTime(times, n, k):
    if len(times) < n - 1: #边数小于n-1，一定不能遍历所有节点
        return -1
    dic = {(i[0],i[1]):i[2] for i in times}
    visited = [k]
    needed = {i for i in range(1,n+1)} - {k}
    new_dic = {}
    for i in needed:
        for m in visited:
            print('i,m:',(i,m))
            if (m,i) in dic:
                new_dic[(m,i)] = dic[(m,i)]
                if (k,m) in dic:
                    if (k,i) in dic:
                        if new_dic[(k,m)] + new_dic[(m,i)] < new_dic[(k,i)]:
                            new_dic[(k,i)] = new_dic[(k,m)] + new_dic[(m,i)]
                    else:
                         new_dic[(k,i)] = new_dic[(k,m)] + new_dic[(m,i)]
            if (i,m) in dic:
                new_dic[(i,m)] = dic[(i,m)]
                if (k,i) in dic:
                    if (k,m) in new_dic:
                        if new_dic[(k,i)] + new_dic[(i,m)] < new_dic[(k,m)]:
                            new_dic[(k,m)] = new_dic[(k,i)] + new_dic[(i,m)]
                    else:
                         new_dic[(k,m)] = new_dic[(k,i)] + new_dic[(i,m)]
            print(new_dic)
        visited.append(i)
        
    ans = [new_dic[(k,i)] for i in needed if (k,i) in new_dic]
    if len(ans) == n - 1:
        return max(ans)
    else:
        return -1


```


# 参考解法

广度优先遍历

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = defaultdict(lambda:defaultdict(int)) #定义字典
        for u,v,w in times: # 生成字典
            connect[u][v] = w
        q = deque([k]) #构建双向队列
        explored = defaultdict(lambda:inf) #扩展字典其余值为无穷大
        explored[k] = 0 #k的值为0
        while q:
            node = q.popleft() #初始元素出列
            t = explored[node]            
            for other, tm in connect[node].items():
                if t + tm < explored[other]:
                    explored[other] = t + tm
                    q.append(other)
        return -1 if len(explored) < n else max(explored.values())


```


# 最优解法
```python
# 广度优先遍历   
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [[float('inf')]*(n+1) for _ in range(n+1)]
        for u,v,p in times:
            dp[u][v] = p
        temp = [i for i in range(1, n+1) if i != k]
        distance = dp[k]
        while temp:
            idx = temp[0]
            for i in temp:
                if distance[i] < distance[idx]:
                    idx = i
            temp.remove(idx)
            for j in temp:
                if distance[idx] + dp[idx][j] < distance[j]:
                    distance[j] = distance[idx] + dp[idx][j]
        ans = [i for i in distance if i != float('inf')]
        return max(ans) if len(ans) == n-1 else -1


```