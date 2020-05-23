# May 22th

## 438. Find All Anagrams in a String

{% embed url="https://leetcode.com/problems/find-all-anagrams-in-a-string/" %}

基本上是 Sliding window

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freqS, freqP= [0 for _ in range(26)], [0 for _ in range(26)]
        res = []
        for ch in p:
            freqP[ord(ch)-97] += 1
        for i in range(len(s)):
            if i >= len(p):
                freqS[ord(s[i-len(p)])-97] -= 1
            freqS[ord(s[i])-97] += 1
            if freqS == freqP:
                # print("Get anagrams:", s[i-len(p)+1:i+1])
                res.append(i+1-len(p))
                
        return res
```

## 3. Longest Substring Without Repeating Characters

{% embed url="https://leetcode.com/problems/longest-substring-without-repeating-characters/" %}

类似 sliding window，移动window右边界，检查边界字符是否与目前substring中的重复，如果【不重复】，就加入边界字符并继续，如果【重复】：1、比较历史最大长度与当前长度；2、把substring中重复字符及它左侧的截去；3、加入边界字符

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        maxLen = 0
        # 移动右指针
        for ch in s:
            if ch in sub:
                # 发现重复 -> 更新最大长度、截去重复字符左侧内容，即移动左指针
                maxLen = max(maxLen, len(sub))
                sub = sub.split(ch)[1]
            # 加入边界字符
            sub += ch
        # sliding 结束之后还要再比较一次
        maxLen = max(maxLen, len(sub))
                
        return maxLen
```



