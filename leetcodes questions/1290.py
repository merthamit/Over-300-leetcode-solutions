# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def getDecimalValue(self, head):
        curr = head
        res = 0

        while curr:
            res = res * 2 + curr.val
            curr = curr.next
        
        return res