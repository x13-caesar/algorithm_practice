# May 12th

## 258. Add Digits

The result slides repeatedly from 1 to 9, and when &lt;num&gt; is able to be rounded by 9, the result is &lt;9&gt; \(e.g. input 36, 45, 54...\). Thus, we can get the result by calculating the remainder of the division by 9.

Special case: the output could be 0 only if the input is 0.

```python
#python solution

class Solution:
    def addDigits(self, num: int) -> int:
        res = num % 9
        if res == 0:
            if num == 0:
                return 0
            else:
                return 9
        else:
            return res
```

## 235. Lowest Common Ancestor of a Binary Search Tree

Recursively search the subtrees, return current root node till both of p and q have been found in subtrees.

```python
#python solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # 设置一个 map 来记录 p/q 是否已经被找到
        self.record={}
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.record={p:False,q:False}
        # [1] 如果 root 是 p/q 中的一个，就算找到了，不继续搜索了
        if any((not root, root == p, root == q)): 
            if root: # 记录找到了 p/q
                self.record[root]=True
            return root
        # 如果不是，再往下搜索 l/r 两个subtrees，这边会 recursively 地往下找，直到触发[1][2][3]开始朝上return
        l = self.lowestCommonAncestor(root.left, p, q)
        # 要是 p/q 都已经在 l 里面找到了，就不需要再搜索 r 了，直接返回 l
        if self.record[p] and self.record[q]:
            return l    
        else:
            r = self.lowestCommonAncestor(root.right, p, q)
            # [2] 如果 l/r 中有至少一个没找到 p/q 的存在：
            if (not l) or (not r): 
                # return 有 p/q 存在的那个
                # 如果 l/r 里都没找到， return null值（说明往下的subtree里都没有）
                return l if l else r
            # [3] 能运行到这里说明 l/r 两个 subtrees 都有找到 p/q 中的其中一个
            # 那 LCA 就是我们目前的 root
            return root
```

solution 2: 

Take advantage of the properties of the binary search tree:

```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return
        # 如果 p,q 都大于 root， 则他们都会在 root 的右分支
        if root.val < p.val and root.val < q.vaL:
            return self.lowestCommanAncester(root.right, p, q)
        # 如果 p,q 都小于 root， 则他们都会在 root 的左分支
        if root.val > p.val and root.val > q.val:
            return self.lowestCommanAncester(root.right, p, q)
        # 如果 p,q 一个大于 root 一个小于 root，则 LCA 就在 root上
        return root
```



