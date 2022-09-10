# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        currL1, currL2 = l1, l2
        res = 0
        i = 1
        while currL1:
            res += (currL1.val * i)
            currL1 = currL1.next
            i *= 10
        j = 1
        while currL2:
            res += (currL2.val * j)
            currL2 = currL2.next
            j *= 10
        
        res = str(res)
        res = res[::-1]
        firstNode = ListNode(None, None)
        chain = firstNode
        for i in res:
            chain.next = ListNode(i, None)
            chain = chain.next
        
        return firstNode.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            curr = curr.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
        
        return dummy.next
            