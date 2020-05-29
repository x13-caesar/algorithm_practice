# May 28th

## 606. Construct String from Binary Tree

{% embed url="https://leetcode.com/problems/construct-string-from-binary-tree/" %}

二叉树遍历，第一反应递归。

本身 **not t** 这个跳出条件很明显，需要多考虑的是：

> The null node needs to be represented by empty parenthesis pair "\(\)". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

所以search左子树之后，要先确认是否符合「左子树空，右子树非空」的情况，符合的话直接添加\(\)占位，再search右子树。而右子树不需要进行这个确认，因为它空也不需要占位。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ""
        res = str(t.val)
        if t.left: res+="(" + self.tree2str(t.left) + ")"
        if not t.left and t.right: res+="()"    
        if t.right: res+="(" + self.tree2str(t.right) + ")"
        return res
```

要省空间的话可以用stack来写，O\(n\)的空间复杂度。

```python
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        res = ""
        stack = [t]
        visited = []
        while stack:
            cur = stack[-1]
            if cur in visited:
                stack.pop()
                res += ")"
            else:
                visited.append(cur)
                res += "("+str(cur.val)
                if (not cur.left) and cur.right: res += "()"
                if cur.right: stack.append(cur.right)
                if cur.left: stack.append(cur.left)
        return res[1:len(res)-1]
```

## 617. Merge Two Binary Trees

{% embed url="https://leetcode.com/problems/merge-two-binary-trees/" %}

还是递归遍历，只不过同时遍历两个tree，结束条件是其中一个树遍历到叶子了，这时候接下来的subtree就可以直接拿另外一个树的来用。

```python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if not t2: return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
```

