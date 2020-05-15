# May 14th

## 125. Valid Palindrome

{% embed url="https://leetcode.com/problems/valid-palindrome/" %}

思路一：相向双指针

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            left = s[i].lower()
            if not (left.isalpha() or left.isdigit()):
                i += 1
                continue
            else:
                right = s[j].lower()
                if not (right.isalpha() or right.isdigit()):
                    j -= 1
                    continue
                else:
                    if left != right:
                        return False
                    else:
                        i += 1
                        j -= 1
        return True
```

思路二：粗暴点，去除无效字符后，全部小写，从中心切割，把右边逆序，再对比

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = [x.lower() for x in s if (x.isalpha() or x.isdigit())]
        mid = len(valid)//2
        left = valid[:mid]
        right = valid[len(valid)-mid:]
        right.reverse()
        if left == right:
            return True
        else:
            return False
```

## 409. Longest Palindrome

{% embed url="https://leetcode.com/problems/longest-palindrome/submissions/" %}

1. 统计字符出现次数然后进行遍历
2. 偶数字符直接加上，奇数字符的话，我们取出其最大偶数，
3. 有遇到过奇数字符，就需要在结果加1，但只能加最多一次，如果结果已经是奇数就代表加过了，不需要再加。

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        count = collections.Counter(s)
        for i in count.values():
            if i % 2 == 0:
                length += i
            else: 
                if (length % 2 == 0):
                    length += 1
                length += (i-1)
        return length
```



