# May 26th

## 535. Encode and Decode TinyURL

{% embed url="https://leetcode.com/problems/encode-and-decode-tinyurl/" %}

偷懒用了hash\(\)，自己写letter+digit的随机抽取，可以固定长度+增加最大容量，懒得写了这里...

```python
class Codec:
    def __init__(self):
        self.map_ = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.map_[hash(longUrl)] = longUrl
        return "http://tinyurl.com/" + str(hash(longUrl))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map_[int(shortUrl.lstrip("http://tinyurl.com/"))]
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

## 89. Gray Code

{% embed url="https://leetcode.com/problems/gray-code/submissions/" %}

原来是需要借助 gray code 的一些性质，参考[维基百科](https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%9B%B7%E7%A0%81)：n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的方式快速的得到，如下图所示一般。

![](.gitbook/assets/image%20%282%29.png)

其实就是把 \(n-1\) 位的gray code逆序，前面加个1（换成十进制来看就是加了2^\(n-1\)）。

```python
class Solution:
    def grayCode(self, n):
        if n == 0: return [0]
        else:
            res = self.grayCode(n - 1)
            for i in range(len(res) - 1, -1, -1):
                res.append((2 ** (n - 1)) + res[i])
            return res
```

