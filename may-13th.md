# May 13th

## 1410. Matrix Water Injection

Basically, use BFS to solve it.

1. Start from \(R,C\), explore all four neighbor points, 
2. add the unvisited ones into applicants, 
3. test height of points in applicants, add the ones which lower than current point into frontiers, 
4. test points in frontiers, if any one is in borders,  return "YES", 
5. otherwise, go on exploring the points in frontiers.

```python
class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def __init__(self):
        self.record = list() # record the visited points
        
    def waterInjection(self, matrix, R, C):
        start = (R,C)
        if any((R==0, R==len(matrix)-1, C==0, C==len(matrix[0])-1)):
            return "YES"
        self.record.append(start)
        return self.explore(start, matrix)
        
    def explore(self, cur, matrix):
        # current point
        (i, j) = cur 
        # all unvisited neighbors
        applicants = [x for x in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)] if x not in self.record]
        
        frontier = list()
        for p in applicants:
            if matrix[p[0]][p[1]] < matrix[i][j]:
                frontier.append(p)
                
        # test frontiers        
        for p in frontier:
            self.record.append(p)
            # when the water in any border of matrix, it can flow out
            if any((p[0]==0, p[0]==len(matrix)-1, p[1]==0, p[1]==len(matrix[0])-1)):
                return "YES"
                
        # go on exploring        
        for p in frontier:
            result = self.explore(p, matrix)
            if result == "YES":
                return "YES"
        return "NO"
        
```

## 171. Excel Sheet Column Number

进制转换：A（N进制） ==&gt; B（M进制）

* 从大位数到小位数： 每访问一个位数，累计结果都需要 \*N，再加上该位数n本身在M进制的值 例如 ABC：0\*26+1=1 ----&gt; 1\*26+2=28 ----&gt; 28\*26+3=731

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result *= 26
            result += (ord(s[i])-ord('A')+1)
        return result
```

* 从小位数到大位数： 每一位数n都代表 \(n在M进制的值\) \* \(M的n-1次方\)，把每位数代表的值相加 例如 ABC：1\*\(26^2\) + 2\*\(26^1\) + 3\*\(26^0\) = 731

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += (ord(s[i])-ord('A')+1) * (26**(len(s)-1-i))
        return result
```

