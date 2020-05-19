# May 16th

## 333. Largest BST Subtree

{% embed url="https://leetcode.com/problems/largest-bst-subtree/" %}

粗暴点就是递归验证每个node下面是不是BST，利用BST的特性，传递val的大小限制即可。

要求O\(n\)解决问题，就只能：

1. 遍历常数次
2. 需要从叶节点往上传递val大小限制
3. 发现当前node不符合BST，就把当前size归零，继续遍历
4. 随时记录得到的最大size

还是有点像DFS。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # 记录最大的 subtree size
        self.maxSize = 0
        
    def explore(self, subRoot):
        # 到叶节点再往下就停住，返回一个不可能大于的min，和一个不可能小于的max.
        if subRoot == None:
            return (0, float('inf'), float('-inf'))
        # 得到两个 subtree 各自的size和val大小限制
        leftSize, leftMin, leftMax = self.explore(subRoot.left)
        rightSize, rightMin, rightMax = self.explore(subRoot.right)
        #print("--------")
        #print("[SubRoot]:", subRoot.val)
        #print("leftMax:", leftMax, "| rightMin", rightMin)
        #print("--------")
        # 如果当前节点仍然可以是 subtree 的一部分：
        if (subRoot.val > leftMax) and (subRoot.val < rightMin):
            # 计算继承的 subtree size
            inheritSize = leftSize+rightSize+1
            # 更新最大size
            self.maxSize = max(self.maxSize, inheritSize)
            return (inheritSize, min(leftMin, rightMin, subRoot.val), max(leftMax, rightMax, subRoot.val))
        # 如果当前节点断开了 BST subtree, size归零，同时返回一定可以继续的大小限制
        else:
            return (0, float('-inf'), float('inf'))
        
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.explore(root)
        return self.maxSize
```

## 513. Find Bottom Left Tree Value

{% embed url="https://leetcode.com/problems/find-bottom-left-tree-value/" %}

DFS遍历，左侧优先，记录当前深度和最大深度，当前深度&gt;最大深度的时候，记录所在node的值。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bottomLeft = 0
        self.maxRow = -1
        
    def dig(self, root, row):
        # 挖到底，停下
        if not root: 
            return
        # 没到底的话，先挖左边（优先最左边的值）
        self.dig(root.left, row + 1)
        # 如果挖的过程里最大深度被更新了，就同时用root更新 leftmost value
        if row > self.maxRow:
            self.maxRow = row
            self.bottomLeft = root.val
        # 左边挖到最底了，再回来挖右边
        self.dig(root.right, row + 1)
        
    def findBottomLeftValue(self, root):      
        self.dig(root, 0)
        return self.bottomLeft
```

