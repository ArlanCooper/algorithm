# 863. 二叉树中所有距离为 K 的结点
地址:https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/


# 题目描述
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。


示例1
![img](../pic/863_1.png)
注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

```


# 参考解法
## 思路
节点可直接构建父节点属性（也是看过其他题解之后学到的……），这一点是关键，通过根节点对所有节点进行一次遍历，完成父节点关联，进而树结构是一个可双向查找的节点网。进而，通过target属性层次向外扩张K次，找到所有距离为K的节点即可。由于任意节点可双向遍历，所以要注意维护一个已遍历节点集合去重。


```python
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.par = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def getParent(root): # 深度优先遍历，实现父节点的构建
            if root.left:
                root.left.par = root
                getParent(root.left)
            if root.right:
                root.right.par = root
                getParent(root.right)
        getParent(root) #构建父节点
        root.par = None #根节点没有父节点
        nodes = [(target,0)] # 存储记录节点的表
        seen = {target} #已经遍历的节点
        res = [] # 最后返回的符合条件的结果节点
        while nodes:
            node,d = nodes.pop() # 节点出来
            if d == k: #满足k的距离，就存进去
                res.append(node.val)
            for i in (node.left,node.right,node.par):
                if i and i not in seen:
                    nodes.append((i,d+1))
                    seen.add(i)
        return res


```

# 最优解法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par = None): #深度优先遍历，生成父节点
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)]) #双向列表
        seen = {target} #已经遍历的节点
        while queue:
            if queue[0][1] == K: #如果距离为k   
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []



```