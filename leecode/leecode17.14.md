# 面试题 17.14. 最小K个数
地址:https://leetcode-cn.com/problems/smallest-k-lcci/

# 题目描述
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
示例
```
输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

```

# 我的解法
```python
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k] if k>0 else []

```

# 参考解法
## 堆排序的方法
```
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

```
