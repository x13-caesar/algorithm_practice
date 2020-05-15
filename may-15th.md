# May 15th

## 722. Remove Comments

{% embed url="https://leetcode.com/problems/remove-comments/" %}

好无聊的问题，本来想不用re，但写得好麻烦。再一想最多就100\*80个字符，直接join之后re解决了。

```python
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        withNull = re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')
        return [x for x in withNull if x != '']
```

## 702. **Concatenated String with Uncommon Characters of Two Strings**

{% embed url="https://www.lintcode.com/problem/concatenated-string-with-uncommon-characters-of-two-strings/" %}

最后的结果是：s1+s2，但去掉了所有一开始的共用字符

直接遍历s2的字符，从s1/s2里面删掉，再拼结果。

遍历s1其实也一样。

```python
class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """
    def concatenetedString(self, s1, s2):
        for char in s2:
            if char in s1:
                s1 = s1.replace(char, '')
                s2 = s2.replace(char, '')
        return s1+s2
```

