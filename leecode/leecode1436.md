# 1436. 旅行终点站
地址:https://leetcode-cn.com/problems/destination-city/


# 题目描述
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。

示例1
```
输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo" 
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。

```

示例2
```
输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。


```

示例3
```
输入：paths = [["A","Z"]]
输出："Z"

```

# 我的解法
## 思路
简单思路，统计每个地方出现的次数，目的地肯定只出现一次，为了区别，最初起始也是只出现一次，则在计数的时候，起始点每次加2
```python

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        dic = defaultdict(int)
        for path in paths:
            dic[path[0]] += 2
            dic[path[1]] += 1
        ans = sorted(dic.items(),key=lambda x:x[1])[0][0]
        return ans
            
        


```


# 参考解法
## 思路
根据终点站的定义，终点站不会出现在cityAi中，因为存在从cityAi出发的线路，所以终点站只会出现在cityBi中。据此，我们可以遍历cityBi，返回不在 cityAi中的城市，即为答案。

```python

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)


```


# 最优答案
```python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        tmp0 = []
        tmp1 =  []
        for item in paths:
            tmp0.append(item[0])
            tmp1.append(item[1])
        return list(set(tmp1)-set(tmp0))[0]        

```