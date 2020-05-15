# Quick Sort & Merge Sort

## 912. Sort an Array

[https://leetcode.com/problems/sort-an-array/](https://leetcode.com/problems/sort-an-array/)

### Bubble sort

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            forj in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
```

### Quick sort 

* 分治法 Divide and conquer
* 三个基本步骤：
  1. 挑选基准值：从数列中挑出一个元素，称为“基准” pivot（方便起见，下面代码里都是挑的当前array第一个元素）
  2. 排序分割： 重新排序数列：比pivot小的元素摆放在pivot前面，所有比pivot大的元素摆在pivot后面（与基准值相等的数可以不动，或者到右边，来尽量保持稳定）。 具体做法：设置两个指针 i, j 都放在最右，j 向左遍历，遇到比 p 大的就放到 i 的位置，然后把 i 往左移动一格（这样再遇到可以继续放）。最后把 p 也放到 i 位置，这样 i 右边 &gt;p 左边 &lt;p，以 i 作为 pivot 位置分割出左右两个子序列。
  3. 递归排序子序列：【递归】地将小于 pivot 元素的子序列和大于 pivot 的子序列进行排序。
* quick sort 的最坏运行情况是 O\(n²\)，比如说顺序数列 quick sort。但它的平摊期望时间是 O\(nlogn\)，且 O\(nlogn\) 记号中隐含的常数因子很小，比复杂度稳定等于 O\(nlogn\) 的 merge sort 要小很多。所以，对绝大多数顺序性较弱的随机数列而言，quick sort 总是优于 merge sort.

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return nums if len(nums) <= 1 else self.sortArray([item for item in nums[1:] if item <= nums[0]]) + [nums[0]] + self.sortArray([item for item in nums[1:] if item > nums[0]])
```

```python
class Solution:
    def quickSort(self, array, l, r):
        if l < r: # 长度小于等于1就不需要排序，直接结束
            # 获取排序后pivot位置q
            q = self.partition(array, l, r)
            # 根据 q 分割两个sub-array，继续排序
            self.quickSort(array, l, q - 1)
            self.quickSort(array, q + 1, r)

    def partition(self, array, l, r):
        x = array[l] # 取当前第一个值作为 pivot value
        i = r # i指针放到最右边
        for j in range(r, l, -1):
            # 从右向左遍历，发现比 pivot 大的，就放到左边（i指针）去
            if array[j] >= x:
                array[i], array[j] = array[j], array[i]
                i -= 1 # 每放一个元素到i位置，就把i向左再移动一格
        # 最后把 pivot 元素也放到 i 位置，这样所有比 pivot 小的元素就都在左边，比它大的在右边
        array[i], array[l] = array[l], array[i]
        return i

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        left = 0
        right = len(nums)-1
        self.quickSort(nums, left, right)
        return nums
```

### Merge sort:

* 从上往下递归

![](.gitbook/assets/image%20%281%29.png)

```python
class Solution:
    def merge(self, left,right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        del left, right
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums)<=1):
            return nums
        mid = int(len(nums)/2)
        left, right = nums[0:mid], nums[mid:]
        return self.merge(self.sortArray(left), self.sortArray(right))
```

* 从下往上迭代

非递归的方法只需要在merge过程中占用最大为n的空间，避免了递归时深度为log2n的栈空间，并且在时间性能上也有一定的提升，因此，使用归并排序是，尽量考虑用非递归的方法。

merge 方法与递归没有区别。

```python
class Solution:
    def merge(self, left, right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        del left, right
        return result

    def sortArray(self, nums: List[int]) -> List[int]:
        step = 1 # 初始步长，也可以从2开始
        while step < len(nums):
            # 每次 merge 两个跟步长等长的 sub array，所以是跳 2*step
            for l in range(0, len(nums), 2*step): 
                r = min(l+2*step,len(nums))
                nums[l:r] = self.merge(nums[l:l+step], nums[l+step:r])
            step *= 2
        return nums
```

## 215. Kth Largest Element in an Array

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums, reverse=True)
        kth = float("-inf")
        n = 0
        while n < k:
            if sortedNums[n] != kth:
                kth = sortedNums[n]
            n += 1
        return kth
```

