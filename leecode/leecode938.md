# 938. 二叉搜索树的范围和
地址: https://leetcode-cn.com/problems/range-sum-of-bst/

# 题目描述
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

示例1：
![img](../pic/938_1.jpg)
```
输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32

```

示例2：
![img](../pic/938_2.jpg)
```
输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23

```
提示：
- 树中节点数目在范围 [1, 2 * $10^4$] 内
- 1 <= Node.val <= $10^5$
- 1 <= low <= high <= $10^5$
- 所有 Node.val 互不相同


# 我的解法
``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sums = 0
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            if low <= root.val <= high:
                self.sums += root.val
            inorder(root.right)
        inorder(root)
        return self.sums


```

# 参考解法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif L > node.val:
                    dfs(node.right)
                else:
                    dfs(node.left)
        self.ans = 0
        dfs(root)
        return self.ans

```