# 99. Recover Binary Search Tree

{% embed url="https://leetcode.com/problems/recover-binary-search-tree/" %}

问题拆解成：

1. 找到是哪两个值被swap了
2. 操作`tree`来swap这两个值进行复位

直接在tree上确认两个值比较困难，因为可能其中一个值的位置本身并不违反`BST`的性质（example 2 中的 2），所以考虑把BST `inorder`遍历成`sorted array`来找这两个值。

复位过程很简单，`recursive`找这两个需要swap的值就可以。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, traversal):
            if not root: return
            inorder(root.left, traversal)
            traversal.append(root.val)
            inorder(root.right, traversal)
        
        array = []
        inorder(root, array)
        
        # 找到被swap的两个值
        swapped = []
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                ## 第一个确定的肯定就是两个中的较大值
                ## 但另一个值需要一直更新
                if not swapped: swapped = [array[i], array[i+1]]
                swapped[1] = array[i+1]
        
        # 复原
        def swap(root, x, y, count = 2):
            if root:
                if root.val == x:
                    root.val = y
                    count -= 1
                elif root.val == y:
                    root.val = x
                    count -= 1
                if not count: return
                # 没找到就继续 recursive
                swap(root.left, x, y, count)
                swap(root.right, x, y, count)
        
        swap(root, swapped[0], swapped[1])
```

