# 149. 直线上最多的点数
地址:https://leetcode-cn.com/problems/max-points-on-a-line/

# 题目描述
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

示例1：
```
输入：points = [[1,1],[2,2],[3,3]]
输出：3

```

示例2：
```
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
```

# 我的解法
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        online_points = []
        lens = len(points)
        if lens <= 2:
            return lens


        def get_nums(mypoints,myfunc):
            count = 0
            for x,y in mypoints:
                if abs(myfunc(x,y)) <= 0.00001: # 因为计算小数，会产生误差
                    count +=1
            return count
        for i in range(lens):
            for j in range(lens):
                if j != i:
                    if points[j][0] != points[i][0]:
                        k = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                        b = (points[i][0] * points[j][1]-points[j][0]*points[i][1])/(points[i][0]-points[j][0])
                        tmp = lambda x,y: k * x + b - y
                    else:
                        tmp = lambda x,y: x - points[i][0]
                    #func.append(tmp)
                    count = get_nums(points,tmp)
                    online_points.append(count)
        return max(online_points)

```

# 参考解法
建立一个 length * length 长度的二维数组存储从第i个点到第j个点的斜率 斜率用[x1-x0,y1-y0]进行存储
只需要遍历这个表中同行斜率最多的相同元素个数即可
备注：也是仅仅考虑斜率，觉得答案很讨巧
```python
class Solution:
    def is_same(self,slope1,slope2): # 判断斜率是否相同
        if slope1[1] == 0 and slope2[1] == 0 and slope2[0]!=0:
            return True
        elif slope1[1] == 0 or slope2[1] == 0:
            return False
        else:
            if slope1[0]/slope1[1] == slope2[0]/slope2[1]:
                return True
            else:
                return False

    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        if length == 1:
            return 1
        slope = [[[0,0]for i in range(length)]for i in range(length)]  # 存储斜率 [x,y] 斜率 x/y
        for i in range(length):
            for j in range(i+1,length):
                slope[i][j][0] = points[j][0] - points[i][0]
                slope[i][j][1] = points[j][1] - points[i][1]
                # 获取斜率

        set = 1
        for i in range(length):
            for j in range(set):
                slope[i][j] = slope[j][i]
            set += 1
        count = 0
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                else:
                    flag = 1
                    for k in range(length):
                        if self.is_same(slope[i][j],slope[i][k]):
                            flag += 1
                    if flag > count:
                        count = flag
        return count

```

# 效率最高解法
这个方法很取巧，但是，不能保证都是对的，因为这个方法只考虑了斜率，而没有考虑b值
```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        res = 0
        
        for i in range(length-1):
            tmpd = {}
            for j in range(i+1,length):
                gradx = points[j][0] - points[i][0]
                if gradx:    
                    grad = (points[j][1] - points[i][1])/gradx
                else:
                    grad = float("inf")
                tmpd[grad] = tmpd.get(grad,0) + 1 
            res = max(res,max(tmpd.values()))
         
        return res+1


```