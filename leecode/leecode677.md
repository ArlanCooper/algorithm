# 677. 键值映射
地址:https://leetcode-cn.com/problems/map-sum-pairs/

# 题目描述
实现一个 MapSum 类，支持两个方法，insert 和 sum：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

示例
```
输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

```

提示：

- 1 <= key.length, prefix.length <= 50
- key 和 prefix 仅由小写英文字母组成
- 1 <= val <= 1000
- 最多调用 50 次 insert 和 sum

# 我的解法
```python

class MapSum:

    def __init__(self):
        self.dics = {}


    def insert(self, key: str, val: int) -> None:
        self.dics[key] = val


    def sum(self, prefix: str) -> int:
        ans = 0
        for key in self.dics:
            if key.startswith(prefix):
                ans += self.dics[key]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

# 参考解法
## 思路
前缀树

```python
class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0            
            node = node.next[ord(c) - ord('a')]
        return node.val



```