# Combination & Permutation

## Combination

排列组合问题基础模版：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        end = len(nums)
        def dfs(nums, path, res):
            if len(path) == end:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        dfs(nums, [], res)
        return res
```

### 555. Split Concatenated Strings



### 

### 680. Split String

{% embed url="https://www.lintcode.com/problem/split-string/description?\_from=ladder&&fromId=1" %}

```python
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def __init__(self):
        self.combination = dict()

    def explore(self, s):
        if len(s) == 1:
            return [[s]]
        elif len(s) == 0:
            return [[]]
        elif len(s) in self.combination.keys():
            return self.combination[len(s)]
        takeOne = [[s[0]]+w for w in self.explore(s[1:])]
        if len(s) >= 2:
            takeTwo = [[s[:2]]+w for w in self.explore(s[2:])]
        else:
            takeTwo = []
        curRes = takeOne+takeTwo
        self.combination[len(s)] = curRes
        return curRes
        
    def splitString(self, s):
        # write your code here
        return self.explore(s)
```

