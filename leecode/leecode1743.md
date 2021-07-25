# 1743. 从相邻元素对还原数组
地址: https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/

# 题目描述
存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。

给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。

题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。

返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。


示例1
```
输入：adjacentPairs = [[2,1],[3,4],[3,2]]
输出：[1,2,3,4]
解释：数组的所有相邻元素对都在 adjacentPairs 中。
特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
```


示例2
```
输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
输出：[-2,4,1,-3]
解释：数组中可能存在负数。
另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
```


示例3
```
输入：adjacentPairs = [[100000,-100000]]
输出：[100000,-100000]
```

# 参考解法
## 思路
我们可以利用 ansans 的长度为$2 <= n <= 10^5$，构造一个长度$10^6$的数组 q（这里可以使用 static 进行加速，让多个测试用例共享一个大数组）。

这里 q 数组不一定要开成 1e61e6 大小，只要我们 qq 大小大于 ans 的两倍，就不会存在越界问题。

从 q数组的 中间位置 开始，先随便将其中一个元素添加到中间位置，使用「双指针」分别往「两边拓展」（l 和 r 分别指向左右待插入的位置）。

当 l 指针和 r 指针之间已经有 n 个数值，说明整个 ans 构造完成，我们将 [l + 1, r - 1] 范围内的数值输出作为答案即可。



```python
class Solution:
    N = 10 ** 6 + 10
    q = [0] * N

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        m = len(adjacentPairs)
        n = m + 1
        hashmap = defaultdict(list)
        for a, b in adjacentPairs:
            hashmap[a].append(b)
            hashmap[b].append(a)
        l = self.N // 2
        r = l + 1
        std = adjacentPairs[0][0]
        lt = hashmap[std]
        self.q[l] = std
        l -= 1
        self.q[r] = lt[0]
        r += 1
        if len(lt) > 1:
            self.q[l] = lt[1]
            l -= 1
        while (r-1)-(l+1)+1<n:
            alt = hashmap[self.q[l+1]]
            j = l
            for i in alt:
                if i != self.q[l+2]:
                    self.q[j] = i
                    j -= 1
            l = j
            
            blt = hashmap[self.q[r-1]]
            j = r
            for i in blt:
                if i != self.q[r - 2]:
                    self.q[j] = i
                    j += 1
            r = j
        ans = [0] * n
        for idx in range(n):
            ans[idx] = self.q[idx+l+1]
        return ans

```


# 最优解法
```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        c = collections.defaultdict(list)#创建字典
        for u, v in adjacentPairs:
            c[u].append(v)
            c[v].append(u)
        ans = collections.deque()#创建队列
        for n, l in c.items():
            if len(l) == 1:
                ans.append(n)
                break
        v = set()
        v.add(ans[-1])
        for _ in range(len(adjacentPairs)):
            for a in c[ans[-1]]:# 取出最后一个元素相邻的数字，如果之前存在就不再存入，否则就存入
                if a not in v:
                    ans.append(a)
                    v.add(a)
        return list(ans)


```