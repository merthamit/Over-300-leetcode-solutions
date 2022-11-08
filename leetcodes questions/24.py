# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head: return head
        
        listhead = dummy = ListNode(0, head)
        curr = head
        while curr and curr.next:
            nxt = curr.next
            curr.next = nxt.next
            dummy.next = nxt
            dummy.next.next = curr
            
            dummy = curr
            curr = curr.next
        return listhead.next

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def swapPairs(self, head):
        if not head: return head
        
        dummy = ListNode(0, head)
        curr, prev = head, dummy
        while curr and curr.next:
            nxtPairs = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nxtPairs
            prev.next = second
            
            prev = curr
            curr = nxtPairs
            
        return dummy.next
                
                
                