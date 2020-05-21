# May 21th

## 1332. Number of 1 Bits

{% embed url="https://www.lintcode.com/problem/number-of-1-bits/" %}

偷懒暴力count

```python
class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        return str(bin(n)).count('1')
```

follow-up: 如果是个类似 10110000000000 这样的数字，最后一个1之后的digits其实就不需要遍历，可以改善平均时间复杂度。

```python
class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        bi = bin(n)[2:]
        res = 0;
        idx = 0
        while (int(bi) != 0) and idx <= len(bi)-1:
            if bi[idx] == '1':
                res += 1;
                # 把当前的1计算进去之后，就把它改成0，这样等所有1都算完，bi=0
                bi[idx] == 0
            idx += 1
        return res
```

## 844. Number Pair Statistics

{% embed url="https://www.lintcode.com/problem/number-pair-statistics/description" %}

想拿类似上面一道的方法做的，结果列表一长就 time limit exceeded 了。此时时间复杂度应该是O\(n^2\)，要想办法降到O\(n\)，也就只能遍历p一遍，在遍历完之后再match pairs。

研究下 有效解 和 p.x/p.y 性质之间的关系，要符合要求，p1/p2只能是以下组合：

1. 都是 \(even, even\)
2. 都是 \(even, odd\)
3. 都是 \(odd, odd\)
4. 都是 \(odd, even\)

像 \(even, odd\) 和 \(even, even\) 这种组合不管怎样都没法满足题设。

所以我们在 1/2/3/4 这四个 group 内部计算 &lt;可能的 pair 数量&gt; 就可以，这个数量也只和 group 的点个数 n 有关，所以遍历 p 的时候累计出四个 group 的 n 就行，最后时间复杂度 O\(n\).

```python
class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):
        # Write your code here
        evenEven, evenOdd, oddOdd, oddEven = 0,0,0,0
        for d in p:
            if d.x%2==0:
                if d.y%2==0:
                    evenEven += 1
                else:
                    evenOdd += 1
            else:
                if d.y%2==0:
                    oddEven += 1
                else:
                    oddOdd += 1 
        
        res = 0
        for n in [evenEven, evenOdd, oddOdd, oddEven]:
            res += (n*(n-1)/2)
            
        return int(res)
```

beats 100.00% Submissions 美滋滋

