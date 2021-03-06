# May 11th

## 189. Rotate Array

```python
# python solution 1:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            s = nums.pop(-1)
            nums.insert(0, s)
```

## 387. First Unique Character in a String

{% embed url="https://leetcode.com/problems/first-unique-character-in-a-string/" %}



```python
# python solution 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_count = 0
        repeat = []
        while s:
            if s[0] in repeat:
                pass
            elif s.count(s[0]) > 1:
                repeat.append(s[0])
            else:
                return index_count
            s = s[1:]
            index_count += 1
        return -1

# solution 2:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for index, l in enumerate(s):
            if count[l] == 1:
                return index
        return -1
        
# solution 3 - O(1) space:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        S = 'abcdefghijklmnopqrstuvwxyz'
        indices = [s.index(c) for c in S if s.count(c) == 1]
        return min(indices) if indices else -1
```

