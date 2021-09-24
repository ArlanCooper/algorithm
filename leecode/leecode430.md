# 430. 扁平化多级双向链表
地址:https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/


# 题目描述
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。

示例1
```
输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：

输入的多级列表如下图所示：

```
![img](../pic/430_1.png)
扁平化后的链表如下图：
![img](../pic/430_12.png)


示例2
```
输入：head = [1,2,null,3]
输出：[1,3,2]
解释：

输入的多级列表如下图所示：

  1---2---NULL
  |
  3---NULL


```

示例3
```
输入：head = []
输出：[]

```


如何表示测试用例中的多级链表？
以 示例 1 为例：
```
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL


```

序列化其中的每一级之后：
```
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]


```

为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。
```
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

```

合并所有序列化结果，并去除末尾的 null 。
```
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```

# 我的解法
没有写出来，针对链表，确实有点害怕


# 参考解法
## 思路
深度优先遍历
当我们遍历到某个节点 \textit{node}node 时，如果它的 \textit{child}child 成员不为空，那么我们需要将 \textit{child}child 指向的链表结构进行扁平化，并且插入 \textit{node}node 与 \textit{node}node 的下一个节点之间。

因此，我们在遇到 child 成员不为空的节点时，就要先去处理 child 指向的链表结构，这就是一个「深度优先搜索」的过程。当我们完成了对 child 指向的链表结构的扁平化之后，就可以「回溯」到 node 节点。

为了能够将扁平化的链表插入 node 与 node 的下一个节点之间，我们需要知道扁平化的链表的最后一个节点 last，随后进行如下的三步操作：

- 将 node 与 node 的下一个节点 next 断开：

- 将 node 与 child 相连；

- 将 last 与 next 相连。

这样一来，我们就可以将扁平化的链表成功地插入。
![img](../pic/430_2.png)

```python

class Solution:
    def flatten(self, head: "Node") -> "Node":
        def dfs(node: "Node") -> "Node":
            cur = node
            # 记录链表的最后一个节点
            last = None
            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    child_last = dfs(cur.child)
                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last
        dfs(head)
        return head

```


