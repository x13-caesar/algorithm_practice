# May 27th

## 199. Binary Tree Right Side View

{% embed url="https://leetcode.com/problems/binary-tree-right-side-view/" %}

DFS 先把最右边的那些node加进去，然后再依序往左边找，确保遍历所有level

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, result, level):
        if not root: return
        # 确保只有新到的level会加值进result里面
        if level == len(result): result.append(root.val)
        # 先traverse右边，确保右子树的都加进去
        self.dfs(root.right, result, level+1)
        # 再左边，寻找遗漏的
        self.dfs(root.left, result, level+1)
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res, 0)
        return res
```

也可以 BFS 做，基本就是使用queue做层序遍历，每层都先把当层node的子节点加进queue里面，（这题需要把最右侧node记录下来），下一轮再把queue里的节点进行同样的操作。

```python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
    
        res, queue = [], []
        if not root: return res
        queue.append(root)
        
        while queue:
            level = len(queue)
            # 
            res.append(queue[-1].val)
            for i in range(level):
                curNode = queue.pop(0)
                if curNode.left: queue.append(curNode.left)
                if curNode.right: queue.append(curNode.right)
        return res
```

## 155. Min Stack

{% embed url="https://leetcode.com/problems/min-stack/" %}

考验数据结构理解的时候到了...

偷懒直接双stack了，一个用来依序存当前最小值。

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if self.stack == []:
            self.min.append(x)
        else:
            self.min.append(min(x, self.min[-1]))
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```



