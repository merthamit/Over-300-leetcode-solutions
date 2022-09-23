# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        
        curr = oddptr = head
        evenptr = evenhead = head.next
        i = 1
        
        while curr:
            if i > 2 and i % 2 != 0:
                oddptr.next = curr
                oddptr = oddptr.next
            elif i > 2 and i % 2 == 0:
                evenptr.next = curr
                evenptr = evenptr.next
            
            curr = curr.next
            i += 1
        
        evenptr.next = None
        oddptr.next = evenhead
        
        return head