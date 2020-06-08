# Sliding Window

{% embed url="https://leetcode.com/tag/sliding-window/" %}

* when sliding window: 在一个长string/list里面找符合条件的substring/sublist
* how: 用双指针标记一个滑动的window来代表当前的子字符串，不断检验子字符串是否符合要求。
* 要求的时间复杂度往往是O\(n\)，空间复杂度往往是常数级的。
* sliding window 很少见easy题目，但不是sliding window本身有多难，基本都是难在变量的维护、指针移动条件的判断等细节，题目变化比较多。

## 要素：

1. 左指针移动条件\[, 停止移动条件\]
2. 记录结果条件

## 模版：

```python
def slidingWindow(A, B=None):
    map = defaultdict(int) # 描述window的hashmap
    res = [] # 记录最终要返回的结果，有时是计数 or sth other
    count = 0 # 条件值：用来维护 {window是否满足要求}
    
    # 有时候可以对主串str或者题目的要求做预处理，通常是算frequency
    
    l, r = 0, 0 # 左右指针，有时寻找的substring长度固定，那就可以只用一个指针（隐式双指针）
    while r < len(A): # 一般是一直移动右指针
        map[A[r]] += 1 # 处理右侧新进字符
        
        # 根据窗口的变更结果来改变条件值
        if (map[A[r]] == ...):
        ...
         
        # 移动左指针的条件（有时是window满足要求就停，有时是不满足要求才停）
        while (count == K):
            if (...):
                res.append(A[l:r+1])
            
            # 处理左边界跳出字符，移动左指针    
            map[A[l]] -= 1
            l += 1
        
        # 移动右指针
        r += 1
     
    return res
```

## 题目整理：

### 窗口大小不变：

{% page-ref page="438.-find-all-anagrams-in-a-string.md" %}

{% page-ref page="567.-permutation-in-string.md" %}

{% page-ref page="1100.-find-k-length-substrings-with-no-repeated-characters.md" %}

### 窗口大小可变：

{% page-ref page="3.-longest-substring-without-repeating-characters.md" %}

{% page-ref page="76.-minimum-window-substring.md" %}

{% page-ref page="159.-longest-substring-with-at-most-two-distinct-characters.md" %}

{% page-ref page="340.-longest-substring-with-at-most-k-distinct-characters.md" %}

{% page-ref page="424.-longest-repeating-character-replacement.md" %}

{% page-ref page="992.-subarrays-with-k-different-integers.md" %}

### 特殊数据结构：

{% page-ref page="239.-sliding-window-maximum.md" %}



