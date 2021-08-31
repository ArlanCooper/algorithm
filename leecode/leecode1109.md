# 1109. 航班预订统计
地址:https://leetcode-cn.com/problems/corporate-flight-bookings/

这里有 n 个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。


示例1
```
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]
```

示例2
```
输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]

```

# 我的解法
时间复杂度超了
```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dics = {i:0 for i in range(1,n+1)}
        for book in bookings:
            for j in range(book[0],book[1]+1):
                dics[j] += book[2]
        res = [val for val in dics.values()]
        return res
```


# 参考解法
## 思路
差分数组
注意到一个预订记录实际上代表了一个区间的增量。我们的任务是将这些增量叠加得到答案。因此，我们可以使用差分解决本题。
差分数组对应的概念是前缀和数组，对于数组 [1,2,2,4]，其差分数组为 [1,1,0,2]，差分数组的第 ii 个数即为原数组的第 i-1个元素和第 i个元素的差值，也就是说我们对差分数组求前缀和即可得到原数组。

差分数组的性质是，当我们希望对原数组的某一个区间 [l,r]施加一个增量nc 时，差分数组 dd 对应的改变是：d[l]增加inc，d[r+1] 减少 inc。这样对于区间的修改就变为了对于两个位置的修改。并且这种修改是可以叠加的，即当我们多次对原数组的不同区间施加不同的增量，我们只要按规则修改差分数组即可。

在本题中，我们可以遍历给定的预定记录数组，每次 O(1)地完成对差分数组的修改即可。当我们完成了差分数组的修改，只需要最后求出差分数组的前缀和即可得到目标数组。



```python

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for left,right,seat in bookings:
            diff[left -1 ] += seat
            if right < n:
                diff[right] -= seat
        for i in range(1,n):
            diff[i] += diff[i-1]
        return diff

```
