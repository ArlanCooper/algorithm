# 138. 复制带随机指针的链表
地址: https://leetcode-cn.com/problems/copy-list-with-random-pointer/


# 题目描述
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。


示例1
```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

```


示例2
```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

```


示例3
```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

```

示例4
```
输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
```

# 我的解法
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        import copy
        res = copy.deepcopy(head)

        return res

```


# 最优解法
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic, prev, node = {}, None, head
        while node:
            if node not in dic:
                dic[node] = Node(node.val, node.next, node.random)
            if prev:
                prev.next = dic[node]
            else:
                head = dic[node]
            if node.random:
                if node.random not in dic:
                    dic[node.random] = Node(node.random.val, node.random.next, node.random.random)
                dic[node].random = dic[node.random]
            prev, node = dic[node], node.next
        return head
        


```
