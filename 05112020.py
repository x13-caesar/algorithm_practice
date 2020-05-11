'''
May 11 2020
author: Qiangwen Xu
'''

# 189. Rotate Array
# solution 1:
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            s = nums.pop(-1)
            nums.insert(0, s)

# solution 2:



# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_count = 0
        repeat = []
        while s:
            if s[0] in repeat:
                pass
            elif s.count(s[0]) > 1:
                repeat.append(s[0])
            else:
                return index_count
            s = s[1:]
            index_count += 1
        return -1


