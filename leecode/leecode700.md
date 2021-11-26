# 700. 二叉搜索树中的搜索
地址:https://leetcode-cn.com/problems/search-in-a-binary-search-tree/


# 题目描述
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
例如，
```
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2

```

你应该返回如下子树:
```
      2     
     / \   
    1   3

```

在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。



# 我的解法
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(root,val):
            if not root:
                return None
            if root.val == val:
                return root
            a = dfs(root.left,val)
            b = dfs(root.right,val)
            if a:
                return a
            else:
                return b
        
        return dfs(root,val)



```

# 参考解法

##思路
题目说了是二叉搜索树

```python
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            root = root.left if val < root.val else root.right
        return None
```
