# 1300. Sum of Mutated Array Closest to Target

{% embed url="https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/" %}

要把数组中所有大于value的数替换成value，肯定是先`sort`，左边元素不用变，直接求和，右边全部算value，加总跟target比较，即可获得距离`diff`。如果直接`sort`然后`二分法`做，可以把结果定位到`arr`中的某个元素值。但题目要求：

> Notice that the answer is not necessarily a number from `arr`

这样就没法直接对`arr`做二分法来找结果，还是得从0到max\(arr\)遍历过去，找 threshold value，而不是element of arr。借助`bisect`可以确定具体值在`sorted arr`中的位置，然后分别计算左右部分来跟target比较。

每次都重新对左边求和，造成很多重复运算，可以直接预先遍历一次，记录`pre_sum`，优化时间到O\(nlogn\)。

```python
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        pre_sum, left_sum = 0, [0]
        for v in arr:
            pre_sum += v
            left_sum.append(pre_sum)
            
        diff, res = float('inf'), 0
        for i in range(arr[-1]+1):
            idx = bisect.bisect_right(arr, i)
            after_sum = left_sum[idx] + i * (n-idx)
            if abs(after_sum-target) < diff:
                diff = abs(after_sum-target)
                res = i
                
        return res
```

