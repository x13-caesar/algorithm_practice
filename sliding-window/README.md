# Sliding Window

when sliding window: 在长的数据里找短的，一般基于string/list of number/tuple，研究主字符串和子字符串的关系，子字符串可能会直接给出确定的（anagram/palindrome），也可能不会（另给出一个需要满足的条件）。

要求的时间复杂度往往是O\(n\)，空间复杂度往往是常数级的。之所以是滑动窗口，是因为，遍历的时候，两个指针一前一后夹着的子串（子数组）类似一个窗口，这个窗口大小和范围会随着前后指针的移动发生变化。

两种方法：

1. 同向双指针： 左指针移动条件、停止移动条件、左右指针移动时维护对象的变化、记录结果条件、是否滑动整个主串

* 窗口大小不变：[https://leetcode.com/problems/find-all-anagrams-in-a-string/](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
* 窗口大小可变：
  * [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
  * [https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

1. 特定数据结构

