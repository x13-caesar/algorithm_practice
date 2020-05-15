# May 5th

## 138. Copy List with Random Pointer

Iterate the linked list twice: 

1. first round copying the node value, and mapping the original node to new generated node. 
2. second round assigning the random pointer in new linked list by hash map.

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        # 建立一个值为 0 的新 node，它的 next 和 random 都是 None
        copy = Node(0)
        # 将 curNode 指针放在 copy 当前位置 i.e 0
        curNode = copy
        # 用来临时存储随即指针的 hash map
        randomPointerMap = {}

        # 遍历原始链表，拷贝每个 node 的值，记录随机指针到 hash map
        while head is not None:
            # 根据原始链表生成下一个新节点（有值，但next和random都是None）
            newNode = Node(head.val)
            # 把新节点接到当前节点后面
            curNode.next = newNode
            # 把原始链表上的节点map到新链表上的对应节点
            randomPointerMap[head] = newNode
            # 从原始链表上拷贝随机指针
            newNode.random = head.random
            # 移动指针到下一个node
            head = head.next
            curNode = curNode.next

        # 遍历新链表，设置随机指针
        # 重新把curNode指针挪到对应位置（copy还在Node(0)，所以是下一个）
        curNode = copy.next
        while curNode is not None:
            if curNode.random is not None:
                # 从hash-map里面找随机指针应该指向的对应新node
                curNode.random = randomPointerMap[curNode.random]
            curNode = curNode.next
        
        return copy.next
```

## 273. Integer to English Words

```python
# python solution 1

belowTwenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def convert(num: int):
    if (num < 20):
        result = belowTwenty[num];
    elif (num < 100):
        result = belowHundred[num//10] 
        result = result if (num%10 == 0) else (result + " " + convert(num%10))
    elif (num < 1000):
        result = convert(num//100) + " Hundred"
        result = result if (num%100 == 0) else (result + " " + convert(num%100))
    elif (num < 1000000):
        result = convert(num//1000) + " Thousand"
        result = result if (num%1000 == 0) else (result + " " + convert(num%1000))
    elif (num < 1000000000):
        result = convert(num//1000000) + " Million"
        result = result if num%1000000 == 0 else result + " " + convert(num%1000000)
    elif (num >= 1000000000):
        result = convert(num//1000000000) + " Billion"
        result = result if num%1000000000 == 0 else result + " " + convert(num%1000000000)
    return result

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        else:
            return convert(num).strip()
```



