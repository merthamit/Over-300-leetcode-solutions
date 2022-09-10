class ListNode(object):
    def __init__(self):
        return
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0, head)
        curr = dummy
        
        while curr and curr.next:
            while curr.next and val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return dummy.next
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(None, head)
        curr, prev = head, dummy

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = curr.next
    
        return dummy.next