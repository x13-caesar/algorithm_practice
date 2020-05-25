# May 25th

## 762. Prime Number of Set Bits in Binary Representation

{% embed url="https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/" %}

难道就是考我判断质数...？

```python
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def isPrime(n) : 
            if (n <= 1) : return False
            if (n <= 3) : return True
            if (n % 2 == 0 or n % 3 == 0) : return False
            i = 5
            while(i * i <= n) : 
                if (n % i == 0 or n % (i + 2) == 0) : return False
                i = i + 6
            return True
        
        res = 0
        for N in range(L, R+1):
            if isPrime(bin(N).count("1")): res += 1
        return res
```

## 1380. Log Sorting

{% embed url="https://www.lintcode.com/problem/log-sorting/description" %}

定制rule的sorting，跟排序dict的原理一样

```python
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        def rules(log):
            _id, content = log.split(" ", 1)
            # 返回的两个 tuple 分别以 0/1 开头，为了把letter content放在前面
            # content 一样的话，就会往后看key，i.e. 排_id
            return (0, content, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key = rules)
```

