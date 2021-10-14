# 剑指 Offer II 069. 山峰数组的顶部
地址:https://leetcode-cn.com/problems/B1IidL/

# 题目描述
符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。


示例1
```
输入：arr = [0,1,0]
输出：1

```

示例2
```
输入：arr = [1,3,5,4,2]
输出：2

```


示例3
```
输入：arr = [0,10,5,2]
输出：1

```

示例4
```
输入：arr = [3,4,5,1]
输出：2

```


示例5
```
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2

```

# 我的解法
```python

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1,n):
            if arr[i-1]< arr[i]:
                continue
            else:
                return i-1

```


# 参考解法
```python

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans


```

# 最优解法
```python

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))

```
