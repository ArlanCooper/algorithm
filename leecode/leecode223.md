# 223. 矩形面积
地址:https://leetcode-cn.com/problems/rectangle-area/


# 题目描述
给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。

每个矩形由其 左下 顶点和 右上 顶点坐标表示：

- 第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。
- 第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。


示例1
![img](../pic/223_1.png)
```
输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
输出：45

```

示例2
```
输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
输出：16

```

# 我的解法
考虑不周，很多情况没考虑


# 参考解法
## 思路
两个矩形覆盖的总面积等于两个矩形的面积之和减去两个矩形的重叠部分的面积。由于两个矩形的左下顶点和右上顶点已知，因此两个矩形的面积可以直接计算。如果两个矩形重叠，则两个矩形的重叠部分也是矩形，重叠部分的面积可以根据重叠部分的边界计算。

```python

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        overlapArea = max(overlapWidth, 0) * max(overlapHeight, 0)
        return area1 + area2 - overlapArea


```

