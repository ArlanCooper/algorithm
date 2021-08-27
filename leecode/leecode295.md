# 295. 数据流的中位数
地址:https://leetcode-cn.com/problems/find-median-from-data-stream/


# 题目描述
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

- void addNum(int num) - 从数据流中添加一个整数到数据结构中。
- ouble findMedian() - 返回目前所有元素的中位数。

示例：
```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

```


# 我的解法
```python
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.median = 0


    def addNum(self, num: int) -> None:
        if len(self.data) == 0:
            self.data.append(num)
        else:
            l,r =0, len(self.data)-1
            while l<= r:
                mid = (l+r)//2
                if num == self.data[mid]:
                    self.data.insert(mid,num)
                    return
                elif num < self.data[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            self.data.insert(l,num)


    def findMedian(self) -> float:
        mid = (len(self.data) -1)//2
        if len(self.data) % 2 == 0:
            self.median = (self.data[mid] + self.data[mid+1])/2
        else:
            self.median = self.data[mid]
        return self.median




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


```


# 参考解法
```python
from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半


    def addNum(self, num: int) -> None:
    #python的heapq默认实现小顶堆的操作，要实现大顶堆，需要将元素取负。
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))


    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


```
