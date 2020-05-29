# May 29th

## 819. Most Common Word

{% embed url="https://leetcode.com/problems/most-common-word/" %}

顺带实验了几种不同的去标点方法，发现的确是translate显著地快，虽然代码有点不直观。

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 创建个 translate table, 所有 punctutaion 都替换为空格
        remove_punct_map = dict.fromkeys(map(ord, string.punctuation), ' ')
        freq = Counter([x for x in paragraph.translate(remove_punct_map).lower().split(' ')])
        rank = sorted(freq.items(), key = lambda item:item[1], reverse=True)
        for w in rank:
            if w[0] not in banned and w[0].isalpha():
                return w[0]
```

## 414. Third Maximum Number

{% embed url="https://leetcode.com/problems/third-maximum-number/" %}

要求时间复杂度O\(n\)，只能遍历一次。

遍历的同时维护top3最大值即可，因为有重复数字，所以用list会很麻烦，直接利用set维护。

```python
class Solution:
    def __init__(self):
        self.max_ = set()
        
    def thirdMax(self, nums: List[int]) -> int:    
        for n in nums:
            self.max_.add(n)
            if len(self.max_)>3:
                self.max_.remove(min(self.max_))
        return min(self.max_) if len(self.max_) == 3 else max(self.max_)
```



