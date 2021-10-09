# 352. 将数据流变为多个不相交区间
地址:https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals/


# 题目描述
 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 SummaryRanges 类：

- SummaryRanges() 使用一个空数据流初始化对象。
- void addNum(int val) 向数据流中加入整数 val 。
- int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。

示例
```
输入：
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]

```


# 我的解法
没写出来


# 参考解法
## 思路
假设我们使用某一数据结构维护这些不相交的区间，在设计具体的数据结构之前，我们需要先明确 void addNum(int val) 这一操作会使得当前的区间集合发生何种变化：

情况一：如果存在一个区间 [l,r]，它完全包含 val，即 rl≤val≤r，那么在加入 val 之后，区间集合不会有任何变化；

情况二：如果存在一个区间[l,r]，它的右边界 rr「紧贴着」val，即 r+1=val，那么在加入 val 之后，该区间会从 [l,r] 变为 [l,r+1]；

情况三：如果存在一个区间 [l,r]，它的左边界 ll「紧贴着」val，即 l−1=val，那么在加入 val 之后，该区间会从 [l,r] 变为 [l−1,r]；

情况四：如果情况二和情况三同时满足，即存在一个区间 [l_0, r_0]满足 r0+1=val，并且存在一个区间 [l_1, r_1]满足 l1−1=val，那么在加入val 之后，这两个区间会合并成一个大区间 [l_0, r_1]

情况五：在上述四种情况均不满足的情况下，val 会单独形成一个新的区间[val,val]。


```python

from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, val: int) -> None:
        intervals_ = self.intervals
        keys_ = self.intervals.keys()
        values_ = self.intervals.values()

        # 找到 l1 最小的且满足 l1 > val 的区间 interval1 = [l1, r1]
        # 如果不存在这样的区间，interval1 为 len(intervals)
        interval1 = intervals_.bisect_right(val)
        # 找到 l0 最大的且满足 l0 <= val 的区间 interval0 = [l0, r0]
        # 在有序集合中，interval0 就是 interval1 的前一个区间
        # 如果不存在这样的区间，interval0 为尾迭代器
        interval0 = (len(intervals_) if interval1 == 0 else interval1 - 1)

        if interval0 != len(intervals_) and keys_[interval0] <= val <= values_[interval0]:
            # 情况一
            return
        else:
            left_aside = (interval0 != len(intervals_) and values_[interval0] + 1 == val)
            right_aside = (interval1 != len(intervals_) and keys_[interval1] - 1 == val)
            if left_aside and right_aside:
                # 情况四
                left, right = keys_[interval0], values_[interval1]
                intervals_.popitem(interval1)
                intervals_.popitem(interval0)
                intervals_[left] = right
            elif left_aside:
                # 情况二
                intervals_[keys_[interval0]] += 1
            elif right_aside:
                # 情况三
                right = values_[interval1]
                intervals_.popitem(interval1)
                intervals_[val] = right
            else:
                # 情况五
                intervals_[val] = val

    def getIntervals(self) -> List[List[int]]:
        # 这里实际上返回的是 List[Tuple[int, int]] 类型
        # 但 Python 的类型提示不是强制的，因此也可以通过
        return list(self.intervals.items())


```

# 最优解法
```python
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []


    def addNum(self, val: int) -> None:
        if len(self.intervals)==0:
            self.intervals.append([val,val])
            return
        idx = bisect.bisect_left(self.intervals, [val,val])
        if idx==len(self.intervals):
            if self.intervals[-1][1]>=val: return
            elif self.intervals[-1][1]==val-1:
                self.intervals[-1][1] = val
            else: self.intervals.append([val,val])
        elif idx==0:
            if val>=self.intervals[0][0]: return
            elif val==self.intervals[0][0]-1: self.intervals[0][0] = val
            else: self.intervals.insert(0, [val,val])
        else:
            if val<self.intervals[idx][0]-1 and val>self.intervals[idx-1][1]+1: self.intervals.insert(idx, [val,val])
            elif val==self.intervals[idx][0]-1 and val==self.intervals[idx-1][1]+1:
                self.intervals[idx-1][1] = self.intervals[idx][1]
                del self.intervals[idx]
            elif val>=self.intervals[idx][0]-1: self.intervals[idx][0] = min(self.intervals[idx][0], val)
            elif val<=self.intervals[idx-1][1]+1: self.intervals[idx-1][1] = max(self.intervals[idx-1][1], val)


    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


```
