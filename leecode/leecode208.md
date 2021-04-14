# 208. 实现 Trie (前缀树)
地址: https://leetcode-cn.com/problems/implement-trie-prefix-tree/


# 题目描述

Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

- Trie() 初始化前缀树对象。
- void insert(String word) 向前缀树中插入字符串 word 。
- boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
- boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。

示例：
```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

提示:
- 1 <= word.length, prefix.length <= 2000
- word 和 prefix 仅由小写英文字母组成
- insert、search 和 startsWith 调用次数 总计 不超过 3 * $10^4$ 次


# 我的解法
```python
'''
使用集合的方式存储数据，时间复杂度比较高，空间占有率低
执行用时：
1672 ms, 在所有 Python3 提交中击败了5.01%的用户
内存消耗：
21.5 MB, 在所有 Python3 提交中击败了94.08%的用户

'''

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_set = set() #初始化成集合


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.val_set.add(word) #添加元素


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.val_set:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        lens = len(prefix)
        tmp_set = {i[0:lens] for i in self.val_set}
        if prefix in tmp_set:
            return True
        else:
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


```


# 参考解法
## 官方解题思路
Trie，又称前缀树或字典树，是一棵有根树，其每个节点包含以下字段：

- 指向子节点的指针数组 children。对于本题而言，数组长度为 26，即小写英文字母的数量。此时 children[0] 对应小写字母 a，children[1] 对应小写字母 b，…，children[25] 对应小写字母 z。
- 布尔字段 isEnd，表示该节点是否为字符串的结尾。

插入字符串

我们从字典树的根开始，插入字符串。对于当前字符对应的子节点，有两种情况：

- 子节点存在。沿着指针移动到子节点，继续处理下一个字符。
- 子节点不存在。创建一个新的子节点，记录在 children 数组的对应位置上，然后沿着指针移动到子节点，继续搜索下一个字符。

重复以上步骤，直到处理字符串的最后一个字符，然后将当前节点标记为字符串的结尾。

查找前缀

我们从字典树的根开始，查找前缀。对于当前字符对应的子节点，有两种情况：

- 子节点存在。沿着指针移动到子节点，继续搜索下一个字符。
- 子节点不存在。说明字典树中不包含该前缀，返回空指针。

重复以上步骤，直到返回空指针或搜索完前缀的最后一个字符。

若搜索到了前缀的末尾，就说明字典树中存在该前缀。此外，若前缀末尾对应节点的 isEnd 为真，则说明字典树中存在该字符串。


```python
'''



'''


class Trie:
    def __init__(self):
        # 每个节点给26个子节点，因为只有小写字母
        self.children = [None] * 26
        self.isEnd = False # 默认不为叶子结点，也就是不存在
    
    def searchPrefix(self, prefix: str) -> "Trie":
        # 查找前缀
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        # 插入字符串
        node = self
        for ch in word:
            ch = ord(ch) - ord("a") #转换成索引
            if not node.children[ch]: # 如果该子节点不存在，则进行添加
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True #最后的叶子结点是存在的

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None


```

## 效率最高解题方法
```python

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree=self.lookup
        for n in word:
            if not n in tree:
                tree[n]={}
            tree=tree[n]
        tree["#"]="#"


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree=self.lookup
        for n in word:
            if not n in tree:
                return False
            tree=tree[n]
        
        if("#" in tree):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree=self.lookup
        for n in prefix:
            if not n in tree:
                return False
            tree=tree[n]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```
