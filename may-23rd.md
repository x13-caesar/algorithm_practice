# May 23rd

## 76. Minimum Window Substring

{% embed url="https://leetcode.com/problems/minimum-window-substring/" %}

在S中找包含T的substring，暴力搜索没法把时间复杂度控制在O\(n\)，还是sliding window，跟 [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) 相比只是变成了window跟T的比较，而非检查重复。所以基本上还是移动左右指针 i, j 然后检查 window.

这边有个优化，就是可以不用滑过整个S，只需要把S里面出现的T元素挑出来，然后用window左右边界跳跃式地滑在这些元素上，没出现在T里面的元素，可以直接跳过不看。

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 这一块是获取T中元素在S的位置，接下来只检查这些位置的window就可以
        freqT = Counter(t)
        path = []
        for n, ch in enumerate(s):
            if ch in freqT.keys():
                path.append((ch, n))
        
        window = {}
        match = 0
        res = s+" " # 加个字符以防最终解是整个s
        
        i, j = 0, 0
        while j < len(path):
            
            edge = path[j][0]
            window[edge] = window.get(edge, 0) + 1
            # edge字符的频率符合要求时，match+1
            if window[edge] == freqT[edge]: match += 1
            
            # 当match数量等于T中独特字符的数量，i.e. 当前window和T的字符频率分布相同
            while i <= j and match == len(freqT):
                temp = s[path[i][1]:path[j][1]+1]
                # 比记录的解更短的话，就更新
                if len(temp) <= len(res): res = temp
                
                # 移动左指针之前，左边界的字符频率要调整
                edge = path[i][0]
                window[edge] -= 1
                if window[edge] < freqT[edge]: match -= 1
                # 左指针
                i += 1
                
            j += 1
            
        return "" if len(res)>len(s) else res
```

## 30. Substring with Concatenation of All Words

{% embed url="https://leetcode.com/problems/substring-with-concatenation-of-all-words/" %}

跟昨天的 [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) 基本上是一道题，character换成了word而已。

```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        res = []
        freqT = Counter(words)
        lenW = len(words[0])
        lenT = lenW*len(words)
        for i in range(len(s)-lenT+1):
            window = s[i:i+lenT]
            freqW = dict()
            for j in range(0, len(window), lenW):
                word = window[j:j+lenW]
                if word not in freqT: break
                else:
                    freqW[word] = freqW.get(word, 0) + 1
            if freqW == freqT:
                res.append(i)
        return res
```

