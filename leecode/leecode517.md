# 517. 超级洗衣机
地址:https://leetcode-cn.com/problems/super-washing-machines/


# 题目描述
假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 m (1 <= m <= n) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 machines 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 最少的操作步数 。如果不能使每台洗衣机中衣物的数量相等，则返回 -1 。

示例1
```
输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2 

```


示例2
```
输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1  

```


# 我的解法
没做出来

# 参考解法

# 思路
设所有洗衣机内的衣服个数之和为 tot，要使最终所有洗衣机内的衣服个数相同，那么 tot 必须是 n 的倍数，否则我们直接返回 -1。

记$$avg = \frac{tot}{n}$$ ，定义 $machines[i]' =machines[i]−avg$，若 machines[i]'为正则说明需要移出machines[i]'件衣服，为负则说明需要移入−machines[i]′件衣服。

我们分两种情况来考虑操作步数：

A 与 B 两组之间的衣服，最多需要maxi=0n−1∣sum[i]∣ 次衣服移动；
组内的某一台洗衣机内的衣服数量过多，需要向左右两侧移出衣服，这最多需要
$$ max^{n-1}_{i=0} machines[i]' $$ 
次衣服移动。


参考详细讲解

https://leetcode-cn.com/problems/super-washing-machines/solution/jie-du-yi-xia-zi-ji-li-jie-de-guan-fang-ydl19/
```python

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        tot = sum(machines)
        n = len(machines)
        if tot % n:
            return -1
        avg = tot // n
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans


```
