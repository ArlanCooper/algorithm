# 1583. 统计不开心的朋友
地址:https://leetcode-cn.com/problems/count-unhappy-friends/


# 题目描述
给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。

对每位朋友 i，preferences[i] 包含一份 按亲近程度从高到低排列 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 0 到 n-1 之间的整数表示。

所有的朋友被分成几对，配对情况以列表 pairs 给出，其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。

但是，这样的配对情况可能会是其中部分朋友感到不开心。在 x 与 y 配对且 u 与 v 配对的情况下，如果同时满足下述两个条件，x 就会不开心：

- x 与 u 的亲近程度胜过 x 与 y，且
- u 与 x 的亲近程度胜过 u 与 v

返回 不开心的朋友的数目 。

示例1:
```
输入：n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
输出：2
解释：
朋友 1 不开心，因为：
- 1 与 0 配对，但 1 与 3 的亲近程度比 1 与 0 高，且
- 3 与 1 的亲近程度比 3 与 2 高。
朋友 3 不开心，因为：
- 3 与 2 配对，但 3 与 1 的亲近程度比 3 与 2 高，且
- 1 与 3 的亲近程度比 1 与 0 高。
朋友 0 和 2 都是开心的。

```


示例2:
```
输入：n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
输出：0
解释：朋友 0 和 1 都开心。

```

示例3:
```
输入：n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
输出：4

```

# 我的解法
没解出来，今天的题目有点虐狗

# 参考解法
## 思路
七夕节出这么一道统计不开心的朋友，简直是关起门来打单身狗...
这道题思路其实比较简单就是个暴力模拟搜索，这里记下解题思路：
1. 初始化ret = 0 用于记录不开心的人数
2. 为了减少搜索条件，我们定义一个字典dic，然后循环pairs，保存每个人当前的匹配关系
3. 之后循环pairs，分别判断当前匹配对中，每个人是否快乐，判断方式如下：
   - 由于涉及相互判断最好单独定义一个check函数进行比较
   - 将x, y 传入比较函数，然后循环preferences[x]的亲密排行中每一个人，定义为idx
   - 如果idx当前配对的人亲密度比x低，则idx不开心，x也不开心，ret+=1 终止搜索
   - 否则持续查找，直到x亲密排行中idx == y，表示当前的配对符合开心条件，终止循环
4. 最终返回ret即可

```python
class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        ret, dic = 0, {} #初始化
        for p in pairs: #生成配对的字典
            dic[p[0]], dic[p[1]] = p[1], p[0]

        def check(i, j): 
            #检验是否不开心
            nonlocal ret
            # 找i的亲密度列表
            for idx in preferences[i]: #遍历与i关系好的列表
                # 如果遇到J终止
                if idx == j: break
                # 找idx当前搭配的队友,是否比i更亲密
                if preferences[idx].index(dic[idx]) > preferences[idx].index(i):
                    ret += 1
                    return

        for pair in pairs:
            check(pair[0], pair[1])
            check(pair[1], pair[0])
        return ret

```


# 另一种参考解法
```python

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n == 2:return 0
        dicts = dict()
        for i,j in pairs:
            dicts[i] = j
            dicts[j] = i
        res = 0
        for i,j in pairs:
            for x in preferences[i][:preferences[i].index(j)]:
                if preferences[x].index(i) < preferences[x].index(dicts[x]):
                    res += 1
                    break
            for x in preferences[j][:preferences[j].index(i)]:
                if preferences[x].index(j) < preferences[x].index(dicts[x]):
                    res += 1
                    break
        return res
                    


```