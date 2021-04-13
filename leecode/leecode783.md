# 783. 二叉搜索树节点最小距离
地址: https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/


# 题目描述
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同


示例 1：
![img](../pic/783_bst1.jpg)
```
输入：root = [4,2,6,1,3]
输出：1
```


示例 2：
![img](../pic/783_bst2.jpg)
```
输入：root = [1,0,48,null,null,12,49]
输出：1
```

提示:
- 树中节点数目在范围 [2, 100] 内
- 0 <= Node.val <= $10^5$

# 我的解法
```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        val_list = []
        # 因为是二叉搜索树，所以中序遍历二叉树，生成节点的列表就是有序的
        def travel(root):
            if root is None:
                return
            travel(root.left)
            val_list.append(root.val)
            
            travel(root.right)
        travel(root)
        mins = float('inf')
        # 找出最小的差值
        for i,j in zip(val_list[0:-1],val_list[1:]):
            tmp = abs(i - j)
            if tmp < mins:
                mins = tmp
        return mins


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
    def minDiffInBST(self, root: TreeNode) -> int:
        # 中序遍历
        def dfs(root) :
            if not root : return None 
            dfs(root.left)
            # 比较最小值，当前值减去左子节点的值
            self.minval = min(self.minval,root.val-self.preval)
            self.preval = root.val
            dfs(root.right)
        self.minval = float('inf')
        self.preval = float('-inf')
        dfs(root)
        return self.minval

这个解法的优点：不需要分两步计算最小值，直接在遍历的时候，就将结果值计算出来。
```
