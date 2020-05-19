# May 19th

## 139. Word Break

{% embed url="https://leetcode.com/problems/word-break/" %}

#### 思路一：直接 DFS 枚举 wordDict 的所有permutation, 遇到等于s的就返回True

太慢， time limit exceeded

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        limit = len(s)
        def dfs(words, path):
            if path == s:
                return True
            elif len(path) < limit:
                for i in range(len(words)):
                    judge = dfs(words, path+words[i])
                    if judge:
                        return True
            else:
                return False
        return dfs(wordDict, '')
```

#### 思路二：遍历 s ，在 wordDict 中搜索

节约重复计算，用 record 去记录已经算过的 sub-problem \(**Recursion with memoization** 记忆化搜索\)

```python
class Solution(object):
    def wordBreak(self, s, wordDict)
        record = {} #记录搜索过的sub-problem
        def segement(s):
            if s in record: return record[s]
            if s in wordDict: 
                record[s] = True
                return True
            
            for i in range(1, len(s)):
            #从当前string最左开始
                r = s[:i]
                # 如果s[:i]在wordDict里面，且后面的部分也可以被分割
                # 那整个当前string就可以分割
                if r in wordDict and segement(s[i:]):
                    record[s] = True
                    return True
            
            record[s] = False
            return False
            
        return segement(s)
```

## 120. Triangle

{% embed url="https://leetcode.com/problems/triangle/submissions/" %}

核心思路：到达当前点的最小路径由到达上方两个点的最小路径决定，不考虑 edge case 的话，状态转移方程是：

```python
minPath[i][j] = min(minPath[i-1][j], minPath[i-1][j-1]) + triangle[i][j]
```

到达当前点 \(i, j\) 的最小路径等于：到达上方两个点 \(i-1, j\) \(i-1, j-1\) 的最小路径，加上 \(i, j\) 的值本身。

每个点的最小路径都存储的话，会要O\(n\*\*2/2\) 的空间，题目要求 O\(n\) 的额外空间，可以考虑直接 inplace 操作，我们是按顺序（上-&gt;下，左-&gt;右）遍历的，直接用 minPath 替换掉原 triangle 的值，这样应该是 O\(1\).

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 从1开始，第0行的最小路径是它值本身，不用更新
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # edge case 1
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                # edge case 2
                elif j == len(triangle[i])-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
        return min(triangle[len(triangle)-1])
```

看了下别人的解，直接滚动保存前一行数据，也可以实现 O\(n\) 复杂度，也避免了 inplace 操作。

