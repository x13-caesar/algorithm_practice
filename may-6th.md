# May 6th

## 26. Remove Duplicates from Sorted Array

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 1
        f = 0
        while f < len(nums)-1:
            if nums[f] != nums[f+1]:
                nums[s] = nums[f+1]
                s += 1
            f += 1
        return s
```

## 151. Reverse Words in a String

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words=[x for x in s.split(' ') if x != '']
        new_str = ''
        for n in range(len(words)):
            new_str += words[len(words)-n-1]
            if n != len(words)-1:
                new_str += ' '
        return new_str
```

## 75. Sort Colors

```python
# python solution 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            for j in range(len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
# python solution 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)-1
        n = 0
        while n <= r:
            if nums[n] == 0:
                nums[n], nums[l] = nums[l], nums[n]
                print(nums)
                l += 1
            elif nums[n] == 2:
                nums[n], nums[r] = nums[r], nums[n]
                print(nums)
                r -= 1
                n -= 1
            n += 1
```



