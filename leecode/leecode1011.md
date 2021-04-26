# 1011. 在 D 天内送达包裹的能力
地址: https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/


# 题目描述
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。


示例 1：
```
输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

```

示例 2：
```
输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

```


示例 3：
```
输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

```

提示:
- 1 <= D <= weights.length <= 50000
- 1 <= weights[i] <= 500


# 我的解法
```python
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if D == 1: #如果只需要一天，则直接返回所有的重量的和
            return sum(weights)
        if sum(weights) % D == 0: # 返回商的 上取整 与 权重中最大值 中的大的数
            least = max(int(sum(weights) / D), max(weights))
        else:
            least = max(int(sum(weights) / D)+1, max(weights))
        def get_nd(weights,least): # 按照least值划分所需要的天数
            index,lens = 0, len(weights)
            init,nd = 0,1
            while(index < lens):
                if init+weights[index] <= least:
                    init += weights[index]
                    index += 1
                else:
                    nd += 1
                    init = 0
            return nd
        nd = get_nd(weights,least)
        while(nd > D): # 与必要天数对比，如果比D大，则添加least的值继续划分，直到nd小于等于D为止
            least += 1
            nd = get_nd(weights,least)
        return least
```

# 参考解法
解题思路:
首先这艘船的重量是固定的, 货物的运输顺序必须按照数组weights的顺序来, 不能打乱顺序. 那么我们可以想到这艘船最小的运载能力必须是所有货物中最重的那一件max(weights), 否则无法完成运输的任务. 这艘船最大的运载能力就是一次性把所有的货都搬走, 就是sum(weights). 所以答案就在区间[max(weights), sum(weights)]之间啦!

有了这个思路, 那就找这个区间内的运载能力最小值, 最简单的方法就是从头到尾搜一遍. 但是不太高效, 这样的解法可能也无法满足面试官的要求. 为了找到一个有序区间内的最优解, 用二分法就非常好, 因为折半查找的效率比顺序查找要高.

```python

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 最小值得是任何一个货物都可以运走, 不可以分割货物
        start = max(weights)
        # 最大值是一趟就全部运走, 所以是所有货物之和
        end = sum(weights)
        # 二分法模板
        while start < end:
            # 先求中间值
            mid = (start + end)//2

            # 计算这个中间值需要计算需要多少天运完
            days = self.countDays(mid, weights)
            # 如果天数超了, 说明运载能力有待提升, start改大一点, 继续二分搜索
            if days > D:
                start = mid + 1
            # 否则运载能力改小一点继续搜索
            else:
                end = mid
        return start

    def countDays(self, targetWeight, weights):
        days = 1
        i = 0
        current = 0
        for weight in weights:
            current += weight
            if current > targetWeight:
                days += 1
                current = weight
        return days

```