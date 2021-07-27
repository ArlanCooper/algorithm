# 671. 二叉树中第二小的节点
地址: https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/


# 题目描述
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。


示例1
![img](../pic/671_1.jpg)
```
输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。
```

示例2
![img](../pic/671_2.jpg)
```
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
```

# 我的解法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        mins = root.val #根节点是最小值
        def get_second(root,mins): #遍历整棵树，发现比最小值大的数就返回
            if root.val > mins:
                return root.val
            if root.left is None: #如果到最后都没有比最小值大的数，则返回最小值
                return mins
            left = get_second(root.left,mins)
            right = get_second(root.right,mins)
            if left == mins or right == mins:
                return max(left,right)
            else:
                return min(left,right)
        val = get_second(root,mins)
        if val == mins:
            return -1
        else:
            return val
```

# 参考解法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return -1
        res = self.search(root)
        if res == root.val:
            return -1
        else:
            return res
    
    def search(self, root):
        if root.left == None and root.right == None:
            return root.val
        
        if root.left.val == root.val and root.right.val != root.val:
            res1 = self.search(root.left)
            res2 = root.right.val
        elif root.right.val == root.val and root.left.val != root.val:
            res1 = root.left.val
            res2 = self.search(root.right)
        elif root.left.val == root.val and root.right.val == root.val:
            res1 = self.search(root.left)
            res2 = self.search(root.right)
        
        if res1 == root.val and res2 == root.val:
            return res1
        elif res1 == root.val and res2 != root.val:
            return res2
        elif res1 != root.val and res2 == root.val:
            return res1
        else:
            return min(res1, res2)

```
