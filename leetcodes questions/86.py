# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        left = ltail = ListNode()
        right = rtail = ListNode()
        curr = head
        
        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            
            head = head.next
        
        ltail.next = right.next
        rtail.next = None   
        
        return left.next
        
        