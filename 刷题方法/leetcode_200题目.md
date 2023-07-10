刷题
====

[toc]

# 第一周，链表、栈、队列

## 单链表定义

单向链表也叫单链表，是链表中最简单的一种形式，它的每个节点包含两个域，一个信息域（元素域）和一个链接域。这个链接指向链表中的下一个节点，而最后一个节点的链接域则指向一个空值。

```python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
```

##leetcode206
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
![img](./pic/leetcode206.jpg)

### 解题思路

在遍历链表时，将当前节点的 next\textit{next}next 指针改为指向前一个节点。由于节点没有引用其前一个节点，因此必须事先存储其前一个节点。在更改引用之前，还需要存储后一个节点。最后返回新的头引用。

### python

```python
class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            onext = curr.next
            curr.next = prev
            prev = curr
            curr = onext
        return prev
```

## leetcode160

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
![img](./pic/160_statement.png)

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

示例 1：
![img](./pic/160_example_1_1.png)

```angular2html
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
```

### 解题思路

一图胜千言，看图你就明白了

空间复杂度 O(1)O(1)O(1) 时间复杂度为 O(n)O(n)O(n)

这里使用图解的方式，解释比较巧妙的一种实现。

根据题目意思 如果两个链表相交，那么相交点之后的长度是相同的

我们需要做的事情是，让两个链表从同距离末尾同等距离的位置开始遍历。这个位置只能是较短链表的头结点位置。 为此，我们必须消除两个链表的长度差

指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
如果 pA 到了末尾，则 pA = headB 继续遍历
如果 pB 到了末尾，则 pB = headA 继续遍历
比较长的链表指针指向较短链表head时，长度差就消除了
如此，只需要将最短链表遍历两次即可找到位置
听着可能有点绕，看图最直观，链表的题目最适合看图了

![img](./pic/leetcode160.png)

### python

```python
class ListNode:
    def __init(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self,headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA
```

## leetcode21

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
![img](./pic/21_merge_ex1.jpg)

```angular2html
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

### 解题思路

当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

### python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list2:
            return list1
        if not list1:
            return list2
        ans = ListNode()
        #初始化
        if list1.val < list2.val:
            ans.val = list1.val
            list1 = list1.next
        else:
            ans.val = list2.val
            list2 = list2.next
        tmp = ans
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                tmp = tmp.next
                list1 = list1.next
            else:
                tmp.next = list2
                tmp = tmp.next
                list2 = list2.next
        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2
        return ans
```

### python2

```python
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next          
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next
```

## leetcode86 **分隔链表**

给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

示例1:
![img](./pic/86_partition.jpg)

```
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
```

### python(我的解法)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        new_head = None
        big_head = None
        big_node = None
        small_node = None
        curr = head
        while curr:
            if curr.val < x:
                if new_head is None:
                    new_head = curr
                    small_node = new_head
                else:
                    small_node.next = curr
                    small_node = small_node.next
            else:
                if big_head is None:
                    big_head = curr
                    big_node = big_head
                else:
                    big_node.next = curr
                    big_node = big_node.next
            curr = curr.next
        if big_node:
            big_node.next = None
        if small_node:
            small_node.next = None
            small_node.next = big_head
        return new_head if new_head else big_head
```

### python(参考解法)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        small = ListNode()
        small_head = small
        big = ListNode()
        big_head = big
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big.next = None
        small.next = big_head.next
        return small_head.next
```

## leetcode142 环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

示例1:
![img](./pic/142_circularlinkedlist.png)

```angular2html
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

###题解
这类链表题目一般都是使用双指针法解决的，例如寻找距离尾部第 K 个节点、寻找环入口、寻找公共尾部入口等。

算法流程：

1. 双指针第一次相遇： 设两指针 fast，slow 指向链表头部 head，fast 每轮走 2 步，slow 每轮走 1 步；
   
   a. 第一种结果： fast 指针走过链表末端，说明链表无环，直接返回 null；
   
   ```
   - TIPS: 若有环，两指针一定会相遇。因为每走 111 轮，fast 与 slow 的间距 +1+1+1，fast 终会追上 slow；
   ```
   
   b. 第二种结果： 当fast == slow时， 两指针在环中 第一次相遇 。下面分析此时fast 与 slow走过的 步数关系 ：
   
   - 设链表共有 a+b个节点，其中 链表头部到链表入口 有 aaa 个节点（不计链表入口节点）， 链表环 有 bbb 个节点（这里需要注意，aaa 和 bbb 是未知数，例如图解上链表 a=4, b=5）；设两指针分别走了 f，s 步，则有：
   - a. fast 走的步数是slow步数的 222 倍，即 f=2s；（解析： fast 每轮走 2 步）
   - fast 比 slow多走了 n个环的长度，即 f=s+nb；（ 解析： 双指针都走过 aaa 步，然后在环内绕圈直到重合，重合时 fast 比 slow 多走 环的长度整数倍 ）；
   - 以上两式相减得：f=2nb，s=nb，即fast和slow 指针分别走了2n，n个 环的周长 （注意： n是未知数，不同链表的情况不同）。
2. 目前情况分析：

如果让指针从链表头部一直向前走并统计步数k，那么所有 走到链表入口节点时的步数 是：k=a+nb（先走 a 步到入口节点，之后每绕 1圈环（ b步）都会再次到入口节点）。
而目前，slow 指针走过的步数为 nb 步。因此，我们只要想办法让 slow 再走 a步停下来，就可以到环的入口。
但是我们不知道 a的值，该怎么办？依然是使用双指针法。我们构建一个指针，此指针需要有以下性质：此指针和slow 一起向前走 a 步后，两者在入口节点重合。那么从哪里走到入口节点需要 a步？答案是链表头部head。

3. 双指针第二次相遇：

slow指针 位置不变 ，将fast指针重新 指向链表头部节点 ；slow和fast同时每轮向前走 1步；
TIPS：此时 f=0，s=nb；
当 fast 指针走到f=a步时，slow 指针走到步s=a+nb，此时 两指针重合，并同时指向链表环入口 。

4. 返回slow指针指向的节点。

### python（参考解法）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head,head
        while True:
            if not (fast and fast.next):
                return
            fast,slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast,slow = fast.next, slow.next
        return fast
```

## leetcode92 反转链表 II

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例1：
![img](./pic/92_rev2ex2.jpg)

```angular2html
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
```

### python（我的解法）

思路很简单：

1. 如果left == right,直接返回原来的链表即可；
2. 遍历链表，根据left和right的值，调换里面的节点顺序，主要需要注意，left从1开始编号，而且，如果left等于1的时候的边界处理情况;

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        i = 1
        prev = None
        curr = head
        while curr:
            if i == left:
                new_curr = curr
                new_prev = prev
                nex = curr.next
                curr.next = prev
                prev  = curr
                curr = nex
            elif i < right and i > left:
                nex = curr.next
                curr.next = prev
                prev  = curr
                curr = nex
            elif i == right:
                nex = curr.next
                curr.next = prev
                if new_prev:
                    new_prev.next = curr
                else:
                    head = curr
                new_curr.next = nex
                break
            
            else:
                prev = curr
                curr = curr.next
            
            i += 1
        return head
```

###参考思路
第 1 步：先将待反转的区域反转；

第 2 步：把 pre 的 next 指针指向反转以后的链表头节点，把反转以后的链表的尾节点的 next 指针指向 succ。

**因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论**
**dummy_node = ListNode(-1)**

### python(参考)

```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_linked_list(head: ListNode):
            # 也可以使用递归反转一个链表
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next

        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        # 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
        # 建议写在 for 循环里，语义清晰
        for _ in range(left - 1):
            pre = pre.next

        # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
        right_node = pre
        for _ in range(right - left + 1):
            right_node = right_node.next
        # 第 3 步：切断出一个子链表（截取链表）
        left_node = pre.next
        curr = right_node.next

        # 注意：切断链接
        pre.next = None
        right_node.next = None

        # 第 4 步：同第 206 题，反转链表的子区间
        reverse_linked_list(left_node)
        # 第 5 步：接回到原来的链表中
        pre.next = right_node
        left_node.next = curr
        return dummy_node.next
```

## leetcode138 复制带随机指针的链表

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

示例1:
![img](./pic/138_e1.png)

```angular2html
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

### 思路

本题要求我们对一个特殊的链表进行深拷贝。如果是普通链表，我们可以直接按照遍历的顺序创建链表节点。而本题中因为随机指针的存在，当我们拷贝节点时，「当前节点的随机指针指向的节点」可能还没创建，因此我们需要变换思路。一个可行方案是，我们利用回溯的方式，让每个节点的拷贝操作相互独立。对于当前节点，我们首先要进行拷贝，然后我们进行「当前节点的后继节点」和「当前节点的随机指针指向的节点」拷贝，拷贝完成后将创建的新节点的指针返回，即可完成当前节点的两指针的赋值。

具体地，我们用哈希表记录每一个节点对应新节点的创建情况。遍历该链表的过程中，我们检查「当前节点的后继节点」和「当前节点的随机指针指向的节点」的创建情况。如果这两个节点中的任何一个节点的新节点没有被创建，我们都立刻递归地进行创建。当我们拷贝完成，回溯到当前层时，我们即可完成当前节点的指针赋值。注意一个节点可能被多个其他节点指向，因此我们可能递归地多次尝试拷贝某个节点，为了防止重复拷贝，我们需要首先检查当前节点是否被拷贝过，如果已经拷贝过，我们可以直接从哈希表中取出拷贝后的节点的指针并返回即可。

在实际代码中，我们需要特别判断给定节点为空节点的情况。

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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dic = {}
        def get_new_list(nod):
            if not nod:
                return None
            if nod not in node_dic:
                nod_new = Node(nod.val)
                node_dic[nod] = nod_new
                nod_new.next = get_new_list(nod.next)
                nod_new.random = get_new_list(nod.random)
            return node_dic[nod]
        return get_new_list(head)
```

## 栈的基础知识

堆栈（Stack）：简称为栈。一种线性表数据结构，是一种只允许在表的一端进行插入和删除操作的线性表。
我们把栈中允许插入和删除的一端称为 「栈顶（top）」；另一端则称为 「栈底（bottom）」。当表中没有任何数据元素时，称之为 「空栈」。

栈的基本性质：先进后出。

## leetcode20 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：

```angular2html
输入：s = "()"
输出：true
```

### 思路

栈先入后出特点恰好与本题括号排序特点一致，即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，则遍历完所有括号后 stack 仍然为空；

建立哈希表 dic 构建左右括号对应关系：keykeykey 左括号，valuevaluevalue 右括号；这样查询 222 个括号是否对应只需 O(1)O(1)O(1) 时间复杂度；建立栈 stack，遍历字符串 s 并按照算法流程一一判断。

### python（参考解法）

```python
class Solution:
    def isValid(selfself, s):
        dic = {'{':'}','[':']','(':')','?':'?'}
        stack = ['?']
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if dic[stack.pop()] != i:
                    return False
        return True
```

## leetcode 224 基本计算器

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例1：

```angular2html
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
```

### 解题思路

由于字符串除了数字与括号外，只有加号和减号两种运算符。因此，如果展开表达式中所有的括号，则得到的新表达式中，数字本身不会发生变化，只是每个数字前面的符号会发生变化。

因此，我们考虑使用一个取值为 {−1,+1}的整数 sign代表「当前」的符号。根据括号表达式的性质，它的取值：

与字符串中当前位置的运算符有关；
如果当前位置处于一系列括号之内，则也与这些括号前面的运算符有关：每当遇到一个以 −-− 号开头的括号，则意味着此后的符号都要被「翻转」。
考虑到第二点，我们需要维护一个栈 ops，其中栈顶元素记录了当前位置所处的每个括号所「共同形成」的符号。例如，对于字符串 1+2+(3-(4+5))：

扫描到 1+2时，由于当前位置没有被任何括号所包含，则栈顶元素为初始值 +1；
扫描到 1+2+(3时，当前位置被一个括号所包含，该括号前面的符号为+号，因此栈顶元素依然 +1；
扫描到 1+2+(3-(4时，当前位置被两个括号所包含，分别对应着+号和−号，由于 +号和−号合并的结果为−号，因此栈顶元素变为−1。
在得到栈 ops之后，sign的取值就能够确定了：如果当前遇到了+号，则更新 sign←ops.top()；如果遇到了遇到了−号，则更新 sign←−ops.top()。

然后，每当遇到 (时，都要将当前的 sign取值压入栈中；每当遇到)时，都从栈中弹出一个元素。这样，我们能够在扫描字符串的时候，即时地更新 ops中的元素。

### python(参考解法)

```python
class Solution:
    def calculate(self, s):
        opt = [1]
        sign = 1
        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = opt[-1]
                i += 1
            elif s[i] == '-':
                sign = -opt[-1]
                i += 1
            elif s[i] == '(':
                opt.append(sign)
                i += 1
            elif s[i] == ')':
                opt.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ret += num * sign
        return ret
```

## leetcode155 最小栈

设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

- MinStack() 初始化堆栈对象。
- void push(int val) 将元素val推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。

示例1:

```angular2html
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

### python(我的解法)

思路：按照栈的方式，存储即可，主要是存储最小值，在pop的时候，需要更新最小值。

```python
class MinStack:

    def __init__(self):
        self.stock = []
        self.min = 2**31


    def push(self, val: int) -> None:
        self.stock.append(val)
        if val < self.min:
            self.min = val


    def pop(self) -> None:
        val = self.stock.pop()
        self.min = min(self.stock) if len(self.stock) > 0 else 2**31
        return val


    def top(self) -> int:
        return self.stock[-1]


    def getMin(self) -> int:
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### 参考思路

我们只需要设计一个数据结构，使得每个元素 a 与其相应的最小值 m 时刻保持一一对应。因此我们可以使用一个辅助栈，与元素栈同步插入与删除，用于存储与每个元素对应的最小值。

- 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
- 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
- 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中。

```python
class MinStack:

    def __init__(self):
        self.stock = []
        self.min_stack = [math.inf]


    def push(self, val: int) -> None:
        self.stock.append(val)
        self.min_stack.append(min(val,self.min_stack[-1]))

    def pop(self) -> None:
        self.stock.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stock[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## leetcode946 验证栈序列

给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

示例1:

```angular2html
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

###参考思路
这道题需要利用给定的两个数组 pushed和 popped的如下性质：

数组 pushed中的元素互不相同；

数组 popped和数组pushed的长度相同；

数组 popped是数组 pushed的一个排列。

根据上述性质，可以得到如下结论：

栈内不可能出现重复元素；

如果 pushed和popped是有效的栈操作序列，则经过所有的入栈和出栈操作之后，每个元素各入栈和出栈一次，栈为空。

因此，可以遍历两个数组，模拟入栈和出栈操作，判断两个数组是否为有效的栈操作序列。

模拟入栈操作可以通过遍历数组 pushed实现。由于只有栈顶的元素可以出栈，因此模拟出栈操作需要判断栈顶元素是否与 popped的当前元素相同，如果相同则将栈顶元素出栈。由于元素互不相同，因此当栈顶元素与 popped的当前元素相同时必须将栈顶元素出栈，否则出栈顺序一定不等于 popped。

根据上述分析，验证栈序列的模拟做法如下：

遍历数组 pushed，将 pushed的每个元素依次入栈；

每次将 pushed的元素入栈之后，如果栈不为空且栈顶元素与 popped的当前元素相同，则将栈顶元素出栈，同时遍历数组 popped，直到栈为空或栈顶元素与 popped的当前元素不同。

遍历数组 pushed结束之后，每个元素都按照数组 pushed的顺序入栈一次。
如果栈为空，则每个元素都按照数组 popped的顺序出栈，返回 true。如果栈不为空，则元素不能按照数组 popped的顺序出栈，返回 false。

### python(参考解法)

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        j = 0
        for i in pushed:
            st.append(i)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return len(st) == 0
```

## leetcode 739每日温度

给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例1:

```angular2html
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```

### 参考思路

可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。

正向遍历温度列表。对于温度列表中的每个元素 temperatures[i]，如果栈为空，则直接将 i 进栈，如果栈不为空，则比较栈顶元素 prevIndex 对应的温度 temperatures[prevIndex] 和当前温度 temperatures[i]，如果 temperatures[i] > temperatures[prevIndex]，则将 prevIndex 移除，并将 prevIndex 对应的等待天数赋为 i - prevIndex，重复上述操作直到栈为空或者栈顶元素对应的温度小于等于当前温度，然后将 i 进栈。

为什么可以在弹栈的时候更新 ans[prevIndex] 呢？因为在这种情况下，即将进栈的 i 对应的 temperatures[i] 一定是 temperatures[prevIndex] 右边第一个比它大的元素，试想如果 prevIndex 和 i 有比它大的元素，假设下标为 j，那么 prevIndex 一定会在下标 j 的那一轮被弹掉。

由于单调栈满足从栈底到栈顶元素对应的温度递减，因此每次有元素进栈时，会将温度更低的元素全部移除，并更新出栈元素对应的等待天数，这样可以确保等待天数一定是最小的。

### python(参考)

```python
class Solution:
    def dailyTemperature(self, temperatures):
        stack = []
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                ans[pre] = i - pre
            stack.append(i)
        return ans
```

## leetcode42 接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例1:
![img](./pic/42_rainwatertrap.png)

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

### 解题思路

除了计算并存储每个位置两边的最大高度以外，也可以用单调栈计算能接的雨水总量。

维护一个单调栈，单调栈存储的是下标，满足从栈底到栈顶的下标对应的数组 height中的元素递减。

从左到右遍历数组，遍历到下标 i 时，如果栈内至少有两个元素，记栈顶元素为 top 的下面一个元素是left，则一定有 height[left]≥height[top]。如果 height[i]>height[top]，则得到一个可以接雨水的区域，该区域的宽度是 i−left−1，高度是 min⁡(height[left],height[i])−height[top]，根据宽度和高度即可计算得到该区域能接的雨水量。

为了得到 left，需要将top出栈。在对top计算能接的雨水量之后，left变成新的top，重复上述操作，直到栈变为空，或者栈顶下标对应的 height中的元素大于或等于height[i]。

在对下标 i 处计算能接的雨水量之后，将i入栈，继续遍历后面的下标，计算能接的雨水量。遍历结束之后即可得到能接的雨水总量。

### python(参考)
```python
class Solution:
    def trap(self, height):
        stack = []
        ans = 0
        n = len(height)
        for i,h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                weight = i - left - 1
                curheight = min(h, height[left]) - height[top]
                ans += weight * curheight
            stack.append(i)
        return ans
```



# 参考文献

1. https://jackkuo666.github.io/Data_Structure_with_Python_book/chapter3/section1.html
2. https://github.com/itcharge/LeetCode-Py
3. https://algo.itcharge.cn/03.Stack/01.Stack-Basic/01.Stack-Basic/

