# May 18th

## 567. Permutation in String

{% embed url="https://leetcode.com/problems/permutation-in-string/" %}

#### 思路一：

判断s2里面是否有s1的permutation，第一反应是遍历s1的permutation，每个都判断一下是不是在s2存在，如果存在就True，不存在继续。提交发现超时，反思：如果结果是都不存在，这个方法会遍历s1的所有permutation，时间复杂度的确不友好。

代码也存一下。

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def dfs(app, path):
            if len(path) <= len(s1):
                if len(path) == len(s1) and path in s2:
                    return True
                for i in range(len(app)):
                    p = dfs(app[:i]+app[i+1:], path+app[i])
                    if p: return p
                return False
        return dfs(s1, '')
```

#### 思路二：

s1的permutation肯定是 **连续的** 长度为len\(s1\)的字符串，可以直接在s2里面sliding window，window里面的字符串有跟s1一样的frequency就肯定与它的某个permutation相同。

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = dict()
        for char in s1:
            if (char not in freq1.keys()):
                freq1[char] = 0  
            else:
                freq1[char] += 1
        for i in range(len(s2)-len(s1)+1):
            compare = s2[i:i+len(s1)]
            freq2 = dict()
            for char in compare:
                if (char not in freq2.keys()):
                    freq2[char] = 0  
                else:
                    freq2[char] += 1
            if freq2 == freq1:
                return True
        return False
        
```

#### 思路二 follow up​

每个window都重新算freq有点慢，可以直接更新维护同一个freq dict

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2 = [0 for _ in range(26)], [0 for _ in range(26)]
        for char in s1:
            freq1[ord(char)-97] += 1
        
        r = 0
        while r < len(s2):
            freq2[ord(s2[r])-97] += 1
            
            if r >= len(s1):
                freq2[ord(s2[r-len(s1)])-97] -= 1            
            
            if freq2 == freq1:
                return True
            
            r += 1
            
        return False
```

## 756. Multiply Two Numbers

{% embed url="https://www.lintcode.com/problem/multiply-two-numbers/description" %}

```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        def decode(linkedList):
            digit = linkedList
            num = 0
            while digit:
                num *= 10
                num += digit.val
                digit = digit.next
            return num
        sumNum = decode(l1) * decode(l2)
        return sumNum
```

