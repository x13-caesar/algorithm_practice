# 1268. Search Suggestions System

{% embed url="https://leetcode.com/problems/search-suggestions-system/" %}

数据规模不大，暴力遍历也就1000\*1000，完全可以接受

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        for i in range(len(searchWord)):
            res.append(sorted([word for word in products if len(word) > i and word[:i+1] == searchWord[:i+1]])[:3])
        return res
```

